#!/usr/bin/env python3
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = ROOT / "templates" / "task-contract-from-brief.md"
DEFAULT_DRAFT_DIR = ROOT / "tasks" / "drafts"
SECTION_RE = re.compile(r"^## .+$")
LIST_ITEM_RE = re.compile(r"^- (.+)$")


def usage():
    print("Usage: python3 scripts/generate-task-contract.py tasks/{task-id}/TASK.md [--output tasks/drafts/{task-id}-contract-draft.md]")
    return 2


def parse_bool(value):
    text = value.strip()
    if text == "true":
        return True
    if text == "false":
        return False
    return text


def extract_metadata(lines):
    return extract_key_values(lines, "## Metadata")


def extract_key_values(lines, section_name):
    start = None
    end = None
    for index, line in enumerate(lines):
        if line == section_name:
            start = index + 1
            continue
        if start is not None and index >= start and SECTION_RE.match(line):
            end = index
            break

    if start is None:
        return {}

    if end is None:
        end = len(lines)

    result = {}
    for line in lines[start:end]:
        stripped = line.strip()
        if not stripped or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        result[key.strip()] = parse_bool(value)
    return result


def extract_section_body(lines, section_name):
    start = None
    end = None
    for index, line in enumerate(lines):
        if line == section_name:
            start = index + 1
            continue
        if start is not None and index >= start and SECTION_RE.match(line):
            end = index
            break

    if start is None:
        return []

    if end is None:
        end = len(lines)

    body = []
    for line in lines[start:end]:
        stripped = line.rstrip()
        if stripped == "":
            continue
        body.append(stripped)
    return body


def extract_list_items(lines, section_name):
    items = []
    for line in extract_section_body(lines, section_name):
        match = LIST_ITEM_RE.match(line.strip())
        if match:
            items.append(match.group(1).strip())
    return items


def section_text(lines, section_name):
    body = extract_section_body(lines, section_name)
    if not body:
        return "TODO: missing from approved Task Brief"
    return " ".join(part.strip() for part in body)


def task_id_from_metadata(metadata, task_path):
    value = metadata.get("task_id")
    if isinstance(value, str) and value.strip():
        return value.strip()
    return task_path.parent.name


def ensure_output_path(task_id, output_arg):
    if output_arg is None:
        path = DEFAULT_DRAFT_DIR / f"{task_id}-contract-draft.md"
    else:
        path = (ROOT / output_arg).resolve() if not Path(output_arg).is_absolute() else Path(output_arg)
    drafts_dir = DEFAULT_DRAFT_DIR.resolve()
    try:
        path.resolve().relative_to(drafts_dir)
    except ValueError:
        print("FAIL: output must be inside tasks/drafts/")
        return None
    return path


def quote_yaml(value):
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def yaml_list(items):
    if not items:
        return ['  - "TODO: missing from approved Task Brief"']
    return [f"  - {quote_yaml(item)}" for item in items]


