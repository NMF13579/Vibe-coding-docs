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

