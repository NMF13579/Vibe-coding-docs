# Validate Queue Entry

## Purpose
Queue Entry Validator checks one queue entry file for required metadata consistency.

## Input file
Run validator for one file:

```bash
python3 scripts/validate-queue-entry.py tasks/queue/{entry}.md
```

## Required fields
Queue entry frontmatter must contain:

- `task_id`
- `status`
- `priority`
- `blocked_by`

## Allowed status values
Allowed values:

- `queued`
- `blocked`
- `in_progress`
- `done`
- `dropped`

## Allowed priority values
Allowed values:

- `high`
- `normal`
- `low`

## blocked_by inline-list format
`blocked_by` must be parseable as inline list:

- `blocked_by: []`
- `blocked_by: [task-a, task-b]`

`blocked_by` must exist.

## Blocked status dependency rule
- If `status: blocked`, then `blocked_by` must contain at least one item.
- If `status != blocked`, `blocked_by` may be empty.

## Empty field rule
A value is treated as empty after trim and paired outer quote removal when it equals:

- empty string
- `null`
- `Null`
- `NULL`
- `~`

Also invalid:

- absent required field
- key with no value

For `task_id`, `status`, and `priority`, empty value fails validation.

## Malformed frontmatter behavior
Validator uses a simple line-by-line parser with Python standard library only.

Rules:

- opening `---` must be first line
- closing `---` must exist
- metadata lines are parsed as `key: value`
- empty lines inside frontmatter are ignored

Missing delimiters fail validation.

## CLI usage

```bash
python3 scripts/validate-queue-entry.py tasks/queue/{entry}.md
```

## PASS / FAIL semantics
- `PASS` + exit code `0`: valid queue entry metadata
- `FAIL` + exit code `1`: missing file, malformed frontmatter, missing/empty required fields, unknown values, or blocked_by rule violation
- exit code `2`: usage error

## Known limitations
- Validator checks one file only.
- Validator parses simple inline list format only.
- Validator does not validate whole queue directory.

## Safety boundaries
Queue Entry Validator checks one file only.
Queue Entry Validator does not validate the whole queue directory.
Queue Entry Validator does not move queue items.
Queue Entry Validator does not approve execution.
Human approval is still required for execution and state transitions.
Queue Entry Validator does not move tasks.
Queue Entry Validator does not update active-task.md.
Queue Entry Validator does not update task state.
