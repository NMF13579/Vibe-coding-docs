# extra-dangerous-execution-claim
Broken rule:
- active-task asserts autonomous execution claim (invalid state, transition, activated_by).
Expected:
- status: FAIL
- exit code: 1
Notes:
- This fixture must be rejected by validate-active-task.py.
