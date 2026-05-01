# AgentOS Validate Usage Integration Report

## Date

2026-04-28

## Branch

dev

## Files Checked

- README.md
- docs/usage.md
- docs/quickstart.md
- tools/validation/AGENTOS-VALIDATE.md

## Files Updated

- README.md
- docs/usage.md
- docs/quickstart.md
- tools/validation/AGENTOS-VALIDATE.md

## Official Commands

- `python3 scripts/agentos-validate.py all`
- `python3 scripts/agentos-validate.py all --json`

## Focused Commands

- `python3 scripts/agentos-validate.py template`
- `python3 scripts/agentos-validate.py negative`
- `python3 scripts/agentos-validate.py guard`
- `python3 scripts/agentos-validate.py audit`
- `python3 scripts/agentos-validate.py queue`
- `python3 scripts/agentos-validate.py runner`

## Old Command References

Found in validator-specific and legacy validation docs.
Kept as advanced/debugging references.
Primary usage now points to `python3 scripts/agentos-validate.py`.

## Documentation Notes

The usage docs now present `scripts/agentos-validate.py all` as the main validation entrypoint.
The JSON mode entrypoint is documented with `scripts/agentos-validate.py all --json`.
Focused commands remain documented for debugging specific validators.
Existing underlying validator commands are still referenced where they help explain a single validator.
The wrapper is documented as orchestration only and not as a new validator.

## Known Limitations

- This milestone updates usage documentation only.
- It does not add new validation logic.
- It does not add new CLI commands.
- It does not add CI integration.
- It does not add packaging or an installable `agentos` command.
- It does not approve release.

## Safety Confirmation

This milestone only updated validation usage documentation and evidence.

No task files were intentionally modified.
No queue entries were moved.
No approval markers were created.
No state transitions were executed.
No release approval was granted.
No active-task.md replacement was performed.
No validator logic was changed.
No audit policy was changed.
WARN_THRESHOLD was not re-implemented.
Warning counts were not recalculated by the wrapper.
