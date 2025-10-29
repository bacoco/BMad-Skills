#!/usr/bin/env python3
"""Archive an OpenSpec change by copying validated spec deltas into the canonical specs folder."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
OPEN_SPEC_ROOT = REPO_ROOT / "openspec"
CHANGE_ROOT = OPEN_SPEC_ROOT / "changes"
SPEC_ROOT = OPEN_SPEC_ROOT / "specs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("change_id", help="OpenSpec change identifier")
    parser.add_argument(
        "--spec",
        action="append",
        help="Specific spec file(s) within the change to archive. Defaults to all files in specs/.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned copy operations without modifying files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Allow overwriting files in openspec/specs when names collide.",
    )
    return parser.parse_args()


def ensure_directories() -> None:
    OPEN_SPEC_ROOT.mkdir(exist_ok=True)
    CHANGE_ROOT.mkdir(parents=True, exist_ok=True)
    SPEC_ROOT.mkdir(parents=True, exist_ok=True)


def resolve_spec_paths(change_dir: Path, spec_args: list[str] | None) -> list[Path]:
    specs_dir = change_dir / "specs"
    if not specs_dir.exists():
        raise FileNotFoundError(f"No specs directory found for change: {change_dir}")
    if spec_args:
        paths: list[Path] = []
        for spec in spec_args:
            candidate = specs_dir / spec
            if not candidate.exists():
                raise FileNotFoundError(f"Specified spec not found: {candidate}")
            paths.append(candidate)
        return paths
    return [path for path in specs_dir.rglob("*.md") if path.is_file()]


def copy_spec(spec_path: Path, overwrite: bool, dry_run: bool) -> None:
    relative = spec_path.relative_to(spec_path.parents[1])  # strip change folder
    destination = SPEC_ROOT / relative
    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists() and not overwrite:
        raise FileExistsError(f"Destination already exists: {destination}")
    if dry_run:
        print(f"DRY RUN: {spec_path} -> {destination}")
        return
    shutil.copyfile(spec_path, destination)
    print(f"Archived {spec_path} -> {destination}")


def main() -> None:
    args = parse_args()
    ensure_directories()
    change_dir = CHANGE_ROOT / args.change_id
    if not change_dir.exists():
        raise FileNotFoundError(f"Change directory not found: {change_dir}")
    spec_paths = resolve_spec_paths(change_dir, args.spec)
    if not spec_paths:
        raise FileNotFoundError(f"No spec files found to archive for {change_dir}")
    for spec_path in spec_paths:
        copy_spec(spec_path, args.overwrite, args.dry_run)


if __name__ == "__main__":
    main()
