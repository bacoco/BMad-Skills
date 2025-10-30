# BMAD Skills Style Guide

## Naming & Metadata
- Use `bmad-<capability>` or `<pack>-<capability>` naming with hyphens.
- Keep `description` under 160 characters with activation keywords.
- Restrict `allowed-tools` to the minimum necessary for the skill.

## File Layout
Each skill MUST include the following directories and files:
- `SKILL.md` - Contract with YAML frontmatter and process documentation
- `REFERENCE.md` - Deep domain knowledge and extended context
- `WORKFLOW.md` - Human-readable step sequence
- `CHECKLIST.md` - Quality gates before delivering artifacts
- `assets/` - MUST contain string.Template templates (.md.template) for all declared outputs
- `scripts/` - MUST contain either automation tooling OR a README.md explaining why automation is not applicable

Reference deep material from `SKILL.md` rather than embedding it directly.

## Writing Principles
- Lead with mission, inputs, outputs, process, quality gates, and error handling.
- Address the assistant in second person (“You”) and refer to the skill in third person when summarizing capabilities.
- Prefer bullet lists and numbered steps for scannability.
- Cite templates, scripts, or shared glossary entries explicitly.
- Clarify whether the skill belongs to the BMAD track (end-to-end framing) or the OpenSpec track (Level 0-1 incremental work) so users choose the correct path.

## Progressive Disclosure
- Keep `SKILL.md` under ~500 lines; move extended context to `REFERENCE.md` or assets.
- Link to `CHECKLIST.md` for gating instead of duplicating criteria.
- Scripts should read templates from `assets/` relative paths to avoid brittle assumptions.

## Versioning
- Update the `version` field when behavior changes materially.
- Reflect changes in `meta/MANIFEST.json` during publication.
