# Test Execution Runner Fixtures

## Purpose

This fixture suite validates M13 safety behavior for execution runner components.
It focuses on rejecting unsafe or not-ready states.

## Fixture Directory

Fixtures live under:

- `tests/fixtures/negative/execution-runner/<case-name>/`

Case structure:

- `README.md`
- `expected.json`
- optional `active-task.md`
- optional `session.md`
- optional `source-contract.md`
- optional `approvals/`

## expected.json

Each case defines:

- `case`
- `target` (`dry-run`, `start`, `scope`, `verification`)
- `command` (description)
- `expected_result`
- `expected_exit_code`
- `must_not_create_session`
- `must_not_modify_fixture_inputs`
- `notes`

Primary assertion is `expected_exit_code`.
`expected_result` marker in stdout/stderr is secondary evidence.

## Supported Targets

Fixture runner executes selected M13 scripts:

- `scripts/run-active-task.py --dry-run`
- `scripts/run-active-task.py --start`
- `scripts/check-execution-scope.py`
- `scripts/run-execution-verification.py`

## Result Semantics

Fixture runner statuses are only:

- `PASS`
- `FAIL`
- `SKIPPED`

`PASS` means fixture expectation is satisfied (usually unsafe input was rejected).
For behavior coverage (`expected_result: PASS`), `PASS` means expected successful behavior matched.

Target result values (`PASS`, `FAIL`, `PARTIAL`, `NOT RUN`) are not fixture statuses.
Target `FAIL`/`PARTIAL`/`NOT RUN` can still mean fixture `PASS` when that is expected.

PASS / FAIL / SKIPPED are the only fixture suite statuses.

## Isolation Rules

Start case isolation priority:

1. Priority 1: use direct invalid input when `must_not_create_session: true` (used for all start cases here)
2. Priority 2: if case could create production session, mark `SKIPPED` with rationale
3. Priority 3: prohibited — no `shutil.copytree` of repository root

Fixtures must not write into production `tasks/active-task.md`, `approvals/`, queue/done/failed state, or production `reports/execution/*.md`.

## Production Mutation Protection

Before/after each case, runner snapshots protected paths:

- `tasks/active-task.md`
- `reports/execution-evidence-report.md`
- `reports/execution/`
- `approvals/`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`

Any mutation in protected paths marks case as `FAIL`.

## Marker Check

`expected_result` marker in output is secondary evidence.

- If marker is found and exit code matches: fixture `PASS`
- If marker is missing but exit code matches: fixture `PASS` + warning
- If marker is missing and exit code mismatches: fixture `FAIL`

Missing marker warning does not create extra statuses.

## Command

Run suite:

```bash
python3 scripts/test-execution-runner-fixtures.py
```

Show help:

```bash
python3 scripts/test-execution-runner-fixtures.py --help
```

## Known Limitations

- Exit code is primary assertion; marker matching is best-effort secondary evidence.
- Command mapping is case-name based in MVP.
- Full temporary repo cloning is intentionally not used for safety.
- Cases that might create production session without safe override are skipped.

## Future Work

- richer command templates in `expected.json`
- per-target output parser for stronger marker validation
- additional artifact-level checks for generated temporary files
