# ANTIGRAVITY ADAPTER

## Purpose
This file adapts Antigravity to the repository's governance system.

It provides navigation hints only.
It does NOT define logic, rules, or authority.

---

## Canonical entry point
- `llms.txt`

## Common references
- `STATE.md`
- `HANDOFF.md`

`llms.txt` is the canonical entry point for repository coordination.
`STATE.md` and `HANDOFF.md` are commonly referenced coordination files.

These references do not define execution order or authority.

---

## Important constraints
- This is not a reading order.
- Do not infer execution sequence from this file.
- Do not treat this file as a source of truth.
- This adapter must not redefine authority, routing, or execution order.

---

## Adapter contract

Adapters must NOT:
- Define rules
- Define workflows
- Override system behavior
- Introduce new authority layers

Adapters may:
- Reference existing files
- Provide platform-specific hints
- Clarify how the platform should interpret the repo

---

## Platform-specific notes
Antigravity should treat this repository as a governed workspace  
with a single canonical entry point.

When repository coordination is needed:
- use `llms.txt` as the canonical bootstrap surface
- treat `STATE.md` and `HANDOFF.md` as common coordination references
- treat all adapter files as compatibility layers only

If Antigravity supports contextual file selection,  
this adapter may be used as a discovery hint,  
but not as a substitute for core governance files.

If ambiguity exists between this adapter and core governance documents,  
**core governance documents take precedence**.

---

## Anti-patterns (forbidden)
- "Start from this file"
- "Follow this order"
- "Primary routing"
- "Use this adapter as the main system guide"
- Any instruction that redefines system flow

---

## Extension (optional)
Add platform-specific constraints or context-loading quirks here if needed.

Do not duplicate logic from core files.
Do not restate governance already defined elsewhere.
