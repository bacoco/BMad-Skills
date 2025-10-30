# Skill Activation Verification Guide

## Problem Statement

When testing BMAD Skills via `claude` CLI, we need to verify that:
1. Skills are actually activating (not just Claude responding generically)
2. The correct skill activates for a given prompt
3. Skills produce expected artifacts
4. Multi-skill workflows maintain context

## Methods for Verification

### Method 1: Content Analysis (Keywords)

**Principle:** Each skill has characteristic vocabulary and patterns in its responses.

**Implementation:**
```python
SKILL_SIGNATURES = {
    'bmad-discovery-research': {
        'keywords': ['discovery', 'research', 'explore', 'analyst', 'brainstorm', 'problem space'],
        'questions': ['What problem', 'Who are', 'pain point', 'target user'],
        'deliverables': ['Discovery Brief', 'research findings']
    },
    'bmad-product-planning': {
        'keywords': ['prd', 'product requirements', 'features', 'goals', 'metrics', 'success criteria'],
        'sections': ['Goals', 'Features', 'Requirements', 'Metrics'],
        'deliverables': ['PRD.md', 'product-requirements-document']
    },
    'bmad-architecture-design': {
        'keywords': ['architecture', 'technical design', 'system design', 'components', 'data flow'],
        'patterns': ['tech stack', 'scalability', 'database'],
        'deliverables': ['architecture-decisions.md', 'technical-design']
    },
    'bmad-ux-design': {
        'keywords': ['ux', 'user flow', 'wireframe', 'user experience', 'interface'],
        'deliverables': ['user-flows.md', 'wireframes']
    },
    'openspec-change-proposal': {
        'keywords': ['proposal', 'level 0', 'level 1', 'lightweight', 'change'],
        'deliverables': ['proposal.md', 'tasks.md']
    }
}

def detect_skill_activation(response_text: str) -> Optional[str]:
    """Detect which skill was activated based on response content."""
    scores = {}

    for skill_name, signature in SKILL_SIGNATURES.items():
        score = 0
        text_lower = response_text.lower()

        # Count keyword matches
        for keyword in signature.get('keywords', []):
            if keyword in text_lower:
                score += 2

        # Count question patterns
        for question in signature.get('questions', []):
            if question.lower() in text_lower:
                score += 1

        # Count section headers
        for section in signature.get('sections', []):
            if section.lower() in text_lower:
                score += 3

        scores[skill_name] = score

    # Return skill with highest score if above threshold
    if max(scores.values()) >= 3:
        return max(scores, key=scores.get)
    return None
```

**Pros:** Fast, doesn't require file system access
**Cons:** Heuristic, can have false positives

---

### Method 2: Artifact Detection (File System)

**Principle:** Skills generate specific artifacts in known locations.

**Implementation:**
```python
from pathlib import Path
from workspace_snapshot import WorkspaceSnapshot

def verify_skill_by_artifacts(before: WorkspaceSnapshot, after: WorkspaceSnapshot, expected_skill: str) -> bool:
    """Verify skill activation by checking generated artifacts."""

    SKILL_ARTIFACTS = {
        'bmad-product-planning': ['PRD.md', 'prd.md', 'product-requirements-document.md'],
        'bmad-discovery-research': ['discovery-brief.md', 'research-notes.md'],
        'bmad-architecture-design': ['architecture-decisions.md', 'technical-design.md'],
        'bmad-ux-design': ['user-flows.md', 'wireframes.md'],
        'bmad-story-planning': ['story-*.md'],  # Glob pattern
        'openspec-change-proposal': ['proposal.md', 'tasks.md'],
    }

    diff = before.diff(after)
    added_files = [str(path) for path in diff.added]

    expected_patterns = SKILL_ARTIFACTS.get(expected_skill, [])

    for pattern in expected_patterns:
        if '*' in pattern:
            # Glob pattern
            if any(Path(f).match(pattern) for f in added_files):
                return True
        else:
            # Exact match
            if any(pattern in f for f in added_files):
                return True

    return False
```

**Pros:** Definitive proof of skill execution
**Cons:** Requires write permissions, slower, not all skills produce immediate artifacts

---

### Method 3: Turn Count Analysis

**Principle:** Skills involve internal tool calls, increasing turn count.

**Implementation:**
```python
def is_skill_activated(response_json: dict) -> bool:
    """Check if a skill was likely activated based on turn count."""
    num_turns = response_json.get('num_turns', 1)

    # Single turn = no skill activation (just direct response)
    # Multiple turns = skill activation with internal tool use
    return num_turns > 1
```

**Pros:** Simple, available in JSON response
**Cons:** Not specific to which skill, can have false positives from other tools

---

### Method 4: Permission Denials Analysis

**Principle:** If `Skill` tool was denied, no skill activated.

**Implementation:**
```python
def check_skill_blocked(response_json: dict) -> bool:
    """Check if skill activation was blocked by permissions."""
    denials = response_json.get('permission_denials', [])

    for denial in denials:
        if denial.get('tool_name') == 'Skill':
            return True
    return False
```

**Pros:** Definitive proof skill was attempted but blocked
**Cons:** Only detects failures, not successes

---

## Recommended Verification Strategy

**Multi-level validation** for robust E2E testing:

