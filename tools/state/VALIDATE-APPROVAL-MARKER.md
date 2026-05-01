# Validate Approval Marker

## Purpose

`validate-approval-marker.py` checks whether an approval marker is valid for a specific task and scope.
Validator checks marker validity only.
Validator does not grant approval.
Validator does not execute transitions.
Validator does not modify files.
Validator does not create `approvals/`.

## Command

```text
python3 scripts/validate-approval-marker.py approvals/{approval-id}.md --task task-001 --scope activate_task
```

Optional transition check:

```text
python3 scripts/validate-approval-marker.py approvals/{approval-id}.md --task task-001 --scope activate_task --transition approved_for_execution:active
```

## Inputs

- marker file path
- `--task <task_id>`
- `--scope <scope>`
- optional `--transition <from:to>`

The validator uses only Python standard library code.
It reads the marker file as read-only input.

## Required Fields

The validator checks that these frontmatter fields exist:

- `approval_id`
- `task_id`
- `approval_type`
- `approved_by`
- `approved_at`
- `status`
- `scope`

`related_contract` is required when:

- `approval_type: execution`
- `scope: activate_task`
- `scope: approve_contract`

## Allowed Values

Allowed `approval_type` values:

- `brief`
- `review`
- `trace`
- `contract`
- `execution`
- `drop`
- `restart`

Allowed `scope` values:

- `approve_brief`
- `approve_contract`
- `activate_task`
- `mark_completed`
- `mark_failed`
- `drop_task`
- `restart_task`

Allowed `status` values:

- `approved`
- `revoked`
- `expired`
- `superseded`

Only `status: approved` is valid approval evidence.

## Scope and Transition Matching

If `--transition` is provided, validator checks that the marker scope matches the requested transition.

Transition to scope map:

- `contract_drafted:approved_for_execution` -> `approve_contract`
- `approved_for_execution:active` -> `activate_task`
- `active:completed` -> `mark_completed`
- `active:failed` -> `mark_failed`
- `active:dropped` -> `drop_task`
- `failed:brief_draft` -> `restart_task`
- `brief_draft:brief_approved` -> `approve_brief`

If `--transition` is not provided, validator checks that the marker scope matches `--scope`.

## Date Rules

- `approved_at` must be a parseable ISO 8601 timestamp with timezone
- `expires_at` may be empty
- if `expires_at` is present and parseable but in the past, validation fails
- if `expires_at` is malformed, validation fails
- timezone offset is required for non-empty timestamps

## Revoked Markers

Markers are revoked if:

- `status: revoked`
- `revoked_at` is present and non-empty
- `revoked_by` is present and non-empty

Revoked markers fail validation.

## Expired Markers

Markers are expired if:

- `status: expired`
- `expires_at` is present and earlier than current UTC time

Expired markers fail validation.

## Superseded Markers

Markers are superseded if:

- `status: superseded`
- `superseded_by` is present and non-empty

Superseded markers fail validation.

## Duplicate Marker Handling

The validator performs a read-only best-effort scan of other `.md` files in the marker directory when that directory exists.

Duplicate handling rules:

- skip the current marker file
- parse other marker files best-effort
- parser failures in unrelated marker files produce warnings, not crashes
- if another marker has the same `task_id`, same `scope`, and `status: approved`, then a different `approval_id` is treated as ambiguous or conflicting
- conflicting markers fail validation unless the other marker is revoked or superseded

The scan may stop after a reasonable file count threshold to avoid slowdowns.

## Output

Human-readable output.

PASS example:

```text
APPROVAL MARKER VALIDATION
Marker: approvals/approval-task-001-execution.md
Task: task-001
Scope: activate_task
Result: PASS
Transition executed: no
Approval granted by validator: no
```

FAIL example:

```text
APPROVAL MARKER VALIDATION
Marker: approvals/approval-task-001-expired.md
Task: task-001
Scope: activate_task
Result: FAIL
Reasons:
- marker expired
Transition executed: no
Approval granted by validator: no
```

## Exit Codes

- `0` - marker valid
- `1` - marker invalid
- `2` - CLI usage error

Missing arguments or `--help` return exit code `2`.

## Safety Boundaries

Validator does not execute transitions.
Validator does not create approval markers.
Validator does not modify approval markers.
Validator does not create `approvals/`.
Validator does not create approvals/ directories.
Validator does not replace `tasks/active-task.md`.
Validator does not move queue entries.
Validator does not mark tasks completed.
Validator does not mark tasks failed.
Validator does not drop tasks.
Validator does not grant release approval.
Validator does not bypass validators.

## Examples

- valid execution approval marker
- revoked marker
- expired marker
- superseded marker
- duplicate/conflicting marker handling

## Out of Scope

Milestone 10.15 does not add:

- approval marker schema
- approval marker fixtures
- approval marker generation
- automatic approval
- automatic transition execution
- approved mode
- `tasks/active-task.md` replacement
- queue movement
- completion automation
- failure automation
- drop automation
- release approval
- approved_by identity format validation
- backend
- RAG
- vector DB
- web UI
