# CHECKLIST — перед деплоем / релизом

Короткий список перед выкатом. Детали по проверкам: `quality/MAIN.md`, `security/MAIN.md`, `workflow/MAIN.md`.

## Безопасность

- [ ] Нет секретов и ключей в коде и в коммитах.
- [ ] Проверены права доступа к данным и окружениям.
- [ ] Данные, доступы и секреты проверены по `security/MAIN.md`.

## Окружение

- [ ] Переменные окружения задокументированы без значений секретов.
- [ ] Известен способ восстановления через `workflow/MAIN.md` и `state/MAIN.md`.

## Smoke после выката

- [ ] Главный пользовательский сценарий проходит end-to-end.
- [ ] Критичные интеграции отвечают ожидаемо.
- [ ] Smoke-check зафиксирован по `quality/MAIN.md`.

## Продукт и UX

- [ ] Нет расхождения с согласованным scope без записи в план.
- [ ] Владелец явно подтвердил план выката.

## Merge Gate

- [ ] Startup order задан только в `llms.txt`.
- [ ] Route ownership задан в `ROUTES-REGISTRY.md`.
- [ ] Release blockers проверены по `quality/MAIN.md`.
- [ ] Security blockers проверены по `security/MAIN.md`.
- [ ] Scope и execution boundaries проверены по `workflow/MAIN.md`.
