# GEMINI.md

This repository uses a docs-first structure for vibe coding.

## Read first

1. `README.md`
2. `llms.txt` и `LAYER-1/workflow.md`
3. `CLAUDE.md`
4. `HANDOFF.md`

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

## Behavior

- Explain things in simple language.
- Ask one question at a time when the task is unclear.
- Prefer repository docs over assumptions.
- Keep answers practical and supportive.

## Interview control (Gemini)

When running `LAYER-2/discovery/project-interview.md`, follow `LAYER-1/tools/adapters/GEMINI-INTERVIEW-CONTROL.md`: mandatory **СТРАЖ** self-check after each step per `LAYER-1/interview-system.md`; on critical **❌**, stop-block until fixed. Log to `LAYER-3/interview-session.md` with `control-mode: gemini-self-check`.

## Route by task

- Startup (new project or existing code) → `llms.txt` / `LAYER-1/workflow.md` Этап 0, `LAYER-1/agent-bootstrap.md`
- Communication → `LAYER-1/dialog-style.md`, `LAYER-1/glossary.md`
- Planning → `LAYER-2/specs/planning.md`, `LAYER-2/specs/roadmap.md`
- Architecture → `LAYER-2/specs/architecture.md`, `LAYER-1/stack-presets.md`
- Review → `LAYER-1/task-protocol.md`
- Audit → `LAYER-1/audit.md`
- Security → `LAYER-1/security.md`, `LAYER-3/security.md`
- Product suggestions → `LAYER-1/feature-radar.md`, `LAYER-3/features.md`
- Recovery → `LAYER-1/context-recovery.md`

## Sub-agent equivalents (doc-based)

| Trigger | Action |
|---|---|
| «проверь проект», «аудит», «здоровье» | Run `LAYER-1/audit.md` protocol |
| «что добавить», «что дальше», after phase close | Read `LAYER-1/feature-radar.md` + `LAYER-3/features.md`, suggest top 3 |
| 10+ edits or 3+ step plan without saving | Remind to save context |

## Update after major changes

- `HANDOFF.md`
- `LAYER-3/project-status.md`
- `LAYER-3/fixes.md` — если найден баг или откат
- `LAYER-3/deferred-decisions.md` — если решение отложено
