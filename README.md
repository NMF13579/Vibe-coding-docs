<!-- 
  🔍 SEARCH TAGS / ПОИСКОВЫЕ ТЕГИ
  EN: vibe coding, AI agent documentation, no-code, LLM workflow, Claude Code, Cursor IDE,
      medical IT, MVP template, AI-assisted development, prompt engineering, context management,
      agent orchestration, AI tools, project template, documentation framework
  RU: вайб-кодинг, документация для AI-агентов, без кода, шаблон проекта, управление контекстом,
      медицинские IT, MVP шаблон, разработка с ИИ, агентная разработка, Клод Код, Курсор
-->

<div align="center">

<img src="https://img.shields.io/badge/-%F0%9F%A7%A0%20Vibe--coding--docs-1a1a2e?style=for-the-badge&logoColor=white" height="50" alt="Vibe-coding-docs"/>

**AI-agent documentation template · from idea to MVP without chaos**  
*Шаблон документации для AI-агентов · от идеи до MVP без хаоса*

*For doctors, designers, managers — anyone building with AI, no deep coding required*  
*Для врачей, дизайнеров, менеджеров — всех, кто строит с ИИ без погружения в код*

<br/>

[![Stars](https://img.shields.io/github/stars/NMF13579/Vibe-coding-docs?style=flat-square&logo=github&label=stars)](https://github.com/NMF13579/Vibe-coding-docs/stargazers)
[![Forks](https://img.shields.io/github/forks/NMF13579/Vibe-coding-docs?style=flat-square&logo=github&label=forks)](https://github.com/NMF13579/Vibe-coding-docs/network)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](./LICENSE)
[![Topics](https://img.shields.io/badge/topics-vibe--coding_·_AI_·_no--code_·_LLM-555?style=flat-square)](#)

</div>

---

## 🚀 Quick Start · Быстрый старт

→ Начни с [START.md](./START.md)

---

> ⚠️ **Медицинский домен**
> Проект может использоваться в медицинских сценариях, но:
> — не является медицинским изделием
> — не заменяет врача и не даёт клинических назначений
> — требует human oversight для клинических решений
> — работа с данными пациентов требует отдельной legal/security проверки
>
> Подробнее: [LAYER-1/MEDICAL-SAFETY.md](./LAYER-1/MEDICAL-SAFETY.md)

---

## Статус проекта

`✅ Стабильная версия: v1.1.0 (готов к использованию)`

### 🔄 Что нового в v1.1.0

- GUI-онбординг для новичков: [`ONBOARDING-WIZARD.md`](./ONBOARDING-WIZARD.md)
- Юридический и security-контур: [`LEGAL-152FZ.md`](./LAYER-1/LEGAL-152FZ.md), prompt injection: [`security.md`](./LAYER-1/security.md), откат: [`error-handling.md`](./LAYER-1/error-handling.md) («Процедура отката»)
- Learning loop и инциденты: [`LEARNING-LOOP.md`](./LEARNING-LOOP.md), [`incidents/incident-template.md`](./incidents/incident-template.md)
- Архитектура и глоссарий: [`ARCHITECTURE.md`](./ARCHITECTURE.md), [`GLOSSARY.md`](./GLOSSARY.md)

---

### Ключевые материалы

- Архитектура фреймворка: [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- Глоссарий для не-технических ролей: [`GLOSSARY.md`](./GLOSSARY.md)

### GUI-поток запуска (без терминала)

1. Открой папку проекта в Cursor/Claude Code.
2. Открой в корне [`START.md`](./START.md) и выбери в таблице строку под свою роль.
3. Перейди по ссылке «Куда идти» — дальнейшие шаги описаны в том документе.
4. Если ты уже пользователь IDE и нужен готовый текст для агента — открой [`QUICK-START.md`](./QUICK-START.md), шаг 2 (шаблон промпта).
5. Нажми **Run** (где применимо) и подтверди предложенный следующий шаг.

Для продвинутой кастомизации (LLM, `.cursor/`, `.claude/`, MCP, CLI):  
[`ADVANCED-SETUP.md`](./ADVANCED-SETUP.md)

---

## 📚 Навигация по документации

- Быстрый онбординг: [`ONBOARDING-WIZARD.md`](./ONBOARDING-WIZARD.md)
- Базовый GUI-старт: [`QUICK-START.md`](./QUICK-START.md)
- Продвинутая настройка: [`ADVANCED-SETUP.md`](./ADVANCED-SETUP.md)
- Релизный чеклист: [`CHECKLIST.md`](./CHECKLIST.md)
- Цикл обучения на инцидентах: [`LEARNING-LOOP.md`](./LEARNING-LOOP.md)
- Шаблон записи инцидента: [`incidents/incident-template.md`](./incidents/incident-template.md)
- Адаптация под другой домен: [`DOMAIN-ADAPTER.md`](./DOMAIN-ADAPTER.md)
- Архитектурная схема: [`ARCHITECTURE.md`](./ARCHITECTURE.md)
- Глоссарий терминов: [`GLOSSARY.md`](./GLOSSARY.md)

## 👤 Choose your role · Выбери свою роль

<div align="center">

| | Role / Роль | Path / Путь |
|:---:|:---|:---|
| [![](https://img.shields.io/badge/🔰_First_time_·_Первый_раз-2ea44f?style=flat-square)](./START.md) | No coding or agent experience / Нет опыта с кодом | [START.md](./START.md) → [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) |
| [![](https://img.shields.io/badge/🩺_Doctor_·_Врач-e05c00?style=flat-square)](./START.md) | Automate clinical routine or build medical service / Медицинский сервис | [START.md](./START.md) → [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) → [MEDICAL-SAFETY.md](./LAYER-1/MEDICAL-SAFETY.md) |
| [![](https://img.shields.io/badge/🎨_Designer_·_Дизайнер-8b44ac?style=flat-square)](./START.md) | Product idea, want prototype without code / Прототип без кода | [START.md](./START.md) → [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) → [interview-system.md](./LAYER-1/interview-system.md) |
| [![](https://img.shields.io/badge/📋_Manager_·_Менеджер-d4ac0d?style=flat-square)](./START.md) | Validate idea and reach MVP fast / Идея → MVP быстро | [START.md](./START.md) → [QUICK-START-NOVICE.md](./QUICK-START-NOVICE.md) → [PROJECT.md](./project/PROJECT.md) |
| [![](https://img.shields.io/badge/🔁_Lost_context_·_Потерял_контекст-c0392b?style=flat-square)](./START.md) | Project exists but something went wrong / Что-то пошло не так | [START.md](./START.md) → [STATE.md](./LAYER-3/STATE.md) → [HANDOFF.md](./HANDOFF.md) |
| [![](https://img.shields.io/badge/🛠️_Developer_·_Разработчик-0366d6?style=flat-square)](./START.md) | Know the basics, want to customize the agent / Настроить агента | [START.md](./START.md) → [QUICK-START.md](./QUICK-START.md) |
| [![](https://img.shields.io/badge/🤖_Claude_Code-1a1a2e?style=flat-square)](./START.md) | Run project in stages: interview → UX → deploy / По этапам | [START.md](./START.md) → [CLAUDE-CODE-FLOW.md](./CLAUDE-CODE-FLOW.md) → [BOOT.md](./stages/01-interview/BOOT.md) |

</div>

---

## ⚡ Installation · Установка

Installation uses stable **main** branch. **dev** branch is for development.

```bash
curl -fsSL https://raw.githubusercontent.com/NMF13579/Vibe-coding-docs/main/install.sh | bash
```

> Or click **[Use this template](https://github.com/NMF13579/Vibe-coding-docs/generate)** — no terminal needed.  
> *Или нажми Use this template — без терминала.*

---

## 💬 Agent Commands · Команды агента

<div align="center">

| Command / Команда | Action / Действие |
|:---:|:---|
| [![](https://img.shields.io/badge/Start_·_Начнём-2ea44f?style=flat-square)](./START.md) | Launch a new project / Запустить новый проект |
| [![](https://img.shields.io/badge/Restore_context_·_Восстанови_контекст-0366d6?style=flat-square)](./HANDOFF.md) | Resume an existing project session / Начать сессию по существующему проекту |
| [![](https://img.shields.io/badge/Save_context_·_Сохрани_контекст-5c6bc0?style=flat-square)](./HANDOFF.md) | End session without losing progress / Закончить сессию без потерь |
| [![](https://img.shields.io/badge/Everything_broke_·_Всё_сломалось-c0392b?style=flat-square)](./LAYER-1/error-handling.md) | Roll back changes when something went wrong / Откатить изменения |
| [![](https://img.shields.io/badge/Check_release_readiness_·_Проверь_готовность-e67e22?style=flat-square)](./LAYER-1/audit.md) | Final check before deploy / Финальная проверка перед деплоем |

</div>

---

## 🗂️ Docs Map · Карта документов

<div align="center">

| Situation / Ситуация | Document / Документ |
|:---|:---:|
| Brand new? / Совсем новый? | [START.md](./START.md) → [![](https://img.shields.io/badge/QUICK--START--NOVICE-2ea44f?style=flat-square)](./QUICK-START-NOVICE.md) |
| Developer setup / Технический старт | [START.md](./START.md) → [![](https://img.shields.io/badge/QUICK--START-0366d6?style=flat-square)](./QUICK-START.md) · [![](https://img.shields.io/badge/ADVANCED--SETUP-555?style=flat-square)](./ADVANCED-SETUP.md) |
| Agent entry point / Точка входа агента | [![](https://img.shields.io/badge/llms.txt-555?style=flat-square)](./llms.txt) [![](https://img.shields.io/badge/HANDOFF-0366d6?style=flat-square)](./HANDOFF.md) |
| Claude Code stage flow / Флоу по этапам | [![](https://img.shields.io/badge/CLAUDE--CODE--FLOW-1a1a2e?style=flat-square)](./CLAUDE-CODE-FLOW.md) [![](https://img.shields.io/badge/BOOT.md-555?style=flat-square)](./stages/01-interview/BOOT.md) |
| Where did we stop? / Где остановились? | [![](https://img.shields.io/badge/HANDOFF-0366d6?style=flat-square)](./HANDOFF.md) [![](https://img.shields.io/badge/project--status-555?style=flat-square)](./LAYER-3/project-status.md) |
| Scope is creeping / Задача расползается | [![](https://img.shields.io/badge/scope--guard-e67e22?style=flat-square)](./LAYER-1/scope-guard.md) |
| Onboarding для новичков | [![](https://img.shields.io/badge/ONBOARDING--WIZARD-2ea44f?style=flat-square)](./ONBOARDING-WIZARD.md) |
| Medical / границы ИИ | [![](https://img.shields.io/badge/MEDICAL--SAFETY-e05c00?style=flat-square)](./LAYER-1/MEDICAL-SAFETY.md) |
| 152-ФЗ и мед-комплаенс | [![](https://img.shields.io/badge/LEGAL--152FZ-e05c00?style=flat-square)](./LAYER-1/LEGAL-152FZ.md) |
| Prompt injection безопасность | [![](https://img.shields.io/badge/security_·_prompts-c0392b?style=flat-square)](./LAYER-1/security.md) |
| Learning loop по инцидентам | [![](https://img.shields.io/badge/LEARNING--LOOP-5c6bc0?style=flat-square)](./LEARNING-LOOP.md) |
| Domain adapter | [![](https://img.shields.io/badge/DOMAIN--ADAPTER-8b44ac?style=flat-square)](./DOMAIN-ADAPTER.md) |
| Архитектура фреймворка | [![](https://img.shields.io/badge/ARCHITECTURE-0366d6?style=flat-square)](./ARCHITECTURE.md) |
| Глоссарий терминов | [![](https://img.shields.io/badge/GLOSSARY-555?style=flat-square)](./GLOSSARY.md) |
| Everything confused / Всё перепуталось | [![](https://img.shields.io/badge/context--recovery-c0392b?style=flat-square)](./LAYER-1/context-recovery.md) |
| Roll back changes / Откатить изменения | [![](https://img.shields.io/badge/error--handling-c0392b?style=flat-square)](./LAYER-1/error-handling.md) |
| Roadmap & planning / Дорожная карта | [![](https://img.shields.io/badge/roadmap-8b44ac?style=flat-square)](./LAYER-2/specs/roadmap.md) |
| Changelog / История изменений | [![](https://img.shields.io/badge/CHANGELOG-555?style=flat-square)](./CHANGELOG.md) |
| Project audit / Аудит проекта | [![](https://img.shields.io/badge/audit-e05c00?style=flat-square)](./LAYER-1/audit.md) [![](https://img.shields.io/badge/audit--checklist-e05c00?style=flat-square)](./LAYER-1/audit.md) |

</div>

---

## 🤖 Supported AI Tools · Поддерживаемые среды

<div align="center">

[![Claude Code](https://img.shields.io/badge/Claude_Code-1a1a2e?style=for-the-badge&logo=anthropic&logoColor=white)](./CLAUDE.md)
[![Cursor](https://img.shields.io/badge/Cursor-0366d6?style=for-the-badge&logoColor=white)](./QUICK-START.md)
[![GitHub Copilot](https://img.shields.io/badge/GitHub_Copilot-238636?style=for-the-badge&logo=github&logoColor=white)](./.github/copilot-instructions.md)
[![Lovable](https://img.shields.io/badge/Lovable-e05c00?style=for-the-badge&logoColor=white)](./LAYER-1/system-prompt.md)
[![Bolt](https://img.shields.io/badge/Bolt-8b44ac?style=for-the-badge&logoColor=white)](./LAYER-1/system-prompt.md)

</div>

| IDE / Среда | Файл конфигурации | Уровень поддержки |
|---|---|---|
| Claude Code | [CLAUDE.md](./CLAUDE.md), [.claude/](./.claude/) | ✅ Полная |
| Cursor | [.cursor/rules/](./.cursor/rules/) | ✅ Полная |
| GitHub Copilot | [copilot-instructions.md](./.github/copilot-instructions.md) | ✅ Полная |
| OpenCode | [opencode.json](./opencode.json) | ⚠️ Базовая |
| Gemini | [GEMINI.md](./GEMINI.md) | ⚠️ Минимальная |
| Lovable / Bolt | [system-prompt.md](./LAYER-1/system-prompt.md) | ⚠️ Через system prompt |

---

## 📐 Agent Principles · Принципы агента

- 🚫 **No code without a confirmed plan** · *Агент не пишет код без подтверждённого плана*
- 💬 **One question at a time** · *Один вопрос за раз — агент не засыпает списком*
- 📄 **Documents get filled in**, not left as empty templates · *Документы заполняются, не остаются пустыми шаблонами*
- 🛡️ `roadmap.md` **protects against scope creep** · *Защищает от расползания проекта*
- 🔒 `decisions.md` **stops re-discussing settled decisions** · *Останавливает повторное обсуждение*

---

<div align="center">

Made with ❤️ for vibe-coders · *Сделано для вайб-кодеров*

[![Issues](https://img.shields.io/badge/Issues-c0392b?style=flat-square&logo=github&logoColor=white)](https://github.com/NMF13579/Vibe-coding-docs/issues)
[![Discussions](https://img.shields.io/badge/Discussions-0366d6?style=flat-square&logo=github&logoColor=white)](https://github.com/NMF13579/Vibe-coding-docs/discussions)
[![Use Template](https://img.shields.io/badge/Use_this_template-238636?style=flat-square&logo=github&logoColor=white)](https://github.com/NMF13579/Vibe-coding-docs/generate)

</div>
