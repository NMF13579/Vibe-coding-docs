---
type: canonical
module: doctor
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Doctor

## Purpose
Optional operating mode for diagnosis, triage, stabilization, and recovery planning.
Used when project state becomes chaotic or confidence in current path drops.

## When to enter doctor mode
- Repeated failures or conflicting signals block normal execution.
- Context drift, unclear state, or broken routing is suspected.
- Owner asks for health check or controlled recovery plan.

## Doctor mode vs normal workflow
- Normal workflow executes confirmed plan.
- Doctor mode pauses delivery speed and prioritizes system diagnosis.
- Output is a stabilization plan and safe next step, not immediate feature velocity.

## Core tasks in doctor mode
- Diagnose failure type and current impact.
- Triage: critical vs important vs cosmetic.
- Stabilize state/context before new changes.
- Build recovery plan with explicit owner confirmation.

## Active supporting legacy sources
- `LAYER-1/error-handling.md`
- `LAYER-1/context-recovery.md`
- `LAYER-1/audit.md` and `LAYER-1/audit-quick.md`
- `LAYER-3/STATE.md` and `HANDOFF.md`

## Current maturity
- Mode is operational as routing entry.
- Full playbooks and deeper automation are not fully migrated yet.
- Some diagnosis heuristics remain distributed across legacy docs.

## Authority boundary
- Doctor mode does not override core authority model.
- State and core-rules remain canonical during recovery.

## Routing
- Read this module when diagnosis/triage trigger matches.
- Start with state check (`LAYER-3/STATE.md`) and error classification.
- Continue to incident handling and return to workflow after stabilization.
