# Negative Fixture - draft-already-exists

## Category

contract-generation

## Purpose

Verify that contract generator does not overwrite an existing draft file.

## Expected Tool

scripts/generate-task-contract.py

## Expected Result

FAIL - draft already exists, must not overwrite

## Notes

Payload files: task-example/TASK.md, task-example/REVIEW.md, drafts/task-example-contract-draft.md (added in Task 7.1.2)

## Manual Verification

Command: python3 scripts/generate-task-contract.py tests/fixtures/negative/contract-generation/draft-already-exists/task-example

Expected: FAIL

Reason: draft already exists and must not be overwritten
