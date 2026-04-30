# Completion Readiness

## 1. Purpose

Completion readiness is a verifiable readiness model for an active task
before controlled completion preparation.

Its purpose is to decide whether evidence is sufficient to prepare a
completion transition record.

Important:

- completion readiness is not completion
- completion readiness is not lifecycle mutation
- completion readiness is not human approval
- completion readiness is not transition application
- completion readiness PASS only allows future preparation step

## 2. Relationship to Controlled Completion

This model is linked to:

`docs/CONTROLLED-COMPLETION.md`

Full gate chain definition is in `docs/CONTROLLED-COMPLETION.md` §4.
The chain below is shown for context; the canonical definition is there.

Completion readiness is a gate inside M14:

active task
↓
execution evidence
↓
scope check
↓
verification
↓
execution evidence report
↓
completion readiness
↓
completion transition may be prepared

Important:

completion readiness PASS means "may prepare transition", not
"task completed".

## 3. Readiness Statuses

Allowed statuses:

- PASS
- FAIL
- PARTIAL
- NOT RUN

Definitions:

PASS:

All required gates and evidence checks passed.

FAIL:

At least one required gate failed, or required evidence is invalid.

PARTIAL:

One or more required gates are not yet PASS but no gate is FAIL.
Includes:

- evidence partially assembled
- human review pending
- session in_progress

PARTIAL is distinct from FAIL. It indicates incomplete readiness,
not a hard block.

NOT RUN:

Required readiness check was not executed, active task is missing,
or no execution session exists.

Required rule:

PARTIAL is not completion-ready.
NOT RUN is not completion-ready.
FAIL blocks completion preparation.
Only PASS may allow completion transition preparation.

## 4. Required Evidence Inputs

Completion readiness must evaluate at minimum:

- active task exists
- execution session exists
- session.status is evidence_ready
- session.status is NOT in_progress
- session.status is NOT blocked
- session.status is NOT failed
- scope check result exists
- scope check result is PASS
- verification runner result exists
- verification runner result is PASS
- execution evidence report exists
- execution evidence report status is PASS
- source_contract exists
- acceptance criteria exist
- changed files list exists
- no critical evidence gaps are present
- human review status is satisfied if human review is required

Session status mapping:

- evidence_ready -> eligible for readiness check
- in_progress -> PARTIAL
- blocked -> FAIL, session is waiting and cannot proceed
- failed -> FAIL, session terminated with error
- missing session -> NOT RUN; stop_reason: session_missing
- missing active task -> NOT RUN; stop_reason: active_task_missing

Note:

`blocked` and `failed` are intentionally separated for M15
compatibility, where their semantics may differ. In M14 both produce FAIL.

## 5. Source Contract Rule

`source_contract` is defined exactly as follows:

source_contract = documented input/output guarantees of the task's implementation scope: what the task accepts, what it produces, and what invariants it preserves. Defined at task creation time.

Rule:

If source_contract is missing, completion readiness MUST NOT be PASS.

Recommended result:

source_contract missing -> FAIL
stop_reason: source_contract_missing

## 6. Acceptance Criteria Rule

Completion readiness must verify that acceptance criteria exist.

Rule:

If acceptance criteria are missing, completion readiness MUST NOT be PASS.

Recommended result:

acceptance criteria missing -> FAIL
stop_reason: acceptance_criteria_missing

Completion readiness does not re-implement all tests.
It verifies that acceptance criteria exist and were covered by
verification evidence.

## 7. Changed Files Rule

Completion readiness must require a known changed files list.

Rule:

If changed files are unknown, completion readiness MUST NOT be PASS.

Recommended result:

changed files completely unknown -> FAIL
stop_reason: changed_files_unknown

changed files partially assembled -> PARTIAL
stop_reason: changed_files_incomplete

Use FAIL if the execution claims completion but changed files are missing.
Use PARTIAL if execution evidence is still being assembled.

Changed files list is needed so future completion transition can be audited.

## 8. Human Review Rule

Human review is required when:

human_review_required: true

is explicitly set in active task, task spec, or source contract.

Rules:

human_review_required: true
human_review_status: satisfied
-> may allow PASS

human_review_required: true
human_review_status: pending
-> PARTIAL
stop_reason: human_review_pending

human_review_required: true
human_review_status: missing
-> FAIL
stop_reason: human_review_missing

human_review_required: false or absent
-> human review does not block PASS

Important:

Pending human review MUST NOT produce completion readiness PASS.

## 9. Propagation Rule

Completion readiness must follow this propagation rule:

- If any required gate = FAIL -> completion readiness = FAIL
- If no FAIL exists, but any required gate = PARTIAL -> completion readiness = PARTIAL
- If no FAIL/PARTIAL exists, but any required gate = NOT RUN -> completion readiness = NOT RUN
- Only if all required gates = PASS -> completion readiness may be PASS

Completion readiness MUST NOT be self-referential.

Invalid:

completion readiness PASS because readiness_result == PASS

Valid:

completion readiness PASS because all required evidence and gates are PASS

## 10. Stop Reason Model

If readiness_result is not PASS, stop_reason MUST be recorded.

Allowed stop_reason values:

- active_task_missing — active task file was not found; gate result = NOT RUN
- evidence_missing — one or more required evidence artifacts are missing
- session_missing — no execution session found; gate result = NOT RUN
- scope_violation — scope check did not pass
- verification_fail — verification runner did not pass
- evidence_report_fail — execution evidence report did not pass
- human_review_pending — required human review is pending
- human_review_missing — required human review status is missing
- changed_files_unknown — changed files list is missing or unknown, FAIL
- changed_files_incomplete — changed files list is partially assembled, PARTIAL
- source_contract_missing — source contract is missing
- acceptance_criteria_missing — acceptance criteria are missing
- watchdog_abort — execution was terminated by watchdog
- manual_abort — execution was manually stopped
- readiness_fail — fallback: internal readiness check error when no more specific stop_reason applies; MUST NOT be used when a specific type matches

Specific stop_reason values MUST take priority over readiness_fail.

readiness_fail MUST NOT be used when a more specific stop_reason applies.

## 11. Readiness Output Fields

Completion readiness artifact should contain:

- readiness_id
- task_id
- session_id
- source_task
- source_contract
- execution_evidence_report
- readiness_result
- stop_reason
- required_gates
- evidence_inputs
- scope_result
- verification_result
- evidence_report_result
- session_status
- acceptance_criteria_status
- changed_files_status
- human_review_required
- human_review_status
- critical_evidence_gaps
- notes
- created_at
- created_by

Allowed readiness_result values:

- PASS
- FAIL
- PARTIAL
- NOT RUN

## 12. Safety Boundaries

Safety boundaries mirror `docs/CONTROLLED-COMPLETION.md` §9.

Completion readiness model MUST NOT:

- complete task
- move task to done/
- modify tasks/active-task.md
- advance queue
- create approval records
- create transition records with status: applied
- apply lifecycle transition
- deploy
- merge
- rollback

Completion readiness is evidence only.

## 13. Expected Result

Completion readiness means:

AgentOS can determine whether completion preparation is allowed,
but cannot complete or mutate task lifecycle state.
