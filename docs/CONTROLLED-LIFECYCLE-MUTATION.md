# Controlled Lifecycle Mutation

## 1. Purpose

Controlled lifecycle mutation is the M15 safety model for applying a
previously prepared lifecycle transition.

It defines how lifecycle state may be changed only through an explicit,
controlled apply operation.

## 2. Core Boundary Statements

Verification PASS does not imply lifecycle mutation.
Completion readiness PASS does not imply lifecycle mutation.
Prepared transition does not imply lifecycle mutation.
Only an explicit controlled apply operation may mutate lifecycle state.

## 3. Relationship to M13, M14, M15

M13:

- executes task work in controlled execution mode
- collects execution evidence
- does not mutate lifecycle by itself

M14:

- evaluates completion readiness
- may prepare transition artifacts
- does not apply lifecycle mutation

M15:

- may apply lifecycle mutation only through explicit controlled apply
- must use prepared transition + required evidence + human approval

## 4. Prepared vs Applied Transition

Prepared transition:

- evidence artifact created before mutation
- states intent/candidate outcome
- does not change lifecycle state

Applied transition:

- explicit controlled apply action
- changes lifecycle state to allowed target state
- must produce applied transition evidence

## 5. Allowed Mutation Outcomes (Target States)

Allowed target states for controlled apply in M15:

- completed
- needs_review
- failed
- blocked
- manual_abort

Any other target state is forbidden for this model.

## 6. Forbidden Mutation Cases

Forbidden:

- implicit mutation from verification result
- implicit mutation from readiness result
- implicit mutation from prepared transition status
- autonomous mutation without human approval
- applying transition when required evidence is missing
- applying transition when source prepared transition is missing
- applying transition when previous state is unknown
- applying transition directly from M14 checks

## 7. Required Inputs for Future Apply Operation

Minimum required inputs:

- source prepared transition reference
- task_id
- previous lifecycle state
- target lifecycle state (one of allowed outcomes)
- approval reference
- evidence references
- apply actor identity
- apply timestamp
- explicit apply reason/result

## 8. Apply Preconditions

All preconditions are required before lifecycle mutation:

- prepared transition exists and is valid
- prepared transition belongs to the same task_id
- required M13/M14 evidence is present
- target state is allowed by this spec
- human approval is present and explicit
- previous_state is known and consistent with active record
- no higher-priority safety blocker is open

If any precondition fails, apply must not mutate lifecycle state.

## 9. Applied Transition Evidence Model

When mutation is applied, evidence record must contain only required fields:

```yaml
applied_transition_id:
source_prepared_transition:
task_id:
previous_state:
new_state:
applied_at:
applied_by:
approval_ref:
evidence_refs:
result:
reason:
```

## 10. Human Approval Boundary

Human approval is a mandatory boundary for lifecycle mutation in M15.

Rules:

- without explicit human approval, apply is forbidden
- approval must be linked by `approval_ref`
- approval must exist before lifecycle mutation
- automation must not create or infer approval implicitly

## 11. Non-Goals

This spec does not:

- implement apply logic
- apply transition automatically
- redefine completion readiness rules
- redefine completion transition preparation rules
- redefine failure/review classification semantics
- require creating new lifecycle directories
- require moving files in this task
- mutate lifecycle in this task

## 12. Expected Safety Result

M15 controlled lifecycle mutation means:

prepared evidence can be safely converted into a lifecycle change only by
an explicit approved apply operation, never by implicit PASS signals.
