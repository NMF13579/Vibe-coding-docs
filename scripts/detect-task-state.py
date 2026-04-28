#!/usr/bin/env python3
"""Read-only task state detector for AgentOS."""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


ALLOWED_STATES = [
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
]

ALLOWED_REVIEW_BLOCKED = {
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}

ALLOWED_REVIEW_READY = {"READY", "READY_WITH_EDITS"}


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


def determine_task_id(task_dir: Path, task_text: str, warnings: list[str]) -> tuple[str, bool]:
    dir_task_id = task_dir.name
    parsed_task_id = extract_task_id_from_task_md(task_text)
    if parsed_task_id and parsed_task_id != dir_task_id:
        return dir_task_id, True
    if parsed_task_id:
        return parsed_task_id, False
    if not dir_task_id:
        warnings.append("task id fallback used from task directory name")
    return dir_task_id, False


def detect_state(task_dir: Path) -> dict:
    warnings: list[str] = []
    evidence: list[dict] = []
    missing_evidence: list[str] = []
    conflict_reasons: list[str] = []

    task_md = task_dir / "TASK.md"
    review_md = task_dir / "REVIEW.md"
    trace_md = task_dir / "TRACE.md"
    approvals_dir = task_dir / "approvals"
    active_task_path = task_dir.parent / "active-task.md"
    done_dir = task_dir.parent / "done"
    failed_dir = task_dir.parent / "failed"
    dropped_dir = task_dir.parent / "dropped"
    draft_path = task_dir.parent / "drafts" / f"{task_dir.name}-contract-draft.md"

    task_text = read_text(task_md) if task_md.is_file() else ""
    task_id, task_id_conflict = determine_task_id(task_dir, task_text, warnings)

    if task_id_conflict:
        conflict_reasons.append("task_id in TASK.md conflicts with directory name")

    task_exists = task_md.is_file()
    task_approved = task_exists and task_is_approved(task_text)
    if task_exists:
        evidence.append(
            make_evidence_item(
                "TASK",
                str(task_md),
                "valid" if task_approved else "present",
                "TASK.md exists and is approved" if task_approved else "TASK.md exists",
            )
        )
    else:
        evidence.append(make_evidence_item("TASK", str(task_md), "missing", "TASK.md missing"))
        missing_evidence.append(str(task_md))

    review_exists = review_md.is_file()
    review_text = read_text(review_md) if review_exists else ""
    review_status = extract_review_status(review_text) if review_exists else None
    execution_allowed = extract_execution_allowed(review_text) if review_exists else None
    review_ready = review_status in ALLOWED_REVIEW_READY and execution_allowed is True
    review_blocked = review_status in ALLOWED_REVIEW_BLOCKED

    if review_exists:
        note = f"review_status={review_status or 'unknown'}"
        if execution_allowed is not None:
            note += f", execution_allowed={str(execution_allowed).lower()}"
        evidence.append(
            make_evidence_item(
                "REVIEW",
                str(review_md),
                "valid" if (review_ready or review_blocked) else "present",
                note,
            )
        )
    else:
        evidence.append(make_evidence_item("REVIEW", str(review_md), "missing", "REVIEW.md missing"))
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

    approval_valid = False
    approval_path = approvals_dir
    if approvals_dir.is_dir():
        for md_path in approvals_dir.rglob("*.md"):
            if task_id in md_path.name or task_id in read_text(md_path):
                approval_valid = True
                approval_path = md_path
                break
        evidence.append(
            make_evidence_item(
                "APPROVAL",
                str(approval_path),
                "valid" if approval_valid else "missing",
                "approval marker contains task_id" if approval_valid else "approval marker missing",
            )
        )
        if not approval_valid:
            missing_evidence.append(str(approval_path))
    else:
        evidence.append(
            make_evidence_item(
                "APPROVAL",
                str(approval_path),
                "missing",
                "approvals/ directory missing",
            )
        )
        missing_evidence.append(str(approval_path))

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
                "FAILED",
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
                "FAILED",
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

    if active_ref and any([completed_present, failed_present, dropped_present]):
        conflict_reasons.append("active evidence conflicts with terminal evidence")
    if completed_present and any([failed_present, dropped_present]):
        conflict_reasons.append("completed evidence conflicts with failed/dropped evidence")
    if failed_present and dropped_present:
        conflict_reasons.append("failed evidence conflicts with dropped evidence")
    if approval_valid and completed_present:
        conflict_reasons.append("approval marker exists but task is already completed")
    if approval_valid and not draft_valid:
        conflict_reasons.append("approval marker exists without contract draft")
    if draft_valid and not trace_valid:
        conflict_reasons.append("contract_drafted without trace_written")
    if trace_valid and not review_exists:
        conflict_reasons.append("trace_written without REVIEW.md")
    if review_ready and not task_exists:
        conflict_reasons.append("review_ready evidence exists without TASK.md")
    if review_blocked and not task_exists:
        conflict_reasons.append("review_blocked evidence exists without TASK.md")

    if task_id_conflict:
        conflict_reasons.append("task_id conflict between directory name and TASK.md")

    if conflict_reasons:
        state = "state_conflict"
    elif active_ref:
        state = "active"
    elif completed_present:
        state = "completed"
    elif failed_present and failed_dir.is_dir():
        state = "failed"
    elif dropped_present:
        state = "dropped"
    elif approval_valid:
        state = "approved_for_execution"
    elif draft_valid:
        state = "contract_drafted"
    elif trace_valid:
        state = "trace_written"
    elif review_ready:
        state = "review_ready"
    elif review_blocked:
        state = "review_blocked"
    elif task_approved:
        state = "brief_approved"
    elif task_exists:
        state = "brief_draft"
    else:
        state = "idea"

    allowed_next_states = {
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
        "state_conflict": [],
    }[state]

    blocked_reason = "; ".join(conflict_reasons) if conflict_reasons else ""

    return {
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "task_id": task_id,
        "state": state,
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
