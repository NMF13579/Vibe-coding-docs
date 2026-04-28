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
    "state_conflict",
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


def lookup_evidence(report: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for item in report.get("evidence", []):
        if isinstance(item, dict) and "type" in item:
            lookup[str(item["type"])] = item
    return lookup


def evidence_status(item: dict | None) -> str | None:
    if not item:
        return None
    return str(item.get("status"))


def has_status(item: dict | None, statuses: set[str]) -> bool:
    return evidence_status(item) in statuses


def report_is_v1_compat(report: object) -> bool:
    return isinstance(report, dict) and "state" in report and "evidence" in report and "missing_evidence" in report


def validate_consistency(report: dict) -> list[str]:
    reasons: list[str] = []

    if not report_is_v1_compat(report):
        return ["detector output is invalid"]

    state = str(report.get("state", ""))
    if state not in VALID_STATES:
        return [f"invalid state: {state}"]
    if state == "state_conflict":
        return ["detector returned state_conflict"]

    lookup = lookup_evidence(report)
    task = lookup.get("TASK")
    review = lookup.get("REVIEW")
    trace = lookup.get("TRACE")
    contract = lookup.get("CONTRACT")
    approval = lookup.get("APPROVAL")
    active = lookup.get("ACTIVE")
    done = lookup.get("DONE")
    failed = lookup.get("FAILED")
    dropped = lookup.get("DROPPED")

    task_status = evidence_status(task)
    review_status = evidence_status(review)
    trace_status = evidence_status(trace)
    contract_status = evidence_status(contract)
    approval_status = evidence_status(approval)
    active_status = evidence_status(active)
    done_status = evidence_status(done)
    failed_status = evidence_status(failed)
    dropped_status = evidence_status(dropped)

    def present_or_valid(item: dict | None) -> bool:
        return evidence_status(item) in {"present", "valid"}

    def valid_only(item: dict | None) -> bool:
        return evidence_status(item) == "valid"

    def present_or_valid_or_planned(item: dict | None) -> bool:
        return evidence_status(item) in {"present", "valid", "planned"}

    all_other_stronger = any(
        present_or_valid(item)
        for item in [review, trace, contract, approval, active, done, failed, dropped]
    )

    if state == "idea":
        if task_status != "missing":
            reasons.append("TASK.md evidence exists")
        if all_other_stronger:
            reasons.append("stronger evidence exists")

    elif state == "brief_draft":
        if task_status not in {"present", "valid"}:
            reasons.append("TASK.md is missing")
        if task_status == "valid":
            reasons.append("TASK.md is already approved")
        if any(
            present_or_valid(item)
            for item in [review, trace, contract, approval, active, done, failed, dropped]
        ):
            reasons.append("stronger evidence exists")

    elif state == "brief_approved":
        if task_status != "valid":
            reasons.append("TASK.md is not approved")

    elif state == "review_ready":
        if task_status == "missing":
            reasons.append("TASK.md is missing")
        if review_status not in {"valid"}:
            reasons.append("REVIEW.md is missing or invalid")
        review_note = str(review.get("note", "")) if review else ""
        if "review_status=READY" not in review_note and "review_status=READY_WITH_EDITS" not in review_note:
            reasons.append("REVIEW.md is not READY or READY_WITH_EDITS")
        if "execution_allowed=true" not in review_note:
            reasons.append("execution_allowed is not true")

    elif state == "review_blocked":
        if task_status == "missing":
            reasons.append("TASK.md is missing")
        if review_status not in {"valid"}:
            reasons.append("REVIEW.md is missing or invalid")
        review_note = str(review.get("note", "")) if review else ""
        if not any(status in review_note for status in BLOCKED_REVIEW_STATUSES):
            reasons.append("review_status is not blocked")

    elif state == "trace_written":
        if trace_status != "valid":
            reasons.append("TRACE.md is missing or invalid")
        if review_status == "missing":
            reasons.append("REVIEW.md is missing")

    elif state == "contract_drafted":
        if contract_status != "valid":
            reasons.append("contract draft is missing or invalid")
        if trace_status == "missing":
            reasons.append("TRACE.md is missing")

    elif state == "approved_for_execution":
        if approval_status != "valid":
            reasons.append("approval marker is missing or invalid")
        if contract_status != "valid":
            reasons.append("contract draft is missing or invalid")

    elif state == "active":
        if active_status != "valid":
            reasons.append("tasks/active-task.md does not reference the task")
        if any(status == "valid" for status in [done_status, failed_status, dropped_status]):
            reasons.append("terminal evidence also exists")

    elif state == "completed":
        if done_status != "valid":
            reasons.append("task is not present in tasks/done/")
        if any(status == "valid" for status in [active_status, failed_status, dropped_status]):
            reasons.append("active/failed/dropped evidence also exists")

    elif state == "failed":
        if failed_status == "planned":
            # Planned path is acceptable when the repository does not yet have tasks/failed/.
            if task_status == "missing" and not any(
                status == "valid" for status in [active_status, done_status, dropped_status]
            ):
                pass
        elif failed_status != "valid":
            reasons.append("task is not present in tasks/failed/")
        if any(status == "valid" for status in [active_status, done_status, dropped_status]):
            reasons.append("active/completed/dropped evidence also exists")

    elif state == "dropped":
        if dropped_status != "valid":
            reasons.append("task is not present in tasks/dropped/")
        if any(status == "valid" for status in [active_status, done_status, failed_status]):
            reasons.append("active/completed/failed evidence also exists")

    else:
        reasons.append(f"unsupported state: {state}")

    return reasons


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
    reasons = validate_consistency(report)

    print("TASK STATE VALIDATION")
    print()
    print(f"Task: {task_id}")
    print(f"Detected state: {state}")
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
