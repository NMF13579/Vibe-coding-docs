#!/usr/bin/env python3
import json
import sys
from pathlib import Path

import yaml
from jsonschema import validate


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = ROOT / "lessons" / "lessons.md"
SCHEMA_PATH = ROOT / "schemas" / "lessons.schema.json"


def load_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("invalid frontmatter")

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("invalid frontmatter")

    closing_index = -1
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break

    if closing_index == -1:
        raise ValueError("invalid frontmatter")

    for line in lines[closing_index + 1:]:
        if line.strip() == "---":
            raise ValueError("invalid frontmatter")

    frontmatter = "\n".join(lines[1:closing_index])
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("invalid frontmatter")
    return data


def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_TARGET
    target = target if target.is_absolute() else ROOT / target

    if not target.exists():
        raw_path = sys.argv[1] if len(sys.argv) > 1 else "lessons/lessons.md"
        print("FAIL: lessons validation failed")
        print(f"missing file: {raw_path}")
        return 1

    if not SCHEMA_PATH.exists():
        print("FAIL: lessons validation failed")
        print("missing schema: schemas/lessons.schema.json")
        return 1

    try:
        data = load_frontmatter(target)
    except ValueError:
        print("FAIL: lessons validation failed")
        print("invalid frontmatter")
        return 1

    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
    except Exception as error:
        print("FAIL: lessons validation failed")
        print(str(error))
        return 1

    print("PASS: lessons validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
