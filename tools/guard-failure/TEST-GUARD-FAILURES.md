# Guard Failure Test Runner

## Purpose

Guard Failure Runner aggregates existing guard/failure checks into one command.
It is an orchestration layer, not a new validator.

## Command

python3 scripts/test-guard-failures.py

## Runnable Suites

| Suite | Command | Expected |
|---|---|---|
| template-integrity | `python3 scripts/test-template-integrity.py` | exit 0 |
| negative-fixtures | `python3 scripts/test-negative-fixtures.py` | exit 0 |

## Skipped Suites

| Suite | Status | Reason |
|---|---|---|
| review guard failures | SKIPPED | future validator |
| trace guard failures | SKIPPED | future validator |
| queue guard failures | SKIPPED | future validator |
| runner protocol guard failures | SKIPPED | future guard test |
| audit runner | SKIPPED | future milestone |
| release checklist | SKIPPED | future milestone |

## Result Interpretation

PASS means all runnable suites passed.
FAIL means at least one runnable suite failed or prerequisite was missing.
SKIPPED means the suite is intentionally not automated yet.

## Prerequisites

The runner requires:

- `scripts/test-template-integrity.py`
- `scripts/check-template-integrity.py`
- `scripts/test-negative-fixtures.py`
- `tools/template-integrity/CHECK-TEMPLATE-INTEGRITY.md`
- `tools/negative-fixtures/TEST-NEGATIVE-FIXTURES.md`
- `reports/negative-fixtures-smoke.md`

The smoke report must contain:

```markdown
## Actual Result

PASS
```

The runner checks the `## Actual Result` section value. It does not treat any
arbitrary `PASS` in the file as sufficient.

## Smoke test

Run:

```
python3 scripts/test-guard-failures.py
```

Expected result:

```
Result: PASS
```

Smoke report:

- `reports/guard-failures-smoke.md`

If the smoke test fails, do not fix unrelated systems automatically.
Record the failed suite or prerequisite and create a follow-up task.

## Non-Goals

Guard Failure Runner does not:

- create new validators
- validate review files directly
- validate trace files directly
- validate queue entries directly
- run agent-next.py
- run agent-complete.py
- run agent-fail.py
- execute tasks
- modify tasks/active-task.md
- move queue items
- act as audit runner
- act as release checklist
- perform autonomous runner behavior
