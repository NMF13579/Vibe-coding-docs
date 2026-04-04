#!/usr/bin/env node

/**
 * TEMPLATE SYNC — Синхронизатор файлов Vibe Coding Docs
 *
 * Копирует только новые файлы из шаблона в целевой проект.
 * Существующие файлы не перезаписываются.
 *
 * Использование:
 *   node template-sync.js <source-dir> <target-dir> [--dry-run]
 *
 * 
 * Копирует только новые файлы из шаблона в целевой проект.
 * Существующие файлы не перезаписываются.
 * 
 * Использование:
 *   node template-sync.js <source-dir> <target-dir> [--dry-run]
 * 
 * Примеры:
 *   node template-sync.js ./vibe-docs ./my-project
 *   node template-sync.js ./vibe-docs ./my-project --dry-run
 */

const fs = require('fs');
const path = require('path');

// ============================================================================
// КОНФИГУРАЦИЯ
// ============================================================================

const IGNORE_PATTERNS = [
  /^\.git\//,
  /^node_modules\//,
  /^\.env/,
  /^\.DS_Store$/,
  /^Thumbs\.db$/,
  /setup\.js$/,
  /template-sync\.js$/,
  /README-TEMPLATE\.md$/,
  /README-TEMPLATE\.md$/, // если есть файл с инструкциями
];

const REPORT_FILENAME = 'template-sync-report.md';

// ============================================================================
// УТИЛИТЫ
// ============================================================================

function shouldIgnore(filePath) {
  return IGNORE_PATTERNS.some(pattern => pattern.test(filePath));
}

function getAllFiles(dir, baseDir = '') {
  let files = [];

  
  if (!fs.existsSync(dir)) {
    return files;
  }

  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    const relativePath = path.join(baseDir, entry.name);

    if (shouldIgnore(relativePath)) {
      continue;
    }

    if (entry.isDirectory()) {
      files = files.concat(getAllFiles(fullPath, relativePath));
    } else {
      files.push(relativePath);
    }
  }

  return files;
}

function ensureDir(dir) {
  if (!fs.existsSync(dir)) {
    fs.mkdirSync(dir, { recursive: true });
  }
}

function copyFile(src, dst) {
  ensureDir(path.dirname(dst));
  fs.copyFileSync(src, dst);
}

// ============================================================================
// ОСНОВНАЯ ЛОГИКА
// ============================================================================

function syncTemplates(sourceDir, targetDir, dryRun = false) {
  console.log('🔄 TEMPLATE SYNC — начало синхронизации\n');
  console.log(`📂 Источник: ${sourceDir}`);
  console.log(`📂 Целевой:  ${targetDir}`);
  console.log(`🔍 Режим:    ${dryRun ? 'DRY-RUN (без изменений)' : 'НОРМАЛЬНЫЙ'}`);
  console.log('');

  // Проверка директорий
  if (!fs.existsSync(sourceDir)) {
    console.error(`❌ Ошибка: директория источника не найдена: ${sourceDir}`);
    process.exit(1);
  }

  ensureDir(targetDir);

  // Получить все файлы
  const sourceFiles = getAllFiles(sourceDir);
  const targetFiles = getAllFiles(targetDir);
  const targetFilesSet = new Set(targetFiles);

  console.log(`📊 Файлы в источнике: ${sourceFiles.length}`);
  console.log(`📊 Файлы в целевом:   ${targetFiles.length}`);
  console.log('');

  // Определить какие файлы нужно добавить
  const filesToAdd = sourceFiles.filter(file => !targetFilesSet.has(file));
  const filesToSkip = sourceFiles.filter(file => targetFilesSet.has(file));

  console.log(`✅ Файлы к добавлению: ${filesToAdd.length}`);
  console.log(`⏭️  Файлы к пропуску:   ${filesToSkip.length}`);
  console.log('');

  // Выполнить копирование (или показать что было бы скопировано)
  const copied = [];
  const skipped = [];

  for (const file of filesToAdd) {
    const src = path.join(sourceDir, file);
    const dst = path.join(targetDir, file);

    if (dryRun) {
      console.log(`  [DRY-RUN] + ${file}`);
    } else {
      copyFile(src, dst);
      console.log(`  ✓ ${file}`);
    }
    copied.push(file);
  }

  for (const file of filesToSkip) {
    skipped.push(file);
  }

  // Создать отчёт
  const report = generateReport({
    sourceDir,
    targetDir,
    dryRun,
    timestamp: new Date().toISOString(),
    copied,
    skipped,
    totalSource: sourceFiles.length,
    totalTarget: targetFiles.length,
  });

  if (!dryRun) {
    const reportPath = path.join(targetDir, REPORT_FILENAME);
    fs.writeFileSync(reportPath, report);
    console.log('');
    console.log(`📄 Отчёт сохранён: ${reportPath}`);
  }

  // Итоги
  console.log('');
  console.log('═'.repeat(60));
  if (dryRun) {
    console.log(`DRY-RUN: было бы скопировано ${copied.length} файлов`);
  } else {
    console.log(`✅ Готово! Добавлено ${copied.length} файлов`);
  }
  console.log('═'.repeat(60));

  return {
    copied: copied.length,
    skipped: skipped.length,
    total: copied.length + skipped.length,
  };
}

function generateReport(data) {
  const {
    sourceDir,
    targetDir,
    dryRun,
    timestamp,
    copied,
    skipped,
    totalSource,
    totalTarget,
  } = data;

  return `# Template Sync Report

**Дата:** ${timestamp}
**Режим:** ${dryRun ? 'DRY-RUN (без изменений)' : 'Нормальный'}

## Источники

- **Источник:** \`${sourceDir}\`
- **Целевой:** \`${targetDir}\`

## Статистика

| Метрика | Значение |
|---------|----------|
| Файлов в источнике | ${totalSource} |
| Файлов в целевом | ${totalTarget} |
| Добавлено | ${copied.length} |
| Пропущено (уже есть) | ${skipped.length} |

## Добавленные файлы (${copied.length})

\`\`\`
${copied.length > 0 ? copied.map(f => '+ ' + f).join('\n') : '(нет)'}
\`\`\`

## Пропущенные файлы (${skipped.length})

Эти файлы уже существуют в целевом проекте и не перезаписывались:

\`\`\`
${skipped.length > 0 ? skipped.map(f => '- ' + f).join('\n') : '(нет)'}
\`\`\`

---

## Как использовать этот отчёт

1. **Проверь добавленные файлы** — они новые и не конфликтуют с существующими
2. **Обнови документацию** — если добавились новые docs/ файлы
3. **Обнови HANDOFF.md** — добавь запись о синхронизации
4. **Закоммить изменения** — все файлы готовы к коммиту

## Команда для отката

Если что-то пошло не так, откати последний коммит:

\`\`\`bash
git reset --hard HEAD~1
\`\`\`
`;
}

// ============================================================================
// ЗАПУСК
// ============================================================================

function main() {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.log(`
Использование:
  node template-sync.js <source-dir> <target-dir> [--dry-run]

Примеры:
  node template-sync.js ./vibe-docs ./my-project
  node template-sync.js ./vibe-docs ./my-project --dry-run

Опции:
  --dry-run    Показать что было бы скопировано, без реальных изменений
`);
    process.exit(1);
  }

  const sourceDir = args[0];
  const targetDir = args[1];
  const dryRun = args.includes('--dry-run');

  syncTemplates(sourceDir, targetDir, dryRun);
}

main();
