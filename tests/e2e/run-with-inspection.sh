#!/bin/bash
#
# Run E2E tests with manual inspection mode
#
# This script runs E2E tests and pauses before cleanup,
# allowing you to inspect generated artifacts manually.
#
# Usage:
#   ./tests/e2e/run-with-inspection.sh [pytest-args]
#
# Examples:
#   ./tests/e2e/run-with-inspection.sh                           # Run all E2E tests with pause
#   ./tests/e2e/run-with-inspection.sh -m smoke                  # Run only smoke tests
#   ./tests/e2e/run-with-inspection.sh test_bmad_workflows.py    # Run specific file
#

set -e

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=================================="
echo "E2E Tests with Manual Inspection"
echo -e "==================================${NC}\n"

echo -e "${YELLOW}Mode: PAUSE BEFORE CLEANUP${NC}"
echo "Tests will pause after execution to allow manual file inspection."
echo "Press ENTER to cleanup and continue to next test."
echo ""

# Set environment variable to enable pause
export E2E_PAUSE_BEFORE_CLEANUP=1

# Run pytest with provided arguments
echo -e "${GREEN}Running tests...${NC}\n"
python3 -m pytest tests/e2e/ -v "$@"

echo ""
echo -e "${GREEN}✅ All tests complete!${NC}"
