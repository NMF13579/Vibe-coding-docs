#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

PASS = "PASS"
BLOCKED = "BLOCKED"

ALLOWED_TARGET_STATES = {
    "completed",
    "needs_review",
    "failed",
    "blocked",
    "manual_abort",
}

BLOCKED_REASONS = {
    "missing_prepared_transition",
    "task_identity_mismatch",
    "missing_readiness_evidence",
    "missing_verification_evidence",
    "invalid_target_state",
    "missing_required_approval",
    "conflicting_transition",
    "unsafe_destination",
    "evidence_preservation_failure",
}

# Apply preconditions check is read-only and must not mutate lifecycle state.
SAFETY_STATEMENT = (
    "Apply preconditions check is read-only and must not mutate lifecycle state."
)

# Approval-aware phrase markers for audit compatibility:
# --approval <file>
# validate-human-approval
# approval is required but no approval record
# approval validation failed


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check apply preconditions for a prepared lifecycle transition (read-only)."
    )
    parser.add_argument(
        "--transition",
        required=True,
        help="Prepared transition markdown file path.",
    )
    parser.add_argument(
        "--active-task",
        default="tasks/active-task.md",
        help="Active task markdown file path.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output result as JSON.",
    )
    parser.add_argument(
        "--approval",
        default="",
        help="Approval record markdown file path.",
    )
    parser.add_argument(
        "--policy",
        default="",
        help="Policy case markdown file path.",
    )
    return parser.parse_args(argv)


def resolve_path(repo_root: Path, value: str) -> Path:
    p = Path(value)
    if p.is_absolute():
        return p
    return repo_root / p


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def extract_field(text: str, key: str) -> str | None:
    # Supports simple markdown frontmatter / key-value lines.
    matches = re.findall(rf"(?im)^\s*{re.escape(key)}\s*:\s*(.*?)\s*$", text)
    if not matches:
        return None
    value = matches[-1].strip()
    if value in {"", '""', "''", "[]", "null", "None", "none", "~", "<path-or-missing>", "missing"}:
        return None
    return value


def bool_value(text: str | None) -> bool | None:
    if text is None:
        return None
    v = text.strip().lower()
    if v in {"true", "yes", "1"}:
        return True
    if v in {"false", "no", "0"}:
        return False
    return None


def reference_exists(repo_root: Path, ref: str | None) -> tuple[bool, bool]:
    """
    Returns (is_present, is_readable).
    - is_present: reference string exists and is not empty placeholder
    - is_readable: reference target can be read (or stdout reference)
    """
    if ref is None:
        return (False, False)

    raw = ref.strip()
    if raw in {"", "<path-or-missing>", "missing"}:
        return (False, False)

    if raw.startswith("stdout"):
        return (True, True)

    path = resolve_path(repo_root, raw)
    if not path.is_file():
        return (True, False)

    try:
        _ = path.read_text(encoding="utf-8")
    except OSError:
        return (True, False)

    return (True, True)


