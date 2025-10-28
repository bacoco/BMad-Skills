---
name: openspec-implement
description: Proactively activates when user approves an OpenSpec proposal or says "implement the change". Executes tasks from approved OpenSpec proposals sequentially. (user)
version: 1.0.0
source: OpenSpec by Fission-AI (https://github.com/Fission-AI/OpenSpec)
attribution: Based on OpenSpec workflow - Stage 2 (Implementing Changes)
---

# OpenSpec Implement Quick Guide

Stage 2 skill for executing approved OpenSpec proposals.

## Role Snapshot
- Validate approval and prerequisites before touching code.
- Execute tasks sequentially, keeping diffs small and reviewed.
- Run/record tests and update proposal status as tasks complete.

## Fast Start
1. Confirm proposal + tasks exist and have explicit approval.
2. Review scope, affected files, and success criteria.
3. Implement tasks in order, committing intermediate progress as needed.
4. Run tests for each change; capture commands + results.
5. Update `tasks.md` with completion notes and summarize remaining work.

## Trigger Conditions
Invoke once the user says "implement" or approves a proposal.

## Guardrails
- Refuse to start if approval or tasks are missing.
- Keep within defined scope; route new ideas back to `openspec-propose`.
- Coordinate with archive stage when work is merged/deployed.

## References (load as needed)
- [`references/operating-manual.md`](references/operating-manual.md) – Detailed task execution workflow, testing matrix, and troubleshooting tips.

Stay focused on execution; open the manual when you need the full task checklist or remediation guidance.
