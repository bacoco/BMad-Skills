---
name: bmad-orchestrator
description: Global workflow orchestrator for BMAD and OpenSpec. Auto-invokes at conversation start. Routes Level 0-1 to OpenSpec, Level 2-4 to BMAD. Tracks status, guides through phases. Invoke when user says 'start project', 'what's next', 'where am I', 'status', or begins any development work. Keywords: status, workflow, next, start, guide, phase, where, initialize, orchestrate.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# End-to-End Orchestration Skill

## When to Invoke

**ALWAYS auto-invoke at the start of any BMAD project:**
- User says "start project", "new project", "initialize BMAD", "begin"
- User says "what's next?", "where am I?", "check status", "workflow status"
- User begins describing a product idea without mentioning BMAD explicitly
- At the beginning of ANY product development conversation
- User asks for guidance on the development process

**Special auto-behaviors:**
- If no workflow-status.md exists → automatically run initialization workflow
- If workflow-status.md exists → read current status and recommend next action
- If user mentions a specific phase → route to the appropriate skill
- If user is mid-project → check phase completion and suggest next step

**Routing intelligence based on user intent:**

**FIRST: Assess complexity level (0-4)**
- Level 0-1 (bug fix, small change, simple feature) → Route to OpenSpec
- Level 2-4 (new product, complex feature, architecture) → Route to BMAD

**For OpenSpec work (Level 0-1):**
- Mentions "bug", "fix", "small change", "quick" → openspec-propose
- Has proposal, says "implement", "apply" → openspec-implement
- Change complete, says "archive", "close" → openspec-archive

**For BMAD work (Level 2-4):**
- Mentions "idea", "brainstorm", "explore" → bmad-analyst
- Mentions "PRD", "requirements", "plan" → bmad-pm
- Mentions "UX", "UI", "design" → bmad-ux
- Mentions "architecture", "tech stack", "build" → bmad-architecture
- Mentions "test strategy", "QA", "ATDD" → bmad-tea
- Mentions "stories", "breakdown", "backlog" → bmad-stories
- Mentions "implement story", "code", "develop" → bmad-dev

**Critical decision: OpenSpec vs BMAD**
- Small, well-defined, existing codebase → OpenSpec
- Greenfield, complex, or needs discovery → BMAD
- When in doubt, ask user about complexity level

**Do NOT invoke when:**
- User is clearly asking for a specific skill (let that skill handle it)
- User is in the middle of implementing code (appropriate skill is active)
- User is asking technical questions unrelated to workflow

## Auto-Activation Behavior

This skill applies specialized routing heuristics whenever it auto-invokes:

### 1. Conversation Start Detection
When a conversation begins and the user mentions:
- Product development topics
- Project ideas or features
- Building or creating something
- BMAD or OpenSpec methodology

**Auto-action:** Initialize workflow files if none exist and recommend the right path.

### 2. Status Check Detection
When user asks:
- "Where am I?"
- "What's next?"
- "What should I do now?"
- "Check workflow status"

**Auto-action:** Read workflow-status.md, summarize phase progress, and suggest next skill.

### 3. Phase Transition Detection
When a downstream skill completes its phase:
- Analyst delivers discovery brief → confirm Planning readiness
- PM delivers PRD/epics → prepare Solutioning
- Architecture delivers decision doc → move to Implementation

**Auto-action:** Update workflow status and queue the appropriate next capability.

### 4. Routing Intelligence
Based on user intent, automatically route to:
- Mentions "idea", "brainstorm" → bmad-analyst
- Mentions "PRD", "requirements" → bmad-pm
- Mentions "UX", "UI" → bmad-ux
- Mentions "architecture", "tech stack" → bmad-architecture
- Mentions "test strategy", "QA" → bmad-tea
- Mentions "stories", "backlog" → bmad-stories
- Mentions "implement", "code" → bmad-dev
- Mentions "small change", "bug" → openspec-propose

### 5. Safety Checks
Before routing, verify:
- [ ] Required artifacts from previous phase exist
- [ ] Quality gates in CHECKLIST.md are satisfied
- [ ] No unresolved blockers in workflow-status.md

If checks fail, halt routing and request the missing prerequisites.

## Mission
Serve as the global orchestrator for all product development work, intelligently routing between BMAD (Level 2-4 complex projects) and OpenSpec (Level 0-1 lightweight changes). Assess scope, initialize appropriate state management, and sequence skills through correct phase gates for optimal workflow efficiency.

## Inputs Required
- project_summary: current objective, level, and stakeholder context
- artifacts_index: list of delivered files and their status
- status_files: `docs/bmad-workflow-status.md`, `docs/sprint-status.yaml`, or equivalents if they exist

## Outputs
- Updated workflow and sprint status records via `scripts/workflow_status.py` and `scripts/sprint_status.py`
- Recommendation for the next skill to activate with rationale and prerequisites
- Logged artifacts and blockers for stakeholder visibility

## Process

1. **Assess Complexity & Choose Workflow**
   - Determine project level (0-4) from user description
   - Level 0-1: Route to OpenSpec (propose → implement → archive)
   - Level 2-4: Route to BMAD (analysis → planning → solutioning → implementation)
   - When ambiguous: Ask clarifying questions about scope and complexity

2. **Initialize State Management**
   - For BMAD: Create/update `docs/bmad-workflow-status.md` and `docs/sprint-status.yaml`
   - For OpenSpec: Scaffold change workspace in `openspec/changes/<change-id>/`
   - Use helper scripts: `workflow_status.py`, `sprint_status.py`, `scaffold_change.py`

3. **Review Context & Prerequisites**
   - Check existing artifacts from previous phases
   - Validate gate criteria from preceding skills
   - Identify missing prerequisites or blockers

4. **Route to Next Skill**
   - For OpenSpec: openspec-propose → openspec-implement → openspec-archive
   - For BMAD: Route through phases (analyst → pm → ux/architecture/tea → stories → dev)
   - Communicate required inputs and outstanding risks

5. **Update State & Report Progress**
   - Update workflow status files
   - Log completed artifacts and next actions
   - Highlight blockers and recommend remediation
   - Escalate from OpenSpec to BMAD if scope grows beyond Level 1

## Quality Gates
All items in `CHECKLIST.md` must be satisfied to progress between phases. Never advance without required artifacts.

## Error Handling
- When status files are absent, run initialization scripts and request missing information.
- If prerequisites are not met, halt progression and notify the responsible skill with specific gaps.
- Downgrade to lightweight workflows (e.g., OpenSpec) when project level is 0-1 and BMAD overhead is unnecessary.
