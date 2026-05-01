# Test Approval Marker Fixtures

## Purpose

`test-approval-marker-fixtures.py` runs negative approval marker cases against `scripts/validate-approval-marker.py`.
Invalid approval marker rejected -> fixture PASS.
Invalid approval marker accepted -> fixture FAIL.
This runner does not create production approval markers.
This runner does not execute transitions.
This runner does not modify production task files.

## Command

```text
python3 scripts/test-approval-marker-fixtures.py
```

## Fixture Directory

```text
tests/fixtures/negative/approval-markers/
```

## Fixture Format

Each fixture directory contains:
- `fixture.json`
- `approval.md`
- optional supporting files such as a dummy contract draft

The runner may replace `__FIXTURE_DIR__` in copied fixture files with the temporary workspace path.

## Required Cases

- missing-required-field
- wrong-task-id
- wrong-scope
- revoked-marker
- expired-marker
- superseded-marker
- missing-related-contract
- duplicate-approved-markers
- malformed-approved-at
- invalid-transition-scope

## Expected Rejection Is PASS

The suite is negative-only.
A validator failure is the expected outcome.
If the validator rejects the marker as intended, the fixture passes.
If the validator accepts an invalid marker, the fixture fails.

## Isolation Rules

- each fixture runs in its own temporary workspace
- the runner uses `tempfile`
- the runner uses `subprocess` to call `scripts/validate-approval-marker.py`
- the runner does not modify production files
- the runner does not create production `approvals/`
- the runner does not modify production `tasks/`
- the runner deletes temporary workspaces automatically

## Output

The runner prints a short human-readable summary for each fixture and a final result line.

## Exit Codes

- `0` - all expected rejections happened
- `1` - at least one invalid marker was accepted, or a fixture failed unexpectedly
- `2` - usage error: fixture directory missing, `fixture.json` unreadable, or `scripts/validate-approval-marker.py` not found

## Safety Boundaries

- does not execute transitions
- does not create production approval markers
- does not create or modify production `approvals/`
- does not modify production task files
- does not replace `active-task.md`
- does not move queue entries
- does not grant approval
- does not enable approved mode

## Known Limitations

- Reason matching, if implemented, should remain warning-level rather than brittle exact matching.
- The duplicate-marker scan is best-effort and may stop at a reasonable file-count threshold.
- The runner relies on the approval marker validator's current marker-scope mapping.

## Out of Scope

Milestone 10.16 does not add:
- approval marker schema
- approval marker generation
- automatic approval
- automatic transition execution
- approved mode
- `active-task.md` replacement
- queue movement
- completion automation
- failure automation
- drop automation
- release approval
- backend
- RAG
- vector DB
- web UI
