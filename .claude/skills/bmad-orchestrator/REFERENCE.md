# Reference — End-to-End Orchestration

Routing matrices, troubleshooting guides, and status file schemas are documented here. Load only when orchestration decisions require deeper context.

# BMAD Orchestrator Skill

**Source**: BMAD Method v6-alpha + OpenSpec by Fission-AI
**References**:
- BMAD: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
- OpenSpec: https://github.com/Fission-AI/OpenSpec
**Purpose**: Intelligent workflow orchestration - routes to BMAD or OpenSpec based on complexity
**State Files**: `docs/bmm-workflow-status.md` (BMAD), `docs/sprint-status.yaml` (BMAD), `openspec/changes/` (OpenSpec)

## 🎯 When Claude Should Invoke This Skill

**PROACTIVELY invoke this skill** when you detect the user:
- Starts a conversation about a new project or feature
- Says "I want to start a new project", "let's build something"
- Asks "what's next?", "where am I in the workflow?", "what should I do now?"
- Seems unsure about which BMAD phase they're in
- Wants to initialize or check workflow status
- Mentions BMAD methodology or workflow
- Just completed a major phase (PRD, Architecture, Stories) and asks what's next
- Wants guidance on the overall development process

**DO NOT invoke for**:
- User clearly knows which skill they need (let them proceed)
- Mid-task implementation (user is actively coding)
- Specific technical questions unrelated to workflow

## Two Workflows Available: BMAD vs OpenSpec

You orchestrate **TWO different workflows** based on project complexity:

### 🚀 OpenSpec Workflow (Level 0-1: Simple Changes)

**When**: Bug fixes, small features, simple modifications to existing projects

**3 Skills Available**:
1. **openspec-propose** - Create lightweight change proposals
2. **openspec-implement** - Implement approved changes
3. **openspec-archive** - Archive deployed changes

**3 Stages**:
- **Stage 1**: Creating Changes (proposal, tasks, delta specs)
- **Stage 2**: Implementing Changes (execute tasks)
- **Stage 3**: Archiving Changes (update living specs)

**Speed**: Hours to days
**Overhead**: Minimal (proposal + tasks)
**Best for**: Existing projects, incremental changes

### 🏗️ BMAD Workflow (Level 2-4: Complex Projects)

**When**: New products, MVPs, comprehensive features, platforms

**7 Agent Skills Available**:
1. **bmad-analyst** - Phase 1: Analysis (brainstorm, product brief, research)
2. **bmad-pm** - Phase 2: Planning (PRD, epics)
3. **bmad-ux** - Phase 2: Planning (UX design for UI-heavy projects)
4. **bmad-architecture** - Phase 3: Solutioning (architecture, tech decisions)
5. **bmad-tea** - Cross-phase: Testing (test strategy, ATDD, automation)
6. **bmad-stories** - Phase 4: Story Creation (developer-ready stories)
7. **bmad-dev** - Phase 4: Implementation (coding, testing, review)

**4 Phases**:
- **Phase 1: Analysis** (Optional for L2, Recommended for L3-4)
- **Phase 2: Planning** (Required for L2-4)
- **Phase 3: Solutioning** (Required for L2-4)
- **Phase 4: Implementation** (Iterative)

**Speed**: Days to weeks
**Overhead**: High (PRD, Architecture, Stories)
**Best for**: New products, greenfield projects

## Your Core Responsibilities

1. **Initialize Workflow** (`workflow-init`)
   - Assess project level (0-4)
   - Create workflow-status.md
   - Recommend workflow path

2. **Track Status** (`workflow-status`)
   - Read workflow-status.md
   - Report current phase
   - Recommend next action

3. **Manage Phase Transitions**
   - Validate phase gates
   - Update workflow-status.md
   - Mark phases complete

4. **Manage Sprint Status**
   - Initialize sprint-status.yaml from epics
   - Track story progress
   - Report story statuses

5. **Guide User**
   - Answer "what's next?"
   - Load appropriate skills
   - Ensure proper sequence

## Workflow: Initialize (`workflow-init`)

**When**: Start of new project, no workflow-status.md exists

**Process**:

### Step 1: Assess Project

Ask user:
1. **What are you building?**
   - Get brief description

2. **Project Type?**
   - Greenfield (new project)
   - Brownfield (existing codebase)

3. **Complexity Assessment**:
   - How many functional requirements? (rough estimate)
   - How many epics? (rough estimate)
   - Timeline/team size?

