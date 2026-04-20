const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..', '..');
const LAYER1_DIR = path.join(ROOT_DIR, 'LAYER-1');

// MUST match LAYER-1/document-governance.md
const ALLOWED_ROLES = [
  'CANONICAL_POLICY', 'RUNTIME_STATE', 'SESSION_CONTEXT',
  'NARRATIVE_CONTEXT', 'NAVIGATION', 'ADAPTER',
  'REFERENCE', 'DEPRECATED', 'ARCHIVE'
];

const ALLOWED_AUTHORITIES = [
  'PRIMARY', 'SECONDARY', 'TERTIARY', 'NON-AUTHORITY'
];

const ALLOWED_STATUSES = [
  'ACTIVE', 'LIMITED', 'DEPRECATED', 'ARCHIVED'
];

const EXCLUDED_DIRS = new Set(['archive', 'deprecated']);

function toPosix(filePath) {
  return filePath.split(path.sep).join('/');
}

function collectLayerOneMarkdownFiles(dir, files = []) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      if (EXCLUDED_DIRS.has(entry.name)) {
        continue;
      }
      collectLayerOneMarkdownFiles(fullPath, files);
      continue;
    }

    if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(fullPath);
    }
  }

  return files;
}

function parseMetadata(content, key) {
  const regex = new RegExp(`<!--\\s*${key}:\\s*([^>]+?)\\s*-->`, 'm');
  const match = content.match(regex);
  return match ? match[1].trim() : null;
}

async function run() {
  const failItems = [];
  const warningItems = [];
  const files = collectLayerOneMarkdownFiles(LAYER1_DIR);

  for (const file of files) {
    const content = fs.readFileSync(file, 'utf8');
    const relativePath = toPosix(path.relative(ROOT_DIR, file));

    const role = parseMetadata(content, 'ROLE');
    if (role !== null && !ALLOWED_ROLES.includes(role)) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: `[check-metadata] Invalid ROLE value "${role}".`
      });
    }

    const authority = parseMetadata(content, 'AUTHORITY');
    if (authority !== null && !ALLOWED_AUTHORITIES.includes(authority)) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: `[check-metadata] Invalid AUTHORITY value "${authority}".`
      });
    }

    const status = parseMetadata(content, 'STATUS');
    if (status !== null && !ALLOWED_STATUSES.includes(status)) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: `[check-metadata] Invalid STATUS value "${status}".`
      });
    }
  }

  return {
    name: 'check-metadata',
    fails: failItems.length,
    warnings: warningItems.length,
    issues: [...failItems, ...warningItems]
  };
}

module.exports = { run };
