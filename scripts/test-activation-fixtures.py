#!/usr/bin/env python3
"""Negative fixture runner for activation safety checks."""

from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURES_ROOT = REPO_ROOT / "tests" / "fixtures" / "negative" / "activation"
ACTIVATE_SCRIPT = REPO_ROOT / "scripts" / "activate-task.py"
PROD_ACTIVE_TASK = REPO_ROOT / "tasks" / "active-task.md"


CASE_COMMANDS = {
    "missing-approved-flag": ["tasks/task-001", "--approval", "approvals/approval.md"],
    "both-approved-and-dry-run": [
        "tasks/task-001",
        "--approval",
        "approvals/approval.md",
        "--dry-run",
        "--approved",
    ],
    "missing-approval-marker": ["tasks/task-001", "--approval", "approvals/missing.md", "--approved"],
    "invalid-approval-marker": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "expired-approval-marker": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "revoked-approval-marker": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "wrong-task-id": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "wrong-scope": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "wrong-transition": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "analysis-status-invalid": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "analysis-status-conflict": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "check-transition-fail": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "contract-missing": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "active-task-different-task": ["tasks/task-001", "--approval", "approvals/approval.md", "--approved"],
    "dry-run-does-not-write": ["tasks/task-001", "--approval", "approvals/approval.md", "--dry-run"],
    "approval-marker-valid-but-no-approved": ["tasks/task-001", "--approval", "approvals/approval.md"],
}


