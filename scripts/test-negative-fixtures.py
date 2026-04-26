#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
from typing import List, NamedTuple, Optional, Sequence, Set


class Case(NamedTuple):
    name: str
    command: Sequence[str]


class CaseResult(NamedTuple):
    name: str
    passed: bool
    details: List[str]


SKIPPED_GROUPS = [
    ("review", "future validator"),
    ("trace", "future validator"),
    ("queue", "future validator"),
    ("runner", "future guard test"),
]


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def rel(path: Path, root: Path) -> str:
    return str(path.relative_to(root))


def required_paths(root: Path) -> List[Path]:
    return [
        root / "tests/fixtures/negative",
        root / "tests/fixtures/negative/README.md",
        root / "tests/fixtures/negative/task-brief",
        root / "tests/fixtures/negative/contract-generation",
        root / "tests/fixtures/template-integrity",
        root / "scripts/validate-task-brief.py",
        root / "scripts/generate-task-contract.py",
        root / "scripts/check-template-integrity.py",
        root / "tests/fixtures/negative/task-brief/missing-metadata/TASK.md",
        root / "tests/fixtures/negative/task-brief/executable-true/TASK.md",
        root / "tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK.md",
        root / "tests/fixtures/negative/task-brief/status-not-approved/TASK.md",
        root / "tests/fixtures/negative/contract-generation/missing-review/task-example",
        root / "tests/fixtures/negative/contract-generation/missing-review/task-example/TASK.md",
        root / "tests/fixtures/negative/contract-generation/review-not-ready/task-example",
        root / "tests/fixtures/negative/contract-generation/review-not-ready/task-example/TASK.md",
        root / "tests/fixtures/negative/contract-generation/review-not-ready/task-example/REVIEW.md",
        root / "tests/fixtures/negative/contract-generation/execution-not-allowed/task-example",
        root / "tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/TASK.md",
        root / "tests/fixtures/negative/contract-generation/execution-not-allowed/task-example/REVIEW.md",
        root / "tests/fixtures/negative/contract-generation/draft-already-exists/task-example",
        root / "tests/fixtures/negative/contract-generation/draft-already-exists/task-example/TASK.md",
        root / "tests/fixtures/negative/contract-generation/draft-already-exists/task-example/REVIEW.md",
        root / "tests/fixtures/negative/contract-generation/draft-already-exists/drafts/task-example-contract-draft.md",
        root / "tests/fixtures/template-integrity/missing-core-file",
        root / "tests/fixtures/template-integrity/forbidden-auto-runner",
        root / "tests/fixtures/template-integrity/missing-gitignore-drafts",
    ]


def check_prerequisites(root: Path) -> List[str]:
    failures = []
    for path in required_paths(root):
        if not path.exists():
            kind = "directory" if path.suffix == "" else "file"
            failures.append("Missing {0}: {1}".format(kind, rel(path, root)))

    readme = root / "tests/fixtures/negative/README.md"
    if readme.exists():
        text = readme.read_text(encoding="utf-8")
        if "Manual Verification Overview" not in text:
            failures.append(
                "Missing marker in tests/fixtures/negative/README.md: Manual Verification Overview"
            )
    return failures


def task_brief_cases(root: Path) -> List[Case]:
    tool = root / "scripts/validate-task-brief.py"
    base = root / "tests/fixtures/negative/task-brief"
    return [
        Case("missing-metadata", [str(tool), str(base / "missing-metadata/TASK.md")]),
        Case("executable-true", [str(tool), str(base / "executable-true/TASK.md")]),
        Case(
            "missing-acceptance-criteria",
            [str(tool), str(base / "missing-acceptance-criteria/TASK.md")],
        ),
        Case("status-not-approved", [str(tool), str(base / "status-not-approved/TASK.md")]),
    ]


