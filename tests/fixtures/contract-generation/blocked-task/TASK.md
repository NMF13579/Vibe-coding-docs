# Task Brief: Blocked Fixture

## Metadata

task_id: blocked-task
status: APPROVED
created_at: 2026-04-26
source: fixture
executable: false

## Context

This fixture verifies that blocked review status stops automation.

## User Story

As a maintainer, I want blocked review status to prevent draft generation.

## Expected Result

No draft contract is created.

## Acceptance Criteria

- The generator stops with failure.

## Out of Scope

- Creating any draft file.

## Dependencies

- `templates/task-contract-from-brief.md`

## Risks

- None.

## Rollback / Reversal Notes

- No rollback needed.

## Notes

- Fixture only.
