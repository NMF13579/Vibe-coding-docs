# Apply Command Integration
## 1. Purpose
This document defines the command-level integration contract for the existing controlled apply path.

It explains how existing modes of `scripts/apply-transition.py` MUST be used together as one safe lifecycle sequence.

## 2. Command Boundary
- `scripts/apply-transition.py` is the current command surface for controlled apply.
- This document describes existing modes only.
- This document does not create new command authority.
- Command documentation does not itself authorize lifecycle mutation.

## 3. Supported Command Modes
### Dry-run mode
- Command form:
  `python3 scripts/apply-transition.py --transition <prepared-transition-file> --dry-run`
- Purpose: preview and gate checks before mutation.
- Required inputs: prepared transition file.
- Produced output: dry-run result and blocked reasons if any.
- May mutate lifecycle state: MUST NOT.
- May write files: MUST NOT.
- Requires prior evidence: MAY use existing evidence checks, but does not require new write output.

### Apply plan prepare mode
- Command form:
  `python3 scripts/apply-transition.py --transition <prepared-transition-file> --prepare --plan-out <apply-plan-file>`
- Purpose: create apply plan artifact.
- Required inputs: prepared transition file, explicit plan output path.
- Produced output: apply plan file.
- May mutate lifecycle state: MUST NOT.
- May write files: MAY write only explicit `--plan-out` path when checks pass.
- Requires prior evidence: MUST satisfy its own preconditions.

### Evidence-only apply mode
- Command form:
  `python3 scripts/apply-transition.py --transition <prepared-transition-file> --plan <apply-plan-file> --apply --applied-record-out <applied-transition-record-file>`
- Purpose: create applied transition evidence artifact.
- Required inputs: prepared transition file, apply plan file, explicit applied record output path.
- Produced output: applied transition record file.
- May mutate lifecycle state: MUST NOT.
- May write files: MAY write only explicit `--applied-record-out` path when checks pass.
- Requires prior evidence: MUST have valid plan and passing checks.

### Complete-active mutation plan mode
- Command form:
  `python3 scripts/apply-transition.py --transition <prepared-transition-file> --plan <apply-plan-file> --applied-record <applied-transition-record-file> --complete-active-plan`
- Purpose: produce mutation planning evidence.
- Required inputs: prepared transition file, apply plan file, applied transition record file.
- Produced output: mutation plan evidence (printed and/or file-based, depending on implementation).
- May mutate lifecycle state: MUST NOT.
- May write files: MAY write only mutation planning evidence allowed by existing implementation.
- Requires prior evidence: MUST have valid prior artifacts.

### Complete-active lifecycle mutation mode
- Command form:
  `python3 scripts/apply-transition.py --transition <prepared-transition-file> --plan <apply-plan-file> --applied-record <applied-transition-record-file> --mutation-plan <complete-active-mutation-plan-file> --policy <policy-case-file> --complete-active`
- Purpose: execute controlled complete-active lifecycle mutation.
- Required inputs: prepared transition file, apply plan file, applied transition record file, mutation plan file.
- Produced output: controlled mutation result and modified task paths.
- May mutate lifecycle state: MAY, only through supported complete-active path.
- May write files: MAY, only inside allowed complete-active lifecycle path.
- Requires prior evidence: MUST have full required chain.
- Policy gate: MUST run `scripts/check-apply-preconditions.py` before mutation and pass `--policy` (and `--approval` when provided).

## 4. Canonical Command Sequence
Required command sequence:

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --dry-run
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --prepare \
  --plan-out <apply-plan-file>
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --apply \
  --applied-record-out <applied-transition-record-file>
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --applied-record <applied-transition-record-file> \
  --complete-active-plan
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --applied-record <applied-transition-record-file> \
  --mutation-plan <complete-active-mutation-plan-file> \
  --complete-active
