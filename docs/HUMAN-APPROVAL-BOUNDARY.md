# Human Approval Boundary
## 1. Purpose
This document defines the boundary between lifecycle evidence and explicit human authorization.

Normative boundary:
- evidence is not approval
- command success is not approval
- validation PASS is not approval
- approval must be explicit when required by lifecycle rules

## 2. Approval Boundary
Human approval is a distinct authorization artifact or explicit owner decision.

Human approval is not automatically created by:
- verification PASS
- completion readiness PASS
- prepared transition record
- apply preconditions PASS
- dry-run success
- apply plan creation
- applied transition record creation
- mutation plan creation
- fixture test success
- audit PASS
- validator PASS
- vague user confirmation

## 3. Non-Approval Signals
The following MUST NOT be treated as approval:
- `PASS`
- `READY`
- `MILESTONE_COMPLETE`
- successful dry-run
- successful validation command
- successful audit command
- successful fixture run
- existence of an apply plan
- existence of an applied transition record
- existence of a mutation plan
- user messages such as: `ok`, `looks good`, `continue`, `дальше`, `go ahead`, `seems fine`, `probably fine`

These signals MAY support review, but they do not replace explicit approval when approval is required.

## 4. Explicit Approval Requirements
When approval is required, explicit approval should contain at minimum:

```yaml
approval:
  approved_by: "<human-or-owner-identity>"
  approved_at: "<timestamp-or-date>"
  approval_scope: "<specific operation being approved>"
  approval_statement: "<explicit approval text>"
  related_task_id: "<task id>"
  related_transition: "<transition or lifecycle operation>"
```

Incomplete approval evidence MUST NOT authorize controlled lifecycle mutation.

## 5. Approval Scope
Approval is scope-bound.

Approval for one operation MUST NOT authorize another operation.

Examples:
- approval to prepare an apply plan does not approve complete-active mutation
- approval to create applied evidence does not approve lifecycle mutation
- approval to run dry-run does not approve real apply
- approval to complete one task does not approve completing another task
- approval for temp workspace testing does not approve real repository mutation

## 6. Approval and Controlled Apply
- controlled apply may inspect approval evidence if required
- controlled apply must not create approval evidence automatically
- controlled apply must not infer approval from previous successful steps
- approval does not bypass apply preconditions
- approval does not bypass required evidence chain
- approval does not bypass mutation plan requirements
- approval does not authorize unsupported mutation paths

## 7. Approval and Failure Semantics
When any lifecycle step fails:
- failure does not authorize retry
- failure does not authorize mutation
- failure does not create approval
- failure does not allow skipping to a later lifecycle step

Retry after failure requires:
- explicit human decision, or
- a future controlled retry path with its own approval and evidence requirements

This document MUST NOT be interpreted as granting autonomous retry authority.

## 8. Approval and Unsupported Mutation Paths
Approval does not make unsupported lifecycle paths supported.

Even with approval, M16 does not support:
- needs_review lifecycle mutation
- failed lifecycle mutation
- blocked lifecycle mutation
- manual_abort lifecycle mutation
- general apply engine
- autonomous runner mode

Approval cannot expand lifecycle authority beyond implemented controlled paths.

## 9. Approval Evidence Storage Expectations
Approval evidence SHOULD be:
- file-based
- inspectable
- durable
- associated with a specific task or transition
- referenced by later evidence when used
- preserved for audit

Approval evidence MUST NOT be:
- hidden in transient command output only
- inferred from chat context only
- reconstructed after the fact
- fabricated by an agent

## 10. Agent Behavior Rules
Agents MUST:
- stop when approval is required but missing
- report that approval is missing
- ask for explicit approval only when needed
- preserve the distinction between evidence and authorization
- avoid saying a task is completed unless controlled mutation actually occurred

Agents MUST NOT:
- treat vague user text as approval
- create approval records without explicit user instruction
- edit approval evidence after mutation to make it appear valid
- proceed past approval gates automatically
- treat approval as permission to ignore scope, safety, or preconditions

## 11. Audit Visibility Requirements
Future audit coverage should inspect:
- approval boundary document exists
- non-approval signals are documented
- explicit approval fields are documented
- approval scope rules are documented
- approval does not bypass evidence chain
- approval does not bypass preconditions
- approval does not expand unsupported mutation paths
- approval evidence storage expectations are documented
- autonomous approval is explicitly disallowed

## 12. Machine Validation Hooks
This document is designed to be machine-checkable.

The following must be detectable by grep or structured parse:
- human approval boundary is defined
- non-approval signals are listed
- explicit approval fields are listed
- approval scope is required
- approval does not bypass preconditions
- approval does not bypass evidence chain
- autonomous approval is disallowed
- unsupported mutation paths remain unsupported

```yaml
human_approval_boundary:
  approval_is_distinct_authorization: true
  evidence_is_not_approval: true
  command_success_is_not_approval: true
  validation_pass_is_not_approval: true
  vague_user_text_is_not_approval: true
  explicit_approval_required_when_applicable: true
  approval_scope_required: true
  approval_does_not_bypass_preconditions: true
  approval_does_not_bypass_evidence_chain: true
  approval_does_not_expand_lifecycle_authority: true
  autonomous_approval_creation_allowed: false
  supported_mutation_paths:
    - complete-active
  unsupported_mutation_paths:
    - needs_review
    - failed
    - blocked
    - manual_abort
```

## 13. Known Limitations
This task does not implement:
- approval validator
- approval template
- approval record writer
- approval storage directory
- approval enforcement in apply command
- approval audit runner integration
- approval fixtures
- automatic approval detection

## 14. Final Rule
Human approval is valid only when it is explicit, scope-bound, durable, inspectable, and required by the applicable lifecycle rule. No validation result, command success, evidence artifact, or vague user confirmation may substitute for explicit approval.
