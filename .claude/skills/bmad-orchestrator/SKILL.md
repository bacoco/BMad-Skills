---
name: bmad-orchestrator
description: Orchestrates the BMAD workflow phases (Planning → Solutioning → Implementation). Load this when starting a new project or feature to guide through the proper BMAD sequence.
version: 1.0.0
source: BMAD Method v6-alpha (https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)
attribution: Based on BMAD Method workflow sequencing and phase gates
---

# BMAD Orchestrator Skill

**Source**: BMAD Method v6-alpha Workflow Sequencing
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
**Purpose**: Guide users through the complete BMAD workflow in proper sequence

## When to Load This Skill

Load this skill when:
- User wants to start a new project or major feature
- User asks "how do I use BMAD?" or "what's the workflow?"
- User wants guidance on what to do next in BMAD process
- User is unsure which skill/phase to use
- Starting a new project from scratch

**Do NOT load for**:
- Executing a specific phase (use the phase-specific skill instead)
- Bug fixes or small changes (BMAD is overkill)
- When already in middle of a specific workflow phase

## BMAD Method Overview

BMAD (Boring Made Amazing Development) is a structured, agent-driven methodology that takes features from idea to implementation through four phases:

**Phase 1: Analysis** (Optional)
- Creative exploration and investigation
- Use for complex/novel problems
- Skippable for straightforward features

**Phase 2: Planning** (Required for Level 2-4)
- Create PRD (Product Requirements Document)
- Create Epic Breakdown
- **Skill**: `bmad-pm`
- **Outputs**: `docs/PRD.md`, `docs/epics.md`

**Phase 3: Solutioning** (Required for Level 2-4)
- Create Decision Architecture
- Make all technical decisions
- Define consistency patterns
- **Skill**: `bmad-architecture`
- **Precondition**: PRD must exist
- **Output**: `docs/ARCHITECTURE.md`

**Phase 4: Implementation** (Iterative)
- Create developer-ready stories
- Implement stories one by one
- **Skill**: `bmad-stories` (story creation)
- **Precondition**: PRD and Architecture must exist
- **Outputs**: `stories/*.md` files

## Project Level Assessment

First, determine the project level:

### Level 0-1: Simple Change / Bug Fix
- **Scope**: Single file or small isolated change
- **Workflow**: Skip BMAD, just fix it
- **Examples**: Bug fix, config update, documentation update

### Level 2: New Feature (MVP)
- **Scope**: 8-15 Functional Requirements, 1-2 Epics, 5-15 Stories
- **Workflow**: Planning → Solutioning → Implementation
- **Use**: Full BMAD workflow
- **Examples**: User authentication, basic CRUD feature

### Level 3: Comprehensive Product
- **Scope**: 12-25 FRs, 2-5 Epics, 15-40 Stories
- **Workflow**: Optional Analysis → Planning → Solutioning → Implementation
- **Use**: Full BMAD workflow with optional analysis phase
- **Examples**: Multi-feature product, platform component

### Level 4: Enterprise Platform
- **Scope**: 20-35+ FRs, 5-10+ Epics, 40-100+ Stories
- **Workflow**: Analysis → Planning → Solutioning → Implementation
- **Use**: Full BMAD workflow with required analysis
- **Examples**: Multi-tenant SaaS, enterprise system

## Workflow Sequence (Level 2-4)

### Start Here: Assess Project Level

Ask the user:
1. What are you building?
2. How complex is it?
3. Is this greenfield (new) or brownfield (existing codebase)?

Based on answers, determine Level 0-4.

**If Level 0-1**: Inform user BMAD is overkill. Proceed with simple implementation.

**If Level 2-4**: Continue with BMAD workflow below.

---

### Phase 2: Planning (REQUIRED)

**Goal**: Create PRD and Epic Breakdown

**When to Start**:
- Project is Level 2-4
- No PRD exists yet
- User has a feature idea but needs structure