### Step 2: Determine Project Level

| Level | Scope | FRs | Epics | Stories | Workflow |
|-------|-------|-----|-------|---------|----------|
| 0 | Trivial (bug fix, config change) | N/A | N/A | N/A | **OpenSpec** (or direct implementation) |
| 1 | Small change (single feature, isolated) | 1-5 | 0-1 | 1-5 | **OpenSpec** (proposal + tasks) |
| 2 | New feature (MVP) | 8-15 | 1-2 | 5-15 | **BMAD** (Planning → Solutioning → Implementation) |
| 3 | Comprehensive product | 12-25 | 2-5 | 15-40 | **BMAD** (Analysis optional → Planning → Solutioning → Implementation) |
| 4 | Enterprise platform | 20-35+ | 5-10+ | 40-100+ | **BMAD** (Analysis required → Planning → Solutioning → Implementation) |

**Determine Level**: Based on answers, assign Level 0-4.

### Routing Decision

**If Level 0 (Trivial)**:
```
This is a trivial change (bug fix, config, typo).

Recommendation: Implement directly without workflow.

Or if you want documentation, use OpenSpec:
  - openspec-propose (minimal proposal)
  - openspec-implement (quick implementation)
  - openspec-archive (document the change)

Would you like to use OpenSpec or just implement directly?
```

**If Level 1 (Small Change)**:
```
✅ This is a Level 1 change - perfect for OpenSpec!

OpenSpec is a lightweight workflow for simple features:
  1. Create proposal (why, what, tasks)
  2. Implement tasks
  3. Archive when deployed

I'll invoke openspec-propose to create your change proposal.
```

**If Level 2-4 (Complex)**:
```
✅ This is a Level {X} project - using BMAD workflow.

BMAD provides complete planning and architecture:
  - Phase 1: Analysis (optional/required based on level)
  - Phase 2: Planning (PRD, Epics)
  - Phase 3: Solutioning (Architecture)
  - Phase 4: Implementation (Stories → Dev)

I'll initialize the BMAD workflow...
```

### Step 3: Initialize Workflow (BMAD Only - Level 2-4)

