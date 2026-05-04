#!/usr/bin/env python3
"""Unified read-only test runner for M22 scripted guardrails."""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass(frozen=True)
class CommandCase:
    label: str
    command: list[str]
    expected_exit: int
    required_paths: tuple[Path, ...] = ()


@dataclass(frozen=True)
class Suite:
    name: str
    validator: Path
    cases: tuple[CommandCase, ...]
    required_paths: tuple[Path, ...] = ()


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def exists_all(paths: Iterable[Path]) -> bool:
    return all(path.exists() for path in paths)


def summarize_output(text: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        return "no output"
    if len(lines) == 1:
        return lines[0]
    return " | ".join(lines[:2])


def run_command(command: list[str]) -> tuple[int, str]:
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    output = (completed.stdout or "") + (completed.stderr or "")
    return completed.returncode, summarize_output(output)


def suite_status(result_codes: list[bool], has_missing: bool) -> str:
    if has_missing:
        return "NOT_FOUND"
    if all(result_codes):
        return "PASS"
    return "FAIL"


def build_suites(root: Path) -> tuple[Suite, ...]:
    return (
        Suite(
            name="frontmatter",
            validator=root / "scripts/validate-frontmatter.py",
            required_paths=(
                root / "tests/fixtures/frontmatter/valid",
                root / "tests/fixtures/frontmatter/invalid",
            ),
            cases=(
                CommandCase(
                    label="valid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-frontmatter.py"),
                        str(root / "tests/fixtures/frontmatter/valid"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-frontmatter.py",
                        root / "tests/fixtures/frontmatter/valid",
                    ),
                ),
                CommandCase(
                    label="invalid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-frontmatter.py"),
                        str(root / "tests/fixtures/frontmatter/invalid"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-frontmatter.py",
                        root / "tests/fixtures/frontmatter/invalid",
                    ),
                ),
            ),
        ),
        Suite(
            name="status semantics",
            validator=root / "scripts/validate-status-semantics.py",
            required_paths=(
                root / "scripts/validate-status-semantics.py",
                root / "tests/fixtures/status-semantics/valid",
                root / "tests/fixtures/status-semantics/invalid",
            ),
            cases=(
                CommandCase(
                    label="valid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-status-semantics.py"),
                        str(root / "tests/fixtures/status-semantics/valid"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-status-semantics.py",
                        root / "tests/fixtures/status-semantics/valid",
                    ),
                ),
                CommandCase(
                    label="invalid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-status-semantics.py"),
                        str(root / "tests/fixtures/status-semantics/invalid"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-status-semantics.py",
                        root / "tests/fixtures/status-semantics/invalid",
                    ),
                ),
            ),
        ),
        Suite(
            name="required sections",
            validator=root / "scripts/validate-required-sections.py",
            required_paths=(
                root / "scripts/validate-required-sections.py",
                root / "data/required-sections.json",
                root / "tests/fixtures/required-sections/valid",
                root / "tests/fixtures/required-sections/invalid",
            ),
            cases=(
                CommandCase(
                    label="frontmatter_standard",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "frontmatter_standard",
                        str(root / "tests/fixtures/required-sections/valid/frontmatter-standard.md"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/valid/frontmatter-standard.md",
                    ),
                ),
                CommandCase(
                    label="source_of_truth_map",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "source_of_truth_map",
                        str(root / "tests/fixtures/required-sections/valid/source-of-truth-map.md"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/valid/source-of-truth-map.md",
                    ),
                ),
                CommandCase(
                    label="status_semantics",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "status_semantics",
                        str(root / "tests/fixtures/required-sections/valid/status-semantics.md"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/valid/status-semantics.md",
                    ),
                ),
                CommandCase(
                    label="missing_heading",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "frontmatter_standard",
                        str(root / "tests/fixtures/required-sections/invalid/missing-heading.md"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/invalid/missing-heading.md",
                    ),
                ),
                CommandCase(
                    label="no_headings",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "frontmatter_standard",
                        str(root / "tests/fixtures/required-sections/invalid/no-headings.md"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/invalid/no-headings.md",
                    ),
                ),
                CommandCase(
                    label="mismatched_profile",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "source_of_truth_map",
                        str(root / "tests/fixtures/required-sections/invalid/mismatched-profile.md"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/invalid/mismatched-profile.md",
                    ),
                ),
                CommandCase(
                    label="unknown_profile",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-required-sections.py"),
                        "--profile",
                        "unknown_profile",
                        str(root / "tests/fixtures/required-sections/valid/frontmatter-standard.md"),
                    ],
                    expected_exit=2,
                    required_paths=(
                        root / "scripts/validate-required-sections.py",
                        root / "data/required-sections.json",
                        root / "tests/fixtures/required-sections/valid/frontmatter-standard.md",
                    ),
                ),
            ),
        ),
        Suite(
            name="boundary claims",
            validator=root / "scripts/validate-boundary-claims.py",
            required_paths=(
                root / "scripts/validate-boundary-claims.py",
                root / "tests/fixtures/boundary-claims/valid",
                root / "tests/fixtures/boundary-claims/invalid",
            ),
            cases=(
                CommandCase(
                    label="valid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-boundary-claims.py"),
                        str(root / "tests/fixtures/boundary-claims/valid"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-boundary-claims.py",
                        root / "tests/fixtures/boundary-claims/valid",
                    ),
                ),
                CommandCase(
                    label="invalid",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-boundary-claims.py"),
                        str(root / "tests/fixtures/boundary-claims/invalid"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-boundary-claims.py",
                        root / "tests/fixtures/boundary-claims/invalid",
                    ),
                ),
            ),
        ),
        Suite(
            name="index validator",
            validator=root / "scripts/validate-index.py",
            required_paths=(
                root / "scripts/validate-index.py",
                root / "tests/fixtures/index/valid",
                root / "tests/fixtures/index/invalid",
                root / "tests/fixtures/index/files",
            ),
            cases=(
                CommandCase(
                    label="valid_minimal",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-index.py"),
                        "--index",
                        str(root / "tests/fixtures/index/valid/minimal-index.json"),
                        "--root",
                        str(root / "tests/fixtures/index/files"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-index.py",
                        root / "tests/fixtures/index/valid/minimal-index.json",
                        root / "tests/fixtures/index/files",
                    ),
                ),
                CommandCase(
                    label="valid_unknowns",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-index.py"),
                        "--index",
                        str(root / "tests/fixtures/index/valid/index-with-unknowns.json"),
                        "--root",
                        str(root / "tests/fixtures/index/files"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/validate-index.py",
                        root / "tests/fixtures/index/valid/index-with-unknowns.json",
                        root / "tests/fixtures/index/files",
                    ),
                ),
                CommandCase(
                    label="invalid_missing_entry_field",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-index.py"),
                        "--index",
                        str(root / "tests/fixtures/index/invalid/missing-entry-field.json"),
                        "--root",
                        str(root / "tests/fixtures/index/files"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-index.py",
                        root / "tests/fixtures/index/invalid/missing-entry-field.json",
                        root / "tests/fixtures/index/files",
                    ),
                ),
                CommandCase(
                    label="invalid_unsafe_authority",
                    command=[
                        sys.executable,
                        str(root / "scripts/validate-index.py"),
                        "--index",
                        str(root / "tests/fixtures/index/invalid/unsafe-authority-field.json"),
                        "--root",
                        str(root / "tests/fixtures/index/files"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/validate-index.py",
                        root / "tests/fixtures/index/invalid/unsafe-authority-field.json",
                        root / "tests/fixtures/index/files",
                    ),
                ),
            ),
        ),
        Suite(
            name="metadata consistency audit",
            validator=root / "scripts/audit-metadata-consistency.py",
            required_paths=(
                root / "scripts/audit-metadata-consistency.py",
                root / "tests/fixtures/metadata-consistency/valid",
                root / "tests/fixtures/metadata-consistency/warn",
                root / "tests/fixtures/metadata-consistency/invalid",
            ),
            cases=(
                CommandCase(
                    label="valid_clean",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/valid/index-clean.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/valid/files"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/valid/index-clean.json",
                        root / "tests/fixtures/metadata-consistency/valid/files",
                    ),
                ),
                CommandCase(
                    label="warn_unknowns",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/warn/index-with-unknowns.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/warn/files"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/warn/index-with-unknowns.json",
                        root / "tests/fixtures/metadata-consistency/warn/files",
                    ),
                ),
                CommandCase(
                    label="warn_entry_warnings",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/warn/index-with-entry-warnings.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/warn/files"),
                    ],
                    expected_exit=0,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/warn/index-with-entry-warnings.json",
                        root / "tests/fixtures/metadata-consistency/warn/files",
                    ),
                ),
                CommandCase(
                    label="invalid_missing_path",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/invalid/index-missing-path.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/invalid/files"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/invalid/index-missing-path.json",
                        root / "tests/fixtures/metadata-consistency/invalid/files",
                    ),
                ),
                CommandCase(
                    label="invalid_duplicate_path",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/invalid/index-duplicate-path.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/invalid/files"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/invalid/index-duplicate-path.json",
                        root / "tests/fixtures/metadata-consistency/invalid/files",
                    ),
                ),
                CommandCase(
                    label="invalid_unsafe_authority",
                    command=[
                        sys.executable,
                        str(root / "scripts/audit-metadata-consistency.py"),
                        "--index",
                        str(root / "tests/fixtures/metadata-consistency/invalid/index-unsafe-authority-field.json"),
                        "--root",
                        str(root / "tests/fixtures/metadata-consistency/invalid/files"),
                    ],
                    expected_exit=1,
                    required_paths=(
                        root / "scripts/audit-metadata-consistency.py",
                        root / "tests/fixtures/metadata-consistency/invalid/index-unsafe-authority-field.json",
                        root / "tests/fixtures/metadata-consistency/invalid/files",
                    ),
                ),
            ),
        ),
    )


