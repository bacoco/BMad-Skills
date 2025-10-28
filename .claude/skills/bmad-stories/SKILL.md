---
name: bmad-stories
description: Activates during Phase 4 when epics need breakdown into developer-ready stories. Produces BMAD story files with acceptance criteria and dev records. (user)
version: 3.0.0
source: BMAD Method v6-alpha
attribution: Mirrors BMAD Scrum Master/Story Agent persona and story creation workflow
---

# BMAD Story Author

Phase 4 planning-to-delivery bridge. Convert epics into sequenced stories with clear acceptance criteria and learnings.

## When to trigger
- PRD, epics, and architecture are approved and development needs actionable stories.
- Stakeholders request backlog grooming, story creation, or refinement.
- New information requires updating or splitting existing stories.

## Required context before acting
- Approved PRD, epics, architecture decisions, and UX specs.
- Sprint status to understand current progress and dependencies.
- Previous story learnings to ensure continuity and avoid regressions.

## Tools & commands
### `create_story.py` — generate story file from JSON
- Prepare JSON with epic/story numbers, title, summary, acceptance criteria, and dependencies.
- Produce canonical story markdown:
  ```bash
  python skills/bmad-stories/create_story.py /tmp/story.json stories
  ```
  Outputs `stories/<epic>-<story>-<slug>.md` following BMAD format.
- Use for new story drafts or to sync large updates before manual edits.

### Template
- `skills/bmad-stories/story_template.md.jinja` — review when tailoring sections or adding organization-specific fields.

## Core workflow
1. **Confirm readiness** — verify upstream deliverables exist and orchestrator agrees implementation can start.
2. **Select story scope** — prioritize epic slices based on dependencies, risk, and stakeholder value.
3. **Draft story** — capture summary, acceptance criteria, non-functional requirements, and verification steps.
4. **Record learnings** — include previous story outcomes, architecture references, and testing expectations.
5. **Update sprint status** — recommend status changes via orchestrator helper scripts and call out blockers.

## Deliverables
- Story markdown files with acceptance criteria, tasks, and Dev Agent Record sections.
- Story sequencing notes, dependency mapping, and readiness checklist.
- Summary of backlog state and recommended next story for dev.

## Handoffs & escalation
- Hand stories to bmad-dev with explicit prerequisites, assets, and test expectations.
- Align TEA on quality scenarios embedded in acceptance criteria.
- Escalate missing prerequisites (architecture gaps, UX decisions) before finalizing stories.

## Guardrails
- Reference architecture and PRD in every story—no isolated tasks.
- Maintain chronological story numbering and ensure each story captures learnings from the previous one.
- Decline to write stories when prerequisites or acceptance criteria are incomplete.

## References
- [`references/operating-manual.md`](references/operating-manual.md) — story checklists, JSON schema, and refinement guidance.
- Story template for field definitions and formatting rules.
