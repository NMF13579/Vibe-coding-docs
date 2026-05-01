# approval-direct-checks-pass-with-limitations

Broken rule:
- Special PASS_WITH_LIMITATIONS coverage requires dedicated approval validator to be unavailable.

Expected:
- status: SKIPPED
- reason: validate-approval-marker.py is present and mandatory in current MVP path; safe validator-path override is out of scope

Notes:
- This fixture is intentionally skipped in current MVP.
