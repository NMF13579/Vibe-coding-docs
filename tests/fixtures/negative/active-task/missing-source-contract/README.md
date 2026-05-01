# missing-source-contract
Broken rule:
- source_contract field is missing in active-task frontmatter.
Expected:
- status: FAIL
- exit code: 1
Notes:
- This fixture must be rejected by validate-active-task.py.
