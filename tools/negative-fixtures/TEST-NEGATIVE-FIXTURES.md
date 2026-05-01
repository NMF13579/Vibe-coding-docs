# Negative Fixture Test Runner

## Purpose

Negative fixtures are intentionally invalid examples used to prove that AgentOS guardrails reject bad inputs.

The core interpretation is:

- invalid fixture rejected -> PASS
- invalid fixture accepted -> FAIL

A PASS in this runner does not mean the fixture is valid. It means the invalid fixture was correctly rejected.

## Command

Run:

```bash
python3 scripts/test-negative-fixtures.py
```

The command can be run from the repository root. The script resolves the repository root relative to its own file.

## Automated coverage

The MVP runner automatically checks only categories that already have tools:

| Category | Cases | Tool |
|---|---:|---|
| task-brief | 4 | scripts/validate-task-brief.py |
| contract-generation | 4 | scripts/generate-task-contract.py |
| template-integrity | 3 | scripts/check-template-integrity.py |
| review | 5 | scripts/validate-review.py |
| trace | 9 | scripts/validate-trace.py |
| queue | 10 | scripts/validate-queue-entry.py |
| contract-draft | 14 | scripts/validate-contract-draft.py |

Template-integrity negative fixtures are located in:

```text
tests/fixtures/template-integrity/
```

They are not duplicated inside:

```text
tests/fixtures/negative/
```

For each template-integrity fixture path, the runner invokes `scripts/check-template-integrity.py` with `--root`.

## Skipped coverage

These categories are documented but not automated yet:

| Category | Status | Reason |
|---|---|---|
| runner | SKIPPED | future runner guard test |

Skipped groups do not affect exit code. They are documented negative fixtures waiting for future validators or guard tests.

## Result interpretation

PASS means the invalid fixture was rejected.

FAIL means the invalid fixture was unexpectedly accepted, or a runnable prerequisite was missing.

SKIPPED means the category is documented but not automated yet.

Example:

```text
Task Brief:
  executable-true: PASS
```

This means `scripts/validate-task-brief.py` rejected a Task Brief with `executable: true`.

For review fixtures, `scripts/validate-review.py` is used:

- invalid `REVIEW.md` rejected -> PASS
- invalid `REVIEW.md` accepted -> FAIL

For trace fixtures, `scripts/validate-trace.py` is used:

- invalid `TRACE.md` rejected -> PASS
- invalid `TRACE.md` accepted -> FAIL

For queue fixtures, `scripts/validate-queue-entry.py` is used:

- invalid queue entry rejected -> PASS
- invalid queue entry accepted -> FAIL

For contract draft fixtures, `scripts/validate-contract-draft.py` is used:

- invalid contract draft rejected -> PASS
- invalid contract draft accepted -> FAIL

## Exit codes

| Code | Meaning |
|---:|---|
| 0 | all runnable negative tests passed |
| 1 | at least one runnable negative test failed or prerequisite was missing |

Skipped categories do not cause exit code 1.

## Root-level tasks/drafts/ protection

The runner records the root-level `tasks/drafts/` file path set before running child processes.

After all runnable checks finish, it records the same file path set again and compares the two sets.

If `tasks/drafts/` does not exist before the run, the recorded state is `None`. If the directory appears after the run, the comparison fails.

Only relative file paths are compared. The runner does not compare modification time, file size, or file hashes.

If the before and after states differ, the runner prints a failure for root-level `tasks/drafts/` protection and returns `FAIL`.

Reason: contract generation negative tests must not leak runtime artifacts into root-level `tasks/drafts/`.

## Non-goals

`scripts/test-negative-fixtures.py` does not:

- execute tasks
- run runner scripts
- run agent-next.py
- run agent-complete.py
- run agent-fail.py
- modify tasks/active-task.md
- move queue items
- create review validators
- create trace validators
- create queue validators
- create runner guard validators
- act as audit runner
- act as release checklist
- approve execution
- perform autonomous runner behavior

## Relationship to future milestones

Task 7.1.4 provides a narrow MVP runner for runnable negative fixtures.

Future milestones may add validators for runner category.

Milestone 7.2 may introduce a broader Guard Failure Test Runner.

This tool is not the full AgentOS audit runner.
