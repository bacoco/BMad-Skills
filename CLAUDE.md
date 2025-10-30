# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is **BMAD Skills** - a complete workflow ecosystem packaged as Claude Skills. It provides 12 integrated skills that guide users from idea to implementation through natural conversation. This is a **skills library repository**, not an application codebase.

## Core Architecture

### Two-Track System

The repository implements two complementary workflows:

1. **BMAD Track** (8 skills): End-to-end product development for Level 2-4 complexity
   - main-workflow-router → bmad-discovery-research → bmad-product-planning → bmad-ux-design → bmad-architecture-design → bmad-test-strategy → bmad-story-planning → bmad-development-execution
   - Handles: New products, complex features, multi-team coordination

2. **OpenSpec Track** (3 skills): Lightweight change management for Level 0-1 complexity
   - openspec-change-proposal → openspec-change-implementation → openspec-change-closure
   - Handles: Bug fixes, small features, quick changes

The **main-workflow-router** automatically routes work to the appropriate track based on complexity assessment.

### Self-Contained Bundle Architecture

Everything is contained in `.claude/skills/`:

```
.claude/skills/
├── [12 skill directories]     # Each with SKILL.md, REFERENCE.md, WORKFLOW.md, CHECKLIST.md
├── _core/                      # Shared resources (glossary, constraints, quality-gates)
├── _config/                    # Configuration (MANIFEST.json, STYLE-GUIDE.md)
├── _runtime/                   # Runtime workspace for OpenSpec changes
└── _docs/                      # Documentation organized by type
```

**Critical constraint:** All skills must reference resources using paths relative to `.claude/skills/` because the bundle is installed to various locations (`~/.claude/skills/` or `project/.claude/skills/`).

### Dual Manifest Locations

For marketplace compatibility:
- `meta/MANIFEST.json` - Required at root for marketplace tooling
- `.claude/skills/_config/MANIFEST.json` - Used by skills internally

**Both must stay in sync.** When updating skills, update both files.

## Key Commands

### Installation & Distribution

```bash
# Verify current installation
bash scripts/verify.sh [path]

# Install to ~/.claude/skills (global)
bash scripts/install-to-home.sh

# Install to current project
bash scripts/install-to-project.sh

# Create marketplace distribution bundle
bash scripts/package-bundle.sh
```

### Validation & Testing

```bash
# Validate a single skill
python .claude/skills/core-skill-creation/scripts/quick_validate.py .claude/skills/[skill-name]

# Validate all skill contracts
python .claude/skills/_core/tooling/lint_contracts.py

# Run Python tests
pytest tests/

# Test skill metadata consistency
pytest tests/test_skill_metadata.py
pytest tests/test_manifest_consistency.py
```

### OpenSpec Helper Scripts

```bash
# Create new OpenSpec change workspace
python .claude/skills/openspec-change-proposal/scripts/scaffold_change.py [change-id]

# Update execution log
python .claude/skills/openspec-change-implementation/scripts/update_execution_log.py [change-id] "message"

# Archive completed change
python .claude/skills/openspec-change-closure/scripts/archive_change.py [change-id]
```

### Metrics & Analysis

```bash
# Export activation metrics report
python .claude/skills/_core/tooling/activation_metrics.py export
```

## Skill Structure Requirements

Every skill MUST contain:

1. **SKILL.md** - Contract with YAML frontmatter:
   ```yaml
   name: skill-name
   description: Brief description with trigger keywords
   version: 1.0.0
   allowed-tools: ["Read", "Write", "Grep"] # or ["Read", "Write", "Grep", "Bash"]
   metadata:
     auto-invoke: true
     triggers:
       patterns: ["phrase 1", "phrase 2"]
       keywords: [keyword1, keyword2]
     capabilities: [capability1, capability2]
     prerequisites: [artifact1, artifact2]
     outputs: [output1, output2]
   ```

