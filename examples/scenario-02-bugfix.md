# Scenario 02 — Bugfix

## Situation

A bug causes a validator to accept malformed input. The fix must be small and verifiable.

## User Input

The task brief validator currently accepts a `TASK.md` without Acceptance Criteria. Fix that.

## AgentOS Flow

1. `/spec` creates a narrow bugfix Task Brief.
2. Acceptance Criteria define failing and passing examples.
3. `REVIEW.md` checks whether the bugfix is scoped and safe.
4. `TRACE.md` records why this is a bug and what behavior is expected.
5. The draft contract is generated only after the review gate.
6. Human approval is required before active task replacement.

## Expected Artifacts

- `tasks/{task-id}/TASK.md`
- `tasks/{task-id}/REVIEW.md`
- `tasks/{task-id}/TRACE.md`
- `tasks/drafts/{task-id}-contract-draft.md`
- `tests/fixtures/...` if needed by the actual implementation task

## Human Approval Points

- approval before the execution contract becomes active
- approval before accepting the fix as complete

## Validation Commands

- `python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md`
- `python3 scripts/test-negative-fixtures.py`
- `python3 scripts/test-guard-failures.py`
- `python3 scripts/audit-agentos.py`

## What Must Not Happen Automatically

- broad validator rewrite without scoped task approval
- changing unrelated schema behavior
- marking a queue item done without human confirmation
- modifying `tasks/active-task.md` without approval

## Notes

The point of this scenario is controlled repair: fix the bug that is named, and keep everything else unchanged.
