# Negative Fixture Runner Smoke Test

## Command

python3 scripts/test-negative-fixtures.py

## Expected Result

PASS

## Actual Result

PASS

## Exit Code

0

## Automated Coverage

- task-brief: 4
- contract-generation: 4
- template-integrity: 3

## Skipped Coverage

- review: future validator
- trace: future validator
- queue: future validator
- runner: future guard test

## Output Summary

The negative fixture runner reported PASS for all runnable checks:

- Task Brief: missing-metadata, executable-true, missing-acceptance-criteria, status-not-approved
- Contract Generation: missing-review, review-not-ready, execution-not-allowed, draft-already-exists
- Template Integrity: missing-core-file, forbidden-auto-runner, missing-gitignore-drafts

Skipped groups were reported for review, trace, queue, and runner because future validators or guard tests are not implemented yet.

## Failure Details

No failures.

## Safety Notes

- Runner scripts were not executed directly.
- tasks/active-task.md was not modified intentionally.
- Queue items were not moved.
- root-level tasks/drafts/ protection was checked by the negative fixture runner.
- No review/trace/queue/runner validators were created.
