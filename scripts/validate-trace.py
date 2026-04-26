#!/usr/bin/env python3
from pathlib import Path
import sys


REQUIRED_FIELDS = ["task_id", "source_summary", "decision_rationale"]
EMPTY_MARKERS = {"", "null", "Null", "NULL", "~"}
FORBIDDEN_PHRASES = [
    "execution approved",
    "approved for execution",
    "execution_allowed: true",
    "authorizes execution",
    "approval granted",
    "trace replaces task.md",
    "trace replaces review.md",
    "replaces task.md",
    "replaces review.md",
    "active-task.md updated",
    "active task updated",
    "task is now active",
]


def strip_outer_quotes(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        return text[1:-1].strip()
    return text


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, "FAIL: malformed frontmatter: missing opening ---"

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index is None:
        return None, "FAIL: malformed frontmatter: missing closing ---"

    metadata = {}
    for line in lines[1:closing_index]:
        stripped = line.strip()
        if not stripped:
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        metadata[key.strip()] = value.strip()
    return metadata, None


def is_empty_value(raw_value: str) -> bool:
    cleaned = strip_outer_quotes(raw_value)
    return cleaned in EMPTY_MARKERS


def validate_required_fields(metadata):
    for field in REQUIRED_FIELDS:
        raw_value = metadata.get(field)
        if raw_value is None:
            return "FAIL: missing required field: {0}".format(field)
        if is_empty_value(raw_value):
            return "FAIL: required field must not be empty: {0}".format(field)
    return None


def find_forbidden_phrase(text: str):
    lowered = text.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lowered:
            return phrase
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-trace.py tasks/{task-id}/TRACE.md")
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print("FAIL: file not found: {0}".format(target))
        return 1

    content = target.read_text(encoding="utf-8")
    metadata, parse_error = parse_frontmatter(content)
    if parse_error:
        print(parse_error)
        return 1

    fields_error = validate_required_fields(metadata)
    if fields_error:
        print(fields_error)
        return 1

    matched = find_forbidden_phrase(content)
    if matched is not None:
        print("FAIL: forbidden phrase found: {0}".format(matched))
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
