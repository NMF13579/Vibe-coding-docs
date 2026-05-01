# Validate Contract Draft

## Purpose
Contract Draft Validator checks internal consistency and safety boundaries of contract draft files.

## Input file
Run validator on one draft file:

```bash
python3 scripts/validate-contract-draft.py tasks/drafts/{task-id}-contract-draft.md
```

## Required frontmatter fields
Required non-empty fields:

- `task_id`
- `generated_from_task`
- `review_file`
- `review_status`
- `execution_allowed`

## Allowed review_status values
Allowed values are only:

- `READY`
- `READY_WITH_EDITS`

## execution_allowed rule
`execution_allowed` accepts boolean-like values (`true` / `false`, case-insensitive), but valid contract draft requires:

- `execution_allowed: true`

`false` fails validation.
Non-boolean values fail validation.

## Required body sections
Draft body must include:

- `## Verification`
- one risk heading from:
  - `## Risk / Rollback`
  - `## Risk and Rollback`
  - `## Risk`

## Forbidden phrases
Validator rejects draft when forbidden phrase is found in full content (frontmatter + body), case-insensitive substring match.

Examples of violating phrases:

- `replace active-task.md`
- `replaces active-task.md`
- `update active-task.md`
- `updates active-task.md`
- `active-task.md updated`
- `task is now active`
- `promoted to active`
- `approved for execution`
- `execution approved`
- `approval granted`
- `auto-promote`
- `automatic promotion`

These are examples of violations, not instructions.

## Empty field rule
A required value is treated as empty after trim + paired outer quote removal when it equals:

- empty string
- `null`
- `Null`
- `NULL`
- `~`

Also invalid:

- absent required field
- key without value

## Malformed frontmatter behavior
Frontmatter is parsed line-by-line using Python standard library only.

Rules:

- first line must be `---`
- closing `---` must exist
- key-value lines parsed as `key: value`
- empty lines in frontmatter are ignored

No opening or no closing delimiter causes FAIL.

## Optional file existence checks
Validator may check `generated_from_task` and `review_file` paths relative to repository root.
Missing path is `WARN`, not `FAIL`.

MVP scope: `review_file` validation checks only empty value as required field; path format is not validated.

## CLI usage

```bash
python3 scripts/validate-contract-draft.py tasks/drafts/{task-id}-contract-draft.md
```

## PASS / FAIL semantics
- PASS + exit code 0: required fields valid, required sections present, no forbidden phrases
- FAIL + exit code 1: missing file, malformed frontmatter, missing/empty fields, invalid values, missing sections, forbidden phrase
- exit code 2: usage error

## Known limitations
- Validator is intended only for contract draft files.
- Parser is intentionally minimal and does not implement full YAML.
- Validator checks internal consistency and safety boundaries only.

## Safety boundaries
Contract Draft Validator is read-only.
Contract Draft Validator is intended only for contract draft files.
Contract Draft Validator does not approve execution.
Contract Draft Validator does not promote drafts.
Contract Draft Validator does not update tasks/active-task.md.
Contract Draft Validator does not move queue items.
Human approval is still required for execution and state transitions.
