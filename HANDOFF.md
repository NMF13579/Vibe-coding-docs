# HANDOFF — где мы остановились

> Этот файл нужен, чтобы следующая сессия (и человек, и AI) быстро поняли контекст.

## Что мы делали в последний раз (2026-04-10)

**Полный аудит документации + применение всех исправлений:**

- **Битые ссылки:** исправлены 8 UPPERCASE-ссылок в `LAYER-2/discovery/project-interview.md` (таблица «После интервью») — приведены к строчным именам реальных файлов на диске.
- **llms.txt:** добавлены 5 новых маршрутов: `workflow.md`, `anti-patterns.md`, `security.md`, `glossary.md`, `feature-radar.md`.
- **docs/ удалена:** 21 legacy-файл удалён (дублировали LAYER-1/LAYER-2). Два уникальных перенесены:
  - `ROLLBACK-PROTOCOL.md` → `LAYER-1/tools/deploy/ROLLBACK-PROTOCOL.md`
  - `RELEASE-CHECKLIST.md` → `tasks/RELEASE-CHECKLIST.md`
- **Дубли убраны:** `architecture.md` и `decisions.md` — embedded-дубли удалены, файлы стали чистыми шаблонами.
- **navigation.md переименован:** `LAYER-1/navigation.md` → `LAYER-1/tools/template-sync-index.md`; исправлены ссылки на несуществующие TEMPLATE-SYNC-*.md внутри.
- **Orphan-файлы удалены:** `SCOPE-CREEP-GUARD.md` (100% дубль scope-guard.md), `opencode.json`.
- **START.md и SYSTEM_PROMPT.md:** добавлен чёткий платформенный контекст (Lovable/Bolt).

## Что уже работает

- Маршрут агента: `llms.txt` → `HANDOFF.md` → один из 21 маршрута в LAYER-1/LAYER-2.
- Интервью и страж: `LAYER-1/interview-system.md`, `LAYER-2/discovery/project-interview.md`, адаптеры в `LAYER-1/tools/adapters/`.
- Ветка `claude/audit-documentation-105k7` запушена на remote.

## Где мы остановились

Все критические и важные проблемы из аудита закрыты. Репозиторий чист.

## Следующий лучший шаг

1. **Прогон сценариев в IDE** — «Начнём» / «Восстанови контекст» в Claude Code / Cursor.
2. **Обновить CHANGELOG.md** — зафиксировать изменения аудита в v0.2.1.
3. **deploy-config.md** — заполнить или добавить редирект на `LAYER-1/tools/deploy/DEPLOY-CHECKLIST.md`.

## Риски и вопросы

- Внешние ссылки на старые пути `docs/*` / `memory-bank/*` вне репозитория могут отвалиться — при миграции проектов обновить ссылки вручную.
- `START.md` сохранён как legacy-файл для Lovable/Bolt — при желании можно удалить или перенести в LAYER-1/tools/.

## Применимые уроки

- Перед началом сессии: `LAYER-3/project-status.md`, `LAYER-3/lessons.md`, `LAYER-3/session-log.md`.
