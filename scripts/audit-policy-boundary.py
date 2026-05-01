#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent.parent

ARTIFACTS = [
    "docs/OPERATION-RISK-MODEL.md",
    "docs/APPROVAL-REQUIREMENT-POLICY.md",
    "docs/APPLY-PRECONDITIONS.md",
    "docs/APPLY-COMMAND-INTEGRATION.md",
    "scripts/validate-policy.py",
    "scripts/test-policy-fixtures.py",
    "scripts/check-apply-preconditions.py",
    "scripts/apply-transition.py",
    "scripts/test-policy-enforcement-fixtures.py",
    "tests/fixtures/policy-enforcement/README.md",
    "tests/fixtures/policy/",
]

RISK_CLASSES = [
    "READ_ONLY",
    "VALIDATION",
    "AUDIT",
    "PLAN",
    "DRY_RUN",
    "TEMP_WORKSPACE_MUTATION",
    "REAL_LIFECYCLE_MUTATION",
    "UNSUPPORTED_MUTATION",
    "FORBIDDEN_MUTATION",
]

POLICY_RESULTS = [
    "APPROVAL_NOT_REQUIRED",
    "APPROVAL_REQUIRED",
    "APPROVAL_NOT_APPLICABLE",
    "BLOCKED_UNSUPPORTED",
    "BLOCKED_FORBIDDEN",
]

POSITIVE_FIXTURES = [
    "tests/fixtures/policy/read-only-pass.md",
    "tests/fixtures/policy/safe-dry-run-pass.md",
    "tests/fixtures/policy/real-lifecycle-approval-required-pass.md",
]

BLOCKED_FIXTURES = [
    "tests/fixtures/policy/unsupported-mutation-blocked.md",
    "tests/fixtures/policy/forbidden-mutation-blocked.md",
    "tests/fixtures/policy/temp-workspace-not-isolated-blocked.md",
    "tests/fixtures/policy/temp-workspace-no-cleanup-blocked.md",
    "tests/fixtures/policy/real-lifecycle-unsupported-operation-blocked.md",
    "tests/fixtures/policy/real-lifecycle-unsupported-target-blocked.md",
    "tests/fixtures/policy/dry-run-writes-real-repo-unsupported-blocked.md",
    "tests/fixtures/policy/dry-run-irreversible-command-forbidden.md",
]

EDGE_FIXTURE = "tests/fixtures/policy/dry-run-writes-real-repo-supported-approval-required.md"

MALFORMED_FIXTURES = [
    "tests/fixtures/policy/unknown-risk-class-malformed.md",
    "tests/fixtures/policy/missing-risk-class-malformed.md",
    "tests/fixtures/policy/bad-boolean-malformed.md",
    "tests/fixtures/policy/missing-expected-result-malformed.md",
    "tests/fixtures/policy/approval-optional-rejected-malformed.md",
    "tests/fixtures/policy/nested-yaml-malformed.md",
]


def read(rel: str) -> str:
    p = ROOT / rel
    try:
        return p.read_text(encoding="utf-8")
    except OSError:
        return ""


def exists(rel: str) -> bool:
    p = ROOT / rel
    return p.exists()


def contains_all(text: str, needles: list[str]) -> bool:
    return all(n in text for n in needles)


def detail(msg: str) -> None:
    print(f"DETAIL: {msg}")


def check_artifacts() -> str:
    ok = True
    for rel in ARTIFACTS:
        if not exists(rel):
            ok = False
            detail(f"missing artifact {rel}")
    return "PASS" if ok else "FAIL"


def check_risk_model() -> str:
    text = read("docs/OPERATION-RISK-MODEL.md")
    ok = True
    for cls in RISK_CLASSES:
        if cls not in text:
            ok = False
            detail(f"risk class missing: {cls}")
    return "PASS" if ok else "FAIL"


def check_approval_policy() -> str:
    text = read("docs/APPROVAL-REQUIREMENT-POLICY.md")
    ok = True
    for r in POLICY_RESULTS:
        if r not in text:
            ok = False
            detail(f"policy result missing: {r}")
    if "APPROVAL_OPTIONAL" in text:
        ok = False
        detail("found APPROVAL_OPTIONAL in docs/APPROVAL-REQUIREMENT-POLICY.md")
    if "APPROVAL_OPTIONAL" in read("scripts/validate-policy.py"):
        ok = False
        detail("found APPROVAL_OPTIONAL in scripts/validate-policy.py")

    policy_dir = ROOT / "tests/fixtures/policy"
    if policy_dir.exists():
        for f in policy_dir.glob("*.md"):
            t = f.read_text(encoding="utf-8")
            if "APPROVAL_OPTIONAL" in t and f.name != "approval-optional-rejected-malformed.md":
                ok = False
                detail(f"APPROVAL_OPTIONAL not allowed in fixture {f}")
    return "PASS" if ok else "FAIL"


def check_validator() -> str:
    text = read("scripts/validate-policy.py")
    needles = [
        "SUPPORTED_RISK_CLASSES",
        "SUPPORTED_POLICY_RESULTS",
        "DRY_RUN",
        "TEMP_WORKSPACE_MUTATION",
        "REAL_LIFECYCLE_MUTATION",
        "BLOCKED_UNSUPPORTED",
        "BLOCKED_FORBIDDEN",
        "POLICY_RESULT",
        "POLICY_DECISION",
        "VALIDATION",
    ]
    if contains_all(text, needles):
        return "PASS"
    detail("validator evidence missing")
    return "FAIL"


