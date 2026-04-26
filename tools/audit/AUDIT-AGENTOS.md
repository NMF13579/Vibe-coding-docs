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

The runner executes suites via `sys.executable`, not hardcoded `python3`.

Guard-failures section runs `scripts/test-guard-failures.py`.
Guard failure runner covers:
- template-integrity
- negative-fixtures
- runner-protocol

Coverage flow:
- review, trace, queue, contract-draft are covered through `scripts/test-negative-fixtures.py`
- runner-protocol is covered through `scripts/test-guard-failures.py`

## Report

The audit runner writes:

- `reports/audit.md`

## Result Interpretation

PASS means all runnable audit suites returned PASS.
PASS_WITH_WARNINGS means there are no FAIL suites, but at least one suite returned PASS_WITH_WARNINGS or WARN/SKIPPED.
FAIL means at least one runnable suite failed.
SKIPPED means the suite is intentionally left for a future milestone.

Exit codes:
- PASS: `0`
- PASS_WITH_WARNINGS: `0`
- FAIL: `1`

## Skipped Suites

| Suite | Status | Reason |
|---|---|---|
| release checklist | SKIPPED | future milestone |
| full docs hardening | SKIPPED | future milestone |
| example scenarios | SKIPPED | future milestone |
| prompt packs | SKIPPED | future milestone |

## Prerequisites

- `scripts/audit-agentos.py` must exist.
- `scripts/test-guard-failures.py` is optional for this section:
  if missing, guard-failures is reported as `WARN` and overall result degrades to `PASS_WITH_WARNINGS`.

## Smoke test

Run:

```
python3 scripts/audit-agentos.py
```

Expected result:

```
Result: PASS / PASS_WITH_WARNINGS / FAIL
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
- approve execution
- execute tasks
- modify tasks/active-task.md
- move queue items
- act as release checklist
- perform autonomous runner behavior
