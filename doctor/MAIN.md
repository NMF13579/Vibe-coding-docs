---
type: canonical
module: doctor
status: canonical
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Doctor

## Purpose

Optional operating mode for diagnosis, triage, stabilization, and recovery planning.
Used when project state becomes chaotic or confidence in the current path drops.

## When To Enter

- Repeated failures or conflicting signals block normal execution.
- Context drift, unclear state, or broken routing is suspected.
- Owner asks for health check or controlled recovery plan.

## Operating Rules

- Pause delivery speed and prioritize diagnosis.
- Diagnose current impact: critical, important, or cosmetic.
- Stabilize state and context before new changes.
- Build a recovery plan with explicit owner confirmation.

## Routing

- Use `state/MAIN.md` for state recovery.
- Use `workflow/MAIN.md` for recovery planning and execution boundaries.
- Use `quality/MAIN.md` for audit output and proof.
- Use `security/MAIN.md` when safety, data, access, or secrets are involved.
