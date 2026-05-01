# active-task-validation-partial

Broken rule:
- active-task validation returns PARTIAL and readiness must fail at prerequisite gate.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
