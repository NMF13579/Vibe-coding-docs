# HANDOFF — История разработки шаблона

> Архив. Перенесён из `HANDOFF.md` после подготовки шаблона к публикации (2026-04-11).
> Для новых проектов: используй корневой `HANDOFF.md` — он чистый.

---

## Что мы делали в последний раз (2026-04-10)

**Триггеры `lessons.md`:** в `LAYER-1/task-protocol.md` добавлены пункты в Блок 4 (урок задачи → `LAYER-3/lessons.md`) и в RELEASE Блок 5 (уроки релиза); в `LAYER-3/lessons.md` обновлён раздел «Когда обновлять». Коммит: `be3f8df`.

**Разделение аудита (Cursor):** протокол AUDIT-FULL — `LAYER-1/audit.md`; чек-лист и таблица HEALTH-SCORE — новый `LAYER-1/audit-checklist.md`. В `llms.txt` добавлен маршрут для проверки пакета в новой AI-среде. CHANGELOG **v0.3.2**.

**Полный аудит репозитория (Perplexity, 2026-04-10 21:50 +05):**
- Проведён аудит по 6 слоям: Продукт, Архитектура, Процесс, Качество, Безопасность, Маршрутизация агента.
- Обновлены: `HANDOFF.md`, `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/fixes.md`.
- Итог: структура здорова, два критичных пробела — `lessons.md` без реальных записей и `LAYER-2/qa/` с пустыми шаблонами.

**Cursor → Claude workflow:** добавлен `.cursor/CLAUDE-WORKFLOW.md`; README обновлён. CHANGELOG **v0.3.1**.

**Архитектура Claude Code (docs-first, один `PROJECT.md`):**
- Добавлены `project/PROJECT.md`, `stages/01-interview` … `04-deploy` с `BOOT.md`, `shared/`.
- Переписан `CLAUDE.md`; `llms.txt` и `README.md` обновлены.
- Новые файлы: `README-NEW-ARCHITECTURE.md`, `CHECKLIST.md`. CHANGELOG → **v0.3.0**.

**Аудит v2 — доисправление:**
- Устаревшие ссылки (6 штук): `memory-bank/*` и `docs/*` → актуальные пути LAYER-*/
- `llms.txt`: добавлены ещё 4 маршрута.
- CHANGELOG.md: добавлена запись v0.2.1.

**Аудит v1:**
- Исправлены 8 UPPERCASE-ссылок в `project-interview.md`.
- Удалена директория `docs/` (21 legacy-файл), перенесены 2 уникальных.
- Добавлены 5 маршрутов в `llms.txt`.
- Переименован `navigation.md` → `tools/template-sync-index.md`.
- Удалены: `SCOPE-CREEP-GUARD.md`, `opencode.json`.

**Сессия 2026-04-11 (Perplexity):**
- Добавлена таблица уровней (0/1/2) в `QUICK-START-NOVICE.md`.
- Создан `LAYER-1/levels-guide.md` (перенос из `START.md`).
- Удалён `START.md`.
- Удалены ссылки на `GEMINI.md` из `README.md`.
- Проведён аудит качества данных; решено заморозить историю шаблона в архиве.
