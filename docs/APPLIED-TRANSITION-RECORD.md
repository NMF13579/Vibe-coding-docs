# Applied Transition Record

## 1. Definition

An applied transition record is evidence of a lifecycle mutation that already occurred.

This record belongs to M15 controlled lifecycle mutation and documents the
result of a controlled apply operation.

## 2. Prepared vs Applied Record

A prepared transition record is not an applied transition record.

Prepared record:

- describes a candidate transition before mutation
- does not prove mutation

Applied record:

- documents mutation result after controlled apply
- may contain `APPLIED` or `BLOCKED` result only

## 3. Creation Boundary

An applied transition record must not be created before a controlled apply operation succeeds.

Apply preconditions PASS does not create an applied transition record.

The record may be created only as output of a future controlled apply
operation attempt.

## 4. Relationship to Apply Preconditions

Apply preconditions are an allow/block gate before apply.

Rules:

- preconditions PASS allows future apply attempt
- preconditions BLOCKED forbids apply attempt
- applied transition record captures the outcome of apply attempt, not just
  the preconditions decision

## 5. Relationship to Human Approval

Human approval boundary remains mandatory when approval is required.

Rules:

- if approval is required, `approval_ref` must be recorded
- missing required approval must produce blocked outcome
- record must not claim applied mutation without required approval evidence

## 6. Required Fields

Applied transition record must contain only required fields:

- applied_transition_id
- source_prepared_transition
- task_id
- previous_state
- new_state
- applied_at
- applied_by
- approval_required
- approval_ref
- preconditions_result_ref
- evidence_refs
- result
- blocked_reasons
- reason

## 7. Allowed Result Values

Allowed result values:

- APPLIED
- BLOCKED

`APPLIED` means controlled apply succeeded and lifecycle mutation already
happened.

`BLOCKED` means controlled apply did not happen.

## 8. Evidence Preservation Requirements

Record must preserve references to required evidence.

Minimum preservation requirements:

- source prepared transition reference exists
- preconditions result reference exists
- evidence_refs list points to readable evidence artifacts
- task identity consistency is preserved across referenced artifacts

If preservation is broken, result must not be APPLIED.

## 9. Forbidden Record States

Forbidden:

- creating applied record before apply operation
- treating prepared record as applied evidence
- using template file as proof of real mutation
- using undefined result value
- omitting blocked reasons when result is BLOCKED

## 10. Template vs Real Evidence Boundary

The applied transition template is not evidence of lifecycle mutation.

Template file is a schema helper only.
Real evidence exists only when a controlled apply attempt produces a concrete
record with real identifiers, timestamps, and evidence links.

## 11. Non-Goals

This model does not:

- implement apply logic
- apply transitions
- create approvals
- create real applied records in this task
- redefine completion readiness or prepared transition semantics
- require new lifecycle directories
