---
type: canonical
module: incidents
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Incidents

## Purpose
Optional entry for incident handling, rollback context, and lessons learned.
Used when normal workflow is interrupted by failure, regression, or risk escalation.

## When to read
- Owner reports failure, breakage, or emergency stop.
- Rollback/recovery path is required.
- Post-incident analysis and prevention updates are needed.

## How incident layer differs from normal workflow
- Normal workflow optimizes delivery execution.
- Incident layer prioritizes stabilization, containment, and recovery.
- Incident evidence is situational context, not global policy authority.

## Active legacy incident sources
- `LAYER-1/error-handling.md`
- `LEARNING-LOOP.md`
- `incidents/incident-template.md`
- `LAYER-1/audit.md` (post-incident controls)

## Usage model
- Record incident facts in `incidents/` using template.
- Link corrective action to relevant policy/workflow docs.
- Add prevention checks through audit/quality flow.

## Relation to doctor mode
- Incident module captures evidence and recovery context.
- Doctor mode handles diagnosis/triage/stabilization decisions.

## Routing
- Read this module when incident trigger matches.
- Continue to `LAYER-1/error-handling.md` for rollback protocol.
- If system state is unstable, open `doctor/MAIN.md`.
