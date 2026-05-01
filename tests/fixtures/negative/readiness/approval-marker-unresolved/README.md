# approval-marker-unresolved

Broken rule:
- approval marker cannot be resolved in fixture-local approval directory.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
