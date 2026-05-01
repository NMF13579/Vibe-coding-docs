# TEST-ACTIVE-TASK-FIXTURES

## Purpose

Runs negative fixtures for Active Task Integrity validation.
It verifies rejection behavior of `scripts/validate-active-task.py`.

References:
- `docs/ACTIVE-TASK-VALIDATION.md`
- `tools/state/VALIDATE-ACTIVE-TASK.md`

## Command Usage

```bash
python3 scripts/test-active-task-fixtures.py
```

## Fixture Directory

```text
tests/fixtures/negative/active-task/
  <case-name>/
    active-task.md
    source-task.md
    source-contract.md
    README.md
```

`missing-active-task` intentionally does not include `active-task.md`.

## Fixture Format

Each `README.md` must contain:

```text
Expected:
- status: FAIL
- exit code: 1
```

or:

```text
Expected:
- status: PARTIAL
- exit code: 1
```

## Expected Status Detection

Runner determines expected status using this MVP rule:

```python
for each line in README.md:
    if line.strip() == "- status: PARTIAL":
        expected_status = PARTIAL
        break
else:
    expected_status = FAIL
```

`strip()` behavior prevents false matches from indentation/trailing spaces.

## Expected Negative Behavior

A negative fixture is PASS only if validator:
- exits with code `1`
- returns `Active Task Validation: <expected_status>`
- does not output `Traceback`

Fixture FAIL cases:
- exit code `0`
- output contains `Active Task Validation: PASS`
- `Traceback` appears
- wrong rejection status (`FAIL` vs `PARTIAL` mismatch)
- validator crash / uncontrolled failure

## PASS / FAIL Semantics

- invalid active task rejected with expected status -> fixture PASS
- invalid active task accepted -> fixture FAIL
- validator traceback/crash -> fixture FAIL
- wrong rejection status -> fixture FAIL

## Exit Codes

- runner exit `0`: all fixtures passed
- runner exit `1`: at least one fixture failed

## Safety Boundaries

Runner is read-only for production state.
It must not modify:
- `tasks/active-task.md`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `reports/`
- `approvals/`
- git state

Runner does not copy fixtures into production `tasks/active-task.md`.

## Path / CWD Requirement

Validator must be called with:

```bash
python3 scripts/validate-active-task.py --active-task <fixture-path>/active-task.md
```

Runner executes subprocess with `cwd=<repo_root>`.
This is required so repository-relative fixture paths resolve consistently.

## Known Limitations

- This suite validates Active Task Integrity only.
- It does not validate execution readiness.
- It does not validate approval resolver behavior (resolver out of scope in 12.3.1).
