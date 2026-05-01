# Task Brief — Contract Generation Negative
## Metadata
    task_id: task-negative-contract-execution-not-allowed
    status: APPROVED
    created_at: 2026-04-26
    source: negative-fixture
    executable: false
## Context
This is a valid-looking Task Brief used to test contract generation guardrails.
## User Story
As a contract generator, I should respect review gate conditions.
## Expected Result
Contract generation should fail for this negative case.
## Acceptance Criteria
- Contract generation fails.
## Out of Scope
- Real execution.
## Dependencies
- REVIEW.md condition determines expected failure.
## Risks
- Bad review gate could allow invalid contract generation.
## Rollback / Reversal Notes
Delete this fixture.
## Notes
Negative fixture.
