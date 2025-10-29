#!/bin/bash
# Verify BMAD Skills installation

TARGET="${1:-$HOME/.claude/skills}"

# Expand tilde if present
TARGET="${TARGET/#\~/$HOME}"

echo ""
echo "🔍 Verifying BMAD Skills installation"
echo "Location: $TARGET"
echo ""

# Critical paths to check
declare -a checks=(
  "$TARGET/_core/glossary.md:Core glossary"
  "$TARGET/_core/constraints.md:Core constraints"
  "$TARGET/_core/quality-gates.md:Quality gates"
  "$TARGET/_config/MANIFEST.json:Configuration manifest"
  "$TARGET/_config/STYLE-GUIDE.md:Style guide"
  "$TARGET/_runtime/workspace:Runtime workspace"
  "$TARGET/_docs:Documentation"
  "$TARGET/bmad-orchestrator/SKILL.md:Orchestrator skill"
  "$TARGET/bmad-analyst/SKILL.md:Analyst skill"
  "$TARGET/bmad-pm/SKILL.md:PM skill"
  "$TARGET/bmad-ux/SKILL.md:UX skill"
  "$TARGET/bmad-architecture/SKILL.md:Architecture skill"
  "$TARGET/bmad-tea/SKILL.md:TEA skill"
  "$TARGET/bmad-stories/SKILL.md:Stories skill"
  "$TARGET/bmad-dev/SKILL.md:Dev skill"
  "$TARGET/openspec-propose/SKILL.md:OpenSpec Propose"
  "$TARGET/openspec-implement/SKILL.md:OpenSpec Implement"
  "$TARGET/openspec-archive/SKILL.md:OpenSpec Archive"
  "$TARGET/skill-creator/SKILL.md:Skill Creator"
)

all_good=true
for check in "${checks[@]}"; do
  IFS=':' read -r path desc <<< "$check"
  if [ -e "$path" ]; then
    echo "✅ $desc"
  else
    echo "❌ $desc (missing: $path)"
    all_good=false
  fi
done

echo ""
if [ "$all_good" = true ]; then
  echo "✅ Installation verified successfully!"
  echo ""
  echo "🎯 Next steps:"
  echo "   1. Start a new chat with Claude Code"
  echo "   2. Skills activate automatically based on conversation:"
  echo "      • 'I have an idea...' → bmad-analyst"
  echo "      • 'Create a PRD' → bmad-pm"
  echo "      • 'Fix this bug' → openspec-propose"
  echo "      • 'What's next?' → bmad-orchestrator"
  echo ""
  echo "📚 Documentation: $TARGET/_docs/guides/quickstart-conversational.md"
  exit 0
else
  echo "❌ Installation verification failed!"
  echo "   Some files are missing. Please try reinstalling."
  exit 1
fi
