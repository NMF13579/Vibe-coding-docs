# Activation Recovery

## 1. Purpose

This document defines manual recovery rules for incorrect activation in Milestone 11.
It explains how to preserve evidence, restore a safe `active-task.md` state, and maintain traceability.

Core rule:
- Recovery must preserve evidence before changing state.
- Do not hide incorrect activation.
- Do not silently delete evidence.
- Do not rewrite history to make the activation look like it never happened.

## 2. Scope

This document covers recovery from incorrect activation only.
It does not define automatic rollback.
It does not define task execution recovery.
It does not define task completion recovery.
It does not define queue recovery.
It does not define release rollback.

## 3. What Counts as Incorrect Activation

Examples:
- wrong task activated
- wrong approval marker used
- approval marker later discovered invalid
- `active-task.md` references wrong `source_contract`
- activation happened with wrong transition
- `active-task.md` overwritten unexpectedly
- activation happened in wrong workspace
- activation occurred despite failed/unknown checks
- manual edit corrupted `active-task.md`

## 4. Immediate Response

1. Stop task execution immediately.
2. Do not continue from the incorrect `active-task.md`.
3. Do not delete `active-task.md` immediately.
4. Preserve current `active-task.md` as evidence.
5. Record the activation command if known.
6. Record relevant terminal output if available.
7. Identify approval marker and source task.

## 5. Evidence Preservation

Save at minimum:
- current `tasks/active-task.md`
- previous `tasks/active-task.md` if known
- activation command
- approval marker used
- source task path
- source contract path
- terminal output
- git diff
- timestamp of discovery
- person/agent who discovered issue
- reason activation is considered incorrect

Recommended evidence location:
- `incidents/activation/`

Example file:
- `incidents/activation/incident-YYYYMMDD-HHMM-incorrect-activation.md`

## 6. Manual Recovery Flow

1. Preserve evidence.
2. Create incident record.
3. Decide desired recovered state:
   - no active task
   - previous active task
   - corrected active task via approved activation
4. Restore manually only after evidence is saved.
5. Re-run validation.
6. Add note to incident with recovery result.

## 7. Recovery Option A — No Active Task

1. Save current `active-task.md` into incident evidence.
2. Remove `tasks/active-task.md` manually.
3. Record why no active task is safer.
4. Run validation/audit commands.
5. Update incident record.

Important:
- Do not delete `active-task.md` before copying it into evidence.

## 8. Recovery Option B — Restore Previous Active Task

1. Save incorrect `active-task.md` into incident evidence.
2. Restore previous `active-task.md` from git, backup, or incident evidence.
3. Verify restored `task_id`.
4. Run validation/audit commands.
5. Update incident record.

Example command (only if suitable for current repo state):

```bash
git checkout -- tasks/active-task.md
```

## 9. Recovery Option C — Corrected Activation

1. Preserve incorrect `active-task.md` as evidence.
2. Resolve why incorrect activation happened.
3. Prepare valid approval marker for corrected task.
4. Run `activate-task.py` in `--dry-run` first.
5. Run `activate-task.py` with `--approved` only after dry-run PASS and explicit human confirmation.
6. Record corrected activation in incident.

Important:
- Corrected activation must follow the same Milestone 11 approved flow.
- Recovery must not bypass `--approved`.

## 10. Required Validation After Recovery

Run:

```bash
python3 scripts/activate-task.py --help
python3 scripts/test-activation-fixtures.py
python3 scripts/agentos-validate.py activation-fixtures
git diff -- tasks/active-task.md
```

If recovery changes audit assumptions:
- update `reports/activation-audit-report.md`

Do not run production activation with `--approved` unless doing Recovery Option C with explicit human approval.

## 11. Incident Record Template

# Activation Incident

## Summary
Incorrect activation detected.

## Discovered At
`<UTC timestamp>`

## Discovered By
`<human/agent>`

## Incorrect Active Task
`<task_id/path>`

## Approval Marker Used
`<approval path>`

## Source Contract
`<contract path>`

## Activation Command

```bash
<command if known>
```

## Why It Was Incorrect
`<reason>`

## Evidence Preserved
- `<item>`
- `<item>`
- `<item>`
- `<git diff>`

## Recovery Option Chosen
No active task / Restore previous active task / Corrected activation

## Recovery Steps Taken
`<steps>`

## Validation After Recovery
`<commands and results>`

## Follow-up
`<lessons/rules/tests to add>`

## 12. What Not To Do

- do not silently delete `active-task.md`
- do not overwrite `active-task.md` before preserving evidence
- do not edit approval marker to make history look valid
- do not remove failed terminal output from report
- do not bypass `--approved` during corrected activation
- do not modify `queue/done/failed/dropped` as part of activation recovery unless separately approved
- do not mark task complete as part of activation recovery
- do not generate approval marker retroactively to justify activation

## 13. Relationship to Incidents and Lessons

- incorrect activation should create an incident record
- if root cause is a missing guard, add or update negative fixture later
- if root cause is ambiguous documentation, update docs
- if root cause is repeated human mistake, add checklist or rule

## 14. Known Limitations

- Milestone 11 does not provide automated rollback.
- Recovery is manual by design.
- Recovery rules do not replace activation fixtures.
- Recovery rules do not prove implementation correctness.

## 15. Non-goals

This document does not define:
- rollback script
- automatic incident creation
- queue recovery automation
- task execution rollback
- completion rollback
- release rollback
- database rollback
- deployment rollback
