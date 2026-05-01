# Template Integrity Checker

Template Integrity Checker checks whether the AgentOS template still has the required file and directory structure for release readiness.

It is a read-only checker. Read-only means it only reads files and folders, prints a report, and exits with `PASS`, `PASS_WITH_WARNINGS`, or `FAIL`.

## How to run

Run from the repository root:

```bash
python3 scripts/check-template-integrity.py
```

Run against an explicit root:

```bash
python3 scripts/check-template-integrity.py --root tests/fixtures/template-integrity/valid-template
```

`--root` points the checker at another directory and treats that directory as the template root.

## Strict mode

Use strict mode for CI/release gates:

```bash
python3 scripts/check-template-integrity.py --strict
```

Strict mode treats warnings as blocking for exit code purposes, but the printed result remains `PASS_WITH_WARNINGS`.

When result is `FAIL`, `--strict` has no additional effect.

## What it checks

The checker verifies required AgentOS template areas:

- core files;
- input layer;
- task brief validation;
- review and trace files;
- contract generation files;
- queue lifecycle files and directories;
- runner dry-run protocol files;
- task health metrics files;
- `.gitignore` runtime artifact rule;
- forbidden auto-runner file paths;
- optional fixture directories;
- task health report presence.

## Result states

PASS:

- no errors
- no warnings

PASS_WITH_WARNINGS:

- no errors
- at least one warning
- normal mode exit code: 0
- strict mode exit code: 1

FAIL:

- at least one error
- exit code: 1 regardless of `--strict`
- warnings may still be printed, but result remains FAIL

`PASS` means every required file and directory exists, `.gitignore` contains `tasks/drafts/`, and no forbidden file path exists.

The command exits with code `0`.

`PASS_WITH_WARNINGS` means the template structure is not broken, but release-readiness is incomplete.

`FAIL` means at least one required file or directory is missing, `.gitignore` is missing or does not contain `tasks/drafts/`, the root path is invalid, or a forbidden file path exists.

The command exits with code `1`.

The checker collects all section errors and warnings before printing the final result.

## Warning-level checks

Warnings indicate incomplete release-readiness, not broken template structure.

All warning checks are evaluated relative to `--root`.

Current warning-level checks:

- missing `tests/fixtures/task-brief/`
- missing `tests/fixtures/contract-generation/`
- missing `tests/fixtures/agent-runner/`
- missing `tests/fixtures/task-health/`
- missing `reports/task-health.md`

## Self-test

Run all Template Integrity Checker fixtures:

```bash
python3 scripts/test-template-integrity.py
```

The self-test verifies:

- normal PASS behavior
- normal FAIL behavior
- normal PASS_WITH_WARNINGS behavior
- strict mode warning behavior
- expected exit codes
- expected `Result:` lines

The self-test only invokes:

```text
scripts/check-template-integrity.py
```

It does not execute tasks, move queue items, generate contracts, or run runner scripts.

## Forbidden auto-runner files

Forbidden auto-runner files are blocked because AgentOS must stay a Markdown-first guardrail framework. It must not become an autonomous runner that chooses, approves, or executes work by itself.

The checker only checks the exact forbidden relative paths. It does not search for similar file names.

## Runtime artifacts

`tasks/drafts/` must be listed in `.gitignore` because draft contracts are runtime artifacts.

Runtime artifacts are files created while using the system. They should not become a required tracked part of the template.

## Non-goals

Template Integrity Checker does not:

- execute tasks
- modify tasks/active-task.md
- generate task contracts
- move queue items
- approve execution
- run agent-next.py
- run agent-complete.py
- run agent-fail.py
- implement autonomous runner behavior
