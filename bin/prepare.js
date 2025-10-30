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

function checkTemplateAssets() {
  log('\n📄 Checking template assets...', 'reset');

  const skillsDir = path.join(__dirname, '..', '.claude', 'skills');
  const entries = fs.readdirSync(skillsDir);

  const skills = entries.filter(name => {
    const fullPath = path.join(skillsDir, name);
    return fs.statSync(fullPath).isDirectory() &&
           name.includes('-') &&
           !name.startsWith('_');
  });

  let allValid = true;
  let foundCount = 0;
  const missing = [];

  // Check each skill's scripts for template references
  skills.forEach(skill => {
    const scriptsDir = path.join(skillsDir, skill, 'scripts');
    if (!fs.existsSync(scriptsDir)) return;

    const pyFiles = fs.readdirSync(scriptsDir).filter(f => f.endsWith('.py'));

    pyFiles.forEach(pyFile => {
      const scriptPath = path.join(scriptsDir, pyFile);
      const content = fs.readFileSync(scriptPath, 'utf8');

      // Extract template references from Python scripts
      // Pattern: ASSET_DIR / "template-name.md.template"
      const templateRegex = /ASSET(?:_DIR|S_DIR)\s*\/\s*["']([^"']+\.(?:template|jinja))["']/g;
      const mapRegex = /["']([^"']+\.(?:template|jinja))["']/g;

      let match;
      const templates = new Set();

      // Pattern 1: ASSET_DIR / "filename"
      while ((match = templateRegex.exec(content)) !== null) {
        templates.add(match[1]);
      }

      // Pattern 2: from TEMPLATE_MAP dictionaries
      const templateMapMatch = content.match(/TEMPLATE_MAP\s*=\s*{[^}]+}/s);
      if (templateMapMatch) {
        let m;
        while ((m = mapRegex.exec(templateMapMatch[0])) !== null) {
          if (m[1].endsWith('.template') || m[1].endsWith('.jinja')) {
            templates.add(m[1]);
          }
        }
      }

      // Check if templates exist
      templates.forEach(template => {
        const templatePath = path.join(skillsDir, skill, 'assets', template);
        if (fs.existsSync(templatePath)) {
          foundCount++;
        } else {
          missing.push({
            skill,
            script: pyFile,
            template,
          });
          allValid = false;
        }
      });
    });
  });

  if (missing.length > 0) {
    log(`  ✗ Missing ${missing.length} templates referenced by scripts:`, 'red');
    missing.forEach(item => {
      log(`    - ${item.skill}/${item.script} expects: ${item.template}`, 'red');
    });
    return false;
  }

  // Check for .jinja files (should all be .template now)
  const jinjaFiles = [];
  function findJinjaFiles(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    entries.forEach(entry => {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        findJinjaFiles(fullPath);
      } else if (entry.name.endsWith('.jinja')) {
        jinjaFiles.push(path.relative(skillsDir, fullPath));
      }
    });
  }
  findJinjaFiles(skillsDir);

  if (jinjaFiles.length > 0) {
    log(`  ✗ Found ${jinjaFiles.length} .jinja files (should be .template):`, 'red');
    jinjaFiles.forEach(file => log(`    - ${file}`, 'red'));
    allValid = false;
  }

  // Count total .template files
  const templateFiles = [];
  function findTemplateFiles(dir) {
    const entries = fs.readdirSync(dir, { withFileTypes: true });
    entries.forEach(entry => {
      const fullPath = path.join(dir, entry.name);
      if (entry.isDirectory()) {
        findTemplateFiles(fullPath);
      } else if (entry.name.endsWith('.template')) {
        templateFiles.push(fullPath);
      }
    });
  }
  findTemplateFiles(skillsDir);

  if (allValid) {
    log(`  ✓ All ${foundCount} script-referenced templates exist`, 'green');
    log(`  ✓ Found ${templateFiles.length} total .template files`, 'green');
    log(`  ✓ No .jinja files found (all migrated to .template)`, 'green');
  }

  return allValid;
}

function main() {
  log('🚀 Preparing BMAD Skills for publication', 'reset');

  const checks = [
    checkRequiredFiles(),
    checkSkillStructure(),
    checkManifestVersion(),
    checkTemplateAssets(),
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
