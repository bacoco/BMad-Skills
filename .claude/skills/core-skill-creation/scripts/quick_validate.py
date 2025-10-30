#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
Uses stdlib only, no external dependencies (PyYAML-free)
"""

import sys
import os
import re
import json
from pathlib import Path

def parse_simple_yaml(text):
    """
    Parse simple YAML frontmatter using stdlib only.
    Supports: scalars, lists (inline and multi-line), nested dicts, booleans, numbers.
    Does NOT support: anchors, multi-line strings, complex YAML features.
    """
    result = {}
    lines = text.strip().split('\n')
    i = 0
    indent_stack = [(-1, result)]  # (indent_level, dict_ref)

    def get_current_dict(indent):
        """Find the appropriate dict for current indentation level"""
        while len(indent_stack) > 1 and indent_stack[-1][0] >= indent:
            indent_stack.pop()
        return indent_stack[-1][1]

    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith('#'):
            i += 1
            continue

        # Measure indentation
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        # List item (starts with -)
        if stripped.startswith('- '):
            # Find the parent key by looking back for the list key
            current_dict = get_current_dict(indent)
            list_value = stripped[2:].strip()

            # Parse the list value
            if list_value:
                parsed_value = parse_value(list_value)
                # Find the last added list or create one
                last_key = list(current_dict.keys())[-1] if current_dict else None
                if last_key and isinstance(current_dict[last_key], list):
                    current_dict[last_key].append(parsed_value)
            i += 1
            continue

        # Key-value pair
        if ':' in stripped:
            key, _, value = stripped.partition(':')
            key = key.strip()
            value = value.strip()

            current_dict = get_current_dict(indent)

            if not value:
                # Empty value - might be a nested dict or list
                # Peek ahead to see if next line is indented
                if i + 1 < len(lines):
                    next_line = lines[i + 1]
                    next_indent = len(next_line) - len(next_line.lstrip())
                    next_stripped = next_line.strip()

                    if next_indent > indent:
                        if next_stripped.startswith('- '):
                            # It's a list
                            current_dict[key] = []
                        else:
                            # It's a nested dict
                            current_dict[key] = {}
                            indent_stack.append((indent, current_dict[key]))
                    else:
                        current_dict[key] = None
                else:
                    current_dict[key] = None
            else:
                # Parse the value
                current_dict[key] = parse_value(value)

        i += 1

    return result

def parse_value(value):
    """Parse a YAML value into Python type"""
    value = value.strip()

    # Boolean
    if value in ('true', 'True', 'TRUE'):
        return True
    if value in ('false', 'False', 'FALSE'):
        return False

    # Null
    if value in ('null', 'Null', 'NULL', '~', ''):
        return None

    # Number
    try:
        if '.' in value:
            return float(value)
        return int(value)
    except ValueError:
        pass

    # Inline list [item1, item2]
    if value.startswith('[') and value.endswith(']'):
        try:
            return json.loads(value)
        except:
            pass

    # Inline dict {key: value}
    if value.startswith('{') and value.endswith('}'):
        try:
            return json.loads(value.replace("'", '"'))
        except:
            pass

    # String (remove quotes if present)
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        return value[1:-1]

    return value

def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)

    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Parse YAML frontmatter (stdlib only)
    try:
        frontmatter = parse_simple_yaml(frontmatter_text)
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a key/value mapping"
    except Exception as e:
        return False, f"Invalid frontmatter format: {e}"

    # Note: We intentionally do NOT restrict frontmatter keys to maintain
    # forward compatibility with evolving Claude Skills schema.
    # The validator only enforces required fields and format constraints.

    # Check required fields
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # Extract name for validation
    name = frontmatter.get('name', '')
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    name = name.strip()
    if name:
        # Check naming convention (hyphen-case: lowercase with hyphens)
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        # Check name length (max 64 characters per spec)
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # Extract and validate description
    description = frontmatter.get('description', '')
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    description = description.strip()
    if description:
        # Check for angle brackets
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        # Check description length (max 1024 characters per spec)
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    return True, "Skill is valid!"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    valid, message = validate_skill(sys.argv[1])
    print(message)
    sys.exit(0 if valid else 1)
