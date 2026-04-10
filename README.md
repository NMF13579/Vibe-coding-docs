# Vibe-coding-docs

> Шаблон документации для работы с AI-агентами: от идеи до MVP без хаоса и потери контекста.  
> Создан для вайб-кодеров — врачей, дизайнеров, менеджеров и всех, кто строит продукты с ИИ без глубокого погружения в код.

---

<div align="center">

[![Я новичок — начать здесь](https://img.shields.io/badge/🔰_Я_новичок_—_начать_здесь-2ea44f?style=for-the-badge)](./QUICK-START-NOVICE.md)
[![Я разработчик](https://img.shields.io/badge/🛠_Я_разработчик-0366d6?style=for-the-badge)](./QUICK-START.md)
[![FAQ](https://img.shields.io/badge/❓_Частые_вопросы-6e40c9?style=for-the-badge)](./FAQ.md)

[![Use this template](https://img.shields.io/badge/use%20this%20template-238636?style=flat-square&logo=github)](https://github.com/NMF13579/Vibe-coding-docs/generate)
[![Documentation](https://img.shields.io/badge/docs-DOCS--MAP-0366d6?style=flat-square&logo=readthedocs)](./LAYER-1/tools/template-sync-index.md)

</div>

---

## Что это такое

Этот репозиторий — рабочий шаблон, который помогает:

- запускать новый проект структурированно, не теряя мысли;
- сохранять контекст между сессиями — агент «помнит», где остановились;
- фиксировать задачи, решения и статус проекта;
- работать с AI-агентами предсказуемо, по правилам, а не «как получится».

---

## С чего начать — выбери свою роль

| Роль | Ситуация | Твой путь |
|---|---|---|
| 🔰 Первый раз | Нет опыта с кодом и агентами | [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) — 3 шага без терминала |
| 🩺 Врач / медик | Хочу автоматизировать рутину или сделать медицинский сервис | [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) → [`LAYER-1/ux-checklist-medical.md`](./LAYER-1/ux-checklist-medical.md) |
| 🎨 Дизайнер / творческий | Есть идея продукта, хочу прототип без кода | [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) → [`LAYER-1/interview-system.md`](./LAYER-1/interview-system.md) |
| 📋 Менеджер / предприниматель | Хочу проверить идею и дойти до MVP быстро | [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) → [`project/PROJECT.md`](./project/PROJECT.md) |
| 🔁 Уже начал, потерял контекст | Проект есть, но что-то пошло не так | [`HANDOFF.md`](./HANDOFF.md) → [`LAYER-1/context-recovery.md`](./LAYER-1/context-recovery.md) → [`FAQ.md`](./FAQ.md) |
| 🛠️ Разработчик | Понимаю базу, хочу настроить агента под себя | [`QUICK-START.md`](./QUICK-START.md) → [`CLAUDE.md`](./CLAUDE.md) → [`LAYER-1/workflow.md`](./LAYER-1/workflow.md) |

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

<details>
<summary>📂 Куда смотреть дальше — полная карта документов</summary>

| Ситуация | Документ |
|---|---|
| Совсем новый? Начни здесь | [`QUICK-START-NOVICE.md`](./QUICK-START-NOVICE.md) — без терминала |
| Технический старт | [`QUICK-START.md`](./QUICK-START.md) — для разработчиков |
| Точка входа для агента | [`llms.txt`](./llms.txt) → [`HANDOFF.md`](./HANDOFF.md) |
| Claude Code: одно ТЗ + этапы | [`README-NEW-ARCHITECTURE.md`](./README-NEW-ARCHITECTURE.md) → [`project/PROJECT.md`](./project/PROJECT.md) → [`stages/01-interview/BOOT.md`](./stages/01-interview/BOOT.md) |
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
| Аудит проекта | [`LAYER-1/audit.md`](./LAYER-1/audit.md), [`LAYER-1/audit-checklist.md`](./LAYER-1/audit-checklist.md) |
| Процессы и UX (spec-driven) | [`LAYER-1/agent-contract.md`](./LAYER-1/agent-contract.md) |

</details>

<details>
<summary>⚙️ Вставить в настройки AI-инструмента</summary>

Для лучшей работы агента вставь содержимое [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md) в системный промпт своего инструмента:

| Инструмент | Куда вставить |
|---|---|
| Cursor | Settings → Rules for AI |
| Claude Code | `CLAUDE.md` уже в корне — всё готово |
| Lovable | Knowledge → System Instructions |
| Bolt | Project Settings → AI Instructions |
| Gemini | Используй [`GEMINI.md`](./GEMINI.md) |

</details>

<details>
<summary>🔧 Для продвинутой настройки</summary>

Если хочешь детальнее настроить поведение агента или понять внутреннюю логику:

- Правила агента → [`CLAUDE.md`](./CLAUDE.md)
- Системный промпт → [`LAYER-1/system-prompt.md`](./LAYER-1/system-prompt.md)
- Карта ролей агентов → [`LAYER-1/agents.md`](./LAYER-1/agents.md)
- Инструкции агента (слой 1) → [`LAYER-1/`](./LAYER-1/)
- ТЗ продукта (слой 2) → [`LAYER-2/`](./LAYER-2/)
- Память проекта → [`LAYER-3/`](./LAYER-3/)

**Документация по синхронизации шаблона:**
- [`LAYER-1/tools/template-sync.md`](./LAYER-1/tools/template-sync.md) — полная инструкция
- [`LAYER-1/tools/template-sync-index.md`](./LAYER-1/tools/template-sync-index.md) — навигация по файлам

**Поддерживаемые AI-среды:**
- **Claude Code** → `CLAUDE.md`, `.claude/agents/*`
- **Cursor** → `.cursor/rules/*` и [`.cursor/CLAUDE-WORKFLOW.md`](./.cursor/CLAUDE-WORKFLOW.md)
- **GitHub Copilot** → `.github/copilot-instructions.md`
- **Gemini** → `GEMINI.md`

</details>

<details>
<summary>📐 Принципы работы агента</summary>

- Агент не пишет код без подтверждённого плана.
- Один вопрос за раз — агент не засыпает списком.
- Документы заполняются, не остаются пустыми шаблонами.
- `LAYER-2/specs/roadmap.md` защищает от расползания проекта.
- `LAYER-2/specs/decisions.md` останавливает повторное обсуждение уже принятых решений.

</details>
