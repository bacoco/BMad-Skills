---
name: bmad-stories
description: Proactively activates when user says "break this into stories", "create user stories", or wants to prepare development work. Creates developer-ready story files following BMAD standards. Requires PRD and Architecture. (user)
version: 2.1.0
source: BMAD Method v6-alpha (https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)
attribution: Based on BMAD Scrum Master Agent persona and Create Story workflow
---

# BMAD Stories Quick Guide

Phase 4 story authoring skill. Turn epics into developer-ready stories with continuity.

## Role Snapshot
- Generate story files in `stories/` with acceptance criteria and Dev Agent Record headers.
- Pull learnings from the previous story to maintain continuity.
- Map each task back to PRD + architecture decisions.

## Fast Start
1. Confirm epics exist and orchestrator signals implementation phase entry.
2. Identify the next story (epic/story numbering) and read previous story learnings.
3. Draft acceptance criteria first, then outline tasks + test expectations.
4. Capture dependencies, references, and cross-links to architecture + testing artifacts.
5. Save the story file and update workflow status with story queue state.

## Trigger Conditions
Invoke when user asks to create or refine developer stories/backlog items post-planning.

## Guardrails
- Never skip "Learnings from Previous Story"; fetch context or block until available.
- Keep stories actionable: each acceptance criterion must map to tasks and tests.
- Escalate missing architecture/test plans before generating new stories.

## References (load as needed)
- [`references/operating-manual.md`](references/operating-manual.md) – Story templates, continuity checklist, and numbering rules.

Default to lightweight guidance; open the manual when you need the full template or auditing instructions.
