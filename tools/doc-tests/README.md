# Doc Integrity Tests

## Запуск

node tools/doc-tests/run-doc-tests.js

## Проверки

- check-links    — внутренние ссылки ведут на существующие файлы
- check-metadata — ROLE / AUTHORITY / STATUS соответствуют governance vocabulary
- check-bootstrap — canonical bootstrap задан только в llms.txt

## FAIL (блокирует merge)

- битые внутренние markdown-ссылки
- невалидные значения metadata
- competing canonical bootstrap вне llms.txt

## WARNING (не блокирует CI)

- мягкие несоответствия, фиксируются осознанно

## Обновление допустимых значений

При изменении ROLE / AUTHORITY / STATUS в LAYER-1/document-governance.md
обновить списки ALLOWED_* в check-metadata.js вручную.
