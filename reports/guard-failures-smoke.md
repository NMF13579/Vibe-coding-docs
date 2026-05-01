# Guard Failure Runner Smoke Test

## Command

```
python3 scripts/test-guard-failures.py
```

## Expected Result

PASS

## Actual Result

PASS

## Exit Code

0

## Runnable Suites

- template-integrity: PASS
- negative-fixtures: PASS

## Skipped Suites

- review guard failures: future validator
- trace guard failures: future validator
- queue guard failures: future validator
- runner protocol guard failures: future guard test
- audit runner: future milestone
- release checklist: future milestone

## Output Summary

Guard Failure Test Runner executed successfully. Both runnable suites (template-integrity and negative-fixtures) passed validation. All skipped suites are intentionally deferred to future work as validators, guard tests, or milestones.

## Failure Details

No failures.

## Safety Notes

- Runner protocol scripts were not executed directly.
- No new validators were created.
- tasks/active-task.md was not modified intentionally.
- Queue items were not moved.
- Negative fixture payloads were not modified intentionally.
- Template-integrity fixtures were not modified intentionally.
