# Skill Catalog

This catalog applies Claude's skill creation best practices to every BMAD capability. Each entry stays concise, highlights when the skill should trigger, the minimum context it needs, its execution flow, expected outputs, and hard guardrails that prevent regressions. Use the **Skill Creator** first when designing or updating any additional skills.

## Foundational Utilities

### skill-creator
**Role**: Framework for designing, validating, and packaging Claude skills aligned with Anthropic's best practices.

**Use when**
- You need to create a brand-new skill or substantially revise an existing one.
- You are auditing a skill for context efficiency, workflow clarity, or resource organization.
- A teammate provides raw procedures, scripts, or templates that should become a reusable skill.

**Input expectations**
- Concrete example tasks or user prompts the skill must support.
- List of reusable resources (scripts, references, assets) worth bundling.
- Target distribution path for the packaged `.skill` archive (generate locally; do not commit binary bundles).

**Execution flow**
1. Gather representative use cases and confirm activation phrases.
2. Plan reusable resources; decide what lives in `scripts/`, `references/`, or `assets/`.
3. Run `.claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path <output-dir>` to scaffold the skill.
4. Draft SKILL.md using imperative language; move bulky material into references.
5. Validate with `.claude/skills/skill-creator/scripts/quick_validate.py <path>` when iterating.
6. Package with `.claude/skills/skill-creator/scripts/package_skill.py <path> [output-dir]` once validation passes.

**Outputs & handoffs**
- A complete skill directory with SKILL.md plus optional resources.
- Packaged `.skill` artifact ready for distribution (kept out of version control).
- Validation report identifying structure or quality issues.

**Guardrails**
- Keep SKILL.md under 500 lines; rely on references for heavy documentation.
- Do not add auxiliary docs (README, CHANGELOG, etc.) unless they are meant for Claude to load.
- Reference every supplemental file from SKILL.md so Claude discovers it via progressive disclosure.

**Supporting assets**
- `.claude/skills/skill-creator/scripts/init_skill.py`
- `.claude/skills/skill-creator/scripts/package_skill.py`
- `.claude/skills/skill-creator/scripts/quick_validate.py`
- `.claude/skills/skill-creator/references/workflows.md`
- `.claude/skills/skill-creator/references/output-patterns.md`

---

## Phase 0 · Orchestration and State

### bmad-orchestrator
**Role**: Primary conductor that initializes projects, manages BMAD state, and routes work to phase specialists.

**Use when**
- Starting or resuming any BMAD initiative ("Initialize BMAD workflow", "What's next?", "Where am I in the workflow?").
- Syncing status after a manual change request from the user.
- Determining which phase skill should engage next based on progress.

**Input expectations**
- Project goal summary and complexity level (if unspecified, ask to classify Level 1–4).
- Current artifacts (`workflow-status.md`, `sprint-status.yaml`) if they exist.
- Confirmation that prerequisite documents (PRD, epics, etc.) are available when transitioning phases.

**Execution flow**
1. On initialization, create/update workflow and sprint status files; seed default sprint backlog from epics when present.
2. Read current status files every time before suggesting next actions.
3. Recommend the most impactful next step and hand off to the corresponding skill (analyst, PM, UX, architecture, stories, dev, or TEA).
4. After each phase completes tasks, refresh state files to reflect new deliverables and blockers.

**Outputs & handoffs**
- Updated `workflow-status.md` and `sprint-status.yaml`.
- Next-step recommendation with explicit target skill and rationale.
- Phase transition approval notes (e.g., "Phase 2 ready; PRD finalized").

**Guardrails**
- Never modify state files manually; always use helper scripts (`workflow_status.py`, `sprint_status.py`).
- Block progression if mandatory artifacts are missing or inconsistent.
- Keep recommendations concise—surface only the highest priority next action.

**Supporting assets**
- `workflow_status.py`
- `sprint_status.py`

---

## Phase 1 · Analysis

### bmad-analyst
**Role**: Strategic discovery partner who transforms fuzzy ideas into grounded insights and initial documentation.

**Use when**
- User needs structured brainstorming, market/technical research, or reverse-engineering of an existing system.
- Early in projects where requirements are unsettled or ambiguous.
- Before PRD creation to ensure PM receives well-articulated problems and context.

**Input expectations**
- High-level problem statement or existing asset to analyze.
- Target audience, success metrics, or constraints if known.
- Any prior research or stakeholder notes available.

