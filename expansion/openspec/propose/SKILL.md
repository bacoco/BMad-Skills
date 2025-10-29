---
name: openspec-propose
description: Frames lightweight change proposals for Level 0-1 work using OpenSpec methodology.
version: 1.1.0
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
- `proposal.md` summarizing problem, desired behavior, and acceptance signals
- `tasks.md` listing actionable steps sized for rapid implementation
- Next-step recommendation for review or direct execution

## Process
1. Validate Level 0-1 scope using `CHECKLIST.md`.
2. Clarify current vs. target behavior and record any quick feasibility notes.
3. Draft proposal and task list using patterns in `REFERENCE.md` and templates in `assets/`.
4. Highlight dependencies, approvals, and risks.
5. Hand off to reviewers or orchestration for scheduling.

## Quality Gates
Ensure checklist items pass before finalizing. Escalate to BMAD if scope exceeds Level 1 or introduces major unknowns.

## Error Handling
- If information is insufficient, ask for missing context (screenshots, logs, reproduction steps).
- When risks are high or ambiguity remains, recommend migrating to BMAD discovery-analysis.
