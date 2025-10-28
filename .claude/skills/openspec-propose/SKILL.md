---
name: openspec-propose
description: Proactively activates for simple features/bug fixes (L0-1). Creates lightweight change proposals using OpenSpec methodology. Quick alternative to BMAD for small tasks. (user)
version: 1.0.0
source: OpenSpec by Fission-AI (https://github.com/Fission-AI/OpenSpec)
attribution: Based on OpenSpec workflow - Stage 1 (Creating Changes)
---

# OpenSpec Propose Skill

**Source**: OpenSpec by Fission-AI
**Reference**: https://github.com/Fission-AI/OpenSpec
**Purpose**: Create lightweight change proposals for simple features
**Workflow**: Stage 1 - Creating Changes

## 🎯 When Claude Should Invoke This Skill

**PROACTIVELY invoke this skill** when you detect the user:
- Wants to add a small feature to an existing project (Level 0-1)
- Mentions a bug fix or simple enhancement
- Says "add a...", "fix the...", "change the..." (simple modifications)
- Needs to modify existing behavior (not create whole new product)
- Wants something quick without full PRD/Architecture
- Already has a codebase and wants incremental changes

**DO NOT invoke for**:
- New products or complex features (use bmad-pm instead)
- Level 2-4 projects requiring PRD/Architecture
- Greenfield projects (use BMAD workflow)
- When user explicitly asks for "complete planning"

## OpenSpec Methodology

OpenSpec is a **spec-driven development** approach for simple changes:

1. **Draft a proposal** - Capture what needs to change
2. **Review and refine** - Iterate on specs until agreement
3. **Implement tasks** - Write code following approved specs
4. **Archive and update** - Merge changes back to specs

**Key Principle**: Agree on what to build BEFORE writing code (but lightweight, not heavy like BMAD)

## Your Workflow: Stage 1 - Creating Changes

### Step 1: Understand the Change Request

Ask clarifying questions:
- What existing behavior needs to change?
- What's the desired new behavior?
- Are there any edge cases or constraints?
- Is this breaking or non-breaking?

### Step 2: Create Change Directory

Structure:
```
openspec/
  changes/
    [feature-name]/
      proposal.md       # Why, what, impact
      tasks.md          # Sequential checklist
      design.md         # Technical design (optional)
      specs/            # Delta specifications
        [spec-name].md  # ADDED/MODIFIED/REMOVED changes
```

### Step 3: Write proposal.md

Template:
```markdown
# Proposal: [Feature Name]

## Why

[Problem statement - why is this change needed?]

## What

[Clear description of the proposed change]

### Success Criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Impact

**Breaking Changes**: Yes/No
**Affected Components**: [List]
**Dependencies**: [Any new dependencies needed]

## Alternatives Considered

[Other approaches you considered and why you chose this one]
```

### Step 4: Write tasks.md

Sequential, actionable tasks:
```markdown
# Implementation Tasks

- [ ] Task 1: [Specific, testable action]
- [ ] Task 2: [Next specific action]
- [ ] Task 3: [Write tests for X]
- [ ] Task 4: [Update documentation]
```

**Rules**:
- Each task = one concrete action
- Order tasks sequentially (do this, then this)
- Include test tasks
- Include documentation tasks

### Step 5: Write Delta Specs (Optional but Recommended)

Create `specs/[component-name].md` with deltas:

```markdown
# [Component Name] Specification

## ADDED

### Requirement: New Behavior X
SHALL do Y when Z happens.

#### Scenario: Happy Path
GIVEN user does A
WHEN they trigger B
THEN system responds with C

## MODIFIED

### Requirement: Updated Behavior (was: Old Requirement)
SHALL now do Y2 instead of Y1.

#### Scenario: Updated Flow
[New expected behavior]

## REMOVED

### Requirement: Deprecated Feature
[What's being removed and why]
```

**Delta Operations**:
- **ADDED** - New requirements/scenarios
- **MODIFIED** - Changed requirements (show old → new)
- **REMOVED** - Deprecated/deleted requirements
- **RENAMED** - Changed naming

### Step 6: Write design.md (Optional)

For technical changes, include:
```markdown
# Technical Design

## Architecture Changes

[How does this fit into existing architecture?]

## Data Model Changes

[Any DB schema changes, API changes, etc.]

## Implementation Approach

[High-level approach to implementation]

## Testing Strategy

[How will this be tested?]
```

### Step 7: Present to User

Show:
1. Summary of the proposal
2. List of tasks
3. Ask for approval before implementation

**Template**:
```
I've created an OpenSpec change proposal for [feature name]:

📋 Proposal: openspec/changes/[name]/proposal.md
  - Why: [1 sentence]
  - What: [1 sentence]
  - Impact: [Breaking/Non-breaking]

✅ Tasks: openspec/changes/[name]/tasks.md
  - [X] tasks total
  - Includes implementation, tests, docs

Would you like me to:
1. Refine the proposal?
2. Proceed to implementation (openspec-implement)?
3. Make changes to the scope?
```

## When to Skip Proposal

**Skip proposal creation** for:
- Typo fixes
- Obvious bug fixes (one-liner changes)
- Non-breaking dependency updates
- Documentation-only changes

For these, go straight to implementation.

## Critical Rules

### Formatting Requirements

- Scenarios MUST use `#### Scenario:` (four hashtags)
- Every requirement MUST have at least one scenario
- Use normative language: SHALL, MUST, SHOULD, MAY
- Delta operations: ADDED, MODIFIED, REMOVED, RENAMED

### Approval Gate

⚠️ **DO NOT implement until proposal is reviewed and approved by user**

Ask explicitly:
```
Is this proposal approved? Should I proceed with implementation?
```

## Example: Add Profile Search Filters

**User Request**: "Add search filters to the profile page"

**Your Response**:

1. **Ask clarifying questions**:
   - What fields should be filterable? (name, location, skills, etc.)
   - Should filters persist across sessions?
   - Any performance constraints?

2. **Create proposal** in `openspec/changes/profile-search-filters/`:
   - **proposal.md**: Why (better UX), What (add filter UI), Impact (non-breaking)
   - **tasks.md**:
     - Add filter component to profile page
     - Implement filter logic in search service
     - Add tests for filter combinations
     - Update profile page documentation
   - **specs/profile-search.md**: ADDED requirements for filter behavior

3. **Present for approval**:
   ```
   I've created a proposal for profile search filters:

   📋 Why: Users need to quickly find profiles matching criteria
   📋 What: Add filterable search UI with name/location/skills filters
   📋 Impact: Non-breaking, adds new feature

   ✅ 4 tasks: UI component, search logic, tests, docs

   Approve to proceed with implementation?
   ```

## File Locations

All changes go in:
```
openspec/changes/[feature-name]/
```

NOT in root or docs/ - keep isolated until archived.

## Next Steps

After proposal is approved:
- User says "implement" or "proceed" → Invoke `openspec-implement` skill
- User wants changes → Refine proposal.md and tasks.md
- User rejects → Discuss alternative approaches

## Communication Style

- **Concise and actionable** - OpenSpec is lightweight, not verbose
- **Show file locations** - Always cite where files are created
- **Seek approval explicitly** - Don't assume, ask
- **Focus on delta** - What's changing, not restating everything

---

**Remember**: OpenSpec is for SIMPLE changes. If the user's request grows complex (multiple epics, new product, architecture decisions), recommend switching to BMAD workflow instead.
