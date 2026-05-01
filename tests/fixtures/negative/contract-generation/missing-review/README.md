# Negative Fixture - missing-review

## Category

contract-generation

## Purpose

Verify that contract generator rejects input when REVIEW.md is absent.

## Expected Tool

scripts/generate-task-contract.py

## Expected Result

FAIL - REVIEW.md is required before contract generation

## Notes

Payload file: task-example/TASK.md (added in Task 7.1.2). REVIEW.md intentionally absent.

## Manual Verification

Command: python3 scripts/generate-task-contract.py tests/fixtures/negative/contract-generation/missing-review/task-example

Expected: FAIL

Reason: REVIEW.md is missing from task-example/