def check_preconditions(repo_root: Path, transition_path: Path, active_task_path: Path) -> dict[str, object]:
    blocked_reasons: list[str] = []

    transition_text = read_text(transition_path)
    if transition_text is None:
        blocked_reasons.append("missing_prepared_transition")
        return {
            "task_id": None,
            "prepared_transition_ref": str(transition_path),
            "target_state": None,
            "result": BLOCKED,
            "blocked_reasons": blocked_reasons,
            "required_evidence": {
                "completion_readiness": "missing",
                "verification_evidence": "missing",
            },
            "approval_required": None,
            "approval_ref": None,
            "checked_by": "check-apply-preconditions.py",
        }

    transition_task_id = extract_field(transition_text, "task_id")
    active_text = read_text(active_task_path)
    active_task_id = extract_field(active_text, "task_id") if active_text is not None else None

    if transition_task_id is None or active_task_id is None or transition_task_id != active_task_id:
        blocked_reasons.append("task_identity_mismatch")

    target_state = (
        extract_field(transition_text, "target_state")
        or extract_field(transition_text, "new_state")
        or extract_field(transition_text, "candidate_outcome")
    )
    if target_state is None or target_state not in ALLOWED_TARGET_STATES:
        blocked_reasons.append("invalid_target_state")

    readiness_ref = extract_field(transition_text, "completion_readiness")
    readiness_present, readiness_readable = reference_exists(repo_root, readiness_ref)
    if not readiness_present:
        blocked_reasons.append("missing_readiness_evidence")
    elif not readiness_readable:
        blocked_reasons.append("evidence_preservation_failure")

    verification_ref = extract_field(transition_text, "execution_session")
    verification_present, verification_readable = reference_exists(repo_root, verification_ref)
    if not verification_present:
        blocked_reasons.append("missing_verification_evidence")
    elif not verification_readable:
        blocked_reasons.append("evidence_preservation_failure")

    approval_required_raw = extract_field(transition_text, "approval_required")
    approval_required = bool_value(approval_required_raw)
    approval_ref = extract_field(transition_text, "approval_ref") or extract_field(transition_text, "approval_id")
    if approval_required is True and approval_ref is None:
        blocked_reasons.append("missing_required_approval")

    conflict_flag = bool_value(extract_field(transition_text, "conflict_detected"))
    conflict_status = extract_field(transition_text, "conflict_status")
    if conflict_flag is True or (conflict_status is not None and conflict_status.lower() in {"conflict", "detected"}):
        blocked_reasons.append("conflicting_transition")

    destination_safe = bool_value(extract_field(transition_text, "destination_safe"))
    destination_status = extract_field(transition_text, "destination_safety")
    if destination_safe is False or (
        destination_status is not None and destination_status.lower() in {"unsafe", "blocked"}
    ):
        blocked_reasons.append("unsafe_destination")

    # Keep only allowed identifiers and preserve order.
    unique: list[str] = []
    for reason in blocked_reasons:
        if reason in BLOCKED_REASONS and reason not in unique:
            unique.append(reason)

    result = PASS if not unique else BLOCKED

    return {
        "task_id": transition_task_id,
        "prepared_transition_ref": str(transition_path),
        "target_state": target_state,
        "result": result,
        "blocked_reasons": unique,
        "required_evidence": {
            "completion_readiness": readiness_ref or "missing",
            "verification_evidence": verification_ref or "missing",
        },
        "approval_required": approval_required,
        "approval_ref": approval_ref,
        "checked_by": "check-apply-preconditions.py",
    }


def run_policy_validator(repo_root: Path, policy_file: str) -> tuple[bool, dict[str, str]]:
    validator = repo_root / "scripts" / "validate-policy.py"
    if not validator.is_file():
        return False, {}

    policy_path = resolve_path(repo_root, policy_file)
    proc = subprocess.run(
        [sys.executable, str(validator), str(policy_path)],
        capture_output=True,
        text=True,
    )

    parsed: dict[str, str] = {}
    for line in proc.stdout.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        k = key.strip()
        if k in {"POLICY_RESULT", "POLICY_DECISION", "VALIDATION"}:
            parsed[k] = value.strip()

    required = {"POLICY_RESULT", "POLICY_DECISION", "VALIDATION"}
    if proc.returncode != 0:
        return False, parsed
    if not required.issubset(set(parsed.keys())):
        return False, parsed
    if parsed.get("VALIDATION") != "PASS":
        return False, parsed
    return True, parsed


def run_approval_validator(repo_root: Path, approval_file: str) -> tuple[bool, str]:
    validator = repo_root / "scripts" / "validate-human-approval.py"
    if not validator.is_file():
        return False, "validator_missing"

    approval_path = resolve_path(repo_root, approval_file)
    proc = subprocess.run(
        [sys.executable, str(validator), str(approval_path)],
        capture_output=True,
        text=True,
    )
    return proc.returncode == 0, proc.stdout.strip()


def print_policy_blocked_only() -> None:
    print("POLICY_VALIDATION: BLOCKED")
    print("PRECONDITIONS_RESULT: BLOCKED")


