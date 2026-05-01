# Negative Fixture - executable-true

## Category

task-brief

## Purpose

Verify that validator rejects a Task Brief with executable: true.

## Expected Tool

scripts/validate-task-brief.py

## Expected Result

FAIL - executable must be false in Task Brief

## Notes

Payload file: TASK.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/validate-task-brief.py tests/fixtures/negative/task-brief/executable-true/TASK.md

Expected: FAIL

Reason: metadata.executable is true
