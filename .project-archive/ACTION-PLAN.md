# IMMEDIATE ACTION PLAN – BMAD Skills Activation Fixes

**Objective:** Raise the activation score from 85/100 to 95/100 within three days.  
**Focus:** Deliver automatic conversational activation that matches the Bimath methodology.

---

## DAY 1 – Conversational Descriptions and Manifest Updates

### Task 1.1 – Update `meta/MANIFEST.json`
**Goal:** Replace every technical description with the conversational version listed below.

| Skill ID | Conversational Description |
|----------|----------------------------|
| `bmad-orchestrator` | "BMAD workflow orchestrator. Auto-invokes at conversation start. Tracks status and guides through phases. Invoke when users say 'start project', 'what's next', 'where am I', 'status', 'initialize', or when any BMAD work begins implicitly. Keywords: status, workflow, next, start, guide, phase, where, initialize." |
| `bmad-analyst` | "Brainstorms ideas and researches projects. Invoke when users say 'I have an idea', 'What if we', 'Help me think', 'Explore possibilities', 'I'm thinking about', 'brainstorm', 'research'. Keywords: idea, brainstorm, explore, research, thinking, new project, discovery." |
| `bmad-pm` | "Creates PRDs and plans features. Invoke when users say 'I want to build', 'Create a PRD', 'Plan this feature', 'Write requirements', 'Product document'. Keywords: PRD, requirements, plan, build, feature, epic, roadmap, product." |
| `bmad-ux` | "Designs UX and produces wireframes. Invoke when users ask 'What should the UI look like', 'Design the UX', 'User experience', 'Wireframes', 'User flow'. Keywords: UX, UI, design, wireframe, user flow, interface, usability." |
| `bmad-architecture` | "Produces technical architecture. Invoke when users ask 'How should we build', 'What's the architecture', 'Tech stack', 'System design', 'How do we build this'. Keywords: architecture, tech stack, design, system, build, technical, structure." |
| `bmad-tea` | "Creates the test strategy. Invoke when users say 'How should we test', 'Create a test strategy', 'Test plan', 'ATDD', 'Quality assurance'. Keywords: test, testing, strategy, QA, quality, ATDD, automation." |
| `bmad-stories` | "Breaks epics into developer stories. Invoke when users say 'Break into stories', 'Create user stories', 'Story breakdown', 'Developer tasks'. Keywords: story, stories, epic, breakdown, task, backlog, sprint." |
| `bmad-dev` | "Implements stories with code and tests. Invoke when users say 'Implement the story', 'Develop this', 'Let's code', 'Write the code', 'Start coding'. Keywords: implement, code, develop, build, program, coding, implementation." |
| `skill-creator` | "Creates and validates new skills. Invoke when users say 'Create a skill', 'New skill', 'Validate skill', 'Package skill'. Keywords: skill, create skill, new skill, validate." |
| `openspec-propose` | "Drafts lightweight change proposals for Level 0–1 work. Invoke when users say 'Small change', 'Bug fix', 'Quick feature', 'Propose a change'. Keywords: propose, change, proposal, lightweight, Level 0, Level 1." |
| `openspec-implement` | "Implements Level 0–1 changes. Invoke when users say 'Implement this change', 'Execute proposal', 'Apply the change'. Keywords: implement, execute, apply, change, Level 0, Level 1." |
| `openspec-archive` | "Archives completed Level 0–1 changes. Invoke when users say 'Archive this change', 'Close this change', 'Document the change'. Keywords: archive, close, document, complete, change." |

**Estimated time:** 30 minutes.

---

### Task 1.2 – Add “When to Invoke” to `bmad-orchestrator/SKILL.md`
**File:** `.claude/skills/bmad-orchestrator/SKILL.md`

Insert the following after the YAML front matter and before `# End-to-End Orchestration Skill`:

