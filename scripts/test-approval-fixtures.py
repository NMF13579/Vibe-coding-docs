#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "approval-enforcement"
APPLY_SCRIPT = REPO_ROOT / "scripts" / "apply-transition.py"
HUMAN_FIXTURE_RUNNER = REPO_ROOT / "scripts" / "test-human-approval-fixtures.py"

APPROVAL_GATE_REASON_STRINGS = [
    "approval is required but no approval record was provided",
    "approval record file not found",
    "scripts/validate-human-approval.py not found",
    "approval validation failed",
    "approval related_task_id does not match",
    "approval related_transition_id does not match",
    "approval allowed_target_state does not match",
    "approval allowed_operation does not match",
]

# CASES are implemented as Case 1..Case 9 below.
# Protected path guard requirement: approvals/ must not be modified.


@dataclass
class CaseResult:
    name: str
    ok: bool
    detail: str = ""


def hash_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_paths(root: Path, rel_paths: list[str], approvals_hash: bool = False) -> dict[str, str]:
    out: dict[str, str] = {}
    for rel in rel_paths:
        p = root / rel
        if not p.exists():
            out[rel] = "missing"
            continue
        if p.is_file():
            out[rel] = f"file:{hash_file(p)}"
            continue
        for f in sorted(p.rglob("*")):
            r = f.relative_to(root).as_posix()
            if f.is_dir():
                out[r] = "dir"
            else:
                if approvals_hash and rel == "approvals":
                    out[r] = f"file:{hash_file(f)}"
                else:
                    out[r] = "file"
    return out


def run_cmd(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)


def build_workspace(tmp: Path) -> dict[str, Path]:
    (tmp / "scripts").mkdir(parents=True, exist_ok=True)
    (tmp / "tasks" / "done").mkdir(parents=True, exist_ok=True)
    (tmp / "reports" / "execution").mkdir(parents=True, exist_ok=True)
    (tmp / "approvals").mkdir(parents=True, exist_ok=True)
    (tmp / "plans").mkdir(parents=True, exist_ok=True)
    (tmp / "transitions").mkdir(parents=True, exist_ok=True)

    shutil.copy2(REPO_ROOT / "scripts" / "apply-transition.py", tmp / "scripts" / "apply-transition.py")
    shutil.copy2(REPO_ROOT / "scripts" / "check-apply-preconditions.py", tmp / "scripts" / "check-apply-preconditions.py")
    shutil.copy2(REPO_ROOT / "scripts" / "validate-human-approval.py", tmp / "scripts" / "validate-human-approval.py")

    (tmp / "tasks" / "active-task.md").write_text(
        "---\n"
        "task_id: task-fixture-approval-enforcement\n"
        "state: active\n"
        "source_task: tasks/task-fixture-approval-enforcement/TASK.md\n"
        "source_contract: tasks/drafts/task-fixture-approval-enforcement-contract.md\n"
        "---\n",
        encoding="utf-8",
    )

    (tmp / "reports" / "execution" / "session-fixture.md").write_text(
        "status: evidence_ready\nscope_result: PASS\nverification_result: PASS\n",
        encoding="utf-8",
    )
    (tmp / "reports" / "execution-evidence-report.md").write_text(
        "evidence_report_result: PASS\n",
        encoding="utf-8",
    )

    transition_required = (FIXTURE_ROOT / "approval-required-transition.md").read_text(encoding="utf-8")
    transition_not_required = (FIXTURE_ROOT / "approval-not-required-transition.md").read_text(encoding="utf-8")

    (tmp / "transitions" / "required.md").write_text(transition_required, encoding="utf-8")
    (tmp / "transitions" / "not-required.md").write_text(transition_not_required, encoding="utf-8")

    (tmp / "plans" / "apply-plan.md").write_text(
        "task_id: task-fixture-approval-enforcement\n"
        "result: APPLY_PLAN_PREPARED\n"
        f"source_prepared_transition: {tmp / 'transitions' / 'required.md'}\n",
        encoding="utf-8",
    )

    (tmp / "plans" / "applied-record.md").write_text(
        "task_id: task-fixture-approval-enforcement\n"
        "result: APPLY_EVIDENCE_CREATED\n"
        f"source_prepared_transition: {tmp / 'transitions' / 'required.md'}\n"
        f"preconditions_result_ref: {tmp / 'scripts' / 'check-apply-preconditions.py'}\n",
        encoding="utf-8",
    )

    done_dir = (tmp / "tasks" / "done").resolve().as_posix()
    done_file = ((tmp / "tasks" / "done") / "task-fixture-approval-enforcement.md").resolve().as_posix()

    mp = (FIXTURE_ROOT / "approval-required-mutation-plan.md").read_text(encoding="utf-8")
    mp = mp.replace("__TO_BE_REPLACED__", done_dir).replace("__TO_BE_REPLACED_DONE__", done_file)
    (tmp / "plans" / "required-mutation-plan.md").write_text(mp, encoding="utf-8")

    mp2 = mp.replace("approval_required: true", "approval_required: false")
    (tmp / "plans" / "not-required-mutation-plan.md").write_text(mp2, encoding="utf-8")

    for name in [
        "valid-approval.md",
        "invalid-vague-approval.md",
        "task-mismatch-approval.md",
        "transition-mismatch-approval.md",
        "unsupported-operation-approval.md",
        "unsupported-target-state-approval.md",
    ]:
        shutil.copy2(FIXTURE_ROOT / name, tmp / "approvals" / name)

    return {
        "transition_required": tmp / "transitions" / "required.md",
        "transition_not_required": tmp / "transitions" / "not-required.md",
        "plan": tmp / "plans" / "apply-plan.md",
        "applied": tmp / "plans" / "applied-record.md",
        "mp_required": tmp / "plans" / "required-mutation-plan.md",
        "mp_not_required": tmp / "plans" / "not-required-mutation-plan.md",
    }


