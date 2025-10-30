# Architecture Overview

## 7 Agent Skills

| Skill | Phase | Purpose | Agent Persona |
|-------|-------|---------|---------------|
| **bmad-workflow-router** | All | Workflow orchestration, state management | Workflow Manager |
| **bmad-discovery-research** | Phase 1 | Brainstorm, product briefs, research | Strategic Business Analyst (Mary) |
| **bmad-product-planning** | Phase 2 | PRD, epics breakdown | Investigative Product Strategist (John) |
| **bmad-ux-design** | Phase 2 | UX design specifications | User Experience Designer (Sally) |
| **bmad-architecture-design** | Phase 3 | Technical architecture, decisions | System Architect (Winston) |
| **bmad-test-strategy** | Cross-phase | Test strategy, ATDD, automation | Master Test Architect (Murat) |
| **bmad-story-planning** | Phase 4 | Story creation from epics | Technical Scrum Master (Bob) |
| **bmad-development-execution** | Phase 4 | Implementation, testing, review | Senior Implementation Engineer (Amelia) |

## State Management Files

- **`docs/workflow-status.md`** - Tracks current phase, progress, next actions
- **`docs/sprint-status.yaml`** - Tracks all stories with statuses (backlog → drafted → in-progress → review → done)

## Generated Artifacts

```
docs/
├── workflow-status.md           # Workflow state (managed by orchestrator)
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

## Repository Structure

```
.claude/
  skills/
    bmad-workflow-router/
      SKILL.md                      # Orchestrator with state management
      scripts/
        workflow_status.py          # Manages workflow-status.md
        sprint_status.py            # Manages sprint-status.yaml

    bmad-discovery-research/                   # Phase 1: Analysis
      SKILL.md                      # Brainstorm, product brief, research
      assets/
        brainstorm-template.md.jinja
        product-brief-template.md.jinja
        research-dossier-template.md.jinja

    bmad-product-planning/                        # Phase 2: Planning
      SKILL.md
      generate_prd.py
      prd_template.md.jinja
      epics_template.md.jinja

    bmad-ux-design/                        # Phase 2: UX Design
      SKILL.md                      # UX specifications

    bmad-architecture-design/              # Phase 3: Solutioning
      SKILL.md
      generate_architecture.py
      architecture_template.md.jinja

    bmad-test-strategy/                       # Cross-phase: Testing
      SKILL.md                      # Test strategy, ATDD, automation

    bmad-story-planning/                   # Phase 4: Story Creation
      SKILL.md
      create_story.py
      story_template.md.jinja

    bmad-development-execution/                       # Phase 4: Implementation
      SKILL.md                      # Coding, testing, review

docs/                               # Generated artifacts
stories/                            # Generated story files
```

## Conversational Triggers

Each skill has natural language triggers that Claude detects automatically:

| What You Say | Skill Invoked | What Happens |
|--------------|---------------|--------------|
| "I have an idea...", "What if we...", "Help me think through..." | `bmad-discovery-research` | Brainstorming and product brief creation |
| "I want to build...", "Create a PRD", "Plan this feature" | `bmad-product-planning` | PRD and epics generation |
| "What should the UI look like?", "Design the UX" | `bmad-ux-design` | UX specification and design thinking |
| "How should we build this?", "What's the architecture?" | `bmad-architecture-design` | Technical architecture and stack decisions |
| "How should we test?", "Create test strategy" | `bmad-test-strategy` | Test framework and ATDD implementation |
| "Break into stories", "Create user stories" | `bmad-story-planning` | Developer-ready story file creation |
| "Implement story X", "Develop this feature", "Let's code" | `bmad-development-execution` | Code implementation with tests |
| "What's next?", "Where am I?", "Start new project" | `bmad-workflow-router` | Workflow status and guidance |

**Claude analyzes your message intent and context**, then invokes the appropriate skill automatically.