def build_draft(task_path, review_path, trace_path, task_lines, review_lines, trace_lines):
    task_metadata = extract_metadata(task_lines)
    task_id = task_id_from_metadata(task_metadata, task_path)

    expected_result = section_text(task_lines, "## Expected Result")
    acceptance_criteria = extract_list_items(task_lines, "## Acceptance Criteria")
    out_of_scope = extract_list_items(task_lines, "## Out of Scope")
    dependencies = extract_list_items(task_lines, "## Dependencies")
    rollback_notes = extract_list_items(task_lines, "## Rollback / Reversal Notes")
    risks = extract_list_items(task_lines, "## Risks")
    review_required_edits = extract_list_items(review_lines, "## Required Edits")

    trace_decisions = extract_list_items(trace_lines, "## Decisions Made") if trace_lines else []
    trace_assumptions = extract_list_items(trace_lines, "## Assumptions") if trace_lines else []
    trace_open_questions = extract_list_items(trace_lines, "## Open Questions") if trace_lines else []

    user_story = section_text(task_lines, "## User Story")
    context_text = section_text(task_lines, "## Context")

    goal = user_story
    if goal.startswith("As "):
        goal = user_story

    risk_reason = (
        "Risk requires human review because the approved Task Brief does not provide enough detail."
    )
    if risks:
        risk_reason = " ".join(risks)

    source_trace = str(trace_path.relative_to(ROOT)) if trace_path else "pending"

    lines = [
        "DRAFT ONLY.",
        "This file is not an active execution contract.",
        "Do not execute until human approval replaces tasks/active-task.md.",
        "",
        "task:",
        f"  task_id: {quote_yaml(task_id)}",
        f"  goal: {quote_yaml(goal)}",
        f"  expected_result: {quote_yaml(expected_result)}",
        "  in_scope:",
        *yaml_list(dependencies),
        "  out_of_scope:",
        *yaml_list(out_of_scope),
        '  risk_level: "MEDIUM"',
        f"  risk_reason: {quote_yaml(risk_reason)}",
        "  acceptance_criteria:",
        *yaml_list(acceptance_criteria),
        "  verification_plan:",
        '  - "TODO: define verification command or manual verification step"',
        "  rollback_plan:",
        *yaml_list(rollback_notes),
        f"  source_task: {quote_yaml(str(task_path.relative_to(ROOT)))}",
        f"  source_review: {quote_yaml(str(review_path.relative_to(ROOT)))}",
        f"  source_trace: {quote_yaml(source_trace)}",
        "  human_approval_required: true",
        "",
        "## Supporting Context",
        "",
        f"background: {quote_yaml(context_text)}",
        "dependencies:",
        *yaml_list(dependencies),
        "required_edits:",
        *yaml_list(review_required_edits),
        "decision_context:",
        *yaml_list(trace_decisions),
        "assumptions:",
        *yaml_list(trace_assumptions),
        "open_questions:",
        *yaml_list(trace_open_questions),
        "",
        "## Human Approval Required",
        "Before replacing `tasks/active-task.md`, ask:",
        '"I prepared an executable Task Contract draft from the approved Task Brief.',
        'Do you approve replacing tasks/active-task.md with this contract?"',
        "",
    ]
    return "\n".join(lines)


def main():
    args = sys.argv[1:]
    if not args:
        return usage()

    output_arg = None
    if len(args) == 1:
        task_arg = args[0]
    elif len(args) == 3 and args[1] == "--output":
        task_arg = args[0]
        output_arg = args[2]
    else:
        return usage()

    task_path = Path(task_arg)
    if not task_path.is_absolute():
        task_path = (ROOT / task_path).resolve()
    if not task_path.exists() or task_path.name != "TASK.md":
        print(f"FAIL: invalid TASK.md path: {task_arg}")
        return 2

    if not TEMPLATE_PATH.exists():
        print("Missing required template: templates/task-contract-from-brief.md")
        return 2

    review_path = task_path.parent / "REVIEW.md"
    if not review_path.exists():
        print("FAIL: REVIEW.md not found next to TASK.md")
        return 1

    review_lines = review_path.read_text(encoding="utf-8").splitlines()
    review_metadata = extract_key_values(review_lines, "## Metadata")

    review_status = review_metadata.get("review_status")
    if review_status not in {"READY", "READY_WITH_EDITS"}:
        print("FAIL: review_status must be READY or READY_WITH_EDITS")
        return 1

    if review_metadata.get("execution_allowed") is not True:
        print("FAIL: execution_allowed must be true")
        return 1

    task_lines = task_path.read_text(encoding="utf-8").splitlines()
    task_metadata = extract_metadata(task_lines)
    task_id = task_id_from_metadata(task_metadata, task_path)

    output_path = ensure_output_path(task_id, output_arg)
    if output_path is None:
        return 2
    if output_path.exists():
        print(f"FAIL: output already exists: {output_path.relative_to(ROOT)}")
        return 1

    trace_path = task_path.parent / "TRACE.md"
    trace_lines = trace_path.read_text(encoding="utf-8").splitlines() if trace_path.exists() else None

    DEFAULT_DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    draft_text = build_draft(task_path, review_path, trace_path if trace_path.exists() else None, task_lines, review_lines, trace_lines)
    output_path.write_text(draft_text, encoding="utf-8")
    print(f"PASS: draft created: {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
