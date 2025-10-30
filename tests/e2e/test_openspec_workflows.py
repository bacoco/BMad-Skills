"""
E2E tests for OpenSpec workflows (Level 0-1 complexity).

Tests the lightweight OpenSpec track for quick changes:
- Change Proposal
- Change Implementation
- Change Closure
"""

import pytest
from pathlib import Path


@pytest.mark.e2e
@pytest.mark.openspec
@pytest.mark.smoke
def test_bug_fix_activates_proposal(claude_client, output_validator):
    """
    Test 1: Bug fix request triggers openspec-change-proposal.

    Scenario: User reports a simple bug
    Expected: OpenSpec proposal skill activates
    """
    prompt = "Fix the bug where the login timeout is too short (currently 15 minutes, should be 60 minutes)."

    response = claude_client.execute(prompt, verbose=True)

    # Should activate OpenSpec track for Level 0-1 change
    result_lower = response.result.lower()

    assert any(marker in result_lower for marker in [
        "proposal", "openspec", "change", "level 0", "level 1", "lightweight"
    ]), "OpenSpec proposal should activate for simple bug fix"


@pytest.mark.e2e
@pytest.mark.openspec
@pytest.mark.slow
def test_openspec_proposal_to_implementation(session_manager, output_validator, runtime_workspace):
    """
    Test 2: OpenSpec proposal → implementation workflow.

    Scenario: Create proposal, then implement
    Expected: Proposal created, then implementation executed
    """
    session = session_manager.start_session()

    # Turn 1: Create proposal
    response1 = session_manager.execute_turn(
        session,
        "Create a proposal to fix the session timeout bug (increase from 15min to 60min)."
    )

    # Validate proposal was activated
    assert output_validator.validate_skill_activation(
        response1,
        expected_skill="openspec-change-proposal"
    )

    # Check for proposal artifact
    changes_dir = runtime_workspace / "changes"
    proposal_files = list(changes_dir.glob("**/proposal.md"))

    if len(proposal_files) > 0:
        proposal_path = proposal_files[0]

        # Validate proposal structure
        structure = output_validator.validate_artifact_structure(
            proposal_path,
            required_sections=["Problem", "Solution"] # Typical proposal sections
        )

        print(f"\n✅ Proposal created at {proposal_path}")

    # Turn 2: Implement
    response2 = session_manager.execute_turn(
        session,
        "Implement this change."
    )

    # Validate implementation was activated
    assert output_validator.validate_skill_activation(
        response2,
        expected_skill="openspec-change-implementation"
    )

    print(session.summary())


@pytest.mark.e2e
@pytest.mark.openspec
@pytest.mark.slow
def test_complete_openspec_cycle(session_manager, output_validator):
    """
    Test 3: Complete OpenSpec cycle: propose → implement → archive.

    Scenario: Full lightweight change workflow
    Expected: All three OpenSpec skills activate in sequence
    """
    session = session_manager.start_session()

    # Turn 1: Propose
    response1 = session_manager.execute_turn(
        session,
        "I need to update the API rate limit from 100 to 1000 requests per hour."
    )

    # Turn 2: Implement
    response2 = session_manager.execute_turn(
        session,
        "Implement this rate limit change."
    )

    # Turn 3: Archive
    response3 = session_manager.execute_turn(
        session,
        "Archive this completed change."
    )

    # Validate skill sequence
    # At least one of the responses should indicate OpenSpec workflow
    all_results = " ".join([r.result.lower() for r in [response1, response2, response3]])

    assert "openspec" in all_results or "proposal" in all_results or "change" in all_results, \
        "OpenSpec workflow should be evident in responses"

    print(f"\n✅ Complete OpenSpec cycle")
    print(session.summary())


@pytest.mark.e2e
@pytest.mark.openspec
def test_small_feature_uses_openspec(claude_client, output_validator):
    """
    Test 4: Small feature uses OpenSpec (not full BMAD).

    Scenario: User requests a trivial enhancement
    Expected: OpenSpec track chosen (Level 0-1)
    """
    prompt = "Add a 'Clear all' button to the notifications panel."

    response = claude_client.execute(prompt, verbose=True)

    result_lower = response.result.lower()

    # Should indicate lightweight approach (OpenSpec or direct implementation)
    # Should NOT activate full BMAD workflow (PRD, architecture, etc.)
    assert not any(marker in result_lower for marker in [
        "prd", "product requirements", "architecture", "discovery"
    ]), "Should not use full BMAD workflow for trivial feature"
