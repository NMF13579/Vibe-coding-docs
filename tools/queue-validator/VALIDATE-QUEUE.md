# Validate Queue Directory

## Purpose
Queue Directory Validator checks queue directory structure and validates each queue entry Markdown file using `scripts/validate-queue-entry.py`.

## Required queue directories
Validator requires these directories:

- `tasks/queue/`
- `tasks/done/`
- `tasks/dropped/`

With `--root PATH`, required directories are resolved as:

- `PATH/tasks/queue/`
- `PATH/tasks/done/`
- `PATH/tasks/dropped/`

## Relationship to validate-queue-entry.py
Queue Directory Validator validates one queue entry at a time by invoking:

```bash
python3 scripts/validate-queue-entry.py <entry.md>
```

It uses `sys.executable` and always resolves `scripts/validate-queue-entry.py` from repository root.

## CLI usage and --root

```bash
python3 scripts/validate-queue.py
python3 scripts/validate-queue.py --root tests/fixtures/queue-directory-validator/valid
```

`--root` changes only the directory scan base for `tasks/*` folders.

## Empty directory behavior
If all required directories exist and no `.md` queue entries are found, validation returns PASS.

## Ignored files
During scan, validator ignores:

- files without `.md` suffix
- `.gitkeep`
- hidden files (names starting with `.`)
- subdirectories

Scan is non-recursive and checks only direct children of each required directory.

## PASS / FAIL semantics
- PASS: required directories exist and all found `.md` entries pass entry validator
- PASS: required directories exist and no `.md` files are found
- FAIL: missing prerequisite `scripts/validate-queue-entry.py`
- FAIL: any required directory is missing
- FAIL: any `.md` queue entry fails entry validation

## Known limitations
- Validator checks structure and file-level validity only.
- Validator does not evaluate cross-file dependency consistency beyond each entry file.

## Safety boundaries
Queue Directory Validator is read-only.
Queue Directory Validator does not move queue items.
Queue Directory Validator does not update task state.
Queue Directory Validator does not approve execution.
Human approval is still required for execution and state transitions.
Queue Directory Validator does not move tasks.
Queue Directory Validator does not update active-task.md.
Queue Directory Validator only validates queue directory structure and queue entry files.
