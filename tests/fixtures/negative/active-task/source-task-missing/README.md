# source-task-missing
Broken rule:
- source_task field exists, but referenced file is missing.
Expected:
- status: FAIL
- exit code: 1
Notes:
- This fixture must be rejected by validate-active-task.py.
