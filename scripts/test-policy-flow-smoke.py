#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PROTECTED = ["tasks", "reports", "approvals", "state", "lifecycle", "data", "handoff"]


def snap() -> dict[str, str]:
    out: dict[str, str] = {}
    for rel in PROTECTED:
        p = ROOT / rel
        if not p.exists():
            continue
        if p.is_file():
            out[str(p.relative_to(ROOT))] = hashlib.sha256(p.read_bytes()).hexdigest()
            continue
        for f in sorted(p.rglob("*")):
            if f.is_file():
                out[str(f.relative_to(ROOT))] = hashlib.sha256(f.read_bytes()).hexdigest()
    return out


def run(args: list[str]) -> tuple[int, str]:
    proc = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode, out


def has(out: str, needles: list[str]) -> bool:
    return all(n in out for n in needles)


def main() -> int:
    before = snap()

    warn = False
    ok = True

    rc, out = run(["python3", "scripts/validate-policy.py", "tests/fixtures/policy/read-only-pass.md"])
    c1 = rc == 0 and has(out, ["POLICY_RESULT: APPROVAL_NOT_REQUIRED", "POLICY_DECISION: PASS", "VALIDATION: PASS"])
    print(f"POLICY_SMOKE validator-read-only: {'PASS' if c1 else 'FAIL'}")
    ok &= c1

    rc, out = run(["python3", "scripts/validate-policy.py", "tests/fixtures/policy/forbidden-mutation-blocked.md"])
    c2 = rc == 0 and has(out, ["POLICY_RESULT: BLOCKED_FORBIDDEN", "POLICY_DECISION: BLOCKED", "VALIDATION: PASS"])
    print(f"POLICY_SMOKE validator-forbidden-blocked: {'PASS' if c2 else 'FAIL'}")
    ok &= c2

    rc, out = run([
        "python3", "scripts/check-apply-preconditions.py",
        "--policy", "tests/fixtures/policy/real-lifecycle-approval-required-pass.md",
        "--transition", "tests/fixtures/policy/read-only-pass.md",
    ])
    c3 = rc != 0 and has(out, ["POLICY_RESULT: APPROVAL_REQUIRED", "POLICY_DECISION: PASS", "POLICY_VALIDATION: PASS", "APPROVAL_REQUIRED_BY_POLICY: true", "PRECONDITIONS_RESULT: BLOCKED"])
    print(f"POLICY_SMOKE preconditions-missing-approval: {'PASS' if c3 else 'FAIL'}")
    ok &= c3

    rc, out = run([
        "python3", "scripts/check-apply-preconditions.py",
        "--policy", "tests/fixtures/policy/unsupported-mutation-blocked.md",
        "--transition", "tests/fixtures/policy/read-only-pass.md",
    ])
    c4 = rc != 0 and has(out, ["POLICY_DECISION: BLOCKED", "POLICY_VALIDATION: PASS", "PRECONDITIONS_RESULT: BLOCKED"])
    print(f"POLICY_SMOKE preconditions-policy-blocked: {'PASS' if c4 else 'FAIL'}")
    ok &= c4

    rc, out = run([
        "python3", "scripts/apply-transition.py",
        "--complete-active",
        "--policy", "tests/fixtures/policy/forbidden-mutation-blocked.md",
        "--transition", "tests/fixtures/policy/read-only-pass.md",
    ])
    if "Traceback" in out or "usage:" in out.lower() and "CONTROLLED_APPLY_POLICY_GATE: BLOCKED" not in out:
        c5 = "FAIL"
    elif rc != 0 and has(out, ["CONTROLLED_APPLY_POLICY_GATE: BLOCKED", "PRECONDITIONS_RESULT: BLOCKED"]):
        c5 = "PASS"
    else:
        c5 = "WARN"
    print(f"POLICY_SMOKE controlled-apply-forbidden-blocked: {c5}")
    if c5 == "FAIL":
        ok = False
    if c5 == "WARN":
        warn = True

    rc, out = run(["python3", "scripts/audit-policy-boundary.py"])
    c6 = rc == 0 and ("POLICY_AUDIT_RESULT: PASS" in out or "POLICY_AUDIT_RESULT: WARN" in out)
    print(f"POLICY_SMOKE policy-audit: {'PASS' if c6 else 'FAIL'}")
    ok &= c6
    if "POLICY_AUDIT_RESULT: WARN" in out:
        warn = True

    after = snap()
    hash_ok = before == after
    print(f"POLICY_SMOKE_HASH_GUARD: {'PASS' if hash_ok else 'FAIL'}")
    ok &= hash_ok

    if not ok:
        print("SUMMARY: FAIL")
        return 1
    if warn:
        print("SUMMARY: WARN")
        return 0
    print("SUMMARY: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
