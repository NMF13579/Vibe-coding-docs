# analysis-status-invalid

Broken rule:
- analysis_status in source_contract is invalid.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
