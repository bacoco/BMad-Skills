---
name: openspec-archive
description: Closes out Level 0-1 OpenSpec work with documentation, learnings, and deployment notes.
version: 1.1.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# OpenSpec Archive Skill

## Mission
Document the outcome of Level 0-1 work, ensuring artifacts, approvals, and follow-up actions are captured before closing the OpenSpec workflow.

## Inputs Required
- proposal: original proposal.md with approvals
- implementation_log: execution notes or commits from implement skill
- validation_evidence: test results or reviewer feedback

## Outputs
- Archive summary (e.g., `archive.md`) with outcomes, metrics, and learnings
- Updated proposal/tasks reflecting completion status
- Deployment or rollback notes stored with project documentation

## Process
1. Verify closure conditions using `CHECKLIST.md`.
2. Gather final state: what shipped, what remains, and any deviations.
3. Record metrics, approvals, and validation evidence.
4. Capture learnings and recommended follow-up actions.
5. Update artifacts and communicate closure to stakeholders or orchestrator.

## Quality Gates
All checklist items must pass before marking work as archived.

## Error Handling
- If validation evidence or approvals are missing, request them before closing.
- Surface outstanding tasks and assign owners if work cannot be fully archived.
