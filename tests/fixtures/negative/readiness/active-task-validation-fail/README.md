# active-task-validation-fail

Broken rule:
- active-task validation prerequisite fails (state is queued).

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
