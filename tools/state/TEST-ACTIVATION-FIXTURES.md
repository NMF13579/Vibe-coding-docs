# TEST-ACTIVATION-FIXTURES

## Purpose

This suite validates rejection behavior for activation safety boundaries.
It proves that invalid activation requests are rejected (fail-closed).

These fixtures test rejection behavior.
They do not prove happy path activation.
They must not modify production `tasks/active-task.md`.

## Fixture Directory Layout

```text
tests/fixtures/negative/activation/
  <case-name>/
    task/
      TASK.md
      REVIEW.md
      TRACE.md
    approvals/
      approval.md
    expected.txt
```

## How To Run

```bash
python3 scripts/test-activation-fixtures.py
```

## Covered Cases

- missing-approved-flag
- both-approved-and-dry-run
- missing-approval-marker
- invalid-approval-marker
- expired-approval-marker
- revoked-approval-marker
- wrong-task-id
- wrong-scope
- wrong-transition
- analysis-status-invalid
- analysis-status-conflict
- check-transition-fail
- contract-missing
- active-task-different-task
- dry-run-does-not-write
- approval-marker-valid-but-no-approved

## PASS/FAIL Semantics

- invalid activation rejected -> fixture PASS
- invalid activation accepted -> fixture FAIL
- unexpected zero exit for invalid case -> FAIL
- unexpected active-task write in temp workspace -> FAIL
- any production `tasks/active-task.md` change -> FAIL

## Temp Workspace Safety Rules

- each case runs in isolated temporary workspace
- runner copies required repo scripts into temp workspace
- runner copies fixture task/approval inputs per case
- checks are executed inside temp workspace only
- no test case depends on production `tasks/active-task.md`

## Production active-task.md Protection

- runner snapshots production `tasks/active-task.md` before cases
- after each case, runner compares production file content
- mismatch triggers case FAIL and suite FAIL

## Known Limitations

- suite focuses on negative and dry-run safety boundaries
- it does not prove positive write-path activation success
- some failures can occur earlier than later checks by design (fail-closed)
