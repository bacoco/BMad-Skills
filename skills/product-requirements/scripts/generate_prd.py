#!/usr/bin/env python3
"""
BMAD PRD Generator
Generates PRD.md and epics.md from structured JSON data
Following BMAD Method v6-alpha specifications
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from jinja2 import Template

def load_json_data(json_path):
    """Load PRD data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_template(template_path):
    """Load Jinja2 template"""
    with open(template_path, 'r') as f:
        return Template(f.read())

def generate_prd(data, output_dir='docs'):
    """Generate PRD.md from data"""
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load template
    template_path = Path(__file__).parent.parent / 'assets/prd-template.md.jinja'
    template = load_template(template_path)

    # Render template
    prd_content = template.render(**data)

    # Write PRD
    prd_file = output_path / 'PRD.md'
    with open(prd_file, 'w') as f:
        f.write(prd_content)

    print(f"✅ Generated: {prd_file}")
    return prd_file

def generate_epics(data, output_dir='docs'):
    """Generate epics.md from data"""
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load template
    template_path = Path(__file__).parent.parent / 'assets/epic-roadmap-template.md.jinja'
    template = load_template(template_path)

    # Render template
    epics_content = template.render(**data)

    # Write epics
    epics_file = output_path / 'epics.md'
    with open(epics_file, 'w') as f:
        f.write(epics_content)

    print(f"✅ Generated: {epics_file}")
    return epics_file

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_prd.py <json_data_file> [output_dir]")
        print("Example: python generate_prd.py /tmp/prd_data.json docs")
        sys.exit(1)

    json_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'docs'

    # Load data
    print(f"Loading data from: {json_path}")
    data = load_json_data(json_path)

    # Add generation timestamp if not present
    if 'date' not in data:
        data['date'] = datetime.now().strftime('%Y-%m-%d')

    # Generate both documents
    print("\nGenerating BMAD PRD documents...")
    prd_file = generate_prd(data, output_dir)
    epics_file = generate_epics(data, output_dir)

    print("\n" + "="*60)
    print("✅ PRD Workflow Complete!")
    print("="*60)
    print(f"\nDeliverables Created:")
    print(f"  1. {prd_file} - Strategic product requirements")
    print(f"  2. {epics_file} - Tactical implementation roadmap")
    print(f"\nNext Steps:")
    print(f"  - Review documents for completeness")
    print(f"  - Proceed to Architecture phase (bmad-architecture skill)")
    print(f"  - Run architecture workflow")
    print("="*60)

if __name__ == '__main__':
    main()
