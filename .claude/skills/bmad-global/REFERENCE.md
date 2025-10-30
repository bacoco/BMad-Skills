# BMAD Global - Reference Documentation

## Complete Workflow System

BMAD Global is the **unified entry point** for the entire BMAD Skills ecosystem. It provides intelligent routing and orchestration across all 11 specialized skills.

## Architecture

### Two-Track System

```
BMAD Global
    ├── OpenSpec Track (Level 0-1)
    │   ├── openspec-change-proposal
    │   ├── openspec-change-implementation
    │   └── openspec-change-closure
    │
    └── BMAD Track (Level 2-4)
        ├── main-workflow-router (status & orchestration)
        ├── bmad-discovery-research (Phase 1)
        ├── bmad-product-planning (Phase 2)
        ├── bmad-ux-design (Phase 3, optional)
        ├── bmad-architecture-design (Phase 4)
        ├── bmad-test-strategy (Phase 5)
        ├── bmad-story-planning (Phase 6)
        └── bmad-development-execution (Phase 7)
```

### Routing Logic

The skill uses a decision tree to route conversations:

1. **Check for status request** → `main-workflow-router`
2. **Assess complexity** → Level 0-4
3. **Check existing state** → Resume from current phase
4. **Route appropriately**:
   - Level 0-1 → OpenSpec
   - Level 2-4 + unclear → Discovery
   - Level 2-4 + clear → Planning
   - Continue based on prerequisites

## Complexity Levels (Detailed)

### Level 0: Trivial
- One-line fixes
- Config value changes
- Documentation updates
- Typo fixes

**Indicators:**
- Clear solution
- No design needed
- No testing required
- < 15 minutes

**Route:** OpenSpec direct to implementation

### Level 1: Simple
- Small bug fixes
- Simple enhancements
- Minor feature additions
- Straightforward changes

**Indicators:**
- Clear requirements
- Known solution pattern
- Minimal design
- < 2 hours

**Route:** OpenSpec with brief proposal

### Level 2: Medium
- Feature additions
- Component modifications
- API changes
- Integration work

**Indicators:**
- Requires architecture
- Multiple files affected
- Testing needed
- 2-8 hours

**Route:** BMAD Planning → Architecture → Stories → Dev

### Level 3: Complex
- New product areas
- Major features
- System redesigns
- Cross-cutting changes

**Indicators:**
- Unclear requirements initially
- Multiple components
- UX considerations
- 1-2 weeks

**Route:** BMAD Discovery → Planning → UX → Architecture → Testing → Stories → Dev

### Level 4: Novel
- Innovative solutions
- New product launches
- Unproven approaches
- High uncertainty

**Indicators:**
- Research needed
- Novel patterns
- Market validation
- Multiple sprints

**Route:** Full BMAD with extended discovery and iterative validation

## Sub-Skill Deep Dive

### main-workflow-router
**Purpose:** Status tracking and orchestration
**Invoked when:**
- User asks "what's next?"
- Status check needed
- Phase transition

**Artifacts:**
- `workflow-status.md` - Current state
- `sprint-status.yaml` - Story tracking

### bmad-discovery-research
**Purpose:** Idea exploration and validation
**Invoked when:**
- Vague initial idea
- Level 3-4 project
- Research needed

**Outputs:**
- Discovery brief
- Problem statement
- Research dossier

**Duration:** 30-120 minutes

### bmad-product-planning
**Purpose:** Requirements definition
**Invoked when:**
- Idea validated
- Need formal PRD
- Level 2+ project

**Outputs:**
- Product Requirements Document
- Epic breakdown
- Feature specifications

**Duration:** 1-3 hours

### bmad-ux-design
**Purpose:** User experience design
**Invoked when:**
- UI-heavy features
- User flows needed
- Interface design

**Outputs:**
- User flows
- Wireframes
- Design system

**Duration:** 1-4 hours

**Skip if:** Backend-only, no UI

### bmad-architecture-design
**Purpose:** Technical design decisions
**Invoked when:**
- Level 2+ project
- Tech decisions needed
- Architecture unclear

**Outputs:**
- Decision architecture
- Tech stack choices
- Implementation patterns

**Duration:** 1-3 hours

### bmad-test-strategy
**Purpose:** Quality planning
**Invoked when:**
- Level 2+ project
- Testing approach needed
- Quality gates required

**Outputs:**
- Test strategy
- ATDD scenarios
- Quality checklist

**Duration:** 30-90 minutes

