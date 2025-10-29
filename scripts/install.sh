#!/bin/bash
# BMAD Skills Bundle - Interactive Installer

set -e

echo "🚀 BMAD Skills Bundle Installer"
echo "================================"
echo ""
echo "BMAD is a complete workflow ecosystem with 12 integrated skills:"
echo "  • BMAD Workflow (8 skills): analyst, pm, ux, architecture, tea, stories, dev, orchestrator"
echo "  • OpenSpec (3 skills): propose, implement, archive"
echo "  • Skill Creator (1 skill): create new skills"
echo ""
echo "Where do you want to install BMAD Skills?"
echo "  1) ~/.claude/skills (global - all projects)"
echo "  2) ./.claude/skills (current project only)"
echo "  3) Custom path"
echo ""
read -p "Choose [1-3]: " choice

case $choice in
  1)
    echo ""
    bash "$(dirname "$0")/install-to-home.sh"
    ;;
  2)
    echo ""
    bash "$(dirname "$0")/install-to-project.sh"
    ;;
  3)
    read -p "Enter custom path: " custom_path
    echo ""
    bash "$(dirname "$0")/install-to-custom.sh" "$custom_path"
    ;;
  *)
    echo "❌ Invalid choice. Exiting."
    exit 1
    ;;
esac
