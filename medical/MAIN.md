---
type: canonical
module: medical
status: draft
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Medical

## Purpose
Optional domain layer for medical safety constraints.
Not part of universal core route; activated only for medical/clinical context.

## When to read
- Product/task includes clinical workflows or patient-related context.
- Decision may affect medical risk boundaries.
- Task touches medical UX/roles or medical data constraints.

## Medical constraints (current)
- Autonomous clinical decisions by AI are prohibited.
- Human-in-the-loop remains mandatory for critical clinical decisions.
- Medical safety boundaries and legal/data constraints must be respected.

## Active legacy medical sources
- `LAYER-1/MEDICAL-SAFETY.md`
- `LAYER-1/LEGAL-152FZ.md`
- `LAYER-1/UX-CHECKLIST-MEDICAL.md`
- `LAYER-1/MEDICAL-ROLES-AND-PERMISSIONS.md`
- `LAYER-1/MEDICAL-DASHBOARDS.md`

## Relation to core and security
- Core route remains in `core-rules/state/workflow`.
- Medical module adds domain-specific boundaries on top of core rules.
- Security and privacy controls are applied together with medical constraints.

## Migration boundary
- This module is operational as routing entry.
- Detailed clinical/legal procedures remain in legacy medical docs.

## Routing
- Read this module when medical trigger matches.
- Continue to `LAYER-1/MEDICAL-SAFETY.md` and security module as needed.
- Return to workflow/core route for execution decisions.
