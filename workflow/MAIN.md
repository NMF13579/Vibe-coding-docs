---
type: canonical
module: workflow
status: transitional
authority: canonical
when_to_read: always
owner: unassigned
---

# Workflow

## Purpose
Operational execution backbone for tasks in the new core route.
This module surfaces the operational workflow backbone while deeper detail still lives in approved legacy sources during migration.

## Core workflow
- Receive the task and align the scope before changing anything.
- Build a plan and show it to the owner for confirmation.
- Do not execute until explicit approval is given.
- Run the smallest relevant self-checks/tests for the task.
- Report the result and update the required context artifacts.
- If the task becomes uncertain or expands, stop and route through scope or error handling instead of improvising a wider change.
- Keep the workflow execution-oriented; do not turn it into policy, state, or verification authority.

## Interview to task flow
- When the work begins as an interview, ask one question at a time.
- Stay on the current step until the owner answers.
- If the question or answer blocks progress, stop-block and fix the wording before moving on.
- At completion, give a short summary and ask for confirmation.
- Normalize interview output into the task/spec flow only when the source path makes that explicit.
- If the exact output artifact or file convention is unclear, direct-read is required for detail.

## Scope and change control
- Work only inside the confirmed task.
- Classify new requests as in scope, scope expansion, or out of scope before making changes.
- Stop immediately on scope expansion or out-of-scope requests and ask the owner whether to continue, defer, or update the backlog.
- Do not silently add new work to the live task.
- If the owner approves an expansion, record it through the task flow and backlog path used by the project.

## Failure and escalation route
- If a required step was skipped, return to that step and do it now.
- If the approach is wrong, retry with a different approach up to two times.
- If context is unclear, restore context before continuing.
- If the work is blocked or repeatedly failing, route to incident handling instead of pushing ahead.
- For rollback or recovery detail, open `incidents/MAIN.md` and `LAYER-1/error-handling.md`.

## When to open additional docs
- Open `state/MAIN.md` when the task depends on formal state or blockers.
- Open `quality/MAIN.md` when the task needs verification, readiness, or release checks.
- Open `incidents/MAIN.md` when failure, rollback, or repeated blocking appears.
- Open `LAYER-1/scope-guard.md` when the task starts expanding.

## Routing, state, and execution
- Bootstrap routing starts from `llms.txt`.
- Runtime behavior still follows `LAYER-1/agent-rules.md` for session loading.
- Formal state read/update rules remain tied to `state/MAIN.md` and `LAYER-3/STATE.md`.
- Session transfer context remains in `HANDOFF.md`.

## Migration boundary
- This module partially surfaces approved legacy workflow content from `LAYER-1/workflow.md`, `LAYER-1/interview-system.md`, `LAYER-1/scope-guard.md`, and `LAYER-1/error-handling.md`.
- Those legacy sources still require direct read for the full step sequence, interview guardian mechanics, detailed scope examples, and rollback procedure depth.
- `workflow/MAIN.md` is canonical for workflow entry and routing guidance, but not yet the sole deep source.
- Do not treat this module as policy, state, quality, or incident authority.

## Routing
- Read this module in the core route after state/core-rules.
- Continue via `ROUTES-REGISTRY.md` to optional modules by trigger.
