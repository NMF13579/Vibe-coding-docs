# AGENTS.md — точка входа для OpenCode

Этот файл читается OpenCode автоматически при старте сессии.

## Агент, читай в таком порядке

1. [`START.md`](START.md) — единый старт и модель шаблона.
2. [`llms.txt`](llms.txt) — карта репозитория и маршруты.
3. [`CLAUDE.md`](CLAUDE.md) — поведение агента в сессии.
4. [`LAYER-1/tools/adapters/OPENCODE-INTERVIEW-CONTROL.md`](LAYER-1/tools/adapters/OPENCODE-INTERVIEW-CONTROL.md) — адаптер интервью-протокола.

## Быстрый старт

Скажи агенту **«Начнём»** — он пройдёт `START.md` и `llms.txt`, затем запустит нужный маршрут.
