const fs = require('fs');
const path = require('path');

const ROOT_DIR = path.resolve(__dirname, '..', '..');
const MODULES = ['core-rules', 'state', 'workflow', 'quality', 'security'];
const REQUIRED = {
  type: 'canonical',
  status: 'canonical',
  authority: 'canonical',
  when_to_read: 'always',
};

function toPosix(filePath) {
  return filePath.split(path.sep).join('/');
}

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n/);
  if (!match) return null;
  const data = {};
  for (const line of match[1].split(/\r?\n/)) {
    const index = line.indexOf(':');
    if (index === -1) continue;
    data[line.slice(0, index).trim()] = line.slice(index + 1).trim();
  }
  return data;
}

async function run() {
  const failItems = [];

  for (const moduleName of MODULES) {
    const file = path.join(ROOT_DIR, moduleName, 'MAIN.md');
    const relativePath = toPosix(path.relative(ROOT_DIR, file));

    if (!fs.existsSync(file)) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: '[check-metadata] Missing canonical module.',
      });
      continue;
    }

    const metadata = parseFrontmatter(fs.readFileSync(file, 'utf8'));
    if (!metadata) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: '[check-metadata] Missing frontmatter.',
      });
      continue;
    }

    for (const [key, expected] of Object.entries(REQUIRED)) {
      if (metadata[key] !== expected) {
        failItems.push({
          level: 'fail',
          file: relativePath,
          message: `[check-metadata] ${key} must be ${expected}.`,
        });
      }
    }

    if (metadata.module !== moduleName) {
      failItems.push({
        level: 'fail',
        file: relativePath,
        message: `[check-metadata] module must be ${moduleName}.`,
      });
    }
  }

  return {
    name: 'check-metadata',
    fails: failItems.length,
    warnings: 0,
    issues: failItems,
  };
}

module.exports = { run };
