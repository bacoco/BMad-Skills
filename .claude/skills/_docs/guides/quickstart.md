# Quick Start

## Prerequisites

1. **Claude Code** or **Claude CLI**
2. **Python 3.7+**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Git** (optional, for version control)

## Just Talk to Claude Naturally

**You**: "I want to start a new project for a mobile expense tracker"

**Claude**: Detects new project → Invokes `main-workflow-router`
- Assesses project level (0-4)
- Creates `docs/workflow-status.md`
- Recommends next phase

## Follow the Natural Flow

### Phase 1: Analysis (Optional for L0-2, Recommended for L3-4)

**You**: "Help me think through this idea..."

**Claude**: Detects brainstorming need → Invokes `bmad-discovery-research`
- Creates `docs/product-brief.md`
- Guides through discovery questions

### Phase 2: Planning (Required for L2-4)

**You**: "I want to build an API with user auth and expense tracking"

**Claude**: Detects feature planning → Invokes `bmad-product-planning`
- Creates `docs/PRD.md` and `docs/epics.md`
- Breaks down functional requirements

**Optional: UX Design**

**You**: "What should the user interface look like?"

**Claude**: Detects UX design need → Invokes `bmad-ux-design`
- Creates `docs/ux-spec.md`
- Runs design thinking workshop

### Phase 3: Solutioning (Required for L2-4)

**You**: "How should we architect this?"

**Claude**: Detects architecture planning → Invokes `bmad-architecture-design`
- Creates `docs/ARCHITECTURE.md`
- Defines tech stack and patterns

**Optional: Test Strategy**

**You**: "How should we test this system?"

**Claude**: Detects testing strategy need → Invokes `bmad-test-strategy`
- Creates test framework
- Defines ATDD approach

### Phase 4: Implementation (Iterative)

**You**: "Break this into user stories"

**Claude**: Detects story creation need → Invokes `bmad-story-planning`
- Creates `docs/sprint-status.yaml` from epics
- Generates story files in `stories/`
- Marks stories with Previous Learnings pattern

**You**: "Implement story 1-1-user-login"

**Claude**: Detects implementation request → Invokes `bmad-development-execution`
- Loads story and architecture
- Writes code following acceptance criteria
- Runs tests (100% coverage required)
- Updates Dev Agent Record in story file

## Check Status Anytime

**You**: "What's next?" or "Where am I in the workflow?"

**Claude**: Invokes `main-workflow-router`
- Shows current phase and progress
- Lists completed artifacts
- Recommends next action
- Displays story statuses (if in Implementation)

## Project Levels

| Level | Scope | FRs | Epics | Stories | Workflow Path |
|-------|-------|-----|-------|---------|---------------|
| 0 | Bug fix, config change | N/A | N/A | N/A | Skip BMAD entirely |
| 1 | Small isolated feature | 1-5 | 0-1 | 1-5 | Tech-spec only (lightweight) |
| 2 | New feature (MVP) | 8-15 | 1-2 | 5-15 | Planning → Solutioning → Implementation |
| 3 | Comprehensive product | 12-25 | 2-5 | 15-40 | (Analysis) → Planning → Solutioning → Implementation |
| 4 | Enterprise platform | 20-35+ | 5-10+ | 40-100+ | Analysis → Planning → Solutioning → Implementation |
