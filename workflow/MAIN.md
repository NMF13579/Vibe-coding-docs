---
type: canonical
module: workflow
status: canonical
authority: canonical
when_to_read: always
owner: unassigned
---

# Workflow

## Purpose

Canonical execution backbone for agent work.
This module owns plan gate, scope control, execution boundaries, and the one-task rule.

## Plan Gate

- Receive the task and restate the expected result before changing files.
- Build a plan when the work affects files, behavior, structure, or release readiness.
- Show the plan to the owner when approval is required by task risk or scope.
- Do not execute file or code changes until the required approval is present.
- If the task is unclear, ask for clarification instead of guessing.

## Execution Boundaries

- Work only inside the confirmed task.
- Use the smallest change that satisfies the accepted scope.
- Do not silently add cleanup, refactors, new features, or policy changes.
- If the task becomes uncertain or expands, stop and classify the change before continuing.
- Keep workflow execution-oriented; do not turn it into state, quality, security, or governance authority.

## Scope Control

- Classify new requests as in scope, scope expansion, or out of scope before making changes.
- Continue only when the request is in scope.
- For scope expansion, ask the owner whether to continue, defer, or create a separate task.
- For out-of-scope work, stop and keep it separate from the active task.
- If the owner approves an expansion, record the updated scope before execution.

## One-Task Rule

- Work on one active task at a time.
- Do not mix unrelated fixes into the current task.
- Do not split attention across multiple live tasks.
- If a second task appears, pause and ask which task has priority.

## Failure Route

- If a required step was skipped, return to that step and complete it.
- If the approach is wrong, retry with a smaller corrected approach.
- If context is unclear, return to `state/MAIN.md` and recover state before continuing.
- If verification is unclear, continue to `quality/MAIN.md`.
- If the task touches sensitive data, access, secrets, auth, API, or database boundaries, continue to `security/MAIN.md`.
- If repeated failure or unsafe work appears, stop and ask the owner whether to recover, roll back, or re-plan.

## Runtime Usage

1. Confirm state through `state/MAIN.md`.
2. Confirm authority through `core-rules/MAIN.md`.
3. Define the task boundary.
4. Present or confirm the plan.
5. Execute only inside the approved boundary.
6. Verify through `quality/MAIN.md`.
7. Report the result and any remaining risk.
