#!/usr/bin/env python3
from pathlib import Path
import sys


TARGET_FILES = [
    "agent-next.py",
    "agent-complete.py",
    "agent-fail.py",
]

REQUIRED_MARKERS = {
    "agent-next.py": ["dry-run", "--dry-run"],
    "agent-complete.py": ["human checkpoint", "confirmation", "requires approval", "manual approval"],
    "agent-fail.py": ["human checkpoint", "confirmation", "requires approval", "manual approval"],
}

UNSAFE_PATTERNS = [
    "shutil.move(",
    "os.rename(",
    "path.rename(",
    "path.replace(",
    "write_text(",
    "open(\"tasks/active-task.md\", \"w\")",
    "open('tasks/active-task.md', 'w')",
    "tasks/active-task.md",
    "tasks/done/",
    "tasks/failed/",
]

SAFETY_MARKERS = [
    "dry-run",
    "--dry-run",
    "human checkpoint",
    "requires approval",
    "manual approval",
    "explicit approval",
    "confirmation required",
    "approved mode disabled",
    "approved mode not implemented",
]


STATUS_PASS = "PASS"
STATUS_WARN = "PASS_WITH_WARNINGS"
STATUS_FAIL = "FAIL"


def usage() -> int:
    print("Usage: python3 scripts/validate-runner-protocol.py [--root <path>]")
    return 2


def parse_args(argv):
    if len(argv) == 0:
        return None
    if len(argv) == 2 and argv[0] == "--root":
        return Path(argv[1]).resolve()
    return "__USAGE_ERROR__"


def find_matches(content_lower: str, patterns):
    return [pattern for pattern in patterns if pattern in content_lower]


def evaluate_file(path: Path, filename: str):
    if not path.is_file():
        return STATUS_WARN, "missing file"

    content = path.read_text(encoding="utf-8")
    content_lower = content.lower()

    required_markers = REQUIRED_MARKERS.get(filename, [])
    if not any(marker in content_lower for marker in required_markers):
        if filename == "agent-next.py":
            return STATUS_FAIL, "missing required marker (dry-run or --dry-run)"
        return STATUS_FAIL, "missing required marker (human checkpoint / confirmation / requires approval / manual approval)"

    unsafe_matches = find_matches(content_lower, UNSAFE_PATTERNS)
    if unsafe_matches:
        has_safety_marker = any(marker in content_lower for marker in SAFETY_MARKERS)
        unsafe_text = ", ".join(unsafe_matches)
        if has_safety_marker:
            return STATUS_WARN, "unsafe patterns found: {0} - safety marker present".format(unsafe_text)
        return STATUS_FAIL, "unsafe pattern without safety marker: {0}".format(unsafe_text)

    return STATUS_PASS, None


def main() -> int:
    root_arg = parse_args(sys.argv[1:])
    if root_arg == "__USAGE_ERROR__":
        return usage()

    repo_root = Path(__file__).resolve().parent.parent
    base_root = repo_root if root_arg is None else root_arg
    scripts_dir = base_root / "scripts"

    print("Runner Protocol Validation")

    results = []
    for filename in TARGET_FILES:
        file_path = scripts_dir / filename
        status, reason = evaluate_file(file_path, filename)
        display_path = "scripts/{0}".format(filename)
        results.append((status, display_path, reason))

    any_fail = any(status == STATUS_FAIL for status, _, _ in results)
    any_warn = any(status == STATUS_WARN for status, _, _ in results)

    for status, display_path, reason in results:
        if reason is None:
            print("{0}: {1}".format(display_path, status))
        else:
            print("{0}: {1} - {2}".format(display_path, status if status != STATUS_WARN else "WARN", reason))

    if any_fail:
        print("Result: FAIL")
        return 1

    if any_warn:
        print("Result: PASS_WITH_WARNINGS")
        return 0

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
