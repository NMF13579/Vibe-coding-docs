# AgentOS Audit Runner

## Purpose

AgentOS Audit Runner aggregates existing release-readiness checks into one command.
It is a read-only orchestration/reporting layer, not a new validator and not a release checklist.

## Command

```
python3 scripts/audit-agentos.py
```

## Runnable Suites

| Suite | Command | Expected |
|---|---|---|
| template-integrity-strict | `python3 scripts/check-template-integrity.py --strict` | exit 0 |
| template-integrity-self-test | `python3 scripts/test-template-integrity.py` | exit 0 |
| negative-fixtures | `python3 scripts/test-negative-fixtures.py` | exit 0 |
| guard-failures | `python3 scripts/test-guard-failures.py` | exit 0 |

## Report

The audit runner writes:

- `reports/audit.md`

## Result Interpretation

PASS means all runnable audit suites passed.
FAIL means at least one runnable audit suite failed or prerequisite was missing.
SKIPPED means the suite is intentionally left for a future milestone.

## Skipped Suites

| Suite | Status | Reason |
|---|---|---|
| release checklist | SKIPPED | future milestone |
| full docs hardening | SKIPPED | future milestone |
| example scenarios | SKIPPED | future milestone |
| prompt packs | SKIPPED | future milestone |

## Prerequisites

The runner requires the outputs of Milestone 7.2, including:

- `scripts/test-guard-failures.py`
- `tools/guard-failure/TEST-GUARD-FAILURES.md`
- `reports/guard-failures-smoke.md`

The guard failure smoke report must contain:

```
## Actual Result

PASS
```

The runner checks the `## Actual Result` section value. It does not treat any arbitrary `PASS` in the file as sufficient.

## Smoke test

Run:

```
python3 scripts/audit-agentos.py
```

Expected result:

```
Result: PASS
```

Smoke report:

- `reports/audit-smoke.md`

Audit report:

- `reports/audit.md`

If the smoke test fails, do not fix unrelated systems automatically.
Record the failed suite or prerequisite and create a follow-up task.

## Non-Goals

AgentOS Audit Runner does not:

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
- act as release checklist
- perform autonomous runner behavior
