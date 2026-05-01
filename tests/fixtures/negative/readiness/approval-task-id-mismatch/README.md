# approval-task-id-mismatch

Broken rule:
- approval marker task_id mismatches active task_id.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
