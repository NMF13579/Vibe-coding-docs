# Policy Flow Smoke

## Purpose
This smoke runner checks the M18 policy flow at high level without mutating real lifecycle state.

## Commands covered
- `python3 scripts/validate-policy.py tests/fixtures/policy/read-only-pass.md`
- `python3 scripts/validate-policy.py tests/fixtures/policy/forbidden-mutation-blocked.md`
- `python3 scripts/check-apply-preconditions.py --policy tests/fixtures/policy/real-lifecycle-approval-required-pass.md --transition tests/fixtures/policy/read-only-pass.md`
- `python3 scripts/check-apply-preconditions.py --policy tests/fixtures/policy/unsupported-mutation-blocked.md --transition tests/fixtures/policy/read-only-pass.md`
- `python3 scripts/apply-transition.py --complete-active --policy tests/fixtures/policy/forbidden-mutation-blocked.md --transition tests/fixtures/policy/read-only-pass.md`
- `python3 scripts/audit-policy-boundary.py`

## Safety boundary
PASS-path controlled mutation is not run against real lifecycle state.
Controlled apply smoke uses only pre-mutation-blocking policy cases.

## Hash guard protected paths
- tasks/
- reports/
- approvals/
- state/
- lifecycle/
- data/
- handoff/

## Summary meaning
- `SUMMARY: PASS` all required smoke checks passed and hash guard passed.
- `SUMMARY: WARN` required checks passed but controlled-apply safe limitation or audit WARN exists.
- `SUMMARY: FAIL` at least one required check failed or hash guard failed.

`SUMMARY: WARN` exits with code `0`.

## Runner command

```bash
python3 scripts/test-policy-flow-smoke.py
```