def read_optional(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def parse_expected(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip()
    return result


def copy_repo_runtime(tmp_root: Path) -> None:
    shutil.copytree(REPO_ROOT / "scripts", tmp_root / "scripts")


def prepare_case_workspace(case_dir: Path, tmp_root: Path) -> tuple[Path, str | None]:
    copy_repo_runtime(tmp_root)
    (tmp_root / "tasks").mkdir(parents=True, exist_ok=True)
    (tmp_root / "approvals").mkdir(parents=True, exist_ok=True)
    (tmp_root / "tasks" / "drafts").mkdir(parents=True, exist_ok=True)
    (tmp_root / "tasks" / "done").mkdir(parents=True, exist_ok=True)
    (tmp_root / "tasks" / "failed").mkdir(parents=True, exist_ok=True)
    (tmp_root / "tasks" / "dropped").mkdir(parents=True, exist_ok=True)

    task_src = case_dir / "task"
    if task_src.exists():
        shutil.copytree(task_src, tmp_root / "tasks" / "task-001", dirs_exist_ok=True)

    approvals_src = case_dir / "approvals"
    if approvals_src.exists():
        shutil.copytree(approvals_src, tmp_root / "approvals", dirs_exist_ok=True)

    # Default contract used by most cases.
    default_contract = tmp_root / "tasks" / "drafts" / "task-001-contract-draft.md"
    default_contract.write_text("# contract draft\n", encoding="utf-8")

    before_active_task_content: str | None = None
    case_name = case_dir.name

    if case_name == "analysis-status-invalid":
        # Trigger invalid analysis: active evidence without matching approval evidence.
        before_active_task_content = "task-001\n"
        (tmp_root / "tasks" / "active-task.md").write_text(
            before_active_task_content, encoding="utf-8"
        )
        (tmp_root / "approvals" / "approval.md").write_text(
            "---\n"
            "approval_id: approval-task-999-execution\n"
            "task_id: task-999\n"
            "approval_type: execution\n"
            "approved_by: human\n"
            "approved_at: 2099-01-01T00:00:00Z\n"
            "status: approved\n"
            "scope: activate_task\n"
            "transition: approved_for_execution:active\n"
            "related_contract: tasks/drafts/task-001-contract-draft.md\n"
            "---\n",
            encoding="utf-8",
        )

    if case_name == "analysis-status-conflict":
        # Trigger conflict analysis: active + done evidence together.
        before_active_task_content = "task-001\n"
        (tmp_root / "tasks" / "active-task.md").write_text(
            before_active_task_content, encoding="utf-8"
        )
        (tmp_root / "tasks" / "done" / "task-001.md").write_text("task-001\n", encoding="utf-8")

    if case_name == "check-transition-fail":
        # Keep brief-like state; no contract draft and no valid approval evidence.
        if default_contract.exists():
            default_contract.unlink()

    if case_name == "contract-missing":
        if default_contract.exists():
            default_contract.unlink()

    if case_name == "active-task-different-task":
        before_active_task_content = (
            "---\n"
            "task_id: another-task\n"
            "state: active\n"
            "---\n"
        )
        (tmp_root / "tasks" / "active-task.md").write_text(
            before_active_task_content, encoding="utf-8"
        )

    return tmp_root, before_active_task_content


def validate_active_task_expectation(
    expected_mode: str, active_task_path: Path, before_content: str | None
) -> str | None:
    if expected_mode == "absent":
        if active_task_path.exists():
            return "active-task.md was created/modified unexpectedly"
        return None
    if expected_mode == "unchanged":
        if not active_task_path.exists():
            return "active-task.md expected unchanged but is missing"
        after_content = active_task_path.read_text(encoding="utf-8")
        if before_content is None:
            return "internal error: missing baseline for unchanged check"
        if after_content != before_content:
            return "active-task.md changed but should remain unchanged"
        return None
    return f"unsupported active_task expectation: {expected_mode}"


def run_case(case_dir: Path, production_baseline: str) -> tuple[bool, str]:
    case_name = case_dir.name
    expected = parse_expected(case_dir / "expected.txt")
    args = CASE_COMMANDS.get(case_name)
    if args is None:
        return False, "no command mapping for case"

    with tempfile.TemporaryDirectory(prefix=f"agentos-activation-{case_name}-") as tmp:
        tmp_root = Path(tmp)
        workspace, before_active = prepare_case_workspace(case_dir, tmp_root)
        command = [sys.executable, str(workspace / "scripts" / "activate-task.py"), *args]
        completed = subprocess.run(
            command,
            cwd=str(workspace),
            capture_output=True,
            text=True,
        )
        output = (completed.stdout or "") + (completed.stderr or "")

        expected_exit = expected.get("expected_exit", "nonzero")
        if expected_exit == "zero":
            if completed.returncode != 0:
                return False, f"expected zero exit, got {completed.returncode}"
        else:
            if completed.returncode == 0:
                return False, "expected non-zero exit, got 0"

        contains = expected.get("contains", "")
        if contains and contains not in output:
            return False, f"expected output to contain: {contains}"

        active_expectation = expected.get("active_task", "absent")
        active_error = validate_active_task_expectation(
            active_expectation, workspace / "tasks" / "active-task.md", before_active
        )
        if active_error:
            return False, active_error

    after_production = read_optional(PROD_ACTIVE_TASK)
    if after_production != production_baseline:
        return False, "production tasks/active-task.md was modified"

    return True, ""


def main() -> int:
    if not FIXTURES_ROOT.exists():
        print("Activation negative fixtures: FAIL")
        print("Reason: fixture root does not exist")
        return 1

    production_baseline = read_optional(PROD_ACTIVE_TASK)
    all_ok = True

    for case_dir in sorted(p for p in FIXTURES_ROOT.iterdir() if p.is_dir()):
        try:
            ok, reason = run_case(case_dir, production_baseline)
        except Exception as exc:  # pragma: no cover - defensive
            ok, reason = False, f"runner exception: {exc}"

        if ok:
            print(f"activation fixture {case_dir.name}: PASS")
        else:
            all_ok = False
            print(f"activation fixture {case_dir.name}: FAIL")
            print(f"Reason: {reason}")

    if all_ok:
        print("Activation negative fixtures: PASS")
        return 0

    print("Activation negative fixtures: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
