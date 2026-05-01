# Detect Task State

## Purpose

`scripts/detect-task-state.py` is a read-only detector for Task State Report v1.1.
It inspects task evidence and returns a JSON report for the current task state.
It does not validate transitions and does not execute transitions.

## Output Format

The detector prints Task State Report v1.1 as JSON.

Required fields:

- `schema_version`
- `generated_at`
- `task_id`
- `state`
- `analysis_status`
- `evidence`
- `missing_evidence`
- `allowed_next_states`
- `blocked_reason`
- `warnings`

`schema_version` is always `"1.1"`.
`generated_at` is a UTC ISO 8601 timestamp.

## Analysis Status

| analysis_status | Meaning |
|---|---|
| `ok` | state is consistent with current evidence |
| `invalid` | state was detected, but required path/evidence has gaps |
| `conflict` | mutually exclusive evidence exists |

`state_conflict` is deprecated and must not be emitted as a task state.
Conflicts are represented as `analysis_status: conflict`.
The detector still emits the strongest task state by priority.

## Detector Priority

1. Terminal evidence
   - `completed`
   - `dropped`
   - `failed`, if concrete failed evidence exists
2. Runtime evidence
   - `active`
3. Approval / execution preparation evidence
   - `approved_for_execution`
   - `contract_drafted`
   - `trace_written`
4. Review evidence
   - `review_ready`
   - `review_blocked`
5. Brief evidence
   - `brief_approved`
   - `brief_draft`
6. Fallback
   - `idea`

Examples:

- `completed` + `tasks/active-task.md` reference -> `state: completed`, `analysis_status: conflict`
- `dropped` + `tasks/active-task.md` reference -> `state: dropped`, `analysis_status: conflict`
- `TRACE.md` exists but `REVIEW.md` missing -> `state: trace_written`, `analysis_status: invalid`
- contract draft exists but `TRACE.md` missing -> `state: contract_drafted`, `analysis_status: invalid`

## Evidence

`evidence` is an array of structured objects.
Each item has:

- `type`
- `path`
- `status`
- `note`

Allowed `evidence.status` values:

- `present`
- `missing`
- `valid`
- `invalid`
- `conflicting`
- `planned`

`warnings` is always present and is emitted as `[]` when there are no warnings.

## Read-Only Guarantee

The detector is read-only.
It only reads evidence and returns a JSON report.
It does not modify task files.
It does not create approval markers.
It does not create `tasks/failed/`.
It does not replace `tasks/active-task.md`.
It does not move queue entries.

## Exit Codes

- `0` - JSON report successfully produced
- `1` - runtime or fatal error, such as an unreadable filesystem or unexpected exception
- `2` - CLI usage error or `--help`

## Safety Boundaries

The detector does not:

- validate transitions
- execute transitions
- modify task files
- create approval markers
- create `tasks/failed/`
- replace `tasks/active-task.md`
- move queue entries
- grant execution authority