def check_fixtures() -> str:
    fail = False
    warn = False
    all_required = POSITIVE_FIXTURES + BLOCKED_FIXTURES + [EDGE_FIXTURE] + MALFORMED_FIXTURES
    for rel in all_required:
        if not exists(rel):
            fail = True
            detail(f"missing fixture {rel}")

    for rel in BLOCKED_FIXTURES:
        text = read(rel)
        if "expected_policy_decision: BLOCKED" not in text:
            warn = True
            detail(f"fixture exists but expected_policy_decision BLOCKED missing — {rel}")

    edge_text = read(EDGE_FIXTURE)
    if "expected_policy_result: APPROVAL_REQUIRED" not in edge_text or "expected_policy_decision: PASS" not in edge_text:
        warn = True
        detail(f"fixture exists but edge expected fields missing — {EDGE_FIXTURE}")

    if fail:
        return "FAIL"
    if warn:
        return "WARN"
    return "PASS"


def check_preconditions() -> str:
    text = read("scripts/check-apply-preconditions.py")
    needles = [
        "--policy",
        "validate-policy.py",
        "POLICY_RESULT",
        "POLICY_DECISION",
        "POLICY_VALIDATION",
        "APPROVAL_REQUIRED_BY_POLICY",
        "PRECONDITIONS_RESULT",
        "if not args.policy",
        "APPROVAL_REQUIRED",
    ]
    if contains_all(text, needles):
        return "PASS"
    detail("preconditions policy integration evidence missing")
    return "FAIL"


def check_controlled_apply() -> str:
    text = read("scripts/apply-transition.py")
    required_needles = [
        "--policy",
        "--complete-active",
        "check-apply-preconditions.py",
        "CONTROLLED_APPLY_POLICY_GATE",
        "missing_policy_for_complete_active",
        "if args.complete_active and not args.policy",
        "PRECONDITIONS_RESULT: BLOCKED",
        "APPLY_RESULT: BLOCKED",
    ]
    if not contains_all(text, required_needles):
        detail("controlled apply policy integration evidence missing")
        return "FAIL"
    return "PASS"


def check_enforcement() -> str:
    script = read("scripts/test-policy-enforcement-fixtures.py")
    required = [
        "PROTECTED_STATE_HASH_GUARD",
        "CONTROLLED_APPLY_POLICY_GATE",
        "--complete-active",
        "unsupported-mutation-blocked.md",
        "forbidden-mutation-blocked.md",
        "real-lifecycle-approval-required-pass.md",
        "dry-run-irreversible-command-forbidden.md",
        "usage",
        "traceback",
    ]
    if not contains_all(script, required):
        detail("enforcement fixture runner safety evidence missing")
        return "FAIL"

    readme = read("tests/fixtures/policy-enforcement/README.md")
    warn = False
    readme_needles = [
        "PASS-path controlled mutation is not run",
        "Protected paths",
        "SUMMARY: WARN",
        "python3 scripts/test-policy-enforcement-fixtures.py",
    ]
    for n in readme_needles:
        if n not in readme:
            warn = True
            detail(f"README safety note missing: {n}")

    return "WARN" if warn else "PASS"


def check_safety() -> str:
    files = [
        "scripts/validate-policy.py",
        "scripts/check-apply-preconditions.py",
        "scripts/apply-transition.py",
        "scripts/test-policy-enforcement-fixtures.py",
    ]
    risk_phrases = [
        "writing into approvals/",
        "creating approval records",
        "generating approval evidence",
        "bypassing approval validation",
        "overriding policy block",
        "ignoring BLOCKED_FORBIDDEN",
        "ignoring BLOCKED_UNSUPPORTED",
    ]
    uncertain = False
    for rel in files:
        text = read(rel)
        low = text.lower()
        for phrase in risk_phrases:
            if phrase.lower() in low:
                uncertain = True
                detail(f"safety risk phrase found in {rel}: {phrase}")
    return "WARN" if uncertain else "PASS"


def main() -> int:
    results = {
        "POLICY_AUDIT_ARTIFACTS": check_artifacts(),
        "POLICY_AUDIT_RISK_MODEL": check_risk_model(),
        "POLICY_AUDIT_APPROVAL_POLICY": check_approval_policy(),
        "POLICY_AUDIT_VALIDATOR": check_validator(),
        "POLICY_AUDIT_FIXTURES": check_fixtures(),
        "POLICY_AUDIT_PRECONDITIONS": check_preconditions(),
        "POLICY_AUDIT_CONTROLLED_APPLY": check_controlled_apply(),
        "POLICY_AUDIT_ENFORCEMENT": check_enforcement(),
        "POLICY_AUDIT_SAFETY": check_safety(),
    }

    for k, v in results.items():
        print(f"{k}: {v}")

    any_fail = any(v == "FAIL" for v in results.values())
    any_warn = any(v == "WARN" for v in results.values())

    if any_fail:
        final = "FAIL"
    elif any_warn:
        final = "WARN"
    else:
        final = "PASS"

    print(f"POLICY_AUDIT_RESULT: {final}")
    return 1 if final == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
