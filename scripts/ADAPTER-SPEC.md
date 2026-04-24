# Adapter Spec

Adapters are interface hints only.
They must not define runtime rules, startup order, authority, or policy.

## Required Adapter Shape

- Point to `llms.txt` first.
- Point to `ROUTES-REGISTRY.md` for module ownership.
- Do not duplicate canonical rules.
- Do not define a separate startup path.
- Do not override `core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, or `security/MAIN.md`.

## Validator Signal

Adapter checks should confirm that adapter files stay thin and route back to canonical modules.
