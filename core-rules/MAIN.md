---
type: canonical
module: core-rules
status: canonical
authority: canonical
when_to_read: always
owner: unassigned
---

# Core Rules

## Purpose

Canonical module for priority, authority, governance, and agent behavior boundaries.

## Priority

- System and owner instructions outrank repository guidance.
- `llms.txt` is the only startup entry for agents.
- The five canonical modules define runtime behavior.
- When instructions conflict, follow the higher-authority source and report the conflict.
- Do not resolve important conflicts silently.
- Owner approval can authorize work inside scope, but it does not override hard constraints.

## Authority

- `core-rules/MAIN.md` owns governance and authority rules.
- `state/MAIN.md` owns state lifecycle and transitions.
- `workflow/MAIN.md` owns execution sequence and scope control.
- `quality/MAIN.md` owns verification and readiness proof.
- `security/MAIN.md` owns sensitive data, access, and compliance boundaries.
- Support documents, adapters, archives, and notes do not override canonical modules.

## Governance

- Do not create alternate startup paths.
- Keep one primary authority per rule area.
- If duplicate authority appears, stop and ask whether to merge, downgrade, or remove one source.
- Do not silently weaken prohibitive rules into soft advice.
- Do not invent missing policy.
- Do not make critical decisions without owner confirmation.
- Do not use jargon without explaining it when speaking to non-technical owners.

## Agent Boundaries

- The agent is an executor inside a governed system.
- The agent is not the product owner.
- The agent must not initiate structural changes without explicit request.
- The agent must work inside the confirmed scope.
- The agent must report uncertainty instead of guessing.
- The agent must prefer reversible, minimal changes that satisfy the task.

## Stop Signals

Stop and ask for direction when:

- the task no longer matches the confirmed scope;
- authority conflicts;
- state is contradictory or incomplete;
- verification is unclear;
- a security boundary is touched without enough context;
- one fix starts breaking unrelated behavior;
- the next step would require rewriting the agreed plan.

## Module Boundaries

- Keep governance here.
- Keep state in `state/MAIN.md`.
- Keep execution in `workflow/MAIN.md`.
- Keep proof and readiness in `quality/MAIN.md`.
- Keep security and compliance in `security/MAIN.md`.
