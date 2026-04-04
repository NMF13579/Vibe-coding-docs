# DEPLOY-MCP-UNIVERSAL — Универсальный деплой через MCP

> Этот файл описывает универсальную настройку автодеплоя через MCP-серверы.
> Работает в Cursor, Claude Code, Windsurf, Cline, VS Code — без изменений в логике.
> Кладётся в репозиторий как `docs/deploy/DEPLOY-MCP-UNIVERSAL.md`.

---

## Принцип: один конфиг — все окружения

MCP (Model Context Protocol) — открытый стандарт, принятый Anthropic, OpenAI, Google
и переданный в Linux Foundation в декабре 2025.
Один и тот же MCP-сервер работает везде — меняется только путь к конфиг-файлу.

| Инструмент | Путь к конфигу |
|---|---|
| **Cursor** | `.cursor/mcp.json` (проектный) или `~/.cursor/mcp.json` (глобальный) |
| **Claude Code** | `.mcp.json` в корне проекта или `~/.claude/mcp.json` |
| **Windsurf** | `~/.codeium/windsurf/mcp_config.json` |
| **Cline (VS Code)** | настройки расширения Cline → MCP Servers |
| **Claude Desktop** | `~/Library/Application Support/Claude/claude_desktop_config.json` |

> Содержимое конфига — **одинаковое** для всех. Меняется только где лежит файл.

---

## Универсальный конфиг `mcp.json`

Создай этот файл в `.cursor/mcp.json` (Cursor) или `.mcp.json` (Claude Code).
Для других окружений — скопируй содержимое в соответствующий путь из таблицы выше.

```json
{
  "mcpServers": {

    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ВАШ_GITHUB_TOKEN"
      }
    },

    "timeweb": {
      "command": "npx",
      "args": ["-y", "@timeweb/mcp-server"],
      "env": {
        "TIMEWEB_API_TOKEN": "ВАШ_TIMEWEB_TOKEN"
      }
    },

    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/путь/к/вашему/проекту"
      ]
    }

  }
}
```

> Минимальный набор: `github` + `timeweb` + `filesystem`.
> Этого достаточно для полного цикла: код → push → деплой → логи.

---

## Что делает каждый MCP-сервер

| Сервер | Что агент может делать |
|---|---|
| `github` | читать/создавать PR, issues, ветки, коммиты, запускать Actions |
| `timeweb` | деплоить на App Platform, читать логи, перезапускать приложение |
| `filesystem` | читать и писать файлы проекта напрямую |

---

## Как получить токены

### GitHub Token
1. Открыть [github.com/settings/tokens](https://github.com/settings/tokens)
2. Нажать «Generate new token (classic)»
3. Выбрать права: `repo`, `workflow`, `read:org`
4. Скопировать токен → вставить в конфиг

### Timeweb Token
1. Открыть [timeweb.cloud](https://timeweb.cloud) → Настройки аккаунта → API
2. Создать API-ключ
3. Скопировать → вставить в конфиг

> ⚠️ Токены не коммитить в репозиторий.
> Конфиг с токенами добавь в `.gitignore`:
> ```
> .cursor/mcp.json
> .mcp.json
> ```
> Вместо этого создай `.cursor/mcp.example.json` без токенов — его коммитишь.

---

## Установка по окружениям

### Cursor
```bash
# Создать папку если нет
mkdir -p .cursor

# Создать конфиг
cp .cursor/mcp.example.json .cursor/mcp.json
# Вставить токены в .cursor/mcp.json вручную
```
Затем: `Cursor Settings → MCP → перезагрузить`.

### Claude Code (терминал)
```bash
# Добавить GitHub MCP
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Добавить Timeweb MCP
claude mcp add timeweb -- npx -y @timeweb/mcp-server

# Или через проектный .mcp.json (шарится с командой)
claude mcp add --scope project github -- npx -y @modelcontextprotocol/server-github
```

### Windsurf
Скопировать содержимое `mcp.json` в:
```
~/.codeium/windsurf/mcp_config.json
```
Перезапустить Windsurf.

### Cline (расширение VS Code)
Расширение Cline → иконка MCP Servers → Add Server → вставить JSON-блок сервера.

---

## Команды агенту после настройки

После настройки MCP говори агенту естественным языком:

```
"Задеплой текущую ветку на Timeweb"
"Посмотри логи последнего деплоя"
"Создай PR из текущей ветки в main"
"Перезапусти приложение на Timeweb"
"Покажи статус деплоя"
```

Агент сам читает `docs/deploy/DEPLOY-CHECKLIST-TIMEWEB.md`
перед деплоем, если добавить в `AGENT-CONTRACT.md` блок ниже.

---

## Блок для AGENT-CONTRACT.md

Добавь этот блок в `AGENT-CONTRACT.md` в раздел про деплой:

```markdown
## Деплой

- Всегда делаем через MCP-серверы — не вручную через браузер.
- Перед деплоем проверяй `docs/deploy/DEPLOY-CHECKLIST-TIMEWEB.md`.
- После деплоя фиксируй результат в `docs/deploy/RELEASE-NOTES.md`.
- Post-launch review — в `docs/POST-LAUNCH-REVIEW.md`.
- Если что-то пошло не так — записывай в `docs/deploy/RUNBOOK.md`.
```

---

## Структура файлов деплоя в репозитории

```
.cursor/
  mcp.example.json        ← коммитишь (без токенов)
  mcp.json                ← НЕ коммитишь (с токенами, в .gitignore)

.mcp.json                 ← для Claude Code (НЕ коммитишь)

docs/deploy/
  DEPLOY-CHECKLIST-TIMEWEB.md   ← чеклист деплоя
  DEPLOY-MCP-UNIVERSAL.md       ← этот файл
  RELEASE-NOTES.md              ← лог релизов
  RUNBOOK.md                    ← что делать если что-то сломалось
```

---

## Расширение стека (опционально)

Если нужно больше возможностей — добавить в `mcp.json`:

| Сервер | Когда добавлять |
|---|---|
| `@vercel/mcp-adapter` | если деплоишь на Vercel вместо Timeweb |
| `@deployhq/mcp` | если нужен деплой на несколько серверов сразу |
| `@modelcontextprotocol/server-postgres` | если нужна работа с БД из агента |
| `@modelcontextprotocol/server-brave-search` | если агент должен искать решения в вебе |

Полный каталог MCP-серверов: [mcpbundles.com](https://mcpbundles.com),
[vibehackers.io/blog/best-mcp-servers](https://vibehackers.io/blog/best-mcp-servers)
