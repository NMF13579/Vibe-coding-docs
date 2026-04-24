---
type: canonical
module: medical
status: canonical
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Medical

## Purpose

Optional support module for medical safety constraints.
Not part of universal startup route; activated only for medical or clinical context.

## When To Read

- Product or task includes clinical workflows or patient-related context.
- A decision may affect medical risk boundaries.
- A task touches medical UX, medical roles, or medical data constraints.

## Medical Constraints

- Autonomous clinical decisions by AI are prohibited.
- Human-in-the-loop remains mandatory for critical clinical decisions.
- Medical safety boundaries and legal/data constraints must be respected.
- Medical context must also use `security/MAIN.md` for sensitive data and access boundaries.

## Routing

- Use `security/MAIN.md` for sensitive data, access, and compliance.
- Use `quality/MAIN.md` for release blockers and verification.
- Use `workflow/MAIN.md` for execution boundaries.
- Use `core-rules/MAIN.md` when authority or ownership is unclear.
