# Troubleshooting Guide – Conversational Activation

**Purpose:** Diagnose and resolve activation issues with BMAD skills.

---

## 🔍 Quick Diagnostic Matrix

| Symptom | Section |
|---------|---------|
| Claude does not activate any skill | [No Activation](#no-activation) |
| Claude activates the wrong skill | [Wrong Skill Activated](#wrong-skill-activated) |
| Skill stalls or refuses to continue | [Skill Stuck](#skill-stuck) |
| Tests fail | [Test Failures](#test-failures) |
| Expected artifacts are missing | [Missing Artifacts](#missing-artifacts) |
| A phase was skipped | [Skipped Phases](#skipped-phases) |
| Confusion between OpenSpec and BMAD | [Routing Confusion](#routing-confusion) |

---

## 🚫 No Activation

### Symptom
```
You: "Do something with the project."
Claude: "I'd be happy to help! Can you be more specific?"
[No skill activates]
```

### Possible Causes and Fixes

#### Cause 1 – Vague phrasing
- Problem: not enough keywords for intent detection.
- Ineffective prompts: “Work on this,” “Do something,” “Help me,” “Continue.”
- Solution: use **Action + Artifact + Context**, e.g., “Create a PRD for my budgeting app.”

#### Cause 2 – General technical question
- Problem: Claude answers directly without loading a skill.
- Normal behavior for: “What is Python?”, “How do I center a div?”
- To force a skill: “I want to build a Python microservice—design the architecture.”

#### Cause 3 – Missing context
- Problem: Claude does not know what to break down or build.
- Fix: add the object. “Break this epic into stories,” “Implement story #5 in the backlog.”

**General formula:** `[Action verb] + [Artifact] + [Project context]`.

---

## ⚠️ Wrong Skill Activated

### Symptom
```
You: "Break this down."
Claude: [Activates BMAD Analyst instead of BMAD Stories]
```

### Causes and Remedies

#### Case 1 – Ambiguous wording
- “Break down” may imply analysis or story slicing.
- Be explicit: “Break this epic into stories” or “Break down the problem for analysis.”

#### Case 2 – Dominant keyword
- Example: “I have an idea to implement story #5” → “idea” triggers Analyst.
- Rewrite: “Implement story #5 that we already scoped.”

#### Case 3 – Incorrect level detected
- Example: “Fix authentication” might trigger Architecture (Level 3).
- Clarify scope:
  - Quick bug: “Quick fix for the authentication bug” → OpenSpec Propose.
  - Full build: “Design a complete authentication system” → BMAD Architecture.

**Live correction:** tell Claude “Use BMAD Stories for this” and it will switch.

---

## 🧊 Skill Stuck

### Symptom
```
Claude: “Waiting for confirmation before continuing…”
```

### Fixes
- Confirm or provide the missing detail (“Yes, continue with the plan.”).
- Ask for a summary of what it needs: “What information is missing?”
- If the skill still stalls, hand control back to the orchestrator: “Resume BMAD workflow.”

---

## 🧪 Test Failures

- Ensure `tests/test_skill_activation.md` scenarios reflect the latest trigger phrases.
- Re-run scripted prompts after updating manifest descriptions or skill contracts.
- Capture transcripts whenever a regression occurs so the team can adjust the trigger list.

---

## 📦 Missing Artifacts

- Check whether the relevant skill actually activated.
- Inspect `workflow-status.md` for the last recorded output.
- Ask Claude to regenerate the artifact: “Recreate the PRD based on our last discussion.”
- For OpenSpec changes, verify the expected files under `openspec/changes/<id>/`.

---

## ⏭️ Skipped Phases

- Ask: “Review the BMAD workflow and confirm completed phases.”
- If a phase is missing, `bmad-workflow-router` should either produce the artifact or dispatch the correct skill.
- Ensure each phase has a clearly named artifact (e.g., `PRD.md`, `ARCHITECTURE.md`).

---

## 🔁 Routing Confusion (OpenSpec vs BMAD)

- OpenSpec → Level 0–1 changes (bug fix, small enhancement).
- BMAD → Full product or multi-phase work.
- If Claude chooses the wrong family, clarify: “This is a quick fix—use OpenSpec,” or “This is a full product effort—stay with BMAD.”
- Document new trigger phrases in `meta/MANIFEST.json` and `SKILL.md` as they emerge.

---

Keep this guide updated alongside every major trigger change or skill release.
