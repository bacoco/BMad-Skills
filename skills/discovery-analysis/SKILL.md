---
name: bmad-discovery-analysis
description: Clarifies ambiguous opportunities through structured research, synthesis, and risk surfacing.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Discovery Analysis Skill

## Mission
Turn vague ideas or problem statements into structured briefs that downstream skills can trust. Identify goals, constraints, risks, and unknowns to inform product planning.

## Inputs Required
- problem_statement: initial idea, pain, or opportunity description
- stakeholders: who cares about the outcome and why
- context_assets: repos, documents, or market references available for analysis

If essential context is missing, gather it before deeper synthesis.

## Outputs
- Discovery brief following patterns in `REFERENCE.md`
- Prioritized questions and risk register captured for product-requirements skill
- Recommendation on readiness to progress or need for further discovery

## Process
1. Validate entry criteria in `CHECKLIST.md` and classify project complexity.
2. Conduct desk research across provided assets; cite sources.
3. Frame insights into concise problem summary, goals, personas, and constraints.
4. Document open questions, assumptions, and risks with recommended owners.
5. Deliver summary plus links to created artifacts for the orchestrator and stakeholders.

## Quality Gates
Confirm `CHECKLIST.md` is satisfied before signaling readiness for planning. Missing data or low confidence requires escalation.

## Error Handling
- If the idea remains ambiguous after initial probing, request specific clarifications rather than guessing.
- Flag conflicting stakeholder goals and recommend alignment conversations.
- When scope is too small (Level 0-1), suggest redirecting to lighter-weight workflows documented in `REFERENCE.md`.
