#!/usr/bin/env python3
"""Negative state machine fixture runner for AgentOS.

Expected rejection is PASS.
This runner uses isolated temporary workspaces.
It must not modify production task files.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = REPO_ROOT / "scripts"


CASES = [
    {
        "name": "active-without-approval",
        "expected_state": "active",
        "expected_analysis_status": "invalid",
        "expected_validator_exit": 1,
        "expected_transition_exit": 1,
        "transition_target": "active",
        "build": "build_active_without_approval",
    },
    {
        "name": "contract-without-trace",
        "expected_state": "contract_drafted",
        "expected_analysis_status": "invalid",
        "expected_validator_exit": 1,
        "expected_transition_exit": 1,
        "transition_target": "approved_for_execution",
        "build": "build_contract_without_trace",
    },
    {
        "name": "review-ready-without-task",
        "expected_state": "review_ready",
        "expected_analysis_status": "invalid",
        "expected_validator_exit": 1,
        "expected_transition_exit": 1,
        "transition_target": "trace_written",
        "build": "build_review_ready_without_task",
    },
    {
        "name": "completed-and-active-conflict",
        "expected_state": "completed",
        "expected_analysis_status": "conflict",
        "expected_validator_exit": 1,
        "expected_transition_exit": 1,
        "transition_target": "active",
        "build": "build_completed_and_active_conflict",
    },
    {
        "name": "dropped-and-active-conflict",
        "expected_state": "dropped",
        "expected_analysis_status": "conflict",
        "expected_validator_exit": 1,
        "expected_transition_exit": 1,
        "transition_target": "active",
        "build": "build_dropped_and_active_conflict",
    },
    {
        "name": "invalid-transition-brief-to-active",
        "expected_state": "brief_draft",
        "expected_analysis_status": "ok",
        "expected_validator_exit": 0,
        "expected_transition_exit": 1,
        "transition_target": "active",
        "build": "build_invalid_transition_brief_to_active",
    },
]


REQUIRED_REPORT_FIELDS = {
    "schema_version",
    "generated_at",
    "task_id",
    "state",
    "analysis_status",
    "evidence",
    "missing_evidence",
    "allowed_next_states",
    "blocked_reason",
    "warnings",
}


def usage() -> None:
    print("Usage: python3 scripts/test-state-fixtures.py")


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_task_base(workspace: Path, task_name: str) -> Path:
    tasks_root = workspace / "tasks"
    task_dir = tasks_root / task_name
    task_dir.mkdir(parents=True, exist_ok=True)
    (tasks_root / "drafts").mkdir(parents=True, exist_ok=True)
    (tasks_root / "done").mkdir(parents=True, exist_ok=True)
    (tasks_root / "dropped").mkdir(parents=True, exist_ok=True)
    (tasks_root / "active-task.md").write_text("", encoding="utf-8")
    return task_dir


def build_active_without_approval(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(workspace / "tasks" / "active-task.md", f"{task_name}\n")
    return task_dir


def build_contract_without_trace(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(
        workspace / "tasks" / "drafts" / f"{task_name}-contract-draft.md",
        "contract draft evidence\n",
    )
    return task_dir


def build_review_ready_without_task(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "REVIEW.md", "review_status: READY\nexecution_allowed: true\n")
    return task_dir


def build_completed_and_active_conflict(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(workspace / "tasks" / "active-task.md", f"{task_name}\n")
    write_file(workspace / "tasks" / "done" / f"{task_name}.md", f"{task_name}\n")
    return task_dir


def build_dropped_and_active_conflict(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(workspace / "tasks" / "active-task.md", f"{task_name}\n")
    write_file(workspace / "tasks" / "dropped" / f"{task_name}.md", f"{task_name}\n")
    return task_dir


def build_invalid_transition_brief_to_active(workspace: Path, task_name: str) -> Path:
    task_dir = build_task_base(workspace, task_name)
    write_file(task_dir / "TASK.md", "status: DRAFT\n")
    return task_dir


BUILDERS = {
    "build_active_without_approval": build_active_without_approval,
    "build_contract_without_trace": build_contract_without_trace,
    "build_review_ready_without_task": build_review_ready_without_task,
    "build_completed_and_active_conflict": build_completed_and_active_conflict,
    "build_dropped_and_active_conflict": build_dropped_and_active_conflict,
    "build_invalid_transition_brief_to_active": build_invalid_transition_brief_to_active,
}


def run_script(script_name: str, task_dir: Path, extra_args: list[str]) -> subprocess.CompletedProcess[str]:
    script_path = SCRIPTS_DIR / script_name
    return subprocess.run(
        [sys.executable, str(script_path), str(task_dir), *extra_args],
        cwd=str(task_dir.parent.parent),
        capture_output=True,
        text=True,
    )


def load_detector_report(task_dir: Path) -> tuple[dict | None, subprocess.CompletedProcess[str]]:
    detector_path = SCRIPTS_DIR / "detect-task-state.py"
    completed = subprocess.run(
        [sys.executable, str(detector_path), str(task_dir)],
        cwd=str(task_dir.parent.parent),
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        return None, completed
    try:
        return json.loads(completed.stdout), completed
    except json.JSONDecodeError:
        return None, completed


def expected_status_matches(expected: object, actual: object) -> bool:
    if isinstance(expected, (set, tuple, list)):
        return actual in expected
    return actual == expected


def validate_detector_report(case: dict, report: dict | None) -> list[str]:
    reasons: list[str] = []
    if not isinstance(report, dict):
        return ["detector returned invalid JSON report"]

    missing = REQUIRED_REPORT_FIELDS - set(report)
    if missing:
        reasons.append(f"missing detector fields: {sorted(missing)}")

    if report.get("schema_version") != "1.1":
        reasons.append(f"unexpected schema_version: {report.get('schema_version')}")

    if report.get("analysis_status") not in {"ok", "invalid", "conflict"}:
        reasons.append(f"unexpected analysis_status: {report.get('analysis_status')}")

    if not isinstance(report.get("warnings"), list):
        reasons.append("warnings must be a list")
    if not isinstance(report.get("evidence"), list):
        reasons.append("evidence must be a list")
    elif any(not isinstance(item, dict) for item in report.get("evidence", [])):
        reasons.append("evidence items must be objects")

    if report.get("state") == "state_conflict":
        reasons.append("deprecated state_conflict must not be emitted")

    expected_state = str(case["expected_state"])
    actual_state = str(report.get("state"))
    actual_analysis = str(report.get("analysis_status"))

    if actual_state != expected_state:
        reasons.append(f"unexpected detector state: {actual_state}")

    if not expected_status_matches(case["expected_analysis_status"], actual_analysis):
        reasons.append(f"unexpected analysis_status: {actual_analysis}")

    return reasons


def validate_transition_output(result: subprocess.CompletedProcess[str]) -> list[str]:
    reasons: list[str] = []
    stdout = result.stdout or ""
    if "Transition executed: no" not in stdout:
        reasons.append("transition checker did not print 'Transition executed: no'")
    return reasons


def main() -> int:
    if len(sys.argv) != 1:
        usage()
        return 2

    print("STATE FIXTURES TEST")
    print()

    all_passed = True

    for case in CASES:
        with tempfile.TemporaryDirectory(prefix=f"agentos-{case['name']}-") as tmp:
            workspace = Path(tmp)
            builder = BUILDERS[case["build"]]
            task_dir = builder(workspace, case["name"])

            report, detector_result = load_detector_report(task_dir)
            detector_reasons = validate_detector_report(case, report)

            validator_result = run_script("validate-task-state.py", task_dir, [])
            transition_result = run_script(
                "check-transition.py",
                task_dir,
                ["--to", case["transition_target"]],
            )

            passed = (
                detector_result.returncode == 0
                and not detector_reasons
                and validator_result.returncode == case["expected_validator_exit"]
                and transition_result.returncode == case["expected_transition_exit"]
                and not validate_transition_output(transition_result)
            )

            all_passed &= passed
            print(f"{case['name']}: {'PASS' if passed else 'FAIL'}")
            if not passed:
                print(f"  expected state: {case['expected_state']}")
                print(f"  expected analysis_status: {case['expected_analysis_status']}")
                print(f"  expected validator exit: {case['expected_validator_exit']}")
                print(f"  expected transition exit: {case['expected_transition_exit']}")
                print(f"  detector exit: {detector_result.returncode}")
                print(f"  validator exit: {validator_result.returncode}")
                print(f"  transition exit: {transition_result.returncode}")
                if detector_reasons:
                    print("  detector issues:")
                    for reason in detector_reasons:
                        print(f"    - {reason}")
                transition_notes = validate_transition_output(transition_result)
                if transition_notes:
                    print("  transition output issues:")
                    for note in transition_notes:
                        print(f"    - {note}")
                stdout = transition_result.stdout.strip()
                stderr = transition_result.stderr.strip()
                if stdout:
                    print("  transition stdout:")
                    for line in stdout.splitlines():
                        print(f"    {line}")
                if stderr:
                    print("  transition stderr:")
                    for line in stderr.splitlines():
                        print(f"    {line}")

    print()
    print(f"Result: {'PASS' if all_passed else 'FAIL'}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
