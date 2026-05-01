# Controlled Execution Runner (Milestone 13)

## 1. Purpose

Controlled execution runner is a safety layer that allows execution of the active task only after a successful readiness gate.

Execution readiness PASS means ready-to-start, not completed.
Controlled execution runner starts execution, but does not complete the task automatically.

This document defines the operating boundaries of the runner for Milestone 13 (M13). It does not claim that task execution is autonomous.

## 2. Background

M11, M12, and M13 are connected as separate control layers:

- M11: Safe Active Task Selection
- M12: Active Task Governance + Execution Readiness Gate
- M13: Controlled Execution Runner

Required chain:

`tasks/active-task.md exists`
↓
`active task validation PASS`
↓
`execution readiness PASS`
↓
`controlled execution session may start`

## 3. Core Rule

The controlled execution runner MUST NOT allow execution steps unless execution readiness is PASS.

Readiness outcomes:

- FAIL blocks execution.
- PARTIAL blocks execution.
- NOT RUN blocks execution.
- PASS_WITH_LIMITATIONS may be recorded as a note, but readiness must still resolve to PASS.

A blocked execution attempt may be recorded for audit purposes, but no execution steps may run unless readiness is PASS.

## 4. What the Runner MAY Do

The runner may perform controlled execution support actions:

- call active task validation
- call execution readiness check
- create execution session / attempt metadata
- record blocked attempt evidence
- record execution start evidence
- read source_task and source_contract
- capture `tasks/active-task.md` as a read-only session snapshot
- guide the agent through an execution step protocol
- record changed files
- run verification commands from the task contract
- record verification evidence
- generate execution evidence reports

These actions support controlled execution and evidence collection. They are not autonomous lifecycle management.

## 5. What the Runner MUST NOT Do

The runner MUST NOT:

- allow execution steps before readiness PASS
- select the next task from queue
- replace `tasks/active-task.md`
- modify `tasks/active-task.md` in any way during or after execution session
- generate approval markers
- approve execution
- bypass readiness checks
- mark task as completed
- mark task as failed
- drop task
- move queue items
- perform rollback automatically
- modify approval records
- silently ignore failed verification
- claim PASS without executed evidence
- collapse different stop events into a single generic STOP record

Completion is a separate lifecycle transition and is out of scope for M13.
`tasks/active-task.md` is read-only during M13 execution session.

## 6. Execution Session Boundary

M13 works through an execution session / attempt record.

Term definitions used in this document:

- `source_contract` — file path referenced from `tasks/active-task.md`. It contains acceptance criteria and verification plan for the active task. The runner uses `source_contract` as the authoritative verification source and does not modify it.
- `execution session / attempt record` — evidence artifact for a controlled execution attempt. If readiness is not PASS, a record may still be created with blocked status to preserve the blocking reason. If readiness is PASS, the record may move into controlled execution status.
- `stop_reason` — required field for every STOP event in the execution session / attempt record. Allowed values:
  - `readiness_fail`
  - `scope_violation`
  - `watchdog_abort`
  - `manual_abort`

Execution session / attempt record binds:

- `session_id`
- `task_id`
- `active_task` (path to `tasks/active-task.md`)
- `active_task_snapshot` (read-only snapshot/captured metadata of active task at session start)
- `source_task` (path to source task file)
- `source_contract` (task contract with acceptance criteria and verification plan; read-only)
- `readiness_result` (result of readiness check)
- `started_at`
- `status` (see fixed values below)
- `stop_reason` (required for any STOP event; one of `readiness_fail | scope_violation | watchdog_abort | manual_abort`)
- `changed_files`
- `verification_evidence`

Additional rules:

- Runner captures `tasks/active-task.md` as a read-only session snapshot at session start.
- Validation and readiness checks may read `tasks/active-task.md`.
- No M13 component may modify `tasks/active-task.md` during or after the execution session.
- Any status update to active task is out of scope for M13.

Status values (mandatory and exclusive in this document):

- `blocked` — readiness is not PASS; execution steps are not allowed
- `in_progress` — readiness PASS; controlled execution is running
- `stopped` — session ended early; `stop_reason` is required
- `evidence_ready` — verification evidence is recorded; session ended without completion transition

The document MUST use only these four status values when describing flow.
It MUST NOT introduce additional status values.
Concrete implementation details will be specified in `docs/EXECUTION-SESSION.md`.

## 7. Execution Start vs Execution Completion

Execution start:

- readiness checked
- session / attempt record created
- execution steps may run only if readiness PASS
- task may be worked on inside controlled execution protocol

Execution blocked attempt:

- readiness checked
- session / attempt record may be created
- status: `blocked`
- stop_reason: `readiness_fail`
- no execution steps are allowed

Execution completion:

- implementation done
- verification evidence reviewed
- human or separate completion protocol decides final state

Controlled execution runner may create evidence that completion is possible, but it must not complete the task itself in M13.

## 8. Safety Boundaries

The following safety boundaries must remain in force:

- readiness gate is mandatory
- execution steps are allowed only after readiness PASS
- PARTIAL is not executable
- source_task and source_contract remain authoritative and read-only
- `tasks/active-task.md` remains read-only during and after M13 execution session
- scope must be checked during/after execution
- verification must be evidence-based
- no PASS without actually run checks
- no queue mutation
- no approval generation
- no rollback automation
- every STOP event MUST record a `stop_reason`
- different stop reasons MUST NOT be collapsed into a single generic record
- readiness failure may create a blocked attempt record, but must not start execution steps

## 9. Expected M13 Flow

1. User or agent invokes controlled runner.
2. Runner captures `tasks/active-task.md` as read-only session snapshot.
3. Runner validates active task.
4. Runner checks execution readiness.
5. Runner creates execution session / attempt record.
6. If readiness is not PASS:
   - set status: `blocked`
   - set stop_reason: `readiness_fail`
   - record readiness evidence
   - do not allow execution steps
   - STOP
7. If readiness is PASS:
   - set status: `in_progress`
   - continue controlled execution
8. Agent follows execution step protocol.
9. Runner records changed files.
10. Runner runs verification plan from `source_contract`.
11. Runner records execution evidence.
12. If session ends early:
   - set status: `stopped`
   - record `stop_reason`
   - STOP
13. If verification evidence is recorded and session does not end early:
   - set status: `evidence_ready`
14. Runner stops before task completion.

## 10. Non-goals

M13 does not implement:

- autonomous agent execution
- automatic task completion
- automatic task failure
- automatic task dropping
- queue movement
- approval marker generation
- automatic approval
- rollback automation
- deployment automation
- backend
- web UI
- multi-agent orchestration
- vector DB / full RAG
- modification of `tasks/active-task.md`
- automatic stop_reason inference without evidence
- execution steps when readiness is FAIL, PARTIAL, or NOT RUN
- introduction of status values beyond the four defined in section 6

## 11. Required Future Artifacts

Planned M13 artifacts:

- `docs/EXECUTION-SESSION.md`
- `templates/execution-session.md`
- `scripts/run-active-task.py`
- `tools/execution/RUN-ACTIVE-TASK.md`
- `tools/execution/EXECUTION-STEP-PROTOCOL.md`
- `scripts/check-execution-scope.py`
- `scripts/run-execution-verification.py`
- `reports/execution-evidence-report.md`
- `tests/fixtures/negative/execution-runner/`
- `scripts/test-execution-runner-fixtures.py`
- `reports/milestone-13-completion-review.md`

This specification defines the boundary and behavior model only. It does not implement execution scripts in this task.
