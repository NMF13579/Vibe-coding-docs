# Negative Fixture - approved-mode-requested

## Category

runner

## Purpose

Verify that runner guard rejects execution in approved mode (not yet available).

## Expected Tool

future runner guard test

## Expected Result

FAIL - approved mode is reserved for a future milestone

## Notes

Payload file: scenario.md (added in Task 7.1.2)

## Manual Verification

Command: future runner guard test

Expected: FAIL

Reason: approved mode is reserved and must not execute
