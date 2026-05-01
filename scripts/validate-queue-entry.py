#!/usr/bin/env python3
from pathlib import Path
import sys


REQUIRED_FIELDS = ["task_id", "status", "priority", "blocked_by"]
REQUIRED_NON_EMPTY = ["task_id", "status", "priority"]
EMPTY_MARKERS = {"", "null", "Null", "NULL", "~"}
ALLOWED_STATUS = {"queued", "blocked", "in_progress", "done", "dropped"}
ALLOWED_PRIORITY = {"high", "normal", "low"}


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


def parse_inline_list(raw_value: str):
    cleaned = strip_outer_quotes(raw_value)
    if not (cleaned.startswith("[") and cleaned.endswith("]")):
        return None

    inner = cleaned[1:-1].strip()
    if inner == "":
        return []

    items = []
    for part in inner.split(","):
        item = strip_outer_quotes(part.strip())
        if item == "":
            return None
        items.append(item)
    return items


def validate_metadata(metadata):
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            return "FAIL: missing required field: {0}".format(field)

    for field in REQUIRED_NON_EMPTY:
        if is_empty_value(metadata[field]):
            return "FAIL: required field must not be empty: {0}".format(field)

    status = strip_outer_quotes(metadata["status"])
    if status not in ALLOWED_STATUS:
        return "FAIL: status is not allowed: {0}".format(status)

    priority = strip_outer_quotes(metadata["priority"])
    if priority not in ALLOWED_PRIORITY:
        return "FAIL: priority is not allowed: {0}".format(priority)

    blocked_by_items = parse_inline_list(metadata["blocked_by"])
    if blocked_by_items is None:
        return "FAIL: blocked_by must be an inline list"

    if status == "blocked" and len(blocked_by_items) == 0:
        return "FAIL: status blocked requires non-empty blocked_by"

    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-queue-entry.py tasks/queue/{entry}.md")
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

    validation_error = validate_metadata(metadata)
    if validation_error:
        print(validation_error)
        return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
