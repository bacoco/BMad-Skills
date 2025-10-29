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
from jinja2 import Template

def load_json_data(json_path):
    """Load story data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_template(template_path):
    """Load Jinja2 template"""
    with open(template_path, 'r') as f:
        return Template(f.read())

def create_story(data, output_dir='stories'):
    """Generate story file from data"""
    # Ensure output directory exists
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Load template
    template_path = Path(__file__).parent.parent / 'assets/story-template.md.jinja'
    template = load_template(template_path)

    # Create story filename
    story_filename = f"{data['epic_num']}-{data['story_num']}-{data['story_title']}.md"
    story_file = output_path / story_filename

    # Render template
    story_content = template.render(**data, date=datetime.now().strftime('%Y-%m-%d'))

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
    output_dir = sys.argv[2] if len(sys.argv) > 2 else 'stories'

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
