# Controlled Completion Workflow

## Purpose
This workflow is a protocol, not a single command.

## Core Safety Boundary
- approval evidence is authorization input only
- approval evidence is file-based
- approval evidence is explicit
- approval evidence is not lifecycle mutation
- approval evidence is not task completion
- approval evidence does not bypass preconditions
- approval evidence does not bypass validation
- approval evidence does not bypass audit
- approval evidence does not replace apply preconditions
- approval evidence does not replace prepared transition
- approval evidence does not replace mutation plan
- approval evidence is never inferred
- approval evidence is never created
- approval evidence does not expand supported lifecycle operations
- approval evidence does not authorize unsupported target states

## Controlled Completion Sequence
1. Produce verification evidence
2. Check completion readiness
3. Prepare completion transition
4. Check apply preconditions
5. Confirm explicit human approval evidence if approval is required
6. Run dry-run
7. Prepare apply plan
8. Create applied transition record
9. Prepare mutation plan
10. Run controlled complete-active mutation
11. Run lifecycle validation
12. Run lifecycle audit
13. Preserve evidence

## Step Placement Rule
Approval evidence check is required after apply preconditions and before controlled complete-active mutation.

## Operational Notes
- Approval requirement is detected from lifecycle input fields when present.
- Approval validation is handled by `scripts/validate-human-approval.py`.
- Missing approval when required results in BLOCKED.
- Invalid approval when provided results in BLOCKED.
- Approval does not replace dry-run, apply plan, applied transition record, or mutation plan.
