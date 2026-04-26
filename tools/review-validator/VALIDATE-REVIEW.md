# Validate Review

## Purpose
Review Validator checks consistency of `REVIEW.md` metadata.
It validates whether `review_status` and `execution_allowed` exist, are valid, and match required mapping.

## Input file
The validator reads one file path argument:

```bash
python3 scripts/validate-review.py tasks/{task-id}/REVIEW.md
```

## Required fields
Frontmatter must contain:

- `review_status`
- `execution_allowed`

## Allowed review_status values
Allowed values:

- `READY`
- `READY_WITH_EDITS`
- `NEEDS_CLARIFICATION`
- `TOO_BROAD`
- `TOO_SMALL`
- `DUPLICATE`
- `BLOCKED`

Any other value fails validation.

## execution_allowed mapping
Required mapping:

- `READY` -> `execution_allowed: true`
- `READY_WITH_EDITS` -> `execution_allowed: true`
- `NEEDS_CLARIFICATION` -> `execution_allowed: false`
- `TOO_BROAD` -> `execution_allowed: false`
- `TOO_SMALL` -> `execution_allowed: false`
- `DUPLICATE` -> `execution_allowed: false`
- `BLOCKED` -> `execution_allowed: false`

## Empty field rule
A value is treated as empty after trimming and removing paired outer quotes when it equals:

- empty string
- `null`
- `Null`
- `NULL`
- `~`

Missing key or key with no value is also treated as invalid.

## execution_allowed parser
`execution_allowed` accepts only boolean-like values:

- `true`
- `false`

Parser is case-insensitive (`True`, `FALSE` are accepted).
Any other value fails validation.

## Frontmatter behavior
Validator uses a small line-by-line parser with Python standard library only.

Rules:

- First line must be opening `---`
- A closing `---` must exist
- Only lines in frontmatter are parsed
- Key-value format is `key: value`
- Empty lines in frontmatter are ignored

Missing opening/closing delimiters fails validation.

## CLI usage

```bash
python3 scripts/validate-review.py tasks/{task-id}/REVIEW.md
```

## PASS / FAIL semantics
- `PASS` with exit code `0`: metadata is valid and mapping is consistent
- `FAIL` with exit code `1`: missing field, malformed frontmatter, empty value, unknown status, invalid boolean value, or mapping mismatch
- exit code `2`: usage error (wrong CLI arguments)

## Known limitations
- Parser is intentionally minimal and validates only frontmatter key-value lines.
- Validator checks consistency only; it does not validate review narrative quality.

## Safety boundaries
Review Validator does not approve execution.
Review Validator only checks REVIEW.md consistency.
REVIEW.md does not replace human approval.
Human approval is still required for execution and state transitions.
Review Validator does not move tasks.
Review Validator does not update active-task.md.
Review Validator does not update task state.
