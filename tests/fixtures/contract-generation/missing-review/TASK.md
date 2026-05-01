# Task Brief: Missing Review Fixture

## Metadata

task_id: missing-review
status: APPROVED
created_at: 2026-04-26
source: fixture
executable: false

## Context

This fixture verifies that missing review file stops draft generation.

## User Story

As a maintainer, I want missing review file to prevent draft generation.

## Expected Result

The generator fails because `REVIEW.md` is absent.

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
