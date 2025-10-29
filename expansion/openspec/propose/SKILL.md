---
name: openspec-propose
description: Frames lightweight change proposals for Level 0-1 work using OpenSpec methodology.
version: 1.2.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# OpenSpec Propose Skill

## Mission
Capture small change requests or bug fixes and translate them into concise proposals and task outlines without invoking the full BMAD workflow.

## Inputs Required
- change_request: description of the existing behavior and desired adjustment
- impact_surface: files, services, or user flows likely affected
- constraints: timeline, risk, or approvals that bound the solution

## Outputs
- `proposal.md` summarizing problem, desired behavior, and acceptance signals (template: `assets/proposal-template.md`)
- `tasks.md` listing actionable steps sized for rapid implementation (template: `assets/tasks-template.md`)
- `specs/spec-delta.md` capturing ADDED/MODIFIED/REMOVED requirements (template: `assets/spec-delta-template.md`)
- Optional `design.md` scaffolded when deeper technical notes are required

`scripts/scaffold_change.py` creates this structure in `openspec/changes/<change-id>/` using the templates above.

## Process
1. Validate Level 0-1 scope using `CHECKLIST.md`.
2. Run `scripts/scaffold_change.py <change-id>` to create the workspace under `openspec/changes/`.
3. Clarify current vs. target behavior and record feasibility notes in `proposal.md`.
4. Draft `tasks.md` and populate `specs/spec-delta.md` using the templates in `assets/`.
5. Highlight dependencies, approvals, and risks, then hand off for review or implementation scheduling.

## Quality Gates
Ensure checklist items pass before finalizing. Escalate to BMAD if scope exceeds Level 1 or introduces major unknowns.

## Error Handling
- If information is insufficient, ask for missing context (screenshots, logs, reproduction steps).
- When risks are high or ambiguity remains, recommend migrating to BMAD discovery-analysis.
