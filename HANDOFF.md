# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз (2026-04-10)

**Полный аудит v2 — доисправление оставшихся проблем:**

- **Устаревшие ссылки (6 штук):** `memory-bank/*` и `docs/*` → актуальные пути LAYER-*/
  - `SYSTEM_PROMPT.md`: `memory-bank/project-status.md` → `LAYER-3/project-status.md`
  - `tasks/RELEASE-CHECKLIST.md`: `docs/user-flows.md` → `LAYER-2/ux/USER-FLOWS.md`, `memory-bank/project-status.md` → `LAYER-3/project-status.md`, `docs/ROADMAP.md` → `LAYER-2/specs/roadmap.md`
  - `LAYER-1/tools/deploy/ROLLBACK-PROTOCOL.md`: `memory-bank/fixes.md` → `LAYER-3/fixes.md`
  - `LAYER-1/agents.md`: `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md` (все 6 вхождений)
- **llms.txt:** добавлены ещё 4 маршрута: `testing-guide`, `decision-guide`, `owner`, `agent-bootstrap`.
- **CHANGELOG.md:** добавлена запись v0.2.1 с полным списком изменений аудита.

**Ранее в этой сессии (аудит v1):**

- Исправлены 8 UPPERCASE-ссылок в `project-interview.md`.
- Удалена директория `docs/` (21 legacy-файл), перенесены 2 уникальных.
- Добавлены 5 маршрутов в `llms.txt`.
- Убраны embedded-дубли в `architecture.md` / `decisions.md`.
- Переименован `navigation.md` → `tools/template-sync-index.md`.
- Удалены: `SCOPE-CREEP-GUARD.md`, `opencode.json`.
- Добавлен платформенный контекст в `START.md` и `SYSTEM_PROMPT.md`.

## Что уже работает

- Маршрут агента: `llms.txt` → `HANDOFF.md` → один из 21 маршрута в LAYER-1/LAYER-2.
- Интервью и страж: `LAYER-1/interview-system.md`, `LAYER-2/discovery/project-interview.md`, адаптеры в `LAYER-1/tools/adapters/`.
- Ветка `claude/audit-documentation-105k7` запушена на remote.

## Где мы остановились

Все критические и важные проблемы из аудита закрыты. `llms.txt` содержит 30 маршрутов. CHANGELOG обновлён до v0.2.1.

## Следующий лучший шаг

1. **Прогон сценариев в IDE** — «Начнём» / «Восстанови контекст» в Claude Code / Cursor.
2. **deploy-config.md** — заполнить или добавить редирект на `LAYER-1/tools/deploy/DEPLOY-CHECKLIST.md`.
3. **START.md** — решить: удалить (legacy) или перенести в `LAYER-1/tools/`.

## Риски и вопросы

- Внешние ссылки на старые пути `docs/*` / `memory-bank/*` вне репозитория могут отвалиться — при миграции проектов обновить ссылки вручную.
- `START.md` сохранён как legacy-файл для Lovable/Bolt — при желании можно удалить или перенести в LAYER-1/tools/.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
