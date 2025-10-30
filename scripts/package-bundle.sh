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

# Generate SHA256 checksum
echo ""
echo "🔐 Generating SHA256 checksum..."
CHECKSUM_FILE="build/SHA256SUMS"

if command -v shasum &> /dev/null; then
  # macOS/BSD
  shasum -a 256 "$OUTPUT" > "$CHECKSUM_FILE"
elif command -v sha256sum &> /dev/null; then
  # Linux
  sha256sum "$OUTPUT" > "$CHECKSUM_FILE"
else
  echo "⚠️  Warning: No SHA256 utility found (install coreutils)"
  touch "$CHECKSUM_FILE"  # Create empty file
fi

if [ -s "$CHECKSUM_FILE" ]; then
  echo "✅ Checksum saved to: $CHECKSUM_FILE"
  cat "$CHECKSUM_FILE"
else
  echo "⚠️  Warning: Checksum file is empty"
fi

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
echo ""
echo "🔐 Verify checksum:"
echo "   shasum -a 256 -c build/SHA256SUMS"
