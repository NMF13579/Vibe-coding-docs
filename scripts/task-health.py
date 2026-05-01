#!/usr/bin/env python3
from datetime import datetime, UTC
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TASKS_DIR = ROOT / "tasks"
DEFAULT_OUTPUT = ROOT / "reports" / "task-health.md"
REVIEW_STATUSES = [
    "READY",
    "READY_WITH_EDITS",
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
]
QUEUE_STATUSES = ["queued", "blocked", "in_progress", "done", "dropped"]


def usage():
    print("Usage: python3 scripts/task-health.py [--tasks-dir PATH] [--output PATH]")
    return 2


def parse_scalar(value):
    text = value.strip()
    if text == "true":
        return True
    if text == "false":
        return False
    if text == "[]":
        return []
    return text


def parse_key_values(path):
    data = {}
    current_key = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if current_key is not None and isinstance(data.get(current_key), list):
                data[current_key].append(stripped[2:].strip())
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_key = key
        else:
            data[key] = parse_scalar(value)
            current_key = None
    return data


def resolve_input_path(value, default_path):
    if value is None:
        return default_path
    path = Path(value)
    if path.is_absolute():
        return path
    return (ROOT / path).resolve()


def parse_args(argv):
    tasks_dir = DEFAULT_TASKS_DIR
    output = DEFAULT_OUTPUT
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--tasks-dir":
            index += 1
            if index >= len(argv):
                return None
            tasks_dir = resolve_input_path(argv[index], DEFAULT_TASKS_DIR)
            index += 1
        elif arg == "--output":
            index += 1
            if index >= len(argv):
                return None
            output = resolve_input_path(argv[index], DEFAULT_OUTPUT)
            index += 1
        else:
            return None
    return tasks_dir, output


def task_id_from_dir(task_dir):
    return task_dir.name


def find_draft_path(drafts_dir, task_id):
    if not drafts_dir.exists():
        return None
    matches = sorted(drafts_dir.glob(f"{task_id}*.md"))
    if matches:
        return matches[0]
    return None


def draft_has_todo(draft_path):
    if draft_path is None or not draft_path.exists():
        return False
    return "TODO:" in draft_path.read_text(encoding="utf-8")


def collect_queue_entries(queue_dir):
    entries = []
    if not queue_dir.exists():
        return entries
    for path in sorted(queue_dir.glob("*.md")):
        if path.name == "QUEUE.md":
            continue
        data = parse_key_values(path)
        if "queue_status" not in data:
            continue
        entries.append((path, data))
    return entries


def build_metrics(tasks_dir):
    queue_dir = tasks_dir / "queue"
    drafts_dir = tasks_dir / "drafts"
    task_dirs = sorted(
        task_dir for task_dir in tasks_dir.glob("task-*") if task_dir.is_dir() and (task_dir / "TASK.md").exists()
    )
    queue_entries = collect_queue_entries(queue_dir)
    draft_files = sorted(drafts_dir.glob("*.md")) if drafts_dir.exists() else []

    review_counts = {status: 0 for status in REVIEW_STATUSES}
    queue_counts = {status: 0 for status in QUEUE_STATUSES}
    ready_for_contract = []
    attention = {}
    tasks_missing_contract_draft = 0

    for _, entry in queue_entries:
        status = entry.get("queue_status")
        if status in queue_counts:
            queue_counts[status] += 1

    for task_dir in task_dirs:
        task_id = task_id_from_dir(task_dir)
        review_path = task_dir / "REVIEW.md"
        trace_path = task_dir / "TRACE.md"
        draft_path = find_draft_path(drafts_dir, task_id)
        reasons = []

        if not review_path.exists():
            reasons.append("missing REVIEW.md")
        if not trace_path.exists():
            reasons.append("missing TRACE.md")

        review_data = parse_key_values(review_path) if review_path.exists() else {}
        review_status = review_data.get("review_status")
        execution_allowed = review_data.get("execution_allowed")

        if review_status in review_counts:
            review_counts[review_status] += 1

        if review_path.exists() and review_status in {"READY", "READY_WITH_EDITS"} and execution_allowed is True:
            ready_for_contract.append(task_id)

        if review_status == "NEEDS_CLARIFICATION":
            reasons.append("review_status: NEEDS_CLARIFICATION")
        if review_status == "TOO_BROAD":
            reasons.append("review_status: TOO_BROAD")
        if review_status == "TOO_SMALL":
            reasons.append("review_status: TOO_SMALL")
        if review_status == "DUPLICATE":
            reasons.append("review_status: DUPLICATE")
        if review_status == "BLOCKED":
            reasons.append("review_status: BLOCKED")
        if review_path.exists() and execution_allowed is False:
            reasons.append("execution_allowed: false")

        blocked_queue_entry = None
        for queue_path, entry in queue_entries:
            if entry.get("task_id") == task_id and entry.get("queue_status") == "blocked":
                blocked_queue_entry = queue_path
                break
        if blocked_queue_entry is not None:
            reasons.append("queue entry is blocked")

        if draft_has_todo(draft_path):
            reasons.append("contract draft contains TODO:")

        if draft_path is None:
            tasks_missing_contract_draft += 1

        if reasons:
            attention[task_id] = reasons

    return {
        "generated_at": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "tasks_dir": str(tasks_dir),
        "total_task_briefs": len(task_dirs),
        "task_briefs_with_review": sum(1 for task_dir in task_dirs if (task_dir / "REVIEW.md").exists()),
        "task_briefs_without_review": sum(1 for task_dir in task_dirs if not (task_dir / "REVIEW.md").exists()),
        "task_briefs_with_trace": sum(1 for task_dir in task_dirs if (task_dir / "TRACE.md").exists()),
        "task_briefs_without_trace": sum(1 for task_dir in task_dirs if not (task_dir / "TRACE.md").exists()),
        "reviews_ready": review_counts["READY"],
        "reviews_ready_with_edits": review_counts["READY_WITH_EDITS"],
        "reviews_needs_clarification": review_counts["NEEDS_CLARIFICATION"],
        "reviews_too_broad": review_counts["TOO_BROAD"],
        "reviews_too_small": review_counts["TOO_SMALL"],
        "reviews_duplicate": review_counts["DUPLICATE"],
        "reviews_blocked": review_counts["BLOCKED"],
        "contract_drafts_count": len(draft_files),
        "queue_entries_count": len(queue_entries),
        "queue_queued": queue_counts["queued"],
        "queue_blocked": queue_counts["blocked"],
        "queue_in_progress": queue_counts["in_progress"],
        "queue_done": queue_counts["done"],
        "queue_dropped": queue_counts["dropped"],
        "tasks_missing_contract_draft": tasks_missing_contract_draft,
        "tasks_ready_for_contract_generation": ready_for_contract,
        "tasks_requiring_attention": attention,
    }


