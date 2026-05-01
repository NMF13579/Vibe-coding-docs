# Negative Fixture - ready-but-execution-false

## Category

review

## Purpose

Verify that validator rejects a Review where status is READY but execution_allowed is false.

## Expected Tool

future review validator / guard test runner

## Expected Result

FAIL - READY status requires execution_allowed: true

## Notes

Payload file: REVIEW.md (added in Task 7.1.2)

## Manual Verification

Command: future review validator / guard test runner

Expected: FAIL

Reason: review_status READY conflicts with execution_allowed false
