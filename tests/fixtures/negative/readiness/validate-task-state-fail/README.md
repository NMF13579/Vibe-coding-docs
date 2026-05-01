# validate-task-state-fail

Broken rule:
- Case requires capabilities not safely controllable in current MVP without validator path overrides.

Expected:
- status: SKIPPED
- reason: forcing validate-task-state non-zero without validator-path override is unsafe in current MVP

Notes:
- This fixture is intentionally skipped in current MVP.
