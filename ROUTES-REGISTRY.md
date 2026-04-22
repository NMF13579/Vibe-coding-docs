# ROUTES-REGISTRY

This file is the primary routing and registry hub for the new architecture.
Use it to navigate modules after startup entry points (`llms.txt` for agents, `START.md` for humans).
`always` means required in baseline route.
`conditional` means read only when trigger matches the task context.
`on-request` means explicit owner/user request.
Read core modules first, then open optional modules only by trigger.
Deep docs are not part of mandatory route.
Legacy docs remain available as reference/history sources and deep detail during transition.

| Module | Path | Role | When to read | Status | Current source | Notes |
|---|---|---|---|---|---|---|
| core-rules | `core-rules/MAIN.md` | Core rules module entry | always | draft | `LAYER-1/` | Core entry migrated; detailed rules still in legacy docs |
| state | `state/MAIN.md` | Control-plane module entry | always | draft | `LAYER-3/STATE.md`, `HANDOFF.md` | Core entry migrated; formal state authority remains legacy |
| architecture | `architecture/MAIN.md` | Architecture module entry | always | draft | `ARCHITECTURE.md` | Core entry migrated; detailed architecture still legacy |
| workflow | `workflow/MAIN.md` | Operational workflow entry | always | draft | `LAYER-1/workflow.md` and related legacy docs | Core execution entry migrated; detailed procedures pending |
| adapters | `adapters/MAIN.md` | Adapter routing entry | conditional | draft | Existing adapter docs (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `DOMAIN-ADAPTER.md`) | Compatibility layer only; no alternate bootstrap |
| quality | `quality/MAIN.md` | Quality/QA routing entry | conditional | draft | `LAYER-1/testing-guide.md`, `CHECKLIST.md`, `LAYER-2/qa/` | Verification entry migrated; deep checks remain legacy |
| security | `security/MAIN.md` | Security routing entry | conditional | draft | `LAYER-1/security.md` and related legacy docs | Boundaries defined; consolidation still partial |
| medical | `medical/MAIN.md` | Medical safety routing entry | conditional | draft | `LAYER-1/MEDICAL-SAFETY.md` and related docs | Optional domain layer; not universal core |
| incidents | `incidents/MAIN.md` | Incident response routing entry | conditional | draft | `LAYER-1/error-handling.md`, `LEARNING-LOOP.md`, `incidents/incident-template.md` | Situational evidence + recovery routing |
| doctor | `doctor/MAIN.md` | Diagnosis/stabilization routing entry | conditional | draft | Recovery context from `error-handling`, `audit`, `STATE`, `HANDOFF` | Operational entry; deeper playbooks pending |
