#!/usr/bin/env python3
"""Simple lint that ensures every skill contains SKILL.md, REFERENCE.md, WORKFLOW.md, and CHECKLIST.md."""
from pathlib import Path
import sys

MISSING_MSG = "{path} is missing required files: {missing}"


def validate_skill_dir(directory: Path) -> list[str]:
    required = {"SKILL.md", "REFERENCE.md", "WORKFLOW.md", "CHECKLIST.md"}
    present = {p.name for p in directory.iterdir() if p.is_file()}
    missing = sorted(required - present)
    if missing:
        return [MISSING_MSG.format(path=directory, missing=", ".join(missing))]
    return []


def main(root: str) -> int:
    base = Path(root)
    errors: list[str] = []
    for skill_dir in base.rglob('SKILL.md'):
        directory = skill_dir.parent
        errors.extend(validate_skill_dir(directory))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("All skills include required files.")
    return 0


if __name__ == "__main__":
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    raise SystemExit(main(root))
