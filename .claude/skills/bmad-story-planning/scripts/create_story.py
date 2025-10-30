#!/usr/bin/env python3
"""
BMAD Story Generator
Creates developer-ready story files from structured JSON data
Following BMAD Method v6-alpha specifications
"""

import json
import sys
from pathlib import Path
from datetime import datetime

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
STORIES_DIR = RUNTIME_ROOT.parent / "stories"
DEFAULT_STORIES_DIR = STORIES_DIR  # Backwards compatibility

def load_json_data(json_path):
    """Load story data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def render_story_content(data, date):
    """Render story content from data without external template engine"""
    # Build acceptance criteria
    ac_lines = []
    for idx, ac in enumerate(data['acceptance_criteria'], start=1):
        ac_lines.append(f"{idx}. {ac}")
    acceptance_criteria = '\n'.join(ac_lines)

    # Build prerequisites
    prerequisites = data.get('prerequisites') or 'None'

    # Build tasks
    task_lines = []
    for task in data['tasks']:
        task_lines.append(f"- [ ] {task['task']} (AC: {task['ac_ref']})")
        for subtask in task.get('subtasks', []):
            task_lines.append(f"  - [ ] {subtask}")
    tasks = '\n'.join(task_lines)

    # Build dev notes references
    ref_lines = [f"- {ref}" for ref in data['dev_notes']['references']]
    references = '\n'.join(ref_lines)

    # Optional: previous story learnings
    learnings_section = ''
    if data['dev_notes'].get('previous_story_learnings'):
        learnings_section = f"""
### Learnings from Previous Story

{data['dev_notes']['previous_story_learnings']}
"""

    return f"""# Story {data['epic_num']}.{data['story_num']}: {data['story_title']}

**Status:** drafted
**Created:** {date}

---

## Story

As a {data['story_statement']['role']},
I want {data['story_statement']['action']},
so that {data['story_statement']['benefit']}.

---

## Acceptance Criteria

{acceptance_criteria}

---

## Prerequisites

{prerequisites}

---

## Tasks / Subtasks

{tasks}

---

## Dev Notes

### Architecture Patterns and Constraints

{data['dev_notes']['architecture_patterns']}

### Project Structure Notes

{data['dev_notes']['project_structure']}

### Testing Requirements

{data['dev_notes']['testing_requirements']}
{learnings_section}
### References

{references}

---

## Dev Agent Record

_This section is filled during implementation by the developer/AI agent_

### Context Reference

<!-- Path(s) to story context XML or additional context will be added here during implementation -->

### Agent Model Used

<!-- Agent model name and version used for implementation -->

### Debug Log References

<!-- Links to debug logs or implementation notes -->

### Completion Notes List

<!-- Key notes about implementation:
- New patterns/services created
- Architectural deviations or decisions
- Technical debt deferred
- Warnings for next story
- Interfaces/methods created for reuse
-->

### File List

<!-- Files affected during implementation:
- NEW: path/to/new/file.ext - Description
- MODIFIED: path/to/modified/file.ext - Changes made
- DELETED: path/to/deleted/file.ext - Reason
-->

---

_Generated via BMAD Workflow Skills (v1.0.0) using BMAD v6-alpha spec_
_Source: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha_
_Created: {date}_
"""

def create_story(data, output_dir=None):
    """Generate story file from data"""
    # Ensure output directory exists
    output_path = Path(output_dir) if output_dir else DEFAULT_STORIES_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    # Create story filename
    story_filename = f"{data['epic_num']}-{data['story_num']}-{data['story_title']}.md"
    story_file = output_path / story_filename

    # Render content
    date = datetime.now().strftime('%Y-%m-%d')
    story_content = render_story_content(data, date)

    # Write story file
    with open(story_file, 'w') as f:
        f.write(story_content)

    print(f"✅ Generated: {story_file}")
    return story_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_story.py <json_data_file> [output_dir]")
        print("Example: python create_story.py /tmp/story_data.json stories")
        sys.exit(1)

    json_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # Load data
    print(f"Loading story data from: {json_path}")
    data = load_json_data(json_path)

    # Generate story
    print("\nGenerating BMAD story file...")
    story_file = create_story(data, output_dir)

    print("\n" + "="*60)
    print("✅ Story Created Successfully!")
    print("="*60)
    print(f"\nStory Details:")
    print(f"  - Story ID: {data['epic_num']}.{data['story_num']}")
    print(f"  - Title: {data['story_title']}")
    print(f"  - File: {story_file}")
    print(f"  - Status: drafted")
    print(f"\nNext Steps:")
    print(f"  1. Review the story file for completeness")
    print(f"  2. Developer can now implement using this specification")
    print(f"  3. Create next story in sequence, or proceed to implementation")
    print(f"\nImplementation Note:")
    print(f"  - Developer should update 'Dev Agent Record' section during implementation")
    print(f"  - Mark tasks complete as work progresses")
    print(f"  - Update status to 'in-progress' → 'review' → 'done'")
    print("="*60)

if __name__ == '__main__':
    main()
