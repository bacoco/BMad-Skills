---
name: openspec-implement
description: Executes Level 0-1 change tasks defined by OpenSpec proposals with traceable testing evidence.
version: 1.2.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

# OpenSpec Implement Skill

## Mission
Apply small code or configuration changes approved via OpenSpec proposals, ensuring each task is executed transparently with testing evidence.

## Inputs Required
- proposal: latest proposal.md with decision history
- tasks: tasks.md with sequenced work items and owners
- environment: information about repositories, branches, and tooling needed for execution

## Outputs
- Code or configuration changes committed according to tasks
- Test results demonstrating acceptance criteria were met
- Updated proposal/tasks capturing status and follow-ups
- `execution-log.md` documenting commands and evidence (template: `assets/execution-log-template.md`)

`scripts/update_execution_log.py` appends timestamped entries to the execution log inside `openspec/changes/<change-id>/`.

## Process
1. Confirm scope and prerequisites via `CHECKLIST.md`.
2. Plan work referencing affected files and dependencies.
3. Implement tasks iteratively, documenting commands and results in `execution-log.md` via the script or manual edits.
4. Run relevant tests or validation steps after each change and capture evidence in the log.
5. Update artifacts and communicate completion or blockers.

## Quality Gates
All checklist items must pass. If complexity grows beyond Level 1, escalate back to BMAD pathways.

## Error Handling
- When prerequisites or environment setup are missing, stop and request clarity.
- If tests fail or scope expands, log findings and recommend next actions, including potential migration to BMAD development-execution.
