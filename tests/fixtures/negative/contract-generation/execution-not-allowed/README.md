# Negative Fixture - execution-not-allowed

## Category

contract-generation

## Purpose

Verify that contract generator rejects input when execution_allowed is false, even if review_status is READY.

## Expected Tool

scripts/generate-task-contract.py

## Expected Result

FAIL - execution_allowed must be true

## Notes

Payload files: task-example/TASK.md and task-example/REVIEW.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/generate-task-contract.py tests/fixtures/negative/contract-generation/execution-not-allowed/task-example

Expected: FAIL

Reason: execution_allowed is false
