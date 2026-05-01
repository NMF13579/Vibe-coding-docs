#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

SUPPORTED_RISK_CLASSES = {
    "READ_ONLY",
    "VALIDATION",
    "AUDIT",
    "PLAN",
    "DRY_RUN",
    "TEMP_WORKSPACE_MUTATION",
    "REAL_LIFECYCLE_MUTATION",
    "UNSUPPORTED_MUTATION",
    "FORBIDDEN_MUTATION",
}

SUPPORTED_POLICY_RESULTS = {
    "APPROVAL_NOT_REQUIRED",
    "APPROVAL_REQUIRED",
    "APPROVAL_NOT_APPLICABLE",
    "BLOCKED_UNSUPPORTED",
    "BLOCKED_FORBIDDEN",
}

REQUIRED_FIELDS = [
    "policy_case_id",
    "operation_name",
    "risk_class",
    "writes_real_repository_state",
    "invokes_irreversible_command",
    "temp_workspace_isolated",
    "cleanup_performed",
    "supported_operation",
    "target_state_supported",
    "expected_policy_result",
    "expected_policy_decision",
]


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, ["missing frontmatter start"]

    data: dict[str, str] = {}
    end_found = False
    for line in lines[1:]:
        if line.strip() == "---":
            end_found = True
            break
        if not line.strip():
            continue
        if line.startswith(" ") or line.startswith("\t"):
            errors.append("nested yaml is not supported")
            continue
        if ":" not in line:
            errors.append("invalid frontmatter line")
            continue
        k, v = line.split(":", 1)
        key = k.strip()
        val = v.strip()
        if len(val) >= 2 and ((val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'")):
            val = val[1:-1]
        data[key] = val

    if not end_found:
        errors.append("missing frontmatter end")

    return data, errors


def parse_bool(raw: str, field: str, errors: list[str]) -> bool:
    low = raw.strip().lower()
    if low == "true":
        return True
    if low == "false":
        return False
    errors.append(f"invalid boolean for {field}")
    return False


def map_policy(fields: dict[str, str], errors: list[str]) -> tuple[str, str]:
    risk_class = fields.get("risk_class", "")

    if risk_class not in SUPPORTED_RISK_CLASSES:
        return "BLOCKED_UNSUPPORTED", "BLOCKED"

    writes_real = parse_bool(fields["writes_real_repository_state"], "writes_real_repository_state", errors)
    irreversible = parse_bool(fields["invokes_irreversible_command"], "invokes_irreversible_command", errors)
    isolated = parse_bool(fields["temp_workspace_isolated"], "temp_workspace_isolated", errors)
    cleanup = parse_bool(fields["cleanup_performed"], "cleanup_performed", errors)
    supported_operation = parse_bool(fields["supported_operation"], "supported_operation", errors)
    target_state_supported = parse_bool(fields["target_state_supported"], "target_state_supported", errors)

    if errors:
        return "BLOCKED_UNSUPPORTED", "BLOCKED"

    if risk_class == "READ_ONLY":
        result = "APPROVAL_NOT_REQUIRED"
    elif risk_class == "VALIDATION":
        result = "APPROVAL_NOT_REQUIRED"
    elif risk_class == "AUDIT":
        result = "APPROVAL_NOT_APPLICABLE"
    elif risk_class == "PLAN":
        result = "APPROVAL_NOT_REQUIRED"
    elif risk_class == "DRY_RUN":
        if irreversible:
            result = "BLOCKED_FORBIDDEN"
        elif writes_real:
            if supported_operation and target_state_supported:
                result = "APPROVAL_REQUIRED"
            else:
                result = "BLOCKED_UNSUPPORTED"
        else:
            result = "APPROVAL_NOT_REQUIRED"
    elif risk_class == "TEMP_WORKSPACE_MUTATION":
        if isolated and cleanup:
            result = "APPROVAL_NOT_REQUIRED"
        else:
            result = "BLOCKED_UNSUPPORTED"
    elif risk_class == "REAL_LIFECYCLE_MUTATION":
        if supported_operation and target_state_supported:
            result = "APPROVAL_REQUIRED"
        else:
            result = "BLOCKED_UNSUPPORTED"
    elif risk_class == "UNSUPPORTED_MUTATION":
        result = "BLOCKED_UNSUPPORTED"
    else:
        result = "BLOCKED_FORBIDDEN"

    decision = "PASS" if result in {"APPROVAL_NOT_REQUIRED", "APPROVAL_REQUIRED", "APPROVAL_NOT_APPLICABLE"} else "BLOCKED"
    return result, decision


def main(argv: list[str]) -> int:
    if len(argv) != 1 or argv[0] in {"-h", "--help"}:
        print("usage: python3 scripts/validate-policy.py <policy-case-file>")
        return 1

    path = Path(argv[0])
    if not path.is_file():
        print("POLICY_RESULT: BLOCKED_UNSUPPORTED")
        print("POLICY_DECISION: BLOCKED")
        print("VALIDATION: BLOCKED")
        return 1

    fields, errors = parse_frontmatter(path)

    for req in REQUIRED_FIELDS:
        if req not in fields or fields[req].strip() == "":
            errors.append(f"missing required field: {req}")

    result = "BLOCKED_UNSUPPORTED"
    decision = "BLOCKED"

    if not errors:
        expected_result = fields.get("expected_policy_result", "")
        expected_decision = fields.get("expected_policy_decision", "")

        if expected_result not in SUPPORTED_POLICY_RESULTS:
            errors.append("expected_policy_result is not supported")
        if expected_decision not in {"PASS", "BLOCKED"}:
            errors.append("expected_policy_decision is invalid")

        if not errors:
            result, decision = map_policy(fields, errors)
            if result not in SUPPORTED_POLICY_RESULTS:
                errors.append("computed policy result is invalid")

            if not errors:
                if result != expected_result:
                    errors.append("expected_policy_result mismatch")
                if decision != expected_decision:
                    errors.append("expected_policy_decision mismatch")

    if errors:
        if result not in SUPPORTED_POLICY_RESULTS:
            result = "BLOCKED_UNSUPPORTED"
        decision = "BLOCKED"
        print(f"POLICY_RESULT: {result}")
        print(f"POLICY_DECISION: {decision}")
        print("VALIDATION: BLOCKED")
        return 1

    print(f"POLICY_RESULT: {result}")
    print(f"POLICY_DECISION: {decision}")
    print("VALIDATION: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
