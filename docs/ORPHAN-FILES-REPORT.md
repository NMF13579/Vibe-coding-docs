# ORPHAN-FILES-REPORT — файлы без входящих ссылок из ключевой навигации

Проверено относительно файлов: `CLAUDE.md`, `START.md`, `AGENT-CONTRACT.md`, `docs/DOCS-MAP.md`.

> Обновлено: 2026-04-10 (добавлены корневые файлы, дополнительные docs/ и memory-bank/ файлы, не попавшие в предыдущую версию отчёта).

---

## Корневые файлы

| Файл | Для чего (предположение) | Рекомендация |
|------|--------------------------|--------------|
| `AGENT-CONTRACT.md` | Контракт MVP-пайплайна; упомянут в START.md, но не в CLAUDE.md routing | Упомянуть в CLAUDE.md (раздел «Маршрутизация») |
| `CHANGELOG.md` | История изменений шаблона | Добавить ссылку в README.md |
| `GEMINI.md` | Адаптер для Gemini; есть `docs/adapters/GEMINI-INTERVIEW-CONTROL.md`, но входная точка не явная | Добавить в CLAUDE.md как альтернативный routing-файл |
| `INDEX.md` | Навигационный индекс; упомянут в README.md | Оценить полезность vs DOCS-MAP.md |
| `QUICK-START.md` | Быстрый старт для владельца; не в routing | Добавить ссылку в README.md или START.md |
| `README-PLACEMENT.md` | Карта размещения interview-агентов | Добавить ссылку в START.md (секция кросс-IDE) |
| `SYSTEM_PROMPT.md` | Системный промпт; упомянут в CLAUDE.md «Приоритет источников» | ОК: упоминание есть, ссылка не обязательна |
| `TEMPLATE-SYNC-GUIDE.md` | Инструкция синхронизации шаблона | Добавить ссылку в README.md |
| `TEMPLATE-SYNC-INTEGRATION.md` | Интеграция синхронизации | Добавить ссылку рядом с TEMPLATE-SYNC-GUIDE.md |

---

## docs/ — документы без входящих ссылок

| Файл | Размер | Для чего (предположение) | Рекомендация |
|------|--------|--------------------------|--------------|
| `docs/AGENTS.md` | 2394 B | Карта ролей агентов и правила совместной работы | Добавить ссылку в CLAUDE.md (раздел «Использование subagents») |
| `docs/AUDIT-CHECKLIST.md` | 9772 B | Подробный чеклист аудита проекта | Добавить ссылку в docs/AUDIT-GUIDE.md |
| `docs/ENV.md` | 4086 B | Универсальные правила по переменным окружения | Добавить ссылку в docs/deploy/ENV-SETUP.md |
| `docs/MONITORING.md` | 3965 B | Мониторинг после релиза и критерии инцидента | Добавить ссылку в docs/POST-LAUNCH-REVIEW.md |
| `docs/TASK-TEMPLATE.md` | 1450 B | Шаблон формулировки задач для работы с агентом | Добавить ссылку в tasks/README.md |
| `docs/USER-FLOWS.md` | — | Пользовательские сценарии (generic-пример); не в docs/ux/ | Переместить в docs/ux/ или пометить как шаблон-инструкция |
| `docs/cheatsheet.html` | 30067 B | Визуальная шпаргалка владельца | Добавить ссылку в README.md или docs/OWNER-CHEATSHEET.md |

---

## docs/deploy/ — без входящих ссылок

| Файл | Для чего | Рекомендация |
|------|----------|--------------|
| `docs/deploy/DEPLOY-MCP-UNIVERSAL.md` | Универсальный деплой через MCP | Добавить ссылку в docs/DEPLOY.md или AGENT-CONTRACT.md |
| `docs/deploy/DEPLOY-TIMEWEB.md` | Пошаговый деплой на Timeweb | Добавить ссылку в docs/platforms/timeweb-cloud.md |
| `docs/deploy/MCP-SETUP.md` | Настройка MCP для деплоя | Добавить ссылку в DEPLOY-MCP-UNIVERSAL.md |

---

## docs/platforms/ — без входящих ссылок

| Файл | Для чего | Рекомендация |
|------|----------|--------------|
| `docs/platforms/vercel.md` | Инструкция деплоя на Vercel | Добавить ссылку в docs/DEPLOY.md (уже есть в DOCS-MAP.md) |

---

## docs/standards/ — UX-чеклисты без входящих ссылок

Все чеклисты доступны через `docs/standards/UX-CHECKLIST-INDEX.md` (входная точка для агента).
Ниже — те, у которых нет ссылки даже из INDEX.md.

| Файл | Для чего | Рекомендация |
|------|----------|--------------|
| `docs/standards/UX-CHECKLIST-DASHBOARDS.md` | UX-проверка для дашбордов | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-EMPTY-STATES.md` | UX-проверка пустых состояний | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-FALLBACK-RULES.md` | UX-правила fallback-сценариев | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-HELP-AND-SUPPORT.md` | UX-чеклист помощи и поддержки | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-HISTORY-AND-AUDIT.md` | UX-чеклист истории и аудита действий | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-LEGEND.md` | Легенда и обозначения UX-чеклистов | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-MICROCOPY.md` | UX-проверка текстов интерфейса | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-MINIMAL.md` | Укороченный UX-чеклист для быстрого прохода | Уточнить у владельца |
| `docs/standards/UX-CHECKLIST-NOTIFICATIONS.md` | UX-проверка уведомлений | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-ONBOARDING.md` | UX-чеклист первого входа в продукт | Уже добавлен в INDEX.md ✅ |
| `docs/standards/UX-CHECKLIST-PERMISSIONS-AND-ACCESS.md` | UX-чеклист ролей и прав доступа | Уже добавлен в INDEX.md ✅ |
| `docs/standards/UX-CHECKLIST-ROLE-BASED-UX.md` | UX-проверка сценариев по ролям | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-SEARCH-FILTERS.md` | UX-проверка поиска и фильтров | Добавить в INDEX.md |
| `docs/standards/UX-CHECKLIST-STARTER-FLOW.md` | UX-чеклист стартового пути | Уже добавлен в INDEX.md ✅ |
| `docs/standards/UX-CHECKLIST-TABLES-AND-BULK-ACTIONS.md` | UX-проверка таблиц и массовых действий | Добавить в INDEX.md |

---

## memory-bank/ — без входящих ссылок из ключевой навигации

| Файл | Для чего | Рекомендация |
|------|----------|--------------|
| `memory-bank/PROJECT-MEMORY.md` | Долгая память проекта; упомянут в CONTEXT-LOSS-RECOVERY.md | Добавить упоминание в CLAUDE.md (автозапуск) |
| `memory-bank/atomic-decisions.md` | Атомарные решения | Добавить ссылку в memory-bank/index-memory-bank.md |
| `memory-bank/index-memory-bank.md` | Индекс memory-bank | Добавить ссылку в CLAUDE.md или README.md |
| `memory-bank/open-ui-questions.md` | Открытые UX-вопросы | Добавить ссылку в docs/ux/UX-GAP-REPORT.md |
| `memory-bank/project-context-draft.md` | Устаревший редирект → interview-session.md | Можно удалить или оставить как stub |
| `memory-bank/ui-inventory.md` | Инвентарь UI-компонентов | Добавить ссылку в docs/TASK-REVIEW-PROTOCOL.md (Блок 1.5) |
