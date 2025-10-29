---
name: bmad-development-execution
description: Delivers code changes for ready stories with rigorous testing, documentation, and BMAD governance.
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# Development Execution Skill

## Mission
Implement approved stories end-to-end, maintaining transparency, testing discipline, and traceability back to requirements and architecture decisions.

## Inputs Required
- story: developer-ready story file from delivery-planning skill
- architecture_refs: relevant sections of ARCHITECTURE.md or component notes
- ux_guidance: UX specs or validations tied to the story
- quality_plan: scenarios or gates supplied by quality-assurance skill

## Outputs
- Code diffs and test results captured in the working repository
- Updated story file (Dev Agent Record, status transitions, learnings)
- Summary of changes, tests, and outstanding risks for stakeholders

## Process
1. Confirm prerequisites via `CHECKLIST.md` and restate story scope.
2. Plan implementation steps, identifying affected files and tests.
3. Apply small, reviewable code changes with explanations and references.
4. Execute required test suites and capture command output verbatim.
5. Update story documentation, including Dev Agent Record and status.
6. Summarize work, highlight follow-ups, and notify orchestrator for next steps.

## Quality Gates
All items in `CHECKLIST.md` must pass before code is considered complete. Never mark a story done without full testing evidence.

## Error Handling
If prerequisites or environments are missing:
- Halt implementation, document the specific blocker, and notify orchestrator.
- Provide recommended remediation steps (e.g., refresh artifacts, fix failing baseline tests).
- Avoid speculative changes; keep diffs scoped to the approved story.
