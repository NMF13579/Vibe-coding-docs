#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path

# Apply transition fixtures must not mutate real repository tasks or reports.
SAFETY_STATEMENT = "Apply transition fixtures must not mutate real repository tasks or reports."

FIXTURES = [
    "missing-transition",
    "protected-applied-record-out",
    "missing-apply-plan",
    "missing-applied-evidence",
    "missing-mutation-plan",
    "happy-path",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run apply-transition fixture tests in temp workspaces.")
    parser.add_argument("--keep-temp", action="store_true", help="Keep temp workspaces for debugging.")
    parser.add_argument("--verbose", action="store_true", help="Print command output for each fixture.")
    return parser.parse_args()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True)


def write_common_workspace(temp_root: Path, repo_root: Path) -> None:
    (temp_root / "scripts").mkdir(parents=True, exist_ok=True)
    (temp_root / "tasks" / "done").mkdir(parents=True, exist_ok=True)
    (temp_root / "reports").mkdir(parents=True, exist_ok=True)
    (temp_root / "docs").mkdir(parents=True, exist_ok=True)

    shutil.copy2(repo_root / "scripts" / "apply-transition.py", temp_root / "scripts" / "apply-transition.py")
    shutil.copy2(
        repo_root / "scripts" / "check-apply-preconditions.py",
        temp_root / "scripts" / "check-apply-preconditions.py",
    )

    active = (
        "---\n"
        "task_id: task-fixture-001\n"
        "state: active\n"
        "source_task: tasks/task-fixture-001/TASK.md\n"
        "source_contract: tasks/drafts/task-fixture-001-contract.md\n"
        "---\n"
    )
    (temp_root / "tasks" / "active-task.md").write_text(active, encoding="utf-8")

    (temp_root / "reports" / "execution").mkdir(parents=True, exist_ok=True)
    (temp_root / "reports" / "execution" / "session-fixture.md").write_text(
        "status: evidence_ready\nscope_result: PASS\nverification_result: PASS\n",
        encoding="utf-8",
    )
    (temp_root / "reports" / "execution-evidence-report.md").write_text(
        "evidence_report_result: PASS\n", encoding="utf-8"
    )


