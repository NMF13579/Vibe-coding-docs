# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз (2026-04-10)

**Разделение аудита (Cursor):** протокол AUDIT-FULL — `LAYER-1/audit.md`; чек-лист и таблица HEALTH-SCORE — новый `LAYER-1/audit-checklist.md`. В `llms.txt` добавлен маршрут для проверки пакета в новой AI-среде. CHANGELOG **v0.3.2**.

**Полный аудит репозитория (Perplexity, 2026-04-10 21:50 +05):**

- Проведён аудит по 6 слоям: Продукт, Архитектура, Процесс, Качество, Безопасность, Маршрутизация агента.
- Обновлены: `HANDOFF.md`, `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/fixes.md`.
- Итог: структура здорова, два критичных пробела — `lessons.md` без реальных записей и `LAYER-2/qa/` с пустыми шаблонами.

**Cursor → Claude workflow:** добавлен [`.cursor/CLAUDE-WORKFLOW.md`](./.cursor/CLAUDE-WORKFLOW.md) со ссылкой на [`CLAUDE.md`](./CLAUDE.md) и этапы `stages/*/BOOT.md`; README обновлён. CHANGELOG **v0.3.1**.

**Архитектура Claude Code (docs-first, один `PROJECT.md`):**

- Добавлены `project/PROJECT.md` (шаблон с секциями discovery / ux / specs / deploy / decisions, `LOCKED`, `❓ НЕ ОПРЕДЕЛЕНО`), `project/archive/`.
- Добавлены `stages/01-interview` … `04-deploy` с `BOOT.md` (reads/writes/priority/smoke-test) и тонкими указателями на `LAYER-*`.
- Добавлены `shared/` (README + agent-contract, scope-guard, task-protocol, workflow — сжато со ссылками на LAYER-1).
- Переписан `CLAUDE.md` под этот поток; `llms.txt` и `README.md` обновлены (маршруты + исправлены ссылки navigation → template-sync-index).
- Новые файлы: `README-NEW-ARCHITECTURE.md`, `CHECKLIST.md`. CHANGELOG → **v0.3.0**. Ветка: `cursor/claude-code-architecture-218a`.

**Ранее — полный аудит v2 — доисправление оставшихся проблем:**

- **Устаревшие ссылки (6 штук):** `memory-bank/*` и `docs/*` → актуальные пути LAYER-*/
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

- **Claude Code:** `CLAUDE.md` → `project/PROJECT.md` + `stages/*/BOOT.md` + `shared/`; обзор — `README-NEW-ARCHITECTURE.md`.
- Маршрут агента: `llms.txt` → `HANDOFF.md` → маршруты LAYER-1/LAYER-2 или этапы `stages/`.
- Интервью и страж: `LAYER-1/interview-system.md`, `LAYER-2/discovery/project-interview.md`, адаптеры в `LAYER-1/tools/adapters/`.
- Все обязательные файлы присутствуют и непусты: `CLAUDE.md`, `HANDOFF.md`, `llms.txt`, `LAYER-1/workflow.md`, `LAYER-1/scope-guard.md`, `LAYER-1/agent-bootstrap.md`, `LAYER-1/agent-contract.md`, `LAYER-3/project-status.md`.
- Директория `docs/` удалена (legacy очищен).

## Где мы остановились

Внедрена целевая структура под Claude Code (v0.3.1 в CHANGELOG). Проведён полный аудит v3. Два незакрытых пробела: `lessons.md` без реальных записей; QA-файлы в `LAYER-2/qa/` — пустые шаблоны.

## Следующий лучший шаг

1. **Заполнить `LAYER-3/lessons.md`** реальными уроками из аудитов v1+v2 (накопленные паттерны уже задокументированы в HANDOFF).
2. **Заполнить `LAYER-2/qa/test-scenarios.md`** хотя бы 3–5 сценариями для smoke-test шаблона.
3. **Прогон в Claude Code:** «Прочитай `stages/01-interview/BOOT.md`» на чистом форке шаблона.
4. **Опционально:** link-checker для markdown, шаблон weekly-summary, политика архива в `project/archive/`.

## Риски и вопросы

- `lessons.md` содержит только шаблон — реальные уроки не записаны, знания теряются между сессиями.
- `LAYER-2/qa/` — все три файла (`test-scenarios.md`, `release-blockers.md`, `post-launch-review.md`) содержат только структуру без данных.
- `LAYER-3/fixes.md` — дата не обновлена (`YYYY-MM-DD`), исправлений нет — файл не используется.
- `START.md` сохранён как legacy-файл для Lovable/Bolt — при желании можно удалить или перенести в `LAYER-1/tools/`.
- Внешние ссылки на старые пути `docs/*` / `memory-bank/*` вне репозитория могут отвалиться — при миграции проектов обновить ссылки вручную.
- `src/` директория в корне — в llms.txt не упомянута, роль не задокументирована.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
