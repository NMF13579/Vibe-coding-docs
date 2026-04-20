# ADAPTER TEMPLATE

## Purpose
This file adapts an external platform/tool to the repository's governance system.

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
[Describe minimal integration details here]

Examples:
- How the platform loads context
- Known quirks or limitations
- Required entry points (if any)

Keep this section short and factual.

---

## Anti-patterns (forbidden)
- "Start from this file"
- "Follow this order"
- "Primary routing"
- "Use this adapter as the main system guide"
- Any instruction that redefines system flow

---

## Extension (optional)
Platform-specific integration notes may be added here if the platform
introduces implementation constraints or context-loading quirks.

Do not duplicate logic from core files.
Do not restate governance already defined elsewhere.
