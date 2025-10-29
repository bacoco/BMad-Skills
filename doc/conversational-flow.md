# Conversational Flow Playbook

This playbook illustrates how Claude should auto-activate BMAD skills through natural dialogue.

---

## Scenario 1 – Idea → PRD → Architecture → Implementation

### Conversation Snapshot
- **User:** “I have an idea for a budgeting app that helps young professionals track daily expenses.”
- **Claude:** Auto-activates `bmad-analyst` → runs a brainstorming session, captures goals, pain points, and differentiators.
- **User:** “Great, can you create the PRD?”
- **Claude:** Switches to `bmad-pm`, generates `PRD.md`, outlines epics, and updates `workflow-status.md`.
- **User:** “Design the architecture so we can start building.”
- **Claude:** Activates `bmad-architecture`, produces an architecture document with components, integrations, and risks.
- **User:** “Let’s implement the login story.”
- **Claude:** Hands off to `bmad-dev`, delivers code templates and testing notes.

### Key Triggers
- Idea phrases: “I have an idea,” “Help me brainstorm.”
- PRD phrases: “Create a PRD,” “Plan this product.”
- Architecture phrases: “How should we build it,” “Design the system.”
- Implementation phrases: “Implement story #,” “Let’s code.”

---

## Scenario 2 – Mid-Project Check-in

### Conversation Snapshot
- **User:** “What’s next for our e-commerce project?”
- **Claude:** `bmad-orchestrator` reviews `workflow-status.md`, reports completed phases, and recommends the next step.
- **User:** “We need UX flows before development continues.”
- **Claude:** Activates `bmad-ux`, delivers wireframe guidance and user journeys.
- **User:** “Break the checkout epic into developer stories.”
- **Claude:** Switches to `bmad-stories`, produces story files with acceptance criteria.

### Key Triggers
- Status phrases: “Where am I,” “What’s next,” “Give me an update.”
- UX phrases: “Design the UX,” “Sketch the interface.”
- Story phrases: “Break into stories,” “Create developer tasks.”

---

## Scenario 3 – Quality Assurance Focus

### Conversation Snapshot
- **User:** “How should we test the subscription flow?”
- **Claude:** `bmad-tea` activates, generates a test strategy with ATDD notes.
- **User:** “Run through the plan and confirm coverage gaps.”
- **Claude:** Summarizes coverage, flags missing integration tests, and recommends regression steps.
- **User:** “Let’s archive the results once QA signs off.”
- **Claude:** Uses `openspec-archive` if this is a Level 0–1 change or instructs the BMAD workflow to mark the phase complete.

### Key Triggers
- Testing phrases: “How do we test,” “Create a test plan,” “ATDD strategy.”
- Coverage phrases: “Confirm coverage,” “Review the test plan.”
- Archival phrases: “Archive the change,” “Close out the work.”

---

## Scenario 4 – OpenSpec Quick Change

### Conversation Snapshot
- **User:** “Draft a quick fix for the login error users reported.”
- **Claude:** `openspec-propose` activates, creates a proposal with scope, risks, and validation steps.
- **User:** “Looks good—apply the change.”
- **Claude:** Switches to `openspec-implement`, outlines the code edits and test updates.
- **User:** “Archive the change once tests pass.”
- **Claude:** Uses `openspec-archive`, records final notes under `openspec/changes/<id>/`.

### Key Triggers
- Quick fix phrases: “Quick fix,” “Small change,” “Minor update.”
- Implementation phrases: “Apply the change,” “Implement the proposal.”
- Archive phrases: “Archive change <id>,” “Close the change.”

---

## Guidance for Designers
- Document new trigger phrases as they emerge and propagate them to `meta/MANIFEST.json` and the relevant `SKILL.md` files.
- Verify that each skill announces itself during activation to help users understand the transition.
- Encourage users to provide context when switching phases: “We already finished the PRD—start UX.”
- Capture transcripts of failed activations and add them as regression scenarios in `tests/test_skill_activation.md`.

Keep this playbook updated after every major release or trigger revision.
