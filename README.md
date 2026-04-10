# Vibe-coding-docs

[![Use this template](https://img.shields.io/badge/use%20this%20template-2ea44f?style=for-the-badge&logo=github)](https://github.com/NMF13579/Vibe-coding-docs/generate)

[![Documentation](https://img.shields.io/badge/documentation-DOCS--MAP-0366d6?style=flat&logo=readthedocs)](./LAYER-1/tools/template-sync-index.md)

> Шаблон документации для работы с AI-агентами: помогает вести проект от идеи до MVP без хаоса и потери контекста.

Создан для вайб-кодеров — врачей, дизайнеров, менеджеров и всех, кто строит продукты с помощью ИИ без глубокого погружения в код.

---

## Что это такое

Этот репозиторий — рабочий шаблон, который помогает:

- запускать новый проект структурированно, не теряя мысли;
- сохранять контекст между сессиями — агент «помнит», где остановились;
- фиксировать задачи, решения и статус проекта;
- работать с AI-агентами предсказуемо, по правилам, а не «как получится».

---

## Для кого

Подойдёт, если ты:

- хочешь быстро стартовать цифровой продукт и довести до MVP;
- работаешь через Claude, Cursor, Copilot, Gemini или похожие AI-сервисы;
- не хочешь каждый раз заново объяснять агенту весь проект;
- хочешь, чтобы AI помогал по правилам, а не импровизировал.

---

## Как начать

1. Нажми кнопку **"Use this template"** на GitHub — это создаст чистый репозиторий без истории коммитов.
2. Открой проект в удобном AI-инструменте.
3. Напиши агенту: **«Начнём»** — он сам проведёт через всё остальное.
4. После каждой сессии пиши: **«Сохрани контекст»**.
5. В начале новой сессии пиши: **«Восстанови контекст»**.

---

## Самые полезные команды

| Команда | Что делает |
|---|---|
| `Начнём` | Запустить новый проект |
| `Восстанови контекст` | Начать сессию по существующему проекту |
| `Сохрани контекст` | Закончить сессию без потерь |
| `Всё верно` / `Ок` | Подтвердить план или следующий шаг |
| `Всё сломалось` | Откатить изменения, когда что-то пошло не так |
| `Проверь готовность к релизу` | Финальная проверка перед деплоем |

---

## Куда смотреть дальше

| Ситуация | Документ |
|---|---|
| Совсем новый? Начни здесь | [`QUICK-START.md`](./QUICK-START.md) — минимум для старта |
| Точка входа для агента | [`llms.txt`](./llms.txt) → [`HANDOFF.md`](./HANDOFF.md) |
| **Claude Code: одно ТЗ + этапы** | [`README-NEW-ARCHITECTURE.md`](./README-NEW-ARCHITECTURE.md) → [`project/PROJECT.md`](./project/PROJECT.md) → [`stages/01-interview/BOOT.md`](./stages/01-interview/BOOT.md) |
| Первый запуск / конвейер | [`LAYER-1/workflow.md`](./LAYER-1/workflow.md) |
| Клонировал для нового проекта | [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md) → напиши агенту `Начнём` |
| Не знаешь, что написать агенту | [`LAYER-1/owner.md`](./LAYER-1/owner.md) или [`FAQ.md`](./FAQ.md) |
| Где мы остановились? | [`HANDOFF.md`](./HANDOFF.md) → [`LAYER-3/project-status.md`](./LAYER-3/project-status.md) |
| Планирование и дорожная карта | [`LAYER-2/specs/roadmap.md`](./LAYER-2/specs/roadmap.md), [`LAYER-2/specs/planning.md`](./LAYER-2/specs/planning.md) |
| История изменений шаблона | [`CHANGELOG.md`](./CHANGELOG.md) |
| Прямая подача в LLM | [`llms.txt`](./llms.txt) |
| Частые ситуации (FAQ) | [`FAQ.md`](./FAQ.md) |
| Задача начала расползаться | [`LAYER-1/scope-guard.md`](./LAYER-1/scope-guard.md) |
| Всё перепуталось, нужен recovery | [`LAYER-1/context-recovery.md`](./LAYER-1/context-recovery.md) |
| Нужно откатить изменения | [`LAYER-1/error-handling.md`](./LAYER-1/error-handling.md) |
| Аудит проекта | [`LAYER-1/audit.md`](./LAYER-1/audit.md) (протокол), [`LAYER-1/audit-checklist.md`](./LAYER-1/audit-checklist.md) (чек-лист и HEALTH-SCORE) |
| Процессы и UX (spec-driven) | Если хочешь вести проект по процессам и UX — начни с [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md) и [`LAYER-1/agent-contract.md`](./LAYER-1/agent-contract.md). |

---

## Вставить в настройки AI-инструмента

Для лучшей работы агента вставь содержимое [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md) в системный промпт своего инструмента:

| Инструмент | Куда вставить |
|---|---|
| Cursor | Settings → Rules for AI |
| Claude Code | `CLAUDE.md` уже в корне — всё готово |
| Lovable | Knowledge → System Instructions |
| Bolt | Project Settings → AI Instructions |
| Gemini | Используй [`GEMINI.md`](./GEMINI.md) |

---

## Принципы работы агента

- Агент не пишет код без подтверждённого плана.
- Один вопрос за раз — агент не засыпает списком.
- Документы заполняются, не остаются пустыми шаблонами.
- `LAYER-2/specs/roadmap.md` защищает от расползания проекта.
- `LAYER-2/specs/decisions.md` останавливает повторное обсуждение уже принятых решений.

---

## Для продвинутой настройки

Если хочешь детальнее настроить поведение агента или понять внутреннюю логику:

- Правила агента → [`CLAUDE.md`](./CLAUDE.md)
- Системный промпт → [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md)
- Карта ролей агентов → [`LAYER-1/agents.md`](./LAYER-1/agents.md)
- Инструкции агента (слой 1) → [`LAYER-1/`](./LAYER-1/)
- ТЗ продукта (слой 2) → [`LAYER-2/`](./LAYER-2/)
- Память проекта → [`LAYER-3/`](./LAYER-3/)

**Документация по синхронизации шаблона:**
- [`LAYER-1/tools/template-sync.md`](./LAYER-1/tools/template-sync.md) — полная инструкция и интеграция
- [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md) — навигация по файлам шаблона

### Поддерживаемые AI-среды

- **Claude Code** → `CLAUDE.md`, `.claude/agents/*`
- **Cursor** → `.cursor/rules/*` и [`.cursor/CLAUDE-WORKFLOW.md`](./.cursor/CLAUDE-WORKFLOW.md) (ссылка на поток из [`CLAUDE.md`](./CLAUDE.md))
- **GitHub Copilot** → `.github/copilot-instructions.md`
- **Gemini** → `GEMINI.md`

Основной источник правил для всех сред — `LAYER-1/`, `LAYER-2/` и `LAYER-3/`. Tool-specific файлы только направляют AI, что читать.
