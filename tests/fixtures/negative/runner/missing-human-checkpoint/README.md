# Negative Fixture - missing-human-checkpoint

## Category

runner

## Purpose

Verify that runner guard rejects a flow that skips human approval checkpoint.

## Expected Tool

future runner guard test

## Expected Result

FAIL - human checkpoint is required before start and completion

## Notes

Payload file: scenario.md (added in Task 7.1.2)

## Manual Verification

Command: future runner guard test

Expected: FAIL

Reason: runner flow bypasses required human approval
