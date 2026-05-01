#!/usr/bin/env python3

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
VERSION = "1.0.0"

PASS = "PASS"
WARN = "WARN"
FAIL = "FAIL"


@dataclass
class GroupResult:
    name: str
    status: str
    details: list[str]


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def path_exists(path: Path) -> bool:
    return path.exists()


def check_files_exist(name: str, paths: list[str]) -> GroupResult:
    missing = [p for p in paths if not path_exists(REPO_ROOT / p)]
    if missing:
        return GroupResult(name, FAIL, [f"missing: {m}" for m in missing])
    return GroupResult(name, PASS, [])


def check_file_contains(
    name: str,
    path: str,
    required_strings: list[str],
    missing_is_fail: bool = True,
) -> GroupResult:
    text = read_text(REPO_ROOT / path)
    if text is None:
        return GroupResult(name, FAIL if missing_is_fail else WARN, [f"missing: {path}"])

    missing = [s for s in required_strings if s not in text]
    if not missing:
        return GroupResult(name, PASS, [])

    status = FAIL if missing_is_fail else WARN
    return GroupResult(name, status, [f"missing substring: {m}" for m in missing])


def check_any_doc_contains(docs: list[str], needle: str) -> bool:
    for rel in docs:
        text = read_text(REPO_ROOT / rel)
        if text is not None and needle in text:
            return True
    return False


def check_applied_record_non_equivalence(docs: list[str]) -> bool:
    direct = "applied transition record ≠ lifecycle mutation"
    fallback_any = [
        "does not automatically imply lifecycle mutation",
        "does not imply lifecycle mutation",
        "not lifecycle mutation",
        "is not lifecycle mutation",
    ]

    for rel in docs:
        text = read_text(REPO_ROOT / rel)
        if text is None:
            continue
        if direct in text:
            return True
        if "applied transition record" in text and any(x in text for x in fallback_any):
            return True
    return False


def check_docs_for_concepts(name: str, docs: list[str]) -> GroupResult:
    missing_concepts: list[str] = []

    concept_checks = [
        ("No autonomous lifecycle authority", "autonomous lifecycle authority"),
        ("Explicit controlled apply path", "controlled apply"),
        ("Human approval boundary", "human approval"),
        ("Failure does not authorize mutation", "failure does not authorize lifecycle mutation"),
        ("Complete-active only", "complete-active"),
    ]

    for concept_name, needle in concept_checks:
        if not check_any_doc_contains(docs, needle):
            missing_concepts.append(f"missing concept: {concept_name}")

    if not check_applied_record_non_equivalence(docs):
        missing_concepts.append(
            "applied transition record non-equivalence not found in either integration document"
        )

    if not missing_concepts:
        return GroupResult(name, PASS, [])

    if len(missing_concepts) <= 2:
        return GroupResult(name, WARN, missing_concepts)

    return GroupResult(name, FAIL, missing_concepts)


def compute_overall(results: list[GroupResult]) -> str:
    if any(r.status == FAIL for r in results):
        return FAIL
    if any(r.status == WARN for r in results):
        return WARN
    return PASS


def print_group(result: GroupResult) -> None:
    print(f"[{result.status}] {result.name}")
    for d in result.details:
        print(f"  {d}")


