"""
Unit tests for activation_metrics.py

Tests the BMAD Skills Activation Metrics System:
- Metrics logging
- Statistics generation
- Pattern analysis
- Report export
- Error handling
"""

import pytest
import yaml
import tempfile
import shutil
from pathlib import Path
import sys

# Add activation_metrics.py to path
SKILLS_ROOT = Path(__file__).resolve().parents[2] / ".claude" / "skills"
sys.path.insert(0, str(SKILLS_ROOT / "_core" / "tooling"))

from activation_metrics import ActivationMetrics


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests."""
    tmpdir = tempfile.mkdtemp()
    yield Path(tmpdir)
    shutil.rmtree(tmpdir)


@pytest.fixture
def metrics_file(temp_dir):
    """Create temporary metrics file path."""
    return temp_dir / "test-metrics.yaml"


class TestActivationMetricsInit:
    """Test ActivationMetrics initialization."""

    def test_init_creates_parent_directory(self, temp_dir):
        """Test that initialization creates parent directory."""
        metrics_path = temp_dir / "new" / "nested" / "metrics.yaml"
        metrics = ActivationMetrics(metrics_file=str(metrics_path))

        # Parent directory should be created
        assert metrics_path.parent.exists()

    def test_init_default_path(self):
        """Test initialization with default path."""
        metrics = ActivationMetrics()

        assert metrics.metrics_file.name == "activation-metrics.yaml"


class TestLogActivation:
    """Test activation logging functionality."""

    def test_log_activation_creates_entry(self, metrics_file):
        """Test that log_activation creates metrics entry."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation(
            skill_name="bmad-product-planning",
            trigger_phrase="create a PRD",
            confidence=0.95
        )

        # Metrics file should exist
        assert metrics_file.exists()

        # Load and verify
        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        assert len(data['activations']) == 1
        activation = data['activations'][0]

        assert activation['skill'] == "bmad-product-planning"
        assert activation['trigger'] == "create a PRD"
        assert activation['confidence'] == 0.95
        assert activation['success'] is True

    def test_log_activation_with_context(self, metrics_file):
        """Test logging activation with context."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        context = {
            'phase': 'Planning',
            'previous_skill': 'bmad-discovery-research',
            'artifacts': ['PRD.md']
        }

        metrics.log_activation(
            skill_name="bmad-architecture-design",
            trigger_phrase="design the architecture",
            confidence=0.88,
            context=context
        )

        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        activation = data['activations'][0]
        assert activation['context'] == context

    def test_log_activation_failed(self, metrics_file):
        """Test logging failed activation."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation(
            skill_name="bmad-ux-design",
            trigger_phrase="create wireframes",
            confidence=0.65,
            success=False,
            notes="Missing prerequisites"
        )

        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        activation = data['activations'][0]
        assert activation['success'] is False
        assert activation['notes'] == "Missing prerequisites"
        assert data['summary']['failed_activations'] == 1

    def test_log_activation_updates_summary(self, metrics_file):
        """Test that logging updates summary statistics."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("skill-1", "trigger 1", 0.9)
        metrics.log_activation("skill-2", "trigger 2", 0.8)
        metrics.log_activation("skill-1", "trigger 3", 0.85)

        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        summary = data['summary']

        assert summary['total_activations'] == 3
        assert summary['successful_activations'] == 3
        assert summary['by_skill']['skill-1'] == 2
        assert summary['by_skill']['skill-2'] == 1

    def test_log_activation_validation_empty_skill(self, metrics_file):
        """Test validation rejects empty skill name."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        with pytest.raises(ValueError, match="skill name is required"):
            metrics.log_activation("", "trigger", 0.9)

    def test_log_activation_validation_empty_trigger(self, metrics_file):
        """Test validation rejects empty trigger phrase."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        with pytest.raises(ValueError, match="trigger phrase is required"):
            metrics.log_activation("skill-1", "", 0.9)

    def test_log_activation_validation_invalid_confidence(self, metrics_file):
        """Test validation rejects invalid confidence values."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Confidence > 1
        with pytest.raises(ValueError, match="confidence must be between 0 and 1"):
            metrics.log_activation("skill-1", "trigger", 1.5)

        # Confidence < 0
        with pytest.raises(ValueError, match="confidence must be between 0 and 1"):
            metrics.log_activation("skill-1", "trigger", -0.5)

        # Non-numeric confidence
        with pytest.raises(ValueError, match="confidence must be a number"):
            metrics.log_activation("skill-1", "trigger", "high")

    def test_log_activation_validation_invalid_context(self, metrics_file):
        """Test validation rejects non-dict context."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        with pytest.raises(ValueError, match="context must be a dictionary"):
            metrics.log_activation("skill-1", "trigger", 0.9, context="invalid")


class TestGetStats:
    """Test statistics generation."""

    def test_get_stats_empty_metrics(self, metrics_file):
        """Test stats for empty metrics."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        stats = metrics.get_stats()

        assert stats['total'] == 0
        assert stats['success_rate'] == 0
        assert stats['by_skill'] == {}
        assert stats['common_triggers'] == []
        assert stats['avg_confidence'] == 0

    def test_get_stats_calculates_success_rate(self, metrics_file):
        """Test success rate calculation."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # 3 successful, 1 failed
        metrics.log_activation("skill-1", "trigger 1", 0.9, success=True)
        metrics.log_activation("skill-2", "trigger 2", 0.8, success=True)
        metrics.log_activation("skill-3", "trigger 3", 0.7, success=True)
        metrics.log_activation("skill-4", "trigger 4", 0.6, success=False)

        stats = metrics.get_stats()

        assert stats['total'] == 4
        assert stats['successful'] == 3
        assert stats['failed'] == 1
        assert stats['success_rate'] == 75.0

    def test_get_stats_by_skill(self, metrics_file):
        """Test stats by skill aggregation."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("bmad-product-planning", "create PRD", 0.95)
        metrics.log_activation("bmad-architecture-design", "design arch", 0.88)
        metrics.log_activation("bmad-product-planning", "write PRD", 0.92)
        metrics.log_activation("bmad-architecture-design", "architecture", 0.85)
        metrics.log_activation("bmad-product-planning", "PRD document", 0.90)

        stats = metrics.get_stats()

        assert stats['by_skill']['bmad-product-planning'] == 3
        assert stats['by_skill']['bmad-architecture-design'] == 2

    def test_get_stats_common_triggers(self, metrics_file):
        """Test common triggers identification."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("skill-1", "create PRD", 0.9)
        metrics.log_activation("skill-2", "create PRD", 0.9)
        metrics.log_activation("skill-3", "create PRD", 0.9)
        metrics.log_activation("skill-4", "design architecture", 0.8)
        metrics.log_activation("skill-5", "design architecture", 0.8)

        stats = metrics.get_stats()

        # Should return list of (trigger, count) tuples
        assert len(stats['common_triggers']) == 2
        assert stats['common_triggers'][0] == ("create PRD", 3)
        assert stats['common_triggers'][1] == ("design architecture", 2)

    def test_get_stats_avg_confidence(self, metrics_file):
        """Test average confidence calculation."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("skill-1", "trigger 1", 1.0)
        metrics.log_activation("skill-2", "trigger 2", 0.8)
        metrics.log_activation("skill-3", "trigger 3", 0.6)

        stats = metrics.get_stats()

        # Average: (1.0 + 0.8 + 0.6) / 3 = 0.8
        assert stats['avg_confidence'] == 0.80

    def test_get_stats_low_confidence_activations(self, metrics_file):
        """Test low confidence activation detection."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("skill-1", "trigger 1", 0.95)
        metrics.log_activation("skill-2", "trigger 2", 0.65)
        metrics.log_activation("skill-3", "trigger 3", 0.55)
        metrics.log_activation("skill-4", "trigger 4", 0.85)

        stats = metrics.get_stats()

        # Should include activations with confidence < 0.7
        low_conf = stats['low_confidence_activations']

        assert len(low_conf) == 2
        assert any(a['skill'] == 'skill-2' and a['confidence'] == 0.65 for a in low_conf)
        assert any(a['skill'] == 'skill-3' and a['confidence'] == 0.55 for a in low_conf)


class TestAnalyzePatterns:
    """Test pattern analysis functionality."""

    def test_analyze_patterns_empty_metrics(self, metrics_file):
        """Test pattern analysis with no data."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        patterns = metrics.analyze_patterns()

        assert 'insights' in patterns
        assert 'recommendations' in patterns
        assert len(patterns['insights']) == 0

    def test_analyze_patterns_underutilized_skills(self, metrics_file):
        """Test detection of underutilized skills."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Create 25 activations, mostly for one skill
        for i in range(23):
            metrics.log_activation("bmad-product-planning", f"trigger {i}", 0.9)

        metrics.log_activation("bmad-architecture-design", "arch trigger", 0.9)
        metrics.log_activation("bmad-ux-design", "ux trigger", 0.9)

        patterns = metrics.analyze_patterns()

        # Should detect underutilized skills
        assert any("underutilized" in insight for insight in patterns['insights'])

    def test_analyze_patterns_failed_activations(self, metrics_file):
        """Test analysis of failed activations."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Create some failed activations
        for i in range(3):
            metrics.log_activation("bmad-architecture-design", f"trigger {i}", 0.8, success=False)

        metrics.log_activation("bmad-product-planning", "trigger", 0.9, success=True)

        patterns = metrics.analyze_patterns()

        # Should identify failed activations
        assert any("failed" in insight for insight in patterns['insights'])
        assert any("Review" in rec or "error" in rec for rec in patterns['recommendations'])

    def test_analyze_patterns_orchestrator_usage(self, metrics_file):
        """Test orchestrator usage analysis."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # High orchestrator usage
        for i in range(12):
            metrics.log_activation("main-workflow-router", f"trigger {i}", 0.9)

        for i in range(3):
            metrics.log_activation("bmad-product-planning", f"trigger {i}", 0.9)

        patterns = metrics.analyze_patterns()

        # Should detect high orchestrator usage
        assert any("orchestrator" in insight.lower() for insight in patterns['insights'])

    def test_analyze_patterns_workflow_split(self, metrics_file):
        """Test OpenSpec vs BMAD workflow split analysis."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Create mix of OpenSpec and BMAD activations (need > 10 total for workflow split analysis)
        for i in range(8):
            metrics.log_activation("openspec-change-proposal", f"trigger {i}", 0.9)

        for i in range(4):
            metrics.log_activation("bmad-product-planning", f"trigger {i}", 0.9)

        patterns = metrics.analyze_patterns()

        # Should analyze workflow split (code requires total > 10)
        assert any("OpenSpec" in insight or "BMAD" in insight for insight in patterns['insights'])