def render_report(metrics):
    ready_lines = metrics["tasks_ready_for_contract_generation"] or ["(none)"]
    attention = metrics["tasks_requiring_attention"]
    attention_lines = []
    if attention:
        for task_id in sorted(attention):
            attention_lines.append(f"- {task_id}: {', '.join(attention[task_id])}")
    else:
        attention_lines.append("- (none)")

    lines = [
        "# Task Health Report",
        "",
        "## Metadata",
        f"generated_at: {metrics['generated_at']}",
        f"tasks_dir: {metrics['tasks_dir']}",
        "source: task-health",
        "",
        "## Summary",
        f"- Total Task Briefs: {metrics['total_task_briefs']}",
        f"- With Review: {metrics['task_briefs_with_review']}",
        f"- Without Review: {metrics['task_briefs_without_review']}",
        f"- With Trace: {metrics['task_briefs_with_trace']}",
        f"- Without Trace: {metrics['task_briefs_without_trace']}",
        f"- Contract Drafts: {metrics['contract_drafts_count']}",
        f"- Queue Entries: {metrics['queue_entries_count']}",
        "",
        "## Review Status",
        "| Status | Count |",
        "|---|---|",
        f"| READY | {metrics['reviews_ready']} |",
        f"| READY_WITH_EDITS | {metrics['reviews_ready_with_edits']} |",
        f"| NEEDS_CLARIFICATION | {metrics['reviews_needs_clarification']} |",
        f"| TOO_BROAD | {metrics['reviews_too_broad']} |",
        f"| TOO_SMALL | {metrics['reviews_too_small']} |",
        f"| DUPLICATE | {metrics['reviews_duplicate']} |",
        f"| BLOCKED | {metrics['reviews_blocked']} |",
        "",
        "## Queue Status",
        "| Status | Count |",
        "|---|---|",
        f"| queued | {metrics['queue_queued']} |",
        f"| blocked | {metrics['queue_blocked']} |",
        f"| in_progress | {metrics['queue_in_progress']} |",
        f"| done | {metrics['queue_done']} |",
        f"| dropped | {metrics['queue_dropped']} |",
        "",
        "## Ready for Contract Generation",
    ]
    lines.extend(f"- {task_id}" for task_id in ready_lines)
    lines.extend(
        [
            "",
            "## Requiring Attention",
            *attention_lines,
            "",
            "## Notes",
            "This report is read-only.",
            "It does not select tasks.",
            "It does not execute tasks.",
            "It does not modify active-task.md.",
            "",
        ]
    )
    return "\n".join(lines)


def print_summary(metrics):
    print(f"Total Task Briefs: {metrics['total_task_briefs']}")
    print(f"With Review: {metrics['task_briefs_with_review']}")
    print(f"Without Review: {metrics['task_briefs_without_review']}")
    print(f"With Trace: {metrics['task_briefs_with_trace']}")
    print(f"Without Trace: {metrics['task_briefs_without_trace']}")
    print(f"Contract Drafts: {metrics['contract_drafts_count']}")
    print(f"Queue Entries: {metrics['queue_entries_count']}")
    print(f"Ready for Contract Generation: {len(metrics['tasks_ready_for_contract_generation'])}")
    print(f"Requiring Attention: {len(metrics['tasks_requiring_attention'])}")


def main():
    parsed = parse_args(sys.argv[1:])
    if parsed is None:
        return usage()

    tasks_dir, output = parsed
    if not tasks_dir.exists():
        print(f"FAIL: tasks directory not found: {tasks_dir}")
        return 1

    metrics = build_metrics(tasks_dir)
    print_summary(metrics)

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(render_report(metrics), encoding="utf-8")
    print(f"Report written: {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
