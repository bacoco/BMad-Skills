#!/usr/bin/env python3
"""
Quick validation script for skills - minimal version
"""

import sys
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


_INT_PATTERN = re.compile(r"^[+-]?\d+$")
_FLOAT_PATTERN = re.compile(r"^[+-]?(?:\d*\.\d+|\d+\.\d*|\d+)(?:[eE][+-]?\d+)?$")


class FrontmatterParserError(Exception):
    """Raised when YAML-like frontmatter cannot be parsed."""


def _split_inline_items(text: str) -> List[str]:
    """Split a comma-separated inline list or mapping while respecting nesting."""

    items: List[str] = []
    buffer: List[str] = []
    depth = 0
    quote: Optional[str] = None
    escape = False

    for char in text:
        if quote:
            buffer.append(char)
            if escape:
                escape = False
                continue
            if char == "\\":
                escape = True
            elif char == quote:
                quote = None
            continue

        if char in ('"', "'"):
            quote = char
            buffer.append(char)
        elif char in "[{(":
            depth += 1
            buffer.append(char)
        elif char in "]})":
            depth = max(0, depth - 1)
            buffer.append(char)
        elif char == "," and depth == 0:
            item = "".join(buffer).strip()
            if item:
                items.append(item)
            buffer = []
        else:
            buffer.append(char)

    if quote:
        raise FrontmatterParserError("Unterminated quoted string in inline collection")

    tail = "".join(buffer).strip()
    if tail:
        items.append(tail)

    return items


def _parse_scalar(value: str) -> Any:
    """Parse a scalar value from YAML-like syntax using only the stdlib."""

    if value == "":
        return ""

    lower = value.lower()
    if lower in {"true", "yes"}:
        return True
    if lower in {"false", "no"}:
        return False
    if lower in {"null", "none", "~"}:
        return None

    if _INT_PATTERN.match(value):
        try:
            return int(value)
        except ValueError:
            pass
    if _FLOAT_PATTERN.match(value):
        try:
            return float(value)
        except ValueError:
            pass

    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        escaped = value[1:-1].encode("utf-8").decode("unicode_escape")
        return escaped
    if value.startswith("'") and value.endswith("'") and len(value) >= 2:
        return value[1:-1]

    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item) for item in _split_inline_items(inner)]

    if value.startswith("{") and value.endswith("}"):
        inner = value[1:-1].strip()
        if not inner:
            return {}
        result: Dict[str, Any] = {}
        for item in _split_inline_items(inner):
            key, sep, val = item.partition(":")
            if not sep:
                raise FrontmatterParserError(f"Invalid inline mapping entry: {item}")
            result[key.strip()] = _parse_scalar(val.strip())
        return result

    return value


def _parse_block(lines: List[str], index: int, indent_level: int) -> Tuple[Any, int]:
    """Parse a nested YAML-like block based on indentation."""

    mapping: Dict[str, Any] = {}
    sequence: List[Any] = []
    mode: Optional[str] = None

    while index < len(lines):
        raw_line = lines[index]
        stripped = raw_line.strip()

        if not stripped or stripped.startswith("#"):
            index += 1
            continue

        leading_spaces = len(raw_line) - len(raw_line.lstrip(" "))
        if leading_spaces % 2 != 0:
            raise FrontmatterParserError(
                f"Invalid indentation (must be multiples of two spaces): '{raw_line}'"
            )

        current_level = leading_spaces // 2
        if current_level < indent_level:
            break
        if current_level > indent_level:
            raise FrontmatterParserError(
                f"Unexpected indentation level at line: '{raw_line.strip()}'"
            )

        if stripped.startswith("- "):
            if mode == "mapping":
                raise FrontmatterParserError("Cannot mix list items with mapping entries")
            mode = "sequence"
            item_text = stripped[2:].strip()
            index += 1
            if item_text:
                sequence.append(_parse_scalar(item_text))
            else:
                item_value, index = _parse_block(lines, index, indent_level + 1)
                sequence.append(item_value)
        else:
            if mode == "sequence":
                raise FrontmatterParserError("Cannot mix mapping entries with list items")
            mode = "mapping"
            key, sep, remainder = stripped.partition(":")
            if not sep:
                raise FrontmatterParserError(f"Invalid mapping entry: '{stripped}'")
            key = key.strip()
            remainder = remainder.strip()
            index += 1
            if remainder:
                mapping[key] = _parse_scalar(remainder)
            else:
                value, index = _parse_block(lines, index, indent_level + 1)
                mapping[key] = value

    if mode == "sequence":
        return sequence, index

    return mapping, index


def parse_frontmatter(frontmatter_text: str) -> Dict[str, Any]:
    """Parse skill frontmatter without third-party dependencies."""

    lines = [line.rstrip("\r\n") for line in frontmatter_text.splitlines()]
    parsed, index = _parse_block(lines, 0, 0)

    # Ensure no trailing non-empty lines remain unparsed at root level
    for remaining in lines[index:]:
        if remaining.strip() and not remaining.strip().startswith("#"):
            raise FrontmatterParserError(
                f"Unexpected content after parsing frontmatter: '{remaining.strip()}'"
            )

    if not isinstance(parsed, dict):
        raise FrontmatterParserError("Frontmatter root must be a mapping")

    return parsed

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

    # Parse YAML frontmatter
    try:
        frontmatter = parse_frontmatter(frontmatter_text)
    except FrontmatterParserError as exc:
        return False, f"Invalid YAML frontmatter: {exc}"
    except Exception as exc:  # Defensive guardrail
        return False, f"Invalid frontmatter format: {exc}"

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
