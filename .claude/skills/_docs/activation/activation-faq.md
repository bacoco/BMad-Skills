# Activation FAQ

Frequently asked questions about conversational activation for the BMAD and OpenSpec skill suites.

---

## Why is conversational activation important?
Because users interact in natural language. Claude should auto-select the right skill based on intent without requiring manual commands. This reduces friction, enforces the Bimath methodology, and keeps projects moving.

## How do I know if auto-activation worked?
Claude will respond with a confirmation similar to “Activating BMAD Analyst…” or will immediately deliver the artifact associated with that skill. The response should reference the skill name and the action it is taking.

## What if no skill activates?
1. Rephrase the request using **Action + Artifact + Context**. Example: “Create a PRD for my budgeting app.”
2. Mention the desired outcome explicitly (PRD, architecture, test plan, etc.).
3. If Claude still does not activate a skill, issue the manual command: `Invoke <skill-id>`.

## Why did the wrong skill activate?
Claude weighs strong keywords first. If you say “I have an idea to implement story #5,” the word “idea” may trigger `bmad-discovery-research`. Rephrase to lead with the actual task: “Implement story #5 that we already approved.”

## How do I hand control back to `bmad-workflow-router`?
Say “What’s next for the BMAD workflow?” or “Give me a status update.” The orchestrator will resume control, check `workflow-status.md`, and suggest the next phase.

## Can OpenSpec skills auto-activate too?
Yes. Mention that you need a “quick fix,” “small change,” or “apply the proposal” and Claude will prefer the OpenSpec skills. Make sure the request clearly indicates Level 0–1 scope.

## How do I recover if a phase was skipped?
Ask `bmad-workflow-router`: “Review the workflow and confirm which phases are complete.” If an artifact is missing, the orchestrator will either recreate it or delegate to the correct skill.

## What if I need to override the automatic choice?
You can always instruct Claude: “Use BMAD PM for this request” or “Switch to OpenSpec Implement.” This manual override is useful when experimenting with new triggers.

## Where can I find example conversations?
See `doc/conversational-flow.md` for end-to-end dialogues and `tests/test_skill_activation.md` for scripted regression scenarios.

## Who should maintain these triggers?
Product owners and conversational designers. Revisit the descriptions and trigger lists whenever new phases, deliverables, or vocabulary appear.
