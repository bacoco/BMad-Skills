---
name: bmad-stories
description: Breaks approved epics into sequenced, testable stories and delivery notes ready for development execution.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Delivery Planning Skill

## Mission
Transform epics and architecture decisions into developer-ready story packages, including acceptance criteria, dependencies, and delivery signals.

## Inputs Required
- epics: latest epics.md from product-requirements skill
- architecture: decision architecture outputs and guardrails
- ux_assets: annotated wireframes or UX notes when relevant
- sprint_status: current delivery cadence and capacity information

## Outputs
- Story markdown files created using `assets/story-template.md.jinja`
- Updated backlog summary highlighting sequencing, dependencies, and blockers
- Recommendations for next stories to activate for development-execution

## Process
1. Confirm readiness by running `CHECKLIST.md` and ensuring prerequisite artifacts exist.
2. Prioritize epics/stories based on value, dependencies, and risk.
3. Draft or update story files, capturing acceptance criteria, prerequisites, and test hooks.
4. Use `scripts/create_story.py` when structured JSON is provided; otherwise author manually with template guidance.
5. Document sprint updates and communicate next-step recommendations to orchestrator and stakeholders.

## Quality Gates
`CHECKLIST.md` must pass before handing off stories. Every story must align with architecture decisions and cite upstream references.

## Error Handling
If prerequisites are missing or conflicting:
- Identify the missing artifact or decision and why it blocks story creation.
- Route back to the responsible skill (architecture, UX, product-requirements) for clarification.
- Suggest alternative backlog items only when ready stories already exist.