```markdown
## When to Invoke

**Always auto-invoke at the start of any BMAD project:**
- User says "start project", "new project", "initialize BMAD", or "begin".
- User asks "what's next?", "where am I?", "check status", or "workflow status".
- User begins describing a product idea without referencing BMAD explicitly.
- The conversation starts in a product development context.
- User requests guidance on the overall development process.

**Special automated behaviors:**
- If `workflow-status.md` does not exist → run the initialization workflow automatically.
- If `workflow-status.md` exists → read the current status and recommend the next action.
- If the user mentions a specific phase → route to the corresponding skill.
- During mid-project conversations → verify phase completion and suggest the next step.

**Do not invoke when:**
- The user explicitly calls for a different skill.
- The user is actively implementing code (leave control to `bmad-dev`).
- The user is asking unrelated technical questions.
```

**Estimated time:** 15 minutes.

Repeat this pattern for every BMAD skill (analyst, pm, ux, architecture, tea, stories, dev) using the trigger lists from `REFERENCE.md`. Each insertion should stay under 200 words and highlight trigger phrases, keywords, and situations to avoid.

**Estimated time:** 4 hours total for all skills.

---

## DAY 2 – Scenario Documentation and Orchestrator Enhancements

### Task 2.1 – Consolidate Activation Guidance
**Goal:** Move the activation snippets from every `REFERENCE.md` into the new “When to Invoke” sections, keeping reference files focused on deep knowledge.

**Steps:**
1. Copy the relevant activation bullets (not the entire prose) from each reference file.
2. Integrate them into the corresponding `SKILL.md` section created on Day 1.
3. Leave advanced routing matrices in `REFERENCE.md` under an “Advanced Activation Patterns” heading.

**Estimated time:** 1 hour.

### Task 2.2 – Upgrade `bmad-orchestrator`
**File:** `.claude/skills/bmad-orchestrator/SKILL.md`

Add a new section after “When to Invoke” titled `## Default Behaviors` that covers:
- Auto-start behavior on any BMAD conversation.
- How to hand off to downstream skills when phases complete.
- Guardrails for not double-invoking active skills.
- Escalation path when a required artifact is missing.

**Estimated time:** 30 minutes.

### Task 2.3 – Document Conversational Flow
**File:** `doc/conversational-flow.md`

Create or update scenario walkthroughs that show:
- Natural-language triggers for each BMAD phase.
- Expected auto-activation order (idea → analysis → PRD → UX → architecture → dev → QA → release).
- Recovery behavior when users change direction mid-conversation.

**Estimated time:** 1.5 hours.

---

## DAY 3 – Testing and Troubleshooting Assets

### Task 3.1 – `tests/test_skill_activation.md`
**Goal:** Provide regression tests describing at least five conversational scripts. Each scenario should capture:
- The user utterances.
- Expected skill activations.
- Confirmation that artifacts (PRD, architecture, stories, etc.) are produced when required.

**Estimated time:** 2 hours.

### Task 3.2 – Troubleshooting Guide Refresh
**File:** `doc/troubleshooting.md`

Ensure the guide explains:
- How to phrase prompts that reliably trigger each skill.
- How to correct Claude when the wrong skill activates.
- How to debug missing artifacts or skipped phases.
- How to differentiate BMAD versus OpenSpec routes.

**Estimated time:** 1 hour.

### Task 3.3 – Quickstart and FAQ Review
**Files:** `doc/quickstart-conversational.md`, `doc/activation-faq.md`

Update both documents so new users understand:
- The difference between manual invocation and auto-activation.
- Example prompts for each skill.
- The fallback commands if auto-routing fails.

**Estimated time:** 1 hour.

---

## CHECKLIST FOR COMPLETION

- [ ] `meta/MANIFEST.json` uses conversational descriptions for all twelve skills.
- [ ] Every `SKILL.md` contains a concise “When to Invoke” section.
- [ ] `bmad-orchestrator` documents default auto-routing behaviors.
- [ ] Scenario documentation illustrates natural BMAD conversations.
- [ ] Regression scripts verify automatic activation across phases.
- [ ] Troubleshooting, FAQ, and quickstart docs explain conversational prompts in plain English.

**Success Criteria:** Automatic activation flows behave as described, stakeholders understand how to use the system conversationally, and the follow-up audit confirms a score of 95/100 or higher.
