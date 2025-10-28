---
name: openspec-archive
description: Proactively activates after OpenSpec changes are deployed. Archives completed changes and updates living specifications. (user)
version: 1.0.0
source: OpenSpec by Fission-AI (https://github.com/Fission-AI/OpenSpec)
attribution: Based on OpenSpec workflow - Stage 3 (Archiving Changes)
---

# OpenSpec Archive Quick Guide

Stage 3 skill for closing out OpenSpec changes.

## Role Snapshot
- Confirm deployment success and capture evidence.
- Move change artifacts into the archive structure.
- Update living specs and changelog entries.

## Fast Start
1. Validate that proposal + tasks were completed and tests passed.
2. Ask for deployment confirmation (environment, timestamp, approver).
3. Summarize the implemented delta and update reference docs/spec files.
4. Archive the change folder (`openspec/changes/<name>/`) per playbook.
5. Announce closure and note any follow-up tasks or regressions to watch.

## Trigger Conditions
Use when user says the change is live, wants to document completion, or needs to tidy OpenSpec state.

## Guardrails
- Block if implementation evidence or approvals are missing.
- Preserve history—never delete proposals/tasks; move them per archive steps.
- Encourage quick post-deployment validation and monitoring notes.

## References (load as needed)
- [`references/operating-manual.md`](references/operating-manual.md) – Detailed archive workflow, folder structure, and spec update checklist.

Stay concise unless the user requests the full archive checklist.
