# Audit Checklist – BMAD and OpenSpec Skills

Use this checklist to validate compliance with Duclos-style conventions and conversational activation expectations.

---

## 1. Repository Structure
- ☐ The Duclos architecture is present at the repository root.
- ☐ No legacy directories such as `agents/`, `workflows/`, or `playbooks/` remain.
- ☐ No deprecated `*.workflow.yaml` files exist.

## 2. Skill Directory Completeness
- ☐ Every skill folder contains `SKILL.md`, `REFERENCE.md`, and `CHECKLIST.md`.
- ☐ `WORKFLOW.md` exists unless the skill is strictly atomic.
- ☐ `assets/` and `scripts/` directories exist, even if empty.

## 3. SKILL.md Contract Quality
- ☐ The file begins with YAML front matter wrapped by `---`.
- ☐ Sections include `Mission`, `Inputs Required`, `Output`, `Process`, `Quality Gates`, and `Error Handling`.
- ☐ The `Process` section is organized as numbered steps.
- ☐ `Output` references at least one tangible artifact.

## 4. Progressive Disclosure & Ownership
- ☐ `SKILL.md` stays concise without encyclopedic paragraphs (>500 words).
- ☐ `CHECKLIST.md` offers actionable checkboxes and is referenced from `SKILL.md`.
- ☐ `WORKFLOW.md` describes handoffs (`Step 1`, `Step 2`, etc.).

## 5. Templates and Assets
- ☐ Each promised deliverable has an associated template in `assets/`.
- ☐ No template files contain placeholders like `TODO` or remain empty.
- ☐ Filenames mentioned in `SKILL.md` correspond to real files.

## 6. Supporting Scripts
- ☐ Scripts are clearly named and align with their related deliverables.
- ☐ `SKILL.md` explains when and how to run the scripts.

## 7. `meta/MANIFEST.json`
- ☐ The manifest is valid JSON and lists every skill inside `.claude/skills/`.
- ☐ Each entry includes accurate `id`, `version`, `allowed-tools`, and `path` fields.
- ☐ Manifest data matches the corresponding `SKILL.md` front matter.

## 8. Governance Documents
- ☐ `meta/STYLE-GUIDE.md` explains naming conventions, description rules, and file separation.
- ☐ `meta/VERSIONING.md` documents the policy for updating version numbers.

## 9. Legacy Expansion Packs
- ☐ No `expansion/` directories or remnants are present.
- ☐ Skills are not regrouped by deprecated expansion pack naming.

## 10. Core BMAD Pillars
- ☐ At least one skill covers backlog preparation and user stories.
- ☐ Documentation mentions how context transfers between phases.

## 11. OpenSpec Integration
- ☐ OpenSpec skills (proposal, implement, archive) exist with proper `SKILL.md`/`REFERENCE.md`/`WORKFLOW.md`/`CHECKLIST.md` files.
- ☐ OpenSpec documentation explains change IDs, deliverables, and process flow.
- ☐ OpenSpec remains a skill family, not merely vendored code.

## 12. OpenSpec Skill Quality
- ☐ OpenSpec skills follow the same Duclos conventions as BMAD skills.
- ☐ `SKILL.md` front matter lists accurate allowed tools and deliverables.
- ☐ `Process` sections describe the Proposal → Apply → Archive sequence.
- ☐ `REFERENCE.md` captures OpenSpec philosophy and operational rules.
- ☐ `CHECKLIST.md` enforces validation gates before each stage.

## 13. BMAD vs. OpenSpec Guidance
- ☐ Root documentation clarifies when to use BMAD (full product cycles) versus OpenSpec (incremental change requests).
- ☐ OpenSpec descriptions stay focused on Level 0–1 change management.

## 14. Manifest Coverage for OpenSpec
- ☐ `meta/MANIFEST.json` includes every OpenSpec skill with correct metadata.
- ☐ No manifest entry points to a missing path.

## 15. Runtime Readiness for OpenSpec
- ☐ The repository contains `openspec/changes/` and `openspec/specs/` (or documented equivalents).
- ☐ Scripts generate or archive change artifacts inside those directories.
- ☐ Operational rules from legacy `AGENTS.md` files have been migrated into the OpenSpec references or checklists.

---

## Output Format for Automated Audits
Return a JSON object where each checklist section becomes a key. Each value should contain:
- `status`: `"PASS"` or `"FAIL"`
- `problems`: optional array listing `{path, rule, suggestion}` when `status` is `"FAIL"`
