---
name: bmad-ux-blueprint
description: Converts requirements into UX flows, wireframes, and validation criteria sized to BMAD project levels.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# UX Blueprint Skill

## Mission
Design user experiences that align with BMAD requirements, documenting flows, interaction states, and validation plans that unblock architecture, delivery, and development.

## Inputs Required
- prd_sections: user journeys, functional requirements, constraints
- architecture_notes: technical or platform limits impacting UX
- brand_guidelines: accessibility, tone, device targets, or visual standards

## Outputs
- Annotated flows or wireframes stored alongside project docs
- UX requirements checklist linked to PRD and stories
- Validation plan (usability or experimentation) for quality-assurance alignment

## Process
1. Confirm prerequisites via `CHECKLIST.md`.
2. Clarify personas, scenarios, and surfaces requiring design.
3. Produce information architecture, flows, and state diagrams.
4. Document component specifications and content rules tied to requirements.
5. Define validation approach (tests, instrumentation, success signals) and share with delivery-planning and quality-assurance skills.

## Quality Gates
Ensure every UX decision traces back to requirements or constraints. Run `CHECKLIST.md` prior to handoff.

## Error Handling
- If requirements conflict or are missing, request clarification before designing.
- Flag technical limitations that impact user experience and loop architecture-design.
- Provide alternate recommendations when constraints prevent ideal UX outcomes.
