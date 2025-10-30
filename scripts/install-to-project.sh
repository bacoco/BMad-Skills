#!/bin/bash
# Install BMAD Skills to current project's .claude/skills

set -e

TARGET="./.claude/skills"
SOURCE="$(dirname "$0")/../.claude/skills"

# Check if already in BMad-Skills repo
if [ -f "./.claude/skills/_config/MANIFEST.json" ]; then
  echo "⚠️  You are already in the BMAD Skills repository!"
  echo "   No need to install. Use this repo directly."
  exit 0
fi

echo "📦 Installing BMAD Skills Bundle to current project"
echo "Target: $(pwd)/$TARGET"
echo ""

# Backup existing installation if it exists
if [ -d "$TARGET" ]; then
  BACKUP="$TARGET.backup.$(date +%Y%m%d_%H%M%S)"
  echo "⚠️  Existing .claude/skills found"
  echo "   Creating backup: $BACKUP"
  mv "$TARGET" "$BACKUP"
  echo ""
fi

# Create target directory
mkdir -p "$(dirname "$TARGET")"

# Copy entire bundle
echo "📋 Copying BMAD Skills bundle..."
cp -r "$SOURCE" "$TARGET"

# Create runtime workspace directories
echo "📁 Creating runtime workspace..."
mkdir -p "$TARGET/_runtime/workspace/changes"
mkdir -p "$TARGET/_runtime/workspace/specs"
mkdir -p "$TARGET/_runtime/workspace/artifacts"
mkdir -p "$TARGET/_runtime/workspace/stories"

echo ""
echo "✅ Installation complete for this project!"
echo ""
echo "📊 Installed skills:"
find "$TARGET" -maxdepth 1 -type d -name "*-*" ! -name "_*" -exec basename {} \; | sort | sed 's/^/   • /'

echo ""
echo "🔍 Verifying installation..."
bash "$(dirname "$0")/verify.sh" "$TARGET"
