---
name: bmad-global
description: Complete BMAD workflow system - from idea to implementation. Auto-routes to discovery, planning, architecture, testing, stories, and development skills based on your needs.
version: 2.1.5
allowed-tools: ["Read", "Write", "Grep", "Bash"]
metadata:
  auto-invoke: true
  triggers:
    patterns:
      - "I have an idea"
      - "I want to build"
      - "help me with"
      - "create a"
      - "let's work on"
      - "start a project"
      - "what's next"
      - "status"
    keywords:
      - idea
      - build
      - create
      - project
      - help
      - start
      - plan
      - design
      - develop
      - workflow
  capabilities:
    - complete-workflow
    - auto-routing
    - discovery-research
    - product-planning
    - ux-design
    - architecture-design
    - test-strategy
    - story-planning
    - development-execution
    - change-management
  prerequisites: []
  outputs:
    - workflow-artifacts
    - routed-deliverables
---

# BMAD Global Workflow System

**The complete product development workflow in a single skill.** From vague ideas to working code through natural conversation.

## What This Skill Does

BMAD Global is your **intelligent workflow orchestrator** that automatically routes your work through the right process based on complexity and stage:

- **Level 0-1 Changes** (small fixes, config) → **OpenSpec** workflow
- **Level 2-4 Projects** (features, products) → **Full BMAD** workflow

You don't need to know which sub-skill to invoke - just describe what you want to do, and BMAD Global handles the rest.

## When to Invoke

**Auto-activates when you:**
- Start any new work: "I have an idea", "I want to build", "Let's create"
- Need guidance: "What's next?", "Where should I start?"
- Check status: "What's the status?", "Show me progress"
- Continue work: "Let's keep going", "Continue with this project"

**Specific trigger phrases:**
- "I have an idea for [something]"
- "I want to build [something]"
- "Help me with [task]"
- "Create a [thing]"
- "What's next on [project]?"
- "Show me the workflow status"
- "Let's work on [feature]"

**Works for ANY stage:**
- 💡 Brainstorming & discovery
- 📋 Requirements & planning
- 🎨 UX design
- 🏗️ Architecture
- ✅ Test strategy
- 📝 Story creation
- 💻 Implementation
- 🔧 Bug fixes & changes

## Mission

Provide a **seamless end-to-end workflow** that:
1. Understands where you are in your project journey
2. Routes you to the appropriate skill automatically
3. Tracks progress across all phases
4. Delivers production-ready artifacts at each stage

## How It Works

### Intelligent Routing

```
User Input → Assess Complexity & Stage → Route to Right Skill
     ↓
[Discovery] → [Planning] → [Design] → [Architecture] → [Testing] → [Stories] → [Development]
     ↓                                                                              ↓
  Research Brief          PRD          UX Specs     Architecture    Test Strategy  Stories  → Working Code
```

### Complexity Assessment

**Level 0-1: OpenSpec (Lightweight)**
- Bug fixes
- Config changes
- Small enhancements
- Quick iterations

**Level 2: BMAD Planning**
- New features requiring architecture
- Multi-component changes
- Clear requirements

**Level 3-4: Full BMAD Discovery**
- New product areas
- Complex features
- Novel solutions
- High uncertainty

## Workflow Phases

### Phase 0: Triage (Automatic)
I assess:
- What you want to accomplish
- Current project state
- Complexity level
- Which phase you're in

Then route to the appropriate skill.

### Phase 1: Discovery (Level 3-4)
**Via: `bmad-discovery-research`**

Outputs:
- Discovery brief
- Problem statement
- Research dossier
- Risk assessment

**When:** Vague ideas, new products, complex problems

### Phase 2: Planning (Level 2-4)
**Via: `bmad-product-planning`**

Outputs:
- Product Requirements Document (PRD)
- Epic breakdown
- Feature specifications

**When:** Requirements needed, scope definition

### Phase 3: UX Design (Optional, UI-heavy projects)
**Via: `bmad-ux-design`**

Outputs:
- User flows
- Wireframes
- Design system specs

**When:** User-facing features, UI work

### Phase 4: Architecture (Level 2-4)
**Via: `bmad-architecture-design`**

Outputs:
- Decision architecture
- Tech stack decisions
- Implementation patterns

**When:** Technical decisions needed

### Phase 5: Testing Strategy (Level 2-4)
**Via: `bmad-test-strategy`**

Outputs:
- Test strategy document
- ATDD scenarios
- Quality checklist

**When:** Quality planning needed

### Phase 6: Story Planning (Level 2-4)
**Via: `bmad-story-planning`**

Outputs:
- Developer stories
- Acceptance criteria
- Story files

**When:** Breaking work into tasks

### Phase 7: Development (All levels)
**Via: `bmad-development-execution`**

Outputs:
- Working code
- Tests
- Implementation notes

**When:** Ready to code

### Alternative: OpenSpec (Level 0-1)
**Via: `openspec-change-*` skills**

Process:
1. Propose change
2. Implement change
3. Archive change

**When:** Small, focused changes

## Example Conversations

### Example 1: New Product Idea

**You:** "I have an idea for a task management app"

**BMAD Global:**
- Assesses: Level 3 (new product, high uncertainty)
- Routes to: `bmad-discovery-research`
- Action: Conducts discovery session
- Output: Discovery brief → Ready for planning

### Example 2: Feature Addition

**You:** "I want to add user authentication to my app"

**BMAD Global:**
- Assesses: Level 2 (defined feature, needs architecture)
- Routes to: `bmad-product-planning` (if no PRD)
- Then: `bmad-architecture-design`
- Then: `bmad-story-planning`
- Output: Ready-to-implement stories

