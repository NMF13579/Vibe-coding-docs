# Task Brief: Brief Readiness Check

## Metadata

task_id: task-20260426-brief-readiness-check
status: APPROVED
state: approved_for_execution
created_at: 2026-04-26
source: full-manual-flow-smoke-test
executable: false

This file is an approved Task Brief.
It is not an executable Task Contract.
To execute this task, create tasks/active-task.md from tasks/templates/task-contract.md.

## Context

AgentOS already separates planning artifacts from execution artifacts. A smoke-test task is needed to verify that the full manual Input Layer flow can move from Task Brief to Review and Trace without touching the execution layer.

## User Story

As a repository owner, I want a small approved Task Brief that is safe to review and trace manually so that the full Input Layer flow can be tested end to end.

## Expected Result

A reviewer can validate the brief structure, create a review, create a trace, and prepare a manual execution contract draft without changing `tasks/active-task.md`.

## Acceptance Criteria

- The Task Brief passes `scripts/validate-task-brief.py`.
- A `REVIEW.md` can be created next to the brief.
- A `TRACE.md` can be created next to the brief.
- A manual contract draft can be prepared without writing to `tasks/active-task.md`.

## Out of Scope

- Running execution validators
- Replacing `tasks/active-task.md`
- Automating Brief → Contract conversion
- Creating queue or agent state automation

## Dependencies

- `templates/task-brief-review.md`
- `templates/task-decision-trace.md`
- `tools/task-contract-builder/BUILD-TASK-CONTRACT.md`
- `templates/task-contract-from-brief.md`

## Risks

- The bridge may still need human clarification for risk and verification fields.
- Review status may allow conversion while some details still require manual care.

## Rollback / Reversal Notes

- Delete smoke-test artifacts in this task directory if they are no longer needed.
- Re-check that execution files remain untouched after removal.

## Notes

- This Task Brief exists only for the full manual flow smoke-test.
