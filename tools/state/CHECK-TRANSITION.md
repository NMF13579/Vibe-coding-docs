# Check Transition

## Purpose

`scripts/check-transition.py` is a dry-run transition checker for AgentOS tasks.
It answers one question: can a requested transition be allowed by the current rules without changing any files?
It consumes Task State Report v1.1.

## Outputs

The checker prints a human-readable report:

- current state
- requested target state
- PASS or FAIL
- reasons when the transition is not allowed
- `Transition executed: no` in every case

PASS means dry-run allowed only.

## Relationship with `detect-task-state.py`

The checker calls `scripts/detect-task-state.py` through subprocess to read the current state report.
It reads:

- `analysis_status`
- structured evidence objects, not plain strings
- `allowed_next_states`

The checker rejects:

- `analysis_status: conflict`
- `analysis_status: invalid`
- `state == "state_conflict"` as a deprecated report value
- target `state_conflict`

## Relationship with `validate-task-state.py`

The checker does not rely on transition approval from the validator.
Only `analysis_status = ok` is eligible for transition checks.
If current analysis is invalid or conflicting, the dry-run fails immediately.

## Allowed Transitions

The checker accepts these dry-run transitions:

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

## Forbidden Transitions

Examples of forbidden transitions:

- `brief_approved -> contract_drafted`
- `brief_approved -> active`
- `review_ready -> active`
- `trace_written -> active`
- `contract_drafted -> active` without a valid approval marker
- `any state -> state_conflict`

## Required Evidence

The checker expects evidence that matches the requested transition. Missing evidence fails the dry-run.

- `idea -> brief_draft`
  - task brief draft exists, or `TASK.md` draft exists
- `brief_draft -> brief_approved`
  - `TASK.md` exists and is approved
- `brief_approved -> review_ready`
  - `REVIEW.md` exists
  - `review_status` is `READY` or `READY_WITH_EDITS`
  - `execution_allowed: true`
- `brief_approved -> review_blocked`
  - `REVIEW.md` exists
  - `review_status` is one of `NEEDS_CLARIFICATION`, `TOO_BROAD`, `TOO_SMALL`, `DUPLICATE`, `BLOCKED`
- `review_blocked -> brief_draft`
  - blocked review evidence exists
  - updated `TASK.md` or a brief draft exists
- `review_ready -> trace_written`
  - `TRACE.md` exists and is non-empty
- `trace_written -> contract_drafted`
  - `tasks/drafts/{task-id}-contract-draft.md` exists and is non-empty
- `contract_drafted -> approved_for_execution`
  - valid CONTRACT evidence exists
  - APPROVAL evidence exists
- `approved_for_execution -> active`
  - valid CONTRACT evidence exists
  - APPROVAL evidence exists
  - `active-task.md` replacement is out of scope for Milestone 10
- `active -> completed`
  - completion evidence exists
  - `tasks/active-task.md` references the task
- `active -> failed`
  - failure evidence exists
  - `tasks/active-task.md` references the task
- `active -> dropped`
  - drop evidence exists
  - `tasks/active-task.md` references the task
- `failed -> brief_draft`
  - failure evidence exists
  - updated `TASK.md` or a brief draft exists

## Dry-run Semantics

The checker only reports whether a transition is eligible in dry-run mode.
It does not execute the transition.
It does not modify files.
It does not grant approval.
It always prints `Transition executed: no`.

## Read-only Guarantee

The checker only reads the detector report and task files needed for evidence checks.
It does not write to the repository.

## Safety Boundaries

`scripts/check-transition.py` does not:

- execute transitions
- modify task files
- create approval markers
- replace `tasks/active-task.md`
- move queue entries
- create `tasks/failed/`
- create `tasks/dropped/`
- create `tasks/done/`
- modify detector output
- grant execution authority
- grant approval

