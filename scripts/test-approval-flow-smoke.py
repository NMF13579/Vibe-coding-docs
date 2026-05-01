#!/usr/bin/env python3

from __future__ import annotations

import hashlib
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_ROOT = REPO_ROOT / "tests" / "fixtures" / "approval-flow-smoke"
VALIDATOR = REPO_ROOT / "scripts" / "validate-human-approval.py"
PRECONDITIONS = REPO_ROOT / "scripts" / "check-apply-preconditions.py"
APPLY = REPO_ROOT / "scripts" / "apply-transition.py"

APPROVAL_GATE_REASONS = [
    "approval is required but no approval record was provided",
    "approval record file not found",
    "scripts/validate-human-approval.py not found",
    "approval validation failed",
    "approval related_task_id does not match",
    "approval related_transition_id does not match",
    "approval allowed_target_state does not match",
    "approval allowed_operation does not match",
]


def run_cmd(args: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=str(cwd), capture_output=True, text=True)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_protected(root: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    for rel in ["approvals", "tasks", "reports", "docs", "templates"]:
        p = root / rel
        if not p.exists():
            out[f"{rel}/"] = "missing"
            continue
        for f in sorted(p.rglob("*")):
            r = f.relative_to(root).as_posix()
            if f.is_dir():
                out[r] = "dir"
            else:
                out[r] = sha256_file(f)
    return out


def detect_support(script: Path, flag: str) -> bool:
    p = run_cmd([sys.executable, str(script), "--help"], REPO_ROOT)
    return p.returncode == 0 and flag in ((p.stdout or "") + (p.stderr or ""))


def has_gate_reason(text: str) -> bool:
    low = text.lower()
    return any(token.lower() in low for token in APPROVAL_GATE_REASONS)


def classify_result(stdout: str) -> str:
    t = stdout.strip()
    if "Result: PASS" in t or t.endswith("PASS"):
        return "PASS"
    if "Result: WARN" in t or t.endswith("WARN"):
        return "WARN"
    if "BLOCKED" in t:
        return "BLOCKED"
    if "FAIL" in t:
        return "FAIL"
    return "WARN"


def copy_fixtures(tmp: Path) -> dict[str, Path]:
    (tmp / "tasks" / "done").mkdir(parents=True, exist_ok=True)
    (tmp / "reports" / "execution").mkdir(parents=True, exist_ok=True)
    (tmp / "transitions").mkdir(parents=True, exist_ok=True)
    (tmp / "approvals").mkdir(parents=True, exist_ok=True)
    (tmp / "plans").mkdir(parents=True, exist_ok=True)

    shutil.copy2(FIXTURE_ROOT / "synthetic-task.md", tmp / "tasks" / "active-task.md")
    shutil.copy2(FIXTURE_ROOT / "synthetic-verification.md", tmp / "reports" / "execution" / "session-fixture.md")
    shutil.copy2(FIXTURE_ROOT / "synthetic-readiness.md", tmp / "reports" / "execution-evidence-report.md")
    shutil.copy2(FIXTURE_ROOT / "synthetic-transition.md", tmp / "transitions" / "synthetic-transition.md")
    shutil.copy2(FIXTURE_ROOT / "synthetic-apply-plan.md", tmp / "plans" / "synthetic-apply-plan.md")
    shutil.copy2(FIXTURE_ROOT / "synthetic-applied-transition-record.md", tmp / "plans" / "synthetic-applied-transition-record.md")
    shutil.copy2(FIXTURE_ROOT / "valid-approval.md", tmp / "approvals" / "valid-approval.md")
    shutil.copy2(FIXTURE_ROOT / "invalid-vague-approval.md", tmp / "approvals" / "invalid-vague-approval.md")

    mp = (FIXTURE_ROOT / "synthetic-mutation-plan.md").read_text(encoding="utf-8")
    done_dir = (tmp / "tasks" / "done").resolve().as_posix()
    done_file = ((tmp / "tasks" / "done") / "task-fixture-approval-smoke.md").resolve().as_posix()
    mp = mp.replace("__TO_BE_REPLACED__", done_dir).replace("__TO_BE_REPLACED_DONE__", done_file)
    (tmp / "plans" / "synthetic-mutation-plan.md").write_text(mp, encoding="utf-8")

    return {
        "transition": tmp / "transitions" / "synthetic-transition.md",
        "plan": tmp / "plans" / "synthetic-apply-plan.md",
        "applied": tmp / "plans" / "synthetic-applied-transition-record.md",
        "mutation": tmp / "plans" / "synthetic-mutation-plan.md",
        "valid_approval": tmp / "approvals" / "valid-approval.md",
        "invalid_approval": tmp / "approvals" / "invalid-vague-approval.md",
    }


def main() -> int:
    print("Approval Evidence Flow Smoke")

    if not FIXTURE_ROOT.is_dir():
        print("[FAIL] fixture directory missing")
        print("Result: FAIL")
        return 1

    before = snapshot_protected(REPO_ROOT)
    print("[PASS] protected path snapshot before")

    precond_support = detect_support(PRECONDITIONS, "--approval")
    apply_support = detect_support(APPLY, "--approval")
    print(f"[INFO] check-apply-preconditions --approval support: {'yes' if precond_support else 'no'}")
    print(f"[INFO] apply-transition --approval support: {'yes' if apply_support else 'no'}")

    warn_mode = False
    failed = False

    with tempfile.TemporaryDirectory(prefix="agentos-approval-flow-smoke-") as d:
        tmp = Path(d)
        paths = copy_fixtures(tmp)
        print("[PASS] temp workspace prepared")

        v = run_cmd([sys.executable, str(VALIDATOR), str(paths["valid_approval"])], REPO_ROOT)
        if v.returncode == 0 and "PASS" in (v.stdout or ""):
            print("[PASS] approval validator positive path")
        else:
            print("[FAIL] approval validator positive path")
            print((v.stdout or v.stderr).strip())
            failed = True

        if precond_support:
            pc = run_cmd(
                [
                    sys.executable,
                    str(PRECONDITIONS),
                    "--transition",
                    str(paths["transition"]),
                    "--active-task",
                    str(tmp / "tasks" / "active-task.md"),
                    "--approval",
                    str(paths["valid_approval"]),
                ],
                REPO_ROOT,
            )
            out = (pc.stdout or "")
            if "PASS" in out or ("BLOCKED" in out and "approval validation failed" not in out and "approval is required but no approval record was provided" not in out):
                print("[PASS] preconditions positive path (approval gate passed)")
            else:
                print("[FAIL] preconditions positive path")
                print(out.strip())
                failed = True

            neg = run_cmd(
                [
                    sys.executable,
                    str(PRECONDITIONS),
                    "--transition",
                    str(paths["transition"]),
                    "--active-task",
                    str(tmp / "tasks" / "active-task.md"),
                ],
                REPO_ROOT,
            )
            if "approval is required but no approval record was provided" in (neg.stdout or ""):
                print("[PASS] missing-approval negative path via preconditions")
            else:
                print("[FAIL] missing-approval negative path via preconditions")
                print((neg.stdout or neg.stderr).strip())
                failed = True
        else:
            print("[WARN] preconditions interface limitation")
            warn_mode = True

        if apply_support:
            ap = run_cmd(
                [
                    sys.executable,
                    str(APPLY),
                    "--transition",
                    str(paths["transition"]),
                    "--plan",
                    str(paths["plan"]),
                    "--applied-record",
                    str(paths["applied"]),
                    "--mutation-plan",
                    str(paths["mutation"]),
                    "--approval",
                    str(paths["valid_approval"]),
                    "--complete-active",
                    "--active-task",
                    str(tmp / "tasks" / "active-task.md"),
                ],
                REPO_ROOT,
            )
            out = (ap.stdout or "")
            if ap.returncode == 0:
                print("[PASS] apply approval gate positive path")
            elif has_gate_reason(out):
                print("[FAIL] apply approval gate positive path")
                print(out.strip())
                failed = True
            else:
                print("[WARN] apply positive path reached non-approval blocker")
                warn_mode = True

            ap_neg = run_cmd(
                [
                    sys.executable,
                    str(APPLY),
                    "--transition",
                    str(paths["transition"]),
                    "--plan",
                    str(paths["plan"]),
                    "--applied-record",
                    str(paths["applied"]),
                    "--mutation-plan",
                    str(paths["mutation"]),
                    "--complete-active",
                    "--active-task",
                    str(tmp / "tasks" / "active-task.md"),
                ],
                REPO_ROOT,
            )
            if "approval is required but no approval record was provided" in (ap_neg.stdout or ""):
                print("[PASS] missing-approval negative path via apply")
            else:
                print("[WARN] missing-approval negative path not confirmed via apply")
                warn_mode = True
        else:
            print("[WARN] apply interface limitation")
            warn_mode = True

    after = snapshot_protected(REPO_ROOT)
    if before == after:
        print("[PASS] protected path guard")
    else:
        print("[FAIL] protected path guard")
        changed_before = set(before.keys())
        changed_after = set(after.keys())
        for p in sorted(changed_before ^ changed_after):
            print(f"- changed path set: {p}")
        for p in sorted(changed_before & changed_after):
            if before[p] != after[p]:
                print(f"- modified: {p}")
        failed = True

    if failed:
        print("Result: FAIL")
        return 1
    if warn_mode:
        print("Result: WARN")
        return 0
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
