# BMAD-Style Workflow Skills for Claude

**Version**: 2.1.0 - Proactive Skills
**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha

---

## 🎉 Complete BMAD Implementation with Proactive Invocation

This repository is a **complete, faithful implementation** of BMAD Method v6-alpha as Claude Code Skills. All 7 agents, all workflows, full state management - **with automatic, proactive skill invocation**.

**What's Included:**
- ✅ **All 7 BMAD Agents** as Skills
- ✅ **Proactive Auto-Invocation** - Claude detects context and invokes skills automatically
- ✅ **Complete Workflow Orchestration** with state management
- ✅ **Python Helpers** for workflow-status and sprint-status
- ✅ **All 4 Phases** (Analysis, Planning, Solutioning, Implementation)
- ✅ **Story Lifecycle Management**
- ✅ **BMAD Agent Personas** preserved exactly from v6-alpha

## 🚀 How It Works

**You don't need to manually invoke skills!** Claude automatically detects what you need based on your conversation and proactively invokes the right skill.

### Example Conversations

```
User: "I have an idea for a collaborative todo app"

Claude: I detect you're starting a new project with a vague idea.
Let me invoke bmad-analyst to help you explore this...

[Analyst skill activates - helps brainstorm and create product brief]
```

```
User: "I want to build a REST API for user authentication"

Claude: You're describing a Level 2-3 project. Let me invoke
bmad-pm to help create a Product Requirements Document...

[PM skill activates - creates PRD and epics]
```

```
User: "How should we architect this microservices system?"

Claude: I detect you need architectural planning. Let me invoke
bmad-architecture to define your technical solution...

[Architecture skill activates - creates ARCHITECTURE.md]
```

**No slash commands needed.** Just talk naturally about what you want to build, and Claude will guide you through the right BMAD workflow.

### 🎯 Conversational Triggers

Each skill has natural language triggers that Claude detects automatically:

| What You Say | Skill Invoked | What Happens |
|--------------|---------------|--------------|
| "I have an idea...", "What if we...", "Help me think through..." | `bmad-analyst` | Brainstorming and product brief creation |
| "I want to build...", "Create a PRD", "Plan this feature" | `bmad-pm` | PRD and epics generation |
| "What should the UI look like?", "Design the UX" | `bmad-ux` | UX specification and design thinking |
| "How should we build this?", "What's the architecture?" | `bmad-architecture` | Technical architecture and stack decisions |
| "How should we test?", "Create test strategy" | `bmad-tea` | Test framework and ATDD implementation |
| "Break into stories", "Create user stories" | `bmad-stories` | Developer-ready story file creation |
| "Implement story X", "Develop this feature", "Let's code" | `bmad-dev` | Code implementation with tests |
| "What's next?", "Where am I?", "Start new project" | `bmad-orchestrator` | Workflow status and guidance |

**Claude analyzes your message intent and context**, then invokes the appropriate skill automatically. You just have natural conversations.

---

## 🏗️ Architecture Overview

### 7 Agent Skills

| Skill | Phase | Purpose | Agent Persona |
|-------|-------|---------|---------------|
| **bmad-orchestrator** | All | Workflow orchestration, state management | Workflow Manager |
| **bmad-analyst** | Phase 1 | Brainstorm, product briefs, research | Strategic Business Analyst (Mary) |
| **bmad-pm** | Phase 2 | PRD, epics breakdown | Investigative Product Strategist (John) |
| **bmad-ux** | Phase 2 | UX design specifications | User Experience Designer (Sally) |
| **bmad-architecture** | Phase 3 | Technical architecture, decisions | System Architect (Winston) |
| **bmad-tea** | Cross-phase | Test strategy, ATDD, automation | Master Test Architect (Murat) |
| **bmad-stories** | Phase 4 | Story creation from epics | Technical Scrum Master (Bob) |
| **bmad-dev** | Phase 4 | Implementation, testing, review | Senior Implementation Engineer (Amelia) |

### State Management Files

- **`docs/bmm-workflow-status.md`** - Tracks current phase, progress, next actions
- **`docs/sprint-status.yaml`** - Tracks all stories with statuses (backlog → drafted → in-progress → review → done)