class TestViewRecent:
    """Test recent activations viewing."""

    def test_view_recent_default_count(self, metrics_file):
        """Test viewing recent activations with default count."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Create 15 activations
        for i in range(15):
            metrics.log_activation(f"skill-{i}", f"trigger {i}", 0.9)

        recent = metrics.view_recent()

        # Should return last 10
        assert len(recent) == 10
        assert recent[0]['skill'] == "skill-5"
        assert recent[9]['skill'] == "skill-14"

    def test_view_recent_custom_count(self, metrics_file):
        """Test viewing recent activations with custom count."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        for i in range(10):
            metrics.log_activation(f"skill-{i}", f"trigger {i}", 0.9)

        recent = metrics.view_recent(count=3)

        assert len(recent) == 3
        assert recent[0]['skill'] == "skill-7"
        assert recent[2]['skill'] == "skill-9"

    def test_view_recent_less_than_count(self, metrics_file):
        """Test viewing when total activations < count."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        for i in range(3):
            metrics.log_activation(f"skill-{i}", f"trigger {i}", 0.9)

        recent = metrics.view_recent(count=10)

        # Should return all 3
        assert len(recent) == 3


class TestExportReport:
    """Test report export functionality."""

    def test_export_report_creates_file(self, metrics_file, temp_dir):
        """Test that export_report creates markdown file."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("bmad-product-planning", "create PRD", 0.95)
        metrics.log_activation("bmad-architecture-design", "design arch", 0.88)

        report_file = temp_dir / "test-report.md"
        result = metrics.export_report(output_file=str(report_file))

        assert Path(result).exists()
        assert report_file.read_text().startswith("# Activation Metrics Report")

    def test_export_report_contains_stats(self, metrics_file, temp_dir):
        """Test that exported report contains statistics."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        metrics.log_activation("skill-1", "trigger 1", 0.9, success=True)
        metrics.log_activation("skill-2", "trigger 2", 0.8, success=False)

        report_file = temp_dir / "report.md"
        metrics.export_report(output_file=str(report_file))

        content = report_file.read_text()

        # Format is: **Total Activations:** 2
        assert "**Total Activations:** 2" in content
        assert "**Successful:** 1" in content
        assert "**Failed:** 1" in content
        assert "**Success Rate:** 50" in content

    def test_export_report_contains_insights(self, metrics_file, temp_dir):
        """Test that report includes insights section."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        for i in range(15):
            metrics.log_activation("main-workflow-router", f"trigger {i}", 0.9)

        report_file = temp_dir / "report.md"
        metrics.export_report(output_file=str(report_file))

        content = report_file.read_text()

        assert "## Insights" in content


