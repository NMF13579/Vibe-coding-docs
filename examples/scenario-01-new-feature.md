# Scenario 01 — New Feature

## Situation

A user wants to add a small feature to an existing project, but needs to avoid jumping directly into implementation.

## User Input

I want to add a command that shows task health across briefs, reviews, traces, queue entries, and drafts.

## AgentOS Flow

1. Use `/init` if project context is missing.
2. Use `/spec` to turn the idea into a Task Brief.
3. Validate the brief with `scripts/validate-task-brief.py`.
4. Add `REVIEW.md` to decide whether execution is allowed.
5. Add `TRACE.md` to preserve decision rationale.
6. Use `scripts/generate-task-contract.py` to create a draft contract.
7. Wait for human approval before replacing `tasks/active-task.md`.

## Expected Artifacts

- `project/PROJECT.md`
- `tasks/{task-id}/TASK.md`
- `tasks/{task-id}/REVIEW.md`
- `tasks/{task-id}/TRACE.md`
- `tasks/drafts/{task-id}-contract-draft.md`

## Human Approval Points

- before converting draft contract into `tasks/active-task.md`
- before starting execution
- before marking completion

## Validation Commands

- `python3 scripts/validate-task-brief.py tasks/{task-id}/TASK.md`
- `python3 scripts/generate-task-contract.py tasks/{task-id}`
- `python3 scripts/audit-agentos.py`

Use the actual generator CLI documented in this repository.

## What Must Not Happen Automatically

- Task Brief must not be executed directly.
- Draft contract must not replace `tasks/active-task.md` without human approval.
- Queue items must not move automatically.
- Runner protocol scripts must not execute without explicit user action.

## Notes

This scenario is documentation only. It shows the intended path from idea to reviewed draft without automatic execution.
