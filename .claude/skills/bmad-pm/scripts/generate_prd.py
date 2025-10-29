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

from jinja2 import Template, TemplateError


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


def load_template(template_path: Path) -> Template:
    """Load a Jinja2 template from disk."""

    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    with open(template_path, 'r') as handle:
        try:
            return Template(handle.read())
        except TemplateError as exc:
            raise PRDValidationError(
                f"Template could not be parsed: {template_path}"
            ) from exc


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


def generate_prd(data: Dict[str, Any], output_dir: str = 'docs') -> Path:
    """Generate PRD.md from validated data."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    template_path = Path(__file__).parent.parent / 'assets/prd-template.md.jinja'
    template = load_template(template_path)

    prd_content = template.render(**data)

    prd_file = output_path / 'PRD.md'
    prd_file.write_text(prd_content)

    print(f"✅ Generated: {prd_file}")
    return prd_file


def generate_epics(data: Dict[str, Any], output_dir: str = 'docs') -> Path:
    """Generate epics.md from validated data."""

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    template_path = Path(__file__).parent.parent / 'assets/epic-roadmap-template.md.jinja'
    template = load_template(template_path)

    epics_content = template.render(**data)

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
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'docs'

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
    except (FileNotFoundError, PRDValidationError, TemplateError) as exc:
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
    print("  - Proceed to Architecture phase (bmad-architecture skill)")
    print("  - Run architecture workflow")
    print("=" * 60)


if __name__ == '__main__':
    main()
