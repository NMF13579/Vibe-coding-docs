# CHANGELOG

> История изменений. Агент добавляет запись после каждого релиза или значимого этапа.

## Инструкция для агента

После завершения задачи или достижения версионного рубежа:
1. Добавить новую запись **вверху** раздела «История» (новые записи всегда сверху)
2. Использовать формат ниже
3. Не изменять старые записи

## Формат записи
[версия] — YYYY-MM-DD
Добавлено

-

Изменено

-

Исправлено

-

text

Пропустить раздел если изменений в нём нет.

## Версионирование

- `0.1.0` — первый рабочий прототип
- `0.x.y` — x = новая функция, y = исправление
- `1.0.0` — публичный релиз

---

## История

[0.3.2] — 2026-04-10
Изменено

- Аудит разделён: протокол AUDIT-FULL остаётся в `LAYER-1/audit.md`, чек-лист и HEALTH-SCORE вынесены в `LAYER-1/audit-checklist.md`
- В `llms.txt` добавлен маршрут «Проверка пакета в новой AI-среде» → `audit-checklist.md`
- Обновлены перекрёстные ссылки: README, CLAUDE.md, system-prompt, copilot-instructions, cursor rules, audit-agent, template-sync-index

[0.3.1] — 2026-04-10
Добавлено
- [`.cursor/CLAUDE-WORKFLOW.md`](./.cursor/CLAUDE-WORKFLOW.md) — для Cursor: ссылка на [`CLAUDE.md`](./CLAUDE.md) и этапы `stages/*/BOOT.md`.

Изменено
- [`README.md`](./README.md) — в блоке AI-сред упоминание `CLAUDE-WORKFLOW.md`.

[0.3.0] — 2026-04-10
Добавлено
- Поток **Claude Code**: единое ТЗ [`project/PROJECT.md`](./project/PROJECT.md), этапы [`stages/01-interview`](./stages/01-interview/BOOT.md) … [`stages/04-deploy`](./stages/04-deploy/BOOT.md) с `BOOT.md`, общие правила [`shared/`](./shared/README.md).
- [`README-NEW-ARCHITECTURE.md`](./README-NEW-ARCHITECTURE.md) — краткий обзор; [`CHECKLIST.md`](./CHECKLIST.md) — чеклист перед деплоем.
- [`CLAUDE.md`](./CLAUDE.md) переписан под Plan → Confirm → Execute, `LOCKED`, `❓ НЕ ОПРЕДЕЛЕНО`, smoke-test и приоритет источников.

Изменено
- [`llms.txt`](./llms.txt) — блок маршрутов Claude Code к `project/`, `stages/`, `shared/`, `CHECKLIST.md`.
- [`README.md`](./README.md) — строка про Claude Code; ссылки `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md`.

[0.2.1] — 2026-04-10
Исправлено
- 8 битых UPPERCASE-ссылок в `project-interview.md` → строчные имена файлов.
- 6 устаревших ссылок на `memory-bank/*` и `docs/*` в SYSTEM_PROMPT.md, RELEASE-CHECKLIST.md, ROLLBACK-PROTOCOL.md, agents.md.
- Embedded-дубли в `architecture.md` и `decisions.md` — убраны, оставлены чистые шаблоны.
- `LAYER-1/navigation.md` переименован → `LAYER-1/tools/template-sync-index.md`; ссылки на TEMPLATE-SYNC-*.md исправлены.

Добавлено
- 9 маршрутов в `llms.txt`: workflow, anti-patterns, security, glossary, feature-radar, testing-guide, decision-guide, owner, agent-bootstrap.
- Платформенный контекст в `START.md` и `SYSTEM_PROMPT.md` (deprecated-заголовки для Lovable/Bolt).

Удалено
- Директория `docs/` (21 legacy-файл); 2 уникальных перенесены: `ROLLBACK-PROTOCOL.md` → `LAYER-1/tools/deploy/`, `RELEASE-CHECKLIST.md` → `tasks/`.
- `SCOPE-CREEP-GUARD.md` (дубль scope-guard.md).
- `opencode.json`.

[0.2.0] — 2026-04-10
Добавлено
- Слои `LAYER-1/` (инструкции агента), `LAYER-2/` (ТЗ), `LAYER-3/` (память); точка входа `llms.txt`.
- `FAQ.md`, `LICENSE` (MIT), `LAYER-3/session-log.md`.

Изменено
- Документация перенесена из `docs/` и `memory-bank/` в LAYER-*; корень очищен.
- Скрипты `setup.js` и `template-sync.js` — в `LAYER-1/tools/`.

Исправлено
- Ссылки в README, CLAUDE, GEMINI, правилах Cursor, Copilot, OpenCode, workflow.

