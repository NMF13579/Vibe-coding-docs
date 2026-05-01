# START — с чего начать

Primary human route: `ROUTES-REGISTRY.md` -> canonical modules.

## Ты человек — выбери маршрут

| Кто ты | Куда идти | Что пропустить на первом шаге |
|---|---|---|
| Новичок без опыта | `ROUTES-REGISTRY.md` -> `workflow/MAIN.md` | Детальные заметки и архивы |
| Врач / менеджер / эксперт | `ROUTES-REGISTRY.md` -> `security/MAIN.md` -> `quality/MAIN.md` | Нерелевантные доменные заметки |
| Потерял контекст | `state/MAIN.md` -> `workflow/MAIN.md` | Новые задачи до восстановления состояния |
| IDE user / разработчик | `llms.txt` -> `ROUTES-REGISTRY.md` | Самостоятельный обход файлов |
| AI-agent | `llms.txt` | Всё, что не указано маршрутом |

## AI-агент

Прочитай `llms.txt` и следуй только ему.
Для уточнения владельца правила используй `ROUTES-REGISTRY.md`.
Поведение задают пять canonical modules: `core-rules/MAIN.md`, `state/MAIN.md`, `workflow/MAIN.md`, `quality/MAIN.md`, `security/MAIN.md`.

## Обязательное правило

Plan -> Confirm -> Execute.
Без подтверждения владельца изменения не вносятся, если задача требует согласования.