def main() -> int:
    results: list[GroupResult] = []

    results.append(
        check_files_exist(
            "Lifecycle source coverage",
            [
                "docs/CONTROLLED-LIFECYCLE-MUTATION.md",
                "docs/APPLY-PRECONDITIONS.md",
                "docs/APPLIED-TRANSITION-RECORD.md",
                "docs/APPLY-PLAN.md",
                "docs/COMPLETION-TRANSITION.md",
            ],
        )
    )

    results.append(
        check_files_exist(
            "Lifecycle integration coverage",
            [
                "docs/LIFECYCLE-INTEGRATION.md",
                "docs/APPLY-COMMAND-INTEGRATION.md",
            ],
        )
    )

    validation_required = [
        "Lifecycle Apply Validation",
        "checks: 8",
        "Result: PASS",
        "Result: FAIL",
        "autonomous_lifecycle_authority: false",
        "complete-active",
    ]
    results.append(
        check_file_contains(
            "Lifecycle validation coverage",
            "scripts/validate-lifecycle-apply.py",
            validation_required,
            missing_is_fail=False,
        )
    )

    mode_required = [
        "--dry-run",
        "--prepare",
        "--plan-out",
        "--apply",
        "--applied-record-out",
        "--complete-active-plan",
        "--complete-active",
    ]
    results.append(
        check_file_contains(
            "Lifecycle command surface coverage",
            "scripts/apply-transition.py",
            mode_required,
            missing_is_fail=True,
        )
    )

    results.append(
        check_file_contains(
            "Preconditions coverage",
            "scripts/check-apply-preconditions.py",
            ["PASS", "BLOCKED"],
            missing_is_fail=True,
        )
    )

    fixture_script = path_exists(REPO_ROOT / "scripts/test-apply-transition-fixtures.py")
    fixture_dir = path_exists(REPO_ROOT / "tests/fixtures/apply-transition")
    if fixture_script and fixture_dir:
        results.append(GroupResult("Fixture coverage", PASS, []))
    else:
        details: list[str] = []
        if not fixture_script:
            details.append("missing: scripts/test-apply-transition-fixtures.py")
        if not fixture_dir:
            details.append("missing: tests/fixtures/apply-transition/")
        results.append(GroupResult("Fixture coverage", FAIL, details))

    safety_docs = [
        "docs/LIFECYCLE-INTEGRATION.md",
        "docs/APPLY-COMMAND-INTEGRATION.md",
        "docs/CONTROLLED-LIFECYCLE-MUTATION.md",
        "docs/APPLIED-TRANSITION-RECORD.md",
    ]
    results.append(check_docs_for_concepts("Safety boundary coverage", safety_docs))

    unsupported_docs = [
        "docs/LIFECYCLE-INTEGRATION.md",
        "docs/APPLY-COMMAND-INTEGRATION.md",
    ]
    unsupported_needles = [
        "needs_review",
        "failed",
        "blocked",
        "manual_abort",
        "unsupported_mutation_paths",
    ]

    both_missing = all(read_text(REPO_ROOT / d) is None for d in unsupported_docs)
    if both_missing:
        results.append(
            GroupResult(
                "Unsupported mutation boundary",
                FAIL,
                [
                    "missing: docs/LIFECYCLE-INTEGRATION.md",
                    "missing: docs/APPLY-COMMAND-INTEGRATION.md",
                ],
            )
        )
    else:
        missing_unsup = [n for n in unsupported_needles if not check_any_doc_contains(unsupported_docs, n)]
        if missing_unsup:
            results.append(
                GroupResult(
                    "Unsupported mutation boundary",
                    WARN,
                    [f"missing substring: {m}" for m in missing_unsup],
                )
            )
        else:
            results.append(GroupResult("Unsupported mutation boundary", PASS, []))

    evidence_needles = [
        "verification evidence",
        "completion readiness evidence",
        "prepared transition record",
        "apply preconditions result",
        "apply plan",
        "applied transition record",
        "mutation plan",
        "controlled mutation execution evidence",
    ]
    evidence_result = check_file_contains(
        "Evidence chain coverage",
        "docs/LIFECYCLE-INTEGRATION.md",
        evidence_needles,
        missing_is_fail=False,
    )
    results.append(evidence_result)

    print("Lifecycle Mutation Audit")
    print(f"version: {VERSION}")
    print("groups: 9")
    print()

    # print first 9 required groups (the 10th is computed overall)
    for group in results:
        print_group(group)

    overall = compute_overall(results)
    print()
    print(f"Result: {overall}")

    return 1 if overall == FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
