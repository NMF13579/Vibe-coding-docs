# Task Transition Rules

## Purpose

This document defines transition rules for the AgentOS task state model.
Milestone 10 checks transitions only.
Milestone 10 does not execute transitions.
A PASS transition check means "allowed in dry-run", not "transition executed".
Human approval remains required for state-changing actions.

## Relationship to Existing Scripts

`detect-task-state.py`:
- detects current state and evidence
- does not validate requested transition
- does not execute transition

`validate-task-state.py`:
- validates current state consistency
- does not validate requested target transition
- does not execute transition

`check-transition.py`:
- planned in Milestone 10.6.1
- will validate requested transition in dry-run
- must not execute transition

## Allowed Transitions

### idea -> brief_draft
Meaning:
- A task brief draft becomes visible from an idea.
Required current state:
- idea
Required evidence:
- TASK.md draft exists or task brief draft exists
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- no
Script allowed to execute transition:
- no
Notes:
- This is a draft-only progression and does not change execution state.

### brief_draft -> brief_approved
Meaning:
- The task brief draft has been approved.
Required current state:
- brief_draft
Required evidence:
- TASK.md exists
- TASK.md status/approval indicates approved
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Approval is evidence, not execution.

### brief_approved -> review_ready
Meaning:
- The approved brief is ready for review-based progression.
Required current state:
- brief_approved
Required evidence:
- TASK.md approved
- REVIEW.md exists
- review_status: READY or READY_WITH_EDITS
- execution_allowed: true
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- no
Script allowed to execute transition:
- no
Notes:
- READY_WITH_EDITS is treated as ready when execution is allowed.

### brief_approved -> review_blocked
Meaning:
- The approved brief is blocked by review feedback.
Required current state:
- brief_approved
Required evidence:
- TASK.md exists
- REVIEW.md exists
- review_status is one of NEEDS_CLARIFICATION, TOO_BROAD, TOO_SMALL, DUPLICATE, BLOCKED
- execution_allowed is false or absent
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- no
Script allowed to execute transition:
- no
Notes:
- Blocked review is still non-executing evidence.

### review_blocked -> brief_draft
Meaning:
- A blocked review returns the task to draft work.
Required current state:
- review_blocked
Required evidence:
- REVIEW.md blocked status exists
- updated TASK.md or brief draft exists
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
- `scripts/check-transition.py` # planned in 10.6.1
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- The planned transition checker is not created in this milestone.

### review_ready -> trace_written
Meaning:
- Ready review evidence is followed by trace evidence.
Required current state:
- review_ready
Required evidence:
- REVIEW.md ready status
- execution_allowed: true
- TRACE.md exists and is non-empty
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- no
Script allowed to execute transition:
- no
Notes:
- This is still read-only validation territory.

### trace_written -> contract_drafted
Meaning:
- A valid trace is followed by a contract draft.
Required current state:
- trace_written
Required evidence:
- TRACE.md valid
- `tasks/drafts/{task-id}-contract-draft.md` exists and is non-empty
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- no
Script allowed to execute transition:
- no
Notes:
- The draft is evidence for the next controlled step, not execution.

### contract_drafted -> approved_for_execution
Meaning:
- The drafted contract is approved for controlled execution.
Required current state:
- contract_drafted
Required evidence:
- contract draft valid
- approval marker exists
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Approval marker is evidence only.

### approved_for_execution -> active
Meaning:
- The approved contract becomes the active task.
Required current state:
- approved_for_execution
Required evidence:
- approval marker valid
- contract draft valid
- active-task.md replacement is allowed only in future Milestone 11 approved mode
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Milestone 10 does not replace `tasks/active-task.md`.

### active -> completed
Meaning:
- The active task finishes successfully.
Required current state:
- active
Required evidence:
- active-task.md references task
- completion evidence exists
- verification result supports completion
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Completion requires supporting verification evidence.

### active -> failed
Meaning:
- The active task fails and is recorded as failed.
Required current state:
- active
Required evidence:
- active-task.md references task
- failure evidence exists
- failure reason documented
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Failure is a controlled state change, not an automatic result.

### active -> dropped
Meaning:
- The active task is intentionally dropped.
Required current state:
- active
Required evidence:
- active-task.md references task
- drop reason documented
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Dropping a task is a deliberate human decision.

### failed -> brief_draft
Meaning:
- A failed task returns to draft work after review.
Required current state:
- failed
Required evidence:
- failed evidence exists
- failure reason reviewed
- updated TASK.md or brief draft exists
Required validators:
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
Human approval required:
- yes
Script allowed to execute transition:
- no
Notes:
- Recovery from failure is human-directed.

## state_conflict Transition Rules

- `state_conflict` is not a manual transition target.
- It is set only by `scripts/detect-task-state.py` when conflicting evidence exists.
- No manual transition to `state_conflict` is allowed.
- No transition from `state_conflict` is allowed until conflicting evidence is manually resolved.
- After conflict resolution, the detector must return a non-conflict state.
- Human approval is required before any state-changing action following conflict resolution.
- `state_conflict -> any state` is forbidden without manual resolution and human approval.
- `any state -> state_conflict` is not a manual transition; the detector sets it only on conflicting evidence.

## Forbidden Transitions

Forbidden transition examples:

- `idea -> active`
- `brief_draft -> active`
- `brief_approved -> contract_drafted`
- `brief_approved -> active`
- `review_ready -> active`
- `trace_written -> active`
- `contract_drafted -> active` without approval marker
- `completed -> active`
- `dropped -> active`
- `completed -> dropped`
- `dropped -> completed`
- `state_conflict -> any state` without manual resolution and human approval
- `any state -> state_conflict` as a manual transition

## Human Approval Rules

- Human approval is required before state-changing actions.
- Approval marker is evidence only.
- Approval marker does not execute a transition.
- Approval marker does not replace human review.
- Milestone 10 does not create approval markers.
- Milestone 10 does not consume approval markers to modify files.
- Milestone 10 does not replace `tasks/active-task.md`.
- Milestone 10 does not move queue entries.

## Dry-run Semantics

PASS means:
- requested transition is allowed by rules
- required evidence appears to exist
- state is consistent enough for dry-run approval

PASS does NOT mean:
- transition was executed
- files were modified
- approval was granted
- `tasks/active-task.md` was replaced
- queue entry was moved
- task was completed

## Safety Boundaries

- Milestone 10 checks transitions only.
- Milestone 10 does not execute transitions.
- A PASS transition check means allowed in dry-run, not transition executed.
- `scripts/check-transition.py` is planned and not created in this milestone.
- Transition scripts do not create approval markers.
- Transition scripts do not replace `tasks/active-task.md`.
- Transition scripts do not move queue entries.
- Transition scripts do not create `tasks/failed/`.
- Transition scripts do not create `tasks/dropped/`.
- Transition scripts do not create `tasks/done/`.

## Out of Scope for Milestone 10.5.1

Milestone 10.5.1 does not add:

- automatic transitions
- automatic execution
- automatic approval
- approval marker generation
- `tasks/active-task.md` replacement
- queue movement
- `scripts/check-transition.py`
- fixtures
- CLI integration
- `promote-contract.py` approved mode
- `queue-transition.py` approved mode
- execution approval
- release approval
- installable CLI
- `pyproject.toml`
- backend
- RAG
- vector DB
- web UI
