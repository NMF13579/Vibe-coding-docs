# Apply Preconditions

## 1. Definition

Apply preconditions are mandatory checks that must pass before a prepared
lifecycle transition can be applied in M15.

Apply preconditions do not apply a transition.
Apply preconditions do not mutate lifecycle state.
Apply preconditions only decide whether a future apply operation is allowed.
A prepared transition without passing apply preconditions must remain unapplied.

## 2. Why Apply Preconditions Exist

They exist to prevent unsafe or accidental lifecycle mutation.

They enforce that lifecycle mutation is explicit, approved, evidence-backed,
and conflict-safe.

## 3. Readiness Checks vs Apply Preconditions

Readiness checks (M14):

- decide whether transition may be prepared
- produce readiness/transition evidence
- do not apply lifecycle mutation

Apply preconditions (M15 gate before apply):

- decide whether prepared transition may be applied
- validate approval, destination safety, and conflict conditions
- do not apply lifecycle mutation by themselves

## 4. Required Precondition Groups

All groups are required.

### 4.1 Task Identity

- `task_id` exists
- `task_id` in prepared transition matches apply request

Failure example:

- task_identity_mismatch

### 4.2 Prepared Transition

- prepared transition reference exists
- referenced transition is in prepared state
- transition belongs to target task

Failure example:

- missing_prepared_transition

### 4.3 Readiness Evidence

- required readiness evidence exists
- readiness evidence can be linked to same task

Failure example:

- missing_readiness_evidence

### 4.4 Verification Evidence

- required verification evidence exists
- verification evidence belongs to same execution context

Failure example:

- missing_verification_evidence

### 4.5 Target State

- target state is one of allowed M15 outcomes
- target state is valid for current prepared transition

Failure example:

- invalid_target_state

### 4.6 Approval Requirement

- approval_required is explicit
- if approval_required=true, approval_ref must exist and be valid

Failure example:

- missing_required_approval

### 4.7 Destination Safety

- destination is safe for mutation
- no destination-level safety restriction is violated

Failure example:

- unsafe_destination

### 4.8 Conflict Prevention

- no conflicting transition for same task is active
- no conflicting apply attempt is in progress

Failure example:

- conflicting_transition

### 4.9 Evidence Preservation

- required evidence references are preserved and readable
- evidence links are not broken before apply

Failure example:

- evidence_preservation_failure

## 5. Result Model

Required result values:

```yaml
result: PASS | BLOCKED
```

PASS:

- all required precondition groups pass

BLOCKED:

- one or more required precondition groups fail
- apply must remain disallowed

## 6. Failure Reason Model

Required blocked reason examples:

```yaml
blocked_reasons:
  - missing_prepared_transition
  - task_identity_mismatch
  - missing_readiness_evidence
  - missing_verification_evidence
  - invalid_target_state
  - missing_required_approval
  - conflicting_transition
  - unsafe_destination
  - evidence_preservation_failure
```

Rules:

- `blocked_reasons` must list concrete failures
- empty `blocked_reasons` is invalid when result is BLOCKED
- apply operation must not proceed while any blocked reason remains

## 7. Minimal Precondition Result Fields

If a precondition result artifact is produced, it should contain only:

```yaml
task_id:
prepared_transition_ref:
target_state:
result:
blocked_reasons:
required_evidence:
approval_required:
approval_ref:
checked_at:
checked_by:
```

## 8. Non-Goals

This model does not:

- implement precondition checking logic
- apply transitions
- mutate lifecycle state
- create approvals
- create applied transition records
- redefine readiness, preparation, or lifecycle mutation semantics
- require new lifecycle directories