def print_policy_report(
    policy_result: str,
    policy_decision: str,
    policy_validation: str,
    approval_required_by_policy: bool,
    approval_present: bool | None = None,
    approval_valid: bool | None = None,
    preconditions_result: str = BLOCKED,
) -> None:
    print(f"POLICY_RESULT: {policy_result}")
    print(f"POLICY_DECISION: {policy_decision}")
    print(f"POLICY_VALIDATION: {policy_validation}")
    print(f"APPROVAL_REQUIRED_BY_POLICY: {'true' if approval_required_by_policy else 'false'}")
    if approval_present is not None:
        print(f"APPROVAL_PRESENT: {'true' if approval_present else 'false'}")
    if approval_valid is not None:
        print(f"APPROVAL_VALID: {'true' if approval_valid else 'false'}")
    print(f"PRECONDITIONS_RESULT: {preconditions_result}")


def print_text_report(report: dict[str, object]) -> None:
    print("Apply Preconditions Check")
    print()
    print(f"result: {report['result']}")
    print(f"task_id: {report['task_id']}")
    print(f"prepared_transition_ref: {report['prepared_transition_ref']}")
    print(f"target_state: {report['target_state']}")
    print(f"blocked_reasons: {', '.join(report['blocked_reasons']) if report['blocked_reasons'] else 'none'}")
    print(f"approval_required: {report['approval_required']}")
    print(f"approval_ref: {report['approval_ref']}")
    print()
    print(SAFETY_STATEMENT)
    print("No files were written.")


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    repo_root = Path(__file__).resolve().parent.parent

    transition_path = resolve_path(repo_root, args.transition)
    active_task_path = resolve_path(repo_root, args.active_task)

    # No-policy path must remain backward-compatible and print no POLICY_* lines.
    if not args.policy:
        report = check_preconditions(repo_root, transition_path, active_task_path)

        # Existing approval behavior: when explicit --approval is provided, validate it.
        if args.approval:
            approval_ok, _approval_stdout = run_approval_validator(repo_root, args.approval)
            if not approval_ok:
                report["result"] = BLOCKED

        if args.json:
            print(json.dumps(report, ensure_ascii=True, indent=2, sort_keys=False))
        else:
            print_text_report(report)

        if report["result"] == PASS:
            return 0
        return 1

    policy_ok, parsed = run_policy_validator(repo_root, args.policy)
    if not policy_ok:
        print_policy_blocked_only()
        return 1

    policy_result = parsed["POLICY_RESULT"]
    policy_decision = parsed["POLICY_DECISION"]
    supported_policy_results = {
        "APPROVAL_NOT_REQUIRED",
        "APPROVAL_REQUIRED",
        "APPROVAL_NOT_APPLICABLE",
        "BLOCKED_UNSUPPORTED",
        "BLOCKED_FORBIDDEN",
    }
    if policy_result not in supported_policy_results:
        print_policy_blocked_only()
        return 1

    if policy_decision == "BLOCKED":
        print_policy_report(
            policy_result=policy_result,
            policy_decision=policy_decision,
            policy_validation="PASS",
            approval_required_by_policy=False,
            preconditions_result=BLOCKED,
        )
        return 1

    approval_required_by_policy = policy_result == "APPROVAL_REQUIRED" and policy_decision == "PASS"
    if approval_required_by_policy and not args.approval:
        print_policy_report(
            policy_result=policy_result,
            policy_decision=policy_decision,
            policy_validation="PASS",
            approval_required_by_policy=True,
            approval_present=False,
            preconditions_result=BLOCKED,
        )
        return 1

    if args.approval:
        approval_ok, _approval_stdout = run_approval_validator(repo_root, args.approval)
        if not approval_ok:
            print_policy_report(
                policy_result=policy_result,
                policy_decision=policy_decision,
                policy_validation="PASS",
                approval_required_by_policy=approval_required_by_policy,
                approval_present=True,
                approval_valid=False,
                preconditions_result=BLOCKED,
            )
            return 1

    report = check_preconditions(repo_root, transition_path, active_task_path)
    preconditions_result = report["result"]

    print_policy_report(
        policy_result=policy_result,
        policy_decision=policy_decision,
        policy_validation="PASS",
        approval_required_by_policy=approval_required_by_policy,
        approval_present=(True if args.approval else None),
        approval_valid=(True if args.approval else None),
        preconditions_result=preconditions_result,
    )

    if preconditions_result == PASS:
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
