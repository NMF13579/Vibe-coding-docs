#!/usr/bin/env python3
"""Read-only task state validator for AgentOS."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path


VALID_STATES = {
    "idea",
    "brief_draft",
    "brief_approved",
    "review_ready",
    "review_blocked",
    "trace_written",
    "contract_drafted",
    "approved_for_execution",
    "active",
    "completed",
    "failed",
    "dropped",
}

VALID_ANALYSIS_STATUSES = {"ok", "invalid", "conflict"}
VALID_EVIDENCE_STATUSES = {
    "present",
    "missing",
    "valid",
    "invalid",
    "conflicting",
    "planned",
}
BLOCKED_REVIEW_STATUSES = {
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}
READY_REVIEW_STATUSES = {"READY", "READY_WITH_EDITS"}


def usage() -> None:
    print("Usage: python3 scripts/validate-task-state.py tasks/{task-id}")


def load_detector_report(task_dir: Path) -> tuple[dict | None, str | None]:
    detector_path = Path(__file__).resolve().parent / "detect-task-state.py"

    try:
        completed = subprocess.run(
            [sys.executable, str(detector_path), str(task_dir)],
            cwd=str(detector_path.parent.parent),
            capture_output=True,
            text=True,
        )
        if completed.returncode != 0:
            return None, f"detector exited with code {completed.returncode}"
        try:
            return json.loads(completed.stdout), None
        except json.JSONDecodeError:
            return None, "detector returned invalid JSON"
    except (OSError, FileNotFoundError):
        try:
            spec = importlib.util.spec_from_file_location("detect_task_state", detector_path)
            if spec is None or spec.loader is None:
                return None, "detector could not be loaded"
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            return module.detect_state(task_dir), None
        except Exception as exc:  # pragma: no cover - fallback path
            return None, f"detector fallback failed: {exc}"


def report_is_v11(report: object) -> bool:
    if not isinstance(report, dict):
        return False
    required_fields = {
        "schema_version",
        "generated_at",
        "task_id",
        "state",
        "analysis_status",
        "evidence",
        "missing_evidence",
        "allowed_next_states",
        "blocked_reason",
        "warnings",
    }
    if not required_fields.issubset(report):
        return False
    if report.get("schema_version") != "1.1":
        return False
    if report.get("analysis_status") not in VALID_ANALYSIS_STATUSES:
        return False
    if not isinstance(report.get("evidence"), list):
        return False
    if not isinstance(report.get("missing_evidence"), list):
        return False
    if not isinstance(report.get("allowed_next_states"), list):
        return False
    if not isinstance(report.get("warnings"), list):
        return False
    return True


def lookup_evidence(report: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for item in report.get("evidence", []):
        if isinstance(item, dict) and item.get("type") is not None:
            lookup[str(item["type"])] = item
    return lookup


def validate_consistency(report: dict) -> tuple[list[str], list[str]]:
    reasons: list[str] = []
    warnings: list[str] = []

    if not report_is_v11(report):
        return ["expected v1.1 report"], warnings

    state = str(report.get("state", ""))
    analysis_status = str(report.get("analysis_status", ""))

    if state == "state_conflict":
        reasons.append("deprecated state value: state_conflict")
    if state not in VALID_STATES:
        reasons.append(f"invalid state: {state}")

    if report.get("state") == "state_conflict":
        reasons.append("deprecated state_conflict report value")
    if "state_conflict" in report.get("allowed_next_states", []):
        reasons.append("state_conflict must not be an allowed next state")
    if analysis_status == "conflict":
        reasons.append("analysis_status conflict is rejected by validator")
    if analysis_status == "invalid":
        reasons.append("analysis_status invalid is rejected by validator")

    lookup = lookup_evidence(report)
    for item in report.get("evidence", []):
        if not isinstance(item, dict):
            reasons.append("evidence item is not an object")
            continue
        if not isinstance(item.get("type"), str) or not item.get("type"):
            reasons.append("evidence item has invalid type")
        if not isinstance(item.get("path"), str) or not item.get("path"):
            reasons.append("evidence item has invalid path")
        if item.get("status") not in VALID_EVIDENCE_STATUSES:
            reasons.append(f"evidence item has invalid status: {item.get('status')}")
        if not isinstance(item.get("note"), str):
            reasons.append("evidence item has invalid note")
        if item.get("status") == "conflicting":
            reasons.append(f"{item.get('type')} evidence is conflicting")

    task = lookup.get("TASK")
    review = lookup.get("REVIEW")
    trace = lookup.get("TRACE")
    contract = lookup.get("CONTRACT")
    approval = lookup.get("APPROVAL")
    active = lookup.get("ACTIVE")
    done = lookup.get("DONE")
    failed = lookup.get("FAILED_DIR") or lookup.get("FAILED")
    dropped = lookup.get("DROPPED")

    task_status = str(task.get("status")) if task else None
    review_status = str(review.get("status")) if review else None
    trace_status = str(trace.get("status")) if trace else None
    contract_status = str(contract.get("status")) if contract else None
    approval_status = str(approval.get("status")) if approval else None
    active_status = str(active.get("status")) if active else None
    done_status = str(done.get("status")) if done else None
    failed_status = str(failed.get("status")) if failed else None
    dropped_status = str(dropped.get("status")) if dropped else None

    if state == "idea":
        if task_status != "missing":
            reasons.append("TASK.md evidence exists")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [review_status, trace_status, contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "brief_draft":
        if task_status not in {"present", "valid"}:
            reasons.append("TASK.md is missing")
        if task_status == "valid":
            reasons.append("TASK.md is already approved")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [review_status, trace_status, contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "brief_approved":
        if task_status != "valid":
            reasons.append("TASK.md is not approved")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [review_status, trace_status, contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "review_ready":
        if review_status != "valid":
            reasons.append("REVIEW.md is missing or invalid")
        review_note = str(review.get("note", "")) if review else ""
        if not any(status in review_note for status in READY_REVIEW_STATUSES):
            reasons.append("REVIEW.md is not READY or READY_WITH_EDITS")
        if "execution_allowed=true" not in review_note:
            reasons.append("execution_allowed is not true")
        if task_status == "missing":
            reasons.append("TASK.md is missing")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [trace_status, contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "review_blocked":
        if review_status != "valid":
            reasons.append("REVIEW.md is missing or invalid")
        review_note = str(review.get("note", "")) if review else ""
        if not any(status in review_note for status in BLOCKED_REVIEW_STATUSES):
            reasons.append("review_status is not blocked")
        if "execution_allowed=true" in review_note:
            reasons.append("review_blocked evidence has execution_allowed=true")
        if task_status == "missing":
            reasons.append("TASK.md is missing")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [trace_status, contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "trace_written":
        if trace_status != "valid":
            reasons.append("TRACE.md is missing or invalid")
        if review_status == "missing":
            reasons.append("REVIEW.md is missing")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [contract_status, approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "contract_drafted":
        if contract_status != "valid":
            reasons.append("contract draft is missing or invalid")
        if trace_status != "valid":
            reasons.append("TRACE.md is missing or invalid")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [approval_status, active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "approved_for_execution":
        if approval_status != "valid":
            reasons.append("approval marker is missing or invalid")
        if contract_status != "valid":
            reasons.append("contract draft is missing or invalid")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [active_status, done_status, failed_status, dropped_status]):
            reasons.append("stronger evidence exists")

    elif state == "active":
        if active_status != "valid":
            reasons.append("tasks/active-task.md does not reference the task")
        if approval_status != "valid":
            reasons.append("approval marker is missing or invalid")
        if any(status in {"present", "valid", "invalid", "conflicting"} for status in [done_status, failed_status, dropped_status]):
            reasons.append("terminal evidence also exists")

    elif state == "completed":
        if done_status != "valid":
            reasons.append("task is not present in tasks/done/")
        if active_status in {"valid", "conflicting"}:
            reasons.append("active evidence also exists")
        if dropped_status in {"valid", "conflicting"}:
            reasons.append("dropped evidence also exists")
        if failed_status in {"valid", "conflicting"}:
            reasons.append("failed evidence also exists")

    elif state == "failed":
        if failed_status == "planned":
            reasons.append("failed state is reserved until tasks/failed/ exists")
        elif failed_status != "valid":
            reasons.append("task is not present in tasks/failed/")
        if active_status in {"valid", "conflicting"}:
            reasons.append("active evidence also exists")
        if done_status in {"valid", "conflicting"}:
            reasons.append("completed evidence also exists")
        if dropped_status in {"valid", "conflicting"}:
            reasons.append("dropped evidence also exists")

    elif state == "dropped":
        if dropped_status != "valid":
            reasons.append("task is not present in tasks/dropped/")
        if active_status in {"valid", "conflicting"}:
            reasons.append("active evidence also exists")
        if done_status in {"valid", "conflicting"}:
            reasons.append("completed evidence also exists")
        if failed_status in {"valid", "conflicting"}:
            reasons.append("failed evidence also exists")

    else:
        reasons.append(f"unsupported state: {state}")

    return reasons, warnings


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] == "--help":
        usage()
        return 2

    task_dir = Path(sys.argv[1])
    report, error = load_detector_report(task_dir)
    if error:
        task_id = task_dir.name
        print("TASK STATE VALIDATION")
        print()
        print(f"Task: {task_id}")
        print("Detected state: unknown")
        print()
        print("Result: FAIL")
        print("Reasons:")
        print(f"- {error}")
        return 1

    task_id = str(report.get("task_id", task_dir.name))
    state = str(report.get("state", "unknown"))
    reasons, warnings = validate_consistency(report)

    print("TASK STATE VALIDATION")
    print()
    print(f"Task: {task_id}")
    print(f"Detected state: {state}")
    print()

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if reasons:
        print("Result: FAIL")
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
