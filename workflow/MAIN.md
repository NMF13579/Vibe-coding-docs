---
type: canonical
module: workflow
status: draft
authority: canonical
when_to_read: always
owner: unassigned
---

# Workflow

## Purpose
Operational execution backbone for tasks in the new core route.
Defines how planning, execution, verification, and context updates are performed.

## Execution protocol (current)
1. Receive task and align scope.
2. Build plan and request explicit confirmation.
3. Execute only after explicit approval.
4. Run self-checks/tests relevant to the task.
5. Report result and update context/state artifacts.

## Routing, state, and execution
- Bootstrap routing starts from `llms.txt`.
- Runtime behavior follows `LAYER-1/agent-rules.md` session-load contract.
- Formal state read/update rules remain tied to `LAYER-3/STATE.md`.
- Session transfer context remains in `HANDOFF.md`.

## Safe change criteria
- Change is within confirmed scope.
- No conflict with formal state guards/forbidden actions.
- Verification completed before closing task.
- Handoff/context updates are done for continuity.

## Done / not done
- Done: planned scope implemented, verified, and reflected in required context docs.
- Not done: no explicit approval, missing verification, unresolved blocker, or missing handoff/context update.

## When to open additional docs
- Open `LAYER-1/error-handling.md` on incident/rollback trigger.
- Open `LAYER-1/scope-guard.md` when task starts expanding.
- Open QA/security/medical modules only when trigger requires.

## Active legacy sources (transition phase)
- `LAYER-1/workflow.md`
- `LAYER-1/agent-rules.md`
- `LAYER-1/error-handling.md`
- `LAYER-3/STATE.md`, `HANDOFF.md`

## Migration boundary
- This module is the core workflow entry in new architecture.
- Detailed step-by-step procedures remain in legacy workflow docs for now.

## Routing
- Read this module always after state/core-rules in core route.
- Continue via `ROUTES-REGISTRY.md` to optional modules by trigger.
