# Safe Transition Execution (Milestone 11 MVP)

## 1. Purpose

AgentOS is moving from read-only validation to one narrow controlled write.
This document defines the safety rules for executable task-state transitions.

Milestone formula:
- Milestone 10 checks.
- Milestone 11 executes only narrow approved transitions.

Safety boundary:
- Safe transition execution is not autonomous execution.
- Safe transition execution is not agent runner execution.
- Safe transition execution is not task completion.
- Safe transition execution is not approval generation.

## 2. Definition: Safe Transition

Safe transition is a task-state transition that is:
- explicitly requested by a human
- allowed by the task state machine
- validated by deterministic scripts
- backed by a valid approval marker
- executed only in explicit approved mode
- limited to a known file write
- auditable after execution
- reversible manually

## 3. MVP Allowed Transition

In Milestone 11, only one executable transition is allowed:
- `approved_for_execution -> active`

All other transitions are forbidden for execution in M11.

| From | To | Execution allowed? | Notes |
|---|---|---:|---|
| approved_for_execution | active | yes | MVP only |
| idea | brief_draft | no | documentation/check only |
| brief_approved | review_ready | no | not executable in M11 |
| active | completed | no | forbidden in M11 |
| active | failed | no | forbidden in M11 |
| any | dropped | no | forbidden in M11 |

## 4. Required Checks Before Execution

Before any write, all checks below must pass in order:
1. requested task path exists
2. approval marker path exists
3. `detect-task-state.py` succeeds
4. `validate-task-state.py` succeeds
5. `check-transition.py --to active` succeeds
6. `validate-approval-marker.py` succeeds
7. approval marker `task_id` matches requested task
8. approval marker scope matches activation
9. approval marker transition matches `approved_for_execution:active`
10. approval marker is not expired
11. approval marker is not revoked
12. no `state_conflict`
13. no `analysis_status` invalid
14. no `analysis_status` conflict
15. source contract exists
16. target write is safe
17. explicit approved mode is present

Mode rule:
- `--approved` does not skip checks.
- `--approved` only unlocks the final write after all checks pass.

## 5. Explicit Approved Mode Requirement

Activation requires explicit human-approved mode.
Recommended flag:
- `--approved`

Required boundary:
- approval marker alone is not enough
- dry-run PASS alone is not enough
- human must explicitly pass approved mode

Forbidden approval models:
- implicit approval
- approval by file presence only
- approval by dry-run success only
- remembered approval
- global approval state
- environment-variable-only approval

## 6. Allowed Write Scope

In Milestone 11, write scope is limited to:
- `tasks/active-task.md`

This write is allowed only for transition:
- `approved_for_execution -> active`

## 7. Forbidden Writes

Milestone 11 must not write to:
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `approvals/`
- `reports/verification.md`
- `TASK.md`
- `REVIEW.md`
- `TRACE.md`
- contract drafts
- git state

## 8. Forbidden Behaviors

Milestone 11 must not introduce:
- automatic queue processing
- agent runner execution
- auto task execution
- auto approval marker generation
- auto completion
- auto failure marking
- auto dropping tasks
- release approval
- backend/service mode
- web UI
- RAG/vector DB
- multi-agent orchestration
- package installation

## 9. Failure Behavior

If any required check fails:
- do not write
- return FAIL
- explain the failed check
- preserve existing files
- do not partially update `active-task.md`

## 10. Auditability Requirements

After future activation, it must be possible to determine:
- which task was activated
- which approval marker authorized it
- which transition was requested
- when activation happened
- which source contract was used
- which command/mode performed the activation

## 11. Recovery Expectations

Milestone 11 does not define a rollback script.
Recovery is manual and will be documented later in:
- `docs/ACTIVATION-RECOVERY.md`

## 12. Non-goals

This document does not define:
- task execution
- task completion
- queue automation
- release approval
- autonomous agent behavior
