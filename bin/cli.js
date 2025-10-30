#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const COLORS = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
  red: '\x1b[31m',
};

const DEBUG = process.env.DEBUG === '1';

function log(message, color = 'reset') {
  console.log(`${COLORS[color]}${message}${COLORS.reset}`);
}

function debug(message) {
  if (DEBUG) {
    log(`[DEBUG] ${message}`, 'cyan');
  }
}

function getInstallTarget() {
  const args = process.argv.slice(2);

  // Check for --global or -g flag
  if (args.includes('--global') || args.includes('-g')) {
    return path.join(process.env.HOME, '.claude', 'skills');
  }

  // Check for --path flag
  const pathIndex = args.indexOf('--path');
  if (pathIndex !== -1 && args[pathIndex + 1]) {
    return path.resolve(args[pathIndex + 1]);
  }

  // Default to current project
  return path.join(process.cwd(), '.claude', 'skills');
}

function showHelp() {
  console.log(`
${COLORS.bright}BMAD Skills - Complete Workflow Ecosystem${COLORS.reset}

${COLORS.cyan}Usage:${COLORS.reset}
  npx bmad-skills              Install to current project (./.claude/skills)
  npx bmad-skills --global     Install globally (~/.claude/skills)
  npx bmad-skills --path PATH  Install to custom path

${COLORS.cyan}Options:${COLORS.reset}
  -g, --global                  Install to ~/.claude/skills
  --path PATH                   Install to custom directory
  -h, --help                    Show this help message
  -v, --version                 Show version

${COLORS.cyan}Environment:${COLORS.reset}
  DEBUG=1                       Enable debug logging

${COLORS.cyan}What gets installed:${COLORS.reset}
  • 12 integrated Claude Skills (BMAD + OpenSpec tracks)
  • Complete template library in assets/
  • Runtime workspace directories
  • Validation and helper scripts

${COLORS.cyan}After installation:${COLORS.reset}
  Skills are auto-activated in Claude Code conversations.
  See README.md for workflow documentation.

${COLORS.cyan}More info:${COLORS.reset}
  https://github.com/bacoco/bmad-skills
`);
}

function showVersion() {
  const pkg = require('../package.json');
  log(`v${pkg.version}`, 'cyan');
}

function createBackup(target) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 19);
  const backup = `${target}.backup.${timestamp}`;

  log(`⚠️  Existing installation found`, 'yellow');
  log(`   Creating backup: ${backup}`, 'yellow');
  debug(`Renaming ${target} -> ${backup}`);

  fs.renameSync(target, backup);
  log('');

  return backup;
}

function removeRecursive(dirPath) {
  if (fs.existsSync(dirPath)) {
    debug(`Removing directory: ${dirPath}`);
    fs.rmSync(dirPath, { recursive: true, force: true });
  }
}

function copyRecursive(src, dest) {
  debug(`Copying ${src} -> ${dest}`);
  const stats = fs.statSync(src);

  if (stats.isDirectory()) {
    if (!fs.existsSync(dest)) {
      fs.mkdirSync(dest, { recursive: true });
    }

    const entries = fs.readdirSync(src);
    for (const entry of entries) {
      copyRecursive(path.join(src, entry), path.join(dest, entry));
    }
  } else {
    fs.copyFileSync(src, dest);
  }
}

/**
 * Validate installation integrity
 * @throws {Error} If validation fails
 */
function validateInstallation(target) {
  debug('Starting installation validation...');

  // 1. Check MANIFEST.json exists and is valid JSON
  const manifestPath = path.join(target, '_config', 'MANIFEST.json');
  if (!fs.existsSync(manifestPath)) {
    throw new Error('MANIFEST.json not found in installation');
  }

  let manifest;
  try {
    const manifestContent = fs.readFileSync(manifestPath, 'utf8');
    manifest = JSON.parse(manifestContent);
    debug('MANIFEST.json parsed successfully');
  } catch (err) {
    throw new Error(`Invalid MANIFEST.json: ${err.message}`);
  }

  // Validate manifest structure
  if (!manifest.skills || !Array.isArray(manifest.skills)) {
    throw new Error('MANIFEST.json missing "skills" array');
  }

  if (!manifest.version) {
    throw new Error('MANIFEST.json missing "version" field');
  }

  debug(`Manifest version: ${manifest.version}, skills: ${manifest.skills.length}`);

  // 2. Check required directories exist
  const requiredDirs = [
    '_config',
    '_core',
    '_runtime',
  ];

  for (const dir of requiredDirs) {
    const dirPath = path.join(target, dir);
    if (!fs.existsSync(dirPath)) {
      throw new Error(`Required directory missing: ${dir}`);
    }
  }

  debug('Required directories verified');

  // 3. Check that skills listed in manifest exist
  const missingSkills = [];
  for (const skill of manifest.skills) {
    const skillId = typeof skill === 'string' ? skill : skill.id;
    const skillPath = path.join(target, skillId);
    const skillManifest = path.join(skillPath, 'SKILL.md');

    if (!fs.existsSync(skillPath) || !fs.existsSync(skillManifest)) {
      missingSkills.push(skillId);
    }
  }

  if (missingSkills.length > 0) {
    throw new Error(`Missing skills: ${missingSkills.join(', ')}`);
  }

  debug(`All ${manifest.skills.length} skills verified`);

  // 4. Check that each skill has required assets/ directory
  for (const skill of manifest.skills) {
    const skillId = typeof skill === 'string' ? skill : skill.id;
    const assetsPath = path.join(target, skillId, 'assets');
    if (!fs.existsSync(assetsPath)) {
      throw new Error(`Skill ${skillId} missing assets/ directory`);
    }
  }

  debug('All skill assets directories verified');

  log('✅ Installation validation passed', 'green');
}

