# Task Brief: Ready Fixture

## Metadata

task_id: ready-task
status: APPROVED
created_at: 2026-04-26
source: fixture
executable: false

## Context

This fixture exists to verify draft contract generation when review allows execution.

## User Story

As a maintainer, I want a generator-ready task brief so that a contract draft can be created safely.

## Expected Result

A draft contract file is created in `tasks/drafts/`.

## Acceptance Criteria

- A draft file is created.
- The generator does not touch `tasks/active-task.md`.

## Out of Scope

- Running execution pipeline.

## Dependencies

- `templates/task-contract-from-brief.md`
- `tools/task-contract-builder/BUILD-TASK-CONTRACT.md`

## Risks

- Human review is still required before using any generated draft.

## Rollback / Reversal Notes

- Delete the generated draft if it is no longer needed.

## Notes

- Fixture only.
