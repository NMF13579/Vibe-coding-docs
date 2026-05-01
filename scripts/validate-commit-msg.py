#!/usr/bin/env python3
import re
import sys
from pathlib import Path


ALLOWED_BLOCKS = ["Intent:", "Task:", "Verification:", "Risk:"]
SUBJECT_RE = re.compile(r"^(feat|fix|docs|chore|refactor|test|security|ci)\([a-z0-9._-]+\): .{5,}$")


def strip_comments(lines):
    result = []
    for line in lines:
        if line.startswith("#"):
            continue
        result.append(line)
    return result


def parse_blocks(lines):
    blocks = {}
    current_block = None

    for line in lines:
        if line in ALLOWED_BLOCKS:
            current_block = line[:-1]
            blocks[current_block] = []
            continue
        if current_block is not None:
            blocks[current_block].append(line)

    cleaned = {}
    for name, block_lines in blocks.items():
        start = 0
        end = len(block_lines)
        while start < end and block_lines[start].strip() == "":
            start += 1
        while end > start and block_lines[end - 1].strip() == "":
            end -= 1
        cleaned[name] = "\n".join(block_lines[start:end]).strip()
    return cleaned


def main():
    if len(sys.argv) < 2:
        print("FAIL: commit message validation failed")
        print("missing commit message path")
        return 1

    path_text = sys.argv[1]
    path = Path(path_text)
    if not path.exists():
        print("FAIL: commit message validation failed")
        print(f"missing file: {path_text}")
        return 1

    text = path.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
    lines = strip_comments(text.split("\n"))

    subject = ""
    body_start = 0
    for index, line in enumerate(lines):
        if line.strip():
            subject = line.strip()
            body_start = index + 1
            break

    body_lines = lines[body_start:]
    blocks = parse_blocks(body_lines)
    violations = []

    if not subject or not SUBJECT_RE.match(subject):
        violations.append("invalid subject format")
    else:
        summary = subject.split(": ", 1)[1].strip()
        if summary in ("WIP", "TODO"):
            violations.append("invalid subject format")

    if "Intent" not in blocks:
        violations.append("missing Intent block")
    else:
        if not blocks["Intent"]:
            violations.append("empty Intent block")
        elif blocks["Intent"] == "TODO":
            violations.append("Intent must not be TODO")

    if "Task" not in blocks:
        violations.append("missing Task block")
    else:
        if not blocks["Task"]:
            violations.append("empty Task block")
        elif blocks["Task"] == "TODO":
            violations.append("Task must not be TODO")
        elif not blocks["Task"].startswith("task-"):
            violations.append("Task must start with task-")

    if "Verification" not in blocks:
        violations.append("missing Verification block")
    else:
        if not blocks["Verification"]:
            violations.append("empty Verification block")
        elif "PASS" not in blocks["Verification"]:
            violations.append("Verification must contain PASS")

    if "Risk" not in blocks:
        violations.append("missing Risk block")
    else:
        if not blocks["Risk"]:
            violations.append("empty Risk block")
        elif blocks["Risk"] not in ("LOW", "MEDIUM", "HIGH", "CRITICAL"):
            violations.append("invalid Risk value")

    if violations:
        print("FAIL: commit message validation failed")
        for violation in violations:
            print(f"violation: {violation}")
        return 1

    print("PASS: commit message validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
