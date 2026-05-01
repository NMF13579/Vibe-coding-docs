# CHECK-EXECUTION-READINESS

## Purpose

`scripts/check-execution-readiness.py` checks Layer 2: Execution Readiness.
It answers: can active task be started from readiness perspective.

References:
- `docs/EXECUTION-READINESS.md`
- `docs/ACTIVE-TASK-VALIDATION.md`
- `tools/state/VALIDATE-ACTIVE-TASK.md`

## Command Usage

```bash
python3 scripts/check-execution-readiness.py
python3 scripts/check-execution-readiness.py --active-task tasks/active-task.md
```

## Prerequisite Gate

First step:

```bash
python3 scripts/validate-active-task.py --active-task <path>
```

Rules:
- if active task validation is `FAIL` or `PARTIAL`, readiness is `FAIL`
- checks after prerequisite are not executed
- `PARTIAL` from active validation is never execution-ready

## What It Checks

After prerequisite PASS:
- approval marker resolution (`approvals/<approval_id>.md`)
- approval validation by dedicated validator if available
- direct approval checks fallback when dedicated validator is missing
- task state compatibility (`active`/`approved_for_execution` in MVP)
- `validate-task-state.py` pass
- `analysis_status` checks:
  - primary: source_contract frontmatter
  - fallback 1: detect-task-state JSON
  - fallback 2: `tasks/<task_id>/state.md` (or equivalent when present)
- change detection availability notes

## Approval Marker Resolution

MVP convention:
- `approval_id: approval-task-001-execution`
- resolves to `approvals/approval-task-001-execution.md`

Failures:
- unresolved marker -> `FAIL`
- malformed marker frontmatter -> `FAIL` (controlled output, no traceback)

## Approval Marker Validation

If `scripts/validate-approval-marker.py` exists:
- run it via subprocess
- non-zero exit -> `FAIL`

If dedicated validator is missing:
- run direct frontmatter checks:
  - `task_id`
  - `scope`
  - `transition`
  - `status`
  - revoked/expired indicators

Direct checks unreliable when:
- frontmatter is unparseable, or
- required fields (`task_id`, `scope`, `transition`, `status`) missing/empty

Outcomes:
- direct mismatch/revoked/expired -> `FAIL`
- direct checks unreliable -> `PARTIAL`
- direct checks pass -> approval validation `PASS_WITH_LIMITATIONS`

`PASS_WITH_LIMITATIONS` means readiness may still be `PASS`, but limitation must be shown in Notes.

## State Checks

Uses existing validators via subprocess when available:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`

Rules:
- missing detect validator -> `PARTIAL` (missing validator)
- detect output non-JSON -> `PARTIAL` (inconclusive state)
- incompatible state -> `FAIL`
- missing validate-task-state validator -> `PARTIAL` (missing validator)
- validate-task-state non-zero -> `FAIL`

## analysis_status Checks

Priority order:
1. source_contract frontmatter
2. detect-task-state JSON output
3. `tasks/<task_id>/state.md` (or equivalent if present)

Blocking values:
- `invalid` -> `FAIL`
- `conflict` -> `FAIL`

If not present in all sources:
- `analysis_status check: NOT PRESENT`
- optional note: requiredness may be unknown in current model

## Change Detection Behavior

If no change detection mechanism is available:
- `source_task change detection: NOT AVAILABLE`
- `source_contract change detection: NOT AVAILABLE`

This is not `FAIL` and not `PARTIAL` by itself.

## What It Does Not Check

- task execution
- runner startup
- completion/failure/drop transitions
- queue movement
- pre-execution evidence report generation

## Allowed Reads

- `tasks/active-task.md`
- source task file
- source contract file
- resolved approval marker file
- outputs of existing read-only validators

## Forbidden Writes

Read-only boundary:
- do not modify `tasks/active-task.md`
- do not modify `tasks/queue/`, `tasks/done/`, `tasks/failed/`, `tasks/dropped/`
- do not modify `reports/`, `approvals/`
- do not change git state

Also forbidden:
- approval generation/repair/refresh
- state mutation
- rollback

## Statuses

- `PASS`: required checks passed
- `FAIL`: required check failed
- `PARTIAL`: required checks could not be completed
- `NOT RUN`: checker not executed

## PARTIAL Semantics (3 cases)

1. Missing validator
- example: `scripts/detect-task-state.py missing`

2. Inconclusive state
- example: detect validator returned non-JSON output

3. Unreliable direct approval checks
- example: dedicated approval validator missing + direct check fields missing/unparseable

All three:
- exit code `1`
- not execution-ready

## Exit Codes

- `PASS` -> `0`
- `FAIL` -> `1`
- `PARTIAL` -> `1`
- `NOT RUN` -> `2`

## Examples

PASS:

```text
Execution Readiness: PASS
Checked:
- active task validation: PASS
- approval marker resolved: PASS
- approval marker valid: PASS
...
Notes:
- PASS means ready-to-start, not done.
```

PASS with limitations:

```text
Execution Readiness: PASS
Checked:
- approval marker valid: PASS_WITH_LIMITATIONS
Notes:
- approval marker direct validation used: scripts/validate-approval-marker.py unavailable
- PASS_WITH_LIMITATIONS: MVP direct checks passed, dedicated approval validator was not used
```

FAIL:

```text
Execution Readiness: FAIL
Failures:
- approval marker unresolved: approvals/approval-task-001-execution.md not found
Exit: 1
```

PARTIAL (missing validator):

```text
Execution Readiness: PARTIAL
Failures:
- scripts/detect-task-state.py missing
- task state could not be fully validated
Exit: 1
```

PARTIAL (inconclusive state):

```text
Execution Readiness: PARTIAL
Failures:
- detect-task-state.py returned non-JSON output
- task state could not be determined
Exit: 1
```

PARTIAL (unreliable direct checks):

```text
Execution Readiness: PARTIAL
Failures:
- scripts/validate-approval-marker.py missing
- approval marker direct checks could not be performed reliably
Exit: 1
```

## Expected Validation Failure vs Implementation Failure

Expected validation failure:
- checker runs correctly
- repository/input invalid
- controlled `FAIL`/`PARTIAL` with clear reason

Implementation failure:
- crash/traceback/uncontrolled exception
- this is a bug and must be fixed

## Safety Boundaries

- Execution readiness is not execution.
- It does not bypass human approval.
- It does not mutate task state.
- It does not move queue/done/failed.
- It does not produce completion proof.
- `PASS` means ready-to-start, not done.
- `PARTIAL` is not ready-to-start.

## Known Limitations

- MVP may use direct approval checks when dedicated approval validator is unavailable.
- change detection can be unavailable and is reported as `NOT AVAILABLE`.
- readiness checker does not run execution and does not produce pre-execution evidence report.