**Execution flow**
1. Clarify scope and assumptions; capture open questions for follow-up.
2. Run relevant workflow(s): Brainstorm Project, Product Brief, Research, or Document Project.
3. Distill findings into shareable artifacts (brainstorm notes, research briefs) with key takeaways and risks.
4. Highlight decision-ready insights and flag gaps for the PM to close.

**Outputs & handoffs**
- Structured brainstorming boards, product briefs, or research syntheses stored in project docs.
- Open questions list and recommended follow-up actions for PM or stakeholders.
- Confidence assessment covering unknowns and data quality.

**Guardrails**
- Avoid solutioning; stay focused on problem framing and evidence gathering.
- Cite all sources and assumptions explicitly to support downstream work.
- Keep deliverables concise—surface insights, not raw transcripts.

---

## Phase 2 · Planning and Design

### bmad-pm
**Role**: Product strategist translating analysis into actionable PRDs and epic roadmaps.

**Use when**
- The problem space is understood and requirements must be formalized.
- Creating or updating PRD, epics, or prioritization for Levels 2–4 projects.
- User requests planning help ("Create a PRD", "Plan this feature").

**Input expectations**
- Finalized analysis outputs plus stakeholder goals, success metrics, and constraints.
- Complexity level to size features (Level 2–4 default; Level 1 may skip).
- Existing product documentation to reconcile.

**Execution flow**
1. Validate that analysis artifacts cover user problem, audience, and success metrics.
2. Draft or update PRD with problem statement, objectives, functional requirements, non-functional requirements, and open questions.
3. Break scope into epics with acceptance criteria aligned to PRD requirements.
4. Coordinate with orchestrator to update sprint backlog readiness.

**Outputs & handoffs**
- `docs/PRD.md` updated with the latest requirements and dependencies.
- `docs/epics.md` containing prioritized epics, story seeds, and ACs.
- Readiness summary for downstream skills (UX, architecture, TEA).

**Guardrails**
- Do not invent requirements without traceability back to research or stakeholder directives.
- Maintain level-specific scale guidance (Level 2: 8–15 FRs, etc.).
- Flag unresolved risks or dependency gaps instead of hand-waving them.

---

### bmad-ux
**Role**: UX partner producing actionable UX specs and validation checklists for UI-heavy initiatives.

**Use when**
- Planning indicates user interface or experience changes (Levels 2–4, UI-heavy Level 1s as needed).
- The team needs wireframes, information architecture, or usability validation guidance.
- Requests such as "Design the UX" or "What should the UI look like?" appear.

**Input expectations**
- Approved PRD sections describing user journeys and functional requirements.
- Platform/device constraints, branding guidelines, accessibility targets.
- Current UX artifacts or screenshots for redesign efforts.

**Execution flow**
1. Confirm target users, primary scenarios, and constraints.
2. Produce UX design workflow outputs: personas, journey maps, wireframes, interaction notes.
3. Run the validation workflow to critique flows, accessibility, and edge cases.
4. Package findings into `docs/ux-spec.md` referencing annotated wireframes or assets.

**Outputs & handoffs**
- Updated `docs/ux-spec.md` with flows, component specs, and validation report.
- Asset bundle (links/screens) for dev and architecture to reference.
- Open UX questions and testing recommendations.

**Guardrails**
- Keep fidelity appropriate: wireframes and interaction notes, not production-ready UI code.
- Tie every design decision back to PRD requirements and research insights.
- Document accessibility considerations explicitly (contrast, keyboard, assistive tech).

---

## Phase 3 · Architecture & Quality Strategy

### bmad-architecture
**Role**: Technical architect defining solution patterns, stack choices, and foundational decisions.

**Use when**
- PRD/epics are approved and implementation planning must begin.
- Evaluating starter templates, integration options, or novel patterns.
- Questions like "How should we build this?" or "What's the architecture?" arise.

**Input expectations**
- Final PRD, epics, UX specs, and any existing system documentation.
- Non-functional requirements (performance, security, compliance).
- Tech constraints, existing platforms, or tooling preferences.

**Execution flow**
1. Audit requirements and constraints; confirm they are internally consistent.
2. Produce architecture design covering stack choices, module boundaries, data flows, and integration points.
3. Evaluate starter templates or patterns for reuse, documenting rationale.
4. Define implementation patterns, coding conventions, and version baselines to keep downstream agents aligned.

**Outputs & handoffs**
- `docs/ARCHITECTURE.md` capturing system diagrams, component responsibilities, and design decisions.
- Pattern registry summarizing reusable templates and guardrails.
- Version verification log (package/framework versions confirmed via research or tooling).

