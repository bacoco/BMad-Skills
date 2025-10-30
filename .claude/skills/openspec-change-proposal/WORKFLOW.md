# Workflow — OpenSpec Proposal

1. **Scope Check**
   - Confirm change qualifies as Level 0-1 (small, low risk, limited blast radius).

2. **Scaffold Workspace**
   - Run `scripts/scaffold_change.py <change-id>` to create `openspec/changes/<change-id>/`.
   - Populate proposal, tasks, and spec delta files from templates.

3. **Context Capture**
   - Record current behavior, desired outcome, and affected surfaces.
   - Collect quick feasibility notes (logs, reproduction steps, constraints).

4. **Proposal Drafting**
   - Use `assets/proposal-template.md.template` to capture summary and acceptance signals.
   - Outline tasks using `assets/tasks-template.md.template` and fill `specs/spec-delta.md` for requirement changes.

5. **Review Prep**
   - Document risks, approvals, and follow-up questions.
   - Recommend reviewers or next skills if escalation is needed.

6. **Handoff**
   - Share proposal/tasks with stakeholders and orchestrator for scheduling.
