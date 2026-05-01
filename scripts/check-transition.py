#!/usr/bin/env python3
"""Dry-run transition checker for AgentOS task states."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


VALID_TARGET_STATES = {
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

TRANSITION_MAP = {
    "idea": {"brief_draft"},
    "brief_draft": {"brief_approved"},
    "brief_approved": {"review_ready", "review_blocked"},
    "review_blocked": {"brief_draft"},
    "review_ready": {"trace_written"},
    "trace_written": {"contract_drafted"},
    "contract_drafted": {"approved_for_execution"},
    "approved_for_execution": {"active"},
    "active": {"completed", "failed", "dropped"},
    "failed": {"brief_draft"},
}

BLOCKED_REVIEW_STATUSES = {
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}


def usage() -> None:
    print("Usage: python3 scripts/check-transition.py tasks/{task-id} --to <target_state>")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def is_nonempty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def evidence_lookup(report: dict) -> dict[str, dict]:
    lookup: dict[str, dict] = {}
    for item in report.get("evidence", []):
        if isinstance(item, dict) and "type" in item:
            lookup[str(item["type"])] = item
    return lookup


def has_evidence(report: dict, artifact_type: str, allowed_statuses: tuple[str, ...] = ("valid",)) -> bool:
    """True if evidence contains an item with the given type and allowed status."""
    return any(
        isinstance(item, dict)
        and item.get("type") == artifact_type
        and item.get("status") in allowed_statuses
        for item in report.get("evidence", [])
    )


def has_valid(report: dict, artifact_type: str) -> bool:
    """Shortcut for valid evidence."""
    return has_evidence(report, artifact_type, ("valid",))


def has_path(report: dict, path_fragment: str) -> bool:
    """True if evidence contains a path including the fragment."""
    return any(
        isinstance(item, dict) and path_fragment in str(item.get("path", ""))
        for item in report.get("evidence", [])
    )


def run_json_report(script_name: str, args: list[str]) -> tuple[dict | None, str | None]:
    script_path = Path(__file__).resolve().parent / script_name
    completed = subprocess.run(
        [sys.executable, str(script_path), *args],
        cwd=str(script_path.parent.parent),
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        message = stderr or stdout or f"{script_name} exited with code {completed.returncode}"
        return None, message
    try:
        return json.loads(completed.stdout), None
    except json.JSONDecodeError:
        return None, f"{script_name} returned invalid JSON"


def task_paths(task_dir: Path, task_id: str) -> dict[str, Path]:
    parent = task_dir.parent
    return {
        "task_md": task_dir / "TASK.md",
        "review_md": task_dir / "REVIEW.md",
        "trace_md": task_dir / "TRACE.md",
        "contract_draft": parent / "drafts" / f"{task_id}-contract-draft.md",
        "brief_draft": parent / "drafts" / f"{task_id}-brief-draft.md",
        "active_task": parent / "active-task.md",
        "done_dir": parent / "done",
        "failed_dir": parent / "failed",
        "dropped_dir": parent / "dropped",
        "approvals_dir": task_dir / "approvals",
    }


def task_is_approved(text: str) -> bool:
    lowered = text.lower()
    return (
        "status: approved" in lowered
        or "task_status: approved" in lowered
        or "approved: true" in lowered
    )


def review_ready(text: str) -> bool:
    lowered = text.lower()
    return (
        "review_status: ready" in lowered
        or "review_status: ready_with_edits" in lowered
    ) and "execution_allowed: true" in lowered


def review_blocked(text: str) -> bool:
    lowered = text.lower()
    return any(f"review_status: {status.lower()}" in lowered for status in BLOCKED_REVIEW_STATUSES)


def scan_markdown_dir(directory: Path, task_id: str) -> bool:
    if not directory.is_dir():
        return False
    for path in directory.rglob("*.md"):
        if task_id in path.name or task_id in read_text(path):
            return True
    return False


def find_valid_item(lookup: dict[str, dict], key: str) -> dict | None:
    item = lookup.get(key)
    if item and item.get("status") in {"present", "valid"}:
        return item
    return None


def detect_direct_evidence(task_dir: Path, task_id: str) -> dict[str, bool]:
    paths = task_paths(task_dir, task_id)
    return {
        "task_exists": paths["task_md"].is_file(),
        "task_approved": paths["task_md"].is_file() and task_is_approved(read_text(paths["task_md"])),
        "review_exists": paths["review_md"].is_file(),
        "review_ready": paths["review_md"].is_file() and review_ready(read_text(paths["review_md"])),
        "review_blocked": paths["review_md"].is_file() and review_blocked(read_text(paths["review_md"])),
        "trace_valid": is_nonempty_file(paths["trace_md"]),
        "contract_valid": is_nonempty_file(paths["contract_draft"]),
        "brief_draft_valid": is_nonempty_file(paths["brief_draft"]),
        "approval_valid": False,
        "active_ref": paths["active_task"].is_file() and task_id in read_text(paths["active_task"]),
        "done_valid": scan_markdown_dir(paths["done_dir"], task_id),
        "failed_valid": scan_markdown_dir(paths["failed_dir"], task_id),
        "dropped_valid": scan_markdown_dir(paths["dropped_dir"], task_id),
    }


def collect_approval_marker(lookup: dict[str, dict], task_dir: Path, task_id: str) -> tuple[bool, str]:
    approval = find_valid_item(lookup, "APPROVAL_MARKER")
    if approval:
        return True, str(approval.get("path", task_dir / "approvals"))
    approvals_dir = task_dir / "approvals"
    if approvals_dir.is_dir():
        for md_path in approvals_dir.rglob("*.md"):
            if task_id in read_text(md_path) or task_id in md_path.name:
                return True, str(md_path)
    return False, str(approvals_dir)


def collect_problem_reasons(
    current_state: str,
    target_state: str,
    report: dict,
    task_id: str,
) -> list[str]:
    reasons: list[str] = []
    if not isinstance(report, dict):
        return ["detector returned invalid report"]

    if report.get("schema_version") != "1.1":
        reasons.append("expected v1.1 report")
        return reasons

    if report.get("schema_version") != "1.1":
        reasons.append("expected v1.1 report")
        return reasons

    if current_state == "state_conflict":
        reasons.append("current state is deprecated state_conflict")
        return reasons

    if target_state == "state_conflict":
        reasons.append("state_conflict is detector-only and cannot be requested manually")
        return reasons

    analysis_status = str(report.get("analysis_status", ""))
    if analysis_status == "conflict":
        reasons.append("current state analysis is conflict")
        return reasons
    if analysis_status == "invalid":
        reasons.append("current state analysis is invalid")
        return reasons

    if target_state not in VALID_TARGET_STATES:
        reasons.append(f"invalid target state: {target_state}")
        return reasons

    allowed_targets = set(report.get("allowed_next_states", []))
    map_targets = TRANSITION_MAP.get(current_state, set())
    if target_state not in allowed_targets:
        reasons.append(f"transition {current_state} -> {target_state} is not allowed")
    if target_state not in map_targets:
        reasons.append(f"transition map forbids {current_state} -> {target_state}")

    if target_state in {"approved_for_execution", "active"}:
        if not has_valid(report, "CONTRACT"):
            reasons.append("missing valid CONTRACT evidence")
        if not has_evidence(report, "APPROVAL", ("valid", "present")):
            reasons.append("missing APPROVAL evidence")

    if target_state == "review_ready":
        if not has_evidence(report, "REVIEW", ("valid",)):
            reasons.append("missing ready review evidence")
        if not has_evidence(report, "TASK", ("present", "valid")):
            reasons.append("missing TASK evidence")

    if target_state == "review_blocked":
        if not has_evidence(report, "REVIEW", ("valid",)):
            reasons.append("missing blocked review evidence")
        if not has_evidence(report, "TASK", ("present", "valid")):
            reasons.append("missing TASK evidence")

    if target_state == "trace_written":
        if not has_valid(report, "TRACE"):
            reasons.append("missing valid TRACE evidence")

    if target_state == "contract_drafted":
        if not has_valid(report, "CONTRACT"):
            reasons.append("missing valid CONTRACT evidence")
        if not has_valid(report, "TRACE"):
            reasons.append("missing valid TRACE evidence")

    if target_state == "completed":
        if not has_path(report, "active-task.md") or not has_evidence(report, "ACTIVE", ("valid",)):
            reasons.append("missing active-task.md reference")
        if not has_evidence(report, "DONE", ("valid",)):
            reasons.append("missing completion evidence")

    if target_state == "failed":
        if not has_path(report, "active-task.md") or not has_evidence(report, "ACTIVE", ("valid",)):
            reasons.append("missing active-task.md reference")
        if not has_evidence(report, "FAILED_DIR", ("valid", "planned")):
            reasons.append("missing failure evidence")

    if target_state == "dropped":
        if not has_path(report, "active-task.md") or not has_evidence(report, "ACTIVE", ("valid",)):
            reasons.append("missing active-task.md reference")
        if not has_evidence(report, "DROPPED", ("valid",)):
            reasons.append("missing drop evidence")

    return reasons


def print_result(task_id: str, current_state: str, target_state: str, reasons: list[str], note: str | None = None) -> None:
    print("TASK TRANSITION CHECK")
    print()
    print(f"Task: {task_id}")
    print(f"Current state: {current_state}")
    print(f"Requested target state: {target_state}")
    print()
    if reasons:
        print("Result: FAIL")
        print("Reasons:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("Result: PASS")
        print("Mode: dry-run only")
    print("Transition executed: no")
    if note:
        print(f"Note: {note}")


def main() -> int:
    if "--help" in sys.argv or len(sys.argv) != 4:
        usage()
        return 2 if "--help" in sys.argv or len(sys.argv) != 4 else 2

    task_arg = sys.argv[1]
    to_flag = sys.argv[2]
    target_state = sys.argv[3]

    if to_flag != "--to":
        usage()
        return 2

    if target_state == "state_conflict":
        task_id = Path(task_arg).name
        print_result(
            task_id,
            "unknown",
            target_state,
            ["state_conflict is detector-only and cannot be requested manually"],
        )
        return 1

    if target_state not in VALID_TARGET_STATES:
        task_id = Path(task_arg).name
        print_result(task_id, "unknown", target_state, [f"invalid target state: {target_state}"])
        return 1

    task_dir = Path(task_arg)
    detector_report, detector_error = run_json_report("detect-task-state.py", [str(task_dir)])
    if detector_error:
        task_id = task_dir.name
        print_result(task_id, "unknown", target_state, [f"detector failed: {detector_error}"])
        return 1

    task_id = str(detector_report.get("task_id", task_dir.name))
    current_state = str(detector_report.get("state", "unknown"))
    reasons = collect_problem_reasons(current_state, target_state, detector_report, task_id)

    note = None
    if not reasons and current_state == "approved_for_execution" and target_state == "active":
        note = "active-task.md replacement is out of scope for Milestone 10"

    print_result(task_id, current_state, target_state, reasons, note=note)
    return 0 if not reasons else 1


if __name__ == "__main__":
    raise SystemExit(main())