class TestClearMetrics:
    """Test metrics clearing functionality."""

    def test_clear_metrics_resets_data(self, metrics_file):
        """Test that clear_metrics removes all data."""
        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Create some data
        metrics.log_activation("skill-1", "trigger", 0.9)
        metrics.log_activation("skill-2", "trigger", 0.8)

        # Clear
        metrics.clear_metrics()

        # Verify cleared
        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        assert data['summary']['total_activations'] == 0
        assert len(data['activations']) == 0


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_load_corrupted_yaml(self, metrics_file):
        """Test handling of corrupted YAML file."""
        # Create corrupted YAML
        metrics_file.write_text("invalid: yaml: content: [")

        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Should initialize fresh metrics
        stats = metrics.get_stats()
        assert stats['total'] == 0

    def test_load_non_dict_yaml(self, metrics_file):
        """Test handling of non-dict YAML content."""
        # Create YAML that's not a dict
        metrics_file.write_text("- item1\n- item2")

        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Should initialize fresh metrics
        stats = metrics.get_stats()
        assert stats['total'] == 0

    def test_missing_summary_keys(self, metrics_file):
        """Test handling of missing summary keys."""
        # Create incomplete metrics file
        metrics_file.write_text("activations: []")

        metrics = ActivationMetrics(metrics_file=str(metrics_file))

        # Should add missing keys
        metrics.log_activation("skill-1", "trigger", 0.9)

        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)

        assert 'summary' in data
        assert 'total_activations' in data['summary']


# Run tests with: pytest tests/unit/test_activation_metrics.py -v
