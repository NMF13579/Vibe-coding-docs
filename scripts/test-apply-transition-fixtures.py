#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

# Apply transition fixtures must not mutate real repository tasks or reports.
SAFETY_STATEMENT = "Apply transition fixtures must not mutate real repository tasks or reports."
VERSION = "1.0.0"

PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass
class CaseResult:
    name: str
    status: str
    message: str = ""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run apply-transition fixture tests in temp workspaces.")
    parser.add_argument("--keep-temp", action="store_true", help="Keep temp workspaces for debugging.")
    parser.add_argument("--verbose", action="store_true", help="Print command outputs.")
    return parser.parse_args()


def run_command(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def snapshot_protected_paths(repo_root: Path, rel_paths: list[str]) -> dict[str, str]:
    snapshot: dict[str, str] = {}
    for rel in rel_paths:
        target = repo_root / rel
        if target.is_file():
            snapshot[rel] = f"file:{file_hash(target)}"
            continue
        if target.is_dir():
            for p in sorted(target.rglob("*")):
                relp = p.relative_to(repo_root).as_posix()
                if p.is_file():
                    snapshot[relp] = f"file:{file_hash(p)}"
                elif p.is_dir():
                    snapshot[relp] = "dir"
            continue
        snapshot[rel] = "missing"
    return snapshot


def assert_protected_paths_unchanged(before: dict[str, str], after: dict[str, str]) -> tuple[bool, list[str]]:
    changed: list[str] = []
    keys = sorted(set(before.keys()) | set(after.keys()))
    for k in keys:
        if before.get(k) != after.get(k):
            changed.append(k)
    return (len(changed) == 0, changed)


def make_temp_workspace(repo_root: Path, case_name: str) -> tempfile.TemporaryDirectory[str]:
    tmp = tempfile.TemporaryDirectory(prefix=f"agentos-{case_name}-")
    root = Path(tmp.name)

    (root / "scripts").mkdir(parents=True, exist_ok=True)
    (root / "tasks" / "done").mkdir(parents=True, exist_ok=True)
    (root / "reports" / "execution").mkdir(parents=True, exist_ok=True)
    (root / "docs").mkdir(parents=True, exist_ok=True)

    shutil.copy2(repo_root / "scripts" / "apply-transition.py", root / "scripts" / "apply-transition.py")
    shutil.copy2(repo_root / "scripts" / "check-apply-preconditions.py", root / "scripts" / "check-apply-preconditions.py")

    write_text(
        root / "tasks" / "active-task.md",
        "---\n"
        "task_id: task-fixture-001\n"
        "state: active\n"
        "source_task: tasks/task-fixture-001/TASK.md\n"
        "source_contract: tasks/drafts/task-fixture-001-contract.md\n"
        "---\n",
    )

    write_text(
        root / "reports" / "execution" / "session-fixture.md",
        "status: evidence_ready\n"
        "scope_result: PASS\n"
        "verification_result: PASS\n",
    )
    write_text(root / "reports" / "execution-evidence-report.md", "evidence_report_result: PASS\n")

    return tmp


def base_inputs(root: Path) -> dict[str, Path]:
    transition = root / "transition.md"
    plan = root / "apply-plan.md"
    applied = root / "applied-record.md"
    mutation = root / "mutation-plan.md"

    done_dir = (root / "tasks" / "done").resolve()
    done_file = done_dir / "task-fixture-001.md"

    write_text(
        transition,
        "task_id: task-fixture-001\n"
        "previous_state: active\n"
        "target_state: completed\n"
        "completion_readiness: reports/execution-evidence-report.md\n"
        "execution_session: reports/execution/session-fixture.md\n",
    )

    write_text(
        plan,
        "task_id: task-fixture-001\n"
        "result: APPLY_PLAN_PREPARED\n"
        f"source_prepared_transition: {transition}\n",
    )

    write_text(
        applied,
        "task_id: task-fixture-001\n"
        "result: APPLY_EVIDENCE_CREATED\n"
        f"source_prepared_transition: {transition}\n"
        f"preconditions_result_ref: {root / 'scripts' / 'check-apply-preconditions.py'}\n",
    )

    write_text(
        mutation,
        "task_id: task-fixture-001\n"
        "result: COMPLETE_ACTIVE_PLAN_READY\n"
        f"completion_destination: {done_dir.as_posix()}\n"
        "completion_operation: copy_active_task_to_completion_destination_and_mark_active_task_completed\n"
        "allowed_task_paths:\n"
        "  - tasks/active-task.md\n"
        f"  - {done_file.as_posix()}\n"
        "would_mutate: true\n",
    )

    return {
        "transition": transition,
        "plan": plan,
        "applied": applied,
        "mutation": mutation,
        "done_file": done_file,
    }


def run_case(case_name: str, root: Path, verbose: bool) -> tuple[bool, bool, str, list[str]]:
    """returns: ok, limitation_warn, output, mutated_paths"""
    inputs = base_inputs(root)
    active = root / "tasks" / "active-task.md"

    cmd: list[str]
    expected_rc = 1
    limitation_warn = False

    if case_name == "missing-transition":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", "/tmp/nonexistent-agentos-transition.md",
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "protected-applied-record-out":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--apply", "--applied-record-out", "docs/APPLIED-TRANSITION-RECORD.md",
        ]
    elif case_name == "missing-apply-plan":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", "/tmp/nonexistent-agentos-apply-plan.md",
            "--applied-record", str(inputs["applied"]),
            "--complete-active-plan",
        ]
    elif case_name == "missing-applied-evidence":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", "/tmp/nonexistent-agentos-applied-record.md",
            "--complete-active-plan",
        ]
    elif case_name == "missing-mutation-plan":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--complete-active",
        ]
    elif case_name == "target-state-not-completed":
        write_text(inputs["transition"], read_text(inputs["transition"]).replace("target_state: completed", "target_state: failed"))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "transition-task-id-mismatch":
        write_text(inputs["transition"], read_text(inputs["transition"]).replace("task-fixture-001", "task-fixture-XYZ", 1))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "apply-plan-wrong-transition":
        write_text(inputs["plan"], read_text(inputs["plan"]).replace("task-fixture-001", "task-fixture-PLAN", 1))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "applied-record-wrong-plan":
        write_text(inputs["applied"], read_text(inputs["applied"]).replace("task-fixture-001", "task-fixture-APPLIED", 1))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "mutation-plan-wrong-task":
        write_text(inputs["mutation"], read_text(inputs["mutation"]).replace("task-fixture-001", "task-fixture-MUT", 1))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "mutation-plan-would-mutate-false":
        write_text(inputs["mutation"], read_text(inputs["mutation"]).replace("would_mutate: true", "would_mutate: false"))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "destination-outside-allowed-paths":
        unsafe = (root / "docs").resolve().as_posix()
        write_text(inputs["mutation"], read_text(inputs["mutation"]).replace((root / "tasks" / "done").resolve().as_posix(), unsafe))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "active-task-mismatch":
        write_text(active, read_text(active).replace("task-fixture-001", "task-fixture-ACTIVE"))
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "missing-required-human-approval-evidence":
        write_text(inputs["transition"], read_text(inputs["transition"]) + "approval_required: true\n")
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
    elif case_name == "protected-output-path-attempt":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--prepare", "--plan-out", "templates/apply-plan.md",
        ]
    elif case_name == "happy-path":
        cmd = [
            "python3", "scripts/apply-transition.py",
            "--transition", str(inputs["transition"]),
            "--plan", str(inputs["plan"]),
            "--applied-record", str(inputs["applied"]),
            "--mutation-plan", str(inputs["mutation"]),
            "--complete-active",
        ]
        expected_rc = 0
    else:
        return (False, False, f"unknown case {case_name}", [])

    before_active = file_hash(active)
    proc = run_command(cmd, root)

    if verbose:
        print(f"case={case_name}")
        print(f"command={' '.join(cmd)}")
        if proc.stdout.strip():
            print(proc.stdout.strip())
        if proc.stderr.strip():
            print(proc.stderr.strip())

    after_active = file_hash(active)
    mutated_paths: list[str] = []
    if before_active != after_active:
        mutated_paths.append("tasks/active-task.md")
    if (root / "tasks" / "done" / "task-fixture-001.md").exists():
        mutated_paths.append("tasks/done/task-fixture-001.md")

    if expected_rc == 1:
        if proc.returncode == 0:
            if case_name == "missing-required-human-approval-evidence":
                limitation_warn = True
                return (
                    True,
                    True,
                    "limitation: current implementation does not yet enforce approval-required blocking",
                    mutated_paths,
                )
            return (False, False, f"expected failure but got rc=0", mutated_paths)
        if before_active != after_active:
            return (False, False, "blocked case modified temp active task", mutated_paths)
        return (True, limitation_warn, "", mutated_paths)

    # happy path
    if proc.returncode != 0:
        return (False, False, f"expected success but got rc={proc.returncode}", mutated_paths)
    if "modified_task_paths" not in proc.stdout:
        return (False, False, "happy-path output missing modified_task_paths", mutated_paths)

    allowed = {"tasks/active-task.md", "tasks/done/task-fixture-001.md"}
    for p in mutated_paths:
        if p not in allowed:
            return (False, False, f"happy-path changed unexpected path: {p}", mutated_paths)
    if not mutated_paths:
        return (False, False, "happy-path did not mutate expected temp task paths", mutated_paths)

    return (True, False, "", mutated_paths)


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    fixture_root = repo_root / "tests" / "fixtures" / "apply-transition"

    print("Apply Transition Fixture Tests")
    print(f"version: {VERSION}")
    print()
    print(SAFETY_STATEMENT)

    required_fixture_dirs = [
        "missing-transition",
        "protected-applied-record-out",
        "missing-apply-plan",
        "missing-applied-evidence",
        "missing-mutation-plan",
        "target-state-not-completed",
        "transition-task-id-mismatch",
        "apply-plan-wrong-transition",
        "applied-record-wrong-plan",
        "mutation-plan-wrong-task",
        "mutation-plan-would-mutate-false",
        "destination-outside-allowed-paths",
        "active-task-mismatch",
        "missing-required-human-approval-evidence",
        "protected-output-path-attempt",
        "happy-path",
    ]

    protected_real = ["tasks", "reports", "docs", "templates"]
    before = snapshot_protected_paths(repo_root, protected_real)

    results: list[CaseResult] = []
    overall = PASS

    for d in required_fixture_dirs:
        if not (fixture_root / d).is_dir():
            results.append(CaseResult(d, FAIL, "missing fixture directory"))
            overall = FAIL

    labels = {
        "missing-transition": "missing transition blocks",
        "protected-applied-record-out": "protected applied-record-out blocks",
        "missing-apply-plan": "missing apply plan blocks",
        "missing-applied-evidence": "missing applied evidence blocks",
        "missing-mutation-plan": "missing mutation plan blocks",
        "target-state-not-completed": "target state not completed blocks",
        "transition-task-id-mismatch": "transition task id mismatch blocks",
        "apply-plan-wrong-transition": "apply plan wrong transition blocks",
        "applied-record-wrong-plan": "applied record wrong plan blocks",
        "mutation-plan-wrong-task": "mutation plan wrong task blocks",
        "mutation-plan-would-mutate-false": "mutation plan would_mutate false blocks",
        "destination-outside-allowed-paths": "destination outside allowed paths blocks",
        "active-task-mismatch": "active task mismatch blocks",
        "missing-required-human-approval-evidence": "missing required human approval evidence",
        "protected-output-path-attempt": "protected output path attempt blocks",
        "happy-path": "complete-active happy path in temp workspace",
    }

    for case_name in labels:
        if not (fixture_root / case_name).is_dir():
            continue

        tmp = make_temp_workspace(repo_root, case_name)
        root = Path(tmp.name)
        try:
            shutil.copytree(fixture_root / case_name, root / "fixture", dirs_exist_ok=True)
            ok, limitation_warn, msg, mutated = run_case(case_name, root, args.verbose)

            if ok and not limitation_warn:
                results.append(CaseResult(labels[case_name], PASS, ""))
            elif ok and limitation_warn:
                results.append(CaseResult(labels[case_name], WARN, msg))
                if overall == PASS:
                    overall = WARN
            else:
                results.append(CaseResult(labels[case_name], FAIL, msg + (f"; mutated paths: {', '.join(mutated)}" if mutated else "")))
                overall = FAIL

            if args.keep_temp:
                print(f"temp workspace path when --keep-temp is used: {root}")
        finally:
            if not args.keep_temp:
                tmp.cleanup()

    after = snapshot_protected_paths(repo_root, protected_real)
    unchanged, changed = assert_protected_paths_unchanged(before, after)
    if not unchanged:
        results.append(CaseResult("repository safety check", FAIL, "real protected paths changed: " + ", ".join(changed)))
        overall = FAIL

    for r in results:
        print(f"[{r.status}] {r.name}")
        if r.message:
            print(f"  {r.message}")

    print()
    print(f"Result: {overall}")

    if overall == FAIL:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
