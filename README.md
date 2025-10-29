# BMAD Skills Library

BMAD is now distributed as a native Claude Skills repository. Each capability from the original multi-agent BMAD workflow is packaged as a standalone skill with progressive disclosure, templates, and tooling.

## Repository Layout

```
skills/                 # Core BMAD capabilities (discovery → delivery)
expansion/openspec/     # Lightweight Level 0-1 skills (propose → implement → archive)
shared/                 # Glossary, constraints, quality gates, shared tooling
meta/                   # Manifest, style guide, versioning rules
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
| `bmad-discovery-analysis` | Clarify ambiguous ideas and surface research insights. |
| `bmad-product-requirements` | Produce PRD and epic roadmap packages from discovery inputs. |
| `bmad-architecture-design` | Generate decision-ready architecture documentation. |
| `bmad-ux-blueprint` | Translate requirements into UX flows, wireframes, and validation plans. |
| `bmad-delivery-planning` | Break epics into developer-ready stories and backlog signals. |
| `bmad-development-execution` | Implement ready stories with transparent testing evidence. |
| `bmad-quality-assurance` | Define test strategy, ATDD scenarios, and quality governance. |
| `bmad-end-to-end-orchestration` | Maintain project state and route work across skills. |
| `skill-creator` | Guidance and tooling for authoring additional skills in this ecosystem. |

### Expansion Packs

`expansion/openspec` includes the OpenSpec trio for Level 0-1 work:
- `openspec-propose`
- `openspec-implement`
- `openspec-archive`

Each follows the same structure and references the shared glossary and constraints.

### Choosing BMAD vs OpenSpec

- **Use BMAD skills** when a problem requires end-to-end framing: new product discovery, full PRDs, architectural decisions, or delivery planning across multiple teams.
- **Use OpenSpec skills** when you already have a repo and need to ship a scoped change quickly. The proposal → implement → archive loop keeps specs aligned without invoking the heavier BMAD ceremonies.
- Escalate from OpenSpec to BMAD if any checklist flags indicate high ambiguity, multi-team coordination, or work that spans beyond Level 1 complexity.

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

1. Review the skill relevant to your task under `skills/` or `expansion/`.
2. Load only the sections you need (metadata → SKILL.md → references).
3. Use provided templates and scripts from `assets/` and `scripts/` for consistent outputs.
4. Apply the skill-specific `CHECKLIST.md` and shared quality gates before delivering work.

This structure keeps BMAD aligned with modern Claude Skills design and replaces the previous multi-agent orchestration with modular, composable skills.


> Legacy documentation from the original BMAD/OpenSpec release remains in `doc/` for historical reference.