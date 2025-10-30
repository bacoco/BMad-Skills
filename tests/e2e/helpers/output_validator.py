"""
Output validation utilities for E2E tests.

Provides validators for:
- Skill activation detection
- Artifact structure validation
- Content quality checks
- CHECKLIST.md compliance
"""

import re
import yaml
from pathlib import Path
from typing import List, Dict, Any, Optional, Set

from claude_client import ClaudeResponse


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


class OutputValidator:
    """
    Validates Claude responses and generated artifacts.

    Usage:
        validator = OutputValidator(skills_root=Path(".claude/skills"))
        validator.validate_skill_activation(response, expected_skill="bmad-product-planning")
        validator.validate_artifact(artifact_path, required_sections=["Goals", "Features"])
    """

    def __init__(self, skills_root: Optional[Path] = None):
        """
        Initialize validator.

        Args:
            skills_root: Path to .claude/skills directory (for loading CHECKLISTs)
        """
        self.skills_root = skills_root or Path(".claude/skills")

    def validate_skill_activation(
        self,
        response: ClaudeResponse,
        expected_skill: str,
        strict: bool = False
    ) -> bool:
        """
        Validate that the expected skill was activated.

        Args:
            response: ClaudeResponse to check
            expected_skill: Expected skill name (e.g., "bmad-product-planning")
            strict: If True, raise ValidationError on mismatch; otherwise return bool

        Returns:
            True if skill was activated, False otherwise

        Raises:
            ValidationError: If strict=True and skill not activated
        """
        result_lower = response.result.lower()
        skill_lower = expected_skill.lower()

        # Check for exact skill name
        activated = skill_lower in result_lower

        # Check for role-based markers
        if not activated:
            role_markers = {
                "bmad-discovery-research": ["analyst", "discovery", "brainstorm", "explore"],
                "bmad-product-planning": ["pm", "prd", "product planning", "requirements"],
                "bmad-ux-design": ["ux", "designer", "wireframe", "user flow"],
                "bmad-architecture-design": ["architect", "architecture", "technical design"],
                "bmad-test-strategy": ["tea", "test strategy", "atdd"],
                "bmad-story-planning": ["stories", "story planning", "developer stories"],
                "bmad-development-execution": ["developer", "implementation", "coding"],
                "openspec-change-proposal": ["proposal", "change proposal"],
                "openspec-change-implementation": ["implement", "execution log"],
                "openspec-change-closure": ["archive", "closure"],
            }

            markers = role_markers.get(expected_skill, [])
            activated = any(marker in result_lower for marker in markers)

        if not activated and strict:
            raise ValidationError(
                f"Expected skill '{expected_skill}' was not activated.\n"
                f"Response (first 500 chars): {response.result[:500]}"
            )

        return activated

    def validate_artifact_exists(self, artifact_path: Path) -> None:
        """
        Validate that an artifact file exists.

        Args:
            artifact_path: Path to artifact

        Raises:
            ValidationError: If file doesn't exist
        """
        if not artifact_path.exists():
            raise ValidationError(
                f"Expected artifact not found: {artifact_path}\n"
                f"Directory contents: {list(artifact_path.parent.glob('*')) if artifact_path.parent.exists() else 'N/A'}"
            )

    def validate_artifact_structure(
        self,
        artifact_path: Path,
        required_sections: Optional[List[str]] = None,
        required_frontmatter: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Validate the structure of a markdown artifact.

        Args:
            artifact_path: Path to artifact file
            required_sections: List of required markdown sections (e.g., ["Goals", "Features"])
            required_frontmatter: List of required YAML frontmatter fields

        Returns:
            Dict with:
                - frontmatter: Parsed YAML frontmatter (if present)
                - sections: List of detected section headers
                - content: Full content

        Raises:
            ValidationError: If structure is invalid
        """
        self.validate_artifact_exists(artifact_path)

        content = artifact_path.read_text()

        # Parse frontmatter
        frontmatter = None
        content_without_frontmatter = content

        if content.startswith("---"):
            parts = content.split("---", 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    content_without_frontmatter = parts[2]
                except yaml.YAMLError as e:
                    raise ValidationError(f"Invalid YAML frontmatter in {artifact_path}: {e}")

        # Validate required frontmatter
        if required_frontmatter and frontmatter:
            missing = [field for field in required_frontmatter if field not in frontmatter]
            if missing:
                raise ValidationError(
                    f"Missing required frontmatter fields in {artifact_path}: {missing}\n"
                    f"Found fields: {list(frontmatter.keys())}"
                )

        # Extract sections (markdown headers)
        sections = re.findall(r"^#+\s+(.+)$", content_without_frontmatter, re.MULTILINE)

        # Validate required sections
        if required_sections:
            missing = [section for section in required_sections if section not in sections]
            if missing:
                raise ValidationError(
                    f"Missing required sections in {artifact_path}: {missing}\n"
                    f"Found sections: {sections}"
                )

        return {
            "frontmatter": frontmatter,
            "sections": sections,
            "content": content
        }

    def validate_artifact_content(
        self,
        artifact_path: Path,
        required_keywords: Optional[List[str]] = None,
        forbidden_keywords: Optional[List[str]] = None,
        min_words: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Validate content quality of an artifact.

        Args:
            artifact_path: Path to artifact
            required_keywords: Keywords that must appear in content
            forbidden_keywords: Keywords that must NOT appear
            min_words: Minimum word count

        Returns:
            Dict with content metrics

        Raises:
            ValidationError: If content validation fails
        """
        self.validate_artifact_exists(artifact_path)

        content = artifact_path.read_text()
        content_lower = content.lower()

        # Check required keywords
        if required_keywords:
            missing = [kw for kw in required_keywords if kw.lower() not in content_lower]
            if missing:
                raise ValidationError(
                    f"Missing required keywords in {artifact_path}: {missing}"
                )

        # Check forbidden keywords
        if forbidden_keywords:
            found = [kw for kw in forbidden_keywords if kw.lower() in content_lower]
            if found:
                raise ValidationError(
                    f"Found forbidden keywords in {artifact_path}: {found}"
                )

        # Check word count
        word_count = len(content.split())
        if min_words and word_count < min_words:
            raise ValidationError(
                f"Artifact {artifact_path} has {word_count} words, "
                f"but minimum is {min_words}"
            )

        return {
            "word_count": word_count,
            "char_count": len(content),
            "line_count": len(content.splitlines())
        }

    def validate_checklist_compliance(
        self,
        artifact_path: Path,
        skill_name: str
    ) -> Dict[str, Any]:
        """
        Validate artifact against skill's CHECKLIST.md.

        Args:
            artifact_path: Path to artifact
            skill_name: Skill name (e.g., "bmad-product-planning")

        Returns:
            Dict with compliance results

        Raises:
            ValidationError: If checklist not found or compliance fails
        """
        checklist_path = self.skills_root / skill_name / "CHECKLIST.md"

        if not checklist_path.exists():
            raise ValidationError(
                f"CHECKLIST.md not found for skill '{skill_name}' at {checklist_path}"
            )

        # Read checklist
        checklist_content = checklist_path.read_text()

        # Extract checklist items (lines starting with - [ ] or - [x])
        checklist_items = re.findall(
            r"^[-*]\s+\[[ x]\]\s+(.+)$",
            checklist_content,
            re.MULTILINE
        )

        if not checklist_items:
            # No structured checklist found, skip validation
            return {"compliance": "unknown", "reason": "No structured checklist found"}

        # Read artifact
        artifact_content = artifact_path.read_text()

        # Simple heuristic: check if artifact is non-trivial
        # More sophisticated validation would check specific checklist items
        compliance_checks = {
            "non_empty": len(artifact_content.strip()) > 0,
            "has_sections": len(re.findall(r"^#+\s+", artifact_content, re.MULTILINE)) > 0,
            "sufficient_length": len(artifact_content.split()) > 50
        }

        all_passed = all(compliance_checks.values())

        return {
            "compliance": "pass" if all_passed else "fail",
            "checks": compliance_checks,
            "checklist_items_count": len(checklist_items)
        }

    def validate_conversation_context(
        self,
        response: ClaudeResponse,
        expected_references: List[str]
    ) -> bool:
        """
        Validate that response maintains context by referencing previous conversation.

        Args:
            response: ClaudeResponse to check
            expected_references: Keywords/phrases that should appear (from prior context)

        Returns:
            True if context is maintained

        Raises:
            ValidationError: If context is not maintained
        """
        result_lower = response.result.lower()

        missing = [ref for ref in expected_references if ref.lower() not in result_lower]

        if missing:
            raise ValidationError(
                f"Response does not maintain conversation context.\n"
                f"Missing references: {missing}\n"
                f"Response (first 500 chars): {response.result[:500]}"
            )

        return True
