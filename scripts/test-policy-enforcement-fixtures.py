#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

PROTECTED_STATE_HASH_GUARD = "PROTECTED_STATE_HASH_GUARD"

REPO_ROOT = Path(__file__).resolve().parent.parent

MIN_PROTECTED_DIRS = [
    "tasks",
    "reports",
    "approvals",
    "state",
    "lifecycle",
    "data",
    "handoff",
]

EXTENDED_PROTECTED_PATHS = [
    "tasks/active-task.md",
    "tasks/done",
    "tasks/completed",
]


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def snapshot() -> dict[str, str]:
    out: dict[str, str] = {}

    for rel in MIN_PROTECTED_DIRS:
        root = REPO_ROOT / rel
        if not root.exists():
            continue
        if root.is_file():
            out[str(root.relative_to(REPO_ROOT))] = file_hash(root)
            continue
        for p in sorted(root.rglob("*")):
            if p.is_file():
                out[str(p.relative_to(REPO_ROOT))] = file_hash(p)

    for rel in EXTENDED_PROTECTED_PATHS:
        p = REPO_ROOT / rel
        if not p.exists():
            continue
        if p.is_file():
            out[str(p.relative_to(REPO_ROOT))] = file_hash(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file():
                    out[str(f.relative_to(REPO_ROOT))] = file_hash(f)

    return out


def run_cmd(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(args, cwd=REPO_ROOT, capture_output=True, text=True)
    return proc.returncode, (proc.stdout or "") + (proc.stderr or "")


def generic_cli_only_failure(output: str) -> bool:
    low = output.lower()
    has_gate = "controlled_apply_policy_gate: blocked" in low and "preconditions_result: blocked" in low
    if has_gate:
        return False
    return (
        "usage:" in low
        or "traceback" in low
        or "error:" in low
        or "no such file" in low
        or "not found" in low
    )


def required_case(name: str, policy_fixture: str, required_markers: list[str]) -> bool:
    cmd = [
        "python3",
        "scripts/apply-transition.py",
        "--complete-active",
        "--policy",
        policy_fixture,
        "--transition",
        "tests/fixtures/policy/read-only-pass.md",
    ]
    rc, out = run_cmd(cmd)

    ok = True
    if rc == 0:
        ok = False
    if "Traceback" in out:
        ok = False
    if generic_cli_only_failure(out):
        ok = False
    for marker in [
        "CONTROLLED_APPLY_POLICY_GATE: BLOCKED",
        "PRECONDITIONS_RESULT: BLOCKED",
        *required_markers,
    ]:
        if marker not in out:
            ok = False

    print(f"POLICY_ENFORCEMENT {name}: {'PASS' if ok else 'FAIL'}")
    return ok


def case_non_controlled_policy_isolation() -> str:
    rc_help, out_help = run_cmd(["python3", "scripts/apply-transition.py", "--help"])
    if rc_help != 0:
        print("POLICY_ENFORCEMENT non-controlled-policy-isolation: WARN")
        return "WARN"

    if "--dry-run" not in out_help:
        print("POLICY_ENFORCEMENT non-controlled-policy-isolation: WARN")
        return "WARN"

    rc, out = run_cmd([
        "python3",
        "scripts/apply-transition.py",
        "--dry-run",
        "--policy",
        "tests/fixtures/policy/unsupported-mutation-blocked.md",
        "--transition",
        "tests/fixtures/policy/read-only-pass.md",
    ])

    # For non-controlled mode we only assert no policy-gate marker leaked.
    ok = "CONTROLLED_APPLY_POLICY_GATE" not in out
    if ok:
        print("POLICY_ENFORCEMENT non-controlled-policy-isolation: PASS")
        return "PASS"

    print("POLICY_ENFORCEMENT non-controlled-policy-isolation: WARN")
    return "WARN"


def main() -> int:
    before = snapshot()

    req_ok = True
    req_ok &= required_case(
        "unsupported-mutation-blocked",
        "tests/fixtures/policy/unsupported-mutation-blocked.md",
        ["POLICY_DECISION: BLOCKED"],
    )
    req_ok &= required_case(
        "forbidden-mutation-blocked",
        "tests/fixtures/policy/forbidden-mutation-blocked.md",
        ["POLICY_RESULT: BLOCKED_FORBIDDEN", "POLICY_DECISION: BLOCKED"],
    )
    req_ok &= required_case(
        "approval-required-missing-approval",
        "tests/fixtures/policy/real-lifecycle-approval-required-pass.md",
        ["APPROVAL_REQUIRED_BY_POLICY: true"],
    )
    req_ok &= required_case(
        "dry-run-irreversible-command",
        "tests/fixtures/policy/dry-run-irreversible-command-forbidden.md",
        ["POLICY_RESULT: BLOCKED_FORBIDDEN", "POLICY_DECISION: BLOCKED"],
    )

    case5 = case_non_controlled_policy_isolation()

    after = snapshot()
    hash_ok = before == after
    print(f"{PROTECTED_STATE_HASH_GUARD}: {'PASS' if hash_ok else 'FAIL'}")

    if not req_ok or not hash_ok:
        print("SUMMARY: FAIL")
        return 1

    if case5 == "WARN":
        print("SUMMARY: WARN")
        return 0

    print("SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