def run_suite(root: Path, suite: Suite) -> tuple[str, list[str]]:
    lines: list[str] = [f"SUITE: {suite.name}"]
    missing = [path for path in (suite.validator, *suite.required_paths) if not path.exists()]
    if missing:
        lines.append("RESULT: NOT_FOUND")
        for path in missing:
            lines.append(f"  missing: {path}")
        return "NOT_FOUND", lines

    case_results: list[bool] = []
    has_missing = False

    for case in suite.cases:
        case_missing = [path for path in case.required_paths if not path.exists()]
        if case_missing:
            has_missing = True
            case_results.append(False)
            lines.append(f"CASE: {case.label}")
            lines.append("  RESULT: NOT_FOUND")
            lines.append(f"  COMMAND: {' '.join(case.command)}")
            lines.append(f"  EXPECTED: {case.expected_exit}")
            lines.append(f"  ACTUAL: NOT_RUN")
            for path in case_missing:
                lines.append(f"  missing: {path}")
            continue

        actual_exit, summary = run_command(case.command)
        passed = actual_exit == case.expected_exit
        case_results.append(passed)
        lines.append(f"CASE: {case.label}")
        lines.append(f"  RESULT: {'PASS' if passed else 'FAIL'}")
        lines.append(f"  COMMAND: {' '.join(case.command)}")
        lines.append(f"  EXPECTED: {case.expected_exit}")
        lines.append(f"  ACTUAL: {actual_exit}")
        lines.append(f"  OUTPUT: {summary}")

    suite_result = suite_status(case_results, has_missing)
    lines.insert(1, f"RESULT: {suite_result}")
    return suite_result, lines


def main() -> int:
    root = repo_root()
    suites = build_suites(root)
    results: list[str] = []
    overall_missing = False
    overall_fail = False

    for suite in suites:
        suite_result, lines = run_suite(root, suite)
        results.append(suite_result)
        if suite_result == "NOT_FOUND":
            overall_missing = True
        elif suite_result != "PASS":
            overall_fail = True
        for line in lines:
            print(line)

    print("FINAL SUMMARY")
    for name, status in zip((suite.name for suite in suites), results):
        print(f"  {name}: {status}")

    if overall_missing or overall_fail:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
