"""
Skill activation verification module.

Provides robust multi-level validation for E2E testing.
"""

from typing import Tuple, Optional, Dict, List
from pathlib import Path

from claude_client import ClaudeResponse
from workspace_snapshot import WorkspaceSnapshot


# Skill artifact patterns
SKILL_ARTIFACTS = {
    'bmad-product-planning': {
        'files': ['PRD.md', 'prd.md', 'product-requirements-document.md'],
        'location': 'artifacts/'
    },
    'bmad-discovery-research': {
        'files': ['discovery-brief.md', 'research-notes.md', 'discovery.md'],
        'location': 'artifacts/'
    },
    'bmad-architecture-design': {
        'files': ['architecture-decisions.md', 'technical-design.md', 'architecture.md'],
        'location': 'artifacts/'
    },
    'bmad-ux-design': {
        'files': ['user-flows.md', 'wireframes.md', 'ux-design.md'],
        'location': 'artifacts/'
    },
    'bmad-story-planning': {
        'files': ['story-*.md'],  # Glob pattern
        'location': 'stories/'
    },
    'bmad-test-strategy': {
        'files': ['test-strategy.md', 'test-plan.md'],
        'location': 'artifacts/'
    },
    'openspec-change-proposal': {
        'files': ['proposal.md', 'tasks.md'],
        'location': 'changes/'
    },
    'openspec-change-implementation': {
        'files': ['execution-log.md', 'implementation.md'],
        'location': 'changes/'
    },
}


class SkillVerifier:
    """
    Multi-level skill activation verifier.

    Uses multiple strategies to robustly verify skill activation:
    1. Permission denial check
    2. Turn count analysis
    3. Content/keyword analysis
    4. Artifact detection
    """

    def __init__(self, client=None):
        """Initialize verifier with optional ClaudeClient."""
        self.client = client

    def verify(
        self,
        response: ClaudeResponse,
        expected_skill: str,
        before_snapshot: Optional[WorkspaceSnapshot] = None,
        after_snapshot: Optional[WorkspaceSnapshot] = None,
        strict: bool = False
    ) -> Tuple[bool, str, Dict]:
        """
        Verify skill activation using multi-level validation.

        Args:
            response: Claude response to verify
            expected_skill: Expected skill name
            before_snapshot: Workspace snapshot before execution
            after_snapshot: Workspace snapshot after execution
            strict: If True, require artifact proof

        Returns:
            (success: bool, reason: str, details: dict)
        """
        details = {
            'turn_count': response.raw_json.get('num_turns', 1),
            'permission_denials': response.raw_json.get('permission_denials', []),
            'detected_skill': None,
            'confidence': None,
            'artifacts_found': []
        }

        # Level 1: Check if Skill tool was blocked
        if self.client:
            if self.client.check_skill_blocked(response):
                return (False, "Skill tool was denied by permissions", details)

        # Level 2: Check turn count (quick filter)
        if self.client:
            if not self.client.is_skill_activated(response):
                return (False, "No skill activation detected (single turn response)", details)

        # Level 3: Content/keyword analysis
        if self.client:
            detected_skill = self.client.detect_skill_activation(response)
            details['detected_skill'] = detected_skill

            if detected_skill and detected_skill != expected_skill:
                return (
                    False,
                    f"Wrong skill detected: {detected_skill} (expected {expected_skill})",
                    details
                )

            if detected_skill == expected_skill:
                details['confidence'] = 'high'
            else:
                details['confidence'] = 'low'

        # Level 4: Artifact verification (strongest proof)
        if before_snapshot and after_snapshot:
            artifacts_found = self._check_artifacts(
                expected_skill,
                before_snapshot,
                after_snapshot
            )
            details['artifacts_found'] = artifacts_found

            if artifacts_found:
                return (
                    True,
                    f"Skill verified by artifact generation: {artifacts_found}",
                    details
                )

        # Decision logic
        if strict:
            # Strict mode: require artifacts
            if not details['artifacts_found']:
                return (
                    False,
                    "Strict mode: No artifacts found to confirm skill activation",
                    details
                )

        # Non-strict: accept content detection
        if details['detected_skill'] == expected_skill:
            return (
                True,
                f"Skill detected by content analysis (confidence: {details['confidence']})",
                details
            )

        # Soft pass if turn count high and no contradicting evidence
        if details['turn_count'] > 3:
            return (
                True,
                f"Probable skill activation (high turn count: {details['turn_count']})",
                details
            )

        return (False, "Could not verify skill activation", details)

    def _check_artifacts(
        self,
        skill_name: str,
        before: WorkspaceSnapshot,
        after: WorkspaceSnapshot
    ) -> List[str]:
        """
        Check if expected artifacts were created.

        Returns:
            List of artifact filenames found
        """
        if skill_name not in SKILL_ARTIFACTS:
            return []

        diff = before.diff(after)
        added_files = [str(path) for path in diff.added]

        artifact_config = SKILL_ARTIFACTS[skill_name]
        expected_patterns = artifact_config['files']
        location = artifact_config.get('location', '')

        found_artifacts = []

        for pattern in expected_patterns:
            if '*' in pattern:
                # Glob pattern
                matches = [f for f in added_files if Path(f).match(pattern)]
                if matches:
                    found_artifacts.extend(matches)
            else:
                # Exact match (partial path matching)
                matches = [f for f in added_files if pattern in f or Path(f).name == pattern]
                if matches:
                    found_artifacts.extend(matches)

        return found_artifacts

    def verify_workflow(
        self,
        responses: List[ClaudeResponse],
        expected_skills: List[str],
        snapshots: Optional[List[WorkspaceSnapshot]] = None
    ) -> Tuple[bool, str, List[Dict]]:
        """
        Verify a multi-skill workflow.

        Args:
            responses: List of responses in order
            expected_skills: List of expected skills in order
            snapshots: Optional list of workspace snapshots (before/after each)

        Returns:
            (success: bool, reason: str, details: List[dict])
        """
        if len(responses) != len(expected_skills):
            return (
                False,
                f"Mismatch: {len(responses)} responses but {len(expected_skills)} expected skills",
                []
            )

        all_details = []
        for i, (response, expected_skill) in enumerate(zip(responses, expected_skills)):
            before_snapshot = snapshots[i * 2] if snapshots and len(snapshots) > i * 2 else None
            after_snapshot = snapshots[i * 2 + 1] if snapshots and len(snapshots) > i * 2 + 1 else None

            success, reason, details = self.verify(
                response,
                expected_skill,
                before_snapshot,
                after_snapshot,
                strict=False
            )

            details['step'] = i + 1
            details['expected_skill'] = expected_skill
            details['success'] = success
            details['reason'] = reason

            all_details.append(details)

            if not success:
                return (
                    False,
                    f"Step {i+1} failed: {reason}",
                    all_details
                )

        return (True, "All workflow steps verified", all_details)


def validate_skill_activation(
    response: ClaudeResponse,
    expected_skill: str,
    before_snapshot: Optional[WorkspaceSnapshot] = None,
    after_snapshot: Optional[WorkspaceSnapshot] = None,
    client=None
) -> Tuple[bool, str]:
    """
    Convenience function for skill activation validation.

    Returns: (success: bool, reason: str)
    """
    verifier = SkillVerifier(client=client)
    success, reason, _ = verifier.verify(
        response,
        expected_skill,
        before_snapshot,
        after_snapshot
    )
    return (success, reason)
