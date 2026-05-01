#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys


REQUIRED_TASK_DIRS = ["queue", "done", "dropped"]


def parse_args(argv):
    if len(argv) == 0:
        return None
    if len(argv) == 2 and argv[0] == "--root":
        return argv[1]
    return "__USAGE_ERROR__"


def find_md_files(directory: Path):
    files = []
    for child in sorted(directory.iterdir(), key=lambda path: path.name):
        if not child.is_file():
            continue
        if child.name.startswith("."):
            continue
        if child.name == ".gitkeep":
            continue
        if child.suffix != ".md":
            continue
        if child.name == "QUEUE.md":
            continue
        files.append(child)
    return files


def main():
    repo_root = Path(__file__).resolve().parent.parent
    entry_validator_path = repo_root / "scripts" / "validate-queue-entry.py"

    if not entry_validator_path.is_file():
        print("Prerequisites: FAIL — scripts/validate-queue-entry.py not found")
        print("Result: FAIL")
        return 1

    root_arg = parse_args(sys.argv[1:])
    if root_arg == "__USAGE_ERROR__":
        print("Usage: python3 scripts/validate-queue.py [--root <path>]")
        return 2

    base_root = repo_root if root_arg is None else Path(root_arg).resolve()

    required_dirs = {
        name: base_root / "tasks" / name for name in REQUIRED_TASK_DIRS
    }

    print("Queue Directory Validation")

    for name in REQUIRED_TASK_DIRS:
        if not required_dirs[name].is_dir():
            print("FAIL: required directory not found: tasks/{0}".format(name))
            print("Result: FAIL")
            return 1

    md_files = []
    for name in REQUIRED_TASK_DIRS:
        md_files.extend(find_md_files(required_dirs[name]))

    if not md_files:
        print("No queue entry .md files found.")
        print("Required directories exist.")
        print("Result: PASS")
        return 0

    all_passed = True
    for path in md_files:
        completed = subprocess.run(
            [sys.executable, str(entry_validator_path), str(path)],
            cwd=str(repo_root),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
        )
        display = str(path.relative_to(base_root))
        if completed.returncode == 0:
            print("{0}: PASS".format(display))
        else:
            all_passed = False
            print("{0}: FAIL".format(display))

    if all_passed:
        print("Result: PASS")
        return 0

    print("Result: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
