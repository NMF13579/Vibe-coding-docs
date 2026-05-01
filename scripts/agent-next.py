#!/usr/bin/env python3
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_QUEUE_DIR = ROOT / "tasks" / "queue"
PRIORITY_ORDER = {"high": 0, "normal": 1, "low": 2}


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
    print("Usage: python3 scripts/agent-next.py --dry-run [--queue-dir PATH] [--contract-draft PATH]")
    print("Usage: python3 scripts/agent-next.py --approve-start --contract-draft PATH [--queue-dir PATH]")
    return 2


def parse_args(argv):
    dry_run = False
    approve_start = False
    queue_dir = DEFAULT_QUEUE_DIR
    contract_draft = None
    index = 0
    while index < len(argv):
        arg = argv[index]
        if arg == "--dry-run":
            dry_run = True
            index += 1
        elif arg == "--approve-start":
            approve_start = True
            index += 1
        elif arg == "--queue-dir":
            index += 1
            if index >= len(argv):
                return None
            queue_dir = Path(argv[index])
            index += 1
        elif arg == "--contract-draft":
            index += 1
            if index >= len(argv):
                return None
            contract_draft = argv[index]
            index += 1
        else:
            return None
    if dry_run == approve_start:
        return None
    return {
        "dry_run": dry_run,
        "approve_start": approve_start,
        "queue_dir": queue_dir,
        "contract_draft": contract_draft,
    }


def resolve_path(path_value):
    if path_value.is_absolute():
        return path_value
    return (ROOT / path_value).resolve()


def find_candidate(queue_dir):
    entries = []
    for path in sorted(queue_dir.glob("*.md")):
        if path.name == "QUEUE.md":
            continue
        data = load_yaml_like(path)
        status = data.get("status")
        if status is None:
            status = data.get("queue_status")
        if status != "queued":
            continue
        execution_allowed = data.get("execution_allowed")
        if execution_allowed is False:
            continue
        blocked_by = data.get("blocked_by", [])
        if blocked_by != []:
            continue
        contract_draft = data.get("source_contract_draft")
        if isinstance(contract_draft, str) and contract_draft:
            contract_path = resolve_path(Path(contract_draft))
            if not contract_path.exists():
                continue
        priority = str(data.get("priority", "normal"))
        entries.append((PRIORITY_ORDER.get(priority, 1), path.name, data, path))
    if not entries:
        return None
    entries.sort(key=lambda item: (item[0], item[1]))
    return entries[0]


def main():
    parsed = parse_args(sys.argv[1:])
    if parsed is None:
        return usage()

    if parsed["approve_start"]:
        print("Approved mode is reserved for a future milestone.")
        return 2

    queue_dir = resolve_path(parsed["queue_dir"])
    if not queue_dir.exists():
        print(f"FAIL: queue directory not found: {parsed['queue_dir']}")
        return 1

    candidate = find_candidate(queue_dir)
    if candidate is None:
        print("No queued task is ready for dry-run selection.")
        return 1

    _, _, data, path = candidate
    print(f"SELECTED: {data.get('task_id', path.stem)}")
    print(f"QUEUE_ENTRY: {path}")
    print("I found the next queued task and prepared its contract draft.")
    print("Do you approve replacing tasks/active-task.md and starting execution?")
    print("Do not modify tasks/active-task.md.")
    print("Do not run execution.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
