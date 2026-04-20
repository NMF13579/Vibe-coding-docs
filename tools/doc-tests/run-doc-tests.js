const { run: runLinks } = require('./check-links');
const { run: runMetadata } = require('./check-metadata');
const { run: runBootstrap } = require('./check-bootstrap');

function formatCheckLine(name, statusText) {
  const left = `[${name}]`;
  const targetWidth = 18;
  const spaces = Math.max(1, targetWidth - left.length);
  return `${left}${' '.repeat(spaces)}${statusText}`;
}

async function main() {
  const checks = [runLinks, runMetadata, runBootstrap];
  const results = [];
  let totalFails = 0;
  let totalWarnings = 0;

  for (const check of checks) {
    const result = await check();
    results.push(result);

    const issues = Array.isArray(result.issues) ? result.issues : [];
    for (const issue of issues) {
      const file = issue.file || 'unknown';
      const message = issue.message || 'Integrity issue';
      if (issue.level === 'fail') {
        console.log(`::error file=${file},line=1::${message}`);
      } else if (issue.level === 'warning') {
        console.log(`::warning file=${file},line=1::${message}`);
      }
    }

    totalFails += Number(result.fails || 0);
    totalWarnings += Number(result.warnings || 0);
  }

  for (const result of results) {
    if ((result.fails || 0) > 0) {
      console.log(formatCheckLine(result.name, `FAIL: ${result.fails}`));
    } else {
      console.log(formatCheckLine(result.name, 'PASS'));
    }
  }

  console.log('--- SUMMARY ---');
  console.log(`FAIL: ${totalFails}`);
  console.log(`WARNINGS: ${totalWarnings}`);

  if (totalFails > 0) {
    process.exit(1);
  }
  process.exit(0);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
