# Check Execution Scope

## Purpose

`scripts/check-execution-scope.py` checks whether changed files are inside `source_contract` scope.
This is an MVP file-level checker.
It does not check semantic code correctness.
It does not run verification plan.
It does not complete tasks.

## Command

```bash
python3 scripts/check-execution-scope.py --session reports/execution/<session-id>.md
python3 scripts/check-execution-scope.py --session reports/execution/<session-id>.md --changed-files-from-git
```

## Session Preconditions

Required session fields:

- `session_id`
- `task_id`
- `source_contract`
- `status`
- `readiness_result`
- `changed_files`

Session path rules:

- repository-relative path only
- absolute paths are forbidden
- parent traversal (`..`) is forbidden
- path must exist
- path must be a file

Allowed statuses for scope check:

- `in_progress`
- `evidence_ready`
- `stopped` (allowed by scope model; not yet produced by current M13 scripts)

If session status is `blocked`, result is `NOT RUN` because blocked session has no execution changes to scope-check.
For `stopped`, scope check may run only if changed files are known (session or git). If unknown, result is `NOT RUN`.

## Scope Sources

`source_contract` is read from session and must be:

- repository-relative
- not absolute
- without parent traversal
- existing file

Scope extraction order:

1. `in_scope` / `out_of_scope` from source_contract frontmatter
2. fallback to markdown sections:
   - `## In Scope`
   - `## Out of Scope`

If both `in_scope` and `out_of_scope` are missing, result is `PARTIAL`.

## Scope Entry Safety

Each scope entry must be:

- repository-relative
- not absolute
- without parent traversal
- not empty

Unsafe scope entry causes `PARTIAL`, not `FAIL`, because scope evidence is unreliable.

## Changed Files Detection

Changed files source:

1. if `--changed-files-from-git`: use `git diff --name-only`
2. else if `session.changed_files` is non-empty: use `session.changed_files`
3. else use `git diff --name-only`

If git diff is required but unavailable, result is `NOT RUN`.
If no changed files are found, result is `PASS`.

Changed file path safety is checked before scope matching:

- repository-relative only
- no absolute paths
- no parent traversal
- not empty

Unsafe changed file path causes `FAIL`.

## Path-Boundary Matching

Scope entries are matched as path prefixes with path-boundary awareness.

Examples:

- `scripts/` matches `scripts/check-execution-scope.py`
- `scripts` matches `scripts/check-execution-scope.py`
- `scripts` matches `scripts`
- `scripts` does not match `scripts-old/file.py`
- `scripts/` matches `scripts` (directory itself)

`out_of_scope` has priority over `in_scope`.

## Result Statuses

- `PASS`: changed files are known and no scope violation is detected.
- `FAIL`: out_of_scope violation or unsafe changed file path is detected.
- `PARTIAL`: changed files are known but scope evidence is incomplete/unclear (for example missing scope fields, unsafe scope entry, partial in_scope coverage).
- `NOT RUN`: checker cannot evaluate (invalid session path, unreadable frontmatter, invalid source_contract, unavailable changed files, blocked session).

`PARTIAL` is not success.
It means scope evidence is insufficient to confirm PASS or FAIL.

## Exit Codes

- `0` = `SCOPE_PASS`
- `1` = `SCOPE_FAIL`
- `2` = `SCOPE_PARTIAL_OR_NOT_RUN`

Mapping:

- `PASS` -> exit `0`
- `FAIL` -> exit `1`
- `PARTIAL` -> exit `2`
- `NOT RUN` -> exit `2`

## Safety Boundaries

The checker is read-only.
It must not modify:

- `tasks/active-task.md`
- execution session file
- `source_contract`
- `source_task`
- `reports/execution/.gitkeep`
- queue files
- `approvals/`

It must not create:

- `reports/execution-evidence-report.md`

It must not run:

- verification plan
- task implementation
- completion protocol
- rollback protocol

## Limitations

This is file-level scope checking only.
It does not evaluate code semantics.
It does not prove implementation correctness.
It does not replace verification runner.

## Future Work

Planned follow-up:

- integrate automatic update of session `changed_files`
- integrate verification runner evidence
- add dedicated scope checker fixtures for negative cases
