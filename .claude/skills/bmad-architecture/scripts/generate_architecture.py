#!/usr/bin/env python3
"""
BMAD Architecture Generator
Generates ARCHITECTURE.md from structured JSON data
Following BMAD Method v6-alpha Decision Architecture specifications
"""

import json
import sys
from pathlib import Path
from datetime import datetime

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
ARTIFACTS_DIR = RUNTIME_ROOT.parent / "artifacts"
DEFAULT_OUTPUT_DIR = ARTIFACTS_DIR  # Backwards compatibility

def load_json_data(json_path):
    """Load architecture data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def render_architecture_content(data):
    """Render architecture content from data without external template engine"""
    # Build decision summary table
    decision_rows = []
    for decision in data['decisions']:
        version = decision.get('version') or 'N/A'
        starter_note = ' (Provided by starter)' if decision.get('provided_by_starter') else ''
        decision_rows.append(
            f"| {decision['category']} | {decision['decision']} | {version} | "
            f"{decision['affects_epics']} | {decision['rationale']}{starter_note} |"
        )
    decision_table = '\n'.join(decision_rows)

    # Build epic mapping
    epic_sections = []
    for epic in data['epic_mapping']:
        components = ', '.join(epic['components'])
        epic_sections.append(f"""### Epic {epic['epic_num']}: {epic['epic_title']}

**Components:** {components}
**Location:** {epic['location']}
""")
    epic_mapping = '\n'.join(epic_sections)

    # Optional: project initialization
    init_section = ''
    if data.get('project_initialization'):
        init_section = f"""## Project Initialization

{data['project_initialization']}
"""

    # Optional: novel patterns
    novel_patterns_section = ''
    if data.get('novel_patterns'):
        pattern_sections = []
        for pattern in data['novel_patterns']:
            pattern_sections.append(f"""### {pattern['name']}

**Purpose:** {pattern['purpose']}

**Components:**
{pattern['components']}

**Data Flow:**
{pattern['data_flow']}

**Implementation Guide:**
{pattern['implementation_guide']}

---
""")
        patterns_content = '\n'.join(pattern_sections)
        novel_patterns_section = f"""## Novel Pattern Designs

These patterns were designed specifically for this project to solve unique requirements.

{patterns_content}"""

    return f"""# Decision Architecture: {data['project_name']}

**Author:** {data['user_name']}
**Date:** {data['date']}
**Version:** 1.0.0

---

## Executive Summary

{data['executive_summary']}

{init_section}
---

## Decision Summary

| Category | Decision | Version | Affects Epics | Rationale |
|----------|----------|---------|---------------|-----------|
{decision_table}

---

## Project Structure

```
{data['project_structure']}
```

---

## Epic to Architecture Mapping

{epic_mapping}

---

## Technology Stack Details

### Core Technologies

{data['technology_stack']}

### Integration Points

{data['integration_points']}

---

{novel_patterns_section}

## Implementation Patterns

These patterns ensure consistent implementation across all AI agents:

{data['implementation_patterns']}

---

## Consistency Rules

### Naming Conventions

{data['naming_conventions']}

### Code Organization

{data['code_organization']}

### Error Handling

{data['error_handling']}

### Logging Strategy

{data['logging_strategy']}

---

## Data Architecture

{data['data_architecture']}

---

## API Contracts

{data['api_contracts']}

---

## Security Architecture

{data['security_architecture']}

---

## Performance Considerations

{data['performance_considerations']}

---

## Deployment Architecture

{data['deployment_architecture']}

---

## Development Environment

{data['dev_environment']}

---

_Generated via BMAD Workflow Skills (v1.0.0) using BMAD v6-alpha spec_
_Source: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha_
_Generated: {data['date']}_
_For: {data['user_name']}_
"""

def generate_architecture(data, output_dir=None):
    """Generate ARCHITECTURE.md from data"""
    # Ensure output directory exists
    output_path = Path(output_dir) if output_dir else DEFAULT_OUTPUT_DIR
    output_path.mkdir(parents=True, exist_ok=True)

    # Render content
    arch_content = render_architecture_content(data)

    # Write Architecture document
    arch_file = output_path / 'ARCHITECTURE.md'
    with open(arch_file, 'w') as f:
        f.write(arch_content)

    print(f"✅ Generated: {arch_file}")
    return arch_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_architecture.py <json_data_file> [output_dir]")
        print("Example: python generate_architecture.py /tmp/architecture_data.json docs")
        sys.exit(1)

    json_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # Load data
    print(f"Loading architecture data from: {json_path}")
    data = load_json_data(json_path)

    # Add generation timestamp if not present
    if 'date' not in data:
        data['date'] = datetime.now().strftime('%Y-%m-%d')

    # Generate document
    print("\nGenerating BMAD Decision Architecture document...")
    arch_file = generate_architecture(data, output_dir)

    print("\n" + "="*60)
    print("✅ Decision Architecture Workflow Complete!")
    print("="*60)
    print(f"\nDeliverable Created:")
    print(f"  - {arch_file} - Complete architectural decisions document")
    print(f"\nKey Content:")
    print(f"  - {len(data.get('decisions', []))} architectural decisions documented")
    if data.get('novel_patterns'):
        print(f"  - {len(data['novel_patterns'])} novel pattern(s) designed")
    if data.get('project_initialization'):
        print(f"  - Project initialization command documented")
    print(f"\nNext Steps:")
    print(f"  - Review ARCHITECTURE.md for completeness")
    print(f"  - Proceed to Story Creation phase (bmad-stories skill)")
    print(f"  - Stories will reference this architecture for consistency")
    print("="*60)

if __name__ == '__main__':
    main()
