#!/usr/bin/env python3
"""
Simple YAML parser and dumper using stdlib only (no PyYAML dependency)
Supports basic YAML features: scalars, lists, nested dicts, booleans, numbers
Does NOT support: anchors, multi-line strings, complex YAML features
"""

import json
from typing import Any, Dict, List, Union


def safe_load(text: str) -> Dict[str, Any]:
    """
    Parse simple YAML text into Python dict.
    Supports: scalars, lists (inline and multi-line), nested dicts, booleans, numbers.
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
            current_dict = get_current_dict(indent)
            list_value = stripped[2:].strip()

            # Parse the list value
            if list_value:
                parsed_value = _parse_value(list_value)
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
                current_dict[key] = _parse_value(value)

        i += 1

    return result


def dump(data: Union[Dict, List], file_handle, default_flow_style=False, sort_keys=False):
    """
    Dump Python data structure to YAML format.
    Writes to an open file handle.
    """
    yaml_text = _dump_to_yaml(data, indent=0, sort_keys=sort_keys)
    file_handle.write(yaml_text)


def _parse_value(value: str) -> Any:
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


def _dump_to_yaml(data: Any, indent: int = 0, sort_keys: bool = False) -> str:
    """Recursively convert Python data to YAML string"""
    yaml_lines = []
    indent_str = '  ' * indent

    if isinstance(data, dict):
        items = sorted(data.items()) if sort_keys else data.items()
        for key, value in items:
            if isinstance(value, (dict, list)):
                yaml_lines.append(f"{indent_str}{key}:")
                yaml_lines.append(_dump_to_yaml(value, indent + 1, sort_keys))
            elif value is None:
                yaml_lines.append(f"{indent_str}{key}: null")
            elif isinstance(value, bool):
                yaml_lines.append(f"{indent_str}{key}: {str(value).lower()}")
            elif isinstance(value, str):
                # Escape if needed
                if ':' in value or '#' in value or value.startswith(('-', '[', '{')):
                    yaml_lines.append(f"{indent_str}{key}: '{value}'")
                else:
                    yaml_lines.append(f"{indent_str}{key}: {value}")
            else:
                yaml_lines.append(f"{indent_str}{key}: {value}")

    elif isinstance(data, list):
        for item in data:
            if isinstance(item, (dict, list)):
                yaml_lines.append(f"{indent_str}- ")
                nested = _dump_to_yaml(item, indent + 1, sort_keys)
                # Inline the first line with the dash
                nested_lines = nested.split('\n')
                if nested_lines:
                    first_line = nested_lines[0].lstrip()
                    yaml_lines[-1] += first_line
                    if len(nested_lines) > 1:
                        yaml_lines.extend(nested_lines[1:])
            elif item is None:
                yaml_lines.append(f"{indent_str}- null")
            elif isinstance(item, bool):
                yaml_lines.append(f"{indent_str}- {str(item).lower()}")
            elif isinstance(item, str):
                if ':' in item or '#' in item or item.startswith(('-', '[', '{')):
                    yaml_lines.append(f"{indent_str}- '{item}'")
                else:
                    yaml_lines.append(f"{indent_str}- {item}")
            else:
                yaml_lines.append(f"{indent_str}- {item}")

    return '\n'.join(yaml_lines) if yaml_lines else ''
