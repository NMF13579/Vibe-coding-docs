# approval-transition-mismatch

Broken rule:
- approval marker transition mismatches approved_for_execution:active.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
