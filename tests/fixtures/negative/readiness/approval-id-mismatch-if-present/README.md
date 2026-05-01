# approval-id-mismatch-if-present

Broken rule:
- Case requires capabilities not safely controllable in current MVP without validator path overrides.

Expected:
- status: SKIPPED
- reason: current readiness MVP does not compare active approval_id field with marker internal approval_id

Notes:
- This fixture is intentionally skipped in current MVP.
