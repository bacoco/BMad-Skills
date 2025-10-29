---
name: bmad-end-to-end-orchestration
description: Maintains workflow state, phase gates, and routing decisions across the BMAD skills portfolio.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# End-to-End Orchestration Skill

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