### Generated Artifacts

```
docs/
├── bmm-workflow-status.md        # Workflow state (managed by orchestrator)
├── sprint-status.yaml            # Story tracking (managed by orchestrator)
├── brainstorm-notes.md           # Analysis output (optional)
├── product-brief.md              # Analysis output (optional)
├── research-*.md                 # Research findings (optional)
├── PRD.md                        # Product Requirements (required L2-4)
├── epics.md                      # Epic breakdown (required L2-4)
├── ux-spec.md                    # UX specification (optional)
├── ARCHITECTURE.md               # Technical architecture (required L2-4)
├── testing-strategy.md           # Test strategy (optional)
└── test-scenarios.md             # Test scenarios (optional)

stories/
└── {epic}-{story}-{title}.md     # Individual stories
```

---

## 📦 Repository Structure

```
.claude/
  skills/
    bmad-orchestrator/
      SKILL.md                      # Orchestrator with state management
      helpers/
        workflow_status.py          # Manages workflow-status.md
        sprint_status.py            # Manages sprint-status.yaml

    bmad-analyst/                   # Phase 1: Analysis
      SKILL.md                      # Brainstorm, product brief, research

    bmad-pm/                        # Phase 2: Planning
      SKILL.md
      generate_prd.py
      prd_template.md.jinja
      epics_template.md.jinja

    bmad-ux/                        # Phase 2: UX Design
      SKILL.md                      # UX specifications

    bmad-architecture/              # Phase 3: Solutioning
      SKILL.md
      generate_architecture.py
      architecture_template.md.jinja

    bmad-tea/                       # Cross-phase: Testing
      SKILL.md                      # Test strategy, ATDD, automation

    bmad-stories/                   # Phase 4: Story Creation
      SKILL.md
      create_story.py
      story_template.md.jinja

    bmad-dev/                       # Phase 4: Implementation
      SKILL.md                      # Coding, testing, review

docs/                               # Generated artifacts
stories/                            # Generated story files
```

---

## 🚀 Quick Start

### Just Talk to Claude Naturally

**You**: "I want to start a new project for a mobile expense tracker"

**Claude**: Detects new project → Invokes `bmad-orchestrator`
- Assesses project level (0-4)
- Creates `docs/bmm-workflow-status.md`
- Recommends next phase

### Follow the Natural Flow

**Phase 1: Analysis** (Optional for L0-2, Recommended for L3-4)

**You**: "Help me think through this idea..."

**Claude**: Detects brainstorming need → Invokes `bmad-analyst`
- Creates `docs/product-brief.md`
- Guides through discovery questions

**Phase 2: Planning** (Required for L2-4)

**You**: "I want to build an API with user auth and expense tracking"

**Claude**: Detects feature planning → Invokes `bmad-pm`
- Creates `docs/PRD.md` and `docs/epics.md`
- Breaks down functional requirements

Optional: UX Design

**You**: "What should the user interface look like?"

**Claude**: Detects UX design need → Invokes `bmad-ux`
- Creates `docs/ux-spec.md`
- Runs design thinking workshop

**Phase 3: Solutioning** (Required for L2-4)

**You**: "How should we architect this?"

**Claude**: Detects architecture planning → Invokes `bmad-architecture`
- Creates `docs/ARCHITECTURE.md`
- Defines tech stack and patterns

Optional: Test Strategy

**You**: "How should we test this system?"

**Claude**: Detects testing strategy need → Invokes `bmad-tea`
- Creates test framework
- Defines ATDD approach

**Phase 4: Implementation** (Iterative)

**You**: "Break this into user stories"

**Claude**: Detects story creation need → Invokes `bmad-stories`
- Creates `docs/sprint-status.yaml` from epics
- Generates story files in `stories/`
- Marks stories with Previous Learnings pattern

**You**: "Implement story 1-1-user-login"

**Claude**: Detects implementation request → Invokes `bmad-dev`
- Loads story and architecture
- Writes code following acceptance criteria
- Runs tests (100% coverage required)
- Updates Dev Agent Record in story file

### Check Status Anytime

