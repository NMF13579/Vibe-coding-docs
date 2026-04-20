# ADAPTER REGISTRY

## Purpose
This file is a read-only inventory of adapter files in the repository.

It describes what adapters exist and where they are located.

It does NOT:
- control routing
- define execution order
- grant or change authority

Core governance and bootstrap remain in `llms.txt`.

---

## Registry contract

The registry:
- MAY list adapters with metadata (platform, path, status, notes)
- MAY help agents and humans discover available adapters
- MUST NOT affect reading order, authority, or system behavior

---

## Registered adapters

- id: `antigravity`
  platform: Antigravity
  path: `LAYER-1/adapters/ANTIGRAVITY.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: Production adapter. Uses standard template.

- id: `claude`
  platform: Claude Code
  path: `CLAUDE.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: Root adapter entrypoint. Redirects to llms.txt.

- id: `gemini`
  platform: Gemini CLI
  path: `GEMINI.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: Root adapter entrypoint. Redirects to llms.txt.

- id: `agents`
  platform: Generic agents (Codex, OpenCode и др.)
  path: `AGENTS.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: Root adapter entrypoint. Redirects to llms.txt.

---

## Discovery rules

Agents and users MAY use this registry to:
- find all available adapters
- understand the status of each adapter
- navigate to a specific adapter file via path

They MUST NOT:
- interpret the order of this list as adapter priority
- build a new bootstrap from the registry
- change core authority in favor of an adapter
- store business logic or system rules here

Registry = map of the territory, not a control system.

---

## Anti-patterns (forbidden)
- Using the registry as "primary routing"
- Writing instructions like "Start with this adapter"
- Automatically selecting the "main" adapter by list position
- Storing governance logic inside the registry
