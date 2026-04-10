# Project Status

> Updated: 2026-04-10 (аудит v1)

## Слои

- Discovery: 🟡 — артефакты в `LAYER-2/discovery/`; заполнять по интервью.
- Specs: 🟡 — `LAYER-2/specs/`; архитектура и решения ведутся по мере работы.
- UX: 🟡 — `LAYER-2/ux/` + чеклисты в `LAYER-1/ux-checklist-{core,accessibility,medical,interactions}.md`.
- QA: 🟡 — `LAYER-2/qa/` (сценарии, блокеры, post-launch).
- Deploy: 🟡 — `LAYER-1/deploy-guide.md` + `LAYER-1/tools/deploy/` + `LAYER-2/specs/deploy-config.md`.

## Текущий этап

Стабилизация шаблона документации завершена. Проведён полный аудит и исправлены все найденные проблемы.

## Последнее действие (2026-04-10)

Полный аудит репозитория как системы управления AI-агентами:
- Исправлены 8 битых ссылок в `project-interview.md`
- Удалена директория `docs/` (21 legacy-файл)
- Добавлены 5 маршрутов в `llms.txt`
- Убраны embedded-дубли в `architecture.md` / `decisions.md`
- Переименован `navigation.md` → `tools/template-sync-index.md`
- Удалены: `SCOPE-CREEP-GUARD.md`, `opencode.json`
- Ветка: `claude/audit-documentation-105k7`

См. также `LAYER-3/session-log.md` и `HANDOFF.md`.
