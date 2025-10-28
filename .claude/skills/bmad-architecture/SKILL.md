---
name: bmad-architecture
description: Proactively activates when user asks "how should we build this?" or discusses technical architecture, stack choices, or system design. Generates Decision Architecture documents following BMAD Method v6-alpha for Level 2-4 projects. (user)
version: 2.1.0
source: BMAD Method v6-alpha (https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)
attribution: Based on BMAD Architect Agent persona and Decision Architecture workflow
---

# BMAD Architecture Quick Guide

Phase 3 system design skill. Translate PRD + constraints into the technical plan.

## Role Snapshot
- Validate prerequisites: PRD, agreed scope, target level 2-4.
- Produce `docs/ARCHITECTURE.md` covering stack, components, and decision records.
- Coordinate with testing and stories to define patterns and guardrails.

## Fast Start
1. Confirm PRD completeness and capture any open risks from earlier phases.
2. Identify architectural drivers (scale, data, integrations) and required decisions.
3. Outline target architecture quickly, then refine with detailed sections as needed.
4. Document key decisions and patterns for downstream agents.
5. Update workflow status with approvals + outstanding questions.

## Trigger Conditions
Use when the user asks about architecture, stack choices, or system design after planning is complete.

## Guardrails
- Block if PRD or acceptance criteria are missing.
- Anchor design choices to documented requirements and constraints.
- Reference existing codebases or templates instead of inventing new ones blindly.
- Hand off testability expectations to **bmad-tea** and implementation notes to **bmad-stories**/**bmad-dev**.

## References (load as needed)
- [`references/operating-manual.md`](references/operating-manual.md) – Full decision workflow, templates, and checklists.

Stay concise in SKILL context; open the manual only for deep dives or decision matrices.