def contract_generation_cases(root: Path) -> List[Case]:
    tool = root / "scripts/generate-task-contract.py"
    base = root / "tests/fixtures/negative/contract-generation"
    return [
        Case("missing-review", [str(tool), str(base / "missing-review/task-example/TASK.md")]),
        Case(
            "review-not-ready",
            [str(tool), str(base / "review-not-ready/task-example/TASK.md")],
        ),
        Case(
            "execution-not-allowed",
            [str(tool), str(base / "execution-not-allowed/task-example/TASK.md")],
        ),
        Case(
            "draft-already-exists",
            [str(tool), str(base / "draft-already-exists/task-example/TASK.md")],
        ),
    ]


def template_integrity_cases(root: Path) -> List[Case]:
    tool = root / "scripts/check-template-integrity.py"
    base = root / "tests/fixtures/template-integrity"
    return [
        Case("missing-core-file", [str(tool), "--root", str(base / "missing-core-file")]),
        Case(
            "forbidden-auto-runner",
            [str(tool), "--root", str(base / "forbidden-auto-runner")],
        ),
        Case(
            "missing-gitignore-drafts",
            [str(tool), "--root", str(base / "missing-gitignore-drafts")],
        ),
    ]


def excerpt(text: str) -> Optional[str]:
    stripped = text.strip()
    if not stripped:
        return None
    lines = stripped.splitlines()
    return " | ".join(lines[:3])


def run_case(root: Path, case: Case) -> CaseResult:
    completed = subprocess.run(
        [sys.executable] + list(case.command),
        cwd=str(root),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
    )
    if completed.returncode != 0:
        return CaseResult(case.name, True, [])

    details = ["Expected non-zero exit code, got 0"]
    stdout_excerpt = excerpt(completed.stdout)
    stderr_excerpt = excerpt(completed.stderr)
    if stdout_excerpt:
        details.append("stdout: {0}".format(stdout_excerpt))
    if stderr_excerpt:
        details.append("stderr: {0}".format(stderr_excerpt))
    return CaseResult(case.name, False, details)


def draft_file_set(root: Path) -> Optional[Set[str]]:
    drafts = root / "tasks/drafts"
    if not drafts.exists():
        return None
    return {
        str(path.relative_to(drafts))
        for path in drafts.rglob("*")
        if path.is_file()
    }


def print_group(name: str, results: Sequence[CaseResult]) -> bool:
    print("{0}:".format(name))
    passed = True
    for result in results:
        if result.passed:
            print("  {0}: PASS".format(result.name))
        else:
            passed = False
            print("  {0}: FAIL - {1}".format(result.name, result.details[0]))
            for detail in result.details[1:]:
                print("- {0}".format(detail))
    return passed


def main() -> int:
    root = repo_root()
    print("Negative Fixture Test Report")

    prerequisite_failures = check_prerequisites(root)
    if prerequisite_failures:
        print("Prerequisites: FAIL")
        for failure in prerequisite_failures:
            print("- {0}".format(failure))
        print("Result: FAIL")
        return 1

    before_drafts = draft_file_set(root)

    task_results = [run_case(root, case) for case in task_brief_cases(root)]
    contract_results = [run_case(root, case) for case in contract_generation_cases(root)]
    template_results = [run_case(root, case) for case in template_integrity_cases(root)]

    after_drafts = draft_file_set(root)

    ok = True
    if not print_group("Task Brief", task_results):
        ok = False
    if not print_group("Contract Generation", contract_results):
        ok = False
    if before_drafts != after_drafts:
        ok = False
        print("Contract Generation: root tasks/drafts protection: FAIL - root-level tasks/drafts/ changed during negative fixture tests")
    if not print_group("Template Integrity", template_results):
        ok = False

    print("Skipped:")
    for name, reason in SKIPPED_GROUPS:
        print("{0}: SKIPPED — {1}".format(name, reason))

    if ok:
        print("Result: PASS")
        return 0

    print("Result: FAIL")
    return 1


if __name__ == "__main__":
    sys.exit(main())
