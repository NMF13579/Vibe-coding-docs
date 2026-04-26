# Validate Trace

## Purpose
Trace Validator checks `TRACE.md` consistency and safety boundaries.
It validates required metadata fields and rejects execution-authority claims.

## Input file
Run validator for one trace file:

```bash
python3 scripts/validate-trace.py tasks/{task-id}/TRACE.md
```

## Required fields
Frontmatter must contain non-empty values for:

- `task_id`
- `source_summary`
- `decision_rationale`

## Empty field rule
A required field fails when value is empty after trim and paired outer quote removal.
Values treated as empty:

- `""`
- `''`
- `null`
- `Null`
- `NULL`
- `~`
- absent field
- key with no value

## Forbidden execution authority claims
TRACE must not contain execution-authority phrases.
Validator rejects case-insensitive substring matches across the whole file content.

Forbidden phrases:

- `execution approved`
- `approved for execution`
- `execution_allowed: true`
- `authorizes execution`
- `approval granted`
- `trace replaces task.md`
- `trace replaces review.md`
- `replaces task.md`
- `replaces review.md`
- `active-task.md updated`
- `active task updated`
- `task is now active`

## Forbidden phrase match semantics
Matching is case-insensitive substring search on entire file content, including frontmatter.
Negations still fail (example: `no execution approved` also fails).

## Malformed frontmatter behavior
Validator uses a minimal line-by-line parser with Python standard library only.

- first line must be `---`
- closing `---` must exist
- frontmatter lines are parsed as `key: value`
- empty frontmatter lines are ignored

Missing delimiters fail validation.

## CLI usage

```bash
python3 scripts/validate-trace.py tasks/{task-id}/TRACE.md
```

## PASS / FAIL semantics
- `PASS` + exit code `0`: valid required metadata and no forbidden phrases
- `FAIL` + exit code `1`: missing file, malformed frontmatter, missing/empty required field, or forbidden phrase
- exit code `2`: usage error

## Known limitations
- Parser is intentionally minimal and does not implement full YAML features.
- Validator checks consistency and safety phrases only, not writing quality.

## Safety boundaries
Trace Validator does not approve execution.
Trace Validator only checks TRACE.md consistency and safety boundaries.
TRACE.md does not replace TASK.md.
TRACE.md does not replace REVIEW.md.
Human approval is still required for execution and state transitions.
Trace Validator does not move tasks.
Trace Validator does not update active-task.md.
Trace Validator does not replace task contract.
