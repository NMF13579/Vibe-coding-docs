# AgentOS Audit Report

## Command

```
python3 scripts/audit-agentos.py
```

## Result

PASS_WITH_WARNINGS

## Suites

| Suite | Command | Expected | Actual | Result | Notes |
|---|---|---|---|---|---|
| template-integrity-strict | `python3 scripts/check-template-integrity.py --strict` | exit 0 | exit 0 | PASS | |
| template-integrity-self-test | `python3 scripts/test-template-integrity.py` | exit 0 | exit 0 | PASS | |
| negative-fixtures | `python3 scripts/test-negative-fixtures.py` | exit 0 | exit 0 | PASS | |
| guard-failures | `python3 scripts/test-guard-failures.py` | exit 0 | exit 0 | PASS_WITH_WARNINGS | |

## Skipped

- release checklist: future milestone
- full docs hardening: future milestone
- example scenarios: future milestone
- prompt packs: future milestone

## Failure Details

No failures.
## Safety Notes

- Audit runner is read-only except for writing this report.
- No tasks were executed.
- Runner protocol scripts were not executed directly.
- tasks/active-task.md was not modified intentionally.
- Queue items were not moved.
- No validators were created.
- No release checklist was created.