```

Normative sequence rules:
- commands MUST be executed in this order
- commands MUST NOT be skipped
- commands MUST NOT be reordered
- every command has its own preconditions
- successful completion of one command does not automatically authorize the next command

## 5. Command Non-Equivalence Rules
- dry-run != apply plan
- apply plan != applied transition record
- applied transition record ≠ lifecycle mutation
- mutation plan != lifecycle mutation
- complete-active command is the only supported real lifecycle mutation path
- command documentation != approval
- command output != human approval unless explicit approval evidence exists

## 6. Write Boundary
- dry-run MUST NOT write files.
- prepare mode MAY write only the apply plan output path.
- evidence-only apply MAY write only the applied transition record output path.
- mutation plan mode MAY write or print only mutation planning evidence, depending on existing implementation.
- complete-active MAY mutate only the allowed active task lifecycle path under the controlled command contract.

Protected paths remain protected unless the specific controlled mode explicitly allows the specific write.

Protected paths include:
- `docs/`
- `templates/`
- `reports/` except explicit evidence output when allowed
- `tasks/` except the controlled complete-active lifecycle mutation path
- source-of-truth files

## 7. Required Inputs by Mode
Dry-run:
- prepared transition file

Prepare:
- prepared transition file
- explicit plan output path

Evidence-only apply:
- prepared transition file
- apply plan file
- explicit applied record output path

Complete-active mutation plan:
- prepared transition file
- apply plan file
- applied transition record file

Complete-active mutation:
- prepared transition file
- apply plan file
- applied transition record file
- complete-active mutation plan file

## 8. Required Outputs by Mode
Dry-run:
- human-readable preview
- no durable lifecycle mutation

Prepare:
- apply plan file

Evidence-only apply:
- applied transition record file

Complete-active mutation plan:
- mutation plan evidence describing destination, operation, allowed task paths, would_mutate, and blocked reasons

Complete-active mutation:
- controlled lifecycle mutation
- observable diff and/or durable audit artifact
- no unsupported lifecycle state mutation

## 9. Failure Semantics
- failed dry-run -> stop
- failed plan preparation -> stop
- failed evidence-only apply -> stop
- failed mutation plan -> stop
- failed complete-active -> stop and preserve evidence for review

Normative failure rules:
- failure does not authorize retry
- failure does not authorize lifecycle mutation
- failure does not authorize skipping to a later command
- agent MUST NOT continue automatically after failure
- retry or abort requires explicit human decision, or a future controlled command path with its own approval and evidence requirements

## 10. Human Approval Boundary
Human approval cannot be inferred from:
- command existence
- successful dry-run
- successful plan preparation
- successful applied record creation
- successful mutation plan creation
- vague user confirmation
- command output that is not explicit approval evidence

Approval must be explicit if required by lifecycle rules.

Approval gate interface note:
- `--approval` may be used to provide an approval record file.
- `validate-human-approval` is the validation command for that record.
- if approval is required but missing, expected error text includes: `approval is required but no approval record`
- if approval validation fails, expected error text includes: `approval validation failed`

## 10.1 Policy Gate Boundary
- `--policy` may be used with controlled apply.
- `--complete-active` requires `--policy`.
- missing `--policy` must block `--complete-active`.
- policy-aware preconditions run before controlled lifecycle mutation.
- policy gate must not affect non-complete-active modes.
- existing behavior without `--policy` is preserved only for non-complete-active modes.
- `POLICY_DECISION: BLOCKED` cannot be overridden by valid approval.
- valid approval cannot override `BLOCKED_UNSUPPORTED`.
- valid approval cannot override `BLOCKED_FORBIDDEN`.
- valid approval cannot authorize unsupported target states.
- valid approval cannot bypass apply preconditions, validation, or audit.

## 11. Audit Requirements
Future audit tooling must be able to inspect:
- supported command modes are documented
- command order is documented
- non-equivalence rules are documented
- write boundaries are documented
- required inputs are documented
- required outputs are documented
- failure semantics are documented
- complete-active is the only supported mutation path
- unsupported lifecycle states are documented as unsupported

## 12. Machine Validation Hooks
This command integration contract is intended to be machine-checkable.

The following must be detectable by grep or structured parse:
- all supported command modes
- canonical command sequence
- write boundary
- non-equivalence rules
- failure semantics
- human approval boundary
- supported mutation path
- unsupported mutation paths

```yaml
apply_command_integration:
  command_surface: scripts/apply-transition.py
  command_sequence_defined: true
  strict_order_required: true
  command_non_equivalence_defined: true
  write_boundary_defined: true
  required_inputs_defined: true
  required_outputs_defined: true
  failure_semantics_defined: true
  human_approval_boundary_defined: true
  machine_validation_hooks_defined: true
  autonomous_lifecycle_authority: false
  supported_mutation_paths:
    - complete-active
  supported_modes:
    - dry-run
    - prepare
    - evidence-only-apply
    - complete-active-plan
    - complete-active
  unsupported_mutation_paths:
    - needs_review
    - failed
    - blocked
    - manual_abort
```

## 13. Known Limitations
This command integration contract does not support:
- needs_review mutation
- failed mutation
- blocked mutation
- manual_abort mutation
- general apply engine
- automatic approval creation
- autonomous retry
- autonomous abort
- background execution

## 14. Final Rule
The apply command sequence is valid only when each command is executed in strict order, each command's own preconditions are satisfied, all durable evidence artifacts are preserved, and lifecycle mutation occurs only through the explicitly supported complete-active controlled command path.