### Example 3: Bug Fix

**You:** "Fix the login button alignment"

**BMAD Global:**
- Assesses: Level 0 (small fix)
- Routes to: `openspec-change-proposal`
- Action: Quick proposal → implementation
- Output: Fixed code

### Example 4: Status Check

**You:** "What's the status of my authentication project?"

**BMAD Global:**
- Checks: Workflow status file
- Shows: Current phase, completed artifacts, next steps
- Routes to: Next pending phase

## Integration with Sub-Skills

BMAD Global acts as a **smart router** to specialized skills:

| Sub-Skill | Purpose | When Used |
|-----------|---------|-----------|
| `main-workflow-router` | Status tracking | Invoked by Global for status |
| `bmad-discovery-research` | Idea exploration | Level 3-4, unclear requirements |
| `bmad-product-planning` | Requirements | Level 2-4, need PRD |
| `bmad-ux-design` | User experience | UI-heavy features |
| `bmad-architecture-design` | Tech decisions | Level 2-4, need architecture |
| `bmad-test-strategy` | Quality planning | Level 2-4, need test strategy |
| `bmad-story-planning` | Task breakdown | Level 2-4, need stories |
| `bmad-development-execution` | Coding | All levels, implementation |
| `openspec-change-proposal` | Change proposals | Level 0-1, quick changes |
| `openspec-change-implementation` | Change execution | Level 0-1, implementation |
| `openspec-change-closure` | Change archival | Level 0-1, cleanup |

## Process

1. **Listen & Understand**
   - Parse user intent
   - Identify current context
   - Check for existing workflow state

2. **Assess Complexity**
   - Level 0: Config/trivial
   - Level 1: Small enhancement
   - Level 2: Feature with architecture
   - Level 3: New product area
   - Level 4: Novel innovation

3. **Route to Appropriate Skill**
   - OpenSpec for Level 0-1
   - Discovery for Level 3-4 with unclear requirements
   - Planning for Level 2+ with some clarity
   - Architecture/Testing/Stories as prerequisites are met
   - Development when ready to code

4. **Track Progress**
   - Maintain workflow status
   - Record completed phases
   - Identify next steps
   - Update artifacts list

5. **Deliver Results**
   - Output from routed skill
   - Status summary
   - Next recommended action

## Quality Gates

Before routing to next phase:
- ✅ Prerequisites artifacts exist
- ✅ Current phase deliverables complete
- ✅ Quality checklist satisfied
- ✅ User confirmation obtained

## Error Handling

- **Unclear intent:** Ask clarifying questions
- **Missing prerequisites:** Route to prerequisite skill first
- **Conflicting requirements:** Flag and request resolution
- **Scope creep:** Suggest re-assessment of complexity level

## Commands

You can direct the workflow explicitly:

- `"Show workflow status"` - Display current phase and progress
- `"Start discovery"` - Force discovery phase
- `"Skip to planning"` - Jump to planning (if prerequisites met)
- `"What's next?"` - Get next recommended action
- `"Reset workflow"` - Start fresh (asks for confirmation)

## Workspace & Artifacts

All artifacts are stored in:
```
_runtime/workspace/
├── artifacts/    # BMAD planning artifacts
├── stories/      # Developer stories
├── changes/      # OpenSpec change proposals
└── specs/        # OpenSpec specifications
```

Status tracking:
- `_runtime/workspace/artifacts/workflow-status.md`

## Benefits

### For You
- **No skill selection needed** - Just describe what you want
- **Guided workflow** - Always know what's next
- **Progress tracking** - See where you are
- **Flexible routing** - Skip phases when appropriate

### For Complex Projects
- **Structured approach** - Don't miss important steps
- **Documentation** - Complete artifact trail
- **Quality built-in** - Testing and validation at each stage

### For Quick Changes
- **Fast path** - OpenSpec for small fixes
- **No overhead** - Skip unnecessary planning
- **Quick turnaround** - Propose → Implement → Done

## Getting Started

Just start talking:

```
"I have an idea for a feature that..."
"I want to build something that..."
"Help me fix this bug..."
"What's the status of my project?"
"Let's work on authentication"
```

BMAD Global figures out the rest.

---

## Technical Notes

### Skill References

This skill internally invokes:
- `.claude/skills/main-workflow-router/SKILL.md`
- `.claude/skills/bmad-discovery-research/SKILL.md`
- `.claude/skills/bmad-product-planning/SKILL.md`
- `.claude/skills/bmad-ux-design/SKILL.md`
- `.claude/skills/bmad-architecture-design/SKILL.md`
- `.claude/skills/bmad-test-strategy/SKILL.md`
- `.claude/skills/bmad-story-planning/SKILL.md`
- `.claude/skills/bmad-development-execution/SKILL.md`
- `.claude/skills/openspec-change-proposal/SKILL.md`
- `.claude/skills/openspec-change-implementation/SKILL.md`
- `.claude/skills/openspec-change-closure/SKILL.md`

### Workspace Paths

Uses standard BMAD paths:
```python
SKILLS_ROOT / "_runtime" / "workspace" / "artifacts"
SKILLS_ROOT / "_runtime" / "workspace" / "stories"
SKILLS_ROOT / "_runtime" / "workspace" / "changes"
SKILLS_ROOT / "_runtime" / "workspace" / "specs"
```

### Template Locations

Delegates to sub-skills for template rendering.

---

_BMAD Global Workflow System v2.1.5_
_The complete end-to-end workflow in a single skill_
