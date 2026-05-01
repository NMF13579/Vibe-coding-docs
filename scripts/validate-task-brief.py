#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## Metadata",
    "## Context",
    "## User Story",
    "## Expected Result",
    "## Acceptance Criteria",
    "## Out of Scope",
    "## Dependencies",
    "## Risks",
    "## Rollback / Reversal Notes",
    "## Notes",
]

SCHEMA_PATH = Path(__file__).resolve().parents[1] / "schemas" / "task-brief.schema.json"
METADATA_START = "## Metadata"
SECTION_RE = re.compile(r"^## .+$")


def parse_value(text):
    value = text.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    return value


def extract_metadata(lines):
    start = None
    end = None

    for index, line in enumerate(lines):
        if line == METADATA_START:
            start = index + 1
            continue
        if start is not None and index >= start and SECTION_RE.match(line):
            end = index
            break

    if start is None:
        return {}

    if end is None:
        end = len(lines)

    metadata = {}
    for line in lines[start:end]:
        stripped = line.strip()
        if not stripped or ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        metadata[key.strip()] = parse_value(value)
    return metadata


def validate_metadata(metadata, schema):
    errors = []
    for field in schema.get("required", []):
        if field not in metadata:
            errors.append(f"FAIL: missing required metadata field: {field}")

    if "status" in metadata and metadata["status"] != schema["properties"]["status"]["const"]:
        errors.append("FAIL: metadata.status must be APPROVED")

    if "executable" in metadata and metadata["executable"] is not schema["properties"]["executable"]["const"]:
        errors.append("FAIL: metadata.executable must be false")

    return errors


def validate_sections(lines):
    errors = []
    line_set = set(lines)
    for section in REQUIRED_SECTIONS:
        if section not in line_set:
            errors.append(f"FAIL: missing required section: {section}")
    return errors


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md")
        return 2

    target = Path(sys.argv[1])
    if not target.exists():
        print(f"FAIL: file not found: {target}")
        return 1

    if not SCHEMA_PATH.exists():
        print(f"FAIL: schema not found: {SCHEMA_PATH}")
        return 1

    lines = target.read_text(encoding="utf-8").splitlines()
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    metadata = extract_metadata(lines)

    errors = []
    errors.extend(validate_metadata(metadata, schema))
    errors.extend(validate_sections(lines))

    if errors:
      for error in errors:
          print(error)
      return 1

    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
