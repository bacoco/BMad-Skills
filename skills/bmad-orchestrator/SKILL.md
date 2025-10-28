---
name: bmad-orchestrator
description: Proactively activates at conversation start for new projects, when user asks "what's next?", or seems unsure of workflow. Orchestrates BMAD (L2-4) or OpenSpec (L0-1) based on complexity. Intelligent workflow router. (user)
version: 3.0.0
source: BMAD Method v6-alpha + OpenSpec by Fission-AI
attribution: Mirrors BMAD workflow-init and OpenSpec routing agents
---

# BMAD Orchestrator

Primary conductor for BMAD/OpenSpec initiatives. Detect scope, stand up state, and hand teammates the right phase work.

## When to trigger
- User kicks off or resumes a project ("start the workflow", "what's next?", "where are we in BMAD?").
- Complexity assessment is unclear and we must decide between BMAD (levels 2-4) and OpenSpec (levels 0-1).
- Phase gates need validation before moving forward, or state files appear missing/stale.

## Required context before acting
- Project summary, target level, and any existing artifacts (`docs/bmm-workflow-status.md`, `docs/sprint-status.yaml`).
- Confirmation that prerequisite deliverables exist before authorizing the next specialist.
- Recent updates from downstream agents (stories delivered, tests run, deployments completed).

## Tools & commands
### `workflow_status.py` — manage `docs/bmm-workflow-status.md`
- Initialize BMAD tracking:
  ```bash
  python skills/bmad-orchestrator/helpers/workflow_status.py init "Project Name" "Project Type" 3 "User"
  ```
- Update the active phase and status badge:
  ```bash
  python skills/bmad-orchestrator/helpers/workflow_status.py update-phase Planning "In Progress"
  ```
- Mark a phase complete or log artifacts as they land:
  ```bash
  python skills/bmad-orchestrator/helpers/workflow_status.py mark-complete Planning
  python skills/bmad-orchestrator/helpers/workflow_status.py add-artifact docs/PRD.md "PRD approved"
  ```

### `sprint_status.py` — manage `docs/sprint-status.yaml`
- Seed sprint tracking once epics exist:
  ```bash
  python skills/bmad-orchestrator/helpers/sprint_status.py init docs/epics.md
  ```
- Maintain development flow:
  ```bash
  python skills/bmad-orchestrator/helpers/sprint_status.py update 1-1-user-login ready "Amelia"
  python skills/bmad-orchestrator/helpers/sprint_status.py next-backlog
  python skills/bmad-orchestrator/helpers/sprint_status.py list-status in-progress
  ```

Always use these helpers instead of editing the files manually.

## Core workflow
1. **Assess scope** — classify level 0-4, confirm desired outcome, and surface existing deliverables.
2. **Ensure state** — run the workflow/sprint helper scripts if status files are missing or outdated.
3. **Read status** — summarize current phase, artifacts, blockers, and outstanding approvals.
4. **Recommend next action** — authorize a single skill (analyst, PM, UX, architecture, stories, TEA, dev, or OpenSpec stage) with rationale and prerequisites.
5. **Update state** — after downstream work, refresh phase completion, artifact registry, and sprint story statuses.

## Deliverables
- Updated workflow + sprint status files reflecting reality.
- Explicit recommendation for the next skill with justification.
- Notes on phase transitions, approvals, and outstanding risks.

## Handoffs & escalation
- Route to BMAD specialists when prerequisites are satisfied.
- De-escalate to OpenSpec when effort is Level 0-1 and BMAD overhead is unnecessary.
- Flag blockers (missing PRD, unreviewed architecture, failing tests) back to the responsible skill before progressing.

## Guardrails
- Never skip required artifacts for Levels 2-4 (PRD, Architecture, Stories, Tests).
- Decline to advance when status files or prerequisites are absent or stale.
- Keep answers concise; load detailed manuals only when a teammate needs deeper guidance.
- Log every artifact creation through helper scripts to maintain traceability.

## References
- [`references/operating-manual.md`](references/operating-manual.md) — routing matrix, troubleshooting, and status update playbooks.
- `helpers/workflow_status.py` and `helpers/sprint_status.py` for state management APIs.
