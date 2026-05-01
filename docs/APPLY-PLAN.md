# Apply Plan

## 1. Definition

An apply plan is not lifecycle mutation.

An apply plan is a controlled preparation artifact that describes a future
apply attempt after preconditions are checked.

## 2. Boundaries

An apply plan must not apply a transition.
An apply plan may only describe a future controlled apply operation.
Creating an apply plan does not create an applied transition record.
Apply preconditions PASS may allow preparing an apply plan, but does not apply lifecycle mutation.

## 3. Dry-Run vs Apply Plan vs Applied Record

Dry-run:

- evaluates whether apply would be possible
- does not write plan output by default
- does not mutate lifecycle

Apply plan:

- may be written only after preconditions are checked
- describes planned future controlled steps
- does not mutate lifecycle

Applied transition record:

- evidence of apply outcome after real controlled apply attempt
- not created by dry-run
- not created by apply-plan preparation alone

## 4. When Apply Plan May Be Prepared

Apply plan may be prepared only when:

- prepared transition exists
- apply preconditions result is PASS
- explicit output path is provided and allowed

If any condition fails, result must be blocked and no plan is written.

## 5. Required Apply Plan Fields

Apply plan must contain only required fields:

- apply_plan_id
- source_prepared_transition
- task_id
- previous_state
- target_state
- preconditions_result
- would_mutate
- planned_operations
- approval_required
- approval_ref
- applied_record_template_ref
- blocked_reasons
- prepared_at
- prepared_by
- result
- reason

## 6. Relationship to Apply Preconditions

Apply preconditions are a hard gate before apply-plan preparation.

Rules:

- preconditions PASS may allow plan preparation
- preconditions BLOCKED must block plan preparation
- blocked reasons must be preserved in blocked output

## 7. Relationship to Human Approval

Human approval rules still apply to future real apply operation.

Rules:

- apply plan may reference approval requirements
- apply plan does not create approval
- apply plan does not infer missing approval as satisfied

## 8. Relationship to Future Applied Transition Record

Apply plan may reference future applied record template path.

Rules:

- template reference is planning aid only
- no real applied record is created by plan preparation
- apply plan must not be treated as mutation evidence

## 9. Forbidden Apply Plan States

Forbidden:

- treating apply plan as lifecycle mutation
- treating apply plan as applied transition record
- preparing plan when preconditions are blocked
- writing plan to protected paths
- creating plan in tasks/, reports/, docs/, or source-of-truth templates

## 10. Non-Goals

This model does not:

- implement real apply logic
- apply transitions
- mutate lifecycle
- create approvals
- create real applied transition records
- redefine existing precondition or mutation semantics
