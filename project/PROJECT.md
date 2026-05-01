---
version: 0.1.0
stage: 01-interview
updated: 2026-04-26
---

# PROJECT.md — Единое ТЗ проекта

> Единственный источник истины по продукту в потоке **Claude Code** (`stages/*/BOOT.md`).  
> Каждый этап читает весь файл и дополняет **только свою секцию** (см. `LOCKED`).
> В исходном репозитории шаблона этот файл может быть пустым: он заполняется уже после копирования под конкретный проект.

## Как пользоваться

- Запуск этапа: скажи агенту прочитать соответствующий `stages/0X-*/BOOT.md`.
- Не хватает данных — агент пишет в тексте: `❓ НЕ ОПРЕДЕЛЕНО — что нужно уточнить` (без выдумывания).
- Закрытая секция: `LOCKED:true` — не редактировать без явного решения владельца.

<!-- SECTION:discovery OWNER:interview LOCKED:true -->
## 1. DISCOVERY

### Роли
- Владелец проекта: задаёт цель, подтверждает решения, принимает результат.
- Исполнитель через IDE: оформляет задачи, вносит изменения в проект, запускает проверки.
- AI-агент: помогает оформлять задачи, проверять структуру, подсказывать безопасный порядок работы.

### Процессы
- Идея сначала оформляется как описание задачи, затем при необходимости превращается в executable Task Contract.
- Изменения проходят через локальные проверки структуры, рисков и валидации файлов.
- Для установки в другой проект используется шаблон minimal или full через `install.sh`.
- Для проверки внешнего сценария используются smoke-test скрипты на временных git-проектах.

### Ограничения и контекст
- Проект — это набор guardrails: правил, шаблонов и проверок для других репозиториев, а не backend-приложение и не веб-сервис.
- Базовый сценарий использования: обычный git-проект получает файлы AgentOS, затем в нём запускаются проверки и рабочий процесс задач.
- Нельзя зависеть от RAG, vector DB, embeddings, marketplace-интеграций и сложной оркестрации агентов.
- Все изменения должны быть воспроизводимыми через локальные файлы и простые команды Bash/Python.
- Критичные для структуры зоны: `tasks/`, `reports/`, `schemas/`, `scripts/`, `templates/`, `docs/`, `examples/`.

<!-- END:discovery -->

<!-- SECTION:ux OWNER:ux LOCKED:false -->
## 2. UX

### Экраны
_не заполнено_

### Ключевые флоу
_не заполнено_

### Компоненты
_не заполнено_

<!-- END:ux -->

<!-- SECTION:specs OWNER:dev LOCKED:true -->
## 3. SPECS

### Стек
- Языки и форматы: Python, Bash, Markdown, JSON, YAML.
- Основные рабочие каталоги: `scripts/`, `schemas/`, `tasks/`, `reports/`, `templates/`, `docs/`, `examples/`.
- IDE и агентные конфиги: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `opencode.json`.
- Локальные механизмы проверки и контроля: `.githooks/`, GitHub workflow-файлы в `.github/workflows/`, JSON Schema-файлы в `schemas/`.
- Основные инструменты: shell-скрипты в `scripts/`, Python-валидаторы в `scripts/`, шаблоны задач и отчётов в `tasks/templates/` и `reports/templates/`.
- ❓ НЕ ОПРЕДЕЛЕНО — есть ли дополнительные IDE-конфиги вне `opencode.json` и текущих adapter-файлов.

### Архитектура
- Bootstrap-порядок агента задаётся только через `llms.txt`:
  1. `core-rules/MAIN.md`
  2. `state/MAIN.md`
  3. `workflow/MAIN.md`
  4. `quality/MAIN.md`
  5. `security/MAIN.md`
- Модульная runtime-структура:
  - `core-rules/MAIN.md` — приоритеты, границы, управление правилами.
  - `state/MAIN.md` — состояние, события, переходы, восстановление.
  - `workflow/MAIN.md` — порядок работы, рамки задачи, контроль scope.
  - `quality/MAIN.md` — проверки, smoke-test, критерии готовности.
  - `security/MAIN.md` — чувствительные данные, ограничения доступа, стоп-условия безопасности.
