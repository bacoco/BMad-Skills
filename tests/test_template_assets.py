"""
Test that all templates referenced by Python scripts exist in assets/ directories.

This prevents packaging failures where scripts expect templates that are missing.
"""

import re
from pathlib import Path
import pytest

SKILLS_ROOT = Path(__file__).resolve().parents[1] / ".claude" / "skills"


def find_template_references_in_scripts():
    """
    Extract template file references from all Python scripts in skills/*/scripts/*.py

    Returns:
        list of tuples: [(skill_name, script_path, template_filename), ...]
    """
    references = []

    for skill_dir in SKILLS_ROOT.iterdir():
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue

        scripts_dir = skill_dir / "scripts"
        if not scripts_dir.exists():
            continue

        for script_file in scripts_dir.glob("*.py"):
            content = script_file.read_text()

            # Pattern 1: TEMPLATE_FILE = ASSET_DIR / "filename.md.template"
            matches = re.findall(
                r'ASSET(?:_DIR|S_DIR)\s*/\s*["\']([^"\']+\.(?:template|jinja))["\']',
                content
            )

            # Pattern 2: TEMPLATE_MAP = { "output": "template-name.md.template" }
            map_matches = re.findall(
                r'["\']([^"\']+\.(?:template|jinja))["\']',
                content
            )

            # Combine and deduplicate
            all_matches = set(matches + [m for m in map_matches if m.endswith(('.template', '.jinja'))])

            for template_name in all_matches:
                references.append((skill_dir.name, script_file, template_name))

    return references


def test_script_templates_exist():
    """
    Verify that all templates referenced by Python scripts exist in their assets/ directory.

    This is a critical packaging requirement: scripts will fail at runtime if templates
    are missing from the published bundle.
    """
    references = find_template_references_in_scripts()

    missing = []
    found = []

    for skill_name, script_path, template_name in references:
        skill_dir = SKILLS_ROOT / skill_name
        template_path = skill_dir / "assets" / template_name

        if not template_path.exists():
            missing.append({
                "skill": skill_name,
                "script": script_path.name,
                "template": template_name,
                "expected_path": template_path
            })
        else:
            found.append(template_name)

    if missing:
        error_msg = "\n\nMissing templates referenced by scripts:\n"
        for item in missing:
            error_msg += f"\n  ❌ {item['skill']}/{item['script']} expects:\n"
            error_msg += f"     {item['expected_path']}\n"

        pytest.fail(error_msg)

    # Report success
    print(f"\n✅ All {len(found)} script-referenced templates exist:")
    for template in sorted(set(found)):
        print(f"   - {template}")


def test_no_jinja_templates_in_bundle():
    """
    Verify that no .jinja template files exist in the bundle.

    All templates should use .template extension after the v2.1.8 migration.
    """
    jinja_files = list(SKILLS_ROOT.glob("**/*.jinja"))

    if jinja_files:
        error_msg = f"\n\n❌ Found {len(jinja_files)} .jinja files (should be .template):\n"
        for file in jinja_files:
            rel_path = file.relative_to(SKILLS_ROOT)
            error_msg += f"   - {rel_path}\n"

        pytest.fail(error_msg)


def test_template_count_stability():
    """
    Verify that the published bundle contains the expected .template files.

    Historically this test only asserted the count of templates. As the
    collection grew it became easy to miss accidental additions or removals.
    We now validate the full set of expected relative paths instead of just
    the total number.
    """
    templates = sorted(SKILLS_ROOT.glob("**/*.template"))
    actual_templates = {t.relative_to(SKILLS_ROOT) for t in templates}

    expected_templates = {
        Path("bmad-architecture-design/assets/architecture-script-template.md.template"),
        Path("bmad-observability-readiness/assets/instrumentation-backlog.csv.template"),
        Path("bmad-observability-readiness/assets/observability-plan.md.template"),
        Path("bmad-observability-readiness/assets/runbook-template.md.template"),
        Path("bmad-observability-readiness/assets/slo-dashboard-spec.md.template"),
        Path("bmad-performance-optimization/assets/benchmark-plan.md.template"),
        Path("bmad-performance-optimization/assets/optimization-backlog.csv.template"),
        Path("bmad-performance-optimization/assets/performance-brief.md.template"),
        Path("bmad-product-planning/assets/epics-wrapper-template.md.template"),
        Path("bmad-product-planning/assets/prd-script-template.md.template"),
        Path("bmad-security-review/assets/compliance-matrix.md.template"),
        Path("bmad-security-review/assets/remediation-backlog.csv.template"),
        Path("bmad-security-review/assets/security-gap-report.md.template"),
        Path("bmad-security-review/assets/threat-model-canvas.md.template"),
        Path("bmad-story-planning/assets/story-script-template.md.template"),
        Path("bmad-taskmaster-mcp-bootstrap/assets/taskmaster-bootstrap-report.md.template"),
        Path("openspec-change-closure/assets/archive-template.md.template"),
        Path("openspec-change-implementation/assets/execution-log-template.md.template"),
        Path("openspec-change-proposal/assets/proposal-template.md.template"),
        Path("openspec-change-proposal/assets/spec-delta-template.md.template"),
        Path("openspec-change-proposal/assets/tasks-template.md.template"),
    }

    missing = sorted(expected_templates - actual_templates)
    unexpected = sorted(actual_templates - expected_templates)

    if missing or unexpected:
        error_msg = "\n\n⚠️  Template set mismatch:\n"
        if missing:
            error_msg += "\nExpected but missing:\n"
            for path in missing:
                error_msg += f"   - {path}\n"
        if unexpected:
            error_msg += "\nUnexpected templates:\n"
            for path in unexpected:
                error_msg += f"   - {path}\n"

        error_msg += "\nUpdate expected_templates if this change is intentional.\n"

        pytest.fail(error_msg)

    # Sanity check to keep the human-friendly count in the assertion output
    assert len(actual_templates) == len(expected_templates)
