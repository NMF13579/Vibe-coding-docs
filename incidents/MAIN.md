---
type: canonical
module: incidents
status: canonical
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Incidents

## Purpose

Optional support module for incident handling, rollback context, and lessons learned.
Used when normal workflow is interrupted by failure, regression, or risk escalation.

## When To Read

- Owner reports failure, breakage, or emergency stop.
- Rollback or recovery path is required.
- Post-incident analysis and prevention updates are needed.

## Error Classification

- Process error: a required step was skipped.
- Logic error: the approach is wrong or does not solve the task.
- Context error: project state or prior decision is unclear.
- Scope error: the task expanded beyond the current scope.
- Block error: the task is blocked by an external dependency.
- Semantic error: the result does not match what was asked.

## Stop Conditions

- Two recovery attempts fail.
- The failure repeats after an apparent fix.
- There is risk to safety, data, or core stability.
- Scope breakage damages working functionality.

## Routing

- Use `state/MAIN.md` to recover state.
- Use `workflow/MAIN.md` to plan recovery.
- Use `quality/MAIN.md` for post-incident proof.
- Use `security/MAIN.md` when safety, data, access, or secrets are involved.