### bmad-story-planning
**Purpose:** Task breakdown
**Invoked when:**
- Architecture complete
- Ready to plan implementation
- Need developer stories

**Outputs:**
- User stories
- Story files
- Acceptance criteria

**Duration:** 1-2 hours

### bmad-development-execution
**Purpose:** Implementation
**Invoked when:**
- Stories ready
- Ready to code
- Implementation phase

**Outputs:**
- Working code
- Tests
- Implementation notes

**Duration:** Variable (per story)

### openspec-change-*
**Purpose:** Lightweight change management
**Invoked when:**
- Level 0-1 changes
- Quick fixes
- Incremental work

**Process:**
1. Proposal → 2. Implementation → 3. Closure

**Duration:** 15-60 minutes total

## State Management

BMAD Global tracks state in:

```
_runtime/workspace/artifacts/workflow-status.md
```

**State includes:**
- Current phase
- Completed phases
- Artifacts created
- Next recommended action
- Project metadata

**State transitions:**
```
Idle → Discovery → Planning → [UX] → Architecture → Testing → Stories → Development → Done
                                                                                ↓
                                                                          OpenSpec (Level 0-1)
```

## Best Practices

### For New Users
1. Start with natural language - no commands needed
2. Let BMAD Global guide you through phases
3. Trust the routing logic
4. Provide clarifications when asked

### For Experienced Users
1. Jump to specific phases if prerequisites met
2. Use explicit commands for control
3. Skip optional phases (e.g., UX for backend work)
4. Override routing when appropriate

### For Complex Projects
1. Start with discovery even if it seems clear
2. Don't skip architecture phase
3. Create comprehensive test strategy
4. Break into smaller stories

### For Quick Changes
1. Mention it's a "quick fix" or "small change"
2. Provide clear description
3. Let OpenSpec handle it
4. Review before merging

## Integration Patterns

### With Version Control
BMAD Global works alongside your git workflow:

```
Discovery → Planning → Architecture → Stories → Development
                                          ↓
                                    Feature Branch
                                          ↓
                                  Implement Stories
                                          ↓
                                      PR Review
                                          ↓
                                        Merge
```

### With Project Management
Artifacts can feed into:
- Jira/Linear: Stories from story-planning
- Notion/Confluence: Documentation from all phases
- GitHub Issues: Acceptance criteria

### With Testing Tools
- Test strategy → Test plans
- ATDD scenarios → Automated tests
- Acceptance criteria → Validation tests

## Troubleshooting

### "BMAD Global seems confused"
- Clear your intent explicitly
- Use status check to see current state
- Try explicit routing: "Let's start with discovery"

### "Wrong phase suggested"
- Override: "Skip to [phase]"
- Provide more context about project state
- Use explicit complexity: "This is a Level 2 feature"

### "Missing prerequisites"
- BMAD Global will route to prerequisite first
- Follow the suggested order
- Or provide missing artifacts manually

### "Too much overhead for simple task"
- Explicitly state: "This is a quick fix"
- Level 0-1 will use OpenSpec (lightweight)
- Or just describe the change directly

## Advanced Usage

### Custom Workflows
You can customize phase order:
```
"Let's do architecture before planning for this one"
```

BMAD Global adapts to your needs.

### Parallel Phases
Some phases can run in parallel:
```
"Design UX and test strategy can happen together"
```

BMAD Global coordinates parallel work.

### Iterative Refinement
After development:
```
"Let's refine the architecture based on what we learned"
```

BMAD Global supports iterative improvements.

## Performance Expectations

| Workflow Type | Phases | Duration | Artifacts |
|---------------|--------|----------|-----------|
| Quick Fix (L0) | 1 | 15-30 min | 1 proposal |
| Small Feature (L1) | 2 | 30-60 min | 1-2 docs |
| Medium Feature (L2) | 4-5 | 4-8 hours | 4-6 docs |
| Large Feature (L3) | 6-7 | 2-3 days | 8-10 docs |
| New Product (L4) | 7-8 | 1-2 weeks | 12+ docs |

## Glossary

- **Routing**: Selecting the appropriate sub-skill
- **Phase**: Stage in the BMAD workflow
- **Level**: Complexity assessment (0-4)
- **Track**: OpenSpec or BMAD path
- **Prerequisites**: Required artifacts for phase
- **Artifact**: Deliverable from a phase
- **Status**: Current workflow state
- **Orchestration**: Coordination across skills

---

_For detailed sub-skill documentation, refer to individual SKILL.md files in each skill directory._
