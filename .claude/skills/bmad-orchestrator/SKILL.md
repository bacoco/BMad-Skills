---
name: bmad-orchestrator
description: BMAD workflow orchestrator. Auto-invokes at conversation start. Tracks status, guides through phases. Invoke when user says 'start project', 'what's next', 'where am I', 'status', 'initialize', or implicitly for any BMAD work. Keywords: status, workflow, next, start, guide, phase, where, initialize.
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
- Mentions "idea", "brainstorm" → bmad-analyst
- Mentions "PRD", "requirements" → bmad-pm
- Mentions "architecture", "build" → bmad-architecture
- Mentions "test strategy" → bmad-tea
- Mentions "stories", "breakdown" → bmad-stories
- Mentions "implement", "code" → bmad-dev

**Do NOT invoke when:**
- User is clearly asking for a specific skill (let that skill handle it)
- User is in the middle of implementing code (bmad-dev is active)
- User is asking technical questions unrelated to workflow

## Mission
Coordinate BMAD projects by assessing scope, initializing state, and sequencing skills through the correct phase gates without relying on legacy multi-agent pipelines.

## Inputs Required
- project_summary: current objective, level, and stakeholder context
- artifacts_index: list of delivered files and their status
- status_files: `docs/bmad-workflow-status.md`, `docs/sprint-status.yaml`, or equivalents if they exist

## Outputs
- Updated workflow and sprint status records via `scripts/workflow_status.py` and `scripts/sprint_status.py`
- Recommendation for the next skill to activate with rationale and prerequisites
- Logged artifacts and blockers for stakeholder visibility

## Process
1. Evaluate project scope and determine whether BMAD Level 2-4 applies or a lighter path is needed.
2. Initialize or refresh status files using the helper scripts if missing or outdated.
3. Review deliverables and gate criteria from preceding skills.
4. Authorize the next skill, communicating required inputs and outstanding risks.
5. Update records and summarize progress for the requestor.

## Quality Gates
All items in `CHECKLIST.md` must be satisfied to progress between phases. Never advance without required artifacts.

## Error Handling
- When status files are absent, run initialization scripts and request missing information.
- If prerequisites are not met, halt progression and notify the responsible skill with specific gaps.
- Downgrade to lightweight workflows (e.g., OpenSpec) when project level is 0-1 and BMAD overhead is unnecessary.
