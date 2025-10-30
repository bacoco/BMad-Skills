"""
Unit tests for sprint_status.py

Tests the BMAD Sprint Status Manager functionality:
- Initialization
- Parsing epics.md
- YAML generation
- Error handling
"""

import pytest
import yaml
from pathlib import Path
import sys
import tempfile
import shutil

# Add sprint_status.py to path
SKILLS_ROOT = Path(__file__).resolve().parents[2] / ".claude" / "skills"
sys.path.insert(0, str(SKILLS_ROOT / "main-workflow-router" / "scripts"))

from sprint_status import SprintStatus


@pytest.fixture
def temp_dir():
    """Create temporary directory for tests."""
    tmpdir = tempfile.mkdtemp()
    yield Path(tmpdir)
    shutil.rmtree(tmpdir)


@pytest.fixture
def sample_epics_content():
    """Sample epics.md content for testing."""
    return """# Project Epics

## Epic 1: User Authentication

### Overview
User authentication system

#### Story 1.1: User Registration
Implement user registration form

**Acceptance Criteria:**
- Form validates email
- Password meets requirements

#### Story 1.2: User Login
Implement login functionality

**Acceptance Criteria:**
- Users can login
- Invalid credentials show error

## Epic 2: Dashboard

### Overview
User dashboard

#### Story 2.1: Dashboard Layout
Create dashboard layout

**Acceptance Criteria:**
- Responsive design
- Shows user info
"""


@pytest.fixture
def sample_epics_file(temp_dir, sample_epics_content):
    """Create sample epics.md file."""
    epics_file = temp_dir / "epics.md"
    epics_file.write_text(sample_epics_content)
    return epics_file


class TestSprintStatusInit:
    """Test SprintStatus initialization."""

    def test_init_default_dir(self):
        """Test initialization with default directory."""
        status = SprintStatus()

        assert status.docs_dir is not None
        assert status.status_file.name == 'sprint-status.yaml'

    def test_init_custom_dir(self, temp_dir):
        """Test initialization with custom directory."""
        status = SprintStatus(docs_dir=temp_dir)

        assert status.docs_dir == temp_dir
        assert status.status_file == temp_dir / 'sprint-status.yaml'


class TestParseEpics:
    """Test epic parsing functionality."""

    def test_parse_epics_basic(self, sample_epics_file):
        """Test basic epic parsing."""
        status = SprintStatus()
        stories = status._parse_epics(sample_epics_file)

        # Should find 3 stories total
        assert len(stories) == 3

        # Check first story (epic_num and story_num are integers, not strings)
        assert stories[0]['epic_num'] == 1
        assert stories[0]['story_num'] == 1
        assert 'Registration' in stories[0]['story_title']

        # Check second story
        assert stories[1]['epic_num'] == 1
        assert stories[1]['story_num'] == 2

        # Check third story (Epic 2)
        assert stories[2]['epic_num'] == 2
        assert stories[2]['story_num'] == 1

    def test_parse_epics_file_not_found(self, temp_dir):
        """Test parsing with non-existent file."""
        status = SprintStatus()
        nonexistent_file = temp_dir / "doesnotexist.md"

        with pytest.raises(FileNotFoundError):
            status._parse_epics(nonexistent_file)

    def test_parse_epics_empty_file(self, temp_dir):
        """Test parsing empty epics file."""
        empty_file = temp_dir / "empty.md"
        empty_file.write_text("")

        status = SprintStatus()
        stories = status._parse_epics(empty_file)

        assert len(stories) == 0


