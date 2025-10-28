# Skill Details

## bmad-orchestrator

**Purpose**: Central workflow management

**Responsibilities**:
- Initialize workflow (`workflow-init`)
- Check status (`workflow-status`)
- Manage phase transitions
- Initialize sprint status from epics
- Track story lifecycle
- Recommend next actions

**Python Helpers**:
- `workflow_status.py` - Manages workflow-status.md
- `sprint_status.py` - Manages sprint-status.yaml

**Conversational Triggers**:
- "Start a new project"
- "What's next?"
- "Where am I in the workflow?"
- "Initialize BMAD workflow"

## bmad-analyst (Phase 1)

**Purpose**: Analysis phase workflows

**Workflows**:
- Brainstorm Project - Structured ideation
- Product Brief - Strategic brief
- Research - Market/competitive/technical
- Document Project - Reverse-engineer codebase

**Agent Persona**: Mary (Strategic Business Analyst)

**Outputs**: Brainstorm notes, product briefs, research docs

**Conversational Triggers**:
- "I have an idea..."
- "Help me think through..."
- "What if we..."

## bmad-pm (Phase 2)

**Purpose**: Planning phase - PRD and epics

**Workflows**:
- PRD Creation - Gather requirements, structure PRD
- Epic Breakdown - Organize stories into epics

**Agent Persona**: John (Investigative Product Strategist)

**Outputs**: `docs/PRD.md`, `docs/epics.md`

**Scale-Adaptive**:
- Level 2: 8-15 FRs, 1-2 epics
- Level 3: 12-25 FRs, 2-5 epics
- Level 4: 20-35+ FRs, 5-10+ epics

**Conversational Triggers**:
- "I want to build..."
- "Create a PRD"
- "Plan this feature"

## bmad-ux (Phase 2)

**Purpose**: UX design specifications

**Workflows**:
- Create UX Design - Design thinking workshop
- Validate UX Design - Quality check

**Agent Persona**: Sally (User Experience Designer)

**Outputs**: `docs/ux-spec.md`

**When**: UI-heavy projects, Level 2-4

**Conversational Triggers**:
- "What should the UI look like?"
- "Design the UX"
- "Help me with user experience"

## bmad-architecture (Phase 3)

**Purpose**: Technical architecture and decisions

**Workflows**:
- Architecture Design - Tech stack, patterns, structure
- Discover Starter Templates - Find and evaluate starters
- Novel Pattern Design - Design unique patterns
- Define Implementation Patterns - Consistency rules

**Agent Persona**: Winston (System Architect)

**Outputs**: `docs/ARCHITECTURE.md`

**Critical**: Verifies versions via WebSearch, defines consistency patterns to prevent agent conflicts

**Conversational Triggers**:
- "How should we build this?"
- "What's the architecture?"
- "What tech stack should we use?"

## bmad-tea (Cross-Phase)

**Purpose**: Comprehensive testing strategy

**Workflows**:
- Framework - Initialize test infrastructure
- Test Design - Create test scenarios
- ATDD - Tests-first development
- Automate - Generate test automation
- Trace - Requirements traceability
- NFR Assessment - Validate non-functional requirements
- CI/CD - Quality pipeline setup
- Test Review - Review test quality

**Agent Persona**: Murat (Master Test Architect)

**Outputs**: Test framework, test scenarios, CI/CD configs

**Philosophy**: Risk-based testing, prioritize unit/integration over E2E, flakiness is critical debt

**Conversational Triggers**:
- "How should we test this?"
- "Create test strategy"
- "Set up ATDD"

## bmad-stories (Phase 4)

**Purpose**: Create developer-ready stories

**Workflows**:
- Create Story - Generate story file from epics
- Check Previous Story - Extract learnings for continuity

**Agent Persona**: Bob (Technical Scrum Master)

**Outputs**: `stories/{epic}-{story}-{title}.md`

**Critical Features**:
- Checks previous story for context
- Includes "Learnings from Previous Story" section
- Cites architecture patterns
- Maps tasks to acceptance criteria
- Non-interactive by default (generates from docs)

**Conversational Triggers**:
- "Break into stories"
- "Create user stories"
- "Prepare dev stories"

## bmad-dev (Phase 4)

**Purpose**: Story implementation

**Workflows**:
- Develop Story - Full implementation cycle
- Code Review - Fresh-eyes review
- Story Done - Final completion

**Agent Persona**: Amelia (Senior Implementation Engineer)

**Critical Rules**:
- Never start without story file
- Follow architecture patterns EXACTLY
- Reuse existing services (don't recreate)
- Write AND run tests (no cheating)
- Update Dev Agent Record continuously
- Only mark complete when all ACs met, all tests passing 100%

**Continuous Execution**: Runs without pausing until story complete or blocked

**Conversational Triggers**:
- "Implement story X"
- "Develop this feature"
- "Let's code"
- "Start coding"
