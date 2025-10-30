"""
Pytest configuration and fixtures for E2E tests.
"""

import shutil
import pytest
import sys
from pathlib import Path

# Add helpers to path
sys.path.insert(0, str(Path(__file__).parent / "helpers"))

from claude_client import ClaudeClient
from session_manager import SessionManager
from output_validator import OutputValidator
from workspace_snapshot import WorkspaceSnapshot


@pytest.fixture(scope="session")
def skills_root():
    """Path to .claude/skills directory."""
    # Assume tests run from repo root
    root = Path(".claude/skills").resolve()
    if not root.exists():
        pytest.skip("Skills not installed. Run: bash scripts/install-to-project.sh")
    return root


@pytest.fixture(scope="session")
def runtime_workspace(skills_root):
    """Path to _runtime/workspace directory."""
    workspace = skills_root / "_runtime" / "workspace"
    workspace.mkdir(parents=True, exist_ok=True)
    return workspace


@pytest.fixture
def isolated_workspace(tmp_path, runtime_workspace):
    """
    Create an isolated workspace for a single test.

    Copies the runtime workspace template to a temp directory,
    runs the test, then cleans up.
    """
    # Create temp workspace
    temp_workspace = tmp_path / "workspace"
    temp_workspace.mkdir()

    # Create subdirectories
    (temp_workspace / "artifacts").mkdir()
    (temp_workspace / "stories").mkdir()
    (temp_workspace / "changes").mkdir()
    (temp_workspace / "specs").mkdir()

    # If runtime workspace has templates, copy them
    for subdir in ["artifacts", "stories", "changes", "specs"]:
        source = runtime_workspace / subdir
        dest = temp_workspace / subdir
        if source.exists():
            for item in source.glob("*.template*"):
                if item.is_file():
                    shutil.copy(item, dest)

    yield temp_workspace

    # Cleanup happens automatically via tmp_path
    pass


@pytest.fixture(scope="session")
def claude_client():
    """Shared ClaudeClient instance with reasonable timeout."""
    return ClaudeClient(timeout=120)


@pytest.fixture
def session_manager(runtime_workspace, claude_client):
    """
    SessionManager for multi-turn tests.

    Uses the real runtime workspace (not isolated) to test
    actual artifact generation.
    """
    manager = SessionManager(
        workspace_root=runtime_workspace,
        client=claude_client,
        verbose=True  # Print execution details
    )

    yield manager

    # Cleanup
    manager.cleanup()


@pytest.fixture(scope="session")
def output_validator(skills_root):
    """OutputValidator instance."""
    return OutputValidator(skills_root=skills_root)


@pytest.fixture
def workspace_snapshot(runtime_workspace):
    """Factory for creating workspace snapshots."""
    def _capture(**kwargs):
        return WorkspaceSnapshot.capture(runtime_workspace, **kwargs)
    return _capture


@pytest.fixture(autouse=True)
def log_test_info(request):
    """Automatically log test name at start."""
    print(f"\n{'='*70}")
    print(f"Test: {request.node.name}")
    print(f"{'='*70}")
    yield
    print(f"{'='*70}\n")


# Markers for categorizing tests
def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line(
        "markers", "e2e: End-to-end integration tests using claude CLI"
    )
    config.addinivalue_line(
        "markers", "smoke: Quick smoke tests for basic functionality"
    )
    config.addinivalue_line(
        "markers", "slow: Slow tests that take >1 minute"
    )
    config.addinivalue_line(
        "markers", "expensive: Tests that consume significant API credits"
    )
    config.addinivalue_line(
        "markers", "bmad: Tests for BMAD workflow (L2-4)"
    )
    config.addinivalue_line(
        "markers", "openspec: Tests for OpenSpec workflow (L0-1)"
    )


# Budget tracking
@pytest.fixture(scope="session", autouse=True)
def track_total_cost(claude_client):
    """Track and report total cost of test run."""
    yield

    stats = claude_client.get_stats()
    print(f"\n{'='*70}")
    print(f"E2E Test Run Summary")
    print(f"{'='*70}")
    print(f"Total API calls: {stats['total_calls']}")
    print(f"Total cost: ${stats['total_cost_usd']:.4f}")
    if stats['total_calls'] > 0:
        print(f"Average cost per call: ${stats['avg_cost_per_call']:.4f}")
    print(f"{'='*70}\n")
