"""
E2E tests for BMAD workflows (Level 2-4 complexity).

Tests the complete BMAD track from idea to implementation:
- Discovery/Research
- Product Planning
- UX Design
- Architecture
- Test Strategy
- Story Planning
- Development
"""

import pytest
from pathlib import Path


@pytest.mark.e2e
@pytest.mark.bmad
@pytest.mark.smoke
def test_new_idea_activates_discovery(claude_client, output_validator):
    """
    Test 1: New idea triggers bmad-discovery-research skill.

    Scenario: User expresses a new product idea
    Expected: Analyst skill activates and begins brainstorming
    """
    prompt = "I have an idea for a budgeting app that helps college students track their spending."

    response = claude_client.execute(prompt, verbose=True)

    # Validate skill activation
    assert output_validator.validate_skill_activation(
        response,
        expected_skill="bmad-discovery-research"
    ), "Discovery/Research skill should activate for new ideas"

    # Validate conversational response (asking questions, exploring)
    result_lower = response.result.lower()
    assert any(marker in result_lower for marker in [
        "explore", "brainstorm", "research", "discover", "question", "target"
    ]), "Response should indicate discovery/exploration mode"


@pytest.mark.e2e
@pytest.mark.bmad
@pytest.mark.slow
def test_prd_creation_workflow(session_manager, output_validator, runtime_workspace):
    """
    Test 2: PRD creation generates proper artifact.

    Scenario: User brainstorms idea, then requests PRD
    Expected: PM skill creates PRD.md with required sections
    """
    session = session_manager.start_session()

    # Turn 1: Introduce idea
    response1 = session_manager.execute_turn(
        session,
        "I want to build a budgeting app for college students. "
        "It should help them track spending, set budgets, and get alerts when overspending."
    )

    # Turn 2: Request PRD
    response2 = session_manager.execute_turn(
        session,
        "Create a PRD for this budgeting app."
    )

    # Validate skill transition to PM
    assert output_validator.validate_skill_activation(
        response2,
        expected_skill="bmad-product-planning"
    ), "Product Planning skill should activate for PRD request"

    # Find generated PRD
    artifacts_dir = runtime_workspace / "artifacts"
    prd_files = list(artifacts_dir.glob("**/PRD*.md")) + list(artifacts_dir.glob("**/prd*.md"))

    assert len(prd_files) > 0, f"PRD file should be created in {artifacts_dir}"

    prd_path = prd_files[0]

    # Validate PRD structure
    structure = output_validator.validate_artifact_structure(
        prd_path,
        required_sections=["Goals", "Features"]  # Minimum expected sections
    )

    assert structure["sections"], "PRD should have multiple sections"

    # Validate PRD content quality
    metrics = output_validator.validate_artifact_content(
        prd_path,
        required_keywords=["budget", "student"],  # Should reference the idea
        min_words=100  # PRD should be substantial
    )

    assert metrics["word_count"] >= 100, "PRD should be substantial (100+ words)"

    print(f"\n✅ PRD created at {prd_path}")
    print(f"   Sections: {structure['sections'][:5]}...")  # First 5 sections
    print(f"   Words: {metrics['word_count']}")
    print(session.summary())


@pytest.mark.e2e
@pytest.mark.bmad
@pytest.mark.slow
@pytest.mark.expensive
def test_full_bmad_workflow(session_manager, output_validator, runtime_workspace):
    """
    Test 3: Complete BMAD workflow from idea to stories.

    Scenario: Discovery → Planning → Architecture → Stories
    Expected: Each skill activates in sequence, artifacts created
    """
    session = session_manager.start_session()

    # Turn 1: Discovery
    response1 = session_manager.execute_turn(
        session,
        "I have an idea for a meditation timer app with guided sessions."
    )
    assert "discovery" in response1.result.lower() or "analyst" in response1.result.lower()

    # Turn 2: PRD
    response2 = session_manager.execute_turn(
        session,
        "Create a PRD for this meditation app."
    )
    assert output_validator.validate_skill_activation(response2, "bmad-product-planning")

    # Turn 3: Architecture
    response3 = session_manager.execute_turn(
        session,
        "Design the technical architecture for this app."
    )
    assert output_validator.validate_skill_activation(response3, "bmad-architecture-design")

    # Turn 4: Stories
    response4 = session_manager.execute_turn(
        session,
        "Break this down into developer stories."
    )
    assert output_validator.validate_skill_activation(response4, "bmad-story-planning")

    # Validate artifacts were created
    changes = session.get_all_changes()
    assert len(changes["added"]) > 0, "Multiple artifacts should be created"

    print(f"\n✅ Full BMAD workflow complete")
    print(f"   Total files created: {len(changes['added'])}")
    print(f"   Total cost: ${session.total_cost:.4f}")
    print(session.summary())


@pytest.mark.e2e
@pytest.mark.bmad
def test_orchestrator_routing(claude_client, output_validator):
    """
    Test 4: Orchestrator correctly routes based on complexity.

    Scenario: User asks "What's next?" or workflow status
    Expected: main-workflow-router activates and provides guidance
    """
    prompt = "What's my current workflow status?"

    response = claude_client.execute(prompt, verbose=True)

    result_lower = response.result.lower()

    # Should either activate orchestrator or provide status
    assert any(marker in result_lower for marker in [
        "workflow", "status", "level", "track", "bmad", "openspec", "next"
    ]), "Should provide workflow status information"
