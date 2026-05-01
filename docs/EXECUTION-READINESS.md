# Execution Readiness (Milestone 12.4.1)

## Purpose

This document defines Layer 2: Execution Readiness for Milestone 12.
It specifies how to decide whether an already activated task is ready to start execution checks in future milestones.

Execution readiness is a gate, not execution.

## Layer Separation

- `validate-active-task.py` = Layer 1 (Active Task Integrity)
- `check-execution-readiness.py` = Layer 2 (Execution Readiness)

Required dependency:
- Readiness checker depends on successful active task validation.
- If active task validation is `FAIL` or `PARTIAL`, readiness must be `FAIL`.
- `PARTIAL` active task validation must never be treated as execution-ready.

## Core Definition

Execution readiness checks whether active task can be started from state, approval, consistency, and safety boundary perspective.

Execution readiness is NOT:
- task execution
- agent run
- task state mutation
- completion/failure/drop action
- queue movement

Formula:
- `valid active-task.md` is not equal to `execution-ready task`.

## Required Readiness Checks

### Check 1 (Prerequisite Gate)

1. active task validation passed

Rule:
- If check 1 fails, readiness fails immediately.
- Checks 2–17 must not run when check 1 fails.

### Checks 2–17 (Run only after Check 1 PASS)

2. source_task exists and is still consistent  
3. source_contract exists and is still consistent  
4. approval marker is resolvable  
5. approval marker is valid  
6. approval marker is not expired  
7. approval marker is not revoked  
8. approval marker task_id matches active.task_id  
9. approval marker scope matches `activate_task`  
10. approval marker transition matches `approved_for_execution:active`  
11. detected task state is active-compatible  
12. `validate-task-state.py` passes  
13. analysis_status is not invalid  
14. analysis_status is not conflict  
15. active task validation result is exactly PASS, not PARTIAL  
16. source_task has not changed since activation (if hash/timestamp available)  
17. source_contract has not changed since activation (if hash/timestamp available)

Checks 16–17 availability rule:
- if change detection mechanism is unavailable, record:
  - `source_task change detection: NOT AVAILABLE`
  - `source_contract change detection: NOT AVAILABLE`
- this is a declared limitation, not auto-FAIL by itself.

Implementation note for future checker:
- Use existing validators through `subprocess` where possible:
  - `scripts/validate-active-task.py`
  - `scripts/detect-task-state.py`
  - `scripts/validate-task-state.py`
  - `scripts/validate-approval-marker.py`
- Do not re-implement their logic.

## Approval Marker Readiness Rules

Readiness requires more than `approval_id` field presence.

Required:
- approval marker must be resolvable
- approval marker must be valid
- approval marker must match task_id
- approval marker must match scope
- approval marker must match transition
- approval marker must not be expired
- approval marker must not be revoked

Expected values:
- `scope: activate_task`
- `transition: approved_for_execution:active`

Rule:
- unresolved approval marker means NOT execution-ready.

## State Checks

Readiness checker must ensure state remains active-compatible.

Required:
- detected state must be active-compatible
- `validate-task-state.py` must pass

Examples of incompatible states:
- `failed`
- `completed`
- `dropped`
- `invalid`
- `conflict`

If repository state model differs, use current Milestone 10 state machine as source.

## analysis_status Checks

Primary source:
1. source_contract metadata

Fallback order:
2. detect-task-state output
3. task state file

If none provide analysis_status:
- `analysis_status check: NOT PRESENT`

Handling rule:
- not automatic FAIL unless current state model requires this field.
- if required by current state model and missing, readiness must FAIL.

Blocking values:
- `analysis_status: invalid` -> readiness FAIL
- `analysis_status: conflict` -> readiness FAIL

## Statuses and Exit Codes

| Status | Meaning | Exit code |
|---|---|---:|
| PASS | all required readiness checks passed | 0 |
| FAIL | one or more required checks failed | 1 |
| PARTIAL | required checks could not be fully completed | 1 |
| NOT RUN | readiness checker not executed | 2 |

Important:
- PARTIAL must not be treated as execution-ready.
- PARTIAL must return non-zero in future implementation.

## Allowed Reads

Future readiness checker may read:
- `tasks/active-task.md`
- `source_task` from active-task
- `source_contract` from active-task
- approval marker resolved from `approval_id`
- `docs/ACTIVE-TASK-VALIDATION.md`
- `docs/EXECUTION-READINESS.md`
- existing state/approval validator outputs

It may run read-only validators via `subprocess`:
- `scripts/validate-active-task.py`
- `scripts/detect-task-state.py`
- `scripts/validate-task-state.py`
- `scripts/validate-approval-marker.py`

If script names differ in future, implementation must document mismatch explicitly.

## Forbidden Writes

`check-execution-readiness.py` must be read-only.

It must not modify:
- `tasks/active-task.md`
- `tasks/queue/`
- `tasks/done/`
- `tasks/failed/`
- `tasks/dropped/`
- `reports/`
- `approvals/`
- git state

It also must not:
- create approval marker
- repair approval marker
- refresh approval marker
- rewrite active-task.md
- rewrite source_task
- rewrite source_contract
- generate verification report
- generate pre-execution evidence report

Pre-execution evidence report is a separate stage (12.8.1).

## What Readiness Checker Must NOT Do

`check-execution-readiness.py` must not:
- execute task
- run implementation agent
- call runner
- move task to done
- move task to failed
- move task to dropped
- start workflow execution
- mark task complete
- mark task failed
- perform rollback
- auto-fix invalid state
- auto-generate approval
- bypass human approval

## Future Negative Fixtures (12.6.1)

- `active-task-validation-fail`
- `active-task-validation-partial`
- `approval-marker-unresolved`
- `approval-marker-invalid`
- `approval-marker-expired`
- `approval-marker-revoked`
- `approval-task-id-mismatch`
- `approval-scope-mismatch`
- `approval-transition-mismatch`
- `detected-state-failed`
- `detected-state-completed`
- `detected-state-dropped`
- `detected-state-invalid`
- `detected-state-conflict`
- `validate-task-state-fail`
- `analysis-status-invalid`
- `analysis-status-conflict`
- `source-task-changed-after-activation`
- `source-contract-changed-after-activation`
- `missing-state-validator`
- `missing-approval-validator`

Conditional rule:
- `source-task-changed-after-activation` and `source-contract-changed-after-activation` are conditional on change detection availability.
- If change detection is unavailable at 12.6.1, mark these cases as `SKIPPED` with explicit rationale.

## Safety Boundaries

- Execution readiness is not execution.
- Execution readiness does not grant permission to bypass human approval.
- Execution readiness does not mutate task state.
- Execution readiness does not move queue/done/failed.
- Execution readiness does not produce completion proof.
- Execution readiness is only a precondition for a future controlled execution runner.
- PASS means ready-to-start, not done.
- PARTIAL is not ready-to-start.

## Non-goals (12.4.1)

This stage does not add:
- `check-execution-readiness.py`
- readiness negative fixtures
- CLI integration
- pre-execution evidence report
- runner
- task execution
- queue movement
- auto-completion
- auto-failure
- rollback
- approval marker generation
- approval marker repair
- state mutation