**How to Execute**:
1. Tell user: "Let's start with Planning phase using the bmad-pm skill"
2. Guide user to describe their feature/project
3. Load the `bmad-pm` skill (or tell user you're using it)
4. Follow bmad-pm skill instructions to:
   - Gather requirements (goals, FRs, NFRs, journeys)
   - Define epic structure
   - Break epics into stories
   - Generate `docs/PRD.md` and `docs/epics.md`

**Phase Gate**: Do not proceed to Solutioning until:
- `docs/PRD.md` exists and is complete
- `docs/epics.md` exists with story breakdown
- User has reviewed and approved

**Exit Criteria**:
✅ PRD contains all required sections (Goals, FRs, NFRs, Epics, Out of Scope)
✅ Epics are broken into sequenced stories
✅ Epic 1 establishes foundation
✅ No forward dependencies in story sequence

---

### Phase 3: Solutioning (REQUIRED for Level 2-4)

**Goal**: Create Decision Architecture

**When to Start**:
- Planning phase is complete
- `docs/PRD.md` and `docs/epics.md` exist
- User approved the PRD

**How to Execute**:
1. Verify PRD exists: `docs/PRD.md`
2. Tell user: "Now let's create the architecture using bmad-architecture skill"
3. Load the `bmad-architecture` skill
4. Follow bmad-architecture skill instructions to:
   - Read and understand PRD
   - Discover/evaluate starter templates
   - Make all architectural decisions
   - Design novel patterns (if needed)
   - Define implementation patterns
   - Generate `docs/ARCHITECTURE.md`

**Phase Gate**: Do not proceed to Story Creation until:
- `docs/ARCHITECTURE.md` exists and is complete
- All architectural decisions documented with versions
- Every epic mapped to architecture components
- Implementation patterns defined
- User has reviewed and approved

**Exit Criteria**:
✅ ARCHITECTURE.md contains all required sections
✅ Decision table has specific versions (not "latest")
✅ Every epic mapped to components
✅ Project structure defined (no placeholders)
✅ Implementation patterns documented
✅ Consistency rules defined (naming, formatting, etc.)

**Scale Exception for Level 1**:
If project is very small (Level 1), architecture can be brief or skipped. A simple "Changes are isolated to X module, no new infra" note may suffice.

---

### Phase 4: Implementation - Story Creation (REQUIRED)

**Goal**: Create Developer-Ready Story Files

**When to Start**:
- Planning and Solutioning phases complete
- `docs/PRD.md`, `docs/epics.md`, and `docs/ARCHITECTURE.md` exist
- Ready to prepare stories for development

**How to Execute**:
1. Verify prerequisites exist: PRD, epics, Architecture
2. Tell user: "Let's create stories using bmad-stories skill"
3. Load the `bmad-stories` skill
4. For each story (in sequence):
   - Extract story details from `docs/epics.md`
   - Check previous story for learnings/context
   - Extract architecture constraints
   - Create tasks mapped to acceptance criteria
   - Write dev notes with patterns and structure
   - Generate story file: `stories/{epic}-{story}-{title}.md`

**Important**:
- Create stories in sequential order within each epic
- Always check previous story for context and learnings
- Each story should be AI-agent sized (2-4 hours)
- Stories must be vertical slices (complete functionality)

**Exit Criteria for Story Creation**:
✅ Story file created in `stories/` directory
✅ Acceptance criteria clear and testable
✅ Tasks map to acceptance criteria
✅ Dev notes include architecture patterns
✅ Previous story learnings included (if applicable)
✅ All sources cited

---

### Phase 4: Implementation - Development (ITERATIVE)

**Goal**: Implement Stories One by One

**When to Start**:
- Story files exist in `stories/` directory
- Story is marked "drafted" and ready

**How to Execute**:
1. Developer (human or AI) reads story file
2. Implements according to specifications
3. Updates "Dev Agent Record" section:
   - Context Reference
   - Agent Model Used
   - Debug Log References
   - Completion Notes (patterns created, deviations, technical debt)
   - File List (NEW, MODIFIED, DELETED files)
4. Marks tasks complete as work progresses
5. Updates story status: drafted → in-progress → review → done

**Phase Gate for Next Story**:
- Previous story must be "done" before creating next story
- OR previous story "in-progress" but at a reasonable checkpoint

---

## Critical Workflow Rules

### Rule 1: No Skipping Phases (Level 2-4)
You MUST complete phases in order:
1. Planning (PRD + Epics)
2. Solutioning (Architecture)
3. Story Creation
4. Implementation

Exception: Level 0-1 can skip BMAD entirely.

### Rule 2: No Code Before Stories
Do NOT write implementation code until:
- At least one story file exists in `stories/` directory
- Story is marked "drafted" or "ready"
- Story contains acceptance criteria and architecture guidance

### Rule 3: Phase Gate Validation
Before moving to next phase, verify exit criteria:
- Planning → Check PRD and epics exist and are complete
- Solutioning → Check Architecture exists with all decisions
- Story Creation → Check story file has all required sections

### Rule 4: Sequential Story Creation
Within an epic:
- Create stories in order (Story 1.1, then 1.2, then 1.3, etc.)
- Always check previous story for context before creating next
- Maintain continuity (reuse patterns, don't recreate)

### Rule 5: Scale Adaptation
- Level 1: Architecture may be brief or skipped
- Level 2: Full workflow, but lighter touch
- Level 3-4: Comprehensive workflow with all details

## Status Checking

At any time, user can ask "where are we in the workflow?"

Check and report:
1. **Planning Phase**:
   - ✅ Complete if `docs/PRD.md` and `docs/epics.md` exist
   - ❌ Incomplete otherwise

2. **Solutioning Phase**:
   - ✅ Complete if `docs/ARCHITECTURE.md` exists and has decision table
   - ❌ Incomplete otherwise

3. **Story Creation Phase**:
   - ✅ In progress if some stories exist in `stories/`
   - ❌ Not started if `stories/` is empty
   - Report count: "X of Y stories created"

4. **Implementation Phase**:
   - Report stories by status: drafted, in-progress, review, done
   - Identify next story to implement

## User Guidance

### Starting Fresh
User: "I want to build a feature where users can..."

You:
1. Assess complexity → Determine Level
2. If Level 2-4: "Let's use BMAD workflow. We'll start with Planning phase."
3. Guide to bmad-pm skill

### Mid-Workflow
User: "What do I do next?"

You:
1. Check what exists: PRD? Architecture? Stories?
2. Identify current phase
3. Guide to next phase or next story

### Already Have Docs
User: "I already have a PRD, how do I proceed?"

You:
1. Verify PRD exists and is BMAD-compliant
2. Check if epics exist
3. If yes: Proceed to Solutioning (bmad-architecture)
4. If no: Complete epics first (bmad-pm)

## Common Scenarios

### Scenario 1: Brand New Feature
```
User → Orchestrator → Assess Level (L2) → bmad-pm → PRD + Epics
     → bmad-architecture → Architecture
     → bmad-stories → Story 1.1, 1.2, ... 2.1, 2.2, ...
     → Implementation → Implement stories sequentially
```

### Scenario 2: Have PRD, Need Architecture
```
User → Orchestrator → Verify PRD exists → bmad-architecture → Architecture
     → bmad-stories → Stories
     → Implementation
```

### Scenario 3: Have Everything, Create Next Story
```
User → Orchestrator → Verify PRD + Arch exist → bmad-stories → Next story
```

### Scenario 4: Bug Fix (Level 0)
```
User → Orchestrator → Assess Level (L0) → "BMAD is overkill, just fix it"
```

## Your Role as Orchestrator

1. **Assess** - Determine project level and current phase
2. **Guide** - Tell user which skill to use next
3. **Validate** - Check phase gate criteria before advancing
4. **Enforce** - Ensure proper sequence (no skipping phases)
5. **Status** - Report progress and next steps clearly

You are NOT implementing the phases yourself. You are the guide that tells the user (or Claude) which skill to load next and ensures proper workflow sequencing.

---

**Attribution**: Based on BMAD Method v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org
**Purpose**: Orchestrates BMAD workflow phases following proper sequence and phase gates
