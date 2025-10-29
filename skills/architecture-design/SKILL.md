---
name: bmad-architecture-design
description: Produces decision-ready system architecture packages aligned to BMAD requirements and constraints.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Architecture Design Skill

## Mission
Convert approved product requirements into a Decision Architecture that communicates component structure, technology choices, and rationale for implementation teams.

## Inputs Required
- prd: latest PRD plus epic roadmap from product-requirements skill
- constraints: non-functional requirements, compliance rules, and integrations
- existing_assets: repositories, current architecture diagrams, or technology standards
- project_level: BMAD level sizing to guide depth of design

Missing inputs must be escalated to the orchestrator or originating skill before work proceeds.

## Outputs
- `ARCHITECTURE.md` written using `assets/decision-architecture-template.md.jinja`
- Updated risk and decision log entries summarized for stakeholders

Deliverables should highlight decisions, rejected options, and implementation guardrails.

## Process
1. Validate prerequisites via `CHECKLIST.md` and confirm planning artifacts are approved.
2. Identify architecture drivers (quality attributes, constraints, integrations).
3. Design component topology, data flows, and technology selections with traceability to requirements.
4. Record key decisions, alternatives, and mitigation strategies.
5. Generate or update architecture artifact using `scripts/generate_architecture.py` if structured data is available.
6. Review the quality checklist and publish summary plus follow-up actions for delivery-planning and development-execution skills.

## Quality Gates
Follow `CHECKLIST.md` to ensure completeness, feasibility, and stakeholder alignment. Stop if guardrails fail.

## Error Handling
When contradictions or gaps exist:
- Cite the specific requirement or assumption causing the conflict.
- Request clarifications from product-requirements, UX, or discovery-analysis skills.
- Recommend holding implementation until resolution is documented.
