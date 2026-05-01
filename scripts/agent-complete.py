#!/usr/bin/env python3
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE_DIR = ROOT / "tasks" / "queue"


def parse_scalar(text):
    value = text.strip()
    if value == "true":
        return True
    if value == "false":
        return False
    if value == "[]":
        return []
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1].strip()
    return value


def load_yaml_like(path):
    data = {}
    current_key = None
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            if current_key is not None and isinstance(data.get(current_key), list):
                data[current_key].append(stripped[2:].strip())
            continue
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            data[key] = []
            current_key = key
        else:
            data[key] = parse_scalar(value)
            current_key = None
    return data


def usage():
    print("Usage: python3 scripts/agent-complete.py --dry-run --task-id TASK_ID [--queue-dir PATH]")
    print("Usage: python3 scripts/agent-complete.py --approve-complete --task-id TASK_ID [--queue-dir PATH]")
    return 2


def parse_args(argv):
    dry_run = False
    approve_complete = False
    queue_dir = DEFAULT_QUEUE_DIR
    task_id = None
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--dry-run":
            dry_run = True
            index += 1
        elif arg == "--approve-complete":
            approve_complete = True
            index += 1
        elif arg == "--queue-dir":
            index += 1
            if index >= len(argv):
                return None
            queue_dir = Path(argv[index])
            index += 1
        elif arg == "--task-id":
            index += 1
            if index >= len(argv):
                return None
            task_id = argv[index]
            index += 1
        else:
            return None
    if dry_run == approve_complete or not task_id:
        return None
    return {
        "dry_run": dry_run,
        "approve_complete": approve_complete,
        "queue_dir": queue_dir,
        "task_id": task_id,
    }


def resolve_path(path_value):
    if path_value.is_absolute():
        return path_value
    return (ROOT / path_value).resolve()


def find_task(queue_dir, task_id):
    for path in sorted(queue_dir.glob("*.md")):
        if path.name == "QUEUE.md":
            continue
        data = load_yaml_like(path)
        if data.get("task_id") == task_id:
            return path, data
    return None, None


def main():
    parsed = parse_args(sys.argv[1:])
    if parsed is None:
        return usage()

    if parsed["approve_complete"]:
        print("Approved mode is reserved for a future milestone.")
        return 2

    queue_dir = resolve_path(parsed["queue_dir"])
    if not queue_dir.exists():
        print(f"FAIL: queue directory not found: {parsed['queue_dir']}")
        return 1

    path, data = find_task(queue_dir, parsed["task_id"])
    if path is None:
        print(f"FAIL: task not found in queue: {parsed['task_id']}")
        return 1

    print(f"FOUND: {data.get('task_id')}")
    print(f"QUEUE_ENTRY: {path}")
    print("Verification is complete.")
    print("Do you approve marking this task as done?")
    print("Do not move task to done.")
    print("Do not mark complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