```python
def validate_skill_activation(
    prompt: str,
    response: ClaudeResponse,
    expected_skill: str,
    before_snapshot: WorkspaceSnapshot,
    after_snapshot: WorkspaceSnapshot
) -> Tuple[bool, str]:
    """
    Validate skill activation using multiple methods.

    Returns: (success: bool, reason: str)
    """

    # Level 1: Check if blocked
    if check_skill_blocked(response.raw_json):
        return (False, "Skill tool was denied by permissions")

    # Level 2: Check turn count (quick filter)
    if not is_skill_activated(response.raw_json):
        return (False, "No skill activation detected (single turn)")

    # Level 3: Content analysis
    detected_skill = detect_skill_activation(response.result)
    if detected_skill != expected_skill:
        if detected_skill:
            return (False, f"Wrong skill detected: {detected_skill} (expected {expected_skill})")
        # Continue to artifact check if no clear content signal

    # Level 4: Artifact verification (strongest proof)
    if verify_skill_by_artifacts(before_snapshot, after_snapshot, expected_skill):
        return (True, f"Skill verified by artifact generation")

    # Level 5: Soft match - content analysis with lower threshold
    if detected_skill == expected_skill:
        return (True, f"Skill detected by content analysis")

    return (False, "Could not verify skill activation")
```

---

## CLI Configuration for Skill Testing

### Required Permissions

To allow skills to activate in batch mode:

```bash
claude -p \
  --output-format json \
  --allowedTools "Skill Read Write Grep" \
  <<< "Your prompt"
```

**Critical:** `Skill` tool MUST be in allowed tools for skills to activate.

### Optional: Bypass Permissions (Dev Only)

```bash
claude -p \
  --output-format json \
  --dangerously-skip-permissions \
  <<< "Your prompt"
```

⚠️ **Warning:** Only use in trusted development environments.

---

## E2E Test Template

```python
import pytest
from helpers import ClaudeClient, WorkspaceSnapshot, validate_skill_activation

@pytest.mark.e2e
def test_discovery_skill_activation(runtime_workspace):
    """Test that discovery skill activates for new ideas."""

    # Setup
    client = ClaudeClient()
    before = WorkspaceSnapshot.capture(runtime_workspace)

    # Execute with proper permissions
    response = client.execute(
        "I have an idea for a budgeting app",
        allowed_tools=["Skill", "Read", "Write", "Grep"]
    )

    # Capture after state
    after = WorkspaceSnapshot.capture(runtime_workspace)

    # Validate
    success, reason = validate_skill_activation(
        prompt="I have an idea for a budgeting app",
        response=response,
        expected_skill="bmad-discovery-research",
        before_snapshot=before,
        after_snapshot=after
    )

    assert success, f"Skill activation failed: {reason}"

    # Additional assertions
    assert "discovery" in response.result.lower() or "research" in response.result.lower()
    assert response.duration_ms < 120000  # Should complete within 2 min
```

---

## Known Limitations

### Batch Mode vs Interactive Mode

**Issue:** Skills behave differently in `claude -p` (batch) vs interactive mode.

**Impact:**
- Batch mode: Skills may not auto-activate as smoothly
- Interactive mode: Better context, but harder to automate

**Workaround:** Use `pexpect` for interactive testing:

```python
import pexpect

def test_skill_activation_interactive():
    child = pexpect.spawn('claude', ['--allowedTools', 'Skill Read Write Grep'])
    child.expect('>', timeout=10)

    child.sendline('I have an idea for a todo app')

    # Wait for skill activation
    index = child.expect(['discovery', 'research', pexpect.TIMEOUT], timeout=60)

    assert index != 2, "Skill activation timed out"

    child.close()
```

---

## Debugging Failed Activations

### Checklist

1. **Are skills installed?**
   ```bash
   ls -la .claude/skills/ | grep bmad
   ```

2. **Are permissions correct?**
   ```bash
   # Check permission denials in JSON response
   jq '.permission_denials' response.json
   ```

3. **Is Skill tool allowed?**
   ```bash
   # Must include "Skill" in allowedTools
   claude -p --allowedTools "Skill Read Write" ...
   ```

4. **Check turn count:**
   ```bash
   # Should be > 1 if skill activated
   jq '.num_turns' response.json
   ```

5. **Inspect response content:**
   ```bash
   # Look for skill-specific vocabulary
   jq -r '.result' response.json | grep -i "discovery\|research"
   ```

---

## Future Improvements

### Explicit Skill Metadata in JSON

**Proposal:** Claude CLI should return explicit skill activation metadata:

```json
{
  "result": "...",
  "skills_activated": [
    {
      "name": "bmad-discovery-research",
      "timestamp": "2025-10-30T14:30:00Z",
      "duration_ms": 5000
    }
  ]
}
```

**Benefit:** No heuristic guessing needed.

### Skill Activation Logs

**Proposal:** Skills write activation log to workspace:

```
.claude/skills/_runtime/activation.log
2025-10-30T14:30:00Z bmad-discovery-research ACTIVATED prompt="I have an idea..."
2025-10-30T14:35:00Z bmad-product-planning ACTIVATED prompt="Create a PRD..."
```

**Benefit:** Easy verification via file system.

---

## Summary

**Best practices for verifying skill activation:**

1. ✅ Use multi-level validation (content + artifacts + turn count)
2. ✅ Always include `Skill` in `--allowedTools`
3. ✅ Use workspace snapshots to detect artifacts
4. ✅ Check permission denials for debugging
5. ✅ Accept that some verification is heuristic (until CLI provides explicit metadata)

**For production E2E tests:**
- Use combination of content analysis + artifact detection
- Set reasonable timeouts (skills can be slow)
- Log all verification steps for debugging
- Mark flaky tests appropriately
