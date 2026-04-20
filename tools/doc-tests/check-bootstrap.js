const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', '..');

const SKIP_DIRS = new Set([
  '.git',
  'node_modules',
  'tools/doc-tests',
  'LAYER-1/archive',
  'LAYER-1/deprecated',
]);

const DIRECT_PATTERNS = [
  '## Bootstrap order',
  'This is the canonical agent bootstrap order',
  'No other file defines read order',
];

function toPosix(inputPath) {
  return inputPath.split(path.sep).join('/');
}

function shouldSkipDir(relPath) {
  if (!relPath) return false;
  const normalized = toPosix(relPath);
  for (const skip of SKIP_DIRS) {
    if (normalized === skip || normalized.startsWith(skip + '/')) {
      return true;
    }
  }
  return false;
}

function collectMarkdownFiles(dirPath, out = []) {
  const relDir = toPosix(path.relative(ROOT, dirPath));
  if (shouldSkipDir(relDir)) return out;

  const entries = fs.readdirSync(dirPath, { withFileTypes: true });
  for (const entry of entries) {
    const absPath = path.join(dirPath, entry.name);
    const relPath = toPosix(path.relative(ROOT, absPath));

    if (entry.isDirectory()) {
      if (!shouldSkipDir(relPath)) {
        collectMarkdownFiles(absPath, out);
      }
      continue;
    }

    if (!entry.isFile()) continue;
    if (!entry.name.endsWith('.md')) continue;

    out.push(absPath);
  }

  return out;
}

function hasCompetingNumberedOrder(lines, index, lowerWindowText) {
  const numberedLine = /^\s*\d+\.\s+\S+/;
  if (!numberedLine.test(lines[index])) return false;

  if (lowerWindowText.includes('llms.txt')) return false;

  const hasBootstrapContext =
    lowerWindowText.includes('bootstrap') ||
    lowerWindowText.includes('read order') ||
    lowerWindowText.includes('startup');
  if (!hasBootstrapContext) return false;

  const hasCanonicalIntent =
    lowerWindowText.includes('canonical') ||
    lowerWindowText.includes('read in this sequence') ||
    lowerWindowText.includes('defines read order') ||
    lowerWindowText.includes('read in this order') ||
    lowerWindowText.includes('порядок чтения');

  return hasCanonicalIntent;
}

function hasAllowedLlmsReference(windowText, lineText) {
  const lowerLine = lineText.toLowerCase();
  if (lowerLine.includes('llms.txt')) {
    return true;
  }
  if (
    windowText.includes('canonical bootstrap') &&
    windowText.includes('llms.txt')
  ) {
    return true;
  }
  return false;
}

async function run() {
  const issues = [];
  const files = collectMarkdownFiles(ROOT);

  for (const filePath of files) {
    const relPath = toPosix(path.relative(ROOT, filePath));
    if (relPath === 'llms.txt') {
      continue;
    }

    const content = fs.readFileSync(filePath, 'utf8');
    const contentWithoutCode = content.replace(/```[\s\S]*?```/g, '');
    const lines = contentWithoutCode.split(/\r?\n/);

    for (const pattern of DIRECT_PATTERNS) {
      if (content.includes(pattern)) {
        issues.push({
          level: 'fail',
          file: relPath,
          message: `[check-bootstrap] Competing canonical bootstrap marker found: "${pattern}"`,
        });
      }
    }

    for (let i = 0; i < lines.length; i += 1) {
      const start = Math.max(0, i - 5);
      const end = Math.min(lines.length - 1, i + 5);
      const windowLines = lines.slice(start, end + 1);
      const lowerWindowText = windowLines.join('\n').toLowerCase();
      if (hasAllowedLlmsReference(lowerWindowText, lines[i])) {
        continue;
      }

      if (hasCompetingNumberedOrder(lines, i, lowerWindowText)) {
        issues.push({
          level: 'fail',
          file: relPath,
          message: '[check-bootstrap] Numbered list near bootstrap/read order/startup looks like competing canonical bootstrap',
        });
      }
    }
  }

  return {
    name: 'check-bootstrap',
    fails: issues.length,
    warnings: 0,
    issues,
  };
}

module.exports = { run };