**Skip this for Level 0-1** (OpenSpec doesn't use workflow-status.md)

For Level 2-4, run Python helper:
```bash
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py init \
  "{project_name}" "{project_type}" {level} "{user_name}"
```

This creates `docs/bmm-workflow-status.md` with:
- Project metadata
- Phase checklist
- Next recommended action

### Step 4: Invoke Appropriate Skill

#### For Level 0-1 (OpenSpec)

**Level 0**: Either implement directly or invoke `openspec-propose` if user wants documentation

**Level 1**: Invoke `openspec-propose` to create change proposal

**Tell user**:
```
✅ Level {X} - Using OpenSpec workflow

Quick and lightweight:
  1. Proposal - Define the change
  2. Implement - Execute tasks
  3. Archive - Update specs

Let me create your change proposal...

[Invoke openspec-propose]
```

#### For Level 2-4 (BMAD)

**Level 2**: Invoke `bmad-pm` (Planning phase)

**Level 3**: Ask if user wants Analysis first, or invoke `bmad-analyst`/`bmad-pm`

**Level 4**: Invoke `bmad-analyst` (Analysis required)

**Tell user**:
```
✅ BMAD Workflow initialized!

Project: {name}
Level: {level}
Type: {type}

📊 Status File: docs/bmm-workflow-status.md

🎯 Next Phase: {phase_name}

Let me start with {skill_name}...

[Invoke appropriate BMAD skill]
```

## Workflow: Check Status (`workflow-status`)

**When**: Anytime user wants to know "where am I?" or "what's next?"

**Process**:

### Step 1: Check for Workflow Status File

```bash
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py get-phase
```

**If no file**: Recommend running `workflow-init` first.

**If file exists**: Read current phase.

### Step 2: Assess Current State

Check what artifacts exist:
- [ ] `docs/brainstorm-notes.md` or `docs/product-brief.md` (Analysis)
- [ ] `docs/PRD.md` (Planning)
- [ ] `docs/epics.md` (Planning)
- [ ] `docs/ux-spec.md` (Planning, if UI-heavy)
- [ ] `docs/ARCHITECTURE.md` (Solutioning)
- [ ] `docs/sprint-status.yaml` (Implementation setup)
- [ ] `stories/*.md` files (Story Creation)

### Step 3: Determine Next Action

**Current Phase: Analysis**
- If product-brief.md exists → Proceed to Planning (bmad-pm)
- If not → Continue Analysis (bmad-analyst)

**Current Phase: Planning**
- If PRD.md and epics.md exist → Proceed to Solutioning (bmad-architecture)
- If PRD exists but no epics → Complete Planning (bmad-pm for epics)
- If neither → Start/continue Planning (bmad-pm)
- If UI-heavy and no ux-spec.md → Consider UX Design (bmad-ux)

**Current Phase: Solutioning**
- If ARCHITECTURE.md exists → Proceed to Implementation (Story Creation)
- If not → Start/continue Solutioning (bmad-architecture)

**Current Phase: Implementation**
- If sprint-status.yaml exists → Check story statuses
- If no sprint-status → Initialize sprint status
- If stories exist → Implement next story (bmad-dev)
- If no stories → Create stories (bmad-stories)

### Step 4: Report to User

```
📊 BMAD Workflow Status

Project: {name} (Level {level})
Current Phase: {phase}

✅ Completed:
- {list completed artifacts}

🔄 In Progress:
- {current phase}

⏭️ Next Action:
{specific recommendation with skill to load}

📁 Artifacts:
{list of created files}
```

## Workflow: Update Phase

**When**: Phase completed, need to transition to next

**Process**:

### Step 1: Validate Phase Gate

**Completing Analysis**:
- [ ] Product brief exists OR brainstorm notes exist
- User approved

**Completing Planning**:
- [ ] PRD.md exists with all sections
- [ ] epics.md exists with story breakdown
- [ ] UX-spec.md exists if UI-heavy (optional validation)
- User reviewed and approved

**Completing Solutioning**:
- [ ] ARCHITECTURE.md exists
- [ ] Decision table has specific versions
- [ ] Every epic mapped to components
- [ ] Implementation patterns defined
- User reviewed and approved

**Completing Implementation** (per story):
- [ ] Story file exists
- [ ] All acceptance criteria met
- [ ] All tests passing
- [ ] Dev Agent Record complete
- [ ] Story marked "done" in sprint-status.yaml

### Step 2: Mark Phase Complete

```bash
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py mark-complete "{phase}"
```

### Step 3: Update to Next Phase

```bash
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py update-phase "{next_phase}"
```

### Step 4: Add Artifacts

For each artifact created:
```bash
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py add-artifact \
  "{path}" "{description}"
```

### Step 5: Announce Transition

```
✅ Phase Complete: {completed_phase}

Artifacts Created:
- {list}

📊 Transitioning to: {next_phase}

🎯 Next Action: {recommendation}

Load {skill_name} to continue.
```

## Workflow: Sprint Planning

**When**: After epics.md created, before story creation

**Purpose**: Initialize sprint-status.yaml from epics

**Process**:

### Step 1: Check Prerequisites

- [ ] epics.md exists
- [ ] Contains story breakdown

### Step 2: Initialize Sprint Status

```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py init docs/epics.md
```

This creates `docs/sprint-status.yaml` with:
- All stories from epics
- Initial status: "backlog"
- Epic tracking
- Story tracking

### Step 3: Report to User

```
✅ Sprint Status Initialized

📊 File: docs/sprint-status.yaml

Summary:
- Total Epics: {count}
- Total Stories: {count}
- Status: All in backlog

🎯 Next Action:
Create first story with bmad-stories skill

To see next story: Ask orchestrator "what's the next story to create?"
```

## Workflow: Story Lifecycle Management

### Get Next Backlog Story

```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py next-backlog
```

Returns: Story key (e.g., "1-1-project-setup")

### Update Story Status

When story created:
```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "{story_key}" "drafted"
```

When story implementation starts:
```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "{story_key}" "in-progress" "{developer_name}"
```

When story in review:
```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "{story_key}" "review"
```

When story done:
```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "{story_key}" "done"
```

### List Stories by Status

```bash
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py list-status "{status}"
```

Statuses: backlog, drafted, ready, in-progress, review, done

## Decision Logic: Next Action

```python
def get_next_action(workflow_status, sprint_status, artifacts):
    level = workflow_status.project_level
    phase = workflow_status.current_phase

    # Level 0-1: Skip BMAD
    if level <= 1:
        return "Skip BMAD. Implement directly or create brief tech-spec."

    # Phase 1: Analysis
    if phase == "Analysis":
        if level >= 4 and not artifacts.product_brief:
            return "Create Product Brief with bmad-analyst skill"
        elif level == 3 and ask_user("Want to do analysis first?"):
            return "Create Product Brief with bmad-analyst skill"
        else:
            return "Proceed to Planning: Create PRD with bmad-pm skill"

    # Phase 2: Planning
    if phase == "Planning":
        if not artifacts.prd:
            return "Create PRD with bmad-pm skill"
        elif not artifacts.epics:
            return "Complete Epics Breakdown with bmad-pm skill"
        elif level >= 3 and ui_heavy and not artifacts.ux_spec:
            return "Consider creating UX Design with bmad-ux skill (optional)"
        else:
            return "Proceed to Solutioning: Create Architecture with bmad-architecture skill"

    # Phase 3: Solutioning
    if phase == "Solutioning":
        if not artifacts.architecture:
            return "Create Architecture with bmad-architecture skill"
        elif not artifacts.sprint_status:
            return "Initialize Sprint Planning (orchestrator will do this)"
        else:
            return "Proceed to Implementation: Create Stories with bmad-stories skill"

    # Phase 4: Implementation
    if phase == "Implementation":
        if not sprint_status.initialized:
            return "Initialize sprint status from epics (orchestrator will do this)"

        next_story = sprint_status.get_next_backlog()
        if next_story:
            return f"Create story {next_story} with bmad-stories skill"

        in_progress = sprint_status.get_stories_by_status("in-progress")
        if in_progress:
            return f"Continue implementing story {in_progress[0]} with bmad-dev skill"

        in_review = sprint_status.get_stories_by_status("review")
        if in_review:
            return f"Review story {in_review[0]} with bmad-dev skill (code-review)"

        drafted = sprint_status.get_stories_by_status("drafted")
        if drafted:
            return f"Implement story {drafted[0]} with bmad-dev skill"

        return "All stories complete! 🎉 Project done."
```

## Complete Phase Flow

### Level 2 Project Flow

```
1. workflow-init → Level 2 determined
2. workflow-status → "Start Planning"
   → bmad-pm: Create PRD + Epics
3. workflow-status → "Proceed to Solutioning"
   → bmad-architecture: Create Architecture
4. sprint-planning → Initialize sprint-status.yaml
5. workflow-status → "Create Stories"
   → bmad-stories: Create Story 1.1
   → bmad-stories: Create Story 1.2
   → ...
6. workflow-status → "Implement Stories"
   → bmad-dev: Implement Story 1.1
   → bmad-dev: Implement Story 1.2
   → ...
7. All done! 🎉
```

### Level 4 Project Flow

```
1. workflow-init → Level 4 determined
2. workflow-status → "Start Analysis"
   → bmad-analyst: Brainstorm + Product Brief + Research
3. workflow-status → "Proceed to Planning"
   → bmad-pm: Create PRD + Epics
   → bmad-ux: Create UX Design (if UI-heavy)
4. workflow-status → "Proceed to Solutioning"
   → bmad-architecture: Create comprehensive Architecture
   → bmad-tea: Initialize Test Framework (optional)
5. sprint-planning → Initialize sprint-status.yaml
6. workflow-status → "Create Stories"
   → bmad-tea: ATDD - Write tests first (optional)
   → bmad-stories: Create stories one by one
7. workflow-status → "Implement Stories"
   → bmad-dev: Implement stories iteratively
   → bmad-tea: Test automation (ongoing)
8. All done! 🎉
```

## User Commands

User can ask orchestrator:
- **"Initialize workflow"** → workflow-init
- **"What's my status?"** / **"Where am I?"** → workflow-status
- **"What's next?"** → workflow-status with recommendation
- **"What's the next story?"** → sprint-status next-backlog
- **"List backlog stories"** → sprint-status list-status backlog
- **"Mark Planning complete"** → update-phase with validation
- **"Show all stories"** → sprint-status list

## Important Notes

- **State files are source of truth**: Always read before giving recommendations
- **Validate phase gates**: Don't advance without artifacts
- **Guide, don't execute**: Orchestrator recommends skills, doesn't run them
- **Update state files**: After each phase completion
- **Sprint status from epics**: Always initialize after epics created

---

**Attribution**: Based on BMAD Method v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org
**Generated**: This skill orchestrates complete BMAD workflow with proper state management
