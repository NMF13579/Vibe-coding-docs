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
- If a task affects files, behavior, structure, release readiness, sensitive data, or architecture, the agent must form a task contract before execution.
- Show the plan to the owner when approval is required by task risk or scope.
- Do not execute file or code changes until the required approval is present.
- If the task is unclear, ask for clarification instead of guessing.

## Task Contract

Use this minimum contract before execution when the task crosses the plan gate:

```yaml
task:
  goal:
  expected_result:
  in_scope:
  out_of_scope:
  files_or_areas:
  risk_level:
  requires_owner_approval:
  acceptance_criteria:
  verification_plan:
```

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

## Lesson Capture

After every completed fix, check `lessons/lessons.md` for an existing lesson
covering the root cause of the failure.

- If no lesson exists: create one using `lessons/templates/lesson-entry.md`
- Fields `trigger` and `rule` must be specific - not generic descriptions
- Set `status: active` (not `proposed`)
- Commit separately: `docs(lessons): add lesson-NNN <incident-id>`
- A fix commit is not complete until the lesson is recorded

Lesson is required when:
- a test was failing due to unimplemented code marked by audit comments
- a commit was rejected by a hook due to unknown format
- a blocking error required more than one retry to resolve

## Runtime Usage

1. Confirm state through `state/MAIN.md`.
2. Confirm authority through `core-rules/MAIN.md`.
3. Define the task boundary.
4. Present or confirm the plan.
5. Execute only inside the approved boundary.
6. Verify through `quality/MAIN.md`.
7. Report the result and any remaining risk.
8. After every fix - check `lessons/lessons.md`: if no lesson exists
   for this incident, create one from `lessons/templates/lesson-entry.md`
   and commit separately with type `docs(lessons):` and `status: active`.
