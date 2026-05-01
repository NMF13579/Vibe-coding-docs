# Controlled Completion

## 1. Purpose

Controlled completion is a safety gate between controlled execution and
controlled lifecycle mutation.

Its purpose is to check whether a task may be prepared for completion,
without completing it automatically.

## 2. Core Rule

Task completion MUST NOT happen unless completion readiness is PASS.

Also:

- verification PASS does not imply completion
- execution evidence PASS does not imply completion
- completion readiness PASS does NOT trigger M15 automatically
- completion readiness PASS does not apply lifecycle mutation

Definition used in §5:

  source_contract = documented input/output guarantees of the task's
  implementation scope: what the task accepts, what it produces,
  and what invariants it preserves. Defined at task creation time.

## 3. Lifecycle Boundary

M14 = decide whether completion may be prepared
M15 = safely apply lifecycle transition

Allowed in M14:

- check completion readiness
- produce completion readiness result
- prepare completion transition record
- produce blocked transition record
- produce lifecycle transition evidence report

Forbidden in M14:

- move task to done/
- mutate tasks/active-task.md as completed
- advance queue automatically
- apply completion transition
- create transition records with status: applied
- generate approval automatically
- create approval records
- deploy
- merge
- rollback

## 4. Completion Gate Chain

active task exists
↓
execution session exists
↓
scope check PASS
↓
verification runner PASS
↓
execution evidence report PASS
↓
completion readiness PASS
↓
completion transition may be prepared

Important:

prepared transition is not applied transition

### Required gates

All gates listed in this chain are required unless explicitly marked
optional in the active task spec.
A gate without an explicit `optional` annotation MUST be treated as required.

### Propagation rule

Completion readiness must follow this propagation rule:

- If any required gate = FAIL -> completion readiness = FAIL
- If no FAIL, but any required gate = PARTIAL -> completion readiness = PARTIAL
- If no FAIL/PARTIAL, but any required gate = NOT RUN -> completion readiness = NOT RUN
- Only if all required gates = PASS -> completion readiness may be PASS

### Stop reason rule

If completion readiness is not PASS, `stop_reason` MUST be recorded.

Allowed `stop_reason` values:

- evidence_missing     — one or more required evidence artifacts are missing
- scope_violation      — scope check did not pass
- verification_fail    — verification runner did not pass
- evidence_report_fail — execution evidence report did not pass
- session_missing      — no execution session found; gate result = NOT RUN
- watchdog_abort       — execution was terminated by watchdog
- manual_abort         — execution was manually stopped
- readiness_fail       — fallback: internal readiness check error when no
                         more specific stop_reason applies;
                         MUST NOT be used when a specific type matches

The recorded `stop_reason` MUST reference the specific failing gate.
Specific stop reason types take priority over `readiness_fail`.

## 5. Completion Readiness Is Not Self-Referential

Completion readiness must not reference itself.

Invalid:

  completion readiness PASS because readiness_result == PASS

Valid:

  completion readiness PASS because required evidence exists
  and all required gates pass

Minimum evidence sources:

- active task
- execution session
- scope result
- verification result
- execution evidence report
- source contract (see §2 for definition)
- acceptance criteria
- changed files list
- human review status if required (see §7 for definition of "required")

## 6. Session Status Rule

Safe rule:

session.status = evidence_ready  may be considered for completion readiness
session.status = in_progress     must not produce completion readiness PASS

Definition of `evidence_ready`:

  session.status = evidence_ready when:
  - execution_evidence_report exists
  - scope_check = PASS
  - verification result is recorded

Recommended logic:

- evidence_ready  -> eligible for readiness check
- in_progress     -> PARTIAL
- blocked         -> FAIL (session is waiting and cannot proceed)
- failed          -> FAIL (session terminated with error)
- missing session -> NOT RUN; record stop_reason: session_missing

Note: `blocked` and `failed` are intentionally separated for M15
compatibility, where their semantics may differ. In M14 both result in FAIL.

## 7. Human Review Rule

If human review is required and still pending,
completion readiness MUST NOT be PASS.

Human review is "required" when:

  human_review_required: true

is explicitly set in active task or task spec.

Interpretation:

  human_review_required: true
  human_review_status: satisfied
  -> may allow PASS

  human_review_required: true
  human_review_status: pending
  -> PARTIAL

  human_review_required: true
  human_review_status: missing
  -> FAIL

If `human_review_required` is missing or false, human review
must not block completion readiness if other required gates pass.

## 8. Completion Transition Record

M14 may create a transition record, but only as an evidence artifact.

Allowed transition record statuses in M14:

- prepared
- blocked

`applied` is defined only as a future status for M15.

Explicit prohibitions:

  M14 MUST NOT create transition records with status: applied.
  A prepared completion transition record MUST NOT move task state.
  A blocked completion transition record MUST NOT move task state.

In M14, the transition record is an evidence artifact only.

## 9. Safety Non-Goals

- M14 does not complete tasks.
- M14 does not move queue items.
- M14 does not mutate active-task.md.
- M14 does not apply lifecycle transitions.
- M14 does not approve its own completion.
- M14 does not create approval records.
- M14 does not replace human approval.
- M14 does not deploy.
- M14 does not merge.
- M14 does not rollback.

## 10. Expected Result

Controlled completion means:
AgentOS can prove whether a task may be prepared for completion,
but cannot complete the task automatically.
