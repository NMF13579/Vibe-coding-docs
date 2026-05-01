#!/usr/bin/env python3
"""Execution Readiness checker MVP (read-only)."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from lib.path_utils import resolve_task_dir


ACTIVE_COMPATIBLE_STATES = {"active", "approved_for_execution"}


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check if active task is execution-ready (read-only)."
    )
    parser.add_argument(
        "--active-task",
        default="tasks/active-task.md",
        help="Path to active task pointer file (default: tasks/active-task.md)",
    )
    parser.add_argument(
        "--approval-dir",
        default="approvals",
        help="Approval marker directory (default: approvals, repository-relative only)",
    )
    return parser.parse_args(argv)


def read_text(path: Path) -> tuple[str | None, str | None]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, str(exc)


def parse_frontmatter(text: str) -> tuple[dict[str, str] | None, str | None]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "missing YAML frontmatter"

    frontmatter: dict[str, str] = {}
    end_index = None
    for idx, line in enumerate(lines[1:], start=1):
        stripped = line.strip()
        if stripped == "---":
            end_index = idx
            break
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in line:
            return None, f"malformed frontmatter line: {line}"
        key, value = line.split(":", 1)
        frontmatter[key.strip()] = value.strip().strip("'\"")

    if end_index is None:
        return None, "missing YAML frontmatter terminator"
    return frontmatter, None


def run_subprocess(repo_root: Path, command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=str(repo_root), capture_output=True, text=True)


def is_repo_relative_safe(path_text: str) -> bool:
    if not path_text.strip():
        return False
    path = Path(path_text)
    if path.is_absolute():
        return False
    return ".." not in path.parts


def extract_first_status(output: str, prefix: str) -> str | None:
    for line in output.splitlines():
        line = line.strip()
        if line.startswith(prefix):
            return line.removeprefix(prefix).strip()
    return None


def parse_iso(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None
    if raw.endswith("Z"):
        raw = raw[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(raw)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return None
    return dt.astimezone(timezone.utc)


def detect_analysis_status(
    source_contract_fm: dict[str, str] | None,
    detect_json: dict | None,
    state_file_path: Path,
) -> tuple[str | None, list[str]]:
    notes: list[str] = []
    if source_contract_fm and source_contract_fm.get("analysis_status", "").strip():
        return source_contract_fm.get("analysis_status", "").strip(), notes

    if isinstance(detect_json, dict):
        val = str(detect_json.get("analysis_status", "")).strip()
        if val:
            return val, notes

    if state_file_path.is_file():
        text, err = read_text(state_file_path)
        if err is None and text is not None:
            match = re.search(r"(?im)^\s*analysis_status\s*:\s*([A-Za-z_]+)\s*$", text)
            if match:
                return match.group(1).strip(), notes

    notes.append("analysis_status check: NOT PRESENT")
    notes.append("analysis_status requiredness: UNKNOWN")
    return None, notes


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    failures: list[str] = []
    partials: list[str] = []
    checked: list[tuple[str, str]] = []
    notes: list[str] = []

    active_task_path = Path(args.active_task)
    if not active_task_path.is_absolute():
        active_task_path = repo_root / active_task_path
    if not is_repo_relative_safe(args.approval_dir):
        print("Execution Readiness: FAIL")
        print("Failures:")
        print("- approval-dir must be repository-relative without parent traversal")
        print("Exit: 1")
        return 1
    approval_dir = repo_root / args.approval_dir

    validate_active_script = repo_root / "scripts" / "validate-active-task.py"
    if not validate_active_script.is_file():
        partials.extend(
            [
                "scripts/validate-active-task.py missing",
                "active task prerequisite gate could not be executed",
            ]
        )
        print("Execution Readiness: PARTIAL")
        print("Failures:")
        for item in partials:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    # Prerequisite gate
    prerequisite = run_subprocess(
        repo_root,
        [sys.executable, str(validate_active_script), "--active-task", args.active_task],
    )
    prerequisite_out = (prerequisite.stdout or "") + (prerequisite.stderr or "")
    prereq_status = extract_first_status(prerequisite_out, "Active Task Validation:")
    if prereq_status != "PASS" or prerequisite.returncode != 0:
        failures.append(
            "active task validation prerequisite failed "
            f'(status={prereq_status or "UNKNOWN"}, exit={prerequisite.returncode})'
        )
        print("Execution Readiness: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1
    checked.append(("active task validation", "PASS"))
    checked.append(("active task validation exact PASS (not PARTIAL)", "PASS"))

    active_text, err = read_text(active_task_path)
    if err or active_text is None:
        failures.append(f"cannot read active-task.md: {err}")
        print("Execution Readiness: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1
    active_fm, fm_err = parse_frontmatter(active_text)
    if fm_err or active_fm is None:
        failures.append(f"active-task frontmatter parse error: {fm_err}")
        print("Execution Readiness: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    active_task_id = active_fm.get("task_id", "").strip()
    source_task_rel = active_fm.get("source_task", "").strip()
    source_contract_rel = active_fm.get("source_contract", "").strip()
    approval_id = active_fm.get("approval_id", "").strip()

    source_task_path = repo_root / source_task_rel
    source_task_detect_path = resolve_task_dir(source_task_path)
    source_contract_path = repo_root / source_contract_rel
    source_task_ok = source_task_path.is_file()
    source_contract_ok = source_contract_path.is_file()
    checked.append(("source_task exists and consistent", "PASS" if source_task_ok else "FAIL"))
    checked.append(
        ("source_contract exists and consistent", "PASS" if source_contract_ok else "FAIL")
    )
    if not source_task_ok:
        failures.append(f"source_task missing: {source_task_rel}")
    if not source_contract_ok:
        failures.append(f"source_contract missing: {source_contract_rel}")

    # Approval marker resolution
    approval_path = approval_dir / f"{approval_id}.md"
    if not approval_id:
        failures.append("approval_id missing in active-task.md")
        checked.append(("approval marker resolved", "FAIL"))
    elif not approval_path.is_file():
        failures.append(
            f"approval marker unresolved: {args.approval_dir}/{approval_id}.md not found"
        )
        checked.append(("approval marker resolved", "FAIL"))
    else:
        checked.append(("approval marker resolved", "PASS"))

    approval_fm: dict[str, str] | None = None
    if approval_path.is_file():
        approval_text, approval_err = read_text(approval_path)
        if approval_err or approval_text is None:
            failures.append(f"cannot read approval marker: {approval_err}")
        else:
            approval_fm, approval_parse_err = parse_frontmatter(approval_text)
            if approval_parse_err or approval_fm is None:
                failures.append(f"approval marker malformed: {approval_parse_err}")

    # approval validation (dedicated validator first)
    approval_validator = repo_root / "scripts" / "validate-approval-marker.py"
    approval_valid_status = "FAIL"
    if approval_path.is_file() and approval_fm is not None:
        if approval_validator.is_file():
            run = run_subprocess(
                repo_root,
                [
                    sys.executable,
                    str(approval_validator),
                    str(approval_path),
                    "--task",
                    active_task_id,
                    "--scope",
                    "activate_task",
                    "--transition",
                    "approved_for_execution:active",
                ],
            )
            if run.returncode != 0:
                failures.append("approval marker validator returned non-zero")
            else:
                approval_valid_status = "PASS"
        else:
            # Direct checks fallback (MVP)
            notes.append(
                "approval marker direct validation used: scripts/validate-approval-marker.py unavailable"
            )
            required = ["task_id", "scope", "transition", "status"]
            unreliable = any(not approval_fm.get(k, "").strip() for k in required)
            if unreliable:
                partials.extend(
                    [
                        "scripts/validate-approval-marker.py missing",
                        "approval marker direct checks could not be performed reliably",
                    ]
                )
            else:
                marker_task = approval_fm.get("task_id", "").strip()
                marker_scope = approval_fm.get("scope", "").strip()
                marker_transition = approval_fm.get("transition", "").strip()
                marker_status = approval_fm.get("status", "").strip().lower()

                if marker_task != active_task_id:
                    failures.append("approval marker task_id mismatch")
                if marker_scope != "activate_task":
                    failures.append("approval marker scope mismatch")
                if marker_transition != "approved_for_execution:active":
                    failures.append("approval marker transition mismatch")
                if marker_status == "revoked":
                    failures.append("approval marker is revoked")
                if approval_fm.get("revoked_at", "").strip() or approval_fm.get("revoked_by", "").strip():
                    failures.append("approval marker is revoked")
                expires_at = approval_fm.get("expires_at", "").strip()
                if expires_at:
                    parsed = parse_iso(expires_at)
                    if parsed is None:
                        failures.append("approval marker expires_at malformed")
                    elif parsed <= datetime.now(timezone.utc):
                        failures.append("approval marker is expired")

                if not failures:
                    approval_valid_status = "PASS_WITH_LIMITATIONS"
                    notes.append(
                        "PASS_WITH_LIMITATIONS: MVP direct checks passed, dedicated approval validator was not used"
                    )

    checked.append(("approval marker valid", approval_valid_status))
    checked.append(
        (
            "approval marker task_id match",
            "PASS"
            if approval_fm and approval_fm.get("task_id", "").strip() == active_task_id
            else "FAIL",
        )
    )
    checked.append(
        (
            "approval marker scope match",
            "PASS"
            if approval_fm and approval_fm.get("scope", "").strip() == "activate_task"
            else "FAIL",
        )
    )
    checked.append(
        (
            "approval marker transition match",
            "PASS"
            if approval_fm
            and approval_fm.get("transition", "").strip() == "approved_for_execution:active"
            else "FAIL",
        )
    )

    # State checks
    detect_script = repo_root / "scripts" / "detect-task-state.py"
    detect_json: dict | None = None
    if not detect_script.is_file():
        partials.extend(
            [
                "scripts/detect-task-state.py missing",
                "task state could not be fully validated",
            ]
        )
    else:
        detect_run = run_subprocess(
            repo_root, [sys.executable, str(detect_script), str(source_task_detect_path)]
        )
        if detect_run.returncode != 0:
            failures.append("detect-task-state.py returned non-zero")
        else:
            try:
                detect_json = json.loads(detect_run.stdout or "")
            except json.JSONDecodeError:
                partials.extend(
                    [
                        "detect-task-state.py returned non-JSON output",
                        "task state could not be determined",
                    ]
                )

    if isinstance(detect_json, dict):
        detected_state = str(detect_json.get("state", "")).strip()
        if detected_state in ACTIVE_COMPATIBLE_STATES:
            checked.append(("task state compatible", "PASS"))
        elif detected_state:
            checked.append(("task state compatible", "FAIL"))
            failures.append(f"detected state is not active-compatible: {detected_state}")
        else:
            checked.append(("task state compatible", "FAIL"))
            failures.append("detected state missing in detector output")
    else:
        checked.append(("task state compatible", "PARTIAL"))

    validate_state_script = repo_root / "scripts" / "validate-task-state.py"
    if not validate_state_script.is_file():
        partials.extend(
            [
                "scripts/validate-task-state.py missing",
                "task state could not be fully validated",
            ]
        )
        checked.append(("validate-task-state", "PARTIAL"))
    else:
        run = run_subprocess(
            repo_root, [sys.executable, str(validate_state_script), str(source_task_detect_path)]
        )
        if run.returncode == 0:
            checked.append(("validate-task-state", "PASS"))
        else:
            checked.append(("validate-task-state", "FAIL"))
            failures.append("validate-task-state.py returned non-zero")

    # analysis_status chain
    source_contract_fm: dict[str, str] | None = None
    if source_contract_ok:
        source_contract_text, serr = read_text(source_contract_path)
        if serr is None and source_contract_text is not None:
            parsed, _ = parse_frontmatter(source_contract_text)
            source_contract_fm = parsed

    state_file_path = repo_root / "tasks" / active_task_id / "state.md"
    analysis_status, analysis_notes = detect_analysis_status(
        source_contract_fm, detect_json, state_file_path
    )
    notes.extend(analysis_notes)
    if analysis_status is None:
        checked.append(("analysis_status", "NOT PRESENT"))
    elif analysis_status == "invalid":
        checked.append(("analysis_status", "FAIL"))
        failures.append("analysis_status is invalid")
    elif analysis_status == "conflict":
        checked.append(("analysis_status", "FAIL"))
        failures.append("analysis_status is conflict")
    else:
        checked.append(("analysis_status", "PASS"))

    # Change detection (MVP: not available)
    checked.append(("source_task change detection", "NOT AVAILABLE"))
    checked.append(("source_contract change detection", "NOT AVAILABLE"))

    if failures:
        print("Execution Readiness: FAIL")
        print("Failures:")
        for item in failures:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    if partials:
        print("Execution Readiness: PARTIAL")
        print("Failures:")
        for item in partials:
            print(f"- {item}")
        print("Exit: 1")
        return 1

    print("Execution Readiness: PASS")
    print("Checked:")
    for name, status in checked:
        print(f"- {name}: {status}")
    print("Notes:")
    for item in notes:
        print(f"- {item}")
    print("- source_task change detection: NOT AVAILABLE")
    print("- source_contract change detection: NOT AVAILABLE")
    print("- PASS means ready-to-start, not done.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except Exception as exc:  # pragma: no cover - safety net
        print("Execution Readiness: FAIL")
        print("Failures:")
        print(f"- implementation failure: {exc}")
        print("Exit: 1")
        raise SystemExit(1)
