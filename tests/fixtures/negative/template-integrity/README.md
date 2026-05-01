# Negative Fixtures - template-integrity

This category is reference-only.

## Category

template-integrity

## Purpose

Reference existing template integrity negative fixtures instead of duplicating them.

## Existing Fixtures

Template integrity negative fixtures already exist at:

- `tests/fixtures/template-integrity/missing-core-file/`
- `tests/fixtures/template-integrity/forbidden-auto-runner/`
- `tests/fixtures/template-integrity/missing-gitignore-drafts/`

## Expected Tool

scripts/check-template-integrity.py

## Expected Result

FAIL

## Notes

Do not duplicate those fixtures here. Use the paths above when referencing template integrity negative cases.

## Manual Verification

Command:

    python3 scripts/check-template-integrity.py --root tests/fixtures/template-integrity/missing-core-file
    python3 scripts/check-template-integrity.py --root tests/fixtures/template-integrity/forbidden-auto-runner
    python3 scripts/check-template-integrity.py --root tests/fixtures/template-integrity/missing-gitignore-drafts

Expected: FAIL

Reason: Existing template-integrity fixtures cover missing required files, forbidden auto-runner files, and missing tasks/drafts/ gitignore protection.
