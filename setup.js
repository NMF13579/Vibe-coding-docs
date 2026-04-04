#!/usr/bin/env node

/**
 * INTERACTIVE TEMPLATE SYNC SETUP
 *
 * Мастер синхронизации - спрашивает 2 вопроса и делает всё остальное.
 *
 * Использование:
 *   node setup.js
 */

const fs = require('fs');
const path = require('path');
const readline = require('readline');
const { execSync } = require('child_process');

const COLORS = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  dim: '\x1b[2m',
  cyan: '\x1b[36m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  red: '\x1b[31m',
};

function log(msg, color = 'reset') {
  console.log(`${COLORS[color]}${msg}${COLORS.reset}`);
}

function section(title) {
  console.log('');
  log(`${'═'.repeat(60)}`, 'bright');
  log(title, 'bright');
  log(`${'═'.repeat(60)}`, 'bright');
}

function success(msg) {
  log(`✅ ${msg}`, 'green');
}

function error(msg) {
  log(`❌ ${msg}`, 'red');
}

function warning(msg) {
  log(`⚠️  ${msg}`, 'yellow');
}

function info(msg) {
  log(`ℹ️  ${msg}`, 'cyan');
}

async function ask(question) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise(resolve => {
    rl.question(`${COLORS.bright}${question}${COLORS.reset}\n→ `, answer => {
      rl.close();
      resolve(answer.trim());
    });
  });
}

async function confirmAsync(question) {
  const answer = await ask(`${question} (да/нет)`);
  return answer.toLowerCase().startsWith('д') || answer.toLowerCase() === 'y';
}

async function main() {
  section('🎯 МАСТЕР СИНХРОНИЗАЦИИ ШАБЛОНОВ');

  log('Я помогу синхронизировать файлы из Vibe Coding Docs', 'cyan');
  console.log('');

  // Проверка Node.js
  info('Проверяю окружение...');
  const nodeVersion = execSync('node --version', { encoding: 'utf-8' }).trim();
  success(`Node.js ${nodeVersion} найден`);
  console.log('');

  // Вопрос 1: Путь к Vibe Docs
  section('❓ ВОПРОС 1: Где находится Vibe Coding Docs?');

  log('Укажи полный путь до папки vibe-coding-docs', 'cyan');
  log('Примеры:', 'dim');
  log('  /Users/alex/vibe-coding-docs', 'dim');
  log('  C:\\Users\\alex\\vibe-coding-docs', 'dim');
  log('  ~/projects/vibe-coding-docs', 'dim');
  console.log('');

  let sourceDir = await ask('Путь к Vibe Docs');

  // Развернуть ~
  if (sourceDir.startsWith('~')) {
    sourceDir = sourceDir.replace('~', process.env.HOME || process.env.USERPROFILE);
  }

  // Проверка пути
  if (!fs.existsSync(sourceDir)) {
    error(`Папка не найдена: ${sourceDir}`);
    console.log('');
    log('Проверь что:', 'yellow');
    log('1. Путь написан правильно', 'dim');
    log('2. Папка существует', 'dim');
    log('3. У тебя есть доступ', 'dim');
    process.exit(1);
  }

  success(`Папка найдена: ${sourceDir}`);
  console.log('');

  // Вопрос 2: Подтверждение
  section('❓ ВОПРОС 2: Готов добавить файлы?');

  // Сухой запуск
  log('Запускаю проверку (dry-run)...', 'cyan');
  console.log('');

  try {
    const output = execSync(
      `node template-sync.js "${sourceDir}" . --dry-run`,
      {
        encoding: 'utf-8',
        stdio: ['pipe', 'pipe', 'pipe'],
      }
    );

    // Извлечь статистику
    const lines = output.split('\n');
    let filesToAdd = 0;
    let filesToSkip = 0;

    for (const line of lines) {
      if (line.includes('Файлы к добавлению:')) {
        filesToAdd = parseInt(line.match(/\d+/)[0]);
      }
      if (line.includes('Файлы к пропуску:')) {
        filesToSkip = parseInt(line.match(/\d+/)[0]);
      }
    }

    console.log(output);
    console.log('');

    const confirmed = await confirmAsync(
      `Добавить ${filesToAdd} новых файлов? (${filesToSkip} файлов пропустить)`
    );

    if (!confirmed) {
      warning('Отменено пользователем');
      process.exit(0);
    }

    console.log('');
    section('🔄 ВЫПОЛНЕНИЕ СИНХРОНИЗАЦИИ');

    // Реальный запуск
    log('Копирую файлы...', 'cyan');
    const syncOutput = execSync(`node template-sync.js "${sourceDir}" .`, {
      encoding: 'utf-8',
    });

    console.log(syncOutput);
    console.log('');

    // Финал
    section('✨ ГОТОВО!');

    success('Файлы синхронизированы');
    console.log('');

    log('Дальше:', 'bright');
    log('1. Посмотри что добавилось:', 'dim');
    log('   git status', 'dim');
    console.log('');
    log('2. Прочитай отчёт:', 'dim');
    log('   cat template-sync-report.md', 'dim');
    console.log('');
    log('3. Закоммить изменения:', 'dim');
    log('   git add .', 'dim');
    log('   git commit -m "feat: добавлены файлы из шаблона"', 'dim');
    console.log('');

    success('Успешно!');
    process.exit(0);
  } catch (err) {
    error('Ошибка при синхронизации');
    console.log(err.message);
    process.exit(1);
  }
}

main().catch(err => {
  error(`Ошибка: ${err.message}`);
  process.exit(1);
});
