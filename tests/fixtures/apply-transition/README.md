# Apply Transition Fixtures

These fixtures are used by `scripts/test-apply-transition-fixtures.py`.

Safety:
- All fixture execution runs in isolated temporary workspaces.
- Real repository `tasks/` and `reports/` must not be modified.

Fixture groups:
- missing-transition
- protected-applied-record-out
- missing-apply-plan
- missing-applied-evidence
- missing-mutation-plan
- happy-path
