#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from typing import List, NamedTuple


class TestCase(NamedTuple):
    fixture: str
    mode: str
    expected_result: str
    expected_exit_code: int
    expect_strict_warning: bool
    reject_strict_warning: bool


TEST_CASES = [
    TestCase("valid-template", "normal", "PASS", 0, False, False),
    TestCase("missing-core-file", "normal", "FAIL", 1, False, False),
    TestCase("forbidden-auto-runner", "normal", "FAIL", 1, False, False),
    TestCase("missing-gitignore-drafts", "normal", "FAIL", 1, False, False),
    TestCase("missing-optional-report-warning", "normal", "PASS_WITH_WARNINGS", 0, False, False),
    TestCase("missing-fixtures-warning", "normal", "PASS_WITH_WARNINGS", 0, False, False),
    TestCase("valid-template", "strict", "PASS", 0, False, False),
    TestCase("missing-core-file", "strict", "FAIL", 1, False, True),
    TestCase(
        "missing-optional-report-warning",
        "strict",
        "PASS_WITH_WARNINGS",
        1,
        True,
        False,
    ),
    TestCase("missing-fixtures-warning", "strict", "PASS_WITH_WARNINGS", 1, True, False),
]

STRICT_WARNING_LINE = "Strict mode: FAIL_ON_WARNINGS"


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run_case(root: Path, test_case: TestCase) -> List[str]:
    fixture_path = root / "tests" / "fixtures" / "template-integrity" / test_case.fixture
    checker_path = root / "scripts" / "check-template-integrity.py"
    failures = []

    if not fixture_path.is_dir():
        return ["Missing fixture directory: {0}".format(fixture_path)]

    command = [
        sys.executable,
        str(checker_path),
    ]
    if test_case.mode == "strict":
        command.append("--strict")
    command.extend(["--root", str(fixture_path)])

    completed = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )

    expected_result_line = "Result: {0}".format(test_case.expected_result)
    if expected_result_line not in completed.stdout:
        failures.append("Expected result: {0}".format(test_case.expected_result))
        failures.append("Actual stdout did not contain: {0}".format(expected_result_line))

    if completed.returncode != test_case.expected_exit_code:
        failures.append("Expected exit code: {0}".format(test_case.expected_exit_code))
        failures.append("Actual exit code: {0}".format(completed.returncode))

    if test_case.expect_strict_warning and STRICT_WARNING_LINE not in completed.stdout:
        failures.append("Actual stdout did not contain: {0}".format(STRICT_WARNING_LINE))

    if test_case.reject_strict_warning and STRICT_WARNING_LINE in completed.stdout:
        failures.append("Actual stdout contained forbidden line: {0}".format(STRICT_WARNING_LINE))

    if completed.stderr.strip():
        failures.append("Unexpected stderr: {0}".format(completed.stderr.strip()))

    return failures


def main() -> int:
    root = repo_root()
    has_failures = False

    print("Template Integrity Checker Self-Test")

    for test_case in TEST_CASES:
        failures = run_case(root, test_case)
        label = "{0} [{1}]".format(test_case.fixture, test_case.mode)
        if failures:
            has_failures = True
            print("{0}: FAIL".format(label))
            for failure in failures:
                print("- {0}".format(failure))
        else:
            print("{0}: PASS".format(label))

    if has_failures:
        print("Result: FAIL")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
