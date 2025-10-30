#!/bin/bash
#
# Full Workflow Integration Test
#
# Tests the complete installation and workflow initialization process.
# This validates that:
# 1. CLI installs bundle successfully
# 2. Python modules are importable
# 3. Workflow can be initialized
# 4. Scripts can access core tooling
#

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Test configuration
TEST_DIR="/tmp/bmad-workflow-test-$$"
PROJECT_NAME="TestProject"
PROJECT_TYPE="API"
COMPLEXITY_LEVEL=2
INITIATED_BY="TestUser"

# Cleanup function
cleanup() {
    if [ -d "$TEST_DIR" ]; then
        echo -e "${YELLOW}Cleaning up test directory...${NC}"
        rm -rf "$TEST_DIR"
    fi
}

# Set trap to cleanup on exit
trap cleanup EXIT

echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo -e "${BLUE}   Full Workflow Integration Test${NC}"
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo ""

# Step 1: Install bundle
echo -e "${BLUE}[1/5] Installing BMAD Skills bundle...${NC}"
export BMAD_TEST_MODE=1
node bin/cli.js --path "$TEST_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Installation failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Installation successful${NC}"
echo ""

# Step 2: Verify installation structure
echo -e "${BLUE}[2/5] Verifying installation structure...${NC}"

# Check critical directories
REQUIRED_DIRS=(
    "$TEST_DIR/_config"
    "$TEST_DIR/_core"
    "$TEST_DIR/_core/tooling"
    "$TEST_DIR/_runtime"
    "$TEST_DIR/_runtime/workspace"
    "$TEST_DIR/main-workflow-router"
    "$TEST_DIR/bmad-discovery-research"
)

for dir in "${REQUIRED_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        echo -e "${RED}✗ Required directory missing: $dir${NC}"
        exit 1
    fi
done

echo -e "${GREEN}✓ Directory structure valid${NC}"
echo ""

# Step 3: Test Python module imports
echo -e "${BLUE}[3/5] Testing Python module imports...${NC}"

python3 << EOF
import sys
sys.path.insert(0, '$TEST_DIR/_core/tooling')

# Test core module imports
try:
    from activation_metrics import ActivationMetrics
    print("  ✓ activation_metrics module imports")
except ImportError as e:
    print(f"  ✗ Failed to import activation_metrics: {e}")
    sys.exit(1)

# Test workflow status imports
try:
    sys.path.insert(0, '$TEST_DIR/main-workflow-router/scripts')
    from workflow_status import WorkflowStatus
    print("  ✓ workflow_status module imports")
except ImportError as e:
    print(f"  ✗ Failed to import workflow_status: {e}")
    sys.exit(1)

EOF

if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Module import test failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Module imports successful${NC}"
echo ""

# Step 4: Test workflow initialization
echo -e "${BLUE}[4/5] Testing workflow initialization...${NC}"

python3 << EOF
import sys
import os
from pathlib import Path

# Setup paths
skills_root = Path('$TEST_DIR')
sys.path.insert(0, str(skills_root / '_core' / 'tooling'))
sys.path.insert(0, str(skills_root / 'main-workflow-router' / 'scripts'))

from workflow_status import WorkflowStatus

# Initialize workflow
try:
    manager = WorkflowStatus()
    manager.init_workflow(
        project_name='$PROJECT_NAME',
        project_type='$PROJECT_TYPE',
        project_level=$COMPLEXITY_LEVEL,
        user_name='$INITIATED_BY'
    )
    print("  ✓ Workflow initialized successfully")

    # Verify workflow file was created
    workflow_file = skills_root / '_runtime' / 'workspace' / 'artifacts' / 'workflow-status.md'
    if not workflow_file.exists():
        print(f"  ✗ Workflow status file not created at {workflow_file}")
        sys.exit(1)
    print("  ✓ Workflow status file created")

    # Read and validate workflow data
    with open(workflow_file, 'r') as f:
        data = f.read()

    if '$PROJECT_NAME' not in data:
        print(f"  ✗ Project name not found in workflow file")
        sys.exit(1)
    print("  ✓ Workflow data validated")

except Exception as e:
    print(f"  ✗ Workflow initialization failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

EOF

if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Workflow initialization test failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Workflow initialization successful${NC}"
echo ""

# Step 5: Test core tooling access
echo -e "${BLUE}[5/5] Testing core tooling access...${NC}"

# Test that activation metrics can be loaded
python3 << EOF
import sys
from pathlib import Path

skills_root = Path('$TEST_DIR')
sys.path.insert(0, str(skills_root / '_core' / 'tooling'))

from activation_metrics import ActivationMetrics

try:
    metrics = ActivationMetrics(skills_root)
    print("  ✓ ActivationMetrics instantiated")

    # Test that glossary can be accessed
    glossary_path = skills_root / '_core' / 'glossary.md'
    if not glossary_path.exists():
        print(f"  ✗ Glossary file not found at {glossary_path}")
        sys.exit(1)
    print("  ✓ Glossary file accessible")

    # Test that constraints can be accessed
    constraints_path = skills_root / '_core' / 'constraints.md'
    if not constraints_path.exists():
        print(f"  ✗ Constraints file not found at {constraints_path}")
        sys.exit(1)
    print("  ✓ Constraints file accessible")

except Exception as e:
    print(f"  ✗ Core tooling test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

EOF

if [ $? -ne 0 ]; then
    echo -e "${RED}✗ Core tooling test failed${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Core tooling access successful${NC}"
echo ""

# Final summary
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ All workflow tests passed!${NC}"
echo -e "${BLUE}════════════════════════════════════════════${NC}"
echo ""
echo "Test directory: $TEST_DIR"
echo "Note: Test directory will be automatically cleaned up"
echo ""

exit 0
