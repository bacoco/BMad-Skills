#!/usr/bin/env python3
"""
BMAD PRD Generator
Generates PRD.md and epics.md from structured JSON data
Following BMAD Method v6-alpha specifications
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
ARTIFACTS_DIR = RUNTIME_ROOT / "artifacts"
DEFAULT_OUTPUT_DIR = ARTIFACTS_DIR


class PRDValidationError(ValueError):
    """Raised when the input data cannot produce a valid PRD."""


def load_json_data(json_path: str) -> Dict[str, Any]:
    """Load PRD data from JSON file."""

    data_file = Path(json_path)
    if not data_file.exists():
        raise FileNotFoundError(f"Data file not found: {json_path}")

    with open(data_file, 'r') as handle:
        try:
            payload = json.load(handle)
        except json.JSONDecodeError as exc:
            raise PRDValidationError(
                f"Invalid JSON data in {json_path}: {exc}"
            ) from exc

    if not isinstance(payload, dict):
        raise PRDValidationError('Root JSON value must be an object')

    return payload


def render_prd_content(data: Dict[str, Any]) -> str:
    """Render PRD content from data without external template engine"""
    return f"""# {data['project_name']} Product Requirements Document (PRD)

**Author:** {data['user_name']}
**Date:** {data['date']}
**Project Level:** {data['project_level']}
**Version:** 1.0.0

---

## Goals and Background Context

### Goals

{data['goals']}

### Background Context

{data['background_context']}

---

## Requirements

### Functional Requirements

{data['functional_requirements']}

### Non-Functional Requirements

{data['non_functional_requirements']}

---

## User Journeys

{data['user_journeys']}

---

## UX Design Principles

{data['ux_principles']}

---

## User Interface Design Goals

{data['ui_design_goals']}

---

## Epic List

{data['epic_list']}

> **Note:** Detailed epic breakdown with full story specifications is available in [epics.md](./epics.md)

---

## Out of Scope

{data['out_of_scope']}

---

_Generated via BMAD Workflow Skills (v1.0.0) using BMAD v6-alpha spec_
_Source: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha_
_Generated: {data['date']}_
"""

def render_epics_content(data: Dict[str, Any]) -> str:
    """Render epics content from data without external template engine"""
    # Build epic sections
    epic_sections = []
    for epic in data['epics_details']:
        # Build story sections
        story_sections = []
        for story in epic['stories']:
            # Build acceptance criteria
            ac_lines = []
            for idx, ac in enumerate(story['acceptance_criteria'], start=1):
                ac_lines.append(f"{idx}. {ac}")
            acceptance_criteria = '\n'.join(ac_lines)

            # Optional prerequisites
            prereq_section = ''
            if story.get('prerequisites'):
                prereq_section = f"\n\n**Prerequisites:** {story['prerequisites']}"

            story_sections.append(f"""#### Story {epic['epic_num']}.{story['story_num']}: {story['story_title']}

{story['user_story']}

**Acceptance Criteria:**
{acceptance_criteria}
{prereq_section}

---
""")

        stories_content = '\n'.join(story_sections)
        epic_sections.append(f"""## Epic {epic['epic_num']}: {epic['epic_title']}

### Goal
{epic['epic_goal']}

### Stories

{stories_content}
""")

    epics_content = '\n'.join(epic_sections)

    return f"""# {data['project_name']} - Epic Breakdown

**Author:** {data['user_name']}
**Date:** {data['date']}
**Project Level:** {data['project_level']}
**Total Epics:** {len(data['epics_details'])}

---

## Overview

This document provides the complete tactical implementation roadmap for {data['project_name']}.
Each epic contains sequenced user stories with acceptance criteria and prerequisites.

**Epic Sequencing Rules:**
1. Epic 1 establishes foundation (infrastructure, CI/CD, core setup)
2. Subsequent epics build upon previous work
3. No forward dependencies across epics

**Story Requirements:**
- **Vertical slices**: Each story delivers complete, testable functionality
- **Sequential**: Stories are logically ordered within each epic
- **AI-agent sized**: Completable in single focused session (2-4 hours)
- **No forward dependencies**: No story depends on work from later stories

---

{epics_content}

---

