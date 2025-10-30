# Skill Activation Regression Suite

Use these scripted dialogues to verify that conversational triggers activate the correct skills. Each scenario should be replayed after updating manifest descriptions or skill contracts.

---

## Test 1 – New Idea → Analyst
**Goal:** Confirm that a fresh idea activates `bmad-discovery-research` automatically.

**User prompts:**
1. “I have an idea for a budgeting app that helps students.”
2. “Help me explore the best way to position it.”

**Expected behavior:**
- Claude announces the analyst skill.
- Outputs discovery questions, market research angles, and problem framing.

---

## Test 2 – PRD Creation
**Goal:** Verify that requirement planning routes to `bmad-product-planning`.

**User prompts:**
1. “Create a PRD for the budgeting app we just discussed.”
2. “Outline epics and critical success metrics.”

**Expected behavior:**
- Claude announces BMAD PM.
- Generates `PRD.md` with sections for goals, features, metrics, and open questions.

---

## Test 3 – Architecture Design
**Goal:** Ensure architecture requests switch to `bmad-architecture-design`.

**User prompts:**
1. “Design the system architecture for the budgeting app.”
2. “Recommend the tech stack and integrations.”

**Expected behavior:**
- Claude announces BMAD Architecture.
- Produces an architecture summary, component breakdown, and risk assessment.

---

## Test 4 – Development Execution
**Goal:** Confirm that implementation commands trigger `bmad-development-execution`.

**User prompts:**
1. “Implement the login story from the PRD.”
2. “Provide code snippets and unit tests.”

**Expected behavior:**
- Claude announces BMAD Dev.
- Supplies skeleton code, test cases, and follow-up steps.

---

## Test 5 – Testing Strategy
**Goal:** Validate that testing questions activate `bmad-test-strategy`.

**User prompts:**
1. “Create a test plan for the subscription flow.”
2. “List ATDD scenarios and automation priorities.”

**Expected behavior:**
- Claude announces BMAD Test & QA.
- Delivers a test strategy, coverage checklist, and QA timeline.

---

## Test 6 – Story Breakdown
**Goal:** Confirm `bmad-story-planning` handles backlog decomposition.

**User prompts:**
1. “Break the analytics epic into developer stories.”
2. “Include acceptance criteria for each story.”

**Expected behavior:**
- Claude announces BMAD Stories.
- Produces story files or structured backlog entries with acceptance criteria.

---

## Test 7 – Orchestrator Status Check
**Goal:** Ensure `bmad-workflow-router` auto-responds to status inquiries.

**User prompts:**
1. “Where am I in the BMAD workflow?”
2. “What should we do next?”

**Expected behavior:**
- Claude announces BMAD Orchestrator.
- Reads `workflow-status.md`, summarizes progress, and proposes the next phase.

---

## Test 8 – OpenSpec Quick Change
**Goal:** Verify that Level 0–1 changes activate the OpenSpec skills.

**User prompts:**
1. “Draft a quick fix for the login button bug.”
2. “Apply the change and archive it once tests pass.”

**Expected behavior:**
- Claude sequentially announces `openspec-change-proposal`, `openspec-change-implementation`, and `openspec-change-closure`.
- Creates proposal, implementation notes, and archival summary under `openspec/changes/<id>/`.

---

## Result Template
Use the following table to record the outcome of each run:

| Test | Status | Notes |
|------|--------|-------|
| 1 | ✅/❌ | |
| 2 | ✅/❌ | |
| 3 | ✅/❌ | |
| 4 | ✅/❌ | |
| 5 | ✅/❌ | |
| 6 | ✅/❌ | |
| 7 | ✅/❌ | |
| 8 | ✅/❌ | |

Document any failures and attach transcripts so the trigger lists can be updated accordingly.
