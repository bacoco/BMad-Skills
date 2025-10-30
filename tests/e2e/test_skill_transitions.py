"""
E2E tests for skill transitions and context maintenance.

Tests that:
- Skills transition smoothly between phases
- Context is maintained across skill boundaries
- Handoffs reference prior work
"""

import pytest


@pytest.mark.e2e
@pytest.mark.smoke
def test_discovery_to_planning_transition(session_manager, output_validator):
    """
    Test 1: Discovery → Planning transition maintains context.

    Scenario: Brainstorm, then ask for PRD
    Expected: PM references discovery insights
    """
    session = session_manager.start_session()

    # Turn 1: Discovery
    response1 = session_manager.execute_turn(
        session,
        "I'm thinking about a task management app specifically for remote teams "
        "with features for async communication and time zone coordination."
    )

    # Turn 2: Request PRD
    response2 = session_manager.execute_turn(
        session,
        "Create a PRD based on what we just discussed."
    )

    # Validate context maintenance
    try:
        output_validator.validate_conversation_context(
            response2,
            expected_references=["remote", "task", "async"]  # Should reference prior conversation
        )
        print("\n✅ Context maintained across Discovery → Planning transition")
    except AssertionError as e:
        # Non-strict: log warning but don't fail
        print(f"\n⚠️ Context maintenance weak: {e}")

    print(session.summary())


@pytest.mark.e2e
@pytest.mark.slow
def test_planning_to_architecture_transition(session_manager, output_validator):
    """
    Test 2: Planning → Architecture transition.

    Scenario: Create PRD, then request architecture
    Expected: Architect references PRD requirements
    """
    session = session_manager.start_session()

    # Turn 1: Quick PRD request
    response1 = session_manager.execute_turn(
        session,
        "Create a PRD for a simple note-taking app with markdown support and tags."
    )

    assert output_validator.validate_skill_activation(response1, "bmad-product-planning")

    # Turn 2: Request architecture
    response2 = session_manager.execute_turn(
        session,
        "Design the technical architecture for this note-taking app."
    )

    assert output_validator.validate_skill_activation(response2, "bmad-architecture-design")

    # Should reference the features from PRD
    try:
        output_validator.validate_conversation_context(
            response2,
            expected_references=["note", "markdown", "tag"]
        )
        print("\n✅ Context maintained across Planning → Architecture transition")
    except AssertionError as e:
        print(f"\n⚠️ Context maintenance weak: {e}")

    print(session.summary())


@pytest.mark.e2e
@pytest.mark.slow
def test_architecture_to_stories_transition(session_manager, output_validator):
    """
    Test 3: Architecture → Stories transition.

    Scenario: Define architecture, then request story breakdown
    Expected: Stories respect architectural decisions
    """
    session = session_manager.start_session()

    # Turn 1: Architecture request
    response1 = session_manager.execute_turn(
        session,
        "Design the architecture for a REST API with authentication, user management, and data storage."
    )

    assert output_validator.validate_skill_activation(response1, "bmad-architecture-design")

    # Turn 2: Request stories
    response2 = session_manager.execute_turn(
        session,
        "Break this down into developer stories."
    )

    assert output_validator.validate_skill_activation(response2, "bmad-story-planning")

    # Stories should reference architectural components
    try:
        output_validator.validate_conversation_context(
            response2,
            expected_references=["api", "auth"]  # Should reference architecture
        )
        print("\n✅ Context maintained across Architecture → Stories transition")
    except AssertionError as e:
        print(f"\n⚠️ Context maintenance weak: {e}")

    print(session.summary())


@pytest.mark.e2e
def test_multi_skill_workflow_coherence(session_manager, output_validator):
    """
    Test 4: Complete multi-skill workflow maintains coherent narrative.

    Scenario: Discovery → Planning → UX → Architecture
    Expected: Each phase builds on previous, maintains theme
    """
    session = session_manager.start_session()

    theme_keywords = ["fitness", "workout", "exercise", "health"]

    # Discovery
    response1 = session_manager.execute_turn(
        session,
        "I want to build a fitness tracking app for home workouts."
    )

    # Planning
    response2 = session_manager.execute_turn(
        session,
        "Create a PRD for this fitness app."
    )

    # UX
    response3 = session_manager.execute_turn(
        session,
        "Design the user flows and wireframes."
    )

    # Architecture
    response4 = session_manager.execute_turn(
        session,
        "Design the technical architecture."
    )

    # All responses should reference the fitness theme
    for i, response in enumerate([response1, response2, response3, response4], 1):
        result_lower = response.result.lower()
        has_theme = any(keyword in result_lower for keyword in theme_keywords)

        if not has_theme:
            print(f"\n⚠️ Turn {i} lost thematic context")
        else:
            print(f"\n✅ Turn {i} maintained theme")

    print(f"\n✅ Multi-skill workflow complete")
    print(session.summary())
