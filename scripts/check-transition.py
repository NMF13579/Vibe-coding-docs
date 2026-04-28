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


def status_is(item: dict | None, statuses: set[str]) -> bool:
    return bool(item) and str(item.get("status")) in statuses


def note_contains(item: dict | None, text: str) -> bool:
    return bool(item) and text in str(item.get("note", ""))


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


def run_validator(task_dir: Path) -> tuple[bool, list[str], str | None]:
    validator_path = Path(__file__).resolve().parent / "validate-task-state.py"
    completed = subprocess.run(
        [sys.executable, str(validator_path), str(task_dir)],
        cwd=str(validator_path.parent.parent),
        capture_output=True,
        text=True,
    )
    if completed.returncode == 0:
        return True, [], None

    reasons: list[str] = []
    in_reasons = False
    for line in completed.stdout.splitlines():
        stripped = line.strip()
        if stripped == "Reasons:":
            in_reasons = True
            continue
        if in_reasons and stripped.startswith("- "):
            reasons.append(stripped[2:].strip())
    if not reasons:
        stderr = completed.stderr.strip()
        stdout = completed.stdout.strip()
        message = stderr or stdout or f"validator exited with code {completed.returncode}"
        reasons.append(message)
    return False, reasons, None


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
    task_dir: Path,
    task_id: str,
) -> list[str]:
    reasons: list[str] = []
    lookup = evidence_lookup(report)
    direct = detect_direct_evidence(task_dir, task_id)
    approval_valid, approval_path = collect_approval_marker(lookup, task_dir, task_id)

    task_md = task_paths(task_dir, task_id)["task_md"]
    review_md = task_paths(task_dir, task_id)["review_md"]
    trace_md = task_paths(task_dir, task_id)["trace_md"]
    contract_draft = task_paths(task_dir, task_id)["contract_draft"]
    brief_draft = task_paths(task_dir, task_id)["brief_draft"]
    active_task = task_paths(task_dir, task_id)["active_task"]

    if current_state == "state_conflict":
        reasons.append("current state is state_conflict")
        return reasons

    if target_state == "state_conflict":
        reasons.append("state_conflict is detector-only and cannot be requested manually")
        return reasons

    if target_state not in VALID_TARGET_STATES:
        reasons.append(f"invalid target state: {target_state}")
        return reasons

    allowed_targets = TRANSITION_MAP.get(current_state, set())
    if target_state not in allowed_targets:
        reasons.append(f"transition {current_state} -> {target_state} is not allowed")

    if current_state == "idea" and target_state == "brief_draft":
        if not (direct["task_exists"] or direct["brief_draft_valid"]):
            reasons.append("TASK.md draft or task brief draft is missing")

    elif current_state == "brief_draft" and target_state == "brief_approved":
        if not direct["task_approved"]:
            reasons.append("TASK.md is not approved")

    elif current_state == "brief_approved" and target_state == "review_ready":
        review_item = lookup.get("REVIEW")
        if not (direct["review_exists"] and direct["review_ready"]):
            reasons.append("REVIEW.md is not READY or READY_WITH_EDITS with execution_allowed: true")

    elif current_state == "brief_approved" and target_state == "review_blocked":
        if not (direct["review_exists"] and direct["review_blocked"]):
            reasons.append("REVIEW.md is not blocked")

    elif current_state == "review_blocked" and target_state == "brief_draft":
        if not (direct["task_exists"] or direct["brief_draft_valid"]):
            reasons.append("updated TASK.md or task brief draft is missing")

    elif current_state == "review_ready" and target_state == "trace_written":
        if not direct["trace_valid"]:
            reasons.append("TRACE.md is missing or empty")

    elif current_state == "trace_written" and target_state == "contract_drafted":
        if not direct["contract_valid"]:
            reasons.append("contract draft is missing or empty")

    elif current_state == "contract_drafted" and target_state == "approved_for_execution":
        if not approval_valid:
            reasons.append("approval marker missing")
        if not direct["contract_valid"]:
            reasons.append("contract draft is missing or empty")

    elif current_state == "approved_for_execution" and target_state == "active":
        if not approval_valid:
            reasons.append("approval marker missing")
        if not direct["contract_valid"]:
            reasons.append("contract draft is missing or empty")

    elif current_state == "active" and target_state == "completed":
        if not direct["active_ref"]:
            reasons.append("tasks/active-task.md does not reference the task")
        if not direct["done_valid"]:
            reasons.append("completion evidence is missing")

    elif current_state == "active" and target_state == "failed":
        if not direct["active_ref"]:
            reasons.append("tasks/active-task.md does not reference the task")
        if not direct["failed_valid"]:
            reasons.append("failure evidence is missing")

    elif current_state == "active" and target_state == "dropped":
        if not direct["active_ref"]:
            reasons.append("tasks/active-task.md does not reference the task")
        if not direct["dropped_valid"]:
            reasons.append("drop evidence is missing")

    elif current_state == "failed" and target_state == "brief_draft":
        if not direct["failed_valid"]:
            reasons.append("failed evidence is missing")
        if not (direct["task_exists"] or direct["brief_draft_valid"]):
            reasons.append("updated TASK.md or task brief draft is missing")

    if current_state == "approved_for_execution" and target_state == "active" and not reasons:
        # The output needs to call out that this is a dry-run only.
        pass

    if task_md and not task_md.exists() and current_state == "idea" and target_state == "brief_draft":
        reasons.append("TASK.md is missing")

    if current_state == "brief_approved" and target_state in {"review_ready", "review_blocked"}:
        if not direct["task_exists"]:
            reasons.append("TASK.md is missing")
        if not direct["review_exists"]:
            reasons.append("REVIEW.md is missing")

    if current_state == "review_ready" and target_state == "trace_written" and not direct["review_exists"]:
        reasons.append("REVIEW.md is missing")

    if current_state == "trace_written" and target_state == "contract_drafted" and not direct["trace_valid"]:
        reasons.append("TRACE.md is missing or empty")

    if current_state == "contract_drafted" and target_state in {"approved_for_execution"} and not approval_valid:
        reasons.append(f"approval marker missing at {approval_path}")

    if current_state == "approved_for_execution" and target_state == "active" and approval_valid and direct["contract_valid"]:
        # PASS is possible here; no extra reason needed.
        pass

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

    validator_ok, validator_reasons, validator_error = run_validator(task_dir)
    if validator_error:
        task_id = str(detector_report.get("task_id", task_dir.name))
        current_state = str(detector_report.get("state", "unknown"))
        print_result(task_id, current_state, target_state, [f"validator failed to run: {validator_error}"])
        return 1
    if not validator_ok:
        task_id = str(detector_report.get("task_id", task_dir.name))
        current_state = str(detector_report.get("state", "unknown"))
        print_result(task_id, current_state, target_state, validator_reasons)
        return 1

    task_id = str(detector_report.get("task_id", task_dir.name))
    current_state = str(detector_report.get("state", "unknown"))
    reasons = collect_problem_reasons(current_state, target_state, detector_report, task_dir, task_id)

    note = None
    if not reasons and current_state == "approved_for_execution" and target_state == "active":
        note = "active-task.md replacement is out of scope for Milestone 10"

    print_result(task_id, current_state, target_state, reasons, note=note)
    return 0 if not reasons else 1


if __name__ == "__main__":
    raise SystemExit(main())
