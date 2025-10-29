#!/usr/bin/env python3
"""Append a timestamped entry to an OpenSpec execution log, creating it from the template when missing."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
CHANGE_ROOT = RUNTIME_ROOT / "changes"
ASSET_DIR = Path(__file__).resolve().parent.parent / "assets"
TEMPLATE_FILE = ASSET_DIR / "execution-log-template.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("change_id", help="OpenSpec change identifier (kebab-case)")
    parser.add_argument("entry", help="Summary of the work performed or result observed")
    parser.add_argument(
        "--status",
        choices=["in-progress", "blocked", "done"],
        default="in-progress",
        help="Execution status to associate with the log entry.",
    )
    return parser.parse_args()


def ensure_log(change_id: str) -> Path:
    change_dir = CHANGE_ROOT / change_id
    if not change_dir.exists():
        raise FileNotFoundError(f"Change directory does not exist: {change_dir}")
    log_path = change_dir / "execution-log.md"
    if not log_path.exists():
        template_text = TEMPLATE_FILE.read_text()
        log_path.write_text(template_text)
    return log_path


def append_entry(log_path: Path, entry: str, status: str) -> None:
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")
    formatted = f"\n- {timestamp} [{status.upper()}] {entry}\n"
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(formatted)


def main() -> None:
    args = parse_args()
    log_path = ensure_log(args.change_id)
    append_entry(log_path, args.entry, args.status)
    print(f"Logged entry to {log_path.relative_to(SKILLS_ROOT)}")


if __name__ == "__main__":
    main()
