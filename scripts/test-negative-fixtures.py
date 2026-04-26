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
    ("queue", "future validator"),
    ("runner", "future guard test"),
]

REQUIRED_REVIEW_FIXTURES = [
    "missing-review-status.md",
    "missing-execution-allowed.md",
    "ready-but-execution-false.md",
    "blocked-but-execution-true.md",
    "unknown-review-status.md",
]

REQUIRED_TRACE_FIXTURES = [
    "missing-task-id.md",
    "missing-source-summary.md",
    "missing-decision-rationale.md",
    "empty-task-id.md",
    "execution-approved.md",
    "replaces-task.md",
    "replaces-review.md",
    "active-task-updated.md",
    "malformed-frontmatter.md",
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
        root / "scripts/validate-review.py",
        root / "scripts/validate-trace.py",
        root / "tests/fixtures/negative/trace",
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


def review_cases(root: Path) -> List[Case]:
    tool = root / "scripts/validate-review.py"
    base = root / "tests/fixtures/negative/review"
    return [
        Case("missing-review-status", [str(tool), str(base / "missing-review-status.md")]),
        Case(
            "missing-execution-allowed",
            [str(tool), str(base / "missing-execution-allowed.md")],
        ),
        Case(
            "ready-but-execution-false",
            [str(tool), str(base / "ready-but-execution-false.md")],
        ),
        Case(
            "blocked-but-execution-true",
            [str(tool), str(base / "blocked-but-execution-true.md")],
        ),
        Case(
            "unknown-review-status",
            [str(tool), str(base / "unknown-review-status.md")],
        ),
    ]


def trace_cases(root: Path) -> List[Case]:
    tool = root / "scripts/validate-trace.py"
    base = root / "tests/fixtures/negative/trace"
    return [
        Case("missing-task-id", [str(tool), str(base / "missing-task-id.md")]),
        Case("missing-source-summary", [str(tool), str(base / "missing-source-summary.md")]),
        Case(
            "missing-decision-rationale",
            [str(tool), str(base / "missing-decision-rationale.md")],
        ),
        Case("empty-task-id", [str(tool), str(base / "empty-task-id.md")]),
        Case("execution-approved", [str(tool), str(base / "execution-approved.md")]),
        Case("replaces-task", [str(tool), str(base / "replaces-task.md")]),
        Case("replaces-review", [str(tool), str(base / "replaces-review.md")]),
        Case("active-task-updated", [str(tool), str(base / "active-task-updated.md")]),
        Case(
            "malformed-frontmatter",
            [str(tool), str(base / "malformed-frontmatter.md")],
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
    review_base = root / "tests/fixtures/negative/review"
    review_has_any = review_base.exists() and any(review_base.glob("*.md"))
    missing_review_fixtures = [
        name for name in REQUIRED_REVIEW_FIXTURES if not (review_base / name).is_file()
    ]
    review_results = [run_case(root, case) for case in review_cases(root)] if review_has_any else []
    trace_base = root / "tests/fixtures/negative/trace"
    trace_md_files = sorted(path.name for path in trace_base.glob("*.md")) if trace_base.exists() else []
    trace_has_any = len(trace_md_files) > 0
    missing_trace_fixtures = [
        name for name in REQUIRED_TRACE_FIXTURES if not (trace_base / name).is_file()
    ]
    extra_trace_fixtures = sorted(set(trace_md_files) - set(REQUIRED_TRACE_FIXTURES))
    trace_results = [run_case(root, case) for case in trace_cases(root)] if trace_has_any else []

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
    if not review_has_any:
        ok = False
        print("review: FAIL — review fixtures not found")
    else:
        if not print_group("review", review_results):
            ok = False
        if missing_review_fixtures:
            ok = False
            for fixture_name in missing_review_fixtures:
                print(
                    "  {0}: FAIL - fixture not found: {1}".format(
                        Path(fixture_name).stem,
                        rel(review_base / fixture_name, root),
                    )
                )
    if not trace_has_any:
        ok = False
        print("trace: FAIL — trace fixtures not found")
    else:
        if not print_group("trace", trace_results):
            ok = False
        if missing_trace_fixtures:
            ok = False
            for fixture_name in missing_trace_fixtures:
                print(
                    "  {0}: FAIL - fixture not found: {1}".format(
                        Path(fixture_name).stem,
                        rel(trace_base / fixture_name, root),
                    )
                )
        if extra_trace_fixtures:
            ok = False
            for fixture_name in extra_trace_fixtures:
                print(
                    "  {0}: FAIL - unexpected fixture: {1}".format(
                        Path(fixture_name).stem,
                        rel(trace_base / fixture_name, root),
                    )
                )

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