**Guardrails**
- Validate external dependencies (versions, support) before recommending.
- Keep patterns actionable—include naming conventions, folder structures, and integration hooks.
- Highlight technical debt or risk areas with mitigation strategies.

---

### bmad-tea
**Role**: Test Engineering Architect establishing end-to-end quality strategy across all phases.

**Use when**
- Planning or architecture work is complete and a comprehensive test approach is required.
- Setting up test automation, ATDD workflows, or CI/CD quality gates.
- Questions like "How should we test this?" or "Create test strategy" arise.

**Input expectations**
- PRD, epics, UX spec, architecture decisions, and non-functional requirements.
- Existing test frameworks or automation assets to integrate.
- Release cadence, quality bars, or compliance obligations.

**Execution flow**
1. Establish or confirm test framework scaffolding and tooling (unit, integration, e2e as appropriate).
2. Design test strategy covering risk assessment, scenario catalog, traceability to requirements, and automation approach.
3. Drive ATDD alignment: define acceptance tests before implementation starts.
4. Outline CI/CD quality gates, flakiness monitoring, and review cadences.

**Outputs & handoffs**
- Test strategy documentation with prioritized scenarios and coverage plan.
- Automation roadmap and CI/CD quality checklist.
- Traceability matrix linking requirements to planned tests.

**Guardrails**
- Prioritize unit and integration coverage; flag E2E reliance as technical debt.
- Require measurable pass/fail criteria for every acceptance test.
- Keep continuous communication with bmad-dev to ensure implementation follows ATDD artifacts.

---

## Phase 4 · Delivery

### bmad-stories
**Role**: Story crafter turning epics into development-ready stories with contextual learnings.

**Use when**
- Epics and architecture patterns are ready for implementation.
- The team needs structured story files with acceptance criteria and tasks.
- Requests such as "Break into stories" or "Create user stories" are issued.

**Input expectations**
- `docs/epics.md`, `docs/PRD.md`, `docs/ARCHITECTURE.md`, UX specs, and Dev Agent Record.
- Previous story output to extract learnings and maintain continuity.
- Architecture patterns and testing guardrails defined by other skills.

**Execution flow**
1. Parse target epic plus latest Dev Agent Record to understand context and dependencies.
2. Generate story file with sections for Summary, Requirements Traceability, Tasks, Acceptance Criteria, Test Strategy hooks, and "Learnings from Previous Story".
3. Cite architecture patterns and testing mandates explicitly.
4. Save story under `stories/{epic}-{story}-{title}.md` and notify orchestrator of readiness.

**Outputs & handoffs**
- Story markdown file ready for bmad-dev, including tasks mapped to acceptance criteria.
- Updated Dev Agent Record with new context and decisions.
- Continuity notes for next story in sequence.

**Guardrails**
- Never produce a story without referencing the immediately prior story for lessons learned.
- Keep tasks implementation-agnostic; avoid writing code or design specs here.
- Reject requests if required upstream artifacts are stale or missing.

---

### bmad-dev
**Role**: Senior implementation engineer executing stories end-to-end, including testing and documentation updates.

**Use when**
- A story file exists and the team is ready to implement.
- User requests coding support ("Implement story X", "Start coding").
- Verification or refactor tasks arise that map to existing stories.

**Input expectations**
- Target story markdown with acceptance criteria and tasks.
- Architecture patterns, test strategy, Dev Agent Record, and relevant codebase access.
- Tooling instructions for running tests and linters.

**Execution flow**
1. Read the story, previous learnings, and architecture/testing guardrails.
2. Implement tasks iteratively, updating Dev Agent Record as work progresses.
3. Write and run automated tests; ensure 100% pass rate locally.
4. Perform self-review, note deviations, and mark story complete only when all ACs and quality gates are satisfied.

**Outputs & handoffs**
- Code changes with accompanying tests and documentation updates.
- Updated Dev Agent Record capturing work performed, test evidence, and follow-up issues.
- Ready-for-review summary for human stakeholders if needed.

**Guardrails**
- Never begin work without the story file and confirmed prerequisites.
- Obey architecture patterns exactly; reuse existing services instead of re-implementing.
- Refuse completion if tests cannot be executed or do not pass—raise blockers instead.

---

## Usage Notes

- Always initialize the workflow with **bmad-orchestrator** before invoking downstream skills.
- Hand-offs should include pointers to the latest artifacts so each skill loads only the context it needs, keeping conversation windows lean.
- When evolving this catalog, run the **skill-creator** validation scripts to ensure every entry remains concise, discoverable, and conformant with Anthropic skill guidelines.
