# approval-scope-mismatch

Broken rule:
- approval marker scope mismatches activate_task.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
