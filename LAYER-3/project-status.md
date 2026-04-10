# Project Status

> Updated: 2026-04-10 (аудит v3 + split audit / audit-checklist)

## Слои

- Discovery: 🟡 — артефакты в `LAYER-2/discovery/`; файлы непустые (шаблоны с структурой); заполнять по интервью.
- Specs: 🟡 — `LAYER-2/specs/`; архитектура и решения ведутся по мере работы.
- UX: 🟡 — `LAYER-2/ux/` + чеклисты в `LAYER-1/ux-checklist-{core,accessibility,medical,interactions}.md`. Хорошая UX-база (USER-FLOWS, UX-DESIGN-GUIDE). ATOMS/MOLECULES/ORGANISMS/TEMPLATES — пустые шаблоны.
- QA: 🔴 — `LAYER-2/qa/` — все 3 файла (тest-scenarios, release-blockers, post-launch-review) содержат только структуру без данных. Требует заполнения.
- Deploy: 🟡 — `LAYER-1/deploy-guide.md` + `LAYER-1/tools/deploy/` + `LAYER-2/specs/deploy-config.md`.
- Lessons: 🔴 — `LAYER-3/lessons.md` содержит только шаблон. Реальные уроки не зафиксированы.

## Текущий этап

Проведён полный аудит v3 (2026-04-10). Структура здорова. Два открытых пробела: пустой QA-слой и пустой `lessons.md`. CHANGELOG — **v0.3.1**. Аудиты v1+v2 закрыты.

## Последнее действие (2026-04-10)

**Аудит v3 (Perplexity):**
- Прочитаны: HANDOFF.md, project-status.md, lessons.md, fixes.md, llms.txt, все директории LAYER-1/2/3.
- Обновлены: HANDOFF.md, project-status.md, lessons.md, fixes.md.
- Найдено: `src/` без документации; QA-шаблоны пустые; `lessons.md` не заполнен.

Ранее — `.cursor/CLAUDE-WORKFLOW.md` — мост для Cursor к `CLAUDE.md` и `stages/*/BOOT.md`:
- Новые каталоги: `project/`, `stages/`, `shared/`; переписан `CLAUDE.md`.
- `README.md`: ссылки на `navigation.md` заменены на `LAYER-1/tools/template-sync-index.md`.

Ранее — аудит v2 — доисправление после перепроверки:
- Исправлены 6 устаревших ссылок на `memory-bank/*` и `docs/*` в 4 файлах
- Добавлены 4 маршрута в `llms.txt` (testing-guide, decision-guide, owner, agent-bootstrap)
- Обновлён CHANGELOG.md → v0.2.1

Аудит v1 (ранее):
- 8 битых ссылок в `project-interview.md`
- Удалена `docs/` (21 файл), перенесены 2 уникальных
- 5 маршрутов в `llms.txt`
- navigation.md → template-sync-index.md
- Удалены: SCOPE-CREEP-GUARD.md, opencode.json
- Ветка: `claude/audit-documentation-105k7`

См. также `LAYER-3/session-log.md` и `HANDOFF.md`.
