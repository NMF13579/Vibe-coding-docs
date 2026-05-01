# Negative Fixture - missing-acceptance-criteria

## Category

task-brief

## Purpose

Verify that validator rejects a Task Brief with no Acceptance Criteria section.

## Expected Tool

scripts/validate-task-brief.py

## Expected Result

FAIL - missing Acceptance Criteria section

## Notes

Payload file: TASK.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/validate-task-brief.py tests/fixtures/negative/task-brief/missing-acceptance-criteria/TASK.md

Expected: FAIL

Reason: TASK.md has no Acceptance Criteria section