**You**: "What's next?" or "Where am I in the workflow?"

**Claude**: Invokes `bmad-orchestrator`
- Shows current phase and progress
- Lists completed artifacts
- Recommends next action
- Displays story statuses (if in Implementation)

---

## 📚 Complete Documentation

### Prerequisites

1. **Claude Code** or **Claude CLI**
2. **Python 3.7+**:
   ```bash
   pip install jinja2 pyyaml
   ```
3. **Git** (optional, for version control)

### Project Levels

| Level | Scope | FRs | Epics | Stories | Workflow Path |
|-------|-------|-----|-------|---------|---------------|
| 0 | Bug fix, config change | N/A | N/A | N/A | Skip BMAD entirely |
| 1 | Small isolated feature | 1-5 | 0-1 | 1-5 | Tech-spec only (lightweight) |
| 2 | New feature (MVP) | 8-15 | 1-2 | 5-15 | Planning → Solutioning → Implementation |
| 3 | Comprehensive product | 12-25 | 2-5 | 15-40 | (Analysis) → Planning → Solutioning → Implementation |
| 4 | Enterprise platform | 20-35+ | 5-10+ | 40-100+ | Analysis → Planning → Solutioning → Implementation |

### Phase Flows

#### Phase 1: Analysis (bmad-analyst)

**When**: Level 3-4, complex/novel problems

**Workflows**:
- **Brainstorm**: Structured ideation, problem framing
- **Product Brief**: Strategic brief before detailed PRD
- **Research**: Market/competitive/technical research
- **Document Project**: Reverse-engineer existing codebase

**Outputs**:
- `docs/brainstorm-notes.md`
- `docs/product-brief.md`
- `docs/research-{topic}.md`
- `docs/project-documentation.md`

**Next Phase**: Planning (bmad-pm)

#### Phase 2: Planning (bmad-pm + bmad-ux)

**When**: Level 2-4, always required

**Workflows**:
- **PRD Creation**: Product requirements document
- **Epic Breakdown**: Stories organized into epics
- **UX Design**: User experience specification (optional)

**Outputs**:
- `docs/PRD.md` - Strategic requirements
- `docs/epics.md` - Tactical story breakdown
- `docs/ux-spec.md` - UX specification (optional)

**Next Phase**: Solutioning (bmad-architecture)

#### Phase 3: Solutioning (bmad-architecture + bmad-tea)

**When**: Level 2-4, always required

**Workflows**:
- **Architecture**: Technical design, tech stack, patterns
- **Test Strategy**: Test framework setup (optional)

**Outputs**:
- `docs/ARCHITECTURE.md` - Decision architecture
- `docs/testing-strategy.md` - Test strategy (optional)
- Test framework files (optional)

**Next Phase**: Implementation (story creation)

#### Phase 4: Implementation (bmad-stories + bmad-dev + bmad-tea)

**When**: After Solutioning complete

**Workflows**:

1. **Sprint Planning** (Orchestrator)
   - Initializes `docs/sprint-status.yaml` from epics
   - All stories start in "backlog" status

2. **Story Creation** (bmad-stories)
   - Creates developer-ready story files
   - Each story: `stories/{epic}-{story}-{title}.md`
   - Includes: AC, tasks, dev notes, learnings from previous story

3. **ATDD** (bmad-tea, optional)
   - Write tests BEFORE implementation
   - Tests define expected behavior

4. **Implementation** (bmad-dev)
   - Implement story following architecture
   - Write/run tests
   - Update Dev Agent Record
   - Mark story status: drafted → in-progress → review → done

5. **Code Review** (bmad-dev)
   - Fresh-eyes review of completed story
   - Document findings and action items

**Outputs**:
- `docs/sprint-status.yaml` - Story tracking
- `stories/*.md` - Story files
- Source code files
- Test files

---

## 🎯 Skill Details

### bmad-orchestrator

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

**User Commands**:
- "Initialize BMAD workflow"
- "What's my status?"
- "What's next?"
- "What's the next story?"
- "List backlog stories"
- "Mark Planning complete"

### bmad-analyst (Phase 1)

**Purpose**: Analysis phase workflows

