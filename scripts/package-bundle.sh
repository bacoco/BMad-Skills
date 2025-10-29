#!/bin/bash
# Create distributable BMAD Skills bundle

set -e

OUTPUT="build/bmad-skills-bundle.zip"
VERSION=$(grep -o '"version": *"[^"]*"' .claude/skills/_config/MANIFEST.json | head -1 | cut -d'"' -f4)

echo "📦 Creating BMAD Skills Bundle v$VERSION"
echo ""

# Create build directory
mkdir -p build

# Remove old bundle if it exists
if [ -f "$OUTPUT" ]; then
  echo "🗑️  Removing old bundle..."
  rm "$OUTPUT"
fi

# Package the entire .claude/skills directory
echo "📋 Packaging skills..."
cd .claude
zip -r -q "../$OUTPUT" skills/ \
  -x "*.pyc" \
  -x "*__pycache__*" \
  -x "*.DS_Store" \
  -x "*/.git/*"
cd ..

# Add install scripts
echo "📋 Adding installation scripts..."
zip -r -q "$OUTPUT" scripts/*.sh

# Add documentation
echo "📋 Adding documentation..."
zip -r -q "$OUTPUT" \
  README.md \
  CHANGELOG.md \
  requirements.txt \
  LICENSE 2>/dev/null || true

echo ""
echo "✅ Bundle created: $OUTPUT"
echo ""
echo "📊 Bundle size:"
du -h "$OUTPUT"
echo ""
echo "📦 Contents:"
unzip -l "$OUTPUT" | head -20
echo ""
echo "📤 Ready for distribution!"
echo ""
echo "🚀 Users can install with:"
echo "   unzip bmad-skills-bundle.zip"
echo "   bash scripts/install.sh"
