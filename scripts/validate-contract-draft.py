#!/usr/bin/env python3
from pathlib import Path
import sys


REQUIRED_FIELDS = [
    "task_id",
    "generated_from_task",
    "review_file",
    "review_status",
    "execution_allowed",
]
ALLOWED_REVIEW_STATUS = {"READY", "READY_WITH_EDITS"}
EMPTY_MARKERS = {"", "null", "Null", "NULL", "~"}
RISK_HEADINGS = {"## Risk / Rollback", "## Risk and Rollback", "## Risk"}
FORBIDDEN_PHRASES = [
    "replace active-task.md",
    "replaces active-task.md",
    "update active-task.md",
    "updates active-task.md",
    "active-task.md updated",
    "task is now active",
    "promoted to active",
    "approved for execution",
    "execution approved",
    "approval granted",
    "auto-promote",
    "automatic promotion",
]


def strip_outer_quotes(value: str) -> str:
    text = value.strip()
    if len(text) >= 2 and text[0] == text[-1] and text[0] in {"'", '"'}:
        return text[1:-1].strip()
    return text


def parse_frontmatter(content: str):
    lines = content.splitlines()
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


def is_empty(raw_value: str) -> bool:
    cleaned = strip_outer_quotes(raw_value)
    return cleaned in EMPTY_MARKERS


def parse_execution_allowed(raw_value: str):
    lowered = strip_outer_quotes(raw_value).lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return None


def find_forbidden_phrase(content: str):
    lowered = content.lower()
    for phrase in FORBIDDEN_PHRASES:
        if phrase in lowered:
            return phrase
    return None


def has_required_sections(content: str):
    lines = set(content.splitlines())
    has_verification = "## Verification" in lines
    has_risk = any(heading in lines for heading in RISK_HEADINGS)
    return has_verification, has_risk


def validate_metadata(metadata):
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            return "FAIL: missing required field: {0}".format(field)
        if is_empty(metadata[field]):
            return "FAIL: required field must not be empty: {0}".format(field)

    review_status = strip_outer_quotes(metadata["review_status"])
    if review_status not in ALLOWED_REVIEW_STATUS:
        return "FAIL: review_status is not allowed: {0}".format(review_status)

    execution_allowed = parse_execution_allowed(metadata["execution_allowed"])
    if execution_allowed is None:
        return "FAIL: execution_allowed must be true or false"
    if execution_allowed is not True:
        return "FAIL: execution_allowed must be true"

    return None


def optional_path_warnings(root: Path, metadata):
    warnings = []
    generated_path = root / strip_outer_quotes(metadata["generated_from_task"])
    review_path = root / strip_outer_quotes(metadata["review_file"])
    if not generated_path.is_file():
        warnings.append("WARN: generated_from_task path not found: {0}".format(generated_path))
    if not review_path.is_file():
        warnings.append("WARN: review_file path not found: {0}".format(review_path))
    return warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-contract-draft.py tasks/drafts/{task-id}-contract-draft.md")
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

    meta_error = validate_metadata(metadata)
    if meta_error:
        print(meta_error)
        return 1

    has_verification, has_risk = has_required_sections(content)
    if not has_verification:
        print("FAIL: missing required section: ## Verification")
        return 1
    if not has_risk:
        print("FAIL: missing required risk section")
        return 1

    matched_phrase = find_forbidden_phrase(content)
    if matched_phrase is not None:
        print("FAIL: forbidden phrase found: {0}".format(matched_phrase))
        return 1

    repo_root = Path(__file__).resolve().parent.parent
    for warning in optional_path_warnings(repo_root, metadata):
        print(warning)

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