_Generated via BMAD Workflow Skills (v1.0.0) using BMAD v6-alpha spec_
_Source: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha_
_Generated: {data['date']}_
"""


def _ensure_fields(data: Dict[str, Any], fields: Iterable[str]):
    missing = [field for field in fields if field not in data or data[field] in (None, '')]
    if missing:
        raise PRDValidationError(
            "Missing required fields: " + ", ".join(sorted(missing))
        )


def _validate_epics(epics: Any):
    if not isinstance(epics, list) or not epics:
        raise PRDValidationError('epics_details must be a non-empty list')

    for index, epic in enumerate(epics, start=1):
        if not isinstance(epic, dict):
            raise PRDValidationError(f'Epic #{index} must be an object')

        _ensure_fields(epic, ['epic_num', 'epic_title', 'epic_goal', 'stories'])

        stories = epic['stories']
        if not isinstance(stories, list) or not stories:
            raise PRDValidationError(
                f"Epic {epic.get('epic_title', index)} must contain stories"
            )

        for story_index, story in enumerate(stories, start=1):
            if not isinstance(story, dict):
                raise PRDValidationError(
                    f"Story {epic['epic_num']}.{story_index} must be an object"
                )

            _ensure_fields(
                story,
                ['story_num', 'story_title', 'user_story', 'acceptance_criteria'],
            )

            acceptance = story['acceptance_criteria']
            if not isinstance(acceptance, list) or not acceptance:
                raise PRDValidationError(
                    f"Story {epic['epic_num']}.{story['story_num']} requires acceptance criteria"
                )


def validate_prd_payload(data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate the structured JSON payload used to generate documents."""

    required_fields = [
        'project_name',
        'user_name',
        'project_level',
        'goals',
        'background_context',
        'functional_requirements',
        'non_functional_requirements',
        'user_journeys',
        'ux_principles',
        'ui_design_goals',
        'epic_list',
        'out_of_scope',
        'epics_details',
    ]

    _ensure_fields(data, required_fields)

    try:
        data['project_level'] = int(data['project_level'])
    except (ValueError, TypeError) as exc:
        raise PRDValidationError('project_level must be an integer') from exc

    _validate_epics(data['epics_details'])

    return data


def generate_prd(data: Dict[str, Any], output_dir: str = None) -> Path:
    """Generate PRD.md from validated data."""

    output_path = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    prd_content = render_prd_content(data)

    prd_file = output_path / 'PRD.md'
    prd_file.write_text(prd_content)

    print(f"✅ Generated: {prd_file}")
    return prd_file


def generate_epics(data: Dict[str, Any], output_dir: str = None) -> Path:
    """Generate epics.md from validated data."""

    output_path = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    epics_content = render_epics_content(data)

    epics_file = output_path / 'epics.md'
    epics_file.write_text(epics_content)

    print(f"✅ Generated: {epics_file}")
    return epics_file


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_prd.py <json_data_file> [output_dir]")
        print("Example: python generate_prd.py /tmp/prd_data.json docs")
        sys.exit(1)

    json_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        print(f"Loading data from: {json_path}")
        payload = load_json_data(json_path)
        data = validate_prd_payload(payload)
    except (FileNotFoundError, PRDValidationError) as exc:
        print(f"❌ {exc}")
        sys.exit(1)

    data.setdefault('date', datetime.now().strftime('%Y-%m-%d'))

    print("\nGenerating BMAD PRD documents...")
    try:
        prd_file = generate_prd(data, output_dir)
        epics_file = generate_epics(data, output_dir)
    except (FileNotFoundError, PRDValidationError) as exc:
        print(f"❌ Failed to generate documents: {exc}")
        sys.exit(1)

    print("\n" + "=" * 60)
    print("✅ PRD Workflow Complete!")
    print("=" * 60)
    print("\nDeliverables Created:")
    print(f"  1. {prd_file} - Strategic product requirements")
    print(f"  2. {epics_file} - Tactical implementation roadmap")

    print("\nNext Steps:")
    print("  - Review documents for completeness")
    print("  - Proceed to Architecture phase (bmad-architecture-design skill)")
    print("  - Run architecture workflow")
    print("=" * 60)


if __name__ == '__main__':
    main()
