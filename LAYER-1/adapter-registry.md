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
  notes: |
    type: platform navigation
    contains_logic: no
    warning: "Common references" section names `STATE.md` / `HANDOFF.md` for orientation only — not read order or policy. Not in `scripts/validate-adapters.sh` required path set.

- id: `claude`
  platform: Claude Code
  path: `CLAUDE.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `gemini`
  platform: Gemini CLI
  path: `GEMINI.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `agents`
  platform: Generic agents (Codex, OpenCode и др.)
  path: `AGENTS.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `copilot`
  platform: GitHub Copilot
  path: `.github/copilot-instructions.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `zed-rules`
  platform: Zed / compatible
  path: `.rules`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `system-prompt-pointer`
  platform: External paste / IDE
  path: `SYSTEM_PROMPT.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: pointer
    contains_logic: no

- id: `cursor-governed-repo`
  platform: Cursor
  path: `.cursor/rules/governed-repo.mdc`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect (+ adapter validation hints)
    contains_logic: no

- id: `cursor-00-core`
  platform: Cursor
  path: `.cursor/rules/00-core.mdc`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `cursor-vibe-coding-rules`
  platform: Cursor
  path: `.cursor/rules/vibe-coding-rules.mdc`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: redirect
    contains_logic: no

- id: `cursor-claude-workflow`
  platform: Cursor
  path: `.cursor/CLAUDE-WORKFLOW.md`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: bootstrap pointers
    contains_logic: no

- id: `windsurf`
  platform: Windsurf
  path: `.windsurfrules`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: stub pointer
    contains_logic: no

- id: `aider`
  platform: Aider
  path: `.aider.conf.yml`
  status: `active`
  version: `v1`
  template: `LAYER-1/templates/adapter-template.md`
  notes: |
    type: config
    contains_logic: no

---

## Workflow helpers (not root adapters)

IDE-specific interview self-check snippets; not bootstrap entrypoints and not in `scripts/validate-adapters.sh` required set:

- `LAYER-1/tools/adapters/README.md`
- `LAYER-1/tools/adapters/CURSOR-INTERVIEW-CONTROL.md`
- `LAYER-1/tools/adapters/COPILOT-INTERVIEW-CONTROL.md`
- `LAYER-1/tools/adapters/CLAUDE-INTERVIEW-CONTROL.md`
- `LAYER-1/tools/adapters/GEMINI-INTERVIEW-CONTROL.md`
- `LAYER-1/tools/adapters/OPENCODE-INTERVIEW-CONTROL.md`

---

## Intentionally excluded (artifacts, not primary adapters)

| Path | Notes |
|------|------|
| `.claude/agents/*.md` | Deprecated stubs (see `LAYER-1/document-governance.md`); redirect-only, not listed as root adapters above. |

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
