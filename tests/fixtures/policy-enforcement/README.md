# Policy Enforcement Fixtures

## Purpose
This fixture runner validates that policy/preconditions blocking stops controlled apply before lifecycle mutation.

## Controlled apply invocation used
Required enforcement cases use:

```bash
python3 scripts/apply-transition.py --complete-active --policy <policy-fixture> --transition tests/fixtures/policy/read-only-pass.md
```

## Why only pre-mutation-blocking cases
The runner uses only policy cases that must block before mutation so tests are safe on real repository state.

## Why PASS-path controlled mutation is not run
PASS-path controlled mutation is intentionally not run against real lifecycle state to avoid changing real tasks/reports/approvals artifacts.

## Protected paths hash guard
Minimum protected paths:
- tasks/
- reports/
- approvals/
- state/
- lifecycle/
- data/
- handoff/

Extended protected paths (from apply-transition.py write surface review):
- tasks/active-task.md
- tasks/done/
- tasks/completed/

## Enforcement PASS safety rules
Generic CLI errors, usage errors, missing fixture errors, or Python tracebacks must not count as enforcement PASS.

## SUMMARY and exit code
`SUMMARY: WARN` exits with code `0`, so callers must check stdout for WARN explicitly.

## Runner command

```bash
python3 scripts/test-policy-enforcement-fixtures.py
```
