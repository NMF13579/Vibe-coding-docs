# Lifecycle Integration
## 1. Purpose
This specification defines how controlled lifecycle mutation artifacts are integrated into one auditable workflow.

The integration layer is normative and MUST be used as the lifecycle reference for agents and reviewers.

## 2. Integration Boundary
- M15 created the controlled apply path.
- M16 makes that path visible to workflow, audit, validation, docs, and smoke tests.
- M16 does not grant autonomous lifecycle authority.
- M16 MUST NOT introduce autonomous execution, automatic approval, or hidden lifecycle transitions.

## 3. Canonical Completion Flow
Required ordered sequence:

verification PASS  
→ completion readiness PASS  
→ prepared transition  
→ apply preconditions PASS  
→ dry-run  
→ apply plan  
→ applied transition record  
→ mutation plan  
→ controlled complete-active mutation  
→ audit / evidence / review

Normative rules:
- steps MUST be executed in this exact order
- no step may be skipped
- no step may be executed out of sequence
- completing any step does not authorize executing the next step without satisfying that next step's own preconditions

## 4. Non-Equivalence Rules
- verification PASS != lifecycle mutation
- readiness PASS != lifecycle mutation
- prepared transition != lifecycle mutation
- apply preconditions PASS != lifecycle mutation
- dry-run != lifecycle mutation
- apply plan != lifecycle mutation
- applied transition record != lifecycle mutation
- mutation plan != lifecycle mutation
- only controlled complete-active mutation may mutate lifecycle state

## 5. Controlled Mutation Authority
Current mutation authority is limited to one path:
- complete active task
- `target_state = completed`
- explicit transition input
- explicit plan input
- explicit applied record input
- explicit mutation plan input
- passing preconditions
- controlled command path

Any other lifecycle mutation path MUST be treated as unsupported.

## 6. Required Evidence Chain
Before lifecycle mutation may be considered valid, durable evidence MUST exist:
- verification evidence
  expected artifact: existing verification report or equivalent file-based evidence
- completion readiness evidence
  expected artifact: existing completion readiness report or equivalent file-based evidence
- prepared transition record
  expected artifact: file following `templates/completion-transition.md` or equivalent controlled transition format
- apply preconditions result
  expected artifact: captured checker output or file-based report referenced by later evidence
- apply plan
  expected artifact: file following `templates/apply-plan.md` or equivalent controlled apply plan format
- applied transition record
  expected artifact: file following `templates/applied-transition-record.md` or equivalent applied transition evidence format
- complete-active mutation plan
  expected artifact: file-based mutation plan describing destination, operation, allowed task paths, would_mutate, and blocked reasons
- controlled mutation execution evidence
  expected artifact: observable git diff during execution and/or durable file-based audit artifact

Normative evidence rule:
- All durable evidence artifacts MUST be file-based and detectable via filesystem inspection.
- Transient command output MAY support diagnosis, but it does not replace durable file-based evidence unless captured in an auditable artifact.

## 7. Failure Semantics
- verification FAIL -> flow MUST stop; mutation is not authorized
- completion readiness FAIL -> flow MUST stop; mutation is not authorized
- apply preconditions FAIL -> flow MUST stop; mutation is not authorized
- dry-run FAIL -> flow MUST stop; mutation is not authorized
- incomplete evidence chain -> mutation is not authorized

When any step fails:
- the failure does not authorize lifecycle mutation
- the failure does not imply retry is safe without explicit decision
- explicit retry or explicit abort decision MUST be made by a human, or by a future controlled command path only if that path has its own explicit approval and evidence requirements
- the agent MUST NOT automatically proceed past a failure

Failure semantics are normative and MUST be followed by implementations and agents consuming this spec.

## 8. Audit Visibility Requirements
Future audit coverage MUST be able to inspect:
- controlled lifecycle mutation spec exists
- apply preconditions model exists
- dry-run path exists
- apply plan path exists
- applied record path exists
- mutation plan path exists
- controlled complete-active path exists
- fixtures exist
- evidence report exists
- known limitations are documented

## 9. Workflow Visibility Requirements
User-facing workflow documentation MUST show the full sequence.
Workflow docs MUST NOT collapse multiple lifecycle steps into one hidden operation.

## 10. Human Approval Boundary
Human approval MUST NOT be inferred from:
- verification PASS
- readiness PASS
- prepared transition
- dry-run success
- apply plan
- applied transition record
- mutation plan
- vague user confirmation

Approval MUST be explicit if required by lifecycle rules.

## 11. Safety Invariants
- no implicit completion
- no autonomous apply
- no mutation without explicit command
- no mutation without evidence chain
- no mutation of reports as lifecycle state
- no mutation of docs/templates as lifecycle state
- no hidden movement of active task
- fixtures may mutate temp workspace only

## 12. Known Limitations
This integration layer does not yet support:
- needs_review lifecycle mutation
- failed lifecycle mutation
- blocked lifecycle mutation
- manual_abort lifecycle mutation
- general apply engine
- automatic approval creation
- autonomous runner mode

## 13. Machine Validation Hooks
This lifecycle integration spec is designed to be machine-checkable.

Rules for documents and artifacts implementing this spec:
- canonical flow steps MUST be detectable as distinct named stages via grep or structured parse
- evidence chain artifacts MUST be file-based and locatable via filesystem inspection
- lifecycle mutation MUST produce an observable, inspectable diff or durable audit artifact
- safety invariants MUST be expressible as boolean checks
- the integration spec itself MUST be validatable via a read-only check command

```yaml
lifecycle_integration:
  canonical_flow_defined: true
  strict_sequence_required: true
  non_equivalence_defined: true
  failure_semantics_defined: true
  mutation_authority_limited: true
  evidence_chain_required: true
  evidence_artifacts_file_based: true
  human_approval_boundary_defined: true
  machine_validation_hooks_defined: true
  autonomous_lifecycle_authority: false
  supported_mutation_paths:
    - complete-active
  unsupported_mutation_paths:
    - needs_review
    - failed
    - blocked
    - manual_abort
```

## 14. Final Rule
Controlled lifecycle mutation is valid only when the explicit controlled apply path is followed in strict sequence, the full durable evidence chain exists as inspectable file-based artifacts, and the resulting mutation is auditable through that evidence chain.
