#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const COLORS = {
  reset: '\x1b[0m',
  bright: '\x1b[1m',
  green: '\x1b[32m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  cyan: '\x1b[36m',
};

function log(message, color = 'reset') {
  console.log(`${COLORS[color]}${message}${COLORS.reset}`);
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

  fs.renameSync(target, backup);
  log('');
}

function copyRecursive(src, dest) {
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

function installSkills(target) {
  const sourceDir = path.join(__dirname, '..', '.claude', 'skills');

  log('📦 Installing BMAD Skills Bundle', 'bright');
  log(`Target: ${target}`, 'cyan');
  log('');

  // Backup existing installation
  if (fs.existsSync(target)) {
    createBackup(target);
  }

  // Create target directory
  const targetParent = path.dirname(target);
  if (!fs.existsSync(targetParent)) {
    fs.mkdirSync(targetParent, { recursive: true });
  }

  // Copy entire bundle
  log('📋 Copying BMAD Skills bundle...', 'blue');
  copyRecursive(sourceDir, target);

  // Create runtime workspace directories
  log('📁 Creating runtime workspace...', 'blue');
  const runtimeDirs = [
    path.join(target, '_runtime', 'workspace', 'changes'),
    path.join(target, '_runtime', 'workspace', 'specs'),
    path.join(target, '_runtime', 'artifacts'),
    path.join(target, '_runtime', 'stories'),
  ];

  runtimeDirs.forEach(dir => {
    if (!fs.existsSync(dir)) {
      fs.mkdirSync(dir, { recursive: true });
    }
  });

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

    // Check if we're in the BMAD Skills repo itself
    const manifestPath = path.join(process.cwd(), '.claude', 'skills', '_config', 'MANIFEST.json');
    if (fs.existsSync(manifestPath)) {
      log('⚠️  You are already in the BMAD Skills repository!', 'yellow');
      log('   No need to install. Use this repo directly.', 'yellow');
      process.exit(0);
    }

    installSkills(target);
  } catch (error) {
    log(`❌ Error: ${error.message}`, 'yellow');
    log('');
    log('For help, run: npx bmad-skills --help', 'cyan');
    process.exit(1);
  }
}

main();
