#!/usr/bin/env python3
from pathlib import Path
import sys


ALLOWED_REVIEW_STATUS = {
    "READY",
    "READY_WITH_EDITS",
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}

REQUIRES_TRUE = {"READY", "READY_WITH_EDITS"}
REQUIRES_FALSE = {
    "NEEDS_CLARIFICATION",
    "TOO_BROAD",
    "TOO_SMALL",
    "DUPLICATE",
    "BLOCKED",
}

EMPTY_MARKERS = {"", "null", "Null", "NULL", "~"}


def strip_outer_quotes(value: str) -> str:
    text = value.strip()
    if len(text) >= 2:
        if text[0] == text[-1] and text[0] in {"'", '"'}:
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


def parse_execution_allowed(raw_value: str):
    cleaned = strip_outer_quotes(raw_value)
    lowered = cleaned.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return None


def validate_metadata(metadata):
    review_status_raw = metadata.get("review_status")
    execution_allowed_raw = metadata.get("execution_allowed")

    if review_status_raw is None:
        return "FAIL: missing required field: review_status"
    if execution_allowed_raw is None:
        return "FAIL: missing required field: execution_allowed"

    if is_empty_value(review_status_raw):
        return "FAIL: review_status must not be empty"
    if is_empty_value(execution_allowed_raw):
        return "FAIL: execution_allowed must not be empty"

    review_status = strip_outer_quotes(review_status_raw)
    if review_status not in ALLOWED_REVIEW_STATUS:
        return "FAIL: review_status is not allowed: {0}".format(review_status)

    execution_allowed = parse_execution_allowed(execution_allowed_raw)
    if execution_allowed is None:
        return "FAIL: execution_allowed must be true or false"

    if review_status in REQUIRES_TRUE and execution_allowed is not True:
        return "FAIL: review_status {0} requires execution_allowed true".format(review_status)
    if review_status in REQUIRES_FALSE and execution_allowed is not False:
        return "FAIL: review_status {0} requires execution_allowed false".format(review_status)

    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-review.py tasks/{task-id}/REVIEW.md")
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print("FAIL: file not found: {0}".format(target))
        return 1

    metadata, parse_error = parse_frontmatter(target.read_text(encoding="utf-8"))
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