class TestInitFromEpics:
    """Test sprint status initialization from epics."""

    def test_init_from_epics_success(self, temp_dir, sample_epics_file):
        """Test successful initialization from epics."""
        status = SprintStatus(docs_dir=temp_dir)
        result_file = status.init_from_epics(epics_file=sample_epics_file)

        # File should be created
        assert result_file.exists()
        assert result_file == temp_dir / 'sprint-status.yaml'

        # Load and validate YAML
        with open(result_file, 'r') as f:
            data = yaml.safe_load(f)

        assert 'project_metadata' in data
        assert 'epic_status' in data
        assert 'development_status' in data

        # Check metadata
        metadata = data['project_metadata']
        assert metadata['total_epics'] == 2  # Epic 1 and Epic 2
        assert metadata['total_stories'] == 3  # 3 stories total
        assert 'created' in metadata
        assert 'last_updated' in metadata

    def test_init_from_epics_creates_epic_status(self, temp_dir, sample_epics_file):
        """Test epic status creation."""
        status = SprintStatus(docs_dir=temp_dir)
        result_file = status.init_from_epics(epics_file=sample_epics_file)

        with open(result_file, 'r') as f:
            data = yaml.safe_load(f)

        epic_status = data['epic_status']

        # Should have Epic 1 and Epic 2
        assert 'epic-1' in epic_status
        assert 'epic-2' in epic_status

        # Epic 1 details
        epic1 = epic_status['epic-1']
        assert 'Authentication' in epic1['title']
        assert epic1['total_stories'] == 2
        assert epic1['completed'] == 0
        assert epic1['status'] == 'backlog'

    def test_init_from_epics_creates_development_status(self, temp_dir, sample_epics_file):
        """Test development status creation."""
        status = SprintStatus(docs_dir=temp_dir)
        result_file = status.init_from_epics(epics_file=sample_epics_file)

        with open(result_file, 'r') as f:
            data = yaml.safe_load(f)

        dev_status = data['development_status']

        # Should have entries for all stories
        story_keys = list(dev_status.keys())
        assert len(story_keys) == 3

        # Check story format
        first_story = dev_status[story_keys[0]]
        assert 'title' in first_story
        assert first_story['status'] == 'backlog'
        assert first_story['assigned_to'] is None
        assert first_story['started'] is None
        assert first_story['completed'] is None

    def test_init_from_epics_missing_file(self, temp_dir):
        """Test initialization with missing epics file."""
        status = SprintStatus(docs_dir=temp_dir)
        missing_file = temp_dir / "missing.md"

        with pytest.raises(FileNotFoundError):
            status.init_from_epics(epics_file=missing_file)

    def test_init_from_epics_creates_directory(self, temp_dir):
        """Test that initialization creates docs directory if missing."""
        nested_dir = temp_dir / "new" / "nested" / "dir"
        sample_epics = temp_dir / "epics.md"
        sample_epics.write_text("## Epic 1\n#### Story 1.1: Test\nContent")

        status = SprintStatus(docs_dir=nested_dir)
        result_file = status.init_from_epics(epics_file=sample_epics)

        # Directory should be created
        assert nested_dir.exists()
        assert result_file.exists()


class TestErrorHandling:
    """Test error handling and edge cases."""

    def test_malformed_epic_header(self, temp_dir):
        """Test handling of malformed epic headers."""
        malformed_file = temp_dir / "malformed.md"
        malformed_file.write_text("""
# Not an epic

Some random content

#### Story 1.1: Orphan Story
This story has no epic parent
""")

        status = SprintStatus()
        stories = status._parse_epics(malformed_file)

        # Should still parse orphan stories (with empty epic)
        # Or should handle gracefully
        assert isinstance(stories, list)

    def test_yaml_serialization(self, temp_dir):
        """Test that generated YAML is valid and parseable."""
        epics_file = temp_dir / "epics.md"
        epics_file.write_text("""## Epic 1: Test Epic
#### Story 1.1: Test Story
Content
""")

        status = SprintStatus(docs_dir=temp_dir)
        result_file = status.init_from_epics(epics_file=epics_file)

        # Should be valid YAML
        with open(result_file, 'r') as f:
            data = yaml.safe_load(f)

        assert data is not None
        assert isinstance(data, dict)


# Run tests with: pytest tests/unit/test_sprint_status.py -v
