# Controlled Completion Workflow

## Purpose
workflow is a protocol, not a single autonomous command

## Controlled Completion Sequence
verification evidence
→ completion readiness
→ prepared transition
→ policy classification
→ policy validation
→ approval requirement decision
→ approval evidence if required
→ approval validation if required
→ apply preconditions
→ dry-run
→ apply plan
→ applied transition record
→ mutation plan
→ controlled complete-active mutation
→ validation
→ audit
→ preserve evidence

## Policy Rules
- policy classification happens before approval validation
- policy validation happens before approval validation
- approval requirement is decided by policy
- approval is required only when policy returns `APPROVAL_REQUIRED`
- BLOCKED_UNSUPPORTED blocks workflow even with valid approval
- BLOCKED_FORBIDDEN blocks workflow even with valid approval
- approval cannot override policy block
- approval cannot authorize unsupported target states
- approval cannot expand supported operations
- approval cannot bypass preconditions
- approval cannot bypass validation
- approval cannot bypass audit

## Controlled Apply Rules
- --complete-active is controlled real lifecycle mutation
- --complete-active requires --policy
- missing --policy must block --complete-active
- existing behavior without --policy is preserved only for non-complete-active modes
- policy gate must not affect non-complete-active modes
- policy-aware preconditions must pass before controlled lifecycle mutation
- lifecycle state must not mutate before policy-aware preconditions pass

## Approval Boundary Rules
- approval evidence is authorization input only
- approval evidence is not lifecycle mutation
- approval evidence is not task completion
- approval evidence is never inferred from conversation text
- approval evidence is never inferred from command success
- validation PASS is not approval
- audit PASS is not approval
- approval file does not replace preconditions
- approval file does not replace validation
- approval file does not replace audit

## Non-Autonomy Rules
- policy does not create approval evidence
- policy does not mutate lifecycle state
- policy does not replace approval validation
- policy does not replace preconditions
- controlled mutation remains bounded by explicit mode, policy, approval if required, validation, and audit