def write_happy_inputs(temp_root: Path) -> dict[str, Path]:
    transition = temp_root / "transition.md"
    plan = temp_root / "apply-plan.md"
    applied = temp_root / "applied-record.md"
    mutation = temp_root / "mutation-plan.md"

    transition.write_text(
        "\n".join(
            [
                "task_id: task-fixture-001",
                "previous_state: active",
                "target_state: completed",
                "completion_readiness: reports/execution-evidence-report.md",
                "execution_session: reports/execution/session-fixture.md",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    plan.write_text("task_id: task-fixture-001\nresult: APPLY_PLAN_PREPARED\n", encoding="utf-8")
    applied.write_text("task_id: task-fixture-001\nresult: APPLY_EVIDENCE_CREATED\n", encoding="utf-8")

    destination_dir = (temp_root / "tasks" / "done").resolve()
    destination = (destination_dir / "task-fixture-001.md").as_posix()
    mutation.write_text(
        "\n".join(
            [
                "task_id: task-fixture-001",
                "result: COMPLETE_ACTIVE_PLAN_READY",
                f"completion_destination: {destination_dir.as_posix()}",
                "allowed_task_paths:",
                "  - tasks/active-task.md",
                f"  - {destination}",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    return {"transition": transition, "plan": plan, "applied": applied, "mutation": mutation}


def fixture_case(name: str, temp_root: Path, verbose: bool) -> tuple[bool, list[str]]:
    errors: list[str] = []
    active = temp_root / "tasks" / "active-task.md"
    before_hash = sha256(active)

    inputs = write_happy_inputs(temp_root)

    if name == "missing-transition":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            "/tmp/nonexistent-agentos-transition.md",
            "--plan",
            str(inputs["plan"]),
            "--applied-record",
            str(inputs["applied"]),
            "--mutation-plan",
            str(inputs["mutation"]),
            "--complete-active",
        ]
        expected_zero = False
    elif name == "protected-applied-record-out":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            str(inputs["transition"]),
            "--plan",
            str(inputs["plan"]),
            "--apply",
            "--applied-record-out",
            "docs/APPLIED-TRANSITION-RECORD.md",
        ]
        expected_zero = False
    elif name == "missing-apply-plan":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            str(inputs["transition"]),
            "--plan",
            "/tmp/nonexistent-agentos-apply-plan.md",
            "--applied-record",
            str(inputs["applied"]),
            "--complete-active-plan",
        ]
        expected_zero = False
    elif name == "missing-applied-evidence":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            str(inputs["transition"]),
            "--plan",
            str(inputs["plan"]),
            "--applied-record",
            "/tmp/nonexistent-agentos-applied-record.md",
            "--complete-active-plan",
        ]
        expected_zero = False
    elif name == "missing-mutation-plan":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            str(inputs["transition"]),
            "--plan",
            str(inputs["plan"]),
            "--applied-record",
            str(inputs["applied"]),
            "--complete-active",
        ]
        expected_zero = False
    elif name == "happy-path":
        cmd = [
            "python3",
            "scripts/apply-transition.py",
            "--transition",
            str(inputs["transition"]),
            "--plan",
            str(inputs["plan"]),
            "--applied-record",
            str(inputs["applied"]),
            "--mutation-plan",
            str(inputs["mutation"]),
            "--complete-active",
        ]
        expected_zero = True
    else:
        return (False, [f"unknown fixture {name}"])

    proc = run(cmd, temp_root)

    if verbose:
        print(f"fixture: {name}")
        print(f"command: {' '.join(cmd)}")
        print(proc.stdout.strip())
        if proc.stderr.strip():
            print(proc.stderr.strip())

    ok = (proc.returncode == 0) == expected_zero
    if not ok:
        errors.append(f"unexpected exit code {proc.returncode}, expected_zero={expected_zero}")

    after_hash = sha256(active)
    if not expected_zero and before_hash != after_hash:
        errors.append("blocked case modified temp active task")

    if expected_zero:
        out = proc.stdout
        if "modified_task_paths" not in out:
            errors.append("happy-path output missing modified_task_paths")

        changed = []
        if before_hash != after_hash:
            changed.append("tasks/active-task.md")
        done_file = temp_root / "tasks" / "done" / "task-fixture-001.md"
        if done_file.exists():
            changed.append("tasks/done/task-fixture-001.md")

        allowed = {"tasks/active-task.md", "tasks/done/task-fixture-001.md"}
        for p in changed:
            if p not in allowed:
                errors.append(f"happy-path changed unexpected path: {p}")

        if not changed:
            errors.append("happy-path did not mutate expected temp task paths")

    return (len(errors) == 0, errors)


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    fixtures_root = repo_root / "tests" / "fixtures" / "apply-transition"

    print(SAFETY_STATEMENT)

    passed = 0
    failed = 0

    for name in FIXTURES:
        fixture_dir = fixtures_root / name
        if not fixture_dir.is_dir():
            print(f"FAIL {name}: missing fixture directory")
            failed += 1
            continue

        tmp_obj = tempfile.TemporaryDirectory(prefix=f"agentos-{name}-")
        temp_root = Path(tmp_obj.name)

        try:
            write_common_workspace(temp_root, repo_root)
            # Copy fixture files (minimal metadata) into temp workspace
            shutil.copytree(fixture_dir, temp_root / "fixture", dirs_exist_ok=True)

            ok, errors = fixture_case(name, temp_root, args.verbose)
            cmd_note = "python3 scripts/apply-transition.py ..."
            expected = "PASS" if name == "happy-path" else "FAIL"
            actual = "PASS" if ok else "FAIL"
            print(f"fixture={name} command={cmd_note} expected={expected} actual={actual}")
            if errors:
                for e in errors:
                    print(f"  - {e}")

            if args.keep_temp:
                print(f"temp_workspace={temp_root}")

            if ok:
                passed += 1
            else:
                failed += 1
        finally:
            if args.keep_temp:
                tmp_obj.cleanup = lambda: None
            else:
                tmp_obj.cleanup()

    print(f"PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
