# Validate Runner Protocol

## Purpose
Runner Protocol Validator checks safety markers and unsafe patterns in runner scripts.

## Target runner scripts
Validator checks only Python runner scripts:

- `scripts/agent-next.py`
- `scripts/agent-complete.py`
- `scripts/agent-fail.py`

Markdown documentation is not checked.

## Static-only validation
Validation is static-only. Runner scripts are not executed.

## Order of checks
For each existing runner script, checks run in this order:

1. required marker check
2. unsafe pattern check
3. safety marker exception check

Rules:

- missing required marker -> FAIL
- required marker present + unsafe patterns + safety marker -> PASS_WITH_WARNINGS
- required marker present + no unsafe patterns -> PASS
- required marker present + unsafe patterns + no safety marker -> FAIL

## Required markers
`agent-next.py` requires one of:

- `dry-run`
- `--dry-run`

`agent-complete.py` requires one of:

- `human checkpoint`
- `confirmation`
- `requires approval`
- `manual approval`

`agent-fail.py` requires one of:

- `human checkpoint`
- `confirmation`
- `requires approval`
- `manual approval`

## Forbidden unsafe patterns
Case-insensitive substring match over full script content.

Patterns:

- `shutil.move(`
- `os.rename(`
- `Path.rename(`
- `Path.replace(`
- `write_text(`
- `open("tasks/active-task.md", "w")`
- `open('tasks/active-task.md', 'w')`
- `tasks/active-task.md`
- `tasks/done/`
- `tasks/failed/`

## Why tasks/queue/ is excluded
`tasks/queue/` may appear in comments or documentation-like strings without state transition semantics.
It is intentionally excluded from forbidden patterns.

## Safety marker exception
Unsafe patterns can downgrade from FAIL to PASS_WITH_WARNINGS if at least one safety marker exists.

Safety markers:

- `dry-run`
- `--dry-run`
- `human checkpoint`
- `requires approval`
- `manual approval`
- `explicit approval`
- `confirmation required`
- `approved mode disabled`
- `approved mode not implemented`

If multiple unsafe patterns are found in one file, they are reported together.

## Result semantics
- `PASS` -> all checked files pass and have no warnings
- `PASS_WITH_WARNINGS` -> at least one warning and no failures
- `FAIL` -> at least one file fails

Exit codes:

- PASS: `0`
- PASS_WITH_WARNINGS: `0`
- FAIL: `1`

## All-missing behavior
If all target runner files are missing, result is `PASS_WITH_WARNINGS`.

## CLI usage

```bash
python3 scripts/validate-runner-protocol.py
python3 scripts/validate-runner-protocol.py --root tests/fixtures/runner-validator/valid
```

With `--root`, checked files are resolved as `<root>/scripts/agent-*.py`.

## Known limitations
- Validator uses substring checks and does not parse Python AST.
- Validator targets only three runner script paths.

## Safety boundaries
Runner Protocol Validator is static-only.
Runner Protocol Validator does not execute runner scripts.
Runner Protocol Validator does not move queue items.
Runner Protocol Validator does not update active-task.md.
Runner Protocol Validator does not approve execution.
Runner Protocol Validator checks only Python runner scripts, not Markdown documentation.
Human approval is still required for execution and state transitions.
