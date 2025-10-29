# Conversational Quickstart Guide

Learn how to trigger BMAD and OpenSpec skills through natural dialogue.

---

## 1. Start the BMAD workflow
- Say “I have an idea for…” or “Let’s start a new project.”
- Claude should auto-activate `bmad-orchestrator` or `bmad-analyst`.
- If nothing happens, ask “Start the BMAD workflow for me.”

## 2. Brainstorming and discovery (`bmad-analyst`)
- Prompts: “Help me brainstorm a fintech product,” “Explore the market for…,” “Research similar solutions.”
- Expected output: discovery notes, opportunity framing, clarified problem statement.

## 3. Product requirements (`bmad-pm`)
- Prompts: “Create a PRD for this idea,” “Plan the feature set,” “Write product requirements.”
- Expected output: `PRD.md`, roadmap sections, initial backlog.

## 4. Experience design (`bmad-ux`)
- Prompts: “Design the UX flow,” “Sketch the interface,” “What should the user journey look like?”
- Expected output: wireframe descriptions, user flows, annotated interface guidance.

## 5. Architecture (`bmad-architecture`)
- Prompts: “Design the system,” “What architecture should we use?,” “Choose the tech stack.”
- Expected output: architecture diagrams or text specs, component breakdowns, integration notes.

## 6. Testing strategy (`bmad-tea`)
- Prompts: “Create a test plan,” “How do we validate this?,” “Draft an ATDD strategy.”
- Expected output: test strategy document, coverage checklist, automation outline.

## 7. Story breakdown (`bmad-stories`)
- Prompts: “Break this epic into stories,” “Write developer stories for…,” “Create sprint-ready tasks.”
- Expected output: story files or backlog entries with acceptance criteria.

## 8. Implementation (`bmad-dev`)
- Prompts: “Implement story #5,” “Let’s code the login,” “Write the backend service.”
- Expected output: code snippets, test files, implementation notes.

## 9. OpenSpec change management
- Use when the scope is Level 0–1 (bug fix, small enhancement).
- Prompts:
  - `openspec-propose`: “Draft a quick fix for the login bug.”
  - `openspec-implement`: “Apply the change described in proposal 42.”
  - `openspec-archive`: “Archive change 42 with final notes.”

## 10. Staying on track
- Ask `bmad-orchestrator`: “Where am I in the workflow?”
- Use “What’s next?” to get the next recommended phase.
- Review `workflow-status.md` to confirm deliverables.

---

## Troubleshooting tips
- Lead with the action: “Create,” “Design,” “Implement,” “Test.”
- Name the artifact you expect: PRD, wireframe, story, proposal.
- Provide context: project name, target user, current phase.
- If the wrong skill activates, clarify immediately: “Use BMAD UX instead.”

Keep this quickstart visible while onboarding new team members or auditors.
