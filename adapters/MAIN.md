---
type: canonical
module: adapters
status: canonical
authority: canonical
when_to_read: conditional
owner: unassigned
---

# Adapters

## Purpose

Compatibility layer for specific agent or IDE environments.
Adapters translate canonical routing into platform format and do not define policy.

## When To Read

- A task depends on a specific runtime or IDE adapter.
- An adapter file needs validation.
- A platform wrapper appears to conflict with canonical routing.

## Canonical Constraints

- Adapters are not source of truth.
- Bootstrap remains `llms.txt`.
- Adapters must not create alternate startup paths or read order.
- Adapters may translate canonical instructions into platform-specific wording, but not policy.
- Adapter text must not weaken validator policy or invent governance rules.
- If adapter text conflicts with canonical docs, canonical docs win.

## Routing

- Use `llms.txt` for startup.
- Use `ROUTES-REGISTRY.md` for module ownership.
- Use `core-rules/MAIN.md` if authority or routing is unclear.
- Use `scripts/ADAPTER-SPEC.md` for adapter validation expectations.
