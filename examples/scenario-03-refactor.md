# Scenario 03 — Refactor

## Situation

A user wants to simplify a script, but the change could easily expand into a broad architecture rewrite.

## User Input

Refactor the template integrity checker to make sections easier to maintain without changing behavior.

## AgentOS Flow

1. `/spec` should classify scope carefully.
2. The Task Brief must define behavior-preserving constraints.
3. `Out of Scope` must explicitly exclude new validation behavior.
4. `REVIEW.md` should reject broad rewrites.
5. `TRACE.md` should record why behavior must remain stable.
6. A draft contract can be generated only if review allows execution.

## Expected Artifacts

- `tasks/{task-id}/TASK.md`
- `tasks/{task-id}/REVIEW.md`
- `tasks/{task-id}/TRACE.md`
- `tasks/drafts/{task-id}-contract-draft.md`

## Human Approval Points

- approval of the limited scope
- approval before active-task replacement
- approval before accepting the behavior-preserving refactor as complete

## Validation Commands

- `python3 scripts/check-template-integrity.py --strict`
- `python3 scripts/test-template-integrity.py`
- `python3 scripts/test-guard-failures.py`
- `python3 scripts/audit-agentos.py`

## What Must Not Happen Automatically

- adding new checker behavior during the refactor unless explicitly scoped
- rewriting unrelated scripts
- changing fixtures to make tests pass
- bypassing the review gate

## Notes

This scenario is about restraint: simplify the structure, not the meaning.
