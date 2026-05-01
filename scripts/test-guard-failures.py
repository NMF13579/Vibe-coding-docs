#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from typing import List, NamedTuple, Optional, Sequence


class Suite(NamedTuple):
    name: str
    command_display: str
    command: Sequence[str]
    optional: bool = False


class SuiteResult(NamedTuple):
    name: str
    status: str
    optional: bool
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
    result = [
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
    runner_protocol = root / "scripts/validate-runner-protocol.py"
    if runner_protocol.is_file():
        result.append(
            Suite(
                "runner-protocol",
                "python3 scripts/validate-runner-protocol.py",
                [str(runner_protocol)],
                optional=True,
            )
        )
    return result


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
    suite_status = "PASS"
    if completed.returncode != 0:
        suite_status = "FAIL"
    else:
        combined = "\n".join([completed.stdout or "", completed.stderr or ""])
        if "Result: PASS_WITH_WARNINGS" in combined:
            suite_status = "PASS_WITH_WARNINGS"

    return SuiteResult(
        suite.name,
        suite_status,
        suite.optional,
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
    has_failures = False
    has_warnings = False
    for result in results:
        if result.status == "PASS":
            print("{0}: PASS".format(result.name))
        elif result.status == "PASS_WITH_WARNINGS":
            has_warnings = True
            print("{0}: PASS_WITH_WARNINGS".format(result.name))
            if result.excerpt:
                print("- stdout/stderr excerpt: {0}".format(result.excerpt))
        else:
            if result.optional:
                has_warnings = True
                print("{0}: WARN - optional suite failed".format(result.name))
                print("- Command: {0}".format(result.command_display))
                print("- Expected exit code: 0")
                print("- Actual exit code: {0}".format(result.actual_exit_code))
                if result.excerpt:
                    print("- stdout/stderr excerpt: {0}".format(result.excerpt))
            else:
                has_failures = True
                print("{0}: FAIL".format(result.name))
                print("- Command: {0}".format(result.command_display))
                print("- Expected exit code: 0")
                print("- Actual exit code: {0}".format(result.actual_exit_code))
                if result.excerpt:
                    print("- stdout/stderr excerpt: {0}".format(result.excerpt))

    print_skipped_suites()

    if has_failures:
        print("Result: FAIL")
        return 1

    if has_warnings:
        print("Result: PASS_WITH_WARNINGS")
        return 0

    if not has_failures:
        print("Result: PASS")
        return 0


if __name__ == "__main__":
    sys.exit(main())