2. **REFERENCE.md** - Deep domain knowledge (loaded only when needed)
3. **WORKFLOW.md** - Human-readable step sequence
4. **CHECKLIST.md** - Quality gates before delivering artifacts
5. **assets/** - Templates for consistent output generation (required, may contain placeholder templates)
6. **scripts/** - Python scripts for deterministic operations (required, must contain either automation scripts or README explaining why automation is not needed)

## Editing Skills

### When updating a skill:

1. **Update the skill files** in `.claude/skills/[skill-name]/`
2. **Update BOTH manifests:**
   - `.claude/skills/_config/MANIFEST.json`
   - `meta/MANIFEST.json`
3. **Increment version** in:
   - SKILL.md frontmatter
   - Both MANIFEST.json files
4. **Validate** with `quick_validate.py`
5. **Test** that paths resolve correctly

### Tool Permission Policy (Security)

Follow **principle of least privilege**:

- **Planning/Documentation skills**: Only `["Read", "Write", "Grep"]`
  - bmad-discovery-research, bmad-product-planning, bmad-ux-design, bmad-architecture-design, bmad-test-strategy, bmad-story-planning

- **Execution skills**: May include `"Bash"` when necessary
  - bmad-development-execution (runs tests)
  - main-workflow-router (git status checks)
  - openspec-* (Python script execution)
  - core-skill-creation (validation/packaging)

### Path Resolution in Scripts

All Python scripts in `scripts/` directories must use:

```python
SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
CORE_DIR = SKILLS_ROOT / "_core"

# Workspace subdirectories
ARTIFACTS_DIR = RUNTIME_ROOT / "artifacts"  # BMAD planning artifacts
STORIES_DIR = RUNTIME_ROOT / "stories"      # BMAD developer stories
CHANGES_DIR = RUNTIME_ROOT / "changes"      # OpenSpec change proposals
SPECS_DIR = RUNTIME_ROOT / "specs"          # OpenSpec specifications
```

**Never** use `parents[4]` or assume repo root structure - skills must work when installed anywhere.

## Style Guide Requirements

From `.claude/skills/_config/STYLE-GUIDE.md`:

- Use `hyphen-case` for skill names
- Keep descriptions under 160 characters with activation keywords
- Keep SKILL.md under ~500 lines (move details to REFERENCE.md)
- Address the assistant in second person ("You")
- Scripts should read templates from `assets/` using relative paths
- Update version field when behavior changes materially

## Complexity Levels (BMAD Levels)

Critical for orchestrator routing:

- **Level 0**: Config changes, one-line fixes
- **Level 1**: Small features, simple enhancements
- **Level 2**: Medium features requiring architecture
- **Level 3**: New product areas, significant changes
- **Level 4**: Novel innovations, high uncertainty

Levels 0-1 → OpenSpec | Levels 2-4 → BMAD

## Important Constraints

1. **No external dependencies outside .claude/skills/** - Bundle must be self-contained
2. **Both manifests must stay in sync** - Update meta/ and _config/ simultaneously
3. **Validator must accept all frontmatter fields** - Never restrict to outdated schema
4. **Scripts must use relative paths** - Never hardcode repo root paths
5. **Follow progressive disclosure** - Keep SKILL.md concise, defer to REFERENCE.md

## Testing Changes

Before committing skill changes:

```bash
# 1. Validate the skill
python .claude/skills/core-skill-creation/scripts/quick_validate.py .claude/skills/[skill-name]

# 2. Verify installation works
bash scripts/verify.sh .claude/skills

# 3. Test OpenSpec scripts if modified
python .claude/skills/openspec-change-proposal/scripts/scaffold_change.py test-change
rm -rf .claude/skills/_runtime/workspace/changes/test-change

# 4. Run Python tests
pytest tests/
```

## Distribution

The bundle is distributed as a complete package containing all 12 skills. Users install via:

```bash
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-home.sh | bash
```

The installation creates a unified workspace at `_runtime/workspace/` with the following structure:
- `_runtime/workspace/artifacts/` - BMAD planning artifacts (PRD, architecture, etc.)
- `_runtime/workspace/stories/` - BMAD developer stories
- `_runtime/workspace/changes/` - OpenSpec change proposals
- `_runtime/workspace/specs/` - OpenSpec specifications

## Marketplace Compliance

For Claude Skills Marketplace:

1. **Manifest location**: `meta/MANIFEST.json` must exist at root
2. **Structured metadata**: All skills must have complete `metadata` block with triggers/capabilities
3. **Validator acceptance**: Must accept all current and future Claude schema fields
4. **Tool permissions**: Minimal necessary tools per skill

All 4 requirements are currently satisfied.
