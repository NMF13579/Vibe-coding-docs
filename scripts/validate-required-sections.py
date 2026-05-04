#!/usr/bin/env python3
"""Read-only required sections validator (MVP)."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*$")


class ValidationUsageError(Exception):
    pass


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate required Markdown headings by profile")
    parser.add_argument("target", help="Markdown file or directory")
    parser.add_argument("--profile", required=True, help="Profile name from config")
    parser.add_argument("--config", default="data/required-sections.json", help="Path to config JSON")
    return parser.parse_args(argv)


def load_config(config_path: Path) -> dict:
    if not config_path.is_file():
        raise ValidationUsageError(f"config file not found: {config_path}")
    try:
        data = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ValidationUsageError(f"invalid config JSON: {exc}") from exc

    if not isinstance(data, dict) or "profiles" not in data:
        raise ValidationUsageError("config must contain object field: profiles")
    if not isinstance(data["profiles"], dict):
        raise ValidationUsageError("config field profiles must be an object")
    return data


def collect_markdown_files(target: Path) -> list[Path]:
    if not target.exists():
        raise ValidationUsageError(f"target not found: {target}")
    if target.is_file():
        if target.suffix.lower() != ".md":
            raise ValidationUsageError("file target must be a .md file")
        return [target]
    if target.is_dir():
        return sorted([p for p in target.rglob("*.md") if p.is_file()])
    raise ValidationUsageError(f"unsupported target type: {target}")


def extract_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = HEADING_RE.match(line)
        if match:
            headings.append(match.group(1).strip())
    return headings


def validate_file(path: Path, required_headings: list[str]) -> tuple[str, list[str]]:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception as exc:
        return "ERROR", [f"cannot read file: {exc}"]

    headings = extract_headings(text)
    if not headings:
        return "FAIL", ["no markdown headings found"]

    missing = [h for h in required_headings if h not in headings]
    if missing:
        return "FAIL", [f"missing required heading: {m}" for m in missing]

    return "PASS", ["all required headings present"]


def main(argv: list[str]) -> int:
    try:
        args = parse_args(argv)
        config_path = Path(args.config)
        target_path = Path(args.target)

        config = load_config(config_path)
        profiles = config["profiles"]

        if args.profile not in profiles:
            raise ValidationUsageError(f"unknown profile: {args.profile}")

        profile = profiles[args.profile]
        if not isinstance(profile, dict) or "required_headings" not in profile:
            raise ValidationUsageError(f"invalid profile structure: {args.profile}")
        required_headings = profile["required_headings"]
        if not isinstance(required_headings, list) or not all(isinstance(x, str) and x for x in required_headings):
            raise ValidationUsageError(f"required_headings must be non-empty strings: {args.profile}")

        files = collect_markdown_files(target_path)

    except ValidationUsageError as exc:
        print(f"ERROR: {exc}")
        return 2
    except Exception as exc:
        print(f"ERROR: unexpected: {exc}")
        return 2

    if not files:
        print("FAIL: no markdown files found in target")
        print("SUMMARY: PASS=0 WARN=0 FAIL=1 ERROR=0")
        return 1

    counts = {"PASS": 0, "WARN": 0, "FAIL": 0, "ERROR": 0}

    for path in files:
        status, details = validate_file(path, required_headings)
        counts[status] += 1
        print(f"{status}: {path}")
        for item in details:
            print(f"  - {item}")

    print(
        "SUMMARY: "
        f"PASS={counts['PASS']} "
        f"WARN={counts['WARN']} "
        f"FAIL={counts['FAIL']} "
        f"ERROR={counts['ERROR']}"
    )

    if counts["FAIL"] > 0:
        return 1
    if counts["ERROR"] > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
