"""
Integration tests for CLI installation.

Tests that the CLI installs skills correctly to various targets.
"""

import subprocess
import os
import json
import shutil
import tempfile
from pathlib import Path
import pytest


@pytest.fixture
def temp_install_dir():
    """Create a temporary directory for installation tests."""
    tmp = tempfile.mkdtemp(prefix='bmad-test-')
    yield tmp
    # Cleanup
    if os.path.exists(tmp):
        shutil.rmtree(tmp)


def run_cli(args, check=True):
    """
    Run the CLI with given arguments.

    Args:
        args: List of CLI arguments
        check: Whether to raise exception on failure

    Returns:
        subprocess.CompletedProcess
    """
    cmd = ['node', 'bin/cli.js'] + args

    # Set test mode to allow running from repo
    env = os.environ.copy()
    env['BMAD_TEST_MODE'] = '1'

    result = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        check=check,
        cwd=os.getcwd(),
        env=env
    )
    return result


@pytest.mark.integration
def test_cli_help():
    """Test that CLI help command works."""
    result = run_cli(['--help'])
    assert result.returncode == 0
    assert 'BMAD Skills' in result.stdout
    assert 'Usage:' in result.stdout


@pytest.mark.integration
def test_cli_version():
    """Test that CLI version command works."""
    result = run_cli(['--version'])
    assert result.returncode == 0
    # Should output version number (strip ANSI color codes)
    import re
    clean_output = re.sub(r'\x1b\[[0-9;]*m', '', result.stdout.strip())
    assert clean_output.startswith('v')


@pytest.mark.integration
def test_cli_install_to_custom_path(temp_install_dir):
    """Test that CLI installs successfully to a custom path."""
    install_path = os.path.join(temp_install_dir, 'custom-skills')

    # Run installation
    result = run_cli(['--path', install_path])
    assert result.returncode == 0
    assert '✅ Installation complete!' in result.stdout

    # Verify installation structure
    assert os.path.exists(install_path), "Installation directory not created"

    # Check MANIFEST.json exists and is valid
    manifest_path = os.path.join(install_path, '_config', 'MANIFEST.json')
    assert os.path.exists(manifest_path), "MANIFEST.json not found"

    with open(manifest_path, 'r') as f:
        manifest = json.load(f)
        assert 'skills' in manifest
        assert 'version' in manifest
        assert len(manifest['skills']) > 0

    # Check required directories exist
    required_dirs = [
        '_config',
        '_core',
        '_runtime',
        '_runtime/workspace',
        '_runtime/workspace/changes',
        '_runtime/workspace/specs',
        '_runtime/workspace/artifacts',
        '_runtime/workspace/stories',
    ]

    for dir_name in required_dirs:
        dir_path = os.path.join(install_path, dir_name)
        assert os.path.exists(dir_path), f"Required directory missing: {dir_name}"

    # Check that skills listed in manifest exist
    for skill in manifest['skills']:
        skill_id = skill if isinstance(skill, str) else skill['id']
        skill_path = os.path.join(install_path, skill_id)
        skill_manifest = os.path.join(skill_path, 'SKILL.md')
        assert os.path.exists(skill_path), f"Skill directory missing: {skill_id}"
        assert os.path.exists(skill_manifest), f"SKILL.md missing for: {skill_id}"

        # Check assets directory exists
        assets_path = os.path.join(skill_path, 'assets')
        assert os.path.exists(assets_path), f"Assets directory missing for: {skill_id}"


