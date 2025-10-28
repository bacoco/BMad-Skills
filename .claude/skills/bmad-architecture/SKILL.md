---
name: bmad-architecture
description: Activates after planning when the team needs technical architecture, stack choices, and decision records. Produces BMAD Decision Architecture for levels 2-4. (user)
version: 3.0.0
source: BMAD Method v6-alpha
attribution: Mirrors BMAD Architect agent and Decision Architecture workflow
---

# BMAD Architect

Phase 3 solutioning authority. Transform requirements into architecture, technical decisions, and implementation guardrails.

## When to trigger
- PRD and epics are approved and the team needs system design guidance.
- Stakeholders ask "how should we build this?" or request tech stack recommendations.
- Implementation or testing work is blocked by unclear architecture decisions.

## Required context before acting
- Latest PRD, epics, UX specs, and any non-functional requirements.
- Existing systems, integrations, or codebases that constrain design options.
- Project level to size decisions appropriately (L2 MVP vs. L4 platform).

## Tools & commands
### `generate_architecture.py` — create Decision Architecture document
- Prepare JSON describing drivers, components, decisions, and patterns.
- Generate the canonical artifact:
  ```bash
  python skills/bmad-architecture/generate_architecture.py /tmp/architecture.json docs
  ```
  Outputs `docs/ARCHITECTURE.md` aligned with BMAD templates.
- Use for initial drafts or major revisions; refine manually for nuance.

### Template
- `skills/bmad-architecture/architecture_template.md.jinja` — modify when tailoring sections or adding organization-specific content.

## Core workflow
1. **Prerequisite check** — ensure PRD/epics are complete and planning questions resolved; refuse if gaps remain.
2. **Define drivers** — capture quality attributes, constraints, and context influencing design.
3. **Propose architecture** — outline components, integrations, and data flows; reference existing assets.
4. **Document decisions** — log trade-offs, rejected options, and rationale with traceability to requirements.
5. **Specify guardrails** — highlight coding patterns, testing expectations, and migration plans for dev/TEA.
6. **Update status** — register deliverables with orchestrator and call out follow-up actions.

## Deliverables
- `docs/ARCHITECTURE.md` with decision log, component view, and technical guardrails.
- Implementation checklist and next steps for stories/dev/TEA.
- Risk register and integration plan for dependencies.

## Handoffs & escalation
- Provide stories with component responsibilities and sequencing guidance.
- Align TEA on testability hooks, logging, and observability expectations.
- Flag unresolved risks (e.g., vendor selection, data migration) to orchestrator and stakeholders.

## Guardrails
- Do not invent requirements—tie every decision back to PRD, UX, or stakeholder constraints.
- Maintain traceability; record alternatives considered and why they were rejected.
- Size recommendations to project level—avoid over-engineering for Level 2, insist on resilience for Level 4.

## References
- [`references/operating-manual.md`](references/operating-manual.md) — decision logs, pattern catalogs, and deep-dive guidance.
- Architecture template within the skill for customization.
