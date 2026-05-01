# Negative Fixture - attempts-active-task-replace

## Category

runner

## Purpose

Verify that runner guard rejects automatic replacement of tasks/active-task.md.

## Expected Tool

future runner guard test

## Expected Result

FAIL - active-task.md must not be replaced without explicit human approval

## Notes

Payload file: scenario.md (added in Task 7.1.2)

## Manual Verification

Command: future runner guard test

Expected: FAIL

Reason: runner attempts to replace tasks/active-task.md automatically
