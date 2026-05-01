#!/usr/bin/env python3
"""Activate a task in safe mode for Milestone 11 MVP."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


EXPECTED_SCOPE = "activate_task"
EXPECTED_TRANSITION = "approved_for_execution:active"


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def strip_quotes(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and ((text[0] == text[-1] == '"') or (text[0] == text[-1] == "'")):
        return text[1:-1]
    return text


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}

    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return result
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = strip_quotes(value)
    return {}


def parse_iso_datetime(value: str) -> datetime | None:
    text = value.strip()
    if not text:
        return None
    if text.endswith("Z"):
        text = text[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(text)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def fail(reason: str) -> int:
    print("ACTIVATION FAIL")
    print(f"Reason: {reason}")
    print("No files changed.")
    return 1


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Safely activate a task (approved_for_execution -> active)."
    )
    parser.add_argument("task_path", nargs="?")
    parser.add_argument("--approval", required=True, help="Path to approval marker")
    parser.add_argument("--dry-run", action="store_true", help="Run checks only")
    parser.add_argument("--approved", action="store_true", help="Allow write after all checks")
    return parser.parse_args(argv)


def run_script(script: Path, repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(script), *args],
        cwd=str(repo_root),
        capture_output=True,
        text=True,
    )


def load_active_task_id(active_task_path: Path) -> tuple[str | None, str | None]:
    if not active_task_path.exists():
        return None, None
    try:
        text = active_task_path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, f"cannot read existing active-task.md: {exc}"
    frontmatter = parse_frontmatter(text)
    existing = frontmatter.get("task_id", "").strip()
    if not existing:
        return None, "existing active-task.md has no task_id"
    return existing, None


def write_active_task_atomic(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=str(path.parent),
        delete=False,
        prefix=".active-task.",
        suffix=".tmp",
    ) as tmp:
        tmp.write(content)
        tmp_path = Path(tmp.name)
    os.replace(tmp_path, path)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if not args.task_path:
        return fail("task_path is required")

    # 0. Validate CLI mode before all other checks.
    if args.dry_run == args.approved:
        return fail("exactly one of --dry-run or --approved is required")

    script_path = Path(__file__).resolve()
    repo_root = script_path.parent.parent

    task_input = args.task_path
    approval_input = args.approval

    task_path = Path(task_input)
    if not task_path.is_absolute():
        task_path = repo_root / task_path
    task_path = task_path.resolve()

    approval_path = Path(approval_input)
    if not approval_path.is_absolute():
        approval_path = repo_root / approval_path
    approval_path = approval_path.resolve()

    detect_script = repo_root / "scripts" / "detect-task-state.py"
    validate_state_script = repo_root / "scripts" / "validate-task-state.py"
    check_transition_script = repo_root / "scripts" / "check-transition.py"
    validate_approval_script = repo_root / "scripts" / "validate-approval-marker.py"
    active_task_path = repo_root / "tasks" / "active-task.md"

    # 1. task_path exists
    if not task_path.exists():
        return fail(f"task path does not exist: {task_input}")

    # 2. approval path exists
    if not approval_path.exists():
        return fail(f"approval path does not exist: {approval_input}")

    # 3. call detect-task-state.py
    detect_run = run_script(detect_script, repo_root, [str(task_path)])
    if detect_run.returncode != 0:
        return fail(f"detect-task-state.py failed with exit code {detect_run.returncode}")

    # 4. parse detect-task-state.py JSON output
    try:
        detect_data = json.loads(detect_run.stdout)
    except json.JSONDecodeError:
        return fail("detect-task-state.py returned invalid JSON")

    task_id = str(detect_data.get("task_id", "")).strip()
    if not task_id:
        return fail("detect-task-state.py output is missing task_id")

    # 5. call validate-task-state.py
    validate_state_run = run_script(validate_state_script, repo_root, [str(task_path)])
    if validate_state_run.returncode != 0:
        return fail(f"validate-task-state.py failed with exit code {validate_state_run.returncode}")

    # 6. call check-transition.py --to active
    transition_run = run_script(check_transition_script, repo_root, [str(task_path), "--to", "active"])
    if transition_run.returncode != 0:
        return fail(f"check-transition.py failed with exit code {transition_run.returncode}")

    # 7. call validate-approval-marker.py with expected scope/transition
    approval_run = run_script(
        validate_approval_script,
        repo_root,
        [
            str(approval_path),
            "--task",
            task_id,
            "--scope",
            EXPECTED_SCOPE,
            "--transition",
            EXPECTED_TRANSITION,
        ],
    )
    if approval_run.returncode != 0:
        return fail(f"validate-approval-marker.py failed with exit code {approval_run.returncode}")

    # 8. parse approval marker frontmatter
    try:
        approval_text = approval_path.read_text(encoding="utf-8")
    except OSError as exc:
        return fail(f"cannot read approval marker: {exc}")
    marker = parse_frontmatter(approval_text)
    if not marker:
        return fail("approval marker frontmatter is missing or invalid")

    # 9. verify approval marker task_id matches requested task
    marker_task_id = marker.get("task_id", "").strip()
    if marker_task_id != task_id:
        return fail("approval marker task_id does not match requested task")

    # 10. verify approval marker scope == activate_task
    marker_scope = marker.get("scope", "").strip()
    if marker_scope != EXPECTED_SCOPE:
        return fail("approval marker scope must be activate_task")

    # 11. verify transition if exists
    marker_transition = marker.get("transition", "").strip()
    if marker_transition and marker_transition != EXPECTED_TRANSITION:
        return fail("approval marker transition does not match approved_for_execution:active")

    # 12. verify status == approved
    marker_status = marker.get("status", "").strip()
    if marker_status != "approved":
        return fail("approval marker status must be approved")

    # 13. verify marker is not revoked
    if marker.get("revoked_at", "").strip() or marker.get("revoked_by", "").strip():
        return fail("approval marker is revoked")

    # 14. verify marker is not expired
    expires_at = marker.get("expires_at", "").strip()
    if expires_at:
        parsed_expires = parse_iso_datetime(expires_at)
        if parsed_expires is None:
            return fail("approval marker expires_at is not a valid datetime")
        if parsed_expires <= datetime.now(timezone.utc):
            return fail("approval marker is expired")

    # 15. verify no state_conflict
    analysis_status = str(detect_data.get("analysis_status", "")).strip()
    if analysis_status == "conflict":
        return fail("analysis_status conflict blocks activation")

    # 16. verify analysis_status != invalid
    if analysis_status == "invalid":
        return fail("analysis_status invalid blocks activation")

    # 17. verify source contract exists if declared
    source_contract = marker.get("related_contract", "").strip()
    if source_contract:
        contract_path = Path(source_contract)
        if not contract_path.is_absolute():
            contract_path = repo_root / contract_path
        if not contract_path.exists():
            return fail("related_contract declared in approval marker does not exist")

    # Optional guard from detect JSON.
    allowed_next_states = detect_data.get("allowed_next_states")
    if isinstance(allowed_next_states, list) and "active" not in allowed_next_states:
        return fail("detect-task-state.py does not allow transition to active")

    # 18. verify active-task.md write target is safe
    existing_active_task_id, active_task_error = load_active_task_id(active_task_path)
    if active_task_error:
        return fail(active_task_error)
    if existing_active_task_id and existing_active_task_id != task_id:
        return fail(
            f"active-task.md already references a different task: {existing_active_task_id}"
        )

    # 19. dry-run mode: no write
    if args.dry_run:
        print("ACTIVATION DRY-RUN PASS")
        print("No files changed.")
        return 0

    # 20. approved mode: write tasks/active-task.md
    approval_id = marker.get("approval_id", "").strip()
    activated_at = now_utc_iso()

    content = (
        "---\n"
        f"task_id: {task_id}\n"
        "state: active\n"
        f"activated_at: {activated_at}\n"
        "activated_by: human-approved-command\n"
        f"approval_id: {approval_id}\n"
        f"source_task: {task_input}\n"
        f"source_contract: {source_contract}\n"
        f"transition: {EXPECTED_TRANSITION}\n"
        "---\n"
        "# Active Task\n\n"
        "This task was activated by a human-approved AgentOS command.\n\n"
        f"Source task: {task_input}\n"
        f"Approval marker: {approval_input}\n"
        f"Transition: {EXPECTED_TRANSITION}\n"
    )

    try:
        write_active_task_atomic(active_task_path, content)
    except OSError as exc:
        return fail(f"cannot write active-task.md: {exc}")

    print("ACTIVATION PASS")
    print("Updated: tasks/active-task.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
