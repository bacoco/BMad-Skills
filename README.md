# BMAD Skills Library

BMAD is now distributed as a native Claude Skills repository. Each capability from the original multi-agent BMAD workflow is packaged as a standalone skill with progressive disclosure, templates, and tooling.

## Repository Layout

```
.claude/skills/         # All BMAD and OpenSpec capabilities ready for Claude runtime
shared/                 # Glossary, constraints, quality gates, shared tooling
meta/                   # Manifest, style guide, versioning rules
openspec/               # Runtime workspace for lightweight change specs
docs/                   # Generated artifacts when the skills run
stories/                # Story outputs produced by bmad-stories
```

Every skill folder contains:
- `SKILL.md` — Contract, mission, inputs, outputs, process, quality gates, and error handling.
- `REFERENCE.md` — Deep domain knowledge, manuals, and heuristics (load only when needed).
- `WORKFLOW.md` — Human-readable sequence replacing legacy BMAD agent handoffs.
- `CHECKLIST.md` — Quality gates applied before delivering artifacts.
- `assets/` — Templates or resources required to generate consistent outputs.
- `scripts/` — Optional automation invoked by the skill when deterministic output is needed.

## Core Skill Catalog

| Skill | Purpose |
|-------|---------|
| `bmad-orchestrator` | Maintain project state and route work across skills. |
| `bmad-analyst` | Clarify ambiguous ideas and surface research insights. |
| `bmad-pm` | Produce PRD and epic roadmap packages from discovery inputs. |
| `bmad-ux` | Translate requirements into UX flows, wireframes, and validation plans. |
| `bmad-architecture` | Generate decision-ready architecture documentation. |
| `bmad-tea` | Define test strategy, ATDD scenarios, and quality governance. |
| `bmad-stories` | Break epics into developer-ready stories and backlog signals. |
| `bmad-dev` | Implement ready stories with transparent testing evidence. |
| `skill-creator` | Guidance and tooling for authoring additional skills in this ecosystem. |

### OpenSpec Skills

The OpenSpec trio for Level 0-1 work lives alongside the BMAD skills inside `.claude/skills/`:
- `openspec-propose`
- `openspec-implement`
- `openspec-archive`

Each follows the same structure and references the shared glossary and constraints.

### Choosing BMAD vs OpenSpec

- **Use BMAD skills** when a problem requires end-to-end framing: new product discovery, full PRDs, architectural decisions, or delivery planning across multiple teams.
- **Use OpenSpec skills** when you already have a repo and need to ship a scoped change quickly. The proposal → implement → archive loop keeps specs aligned without invoking the heavier BMAD ceremonies.
- Escalate from OpenSpec to BMAD if any checklist flags indicate high ambiguity, multi-team coordination, or work that spans beyond Level 1 complexity.

## Installing in a Project Workspace

1. Copy the entire `.claude/skills/` directory into your project repo or Claude home (e.g. `~/.claude/skills/`).
2. Copy `shared/`, `meta/`, and `openspec/` alongside the skills if you want the same governance, glossary, and runtime workspace.
3. Keep `docs/` and `stories/` empty in your target repo—BMAD skills populate them when they run.

## Marketplace Bundles

Use the packager script to create Claude marketplace bundles on demand. Archives are **not** stored in the repository to avoid checking in binary files.

```bash
python .claude/skills/skill-creator/scripts/package_skill.py .claude/skills/<skill-name> dist/marketplace
```

Each command produces `<skill-name>.skill` inside `dist/marketplace/`, matching the runtime folder structure. Rebuild the archive whenever you need to upload a skill to the marketplace.

## Shared Assets

- `shared/glossary.md` — Terminology used across skills.
- `shared/constraints.md` — Governance rules that apply to every capability.
- `shared/quality-gates.md` — Global quality checks reused across workflows.
- `shared/tooling/` — Utility scripts (e.g., code flattening, manifest linting).

## Governance & Publishing

- Follow `meta/STYLE-GUIDE.md` when writing or editing skills.
- Update `meta/MANIFEST.json` and respect `meta/VERSIONING.md` when releasing changes.
- Run `shared/tooling/lint_contracts.py` before committing to ensure every skill includes the required files.

## Getting Started

1. Review the skill relevant to your task under `.claude/skills/`.
2. Load only the sections you need (metadata → SKILL.md → references).
3. Use provided templates and scripts from `assets/` and `scripts/` for consistent outputs.
4. Apply the skill-specific `CHECKLIST.md` and shared quality gates before delivering work.

This structure keeps BMAD aligned with modern Claude Skills design and replaces the previous multi-agent orchestration with modular, composable skills.


> Legacy documentation from the original BMAD/OpenSpec release remains in `doc/` for historical reference.