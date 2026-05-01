#!/usr/bin/env python3
import pathlib
import sys

import yaml
from jsonschema import validate

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_TARGET = ROOT / "tasks" / "active-task.md"
SCHEMA_PATH = ROOT / "schemas" / "task.schema.json"


def load_frontmatter(markdown_path: pathlib.Path):
    text = markdown_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("frontmatter is missing")

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("frontmatter is missing")

    try:
        closing_index = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    except StopIteration as exc:
        raise ValueError("frontmatter is missing") from exc

    for line in lines[closing_index + 1 :]:
        if line.strip() == "---":
            raise ValueError("more than one frontmatter block found")

    frontmatter = "\n".join(lines[1:closing_index])
    data = yaml.safe_load(frontmatter)
    if not isinstance(data, dict):
        raise ValueError("frontmatter must be a YAML object")
    return data


def main():
    target = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else DEFAULT_TARGET
    try:
      data = load_frontmatter(target)
      schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
      validate(instance=data, schema=schema)
      print("PASS: task validation passed")
      return 0
    except Exception as exc:
      print("FAIL: task validation failed")
      print(str(exc))
      return 1


if __name__ == "__main__":
    sys.exit(main())