**Workflows**:
- Brainstorm Project - Structured ideation
- Product Brief - Strategic brief
- Research - Market/competitive/technical
- Document Project - Reverse-engineer codebase

**Agent Persona**: Mary (Strategic Business Analyst)

**Outputs**: Brainstorm notes, product briefs, research docs

### bmad-pm (Phase 2)

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

### bmad-ux (Phase 2)

**Purpose**: UX design specifications

**Workflows**:
- Create UX Design - Design thinking workshop
- Validate UX Design - Quality check

**Agent Persona**: Sally (User Experience Designer)

**Outputs**: `docs/ux-spec.md`

**When**: UI-heavy projects, Level 2-4

### bmad-architecture (Phase 3)

**Purpose**: Technical architecture and decisions

**Workflows**:
- Architecture Design - Tech stack, patterns, structure
- Discover Starter Templates - Find and evaluate starters
- Novel Pattern Design - Design unique patterns
- Define Implementation Patterns - Consistency rules

**Agent Persona**: Winston (System Architect)

**Outputs**: `docs/ARCHITECTURE.md`

**Critical**: Verifies versions via WebSearch, defines consistency patterns to prevent agent conflicts

### bmad-tea (Cross-Phase)

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

### bmad-stories (Phase 4)

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

### bmad-dev (Phase 4)

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

---

## 🔄 Complete Workflow Example

### Scenario: E-commerce Product Catalog (Level 3)

**1. Initialize**
```
User: "Initialize BMAD workflow for E-commerce Product Catalog"

Orchestrator:
- Asks questions (what, how complex, timeline)
- Determines: Level 3, Greenfield
- Creates workflow-status.md
- Recommends: "Start with Planning (bmad-pm)"
```

**2. Planning**
```
User: "Create PRD and epics"

bmad-pm:
- Asks clarifying questions
- Gathers: Goals, FRs, NFRs, User Journeys
- Generates PRD: 15 FRs, 3 Epics
- Generates Epics:
  - Epic 1: Foundation & Auth (5 stories)
  - Epic 2: Product Management (8 stories)
  - Epic 3: Shopping Cart (7 stories)
- Total: 20 stories
- Saves: docs/PRD.md, docs/epics.md

Orchestrator:
- Marks Planning complete
- Updates phase to Solutioning
- Recommends: "Create Architecture (bmad-architecture)"
```

**3. Solutioning**
```
User: "Create architecture"

bmad-architecture:
- Reads PRD completely
- Searches for Next.js starter (WebSearch)
- Makes decisions:
  - Stack: Next.js 15, TypeScript, Prisma, tRPC
  - Structure: /app router, /lib utilities
  - Patterns: Server actions, optimistic updates
  - Error handling: Structured responses
  - Testing: Vitest + Playwright
- Generates: docs/ARCHITECTURE.md

Orchestrator:
- Marks Solutioning complete
- Initializes sprint-status.yaml from epics.md
- 20 stories loaded, all "backlog"
- Updates phase to Implementation
- Recommends: "Create first story (bmad-stories)"
```

**4. Story Creation**
```
User: "Create next story"

Orchestrator: Next backlog story is "1-1-project-setup"

bmad-stories:
- Loads PRD, Architecture, Epics
- No previous story (first in epic)
- Extracts Story 1.1 from epics
- Creates tasks from ACs
- Writes dev notes with architecture patterns
- Generates: stories/1-1-project-setup.md

Orchestrator:
- Updates sprint-status: 1-1-project-setup → "drafted"
- Recommends: "Implement story 1-1-project-setup (bmad-dev)"
```

**5. Implementation (Story 1.1)**
```
User: "Implement story 1-1-project-setup"

bmad-dev:
- Loads story file completely
- Loads architecture patterns
- No previous story
- Implements:
  - Runs Next.js create command
  - Configures TypeScript
  - Sets up Prisma
  - Initializes tests
  - Configures ESLint/Prettier
- Writes tests
- Runs tests → All passing
- Updates Dev Agent Record:
  - Files created: package.json, tsconfig.json, prisma/schema.prisma, etc.
  - Patterns established: Server actions pattern
  - Technical debt: None
  - Warnings for next: "Database URL must be configured"
- Marks story "in-progress" → "done"

Orchestrator:
- Updates sprint-status: 1-1-project-setup → "done"
- Recommends: "Create next story 1-2-user-authentication (bmad-stories)"
```