/**
 * Atomic installation with automatic rollback
 */
function installSkills(target) {
  const sourceDir = path.join(__dirname, '..', '.claude', 'skills');
  const timestamp = Date.now();
  const tmpTarget = path.join(path.dirname(target), `.tmp-skills-install-${timestamp}`);

  let backupPath = null;

  log('📦 Installing BMAD Skills Bundle', 'bright');
  log(`Target: ${target}`, 'cyan');
  log('');

  try {
    // STEP 1: Install to temporary directory first
    debug(`Temporary installation path: ${tmpTarget}`);
    log('📋 Stage 1/5: Copying to temporary location...', 'blue');

    const tmpParent = path.dirname(tmpTarget);
    if (!fs.existsSync(tmpParent)) {
      fs.mkdirSync(tmpParent, { recursive: true });
    }

    copyRecursive(sourceDir, tmpTarget);
    debug('Copy to temporary location complete');

    // STEP 2: Create runtime workspace directories in temp installation
    log('📁 Stage 2/5: Creating runtime workspace...', 'blue');
    const runtimeDirs = [
      path.join(tmpTarget, '_runtime', 'workspace', 'changes'),
      path.join(tmpTarget, '_runtime', 'workspace', 'specs'),
      path.join(tmpTarget, '_runtime', 'workspace', 'artifacts'),
      path.join(tmpTarget, '_runtime', 'workspace', 'stories'),
    ];

    runtimeDirs.forEach(dir => {
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
        debug(`Created runtime directory: ${dir}`);
      }
    });

    // STEP 3: Validate temporary installation
    log('🔍 Stage 3/5: Validating installation integrity...', 'blue');
    validateInstallation(tmpTarget);

    // STEP 4: Backup existing installation (if any)
    if (fs.existsSync(target)) {
      log('💾 Stage 4/5: Backing up existing installation...', 'blue');
      backupPath = createBackup(target);
      debug(`Backup created at: ${backupPath}`);
    } else {
      log('📂 Stage 4/5: No existing installation to backup', 'blue');
      // Create parent directory if needed
      const targetParent = path.dirname(target);
      if (!fs.existsSync(targetParent)) {
        fs.mkdirSync(targetParent, { recursive: true });
      }
    }

    // STEP 5: Atomic rename (this is the critical operation)
    log('⚡ Stage 5/5: Atomic installation...', 'blue');
    debug(`Renaming ${tmpTarget} -> ${target}`);

    fs.renameSync(tmpTarget, target);
    debug('Atomic rename complete');

    log('');
    log('✅ Installation complete!', 'green');
    log('');

    // List installed skills
    log('📊 Installed skills:', 'bright');
    const skillDirs = fs.readdirSync(target)
      .filter(name => {
        const fullPath = path.join(target, name);
        return fs.statSync(fullPath).isDirectory() &&
               name.includes('-') &&
               !name.startsWith('_');
      })
      .sort();

    skillDirs.forEach(skill => {
      log(`   • ${skill}`, 'cyan');
    });

    log('');
    log('🚀 Next steps:', 'bright');
    log('   1. Skills will auto-activate in Claude Code conversations');
    log('   2. Try: "I have an idea for a new feature"');
    log('   3. Or: "What\'s my workflow status?"');
    log('');
    log('📖 Documentation: https://github.com/bacoco/bmad-skills', 'cyan');

    // Clean up backup after successful installation (optional)
    if (backupPath && fs.existsSync(backupPath)) {
      log('');
      log(`💡 Backup saved at: ${backupPath}`, 'cyan');
      log('   You can safely delete it after verifying the installation.', 'cyan');
    }

  } catch (error) {
    log('');
    log('❌ Installation failed!', 'red');
    log(`   Error: ${error.message}`, 'red');
    log('');

    // ROLLBACK: Restore from backup if it exists
    if (backupPath && fs.existsSync(backupPath)) {
      log('🔄 Attempting automatic rollback...', 'yellow');

      try {
        // Remove failed installation
        if (fs.existsSync(target)) {
          removeRecursive(target);
          debug('Removed failed installation');
        }

        // Restore from backup
        fs.renameSync(backupPath, target);
        debug('Restored from backup');

        log('✅ Rollback successful - previous installation restored', 'green');
      } catch (rollbackError) {
        log('❌ Rollback failed!', 'red');
        log(`   Error: ${rollbackError.message}`, 'red');
        log(`   Manual intervention required. Backup at: ${backupPath}`, 'yellow');
      }
    }

    // Clean up temporary directory
    if (fs.existsSync(tmpTarget)) {
      removeRecursive(tmpTarget);
      debug('Cleaned up temporary installation');
    }

    throw error;
  }
}

function main() {
  const args = process.argv.slice(2);

  if (args.includes('-h') || args.includes('--help')) {
    showHelp();
    return;
  }

  if (args.includes('-v') || args.includes('--version')) {
    showVersion();
    return;
  }

  try {
    const target = getInstallTarget();

    // Check if we're in the BMAD Skills repo itself (skip check in test mode)
    const manifestPath = path.join(process.cwd(), '.claude', 'skills', '_config', 'MANIFEST.json');
    if (fs.existsSync(manifestPath) && !process.env.BMAD_TEST_MODE) {
      log('⚠️  You are already in the BMAD Skills repository!', 'yellow');
      log('   No need to install. Use this repo directly.', 'yellow');
      process.exit(0);
    }

    installSkills(target);
  } catch (error) {
    log(`❌ Error: ${error.message}`, 'red');
    log('');
    log('For help, run: npx bmad-skills --help', 'cyan');
    if (DEBUG) {
      log('');
      log('Stack trace:', 'red');
      console.error(error);
    }
    process.exit(1);
  }
}

main();
