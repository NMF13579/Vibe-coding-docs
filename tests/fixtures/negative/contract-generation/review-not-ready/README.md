# Negative Fixture - review-not-ready

## Category

contract-generation

## Purpose

Verify that contract generator rejects input when review_status is not READY or READY_WITH_EDITS.

## Expected Tool

scripts/generate-task-contract.py

## Expected Result

FAIL - review_status must be READY or READY_WITH_EDITS

## Notes

Payload files: task-example/TASK.md and task-example/REVIEW.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/generate-task-contract.py tests/fixtures/negative/contract-generation/review-not-ready/task-example

Expected: FAIL

Reason: review_status is not READY or READY_WITH_EDITS
