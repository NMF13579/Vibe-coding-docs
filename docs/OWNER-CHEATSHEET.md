<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Owner Cheatsheet</title>
  <style>
    :root {
      --bg: #f7f6f2;
      --surface: #ffffff;
      --surface-2: #f3f0ec;
      --text: #28251d;
      --muted: #6f6b63;
      --border: #d9d3cb;
      --primary: #01696f;
      --primary-2: #0c4e54;
      --danger: #a13544;
      --warning: #b07a00;
      --success: #437a22;
      --shadow: 0 10px 30px rgba(24, 24, 24, 0.08);
      --radius: 16px;
      --radius-sm: 10px;
      --max: 1180px;
    }

    * { box-sizing: border-box; }
    html { scroll-behavior: smooth; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: linear-gradient(180deg, #f8f7f3 0%, #f3f0ec 100%);
      color: var(--text);
      line-height: 1.5;
    }

    .wrap {
      max-width: var(--max);
      margin: 0 auto;
      padding: 24px;
    }

    .hero {
      background: rgba(255,255,255,0.82);
      backdrop-filter: blur(10px);
      border: 1px solid rgba(0,0,0,0.07);
      border-radius: 24px;
      padding: 28px;
      box-shadow: var(--shadow);
      position: sticky;
      top: 12px;
      z-index: 10;
      margin-top: 12px;
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      color: var(--primary);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: .04em;
      text-transform: uppercase;
      margin-bottom: 10px;
    }

    h1 {
      margin: 0 0 8px;
      font-size: clamp(28px, 4vw, 48px);
      line-height: 1.05;
    }

    .sub {
      margin: 0;
      color: var(--muted);
      max-width: 72ch;
      font-size: 16px;
    }

    .toolbar {
      display: grid;
      grid-template-columns: 1.4fr .8fr;
      gap: 14px;
      margin-top: 20px;
    }

    .searchbox, .statsbox {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 14px;
    }

    .searchbox label, .statsbox .label {
      display: block;
      font-size: 12px;
      color: var(--muted);
      margin-bottom: 8px;
      text-transform: uppercase;
      letter-spacing: .04em;
      font-weight: 700;
    }

    .searchrow {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    input[type="search"] {
      flex: 1;
      min-width: 200px;
      border: 1px solid var(--border);
      background: #fff;
      border-radius: 12px;
      padding: 14px 16px;
      font-size: 15px;
      outline: none;
    }

    input[type="search"]:focus {
      border-color: var(--primary);
      box-shadow: 0 0 0 4px rgba(1, 105, 111, .10);
    }

    .btn {
      border: 0;
      border-radius: 12px;
      padding: 13px 16px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      transition: .18s ease;
    }

    .btn.primary {
      background: var(--primary);
      color: #fff;
    }

    .btn.primary:hover { background: var(--primary-2); }
    .btn.ghost {
      background: #fff;
      border: 1px solid var(--border);
      color: var(--text);
    }

    .stats {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    .pill {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: 999px;
      padding: 10px 12px;
      font-size: 14px;
      color: var(--text);
    }

    .grid {
      display: grid;
      grid-template-columns: 300px 1fr;
      gap: 22px;
      margin-top: 22px;
      align-items: start;
    }

    .sidebar, .contentcard {
      background: rgba(255,255,255,.88);
      border: 1px solid rgba(0,0,0,.07);
      border-radius: 20px;
      box-shadow: var(--shadow);
    }

    .sidebar {
      position: sticky;
      top: 220px;
      padding: 18px;
    }

    .sidebar h2, .contentcard h2 {
      margin: 0 0 12px;
      font-size: 16px;
    }

    .navlist {
      display: grid;
      gap: 8px;
    }

    .navlist a {
      display: block;
      text-decoration: none;
      color: var(--text);
      border: 1px solid transparent;
      background: var(--surface-2);
      padding: 12px 13px;
      border-radius: 12px;
      font-size: 14px;
    }

    .navlist a:hover {
      border-color: var(--border);
      background: #fff;
    }

    .contentcard {
      padding: 18px;
    }

    .section {
      margin-bottom: 24px;
      scroll-margin-top: 220px;
    }

    .sectionhead {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
      margin-bottom: 12px;
      flex-wrap: wrap;
    }

    .sectionhead h3 {
      margin: 0;
      font-size: 20px;
    }

    .sectionhint {
      color: var(--muted);
      font-size: 14px;
    }

    .cards {
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }

    .command {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
      display: grid;
      gap: 10px;
    }

    .command.hidden { display: none; }

    .toprow {
      display: flex;
      align-items: start;
      justify-content: space-between;
      gap: 12px;
    }

    .tag {
      font-size: 12px;
      font-weight: 700;
      border-radius: 999px;
      padding: 7px 10px;
      white-space: nowrap;
    }

    .tag.start { background: rgba(1,105,111,.11); color: var(--primary); }
    .tag.confirm { background: rgba(67,122,34,.12); color: var(--success); }
    .tag.error { background: rgba(161,53,68,.12); color: var(--danger); }
    .tag.scope { background: rgba(176,122,0,.13); color: #8a5b00; }
    .tag.session { background: rgba(0,0,0,.06); color: #514d47; }
    .tag.release { background: rgba(55,91,163,.12); color: #375ba3; }

    .cmd {
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 15px;
      background: var(--surface-2);
      border: 1px dashed var(--border);
      padding: 12px 14px;
      border-radius: 12px;
      word-break: break-word;
    }

    .desc {
      font-size: 15px;
      color: var(--text);
    }

    .meta {
      font-size: 13px;
      color: var(--muted);
    }

    .actions {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .mini {
      padding: 10px 12px;
      font-size: 13px;
      border-radius: 10px;
      border: 1px solid var(--border);
      background: #fff;
      cursor: pointer;
      font-weight: 700;
    }

    .mini:hover { background: var(--surface-2); }

    .note {
      background: #fff8ea;
      border: 1px solid #ecd9a5;
      color: #6b5317;
      border-radius: 14px;
      padding: 14px 16px;
      margin-top: 8px;
      font-size: 14px;
    }

    .quick {
      display: grid;
      gap: 12px;
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .quickbox {
      background: #fff;
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 16px;
    }

    .quickbox h4 {
      margin: 0 0 10px;
      font-size: 16px;
    }

    .quickbox pre {
      margin: 0;
      white-space: pre-wrap;
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 14px;
      background: var(--surface-2);
      border-radius: 12px;
      padding: 12px;
      border: 1px dashed var(--border);
    }

    .footer {
      text-align: center;
      color: var(--muted);
      font-size: 13px;
      padding: 28px 0 16px;
    }

    .empty {
      display: none;
      text-align: center;
      color: var(--muted);
      border: 1px dashed var(--border);
      border-radius: 16px;
      padding: 28px;
      background: #fff;
    }

    @media (max-width: 980px) {
      .grid { grid-template-columns: 1fr; }
      .sidebar { position: static; }
      .cards, .quick, .toolbar { grid-template-columns: 1fr; }
      .hero { position: static; }
    }

    @media (max-width: 640px) {
      .wrap { padding: 14px; }
      .hero, .sidebar, .contentcard { border-radius: 18px; }
      .cards { grid-template-columns: 1fr; }
      .toprow { flex-direction: column; }
      .actions { width: 100%; }
      .mini { flex: 1; }
    }
  </style>
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <div class="eyebrow">Owner Cheatsheet</div>
      <h1>Шпаргалка владельца проекта</h1>
      <p class="sub">Открой этот файл в браузере. Здесь есть команды для работы с агентом, быстрый поиск, копирование в один клик и короткие пояснения — что именно произойдёт после каждой команды.</p>

      <div class="toolbar">
        <div class="searchbox">
          <label for="search">Поиск по командам и действиям</label>
          <div class="searchrow">
            <input id="search" type="search" placeholder="Например: восстанови, ошибка, релиз, идея" />
            <button class="btn primary" id="clearBtn" type="button">Сбросить</button>
          </div>
        </div>
        <div class="statsbox">
          <div class="label">Сводка</div>
          <div class="stats">
            <div class="pill"><span>Команд:</span> <strong id="countAll">0</strong></div>
            <div class="pill"><span>Показано:</span> <strong id="countVisible">0</strong></div>
          </div>
        </div>
      </div>
    </header>

    <main class="grid">
      <aside class="sidebar">
        <h2>Разделы</h2>
        <nav class="navlist">
          <a href="#start">🚀 Начало работы</a>
          <a href="#confirm">✅ Подтверждения</a>
          <a href="#ideas">💡 Идеи и scope</a>
          <a href="#errors">🐛 Ошибки и откат</a>
          <a href="#session">💾 Сессия и контекст</a>
          <a href="#release">🚢 Релиз</a>
          <a href="#templates">🧩 Шаблоны</a>
        </nav>
        <div class="note">
          Совет: если агент начал путаться или сессия стала слишком длинной — сначала нажми <strong>«Сохрани контекст»</strong>, потом начни новый чат и напиши <strong>«Восстанови контекст»</strong>.
        </div>
      </aside>

      <section class="contentcard">
        <div class="section" id="start">
          <div class="sectionhead">
            <h3>🚀 Начало работы</h3>
            <div class="sectionhint">Старт проекта и первое включение</div>
          </div>
          <div class="cards">
            <article class="command" data-text="начнём старт новый проект начать работу create project quick start">
              <div class="toprow">
                <span class="tag start">Старт</span>
                <div class="actions">
                  <button class="mini copy-btn" data-copy="Начнём">Копировать</button>
                </div>
              </div>
              <div class="cmd">Начнём</div>
              <div class="desc">Запускает новый проект с выбором уровня: быстрый старт, стандартный MVP или production MVP.</div>
              <div class="meta">Используй в самом начале, когда проекта ещё нет или хочешь стартовать заново.</div>
            </article>

            <article class="command" data-text="старт новый проект новый чат начать start">
              <div class="toprow">
                <span class="tag start">Старт</span>
                <div class="actions">
                  <button class="mini copy-btn" data-copy="Старт">Копировать</button>
                </div>
              </div>
              <div class="cmd">Старт</div>
              <div class="desc">Короткая альтернатива команде «Начнём». Полезно, если хочешь совсем простой запуск без длинной формулировки.</div>
              <div class="meta">Делает то же самое: агент начинает конвейер запуска проекта.</div>
            </article>
          </div>
        </div>

        <div class="section" id="confirm">
          <div class="sectionhead">
            <h3>✅ Подтверждения</h3>
            <div class="sectionhint">Фразы, после которых агент может двигаться дальше</div>
          </div>
          <div class="cards">
            <article class="command" data-text="всё верно подтверждение continue approve ok">
              <div class="toprow">
                <span class="tag confirm">Подтверждение</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Всё верно">Копировать</button></div>
              </div>
              <div class="cmd">Всё верно</div>
              <div class="desc">Подтверждает, что агент правильно понял идею, план, структуру документа или следующий шаг.</div>
              <div class="meta">Самая полезная фраза в системе: без неё агент не должен двигаться дальше.</div>
            </article>

            <article class="command" data-text="ок да приступай подтверждаю галочка approve yes">
              <div class="toprow">
                <span class="tag confirm">Подтверждение</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Ок">Копировать</button></div>
              </div>
              <div class="cmd">Ок / Да / Приступай / ✓</div>
              <div class="desc">Короткие варианты подтверждения, когда ты согласен и хочешь перейти к следующему действию.</div>
              <div class="meta">Используй после плана, после резюме, после описания задачи или после инструкции на реализацию.</div>
            </article>
          </div>
        </div>

        <div class="section" id="ideas">
          <div class="sectionhead">
            <h3>💡 Идеи и scope</h3>
            <div class="sectionhint">Когда пришла новая мысль посреди текущей работы</div>
          </div>
          <div class="cards">
            <article class="command" data-text="запиши идею новая идея backlog потом отложить future feature">
              <div class="toprow">
                <span class="tag scope">Scope</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Запиши идею: [твоя идея]">Копировать</button></div>
              </div>
              <div class="cmd">Запиши идею: [твоя идея]</div>
              <div class="desc">Сохраняет мысль на потом, не ломая текущую задачу и не уводя проект в хаос.</div>
              <div class="meta">Лучший способ не сорвать текущий фокус и не потерять хорошую идею.</div>
            </article>

            <article class="command" data-text="разбей на части большая задача слишком большая decomposition split task">
              <div class="toprow">
                <span class="tag scope">Scope</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Разбей на части">Копировать</button></div>
              </div>
              <div class="cmd">Разбей на части</div>
              <div class="desc">Просит агента остановиться, показать что уже готово и разделить слишком большую задачу на более маленькие шаги.</div>
              <div class="meta">Нужно использовать, если задача длится слишком долго или агент начинает делать слишком много сразу.</div>
            </article>

            <article class="command" data-text="стоп давай по-другому change approach rethink пересмотреть">
              <div class="toprow">
                <span class="tag scope">Scope</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Стоп, давай по-другому">Копировать</button></div>
              </div>
              <div class="cmd">Стоп, давай по-другому</div>
              <div class="desc">Останавливает текущий подход и просит предложить другой, более простой или безопасный вариант.</div>
              <div class="meta">Полезно, если решение кажется слишком сложным для текущего этапа MVP.</div>
            </article>
          </div>
        </div>

        <div class="section" id="errors">
          <div class="sectionhead">
            <h3>🐛 Ошибки и откат</h3>
            <div class="sectionhint">Когда всё сломалось или ведёт себя странно</div>
          </div>
          <div class="cards">
            <article class="command" data-text="всё сломалось ошибка не работает crash rollback urgent critical">
              <div class="toprow">
                <span class="tag error">Ошибка</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Всё сломалось">Копировать</button></div>
              </div>
              <div class="cmd">Всё сломалось</div>
              <div class="desc">Запускает аварийный сценарий: агент сначала стабилизирует ситуацию, потом уже разбирается в причине.</div>
              <div class="meta">Используй, если приложение не открывается, ломается логин, пропали данные или появился белый экран.</div>
            </article>

            <article class="command" data-text="откати rollback вернуть как было revert last step">
              <div class="toprow">
                <span class="tag error">Ошибка</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Откати">Копировать</button></div>
              </div>
              <div class="cmd">Откати</div>
              <div class="desc">Просит вернуть последнее рабочее состояние вместо дальнейших попыток чинить всё на месте.</div>
              <div class="meta">Подходит, когда после недавнего изменения стало хуже, чем было.</div>
            </article>

            <article class="command" data-text="не работает баг функция broken save auth button error">
              <div class="toprow">
                <span class="tag error">Ошибка</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Не работает: [что именно]">Копировать</button></div>
              </div>
              <div class="cmd">Не работает: [что именно]</div>
              <div class="desc">Быстрый способ описать локальную проблему, если сломалась не вся система, а только одна функция.</div>
              <div class="meta">Добавь одно предложение: что нажал, что ожидал, что произошло.</div>
            </article>
          </div>
        </div>

        <div class="section" id="session">
          <div class="sectionhead">
            <h3>💾 Сессия и контекст</h3>
            <div class="sectionhint">Самые важные команды для длинной работы</div>
          </div>
          <div class="cards">
            <article class="command" data-text="сохрани контекст session save handoff memory status">
              <div class="toprow">
                <span class="tag session">Сессия</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Сохрани контекст">Копировать</button></div>
              </div>
              <div class="cmd">Сохрани контекст</div>
              <div class="desc">Просит агента обновить HANDOFF, project-status и другие служебные документы перед завершением сессии.</div>
              <div class="meta">Лучшая команда перед закрытием окна, переходом в другой чат или длинной паузой.</div>
            </article>

            <article class="command" data-text="восстанови контекст новая сессия lost context forgot previous handoff">
              <div class="toprow">
                <span class="tag session">Сессия</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Восстанови контекст">Копировать</button></div>
              </div>
              <div class="cmd">Восстанови контекст</div>
              <div class="desc">Главная команда для новой сессии: агент читает ключевые файлы и коротко объясняет, где вы остановились.</div>
              <div class="meta">Используй в начале почти каждого нового чата.</div>
            </article>

            <article class="command" data-text="прочитай handoff быстрый старт short recovery">
              <div class="toprow">
                <span class="tag session">Сессия</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Прочитай HANDOFF">Копировать</button></div>
              </div>
              <div class="cmd">Прочитай HANDOFF</div>
              <div class="desc">Быстрый режим восстановления, если не хочется писать длинный ввод и нужен только последний статус.</div>
              <div class="meta">Полезно, если контекст в целом понятен, но нужно быстро вспомнить последний шаг.</div>
            </article>

            <article class="command" data-text="переходим на уровень выше documentation structure mature project">
              <div class="toprow">
                <span class="tag session">Сессия</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Переходим на уровень выше">Копировать</button></div>
              </div>
              <div class="cmd">Переходим на уровень выше</div>
              <div class="desc">Просит агента добавить более взрослую структуру проекта и недостающие документы без полного перезапуска.</div>
              <div class="meta">Нужно, если проект вырос из режима «быстрый старт» и требует большего порядка.</div>
            </article>
          </div>
        </div>

        <div class="section" id="release">
          <div class="sectionhead">
            <h3>🚢 Релиз</h3>
            <div class="sectionhint">Перед показом пользователям или первым деплоем</div>
          </div>
          <div class="cards">
            <article class="command" data-text="проверь готовность к релизу release deploy checklist production">
              <div class="toprow">
                <span class="tag release">Релиз</span>
                <div class="actions"><button class="mini copy-btn" data-copy="Проверь готовность к релизу">Копировать</button></div>
              </div>
              <div class="cmd">Проверь готовность к релизу</div>
              <div class="desc">Запускает финальную проверку перед показом пользователям: функциональность, безопасность, данные и документация.</div>
              <div class="meta">Используй перед публикацией, демонстрацией клиенту или первым реальным тестом на пользователях.</div>
            </article>
          </div>
        </div>

        <div class="section" id="templates">
          <div class="sectionhead">
            <h3>🧩 Шаблоны</h3>
            <div class="sectionhint">Готовые сообщения, которые удобно вставлять как есть</div>
          </div>

          <div class="quick">
            <div class="quickbox">
              <h4>Шаблон ошибки</h4>
              <pre id="tpl-error">🔴 ОШИБКА

Что я делал:
Что ожидал:
Что произошло:
Текст ошибки (если есть):
Когда началось:</pre>
              <div class="actions" style="margin-top:10px;">
                <button class="mini copy-btn" data-copy="🔴 ОШИБКА

Что я делал:
Что ожидал:
Что произошло:
Текст ошибки (если есть):
Когда началось:">Копировать шаблон</button>
              </div>
            </div>

            <div class="quickbox">
              <h4>Шаблон новой сессии</h4>
              <pre id="tpl-session">Восстанови контекст.
Последнее что помню: [кратко опиши 1 фразой]</pre>
              <div class="actions" style="margin-top:10px;">
                <button class="mini copy-btn" data-copy="Восстанови контекст.
Последнее что помню: [кратко опиши 1 фразой]">Копировать шаблон</button>
              </div>
            </div>
          </div>

          <div class="empty" id="emptyState">Ничего не найдено. Попробуй другой запрос: например, «ошибка», «контекст», «релиз», «идея».</div>
        </div>
      </section>
    </main>

    <div class="footer">Локальная HTML-шпаргалка — без сервера, можно хранить прямо в репозитории рядом с документами.</div>
  </div>

  <script>
    const searchInput = document.getElementById('search');
    const cards = Array.from(document.querySelectorAll('.command'));
    const countAll = document.getElementById('countAll');
    const countVisible = document.getElementById('countVisible');
    const emptyState = document.getElementById('emptyState');
    const clearBtn = document.getElementById('clearBtn');

    function updateCounts() {
      const visible = cards.filter(card => !card.classList.contains('hidden')).length;
      countAll.textContent = cards.length;
      countVisible.textContent = visible;
      emptyState.style.display = visible === 0 ? 'block' : 'none';
    }

    function normalize(text) {
      return (text || '').toLowerCase().trim();
    }

    function filterCards() {
      const query = normalize(searchInput.value);
      cards.forEach(card => {
        const text = normalize(card.dataset.text + ' ' + card.innerText);
        const show = !query || text.includes(query);
        card.classList.toggle('hidden', !show);
      });
      updateCounts();
    }

    searchInput.addEventListener('input', filterCards);
    clearBtn.addEventListener('click', () => {
      searchInput.value = '';
      filterCards();
      searchInput.focus();
    });

    async function copyText(text, btn) {
      try {
        await navigator.clipboard.writeText(text);
        const original = btn.textContent;
        btn.textContent = 'Скопировано';
        setTimeout(() => btn.textContent = original, 1200);
      } catch (e) {
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        ta.remove();
        const original = btn.textContent;
        btn.textContent = 'Скопировано';
        setTimeout(() => btn.textContent = original, 1200);
      }
    }

    document.querySelectorAll('.copy-btn').forEach(btn => {
      btn.addEventListener('click', () => copyText(btn.dataset.copy, btn));
    });

    updateCounts();
  </script>
</body>
</html>
