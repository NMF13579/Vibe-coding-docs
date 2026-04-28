#!/usr/bin/env python3
"""Read-only task state detector for AgentOS."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ALLOWED_REVIEW_BLOCKED = {
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}

ALLOWED_REVIEW_READY = {"READY", "READY_WITH_EDITS"}

STATE_ALLOWED_NEXT = {
    "idea": ["brief_draft"],
    "brief_draft": ["brief_approved"],
    "brief_approved": ["review_ready", "review_blocked"],
    "review_ready": ["trace_written"],
    "review_blocked": ["brief_draft"],
    "trace_written": ["contract_drafted"],
    "contract_drafted": ["approved_for_execution"],
    "approved_for_execution": ["active"],
    "active": ["completed", "failed", "dropped"],
    "completed": [],
    "failed": ["brief_draft"],
    "dropped": [],
}


def usage() -> None:
    print("Usage: python3 scripts/detect-task-state.py tasks/{task-id}")


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return ""


def is_nonempty_file(path: Path) -> bool:
    return path.is_file() and path.stat().st_size > 0


def extract_task_id_from_task_md(text: str) -> str | None:
    for pattern in (
        r"(?im)^\s*task_id\s*:\s*['\"]?([^'\"]+)['\"]?\s*$",
        r"(?im)^\s*id\s*:\s*['\"]?([^'\"]+)['\"]?\s*$",
    ):
        match = re.search(pattern, text)
        if match:
            return match.group(1).strip()
    return None


def task_is_approved(text: str) -> bool:
    lowered = text.lower()
    return (
        bool(re.search(r"(?im)^\s*status\s*:\s*approved\s*$", text))
        or bool(re.search(r"(?im)^\s*task_status\s*:\s*approved\s*$", text))
        or bool(re.search(r"(?im)^\s*approved\s*:\s*true\s*$", text))
        or "status: approved" in lowered
        or "task_status: approved" in lowered
        or "approved: true" in lowered
    )


def extract_review_status(text: str) -> str | None:
    match = re.search(r"(?im)^\s*review_status\s*:\s*([A-Z_]+)\s*$", text)
    if match:
        return match.group(1).strip().upper()
    return None


def extract_execution_allowed(text: str) -> bool | None:
    match = re.search(r"(?im)^\s*execution_allowed\s*:\s*(true|false)\s*$", text)
    if match:
        return match.group(1).strip().lower() == "true"
    return None


def file_contains_task_id(path: Path, task_id: str) -> bool:
    return path.is_file() and task_id in read_text(path)


def scan_markdown_dir(directory: Path, task_id: str) -> bool:
    if not directory.is_dir():
        return False
    for path in directory.rglob("*.md"):
        if task_id in path.name or file_contains_task_id(path, task_id):
            return True
    return False


def make_evidence_item(item_type: str, path: str, status: str, note: str) -> dict:
    return {
        "type": item_type,
        "path": path,
        "status": status,
        "note": note,
    }


def determine_task_id(task_dir: Path, task_text: str, warnings: list[str]) -> str:
    dir_task_id = task_dir.name
    parsed_task_id = extract_task_id_from_task_md(task_text)
    if parsed_task_id and parsed_task_id != dir_task_id:
        warnings.append("task_id in TASK.md conflicts with directory name")
        return dir_task_id
    if parsed_task_id:
        return parsed_task_id
    return dir_task_id


def detect_state(task_dir: Path) -> dict:
    warnings: list[str] = []
    evidence: list[dict] = []
    missing_evidence: list[str] = []

    task_md = task_dir / "TASK.md"
    review_md = task_dir / "REVIEW.md"
    trace_md = task_dir / "TRACE.md"
    active_task_path = task_dir.parent / "active-task.md"
    done_dir = task_dir.parent / "done"
    failed_dir = task_dir.parent / "failed"
    dropped_dir = task_dir.parent / "dropped"
    draft_path = task_dir.parent / "drafts" / f"{task_dir.name}-contract-draft.md"
    task_approvals_dir = task_dir / "approvals"
    root_approvals_dir = task_dir.parent.parent / "approvals"

    task_text = read_text(task_md) if task_md.is_file() else ""
    task_id = determine_task_id(task_dir, task_text, warnings)

    task_exists = task_md.is_file()
    task_approved = task_exists and task_is_approved(task_text)
    evidence.append(
        make_evidence_item(
            "TASK",
            str(task_md),
            "valid" if task_approved else ("present" if task_exists else "missing"),
            "TASK.md exists and is approved" if task_approved else ("TASK.md exists" if task_exists else "TASK.md missing"),
        )
    )
    if not task_exists:
        missing_evidence.append(str(task_md))

    review_exists = review_md.is_file()
    review_text = read_text(review_md) if review_exists else ""
    review_status = extract_review_status(review_text) if review_exists else None
    execution_allowed = extract_execution_allowed(review_text) if review_exists else None
    review_ready_valid = review_exists and review_status in ALLOWED_REVIEW_READY and execution_allowed is True
    review_blocked_valid = review_exists and review_status in ALLOWED_REVIEW_BLOCKED and execution_allowed is not True
    evidence.append(
        make_evidence_item(
            "REVIEW",
            str(review_md),
            "valid" if (review_ready_valid or review_blocked_valid) else ("invalid" if review_exists else "missing"),
            (
                f"review_status={review_status or 'unknown'}, execution_allowed={str(execution_allowed).lower()}"
                if review_exists
                else "REVIEW.md missing"
            ),
        )
    )
    if not review_exists:
        missing_evidence.append(str(review_md))

    trace_exists = trace_md.is_file()
    trace_valid = is_nonempty_file(trace_md)
    evidence.append(
        make_evidence_item(
            "TRACE",
            str(trace_md),
            "valid" if trace_valid else ("invalid" if trace_exists else "missing"),
            "TRACE.md exists and is non-empty"
            if trace_valid
            else ("TRACE.md exists but is empty" if trace_exists else "TRACE.md missing"),
        )
    )
    if not trace_exists:
        missing_evidence.append(str(trace_md))

    draft_exists = draft_path.is_file()
    draft_valid = is_nonempty_file(draft_path)
    evidence.append(
        make_evidence_item(
            "CONTRACT",
            str(draft_path),
            "valid" if draft_valid else ("invalid" if draft_exists else "missing"),
            "contract draft exists and is non-empty"
            if draft_valid
            else ("contract draft exists but is empty" if draft_exists else "contract draft missing"),
        )
    )
    if not draft_exists:
        missing_evidence.append(str(draft_path))

    approval_marker = None
    for approvals_dir in (task_approvals_dir, root_approvals_dir):
        if approvals_dir.is_dir():
            for md_path in approvals_dir.rglob("*.md"):
                if task_id in md_path.name or task_id in read_text(md_path):
                    approval_marker = md_path
                    break
        if approval_marker:
            break
    approval_valid = approval_marker is not None
    approval_path = str(approval_marker) if approval_marker else str(root_approvals_dir)
    evidence.append(
        make_evidence_item(
            "APPROVAL",
            approval_path,
            "valid" if approval_valid else "missing",
            "approval marker contains task_id" if approval_valid else "approval marker missing",
        )
    )
    if not approval_valid:
        missing_evidence.append(approval_path)

    active_ref = active_task_path.is_file() and task_id in read_text(active_task_path)
    evidence.append(
        make_evidence_item(
            "ACTIVE",
            str(active_task_path),
            "valid" if active_ref else "missing",
            "tasks/active-task.md references task"
            if active_ref
            else "tasks/active-task.md does not reference task",
        )
    )
    if not active_ref:
        missing_evidence.append(str(active_task_path))

    completed_present = scan_markdown_dir(done_dir, task_id)
    evidence.append(
        make_evidence_item(
            "DONE",
            str(done_dir),
            "valid" if completed_present else "missing",
            "task found in tasks/done/" if completed_present else "task not found in tasks/done/",
        )
    )
    if not completed_present:
        missing_evidence.append(str(done_dir))

    if failed_dir.is_dir():
        failed_present = scan_markdown_dir(failed_dir, task_id)
        evidence.append(
            make_evidence_item(
                "FAILED_DIR",
                str(failed_dir),
                "valid" if failed_present else "missing",
                "task found in tasks/failed/" if failed_present else "task not found in tasks/failed/",
            )
        )
        if not failed_present:
            missing_evidence.append(str(failed_dir))
    else:
        failed_present = False
        warnings.append("tasks/failed/ is missing; failed state is planned evidence path")
        evidence.append(
            make_evidence_item(
                "FAILED_DIR",
                str(failed_dir),
                "planned",
                "tasks/failed/ is a planned evidence path and does not exist yet",
            )
        )

    dropped_present = scan_markdown_dir(dropped_dir, task_id)
    evidence.append(
        make_evidence_item(
            "DROPPED",
            str(dropped_dir),
            "valid" if dropped_present else "missing",
            "task found in tasks/dropped/" if dropped_present else "task not found in tasks/dropped/",
        )
    )
    if not dropped_present:
        missing_evidence.append(str(dropped_dir))

    conflict_reasons: list[str] = []
    conflicting_types: set[str] = set()
    if active_ref and completed_present:
        conflict_reasons.append("task is completed but still referenced as active")
        conflicting_types.update({"ACTIVE", "DONE"})
    if active_ref and dropped_present:
        conflict_reasons.append("task is dropped but still referenced as active")
        conflicting_types.update({"ACTIVE", "DROPPED"})
    if active_ref and failed_present:
        conflict_reasons.append("task is failed but still referenced as active")
        conflicting_types.update({"ACTIVE", "FAILED_DIR"})
    if completed_present and dropped_present:
        conflict_reasons.append("completed and dropped evidence both exist")
        conflicting_types.update({"DONE", "DROPPED"})
    if completed_present and failed_present:
        conflict_reasons.append("completed and failed evidence both exist")
        conflicting_types.update({"DONE", "FAILED_DIR"})
    if dropped_present and failed_present:
        conflict_reasons.append("dropped and failed evidence both exist")
        conflicting_types.update({"DROPPED", "FAILED_DIR"})

    if conflicting_types:
        for item in evidence:
            if item["type"] in conflicting_types and item["status"] in {"valid", "present"}:
                item["status"] = "conflicting"
                if item["type"] == "ACTIVE":
                    item["note"] = "tasks/active-task.md references task but conflicts with terminal evidence"
                elif item["type"] == "DONE":
                    item["note"] = "task found in tasks/done/ but conflicts with active evidence"
                elif item["type"] == "DROPPED":
                    item["note"] = "task found in tasks/dropped/ but conflicts with active evidence"
                elif item["type"] == "FAILED_DIR":
                    item["note"] = "task found in tasks/failed/ but conflicts with active evidence"

    if completed_present:
        state = "completed"
    elif dropped_present:
        state = "dropped"
    elif failed_present:
        state = "failed"
    elif active_ref:
        state = "active"
    elif approval_valid:
        state = "approved_for_execution"
    elif draft_valid:
        state = "contract_drafted"
    elif trace_valid:
        state = "trace_written"
    elif review_ready_valid:
        state = "review_ready"
    elif review_blocked_valid:
        state = "review_blocked"
    elif task_approved:
        state = "brief_approved"
    elif task_exists:
        state = "brief_draft"
    else:
        state = "idea"

    invalid_reasons: list[str] = []
    if state == "brief_draft":
        if not task_exists:
            invalid_reasons.append("TASK.md is missing")
    elif state == "brief_approved":
        if not task_approved:
            invalid_reasons.append("TASK.md is not approved")
    elif state == "review_ready":
        if not review_ready_valid:
            invalid_reasons.append("review_ready evidence is not READY or READY_WITH_EDITS with execution_allowed=true")
        if not task_exists:
            invalid_reasons.append("review_ready evidence exists without TASK.md")
    elif state == "review_blocked":
        if not review_blocked_valid:
            invalid_reasons.append("review_blocked evidence is not blocked")
        if not task_exists:
            invalid_reasons.append("review_blocked evidence exists without TASK.md")
    elif state == "trace_written":
        if not trace_valid:
            invalid_reasons.append("trace_written evidence is missing or invalid")
        if not review_exists:
            invalid_reasons.append("trace_written without REVIEW.md")
    elif state == "contract_drafted":
        if not draft_valid:
            invalid_reasons.append("contract_drafted evidence is missing or invalid")
        if not trace_valid:
            invalid_reasons.append("contract_drafted without TRACE.md")
    elif state == "approved_for_execution":
        if not approval_valid:
            invalid_reasons.append("approved_for_execution without approval marker")
        if not draft_valid:
            invalid_reasons.append("approved_for_execution without contract draft")
    elif state == "active":
        if not active_ref:
            invalid_reasons.append("active evidence is missing")
        if not approval_valid:
            invalid_reasons.append("active without approval marker")
    elif state == "completed":
        if not completed_present:
            invalid_reasons.append("completed evidence is missing")
    elif state == "failed":
        if not failed_dir.is_dir():
            invalid_reasons.append("failed state is reserved until tasks/failed/ exists")
        elif not failed_present:
            invalid_reasons.append("failed evidence is missing")
    elif state == "dropped":
        if not dropped_present:
            invalid_reasons.append("dropped evidence is missing")

    if conflict_reasons:
        analysis_status = "conflict"
        blocked_reason = "; ".join(conflict_reasons)
    elif invalid_reasons:
        analysis_status = "invalid"
        blocked_reason = "; ".join(invalid_reasons)
    else:
        analysis_status = "ok"
        blocked_reason = ""

    allowed_next_states = STATE_ALLOWED_NEXT[state]

    return {
        "schema_version": "1.1",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "task_id": task_id,
        "state": state,
        "analysis_status": analysis_status,
        "evidence": evidence,
        "missing_evidence": missing_evidence,
        "allowed_next_states": allowed_next_states,
        "blocked_reason": blocked_reason,
        "warnings": warnings,
    }


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] == "--help":
        usage()
        return 2

    task_dir = Path(sys.argv[1])
    report = detect_state(task_dir)
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
