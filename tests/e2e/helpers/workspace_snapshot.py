"""
Workspace snapshot utilities for detecting file changes during E2E tests.

Allows taking before/after snapshots of the workspace to detect:
- New files created
- Modified files
- Deleted files
"""

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Set, Dict, List, Optional


@dataclass
class FileInfo:
    """Information about a file at a point in time."""
    path: Path
    size: int
    mtime: float
    md5: Optional[str] = None

    def __hash__(self):
        return hash(str(self.path))


class WorkspaceSnapshot:
    """
    Captures the state of a workspace directory for comparison.

    Usage:
        before = WorkspaceSnapshot.capture(workspace_path)
        # ... do something that modifies workspace ...
        after = WorkspaceSnapshot.capture(workspace_path)
        diff = before.diff(after)
        print(f"New files: {diff.added}")
    """

    def __init__(self, root: Path, files: Dict[Path, FileInfo]):
        """
        Initialize snapshot.

        Args:
            root: Root directory of the snapshot
            files: Dictionary mapping paths to FileInfo objects
        """
        self.root = root
        self.files = files

    @classmethod
    def capture(
        cls,
        root: Path,
        include_patterns: Optional[List[str]] = None,
        exclude_patterns: Optional[List[str]] = None,
        compute_md5: bool = False
    ) -> "WorkspaceSnapshot":
        """
        Capture current state of a directory.

        Args:
            root: Root directory to snapshot
            include_patterns: Glob patterns to include (e.g., ["*.md", "*.py"])
            exclude_patterns: Glob patterns to exclude (e.g., ["__pycache__", ".git"])
            compute_md5: Whether to compute MD5 hashes (slower but more accurate)

        Returns:
            WorkspaceSnapshot object
        """
        root = Path(root).resolve()

        if not root.exists():
            return cls(root, {})

        files = {}

        # Default exclusions
        default_exclusions = {".git", "__pycache__", ".pytest_cache", "*.pyc", ".DS_Store"}
        if exclude_patterns:
            default_exclusions.update(exclude_patterns)

        # Walk directory tree
        for path in root.rglob("*"):
            # Skip if path matches exclusion
            if any(path.match(pattern) for pattern in default_exclusions):
                continue

            # Skip if not a file
            if not path.is_file():
                continue

            # Skip if doesn't match inclusion patterns
            if include_patterns and not any(path.match(pattern) for pattern in include_patterns):
                continue

            stat = path.stat()

            md5 = None
            if compute_md5:
                md5 = cls._compute_md5(path)

            relative_path = path.relative_to(root)
            files[relative_path] = FileInfo(
                path=relative_path,
                size=stat.st_size,
                mtime=stat.st_mtime,
                md5=md5
            )

        return cls(root, files)

    @staticmethod
    def _compute_md5(path: Path) -> str:
        """Compute MD5 hash of a file."""
        md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                md5.update(chunk)
        return md5.hexdigest()

    def diff(self, other: "WorkspaceSnapshot") -> "SnapshotDiff":
        """
        Compare this snapshot with another.

        Args:
            other: Another WorkspaceSnapshot to compare against

        Returns:
            SnapshotDiff describing changes
        """
        added = set(other.files.keys()) - set(self.files.keys())
        removed = set(self.files.keys()) - set(other.files.keys())

        # Check for modifications
        modified = set()
        for path in set(self.files.keys()) & set(other.files.keys()):
            old_info = self.files[path]
            new_info = other.files[path]

            # Check if file changed
            if old_info.size != new_info.size or old_info.mtime != new_info.mtime:
                modified.add(path)
            elif old_info.md5 and new_info.md5 and old_info.md5 != new_info.md5:
                modified.add(path)

        return SnapshotDiff(
            added=added,
            removed=removed,
            modified=modified,
            before=self,
            after=other
        )

    def get_file(self, relative_path: str) -> Optional[FileInfo]:
        """Get FileInfo for a specific file path."""
        return self.files.get(Path(relative_path))

    def exists(self, relative_path: str) -> bool:
        """Check if a file exists in this snapshot."""
        return Path(relative_path) in self.files

    def list_files(self, pattern: str = "*") -> List[Path]:
        """List all files matching a glob pattern."""
        return [
            path for path in self.files.keys()
            if path.match(pattern)
        ]


@dataclass
class SnapshotDiff:
    """
    Represents differences between two workspace snapshots.
    """
    added: Set[Path]
    removed: Set[Path]
    modified: Set[Path]
    before: WorkspaceSnapshot
    after: WorkspaceSnapshot

    def has_changes(self) -> bool:
        """Check if there are any changes."""
        return bool(self.added or self.removed or self.modified)

    def summary(self) -> str:
        """Get a human-readable summary of changes."""
        lines = []
        if self.added:
            lines.append(f"Added: {len(self.added)} files")
            for path in sorted(self.added):
                lines.append(f"  + {path}")

        if self.modified:
            lines.append(f"Modified: {len(self.modified)} files")
            for path in sorted(self.modified):
                lines.append(f"  M {path}")

        if self.removed:
            lines.append(f"Removed: {len(self.removed)} files")
            for path in sorted(self.removed):
                lines.append(f"  - {path}")

        if not self.has_changes():
            lines.append("No changes detected")

        return "\n".join(lines)

    def get_added_by_pattern(self, pattern: str) -> List[Path]:
        """Get added files matching a glob pattern."""
        return [path for path in self.added if path.match(pattern)]

    def assert_file_added(self, relative_path: str) -> None:
        """Assert that a specific file was added."""
        path = Path(relative_path)
        if path not in self.added:
            raise AssertionError(
                f"Expected file '{relative_path}' to be added, but it wasn't.\n"
                f"Added files: {sorted(self.added)}"
            )

    def assert_file_modified(self, relative_path: str) -> None:
        """Assert that a specific file was modified."""
        path = Path(relative_path)
        if path not in self.modified:
            raise AssertionError(
                f"Expected file '{relative_path}' to be modified, but it wasn't.\n"
                f"Modified files: {sorted(self.modified)}"
            )

    def assert_pattern_added(self, pattern: str, min_count: int = 1) -> List[Path]:
        """Assert that at least min_count files matching pattern were added."""
        matches = self.get_added_by_pattern(pattern)
        if len(matches) < min_count:
            raise AssertionError(
                f"Expected at least {min_count} files matching '{pattern}' to be added, "
                f"but found {len(matches)}.\n"
                f"Matches: {sorted(matches)}\n"
                f"All added: {sorted(self.added)}"
            )
        return matches
