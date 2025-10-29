# BMAD Phases

## Phase 1: Analysis (bmad-analyst)

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

## Phase 2: Planning (bmad-pm + bmad-ux)

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

## Phase 3: Solutioning (bmad-architecture + bmad-tea)

**When**: Level 2-4, always required

**Workflows**:
- **Architecture**: Technical design, tech stack, patterns
- **Test Strategy**: Test framework setup (optional)

**Outputs**:
- `docs/ARCHITECTURE.md` - Decision architecture
- `docs/testing-strategy.md` - Test strategy (optional)
- Test framework files (optional)

**Next Phase**: Implementation (story creation)

## Phase 4: Implementation (bmad-stories + bmad-dev + bmad-tea)

**When**: After Solutioning complete

**Workflows**:

### 1. Sprint Planning (Orchestrator)
- Initializes `docs/sprint-status.yaml` from epics
- All stories start in "backlog" status

### 2. Story Creation (bmad-stories)
- Creates developer-ready story files
- Each story: `stories/{epic}-{story}-{title}.md`
- Includes: AC, tasks, dev notes, learnings from previous story

### 3. ATDD (bmad-tea, optional)
- Write tests BEFORE implementation
- Tests define expected behavior

### 4. Implementation (bmad-dev)
- Implement story following architecture
- Write/run tests
- Update Dev Agent Record
- Mark story status: drafted → in-progress → review → done

### 5. Code Review (bmad-dev)
- Fresh-eyes review of completed story
- Document findings and action items

**Outputs**:
- `docs/sprint-status.yaml` - Story tracking
- `stories/*.md` - Story files
- Source code files
- Test files
