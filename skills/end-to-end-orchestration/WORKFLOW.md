# Workflow — BMAD Phase Coordination

1. **Scope Assessment**
   - Classify level (0-4) and confirm objectives.
   - Decide whether to proceed with BMAD skills or redirect to OpenSpec.

2. **State Initialization**
   - Run `scripts/workflow_status.py init` when workflow tracking is missing.
   - Seed sprint tracking via `scripts/sprint_status.py` once epics exist.

3. **Gate Review**
   - Inspect required artifacts for the current phase using each skill's `CHECKLIST.md`.
   - Highlight blockers or missing approvals.

4. **Routing Decision**
   - Recommend the next skill (discovery-analysis, product-requirements, etc.) and specify required inputs.
   - Communicate follow-up tasks and open risks.

5. **Status Update**
   - Record artifacts, completion, and status transitions using helper scripts.
   - Summarize progress for stakeholders and schedule next checkpoint.
