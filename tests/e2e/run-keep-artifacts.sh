#!/bin/bash
#
# Run E2E tests and KEEP all generated artifacts
#
# This script runs E2E tests WITHOUT cleanup.
# All generated files are preserved for inspection after tests complete.
#
# Usage:
#   ./tests/e2e/run-keep-artifacts.sh [pytest-args]
#
# Examples:
#   ./tests/e2e/run-keep-artifacts.sh                           # Run all, keep everything
#   ./tests/e2e/run-keep-artifacts.sh -m smoke                  # Run smoke, keep files
#
# Cleanup manually after:
#   rm -rf .claude/skills/_runtime/workspace/artifacts/*.md
#   rm -rf .claude/skills/_runtime/workspace/stories/*.md
#   rm -rf docs/
#

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=================================="
echo "E2E Tests - Keep All Artifacts"
echo -e "==================================${NC}\n"

echo -e "${YELLOW}Mode: KEEP ALL FILES${NC}"
echo "Tests will NOT cleanup generated files."
echo "All artifacts will be preserved for inspection."
echo ""

# Set environment variable to disable cleanup
export E2E_KEEP_ARTIFACTS=1

# Run pytest with provided arguments
echo -e "${GREEN}Running tests...${NC}\n"
python3 -m pytest tests/e2e/ -v "$@"

echo ""
echo -e "${GREEN}✅ All tests complete!${NC}"
echo ""
echo -e "${YELLOW}⚠️  Generated files have been preserved:${NC}"
echo "  - .claude/skills/_runtime/workspace/artifacts/"
echo "  - .claude/skills/_runtime/workspace/stories/"
echo "  - .claude/skills/_runtime/workspace/changes/"
echo "  - docs/ (if created)"
echo ""
echo "To clean up manually:"
echo "  rm -rf .claude/skills/_runtime/workspace/artifacts/*.md"
echo "  rm -rf .claude/skills/_runtime/workspace/stories/*.md"
echo "  rm -rf .claude/skills/_runtime/workspace/changes/*"
echo "  rm -rf docs/"
