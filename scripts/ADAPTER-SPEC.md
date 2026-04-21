# ADAPTER-SPEC — issue codes (validator v1.2.1)

Единый справочник кодов для людей и инструментов. **Коды и смысл совпадают** с полем `"code"` в JSON-выводе `scripts/validate-adapters.sh` (тот же набор, что в ассоциативных массивах `LEAK_PATTERNS` и ветках `add_issue`).

**Валидатор:** `scripts/validate-adapters.sh`  
**Авто-фикс по отчёту:** `scripts/fix-adapters.sh` — обрабатывает только коды с `auto_fixable: true` в JSON (см. колонку ниже).

**Ссылки в репозитории:** корневые адаптеры должны указывать на этот файл как на **`scripts/ADAPTER-SPEC.md`** (в Cursor rules допускается нотация `@scripts/ADAPTER-SPEC.md` — тот же путь для IDE).

---

## Что проверяется (пути)

### Обязательные файлы (`REQUIRED_ADAPTERS`)

| key | path |
|-----|------|
| cursor | `.cursor/rules/governed-repo.mdc` |
| copilot | `.github/copilot-instructions.md` |
| agents | `AGENTS.md` |
| zed | `.rules` |

Если файл отсутствует → **`REQUIRED_ADAPTER_MISSING`**. Если есть → полная проверка редиректов, мета-тегов и утечек.

### Опциональные файлы (`OPTIONAL_ADAPTERS`)

Если файл **существует**, валидатор выдаёт **`OPTIONAL_ADAPTER_PRESENT`** (warning) и затем ту же проверку, что для required:

| key | path |
|-----|------|
| claude | `CLAUDE.md` |
| gemini | `GEMINI.md` |
| windsurf_rules | `.windsurf/rules` |
| agents_override | `AGENTS.override.md` |

### Конфликт Zed-совместимых инструкций

Если существует **более одного** файла из списка `ZED_COMPAT`:

`.cursorrules`, `.windsurfrules`, `.clinerules`, `.github/copilot-instructions.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`

→ **`ZED_COMPAT_CONFLICT`** (warning).

---

## Правила проверки (кратко)

1. В каждом проверяемом файле должны встречаться строки с **`llms.txt`** и **`LAYER-1/agent-rules.md`** (редирект после bootstrap).
2. Желательные HTML-комментарии в начале (первые строки): `ROLE: ADAPTER ENTRYPOINT`, `AUTHORITY: NON-AUTHORITY`, `SOURCE_OF_TRUTH: no` — иначе коды **`MISSING_META_*`**.
3. Запрещённые вхождения (регистронезависимо, см. `LEAK_PATTERNS` в скрипте): ссылки на внутренние governance-доки и шаблоны конкурирующего bootstrap — коды **`ADAPTER_*_LEAK`**, **`ALT_BOOTSTRAP_LANGUAGE`**, **`COMPETING_ROUTING_LIST`**.

---

## Таблица кодов

| Code | Enforcement | Severity | auto_fixable | fix_type | Эмиттер в `validate-adapters.sh` |
|------|---------------|----------|--------------|----------|----------------------------------|
| REQUIRED_ADAPTER_MISSING | hard | error | false | — | отсутствует required path |
| MISSING_LLMS_REDIRECT | hard | error | true | insert | `check_redirect` / `validate_adapter` |
| MISSING_AGENT_RULES_REDIRECT | hard | error | true | insert | `check_agent_rules` |
| MISSING_META_ROLE | soft | warning | true | insert | `check_meta` ROLE |
| MISSING_META_AUTHORITY | soft | warning | true | insert | `check_meta` AUTHORITY |
| MISSING_META_SOT | soft | warning | true | insert | `check_meta` SOURCE_OF_TRUTH |
| ADAPTER_STATE_LEAK | hard | error | false | — | `LEAK_PATTERNS` STATE |
| ADAPTER_HANDOFF_LEAK | hard | error | false | — | `LEAK_PATTERNS` HANDOFF |
| ADAPTER_DECISIONS_LEAK | hard | error | false | — | `LEAK_PATTERNS` DECISIONS |
| ADAPTER_INTENT_LEAK | hard | error | false | — | `LEAK_PATTERNS` INTENT |
| ADAPTER_LAYER2_LEAK | hard | error | false | — | `LEAK_PATTERNS` LAYER-2 |
| ALT_BOOTSTRAP_LANGUAGE | hard | error | false | — | `LEAK_PATTERNS` |
| COMPETING_ROUTING_LIST | hard | error | false | — | `LEAK_PATTERNS` |
| OPTIONAL_ADAPTER_PRESENT | soft | warning | false | — | optional file exists |
| ZED_COMPAT_CONFLICT | soft | warning | false | — | несколько файлов из `ZED_COMPAT` |

`enforcement` в JSON: **`hard`** соответствует ошибкам (exit 1 при ошибках), **`soft`** — предупреждениям.

---

## Авто-исправление (`fix-adapters.sh`)

Обрабатываются коды: **`MISSING_LLMS_REDIRECT`**, **`MISSING_AGENT_RULES_REDIRECT`**, **`MISSING_META_ROLE`**, **`MISSING_META_AUTHORITY`**, **`MISSING_META_SOT`** — при условии `auto_fixable: true` в переданном `report.json`. Остальные коды требуют ручного исправления.
