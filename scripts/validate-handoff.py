#!/usr/bin/env python3
import pathlib
import sys

import yaml
from jsonschema import validate

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_TARGET = ROOT / "handoff" / "HANDOFF.md"
SCHEMA_PATH = ROOT / "schemas" / "handoff.schema.json"


def load_frontmatter(markdown_path: pathlib.Path):
    text = markdown_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("invalid frontmatter")

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("invalid frontmatter")

    try:
        closing_index = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("invalid frontmatter") from exc

    for line in lines[closing_index + 1 :]:
        if line.strip() == "---":
            raise ValueError("invalid frontmatter")

    frontmatter = "\n".join(lines[1:closing_index])
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("invalid frontmatter")
    return data


def main():
    target_arg = sys.argv[1] if len(sys.argv) > 1 else "handoff/HANDOFF.md"
    target = pathlib.Path(target_arg).resolve() if len(sys.argv) > 1 else DEFAULT_TARGET

    if not target.exists():
        print("FAIL: handoff validation failed")
        print(f"missing file: {target_arg}")
        return 1

    if not SCHEMA_PATH.exists():
        print("FAIL: handoff validation failed")
        print("missing schema: schemas/handoff.schema.json")
        return 1

    try:
        data = load_frontmatter(target)
        schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
        validate(instance=data, schema=schema)
        print("PASS: handoff validation passed")
        return 0
    except ValueError:
        print("FAIL: handoff validation failed")
        print("invalid frontmatter")
        return 1
    except Exception as exc:
        print("FAIL: handoff validation failed")
        print(str(exc))
        return 1


if __name__ == "__main__":
    sys.exit(main())
