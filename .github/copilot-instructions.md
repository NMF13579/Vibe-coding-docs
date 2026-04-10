# GitHub Copilot repository instructions

This repository is a docs-first operating system for vibe coding.

## How to work in this repository

- Prefer existing repository docs over assumptions.
- Explain things in simple language.
- Ask one question at a time when requirements are unclear.
- Keep suggestions practical and prioritized.
- Avoid introducing unnecessary complexity.

## Session lifecycle

At the start of every session (automatic, no command needed):
1. Read `HANDOFF.md` and `LAYER-3/project-status.md`
2. Read `LAYER-3/lessons.md` if it exists
3. If the same task appears unclosed again — warn: «⚠️ Задача [название] идёт уже несколько сессий. Разбить на части или продолжить?»
4. Summarize in 3–5 lines: current state, what was done last, 1–3 next options
5. Wait for owner's choice — do not write code until confirmed

After every completed task:
1. Update `HANDOFF.md` — what was done, where stopped, what's next
2. Update `LAYER-3/project-status.md`
3. Update additional files per the table in `CLAUDE.md` (Автосохранение section)
4. Confirm: «Контекст сохранён ✅»

Remind to save («⚠️ Контекст не сохранялся. Сохранить сейчас?») if:
- 10 or more file edits since last `HANDOFF.md` update, OR
- A plan of 3+ steps completed without updating `HANDOFF.md`

## Read first

1. `README.md`
2. `llms.txt` и `LAYER-1/workflow.md`
3. `CLAUDE.md`
4. `HANDOFF.md`

## Interview control (GitHub Copilot)

When conducting the product interview per `LAYER-2/discovery/project-interview.md`, follow `LAYER-1/tools/adapters/COPILOT-INTERVIEW-CONTROL.md`: after **every** interviewer message, include a full **СТРАЖ** self-check table from `LAYER-1/interview-system.md`. On critical **❌**, do not ask the next route question until corrected (stop-block). Log steps in `LAYER-3/interview-session.md` with `control-mode: copilot-self-check`.

## Route by task

- Project startup (new project or existing code) → `llms.txt` / `LAYER-1/workflow.md` Этап 0, `LAYER-1/agent-bootstrap.md`
- Communication style → `LAYER-1/dialog-style.md`, `LAYER-1/glossary.md`
- Planning → `LAYER-2/specs/planning.md`, `LAYER-2/specs/roadmap.md`
- Architecture → `LAYER-2/specs/architecture.md`, `LAYER-1/stack-presets.md`
- Review → `LAYER-1/task-protocol.md`
- Audit → `LAYER-1/audit.md`
- Security → `LAYER-1/security.md`, `LAYER-3/security.md`
- Product suggestions → `LAYER-1/feature-radar.md`, `LAYER-3/features.md`
- Recovery after confusion → `LAYER-1/context-recovery.md`

## Sub-agent equivalents (doc-based)

| Trigger | Action |
|---|---|
| «проверь проект», «аудит», «здоровье» | Run `LAYER-1/audit.md` protocol |
| «что добавить», «что дальше», after phase close | Read `LAYER-1/feature-radar.md` + `LAYER-3/features.md`, suggest top 3 |
| 10+ edits or 3+ step plan without saving | Remind to save context |

## Update after major changes

- `HANDOFF.md`
- `LAYER-3/project-status.md`
- `LAYER-3/deferred-decisions.md` if a decision is postponed
- `LAYER-3/fixes.md` if a reusable fix was found
