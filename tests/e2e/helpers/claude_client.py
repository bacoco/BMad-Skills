"""
Claude CLI client wrapper for E2E testing.

Provides a Python interface to the `claude` CLI command with:
- JSON output parsing
- Session management for multi-turn conversations
- Timeout handling
- Cost tracking
"""

import json
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any, List


@dataclass
class ClaudeResponse:
    """Structured response from claude CLI."""
    result: str
    session_id: str
    duration_ms: int
    total_cost_usd: float
    usage: Dict[str, Any]
    is_error: bool
    raw_json: Dict[str, Any]


class ClaudeClientError(Exception):
    """Raised when claude CLI execution fails."""
    pass


class ClaudeClient:
    """
    Wrapper for claude CLI command.

    Usage:
        client = ClaudeClient()
        response = client.execute("Hello, Claude!")
        print(response.result)

        # Multi-turn conversation
        session_id = client.new_session()
        r1 = client.execute("Tell me about BMAD", session_id=session_id)
        r2 = client.execute("What are the levels?", session_id=session_id)
    """

    def __init__(self, timeout: int = 120):
        """
        Initialize Claude client.

        Args:
            timeout: Maximum seconds to wait for response (default: 120)
        """
        self.timeout = timeout
        self.total_cost = 0.0
        self.call_count = 0

    def new_session(self) -> str:
        """Generate a new session ID for multi-turn conversations."""
        return str(uuid.uuid4())

    def execute(
        self,
        prompt: str,
        session_id: Optional[str] = None,
        timeout: Optional[int] = None,
        verbose: bool = False,
        allowed_tools: Optional[List[str]] = None
    ) -> ClaudeResponse:
        """
        Execute a prompt via claude CLI.

        Args:
            prompt: The prompt to send to Claude
            session_id: Optional session ID for multi-turn conversation
            timeout: Override default timeout for this call
            verbose: Print command being executed

        Returns:
            ClaudeResponse with parsed JSON output

        Raises:
            ClaudeClientError: If claude command fails
        """
        cmd = ["claude", "-p", "--output-format", "json"]

        if session_id:
            cmd.extend(["--session-id", session_id])

        # Add allowed tools - critical for skill activation
        if allowed_tools:
            cmd.extend(["--allowedTools", " ".join(allowed_tools)])
        else:
            # Default: Allow skills to activate
            cmd.extend(["--allowedTools", "Skill Read Write Grep"])

        if verbose:
            print(f"[ClaudeClient] Executing: {' '.join(cmd)} (prompt via stdin)")

        timeout_val = timeout or self.timeout

        try:
            result = subprocess.run(
                cmd,
                input=prompt,  # Pass prompt via stdin, not as argument
                capture_output=True,
                text=True,
                timeout=timeout_val
            )

            if result.returncode != 0:
                raise ClaudeClientError(
                    f"claude command failed with code {result.returncode}\n"
                    f"stderr: {result.stderr}\n"
                    f"stdout: {result.stdout}"
                )

            # Parse JSON response
            try:
                json_output = json.loads(result.stdout)
            except json.JSONDecodeError as e:
                raise ClaudeClientError(
                    f"Failed to parse JSON output: {e}\n"
                    f"stdout: {result.stdout}"
                )

            # Create response object
            response = ClaudeResponse(
                result=json_output.get("result", ""),
                session_id=json_output.get("session_id", session_id or ""),
                duration_ms=json_output.get("duration_ms", 0),
                total_cost_usd=json_output.get("total_cost_usd", 0.0),
                usage=json_output.get("usage", {}),
                is_error=json_output.get("is_error", False),
                raw_json=json_output
            )

            # Track costs
            self.total_cost += response.total_cost_usd
            self.call_count += 1

            if verbose:
                print(f"[ClaudeClient] Response: {len(response.result)} chars, "
                      f"${response.total_cost_usd:.4f}, {response.duration_ms}ms")

            return response

        except subprocess.TimeoutExpired:
            raise ClaudeClientError(
                f"claude command timed out after {timeout_val} seconds"
            )
        except Exception as e:
            raise ClaudeClientError(f"Unexpected error: {e}")

    def multi_turn(
        self,
        prompts: List[str],
        session_id: Optional[str] = None,
        verbose: bool = False
    ) -> List[ClaudeResponse]:
        """
        Execute multiple prompts in sequence within same session.

        Args:
            prompts: List of prompts to execute
            session_id: Optional session ID (will create new if not provided)
            verbose: Print execution details

        Returns:
            List of ClaudeResponse objects
        """
        if not session_id:
            session_id = self.new_session()

        responses = []
        for i, prompt in enumerate(prompts):
            if verbose:
                print(f"[ClaudeClient] Turn {i+1}/{len(prompts)}")

            response = self.execute(prompt, session_id=session_id, verbose=verbose)
            responses.append(response)

        return responses

    def detect_skill_activation(self, response: ClaudeResponse) -> Optional[str]:
        """
        Detect which skill was activated using keyword scoring.

        Returns skill with highest confidence score, or None if inconclusive.
        """
        result_lower = response.result.lower()

        # Skill signatures with weighted keywords
        SKILL_SIGNATURES = {
            'bmad-discovery-research': {
                'strong': ['discovery brief', 'research findings', 'competitive analysis'],
                'medium': ['discovery', 'research', 'explore', 'analyst', 'brainstorm'],
                'weak': ['problem space', 'pain point', 'target user']
            },
            'bmad-product-planning': {
                'strong': ['product requirements document', 'success metrics', 'acceptance criteria'],
                'medium': ['prd', 'product planning', 'features', 'goals', 'requirements'],
                'weak': ['roadmap', 'milestones']
            },
            'bmad-architecture-design': {
                'strong': ['architecture decisions', 'technical design', 'system architecture'],
                'medium': ['architect', 'architecture', 'tech stack', 'components'],
                'weak': ['scalability', 'database', 'api']
            },
            'bmad-ux-design': {
                'strong': ['user flows', 'wireframes', 'user journey'],
                'medium': ['ux', 'user experience', 'interface', 'designer'],
                'weak': ['mockup', 'prototype']
            },
            'bmad-test-strategy': {
                'strong': ['test strategy', 'atdd scenarios', 'test plan'],
                'medium': ['tea', 'testing', 'quality', 'test coverage'],
                'weak': ['unit tests', 'integration tests']
            },
            'bmad-story-planning': {
                'strong': ['developer stories', 'story breakdown', 'backlog'],
                'medium': ['stories', 'story planning', 'acceptance criteria'],
                'weak': ['sprint', 'epic']
            },
            'openspec-change-proposal': {
                'strong': ['change proposal', 'proposal.md', 'lightweight change'],
                'medium': ['proposal', 'level 0', 'level 1', 'openspec'],
                'weak': ['quick change', 'small enhancement']
            },
        }

        scores = {}
        for skill_name, signature in SKILL_SIGNATURES.items():
            score = 0

            # Strong keywords = 5 points
            for keyword in signature.get('strong', []):
                if keyword in result_lower:
                    score += 5

            # Medium keywords = 2 points
            for keyword in signature.get('medium', []):
                if keyword in result_lower:
                    score += 2

            # Weak keywords = 1 point
            for keyword in signature.get('weak', []):
                if keyword in result_lower:
                    score += 1

            scores[skill_name] = score

        # Return skill with highest score if above threshold
        max_score = max(scores.values()) if scores else 0
        if max_score >= 5:  # Require at least one strong or 3 medium matches
            return max(scores, key=scores.get)

        return None

    def check_skill_blocked(self, response: ClaudeResponse) -> bool:
        """Check if Skill tool was denied by permissions."""
        denials = response.raw_json.get('permission_denials', [])
        for denial in denials:
            if denial.get('tool_name') == 'Skill':
                return True
        return False

    def is_skill_activated(self, response: ClaudeResponse) -> bool:
        """Check if a skill was likely activated based on turn count."""
        return response.raw_json.get('num_turns', 1) > 1

    def get_stats(self) -> Dict[str, Any]:
        """Get usage statistics for this client instance."""
        return {
            "total_calls": self.call_count,
            "total_cost_usd": self.total_cost,
            "avg_cost_per_call": self.total_cost / self.call_count if self.call_count > 0 else 0
        }
