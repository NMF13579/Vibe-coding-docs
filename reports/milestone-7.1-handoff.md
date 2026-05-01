# Milestone 7.1 - Negative Test Fixtures: Handoff

## Status

COMPLETE - smoke test PASS

## What Was Done

- Task 7.1.1 - Negative Fixtures Inventory: created the negative fixture category and case README inventory.
- Task 7.1.2 - Negative Fixture Minimal Content: added minimal invalid payload files for negative cases.
- Task 7.1.3 - Negative Fixture Manual Verification Notes: documented manual commands, expected FAIL outcomes, and reasons for each case.
- Task 7.1.4 - Negative Fixture Test Runner MVP: added `scripts/test-negative-fixtures.py` for runnable negative fixture checks.
- Task 7.1.5 - Negative Fixture Test Runner Documentation: documented runner usage, result meaning, skipped groups, and safety boundaries.
- Task 7.1.6 - Negative Fixture Runner Smoke Test: recorded `Result: PASS` and exit code `0` in `reports/negative-fixtures-smoke.md`.

Recent commits used for handoff context:

- `32306aa` test(7.1.6): add negative fixture runner smoke report
- `5fb5f70` docs(7.1.5): document negative fixture test runner
- `a115af2` test(7.1.4): add negative fixture test runner MVP
- `85b75f6` test(7.1): add negative fixture inventory and manual notes
- `4a3c4c4` feat(7.0.3): add Template Integrity Checker self-test command
- `5530ff9` feat(7.0.2): add PASS_WITH_WARNINGS, --strict, warning-level checks
- `d796ea7` feat(7.0.1): add Template Integrity Checker MVP
- `2068a9e` docs(project): fill specs section details
- `c8117c1` feat(example-project): add example validation flow
- `1e053f3` Stabilize canonical module architecture and validators

## Automated Coverage

- task-brief: 4 cases
- contract-generation: 4 cases
- template-integrity: 3 cases

## Skipped Coverage

- review: future validator
- trace: future validator
- queue: future validator
- runner: future guard test

## Key Constraints

- Do not run runner scripts directly: `scripts/agent-next.py`, `scripts/agent-complete.py`, or `scripts/agent-fail.py`.
- Do not modify `tasks/active-task.md` or move queue items as part of negative fixture work.
- The negative fixture runner protects root-level `tasks/drafts/` by comparing the set of relative file paths before and after runnable checks.
- The smoke prerequisite for this handoff checks only the value under `## Actual Result` in `reports/negative-fixtures-smoke.md`; it does not search for `PASS` across the whole file.
- AgentOS remains a Markdown-first guardrail framework, not an autonomous runner, backend, RAG system, or orchestration platform.
- Review, trace, queue, and runner negative fixtures are documented but not automated until future validators or guard tests exist.

## Test Runner Interface

- `scripts/validate-task-brief.py`: invoked as `python3 scripts/validate-task-brief.py <TASK.md>`. It reads one Task Brief file, checks required metadata and sections, returns non-zero when the fixture is rejected, and returns `0` with `PASS` only when the file is accepted.
- `scripts/generate-task-contract.py`: invoked as `python3 scripts/generate-task-contract.py <TASK.md> [--output tasks/drafts/<draft>.md]`. It accepts a `TASK.md` path, requires sibling `REVIEW.md`, checks review status and `execution_allowed`, and returns non-zero when contract generation is blocked or invalid.
- `scripts/check-template-integrity.py`: invoked as `python3 scripts/check-template-integrity.py --root <fixture-root>`. It checks required template files, directories, `.gitignore`, forbidden paths, optional warning checks, and returns non-zero for `FAIL` or strict warning failures.
- `scripts/test-negative-fixtures.py`: invokes the three tools above with `sys.executable` and `cwd=repo_root`. For negative fixtures, a non-zero child exit code means the invalid fixture was correctly rejected and the case is reported as `PASS`.

## Next Steps

Milestone 7.2 - Guard Failure Test Runner:

- Task 7.2.1: Guard Failure Runner MVP (`scripts/test-guard-failures.py`)
- Orchestration layer over `scripts/test-template-integrity.py` and `scripts/test-negative-fixtures.py`

## Blocked / Follow-Up

- Review negative fixtures are blocked from automation until a review validator or guard test runner exists.
- Trace negative fixtures are blocked from automation until a trace validator or guard test runner exists.
- Queue negative fixtures are blocked from automation until a queue validator or guard test runner exists.
- Runner negative fixtures are blocked from automation until a runner guard test exists.
- Future milestones should decide whether skipped groups become direct validators, guard tests, or part of a broader Guard Failure Test Runner.
- Future work should keep template-integrity negative fixtures referenced from `tests/fixtures/template-integrity/` instead of duplicating them under `tests/fixtures/negative/`.

## Safety Notes

- No scripts were executed during this handoff task.
- `tasks/active-task.md` was not modified.
- Queue items were not moved.
- Existing files were not modified.
