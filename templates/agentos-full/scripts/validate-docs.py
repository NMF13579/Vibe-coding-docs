#!/usr/bin/env python3
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

MODULES = ["core-rules", "state", "workflow", "quality", "security"]
REQUIRED_FIELDS = ["type", "module", "status", "authority", "when_to_read", "owner"]
ALLOWED_STATUS = {"draft", "canonical", "active", "stub"}


def parse_frontmatter(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return None
    data = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def fail(msg):
    print(f"FAIL {msg}")


def main():
    errors = 0

    for module in MODULES:
        main_path = ROOT / module / "MAIN.md"
        if not main_path.exists():
            fail(f"Missing module entry: {module}/MAIN.md")
            errors += 1
            continue

        fm = parse_frontmatter(main_path)
        if fm is None:
            fail(f"Missing or invalid frontmatter in {main_path.relative_to(ROOT)}")
            errors += 1
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm or fm[field] == "":
                fail(f"Missing frontmatter field '{field}' in {main_path.relative_to(ROOT)}")
                errors += 1

        if fm.get("type") != "canonical":
            fail(f"type must be canonical in {main_path.relative_to(ROOT)}")
            errors += 1

        if fm.get("authority") != "canonical":
            fail(f"authority must be canonical in {main_path.relative_to(ROOT)}")
            errors += 1

        if fm.get("module") != module:
            fail(
                f"module mismatch in {main_path.relative_to(ROOT)}: expected '{module}' got '{fm.get('module', '')}'"
            )
            errors += 1

        if fm.get("status") not in ALLOWED_STATUS:
            fail(f"status must be one of {sorted(ALLOWED_STATUS)} in {main_path.relative_to(ROOT)}")
            errors += 1

        if fm.get("when_to_read") != "always":
            fail(f"when_to_read must be always in {main_path.relative_to(ROOT)}")
            errors += 1

    if errors:
        print(f"\nFound {errors} validation error(s) in module docs.")
        return 1

    print("validate-docs passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
