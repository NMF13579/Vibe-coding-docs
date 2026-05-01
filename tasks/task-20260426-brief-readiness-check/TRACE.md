# Decision Trace: Brief Readiness Check

## Metadata

task_id: task-20260426-brief-readiness-check
trace_created_at: 2026-04-26
trace_author: smoke-test
source_task: tasks/task-20260426-brief-readiness-check/TASK.md
source_review: tasks/task-20260426-brief-readiness-check/REVIEW.md
trace_status: COMPLETE

## Original User Idea

Create a safe smoke-test path for checking the full Input Layer manually without touching the execution contract.

## Interview Summary

The goal was to verify the entire manual flow from Task Brief to Review and Trace and then to a draft executable contract, while keeping execution files untouched.

## Clarifying Questions and Answers

### Q1

Question:
Should the smoke-test modify `tasks/active-task.md`?
Answer:
No, the contract must stay only as a dry-run draft in the report.
Impact on Task Brief:
The brief explicitly keeps execution out of scope.

### Q2

Question:
Can the smoke-test use an existing Task Brief?
Answer:
Only if its source matches the allowed smoke-test source values.
Impact on Task Brief:
Because no matching brief existed, a new smoke-test brief was created.

## Decisions Made

- Use a dedicated smoke-test Task Brief instead of reusing the earlier spec-wizard smoke-test task.
- Allow review status `READY_WITH_EDITS` so the bridge can be tested without claiming full execution readiness.
- Keep all output in the task directory and out of execution files.

## Rejected Options

- Reuse the earlier `task-20260426-brief-to-contract-manual-guide` brief.
- Write the draft contract directly into `tasks/active-task.md`.

## Assumptions

- The owner wants to test the full manual flow, not actual execution.
- Human confirmation will still be required before any future replacement of `tasks/active-task.md`.

## Open Questions

- Which exact files should become `in_scope` if this smoke-test ever becomes a real execution task?
- Should a future execution contract use only manual verification or command-based verification?

## Scope Notes

- This smoke-test covers only manual flow artifacts.
- It does not start execution or validation pipeline for runtime work.

## Risk Notes

- The biggest risk is confusing a dry-run contract draft with a ready executable contract.
- Human review remains necessary before execution.

## Links

- Task Brief: tasks/task-20260426-brief-readiness-check/TASK.md
- Review: tasks/task-20260426-brief-readiness-check/REVIEW.md
- Related Project Section: project/PROJECT.md

## Trace Summary

The smoke-test task was intentionally created as a small, reviewable brief so the full Input Layer flow could be verified without touching execution state.
