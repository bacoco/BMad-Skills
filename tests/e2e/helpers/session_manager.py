"""
Session management utilities for multi-turn E2E tests.

Provides high-level interface for managing conversational test scenarios.
"""

import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional, Dict, Any

from claude_client import ClaudeClient, ClaudeResponse
from workspace_snapshot import WorkspaceSnapshot, SnapshotDiff


@dataclass
class Turn:
    """Represents a single turn in a conversation."""
    prompt: str
    response: ClaudeResponse
    snapshot_before: WorkspaceSnapshot
    snapshot_after: WorkspaceSnapshot
    diff: SnapshotDiff


@dataclass
class TestSession:
    """
    Represents a complete test session with multiple turns.

    Tracks:
    - Conversation history
    - Workspace changes across turns
    - Cumulative costs
    """
    session_id: str
    workspace_root: Path
    turns: List[Turn] = field(default_factory=list)
    total_cost: float = 0.0

    def add_turn(self, turn: Turn) -> None:
        """Add a turn to this session."""
        self.turns.append(turn)
        self.total_cost += turn.response.total_cost_usd

    def get_all_changes(self) -> Dict[str, Any]:
        """Get summary of all changes across all turns."""
        all_added = set()
        all_modified = set()
        all_removed = set()

        for turn in self.turns:
            all_added.update(turn.diff.added)
            all_modified.update(turn.diff.modified)
            all_removed.update(turn.diff.removed)

        return {
            "added": all_added,
            "modified": all_modified,
            "removed": all_removed,
            "total_changes": len(all_added) + len(all_modified) + len(all_removed)
        }

    def summary(self) -> str:
        """Get human-readable summary of session."""
        lines = [
            f"Test Session: {self.session_id}",
            f"Turns: {len(self.turns)}",
            f"Total Cost: ${self.total_cost:.4f}",
            ""
        ]

        changes = self.get_all_changes()
        lines.append(f"Total Changes:")
        lines.append(f"  Added: {len(changes['added'])} files")
        lines.append(f"  Modified: {len(changes['modified'])} files")
        lines.append(f"  Removed: {len(changes['removed'])} files")
        lines.append("")

        for i, turn in enumerate(self.turns, 1):
            lines.append(f"Turn {i}:")
            lines.append(f"  Prompt: {turn.prompt[:60]}...")
            lines.append(f"  Response: {len(turn.response.result)} chars")
            lines.append(f"  Cost: ${turn.response.total_cost_usd:.4f}")
            lines.append(f"  Duration: {turn.response.duration_ms}ms")
            if turn.diff.has_changes():
                lines.append(f"  Changes: +{len(turn.diff.added)} ~{len(turn.diff.modified)} -{len(turn.diff.removed)}")
            lines.append("")

        return "\n".join(lines)


class SessionManager:
    """
    High-level manager for multi-turn test scenarios.

    Handles:
    - Session lifecycle
    - Workspace snapshots before/after each turn
    - Automatic change detection
    - Cost tracking

    Usage:
        manager = SessionManager(workspace_root=Path(".claude/skills/_runtime/workspace"))
        session = manager.start_session()

        # Turn 1
        response1 = manager.execute_turn(session, "I have an idea for an app")

        # Turn 2
        response2 = manager.execute_turn(session, "Create a PRD")

        # Get summary
        print(session.summary())
    """

    def __init__(
        self,
        workspace_root: Path,
        client: Optional[ClaudeClient] = None,
        verbose: bool = False
    ):
        """
        Initialize session manager.

        Args:
            workspace_root: Root directory to monitor for changes
            client: Optional ClaudeClient (will create default if not provided)
            verbose: Print detailed execution logs
        """
        self.workspace_root = Path(workspace_root)
        self.client = client or ClaudeClient()
        self.verbose = verbose
        self.sessions: Dict[str, TestSession] = {}

    def start_session(self, session_id: Optional[str] = None) -> TestSession:
        """
        Start a new test session.

        Args:
            session_id: Optional custom session ID

        Returns:
            TestSession object
        """
        if not session_id:
            session_id = f"test-{uuid.uuid4()}"

        session = TestSession(
            session_id=session_id,
            workspace_root=self.workspace_root
        )

        self.sessions[session_id] = session

        if self.verbose:
            print(f"[SessionManager] Started session: {session_id}")

        return session

    def execute_turn(
        self,
        session: TestSession,
        prompt: str,
        timeout: Optional[int] = None
    ) -> ClaudeResponse:
        """
        Execute a single turn in a session.

        Args:
            session: TestSession to add turn to
            prompt: Prompt to execute
            timeout: Optional timeout override

        Returns:
            ClaudeResponse from this turn
        """
        if self.verbose:
            print(f"[SessionManager] Turn {len(session.turns) + 1}: '{prompt[:60]}...'")

        # Take before snapshot
        before = WorkspaceSnapshot.capture(self.workspace_root)

        # Execute prompt
        response = self.client.execute(
            prompt,
            session_id=session.session_id,
            timeout=timeout,
            verbose=self.verbose
        )

        # Take after snapshot
        after = WorkspaceSnapshot.capture(self.workspace_root)

        # Compute diff
        diff = before.diff(after)

        # Create turn
        turn = Turn(
            prompt=prompt,
            response=response,
            snapshot_before=before,
            snapshot_after=after,
            diff=diff
        )

        # Add to session
        session.add_turn(turn)

        if self.verbose and diff.has_changes():
            print(f"[SessionManager] Changes detected:")
            print(diff.summary())

        return response

    def execute_scenario(
        self,
        prompts: List[str],
        session_id: Optional[str] = None
    ) -> TestSession:
        """
        Execute a complete multi-turn scenario.

        Args:
            prompts: List of prompts to execute in sequence
            session_id: Optional session ID

        Returns:
            TestSession with all turns
        """
        session = self.start_session(session_id)

        for prompt in prompts:
            self.execute_turn(session, prompt)

        if self.verbose:
            print(f"[SessionManager] Scenario complete: {len(prompts)} turns")
            print(session.summary())

        return session

    def get_session(self, session_id: str) -> Optional[TestSession]:
        """Get a session by ID."""
        return self.sessions.get(session_id)

    def cleanup(self) -> None:
        """Clean up all managed sessions."""
        if self.verbose:
            print(f"[SessionManager] Cleaning up {len(self.sessions)} sessions")

        self.sessions.clear()