**6. Story Creation (Story 1.2)**
```
User: "Create next story"

bmad-stories:
- Loads Story 1.1 file completely
- Extracts Previous Story Learnings:
  - Server actions pattern established
  - Prisma schema exists
  - Warning: DB URL needed
- Creates Story 1.2 with:
  - Learnings section referencing 1.1
  - Tasks use existing patterns
  - Notes about DB configuration
- Generates: stories/1-2-user-authentication.md

Orchestrator:
- Updates sprint-status: 1-2-user-authentication → "drafted"
```

**7. Continue...**

Repeat steps 5-6 for all 20 stories across 3 epics.

**8. Done!**
```
Orchestrator: "All stories complete! 🎉 Project done."
```

---

## 📊 State Management

### workflow-status.md Structure

```markdown
# BMM Workflow Status

**Project**: E-commerce Product Catalog
**Type**: Greenfield
**Level**: 3
**Created**: 2025-10-28
**Owner**: User

## Current Status

**Phase**: Implementation
**Status**: In Progress
**Last Updated**: 2025-10-28

## Phase Progress

### Phase 1: Analysis
Status: Skipped (Optional for Level 3)

### Phase 2: Planning
- [x] PRD
- [x] Epics Breakdown
Status: Complete

### Phase 3: Solutioning
- [x] Architecture
Status: Complete

### Phase 4: Implementation
- [x] Story Creation (ongoing)
- [ ] Story Implementation (in progress)
Status: In Progress

## Next Recommended Action

Create next story with bmad-stories skill

## Artifacts Created

- docs/PRD.md - Product Requirements Document (2025-10-28)
- docs/epics.md - Epic Breakdown (2025-10-28)
- docs/ARCHITECTURE.md - Technical Architecture (2025-10-28)
- docs/sprint-status.yaml - Sprint Tracking (2025-10-28)
- stories/1-1-project-setup.md - Story 1.1 (2025-10-28)
```

### sprint-status.yaml Structure

```yaml
project_metadata:
  created: '2025-10-28'
  last_updated: '2025-10-28'
  total_epics: 3
  total_stories: 20

epic_status:
  epic-1:
    title: Foundation & Auth
    total_stories: 5
    completed: 1
    in_progress: 1
    status: in-progress

development_status:
  1-1-project-setup:
    title: Project Setup
    status: done
    assigned_to: Claude
    started: '2025-10-28'
    completed: '2025-10-28'

  1-2-user-authentication:
    title: User Authentication
    status: drafted
    assigned_to: null
    started: null
    completed: null

  # ... (18 more stories)
```

---

## 🛠️ Python Helpers

### workflow_status.py

```bash
# Initialize workflow
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py init \
  "Project Name" "greenfield" 3 "User"

# Update phase
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py update-phase "Planning"

# Mark phase complete
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py mark-complete "Planning"

# Add artifact
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py add-artifact \
  "docs/PRD.md" "Product Requirements Document"

# Get current phase
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py get-phase
```

### sprint_status.py

```bash
# Initialize from epics
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py init docs/epics.md

# Update story status
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "1-1-project-setup" "in-progress" "Claude"

# Get next backlog story
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py next-backlog

# List stories by status
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py list-status "backlog"
```

---

## 🎓 Best Practices

### 1. Always Start with Orchestrator

```
User: "Initialize BMAD workflow"
```

Don't skip initialization - it sets up state management.

### 2. Check Status Frequently

```
User: "What's my BMAD status?"
```

Orchestrator reads state files and recommends next action.

### 3. Complete Phases in Order

- Phase 1: Analysis (optional)
- Phase 2: Planning (required L2-4)
- Phase 3: Solutioning (required L2-4)
- Phase 4: Implementation (iterative)

### 4. Let Orchestrator Manage State

Don't manually edit workflow-status.md or sprint-status.yaml. Let orchestrator and skills update them.

