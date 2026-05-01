#!/usr/bin/env python3

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = REPO_ROOT / "scripts" / "validate-human-approval.py"
FIXTURE_DIR = REPO_ROOT / "tests" / "fixtures" / "human-approval"

CASES = [
    # From 17.3.1
    ("valid-complete-active.md", 0, "PASS", None),
    ("invalid-vague-approval.md", 1, "BLOCKED", "approval_statement is vague"),
    ("invalid-missing-required-field.md", 1, "BLOCKED", "required field missing or empty: approved_by"),
    ("invalid-unsupported-operation.md", 1, "BLOCKED", "allowed_operation is not supported"),
    ("invalid-unsupported-target-state.md", 1, "BLOCKED", "allowed_target_state is not supported"),
    ("invalid-nested-yaml.md", 1, "BLOCKED", None),
    ("invalid-expired-status.md", 1, "BLOCKED", "approval_status is expired"),

    # From 17.4.1
    ("invalid-missing-approval-scope.md", 1, "BLOCKED", "required field missing or empty: approval_scope"),
    ("invalid-missing-related-task-id.md", 1, "BLOCKED", "required field missing or empty: related_task_id"),
    ("invalid-missing-related-transition-id.md", 1, "BLOCKED", "required field missing or empty: related_transition_id"),
    ("invalid-vague-continue.md", 1, "BLOCKED", "approval_statement is vague"),
    ("invalid-approved-by-agent.md", 1, "BLOCKED", "approved_by identifies a known non-human identity"),
    ("invalid-approved-by-openai-exact.md", 1, "BLOCKED", "approved_by identifies a known non-human identity"),
    ("valid-approved-by-openai-substring.md", 0, "PASS", None),
    ("invalid-generic-scope-all.md", 1, "BLOCKED", "approval_scope is too generic"),
    ("invalid-bypass-preconditions.md", 1, "BLOCKED", "approval_statement contains bypass claim"),
    ("invalid-statement-missing-task-reference.md", 1, "BLOCKED", "approval_statement does not reference related_task_id"),
    ("invalid-statement-missing-transition-reference.md", 1, "BLOCKED", "approval_statement does not reference related_transition_id"),
    ("invalid-statement-missing-operation-reference.md", 1, "BLOCKED", "approval_statement does not reference allowed operation"),
    ("invalid-statement-missing-target-state-reference.md", 1, "BLOCKED", "approval_statement does not reference allowed target state"),
    ("invalid-approval-id-task-mismatch.md", 1, "BLOCKED", "approval_id does not reference related_task_id"),
    ("invalid-approval-id-operation-mismatch.md", 1, "BLOCKED", "approval_id does not reference allowed_operation"),
    ("invalid-related-task-id-format.md", 1, "BLOCKED", "related_task_id format is invalid"),
    ("invalid-related-transition-id-format.md", 1, "BLOCKED", "related_transition_id format is invalid"),
    ("invalid-approved-at-format.md", 1, "BLOCKED", "approved_at is not a valid ISO 8601 timestamp"),
    ("invalid-expires-at-format.md", 1, "BLOCKED", "expires_at is not a valid ISO 8601 timestamp"),
    ("invalid-superseded-status.md", 1, "BLOCKED", "approval_status is superseded"),
    ("invalid-revoked-status.md", 1, "BLOCKED", "approval_status is revoked"),
    ("invalid-approval-status-invalid.md", 1, "BLOCKED", "approval_status is invalid"),
    ("invalid-unknown-status.md", 1, "BLOCKED", "approval_status is not an allowed value"),
    ("invalid-unknown-approval-source.md", 1, "BLOCKED", "approval_source is not an allowed value"),
    ("invalid-supersedes-format.md", 1, "BLOCKED", "supersedes does not look like a valid approval_id"),
]


def run_case(name: str, expected_code: int, expected_result: str, expected_reason: str | None) -> list[str]:
    errors: list[str] = []
    fixture = FIXTURE_DIR / name
    if not fixture.is_file():
        return [f"{name}: fixture file not found"]

    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(fixture)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "").strip()

    if proc.returncode != expected_code:
        errors.append(f"{name}: expected exit code {expected_code}, got {proc.returncode}")

    if expected_result not in out:
        errors.append(f"{name}: expected result text '{expected_result}' not found")

    if expected_reason is not None and expected_reason not in out:
        errors.append(f"{name}: expected reason not found: {expected_reason}")

    if errors:
        errors.append(f"{name}: actual output: {out or '<empty>'}")
    return errors


def main() -> int:
    if not VALIDATOR.is_file():
        print("BLOCKED")
        print("- scripts/validate-human-approval.py not found")
        return 1

    if not FIXTURE_DIR.is_dir():
        print("BLOCKED")
        print("- tests/fixtures/human-approval/ directory not found")
        return 1

    failures: list[str] = []

    for name, code, result_text, reason in CASES:
        errs = run_case(name, code, result_text, reason)
        if not errs:
            if reason is None:
                print(f"PASS   {name}")
            else:
                print(f"PASS   {name} -> BLOCKED reason matched")
        else:
            print(f"FAILED {name}")
            for e in errs:
                print(f"       {e}")
            failures.extend(errs)

    if failures:
        print("BLOCKED")
        for f in failures:
            print(f"- {f}")
        return 1

    print(f"All {len(CASES)} fixtures passed.")
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
