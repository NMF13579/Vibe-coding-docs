# approval-marker-expired

Broken rule:
- approval marker has expired expires_at timestamp.

Expected:
- status: FAIL
- exit code: 1

Notes:
- This fixture must be rejected by check-execution-readiness.py.
