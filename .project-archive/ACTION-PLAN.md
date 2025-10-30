# CONTINUOUS IMPROVEMENT PLAN – BMAD Conversational Activation

**Objective:** Sustain the 96/100 audit score and close the remaining automation and telemetry gaps within two days of focused work.
**Focus:** Operationalize automated conversational testing, activation telemetry, and orchestration bootstrapping.

---

## DAY 1 – Automate Conversational Regression Testing

### Task 1.1 – Turn `tests/test_skill_activation.md` into an executable suite
**Goal:** Reuse the eight scripted dialogues as machine-run prompts.

**Steps:**
1. Create `tests/test_skill_activation.py` that replays each scenario against the runtime harness (mock or integration).
2. Parse manifest descriptions to verify that declared keywords appear in the scripted prompts.
3. Emit structured pass/fail results for CI consumption.

**Estimated time:** 4 hours.

### Task 1.2 – Wire into CI / release checklist
**Goal:** Ensure conversational regression runs before publishing updates.

**Steps:**
1. Extend the existing release checklist (or create `.github/workflows/activation.yml`) to call the new suite.
2. Capture transcripts and failures as artifacts for debugging.

**Estimated time:** 1 hour.

---

## DAY 2 – Activation Telemetry & Workflow Bootstrap

### Task 2.1 – Seed activation metrics
**Goal:** Provide a baseline dataset for the included metrics tooling.

**Steps:**
1. Execute representative conversations covering BMAD and OpenSpec flows.
2. Log activations via `shared/tooling/activation_metrics.py` → `docs/activation-metrics.yaml`.
3. Document instructions in `doc/troubleshooting.md` for updating the metrics log.

**Estimated time:** 2 hours.

### Task 2.2 – Publish workflow status starter artifact
**Goal:** Help adopters validate orchestrator handoffs immediately.

**Steps:**
1. Author `docs/bmad-workflow-status.md` with sample phase entries.
2. Reference the template inside `.claude/skills/main-workflow-router/SKILL.md` and `doc/conversational-flow.md`.

**Estimated time:** 1 hour.

---

## CHECKLIST FOR COMPLETION

- [ ] Conversational regression scenarios execute automatically and report pass/fail results.
- [ ] CI or release workflow fails if any conversational scenario regresses.
- [ ] `docs/activation-metrics.yaml` contains at least one logged conversation per skill cluster.
- [ ] `docs/bmad-workflow-status.md` template ships with guidance for orchestrator state tracking.

**Success Criteria:** Conversational activation remains reliable without manual intervention, telemetry tracks real usage, and new teams can bootstrap the orchestrator workflow on day one.
