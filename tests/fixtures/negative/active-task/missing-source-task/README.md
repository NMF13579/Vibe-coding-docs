# missing-source-task
Broken rule:
- source_task field is missing in active-task frontmatter.
Expected:
- status: FAIL
- exit code: 1
Notes:
- This fixture must be rejected by validate-active-task.py.
