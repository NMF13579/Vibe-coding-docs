#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from typing import List, NamedTuple, Optional, Sequence


class Suite(NamedTuple):
    name: str
    command_display: str
    command: Sequence[str]


class SuiteResult(NamedTuple):
    name: str
    passed: bool
    command_display: str
    actual_exit_code: int
    excerpt: Optional[str]


REQUIRED_FILES = [
    "scripts/test-template-integrity.py",
    "scripts/check-template-integrity.py",
    "scripts/test-negative-fixtures.py",
    "tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md",
    "tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md",
    "reports/negative-fixtures-smoke.md",
]

SKIPPED_SUITES = [
    ("review guard failures", "future validator"),
    ("trace guard failures", "future validator"),
    ("queue guard failures", "future validator"),
    ("runner protocol guard failures", "future guard test"),
    ("audit runner", "future milestone"),
    ("release checklist", "future milestone"),
]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def actual_result_from_smoke(smoke_report: Path) -> Optional[str]:
    lines = smoke_report.read_text(encoding="utf-8").splitlines()
    found_section = False
    for line in lines:
        if found_section and line.strip():
            return line.strip()
        if line.strip() == "## Actual Result":
            found_section = True
    return None


def check_prerequisites(root: Path) -> List[str]:
    failures = []
    for relative_path in REQUIRED_FILES:
        path = root / relative_path
        if not path.is_file():
            failures.append("Missing file: {0}".format(relative_path))

    smoke_report = root / "reports/negative-fixtures-smoke.md"
    if smoke_report.is_file():
        actual_result = actual_result_from_smoke(smoke_report)
        if actual_result != "PASS":
            failures.append(
                "Smoke report ## Actual Result is not PASS: {0}".format(
                    actual_result if actual_result is not None else "<missing>"
                )
            )

    return failures


def suites(root: Path) -> List[Suite]:
    return [
        Suite(
            "template-integrity",
            "python3 scripts/test-template-integrity.py",
            [str(root / "scripts/test-template-integrity.py")],
        ),
        Suite(
            "negative-fixtures",
            "python3 scripts/test-negative-fixtures.py",
            [str(root / "scripts/test-negative-fixtures.py")],
        ),
    ]


def output_excerpt(stdout: str, stderr: str) -> Optional[str]:
    combined = "\n".join(part.strip() for part in [stdout, stderr] if part.strip())
    if not combined:
        return None
    return " | ".join(combined.splitlines()[:4])


def run_suite(root: Path, suite: Suite) -> SuiteResult:
    completed = subprocess.run(
        [sys.executable] + list(suite.command),
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    return SuiteResult(
        suite.name,
        completed.returncode == 0,
        suite.command_display,
        completed.returncode,
        output_excerpt(completed.stdout, completed.stderr),
    )


def print_skipped_suites() -> None:
    print("Skipped:")
    for name, reason in SKIPPED_SUITES:
        print("{0}: SKIPPED — {1}".format(name, reason))


def main() -> int:
    root = repo_root()

    print("Guard Failure Test Report")

    prerequisite_failures = check_prerequisites(root)
    if prerequisite_failures:
        print("Prerequisites: FAIL")
        for failure in prerequisite_failures:
            print("- {0}".format(failure))
        print("Result: FAIL")
        return 1

    print("Runnable Suites:")
    results = [run_suite(root, suite) for suite in suites(root)]
    all_passed = True
    for result in results:
        if result.passed:
            print("{0}: PASS".format(result.name))
        else:
            all_passed = False
            print("{0}: FAIL".format(result.name))
            print("- Command: {0}".format(result.command_display))
            print("- Expected exit code: 0")
            print("- Actual exit code: {0}".format(result.actual_exit_code))
            if result.excerpt:
                print("- stdout/stderr excerpt: {0}".format(result.excerpt))

    print_skipped_suites()

    if all_passed:
        print("Result: PASS")
        return 0

    print("Result: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
