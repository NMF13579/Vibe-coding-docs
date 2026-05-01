# Negative Fixture - status-not-approved

## Category

task-brief

## Purpose

Verify that validator rejects a Task Brief with status other than APPROVED.

## Expected Tool

scripts/validate-task-brief.py

## Expected Result

FAIL - status must be APPROVED

## Notes

Payload file: TASK.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/validate-task-brief.py tests/fixtures/negative/task-brief/status-not-approved/TASK.md

Expected: FAIL

Reason: metadata.status is not APPROVED
