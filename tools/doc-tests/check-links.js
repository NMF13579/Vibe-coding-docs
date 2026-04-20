const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..', '..');
const EXCLUDED_DIRS = [
  '.git',
  'node_modules',
  path.join('tools', 'doc-tests'),
  path.join('LAYER-1', 'archive'),
  path.join('LAYER-1', 'deprecated'),
];

function toPosix(filePath) {
  return filePath.split(path.sep).join('/');
}

function isExcluded(relativePath) {
  const normalized = toPosix(relativePath);
  return EXCLUDED_DIRS.some((excluded) => {
    const excludedPosix = toPosix(excluded);
    return normalized === excludedPosix || normalized.startsWith(`${excludedPosix}/`);
  });
}

function collectMarkdownFiles(directory, files = []) {
  const entries = fs.readdirSync(directory, { withFileTypes: true });
  for (const entry of entries) {
    const absolutePath = path.join(directory, entry.name);
    const relativePath = path.relative(ROOT_DIR, absolutePath);

    if (isExcluded(relativePath)) {
      continue;
    }

    if (entry.isDirectory()) {
      collectMarkdownFiles(absolutePath, files);
      continue;
    }

    if (entry.isFile() && entry.name.toLowerCase().endsWith('.md')) {
      files.push(absolutePath);
    }
  }
  return files;
}

function stripFencedCodeBlocks(content) {
  return content.replace(/```[\s\S]*?```/g, '');
}

function normalizeLinkTarget(rawTarget) {
  let target = rawTarget.trim();
  if (!target) {
    return '';
  }

  if (target.startsWith('<') && target.endsWith('>')) {
    target = target.slice(1, -1).trim();
  }

  const firstWhitespace = target.search(/\s/);
  if (firstWhitespace !== -1) {
    target = target.slice(0, firstWhitespace);
  }

  return target;
}

function isExternalTarget(target) {
  if (/^https?:\/\//i.test(target)) {
    return true;
  }

  return /^[a-zA-Z][a-zA-Z0-9+.-]*:/.test(target);
}

function resolveLinkTarget(sourceFile, target) {
  const withoutHash = target.split('#')[0];
  const withoutQuery = withoutHash.split('?')[0];
  if (!withoutQuery) {
    return null;
  }

  if (withoutQuery.startsWith('/')) {
    return path.join(ROOT_DIR, withoutQuery.replace(/^\/+/, ''));
  }

  return path.resolve(path.dirname(sourceFile), withoutQuery);
}

async function run() {
  const failures = [];
  const warnings = [];
  const markdownFiles = collectMarkdownFiles(ROOT_DIR);
  const linkRegex = /\]\(([^)]+)\)/g;

  for (const markdownFile of markdownFiles) {
    const relativeFile = toPosix(path.relative(ROOT_DIR, markdownFile));
    const source = stripFencedCodeBlocks(fs.readFileSync(markdownFile, 'utf8'));

    let match;
    while ((match = linkRegex.exec(source)) !== null) {
      const rawTarget = match[1];
      const target = normalizeLinkTarget(rawTarget);

      if (!target || target.startsWith('#') || isExternalTarget(target)) {
        continue;
      }

      const resolvedTarget = resolveLinkTarget(markdownFile, target);
      if (!resolvedTarget || fs.existsSync(resolvedTarget)) {
        continue;
      }

      const resolvedRelative = toPosix(path.relative(ROOT_DIR, resolvedTarget));
      failures.push({
        file: relativeFile,
        message: `[check-links] Broken internal link "${target}" -> "${resolvedRelative}"`,
      });
    }
  }

  return {
    name: 'check-links',
    fails: failures.length,
    warnings: warnings.length,
    issues: [
      ...failures.map((item) => ({ level: 'fail', ...item })),
      ...warnings.map((item) => ({ level: 'warning', ...item })),
    ],
  };
}

module.exports = { run };
