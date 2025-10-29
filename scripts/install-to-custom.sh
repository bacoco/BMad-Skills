#!/bin/bash
# Install BMAD Skills to a custom path

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 <target-path>"
  exit 1
fi

TARGET="$1"
SOURCE="$(dirname "$0")/../.claude/skills"

# Expand tilde if present
TARGET="${TARGET/#\~/$HOME}"

echo "📦 Installing BMAD Skills Bundle"
echo "Target: $TARGET"
echo ""

# Backup existing installation if it exists
if [ -d "$TARGET" ]; then
  BACKUP="$TARGET.backup.$(date +%Y%m%d_%H%M%S)"
  echo "⚠️  Existing installation found"
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

# Create artifacts directories (for skill outputs)
mkdir -p "$TARGET/_runtime/artifacts"
mkdir -p "$TARGET/_runtime/stories"

echo ""
echo "✅ Installation complete!"
echo ""
echo "📊 Installed skills:"
find "$TARGET" -maxdepth 1 -type d -name "*-*" ! -name "_*" -exec basename {} \; | sort | sed 's/^/   • /'

echo ""
echo "🔍 Verifying installation..."
bash "$(dirname "$0")/verify.sh" "$TARGET"
