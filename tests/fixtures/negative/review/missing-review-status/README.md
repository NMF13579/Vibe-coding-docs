# Negative Fixture - missing-review-status

## Category

review

## Purpose

Verify that validator rejects a Review with no review_status field.

## Expected Tool

future review validator / guard test runner

## Expected Result

FAIL - review_status is required

## Notes

Payload file: REVIEW.md (added in Task 7.1.2)

## Manual Verification

Command: future review validator / guard test runner

Expected: FAIL

Reason: REVIEW.md has no review_status
