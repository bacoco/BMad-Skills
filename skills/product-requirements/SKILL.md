---
name: bmad-product-requirements
description: Drafts complete product requirements and epic roadmap packages from validated discovery inputs using BMAD templates.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Product Requirements Skill

## Mission
Transform validated discovery insights into a production-ready Product Requirements Document (PRD) and epic roadmap that align stakeholders and prepare downstream architecture, UX, and delivery work.

## Inputs Required
- business_goal: clear outcome statement tied to measurable success metrics
- stakeholders: decision makers plus their approvals or open concerns
- constraints: technical, regulatory, financial, or timeline guardrails
- discovery_artifacts: briefs, research memos, or notes from the discovery-analysis skill

If any input is missing or stale, pause and request the exact artifact before proceeding.

## Outputs
Produce two markdown artifacts aligned to the templates in `assets/`:
1. `PRD.md` populated from `assets/prd-template.md.jinja`
2. `epics.md` populated from `assets/epic-roadmap-template.md.jinja`

Deliverables must be written to the project documentation folder (default `docs/`) and summarized for the requestor.

## Process
1. Validate readiness using the gate in `CHECKLIST.md`.
2. Review discovery inputs and clarify remaining unknowns.
3. Map goals, scope, and constraints into structured PRD sections.
4. Prioritize epics, sequencing, and acceptance signals for delivery.
5. Run `scripts/generate_prd.py` when structured data exists; otherwise compose outputs manually following templates.
6. Apply the quality checklist before returning deliverables and recommended next steps.

## Quality Gates
Confirm every item in `CHECKLIST.md` is satisfied before delivering the PRD package. Stop and fix any unmet criteria.

## Error Handling
If prerequisites are missing or contradictions surface:
- Identify which required input is absent and why it blocks progress.
- Provide a minimal list of follow-up questions or stakeholders needed.
- Recommend re-engaging the discovery-analysis skill or orchestrator when scope is unclear.