@pytest.mark.integration
def test_cli_install_with_backup(temp_install_dir):
    """Test that CLI creates backup when reinstalling."""
    install_path = os.path.join(temp_install_dir, 'skills-with-backup')

    # First installation
    result1 = run_cli(['--path', install_path])
    assert result1.returncode == 0

    # Create a marker file to verify backup
    marker_file = os.path.join(install_path, '_config', 'test-marker.txt')
    os.makedirs(os.path.dirname(marker_file), exist_ok=True)
    with open(marker_file, 'w') as f:
        f.write('original installation')

    # Second installation (should create backup)
    result2 = run_cli(['--path', install_path])
    assert result2.returncode == 0
    assert 'backup' in result2.stdout.lower()

    # Verify backup was created (backup has .backup. in its name)
    all_dirs = os.listdir(temp_install_dir)
    backup_dirs = [d for d in all_dirs if '.backup.' in d]
    assert len(backup_dirs) > 0, f"Backup directory not created. Found dirs: {all_dirs}"

    # Verify marker file is in backup (not in new installation)
    backup_marker = os.path.join(temp_install_dir, backup_dirs[0], '_config', 'test-marker.txt')
    assert os.path.exists(backup_marker), f"Backup does not contain original files. Checked: {backup_marker}, backup_dirs: {backup_dirs}"

    # New installation should not have marker
    new_marker = os.path.join(install_path, '_config', 'test-marker.txt')
    assert not os.path.exists(new_marker), "New installation contains old files"


@pytest.mark.integration
def test_cli_validation_integrity(temp_install_dir):
    """Test that CLI validates installation integrity."""
    install_path = os.path.join(temp_install_dir, 'validated-install')

    # Run installation
    result = run_cli(['--path', install_path])
    assert result.returncode == 0

    # Verify validation messages appear
    assert 'Validating installation integrity' in result.stdout
    assert '✅ Installation validation passed' in result.stdout


@pytest.mark.integration
def test_cli_installed_skills_count(temp_install_dir):
    """Test that all expected skills are installed."""
    install_path = os.path.join(temp_install_dir, 'skills-count')

    # Run installation
    result = run_cli(['--path', install_path])
    assert result.returncode == 0

    # Count installed skills
    skill_dirs = [
        d for d in os.listdir(install_path)
        if os.path.isdir(os.path.join(install_path, d))
        and '-' in d
        and not d.startswith('_')
    ]

    # We expect 12 skills
    assert len(skill_dirs) == 12, f"Expected 12 skills, found {len(skill_dirs)}: {skill_dirs}"

    # Verify key skills are present
    expected_skills = [
        'main-workflow-router',
        'bmad-discovery-research',
        'bmad-product-planning',
        'bmad-development-execution',
        'openspec-change-proposal',
        'openspec-change-implementation',
        'openspec-change-closure',
        'core-skill-creation',
    ]

    for expected in expected_skills:
        assert expected in skill_dirs, f"Expected skill missing: {expected}"


@pytest.mark.integration
def test_cli_runtime_workspace_structure(temp_install_dir):
    """Test that runtime workspace is created with correct structure."""
    install_path = os.path.join(temp_install_dir, 'runtime-test')

    # Run installation
    result = run_cli(['--path', install_path])
    assert result.returncode == 0

    # Verify workspace structure
    workspace_path = os.path.join(install_path, '_runtime', 'workspace')
    assert os.path.exists(workspace_path)

    # Check subdirectories
    subdirs = ['changes', 'specs', 'artifacts', 'stories']
    for subdir in subdirs:
        subdir_path = os.path.join(workspace_path, subdir)
        assert os.path.exists(subdir_path), f"Workspace subdirectory missing: {subdir}"
        assert os.path.isdir(subdir_path), f"Workspace path is not a directory: {subdir}"


@pytest.mark.integration
def test_cli_manifest_consistency(temp_install_dir):
    """Test that installed MANIFEST matches source MANIFEST."""
    install_path = os.path.join(temp_install_dir, 'manifest-check')

    # Run installation
    result = run_cli(['--path', install_path])
    assert result.returncode == 0

    # Load installed manifest
    installed_manifest_path = os.path.join(install_path, '_config', 'MANIFEST.json')
    with open(installed_manifest_path, 'r') as f:
        installed_manifest = json.load(f)

    # Load source manifest
    source_manifest_path = os.path.join('.claude', 'skills', '_config', 'MANIFEST.json')
    with open(source_manifest_path, 'r') as f:
        source_manifest = json.load(f)

    # Compare key fields
    assert installed_manifest['version'] == source_manifest['version']
    assert installed_manifest['skills'] == source_manifest['skills']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
