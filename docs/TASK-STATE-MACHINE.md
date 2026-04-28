# Task State Machine

## Purpose

This document defines the task state model for AgentOS.
Markdown remains the source of truth.
Milestone 10 adds state awareness only.
It documents allowed states, evidence used to infer state, allowed transitions, forbidden transitions, and human approval requirements.
Milestone 10 does not execute transitions.

## Evidence Model

State inference uses evidence from:

- `TASK.md`
- `TASK.md` status / approval
- `REVIEW.md`
- `REVIEW.md.review_status`
- `REVIEW.md.execution_allowed`
- `TRACE.md`
- `tasks/drafts/{task-id}-contract-draft.md`
- approval marker
- `tasks/active-task.md` reference
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`

`tasks/failed/` may not yet exist in the repository.
If it is missing, document it as a planned evidence path.
The directory is the intended future location for failed tasks.
Do not create the directory.
Do not treat its absence as an error.
The `failed` state is still part of the model even if `tasks/failed/` does not yet exist.

## State Model

### idea

Meaning:
- The task exists only as an idea.
- No approved task brief exists yet.

Required evidence:
- `TASK.md` is missing.

Missing evidence means:
- If `TASK.md` appears, the task is no longer in `idea`.

Allowed next states:
- `brief_draft`

Forbidden transitions:
- `idea -> active`
- `idea -> completed`
- `idea -> failed`
- `idea -> dropped`

Human approval required:
- no

### brief_draft

Meaning:
- A `TASK.md` exists, but it is not yet approved.
- The task brief is still being prepared.

Required evidence:
- `TASK.md` exists.
- `TASK.md` is not approved.

Missing evidence means:
- If `TASK.md` is missing, the task falls back to `idea`.
- If `TASK.md` becomes approved, the task moves to `brief_approved`.

Allowed next states:
- `brief_approved`

Forbidden transitions:
- `brief_draft -> active`
- `brief_draft -> completed`
- `brief_draft -> failed`
- `brief_draft -> dropped`

Human approval required:
- no

### brief_approved

Meaning:
- `TASK.md` exists and is approved.
- The brief is ready for review work.

Required evidence:
- `TASK.md` exists.
- `TASK.md` is approved.

Missing evidence means:
- If approval is removed or no longer valid, the task returns to `brief_draft`.

Allowed next states:
- `review_ready`
- `review_blocked`

Forbidden transitions:
- `brief_approved -> contract_drafted`
- `brief_approved -> active`
- `brief_approved -> completed`
- `brief_approved -> failed`
- `brief_approved -> dropped`

Human approval required:
- yes

### review_ready

Meaning:
- `REVIEW.md` shows a review state that allows execution preparation.
- `REVIEW.md.review_status` is `READY` or `READY_WITH_EDITS`.
- `REVIEW.md.execution_allowed` is `true`.
- `READY_WITH_EDITS` is explicitly equivalent to `READY` for this state.

Required evidence:
- `REVIEW.md` exists.
- `review_status` is `READY` or `READY_WITH_EDITS`.
- `execution_allowed: true`.

Missing evidence means:
- If review is blocked, the task moves to `review_blocked`.
- If `execution_allowed` is not true, the task is not `review_ready`.

Allowed next states:
- `trace_written`

Forbidden transitions:
- `review_ready -> active`
- `review_ready -> contract_drafted`
- `review_ready -> completed`
- `review_ready -> failed`
- `review_ready -> dropped`

Human approval required:
- yes

### review_blocked

Meaning:
- Review exists, but execution is not allowed yet.
- The task cannot move forward until the review is updated.

Required evidence:
- `REVIEW.md` exists.
- `review_status` is blocked or not ready.
- `execution_allowed` is `false` or missing.

Missing evidence means:
- If review becomes ready with `execution_allowed: true`, the task moves to `review_ready`.

Allowed next states:
- `brief_draft`

Forbidden transitions:
- `review_blocked -> active`
- `review_blocked -> trace_written`
- `review_blocked -> contract_drafted`
- `review_blocked -> completed`
- `review_blocked -> failed`
- `review_blocked -> dropped`

Human approval required:
- no

### trace_written

Meaning:
- `TRACE.md` exists and is valid.
- The task has a trace evidence file.

Required evidence:
- `TRACE.md` exists.
- `TRACE.md` is valid.

Missing evidence means:
- If `TRACE.md` is missing or invalid, the task is not `trace_written`.

Allowed next states:
- `contract_drafted`

Forbidden transitions:
- `trace_written -> active`
- `trace_written -> completed`
- `trace_written -> failed`
- `trace_written -> dropped`

Human approval required:
- no

### contract_drafted

Meaning:
- A draft contract exists at `tasks/drafts/{task-id}-contract-draft.md`.
- The draft is valid and ready for controlled approval review.

Required evidence:
- `tasks/drafts/{task-id}-contract-draft.md` exists.
- The draft is valid.
- `TRACE.md` is valid.

Missing evidence means:
- If the draft is missing, the task returns to `trace_written`.
- If the draft is invalid, the task is not `contract_drafted`.

Allowed next states:
- `approved_for_execution`

Forbidden transitions:
- `contract_drafted -> active`
- `contract_drafted -> completed`
- `contract_drafted -> failed`
- `contract_drafted -> dropped`

Human approval required:
- yes

### approved_for_execution

Meaning:
- A valid approval marker exists for the drafted contract.
- The task is approved for controlled execution.

Required evidence:
- approval marker exists.
- contract draft exists.
- contract draft is valid.

Missing evidence means:
- If the approval marker is missing, the task returns to `contract_drafted`.

Allowed next states:
- `active`

Forbidden transitions:
- `approved_for_execution -> completed`
- `approved_for_execution -> failed`
- `approved_for_execution -> dropped`

Human approval required:
- yes

### active

Meaning:
- `tasks/active-task.md` references the task.
- The task is the current executable task.

Required evidence:
- `tasks/active-task.md` references the task.
- An approval marker exists.
- The task is the current active contract.

Missing evidence means:
- If `tasks/active-task.md` no longer references the task, the task is not `active`.
- If the approval marker is removed, the task is no longer supported for execution.

Allowed next states:
- `completed`
- `failed`
- `dropped`

Forbidden transitions:
- `active -> brief_draft`
- `active -> brief_approved`
- `active -> review_ready`
- `active -> trace_written`
- `active -> contract_drafted`

Human approval required:
- yes

### completed

Meaning:
- The task finished successfully.
- The task exists in `tasks/done/`.

Required evidence:
- task exists in `tasks/done/`.

Missing evidence means:
- If the task is removed from `tasks/done/`, completion evidence is missing.

Allowed next states:
- none

Forbidden transitions:
- `completed -> active`
- `completed -> dropped`
- `completed -> failed`
- `completed -> brief_draft`

Human approval required:
- no

### failed

Meaning:
- The task failed during execution or was marked failed after execution.
- The task exists in `tasks/failed/` when that directory is present.
- If `tasks/failed/` does not exist, the state remains documented and the path is treated as planned evidence.

Required evidence:
- task exists in `tasks/failed/` if the directory exists.
- If `tasks/failed/` does not exist, this state is still part of the model and the path is treated as planned evidence.

Missing evidence means:
- If the task is not present in `tasks/failed/`, the failed state is not confirmed.

Allowed next states:
- `brief_draft`

Forbidden transitions:
- `failed -> active`
- `failed -> completed`
- `failed -> dropped`

Human approval required:
- yes

### dropped

Meaning:
- The task was intentionally stopped and moved to `tasks/dropped/`.

Required evidence:
- task exists in `tasks/dropped/`.

Missing evidence means:
- If the task is not present in `tasks/dropped/`, the dropped state is not confirmed.

Allowed next states:
- none

Forbidden transitions:
- `dropped -> active`
- `dropped -> completed`
- `dropped -> failed`
- `dropped -> brief_draft`

Human approval required:
- yes

### state_conflict

Meaning:
- Conflicting evidence exists.
- The task cannot be assigned a stable state until the conflict is resolved.

Required evidence:
- Conflicting evidence across task files.

Missing evidence means:
- If there is no conflict, the task should remain in its best matching state.

Allowed next states:
- none until resolved

Forbidden transitions:
- `state_conflict -> any state` without manual resolution and human approval

Human approval required:
- yes

state_conflict is set only by the detector - it is not a manual transition target.

No transition TO state_conflict is allowed manually.

No transition FROM state_conflict is allowed without:

- manual human review
- explicit resolution of conflicting evidence
- human approval

`state_conflict -> any state` is forbidden without manual resolution and human approval.

`any state -> state_conflict` is not a manual transition.
It is set only by the detector when conflicting evidence is found.

## Allowed Transitions

- `idea -> brief_draft`
- `brief_draft -> brief_approved`
- `brief_approved -> review_ready`
- `brief_approved -> review_blocked`
- `review_blocked -> brief_draft`
- `review_ready -> trace_written`
- `trace_written -> contract_drafted`
- `contract_drafted -> approved_for_execution`
- `approved_for_execution -> active`
- `active -> completed`
- `active -> failed`
- `active -> dropped`
- `failed -> brief_draft`

## Forbidden Transition Examples

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

## Human Approval Rules

- Human approval is required before any state-changing action.
- Milestone 10 only checks state and transition validity.
- Milestone 10 does not execute state-changing actions.
- Approval marker is evidence for future controlled transition.
- Approval marker does not itself modify files.
- Approval marker does not replace human review.

## Safety Boundaries

- `TRACE.md` does not grant execution authority.
- `REVIEW.md` does not grant execution authority.
- Contract draft does not grant execution authority.
- Approval marker is evidence only.
- Approval marker does not execute transition.
- Milestone 10 does not create approval markers.
- Milestone 10 does not replace `tasks/active-task.md`.
- Milestone 10 does not move queue entries.
- Milestone 10 does not execute transitions.

## Out of Scope for Milestone 10

Milestone 10 does not add:

- automatic transitions
- automatic execution
- automatic approval
- approval marker generation
- `tasks/active-task.md` replacement
- queue movement
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

## Relationship to Milestone 11

- Milestone 10 creates state awareness.
- Milestone 10 checks whether transitions are allowed.
- Milestone 10 does not execute transitions.
- Milestone 11 may introduce safe semi-automation only if:
  - current state is valid
  - requested transition is allowed
  - required evidence exists
  - dry-run check passes
  - explicit human approval marker exists
  - human explicitly requested approved mode
