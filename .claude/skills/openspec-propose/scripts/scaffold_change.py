#!/usr/bin/env python3
"""Create the folder structure for an OpenSpec change and hydrate it with templates."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
CHANGE_ROOT = RUNTIME_ROOT / "changes"
ASSET_DIR = Path(__file__).resolve().parent.parent / "assets"

TEMPLATE_MAP = {
    "proposal.md": "proposal-template.md",
    "tasks.md": "tasks-template.md",
    "specs/spec-delta.md": "spec-delta-template.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("change_id", help="kebab-case identifier for the change (e.g. add-two-factor-auth)")
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files if they already exist."
    )
    parser.add_argument(
        "--include-design",
        action="store_true",
        help="Create an empty design.md for optional technical design notes.",
    )
    return parser.parse_args()


def ensure_repo_structure() -> None:
    RUNTIME_ROOT.mkdir(parents=True, exist_ok=True)
    CHANGE_ROOT.mkdir(parents=True, exist_ok=True)


def copy_template(change_dir: Path, relative_path: str, template_name: str, overwrite: bool) -> None:
    destination = change_dir / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)
    template_path = ASSET_DIR / template_name
    if not template_path.exists():
        raise FileNotFoundError(f"Missing template: {template_path}")
    if destination.exists() and not overwrite:
        return
    shutil.copyfile(template_path, destination)


def main() -> None:
    args = parse_args()
    ensure_repo_structure()
    change_dir = CHANGE_ROOT / args.change_id
    if change_dir.exists() and not args.overwrite:
        print(f"Change directory already exists: {change_dir}")
    change_dir.mkdir(parents=True, exist_ok=True)

    for relative_path, template in TEMPLATE_MAP.items():
        copy_template(change_dir, relative_path, template, args.overwrite)

    if args.include_design:
        design_path = change_dir / "design.md"
        if not design_path.exists() or args.overwrite:
            design_path.write_text("# Technical Design\n\n<!-- Add diagrams, sequence flows, or code notes here. -->\n")

    readme_path = change_dir / "README.md"
    if not readme_path.exists() or args.overwrite:
        readme_path.write_text(
            "# OpenSpec Change Workspace\n\n"
            "- `proposal.md`: summary of the intent and acceptance signals.\n"
            "- `tasks.md`: ordered implementation checklist.\n"
            "- `specs/`: delta specifications scoped by component.\n"
            "- `design.md`: optional deeper technical notes.\n"
        )

    print(f"Scaffold ready at {change_dir.relative_to(SKILLS_ROOT)}")


if __name__ == "__main__":
    main()
