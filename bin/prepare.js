#!/usr/bin/env node

/**
 * NPM prepare hook - runs before npm publish
 * Validates the bundle is ready for distribution
 */

const fs = require('fs');
const path = require('path');

const COLORS = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
};

function log(message, color = 'reset') {
  console.log(`${COLORS[color]}${message}${COLORS.reset}`);
}

function checkRequiredFiles() {
  const required = [
    '.claude/skills/_config/MANIFEST.json',
    '.claude/skills/_config/STYLE-GUIDE.md',
    'README.md',
    'LICENSE',
    'bin/cli.js',
  ];

  log('\n📋 Checking required files...', 'reset');

  let allPresent = true;
  required.forEach(file => {
    const exists = fs.existsSync(path.join(__dirname, '..', file));
    const status = exists ? '✓' : '✗';
    const color = exists ? 'green' : 'red';
    log(`  ${status} ${file}`, color);
    if (!exists) allPresent = false;
  });

  return allPresent;
}

function checkSkillStructure() {
  log('\n📦 Validating skill structure...', 'reset');

  const skillsDir = path.join(__dirname, '..', '.claude', 'skills');
  const entries = fs.readdirSync(skillsDir);

  const skills = entries.filter(name => {
    const fullPath = path.join(skillsDir, name);
    return fs.statSync(fullPath).isDirectory() &&
           name.includes('-') &&
           !name.startsWith('_');
  });

  log(`  Found ${skills.length} skills`, 'green');

  let allValid = true;
  skills.forEach(skill => {
    const skillPath = path.join(skillsDir, skill);
    const required = ['SKILL.md', 'REFERENCE.md', 'WORKFLOW.md', 'CHECKLIST.md', 'assets', 'scripts'];

    const missing = required.filter(file => !fs.existsSync(path.join(skillPath, file)));

    if (missing.length > 0) {
      log(`  ✗ ${skill}: missing ${missing.join(', ')}`, 'red');
      allValid = false;
    } else {
      log(`  ✓ ${skill}`, 'green');
    }
  });

  return allValid;
}

function checkManifestVersion() {
  log('\n🔢 Checking version consistency...', 'reset');

  const pkg = require('../package.json');
  const manifestPath = path.join(__dirname, '..', '.claude', 'skills', '_config', 'MANIFEST.json');
  const manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf8'));

  const pkgVersion = pkg.version;
  const skillVersions = manifest.skills.map(s => s.version);
  const allSame = skillVersions.every(v => v === pkgVersion);

  if (allSame) {
    log(`  ✓ All versions match: ${pkgVersion}`, 'green');
    return true;
  } else {
    log(`  ✗ Version mismatch:`, 'red');
    log(`    package.json: ${pkgVersion}`, 'yellow');
    log(`    skills: ${[...new Set(skillVersions)].join(', ')}`, 'yellow');
    return false;
  }
}

function main() {
  log('🚀 Preparing BMAD Skills for publication', 'reset');

  const checks = [
    checkRequiredFiles(),
    checkSkillStructure(),
    checkManifestVersion(),
  ];

  const allPassed = checks.every(result => result);

  if (allPassed) {
    log('\n✅ All validation checks passed!', 'green');
    log('   Bundle is ready for publication.\n', 'green');
    process.exit(0);
  } else {
    log('\n❌ Validation failed. Please fix the issues above.\n', 'red');
    process.exit(1);
  }
}

main();