### 5. Story Learnings are Critical

bmad-stories ALWAYS checks previous story. This prevents:
- Recreating existing code
- Ignoring technical debt
- Missing architectural decisions

### 6. Dev Agent Record is Mandatory

bmad-dev MUST update Dev Agent Record as implementation progresses. Next story depends on it.

### 7. Tests are Not Optional

bmad-dev will NOT mark story complete unless:
- All tests written
- All tests passing 100%
- No cheating

---

## 🐛 Troubleshooting

### "Workflow status file not found"

**Problem**: No workflow-status.md exists

**Solution**: Run workflow initialization:
```
Initialize BMAD workflow
```

### "Sprint status file not found"

**Problem**: No sprint-status.yaml exists

**Solution**: Orchestrator should initialize after epics created. Or manually:
```
Initialize sprint status
```

### "Story has no previous learnings"

**Problem**: Story doesn't reference previous story

**Solution**: bmad-stories should automatically check. If missing, manually read previous story and include learnings.

### "Tests not running"

**Problem**: bmad-dev not executing tests

**Solution**: Ensure test framework initialized (bmad-tea). Verify tests exist. Dev agent MUST run tests, no exceptions.

---

## 📈 Implementation Stats

**Version 2.0.0 Complete Implementation**:
- ✅ 7 Agent Skills implemented
- ✅ 2,919 lines of Skill documentation
- ✅ 2 Python state management helpers
- ✅ Workflow-status.md management
- ✅ Sprint-status.yaml management
- ✅ All BMAD phases covered
- ✅ Story lifecycle management
- ✅ BMAD agent personas preserved
- ✅ 100% faithful to BMAD v6-alpha

**Files Created**:
- 7 SKILL.md files
- 2 Python helpers
- 3 Python generators (PRD, Architecture, Story)
- 3 Jinja templates
- 1 comprehensive README

---

## 🙏 Attribution & License

**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org

This implementation preserves BMAD v6-alpha agent personas, workflows, and output formats. It is a faithful vendoring of BMAD logic into Claude Code Skills, not a loose recreation.

**Agent Personas** (preserved from BMAD v6-alpha):
- Mary (Analyst) - Strategic Business Analyst
- John (PM) - Investigative Product Strategist
- Sally (UX Designer) - User Experience Designer
- Winston (Architect) - System Architect
- Murat (TEA) - Master Test Architect
- Bob (Scrum Master) - Technical Scrum Master
- Amelia (DEV) - Senior Implementation Engineer

**Important**: This is for internal/educational use. Do not redistribute without proper licensing from bmad-code-org.

---

## 🎯 What's New in v2.0.0

**Complete BMAD Implementation**:
- ✅ Added bmad-analyst (Analysis phase)
- ✅ Added bmad-ux (UX Design)
- ✅ Added bmad-tea (Test Architecture)
- ✅ Added bmad-dev (Implementation)
- ✅ Refactored orchestrator with full state management
- ✅ Added workflow-status.md management
- ✅ Added sprint-status.yaml management
- ✅ Added story lifecycle tracking
- ✅ Added Python helpers for state management
- ✅ All 4 phases now complete
- ✅ All BMAD workflows covered

**v1.0.0** (Initial release):
- 3 Skills: PM, Architecture, Stories
- Basic orchestrator
- No state management

**v2.0.0** (Current - Complete):
- 7 Skills: All agents
- Full orchestrator with state management
- Complete workflow coverage

---

## 📞 Support

**Issues**: GitHub issues with:
- Which skill/phase failed
- Expected vs actual behavior
- State file contents (workflow-status.md, sprint-status.yaml)

**Documentation**:
- BMAD Method v6-alpha: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
- Each SKILL.md contains detailed instructions

---

## 🚀 Happy Building with Complete BMAD!

You now have the full power of BMAD Method v6-alpha in Claude Code.

From idea → product brief → PRD → architecture → stories → implementation.

All 7 agents. All 4 phases. Full state management.

**Start here**:
```
Initialize BMAD workflow for [your project]
```

Let BMAD guide you from 0 to production. 🎉
