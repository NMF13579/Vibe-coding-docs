# Negative Fixture - blocked-but-execution-true

## Category

review

## Purpose

Verify that validator rejects a Review where status is BLOCKED but execution_allowed is true.

## Expected Tool

future review validator / guard test runner

## Expected Result

FAIL - BLOCKED status requires execution_allowed: false

## Notes

Payload file: REVIEW.md (added in Task 7.1.2)

## Manual Verification

Command: future review validator / guard test runner

Expected: FAIL

Reason: review_status BLOCKED conflicts with execution_allowed true
