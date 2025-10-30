# Workflow — Discovery to Planning Handoff

This skill replaces the BMAD Analyst → PM handoff pipeline by capturing all planning steps in one reusable procedure.

1. **Readiness Gate** (former Orchestrator check)
   - Verify discovery-analysis delivered goal statement, personas, research findings, and open questions log.
   - Confirm stakeholders approved moving to planning.

2. **Scope Synthesis** (former Analyst recap)
   - Summarize goals, constraints, and target users.
   - Classify project level (L2-L4) to size requirements appropriately.

3. **Requirements Authoring** (former PM core flow)
   - Populate PRD template sections (goals, background, FR/NFR, journeys, success metrics, out-of-scope).
   - Document assumptions and dependencies with traceability to discovery artifacts.

4. **Epic Roadmap Construction** (former PM epics handoff)
   - Break scope into epics with objective statement, sequencing rationale, and estimated story counts.
   - Note readiness signals for UX, architecture, and delivery-planning skills.

5. **Quality Review & Publication**
   - Run `CHECKLIST.md`.
   - Generate artifacts via `scripts/generate_prd.py` when data is structured.
   - Register deliverables with orchestrator/state tracking if present.
