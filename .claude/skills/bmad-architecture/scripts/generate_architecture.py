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
from jinja2 import Template

def load_json_data(json_path):
    """Load architecture data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_template(template_path):
    """Load Jinja2 template"""
    with open(template_path, 'r') as f:
        return Template(f.read())

def generate_architecture(data, output_dir='docs'):
    """Generate ARCHITECTURE.md from data"""
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load template
    template_path = Path(__file__).parent.parent / 'assets/decision-architecture-template.md.jinja'
    template = load_template(template_path)

    # Render template
    arch_content = template.render(**data)

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
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'docs'

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