- Поддерживающие и вспомогательные модули:
  - `memory-bank/` — сохранение проектного контекста.
  - `handoff/` — передача состояния между сессиями.
  - `incidents/` — шаблоны инцидентов.
  - `lessons/` — зафиксированные уроки и правила на будущее.
- Навигационные и архитектурные документы:
  - `ROUTES-REGISTRY.md` — карта маршрутов и владельцев модулей.
  - `architecture/CANON.md` — архитектурный канон.
  - `architecture/MAIN.md` и `architecture/OPERATING-RULES.md` — поддерживающие архитектурные правила.

### Компоненты (реализованные)
- Runtime-модули: `core-rules/MAIN.md`, `quality/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `security/MAIN.md`.
- Навигация и входные точки: `llms.txt`, `START.md`, `README.md`, `ROUTES-REGISTRY.md`, `ARCHITECTURE.md`, `SYSTEM_PROMPT.md`, `CHECKLIST.md`, `FAQ.md`.
- Архитектурные документы: `architecture/CANON.md`, `architecture/MAIN.md`, `architecture/OPERATING-RULES.md`.
- Adapter-файлы и IDE-указатели: `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md`, `.github/instructions/backend.instructions.md`, `.github/instructions/frontend.instructions.md`, `opencode.json`.
- Хранилища состояния и знаний: `memory-bank/README.md`, `memory-bank/project-status.md`, `handoff/HANDOFF.md`, `handoff/templates/session-summary.md`, `incidents/templates/incident.md`, `lessons/lessons.md`, `lessons/templates/lesson-entry.md`.
- Схемы валидации: `schemas/task.schema.json`, `schemas/verification.schema.json`, `schemas/incident.schema.json`, `schemas/lessons.schema.json`, `schemas/handoff.schema.json`.
- Базовые проверки и скрипты: `scripts/validate-task.py`, `scripts/validate-verification.py`, `scripts/run-all.sh`, `scripts/check-dangerous-commands.py`, `scripts/check-risk.py`, `scripts/check-pr-quality.py`, `scripts/validate-commit-msg.py`, `scripts/validate-incident.py`, `scripts/validate-lessons.py`, `scripts/validate-handoff.py`, `scripts/generate-repo-map.py`, `scripts/select-context.py`, `scripts/install-hooks.sh`, `scripts/health-check.sh`, `scripts/validate-route.py`, `scripts/validate-docs.py`, `scripts/validate-architecture.sh`, `scripts/canonical-cleanup.sh`, `scripts/check-links.py`, `scripts/check-identity-drift.sh`, `scripts/check-llms-graph-files.sh`, `scripts/VALIDATORS.md`.
- Git и CI-компоненты: `.githooks/pre-commit`, `.githooks/commit-msg`, `.github/workflows/agentos-validation.yml`, `.github/workflows/doc-integrity.yml`, `.github/workflows/health.yml`, `.github/workflows/memory-sync.yml`, `.github/workflows/modular-validators.yml`, `.github/pull_request_template.md`.
- Packaging и примеры: `install.sh`, `requirements.txt`, `templates/agentos-minimal/`, `templates/agentos-full/`, `templates/commit-message.md`, `examples/simple-project/README.md`, `examples/simple-project/app.py`, `examples/simple-project/requirements.txt`, `examples/simple-project/run-example.sh`.
- Документация по использованию: `docs/quickstart.md`, `docs/usage.md`.
- Дополнительные generated/служебные артефакты: `repo-map.md`, `reports/verification.md`, `reports/templates/verification-report.md`, `tasks/active-task.md`, `tasks/templates/task-contract.md`, `project/PROJECT.md`.

### Open Task Briefs
- `tasks/task-20260426-brief-to-contract-manual-guide/TASK.md` — status: open

<!-- END:specs -->

<!-- SECTION:deploy OWNER:deploy LOCKED:false -->
## 4. DEPLOY

### Окружение
_не заполнено_

### Домены и сервисы
_не заполнено_

<!-- END:deploy -->

## 5. DECISIONS

_не заполнено_
