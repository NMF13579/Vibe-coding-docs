#!/usr/bin/env python3
import re
import sys
from pathlib import Path


def parse_args(arguments):
    limit = 10
    query_parts = []
    index = 0

    while index < len(arguments):
        value = arguments[index]
        if value == "--limit":
            if index + 1 >= len(arguments):
                return None, None
            limit_value = arguments[index + 1]
            if not limit_value.isdigit() or int(limit_value) <= 0:
                return None, None
            limit = int(limit_value)
            index += 2
            continue
        query_parts.append(value)
        index += 1

    query = " ".join(query_parts).strip()
    if not query:
        return limit, ""
    return limit, query


def tokenize(text):
    tokens = re.split(r"[^\w\-/\.]+", text.lower())
    result = []
    seen = set()
    for token in tokens:
        if not token:
            continue
        if token in seen:
            continue
        seen.add(token)
        result.append(token)
    return result


def parse_repo_map(content):
    if "## Files" not in content:
        return None

    lines = content.splitlines()
    in_files = False
    entries = []
    current = None
    in_headings = False

    for line in lines:
        if not in_files:
            if line.strip() == "## Files":
                in_files = True
            continue

        if line.startswith("## ") and not line.startswith("### "):
            break

        if line.startswith("### "):
            if current is not None:
                entries.append(current)
            current = {
                "path": line[4:].strip(),
                "type": "",
                "headings": [],
            }
            in_headings = False
            continue

        if current is None:
            continue

        stripped = line.strip()
        if stripped.startswith("- type:"):
            current["type"] = stripped[len("- type:"):].strip()
            in_headings = False
            continue
        if stripped == "- headings: []":
            current["headings"] = []
            in_headings = False
            continue
        if stripped == "- headings:":
            current["headings"] = []
            in_headings = True
            continue
        if in_headings and stripped.startswith("- "):
            current["headings"].append(stripped[2:].strip())
            continue
        if stripped.startswith("- ") and not stripped.startswith("- headings"):
            in_headings = False

    if current is not None:
        entries.append(current)

    return entries


def score_entry(entry, tokens):
    path_text = entry["path"].lower()
    type_text = entry["type"].lower()
    headings_text = [heading.lower() for heading in entry["headings"]]
    score = 0

    for token in tokens:
        if token in path_text:
            score += 5
        for heading in headings_text:
            if token in heading:
                score += 3
        if token in type_text:
            score += 1

    if score > 0:
        if entry["path"].startswith("scripts/"):
            score += 2
        if entry["path"].startswith("schemas/"):
            score += 2
        if entry["path"].startswith("policies/"):
            score += 2
        if entry["path"] == "tasks/active-task.md":
            score += 1
        if entry["path"] == "reports/verification.md":
            score += 1

    return score


def main():
    limit, query = parse_args(sys.argv[1:])
    if limit is None:
        print("FAIL: context selection failed")
        print("invalid limit")
        return 1
    if query == "":
        print("FAIL: context selection failed")
        print("missing query")
        return 1

    repo_map_path = Path("repo-map.md")
    if not repo_map_path.exists():
        print("FAIL: context selection failed")
        print("missing file: repo-map.md")
        return 1

    content = repo_map_path.read_text(encoding="utf-8")
    entries = parse_repo_map(content)
    if entries is None:
        print("FAIL: context selection failed")
        print("invalid repo-map format")
        return 1

    tokens = tokenize(query)
    scored = []
    for entry in entries:
        score = score_entry(entry, tokens)
        if score > 0:
            scored.append((score, entry["path"]))

    scored.sort(key=lambda item: (-item[0], item[1]))

    print("Recommended files:")
    for _, path in scored[:limit]:
        print(f"- {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