def has_gate_reason(output: str) -> bool:
    low = output.lower()
    return any(token.lower() in low for token in APPROVAL_GATE_REASON_STRINGS)


def run_complete_active(tmp: Path, paths: dict[str, Path], transition: Path, mutation_plan: Path, approval: Path | None) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(tmp / "scripts" / "apply-transition.py"),
        "--transition",
        str(transition),
        "--plan",
        str(paths["plan"]),
        "--applied-record",
        str(paths["applied"]),
        "--mutation-plan",
        str(mutation_plan),
        "--complete-active",
    ]
    if approval is not None:
        cmd.extend(["--approval", str(approval)])
    return run_cmd(cmd, tmp)


def main() -> int:
    if not HUMAN_FIXTURE_RUNNER.is_file():
        print("BLOCKED")
        print("- scripts/test-human-approval-fixtures.py not found")
        return 1

    pre = run_cmd([sys.executable, str(HUMAN_FIXTURE_RUNNER)], REPO_ROOT)
    if pre.returncode != 0:
        print(pre.stdout.strip())
        if pre.stderr.strip():
            print(pre.stderr.strip())
        print("BLOCKED")
        print("- human approval fixture preflight failed")
        return 1

    protected = ["approvals", "tasks", "reports", "docs", "templates"]
    before = snapshot_paths(REPO_ROOT, protected, approvals_hash=True)

    results: list[CaseResult] = []

    with tempfile.TemporaryDirectory(prefix="agentos-approval-enforcement-") as t:
        tmp = Path(t)
        paths = build_workspace(tmp)

        # Case 1
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], None)
        ok = p.returncode != 0 and "approval is required but no approval record was provided" in p.stdout
        results.append(CaseResult("Case 1", ok, p.stdout.strip()))

        # Case 2
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "invalid-vague-approval.md")
        ok = p.returncode != 0 and "approval validation failed" in p.stdout
        results.append(CaseResult("Case 2", ok, p.stdout.strip()))

        # Case 3
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "task-mismatch-approval.md")
        ok = p.returncode != 0 and "approval related_task_id does not match lifecycle task_id" in p.stdout
        results.append(CaseResult("Case 3", ok, p.stdout.strip()))

        # Case 4
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "transition-mismatch-approval.md")
        ok = p.returncode != 0 and "approval related_transition_id does not match lifecycle transition_id" in p.stdout
        results.append(CaseResult("Case 4", ok, p.stdout.strip()))

        # Case 5
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "unsupported-operation-approval.md")
        ok = p.returncode != 0 and "approval validation failed" in p.stdout and "allowed_operation is not supported" in p.stdout
        results.append(CaseResult("Case 5", ok, p.stdout.strip()))

        # Case 6
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "unsupported-target-state-approval.md")
        ok = p.returncode != 0 and "approval validation failed" in p.stdout and "allowed_target_state is not supported" in p.stdout
        results.append(CaseResult("Case 6", ok, p.stdout.strip()))

        # Case 7 semantics
        p = run_complete_active(tmp, paths, paths["transition_required"], paths["mp_required"], tmp / "approvals" / "valid-approval.md")
        if p.returncode == 0:
            results.append(CaseResult("Case 7", True, "PASS"))
        else:
            if has_gate_reason(p.stdout):
                results.append(CaseResult("Case 7", False, p.stdout.strip()))
            else:
                results.append(CaseResult("Case 7", True, "PASS (approval gate passed, later non-approval check blocked)\nreason: " + p.stdout.strip()))

        # Case 8
        p = run_complete_active(tmp, paths, paths["transition_not_required"], paths["mp_not_required"], tmp / "approvals" / "invalid-vague-approval.md")
        ok = p.returncode != 0 and "approval validation failed" in p.stdout
        results.append(CaseResult("Case 8", ok, p.stdout.strip()))

        # Case 9 isolation semantics
        p = run_cmd(
            [
                sys.executable,
                str(tmp / "scripts" / "apply-transition.py"),
                "--transition",
                str(paths["transition_required"]),
                "--dry-run",
            ],
            tmp,
        )
        if p.returncode == 0:
            results.append(CaseResult("Case 9", True, "PASS"))
        else:
            if has_gate_reason(p.stdout):
                results.append(CaseResult("Case 9", False, p.stdout.strip()))
            else:
                results.append(CaseResult("Case 9", True, "PASS (non-complete-active not blocked by approval gate)\nreason: " + p.stdout.strip()))

    after = snapshot_paths(REPO_ROOT, protected, approvals_hash=True)
    guard_ok = before == after

    all_ok = True
    for r in results:
        if r.ok:
            print(f"PASS   {r.name}")
            if r.detail and ("PASS (" in r.detail):
                print(r.detail)
        else:
            all_ok = False
            print(f"FAILED {r.name}")
            if r.detail:
                print(r.detail)

    if not guard_ok:
        all_ok = False
        print("FAILED protected path guard")
        print("real protected paths changed")

    if all_ok:
        print("PASS")
        return 0

    print("BLOCKED")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
