#!/usr/bin/env python3
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

POLICY_NON_PASS = {
    "unsupported-mutation-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "forbidden-mutation-blocked.md": ("BLOCKED_FORBIDDEN", "BLOCKED"),
    "temp-workspace-not-isolated-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "temp-workspace-no-cleanup-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "real-lifecycle-unsupported-operation-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "real-lifecycle-unsupported-target-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "dry-run-writes-real-repo-supported-approval-required.md": ("APPROVAL_REQUIRED", "PASS"),
    "dry-run-writes-real-repo-unsupported-blocked.md": ("BLOCKED_UNSUPPORTED", "BLOCKED"),
    "dry-run-irreversible-command-forbidden.md": ("BLOCKED_FORBIDDEN", "BLOCKED"),
}

MALFORMED = [
    "unknown-risk-class-malformed.md",
    "missing-risk-class-malformed.md",
    "bad-boolean-malformed.md",
    "missing-expected-result-malformed.md",
    "approval-optional-rejected-malformed.md",
    "nested-yaml-malformed.md",
]

ALL = list(POLICY_NON_PASS.keys()) + MALFORMED


def parse_line_value(stdout: str, key: str) -> str:
    prefix = f"{key}:"
    for line in stdout.splitlines():
        if line.startswith(prefix):
            return line.split(":", 1)[1].strip()
    return ""


def run_fixture(repo_root: Path, filename: str) -> tuple[bool, str]:
    fixture_path = repo_root / "tests" / "fixtures" / "policy" / filename
    if not fixture_path.is_file():
        return False, "missing fixture"

    cmd = [sys.executable, "scripts/validate-policy.py", str(fixture_path)]
    proc = subprocess.run(cmd, cwd=repo_root, capture_output=True, text=True)
    stdout = proc.stdout

    policy_result = parse_line_value(stdout, "POLICY_RESULT")
    policy_decision = parse_line_value(stdout, "POLICY_DECISION")
    validation = parse_line_value(stdout, "VALIDATION")

    if filename in POLICY_NON_PASS:
        expected_result, expected_decision = POLICY_NON_PASS[filename]
        if proc.returncode != 0:
            return False, f"expected exit 0, got {proc.returncode}"
        if policy_result != expected_result:
            return False, f"expected POLICY_RESULT {expected_result}, got {policy_result or 'missing'}"
        if policy_decision != expected_decision:
            return False, f"expected POLICY_DECISION {expected_decision}, got {policy_decision or 'missing'}"
        if validation != "PASS":
            return False, f"expected VALIDATION PASS, got {validation or 'missing'}"
        return True, "ok"

    if proc.returncode == 0:
        return False, "expected non-zero exit for malformed fixture"
    if validation != "BLOCKED":
        return False, f"expected VALIDATION BLOCKED, got {validation or 'missing'}"
    if policy_decision and policy_decision != "BLOCKED":
        return False, f"expected POLICY_DECISION BLOCKED if emitted, got {policy_decision}"
    return True, "ok"


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    all_ok = True

    for filename in ALL:
        ok, _reason = run_fixture(repo_root, filename)
        if ok:
            print(f"POLICY_FIXTURE {filename}: PASS")
        else:
            print(f"POLICY_FIXTURE {filename}: FAIL")
            all_ok = False

    if all_ok:
        print("SUMMARY: PASS")
        return 0

    print("SUMMARY: FAIL")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
