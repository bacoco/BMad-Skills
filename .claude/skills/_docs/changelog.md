# Changelog

## Version 2.1.4 - Compliance Audit Resolution (2025-10-30)

**Patch Release**: Post-2.1.3 compliance audit fixes

**Changes**:
- 🔮 Validator: Removed hard-coded frontmatter key allow-list for future-proofing
  - quick_validate.py now accepts all schema fields
  - Maintains forward compatibility with evolving Claude Skills schema
  - Only enforces required fields and format constraints
- 📌 Version consistency: Updated workflow_status.py footer from v1.0.0 to current version
- 📚 Changelog completeness: Documented all releases from v2.1.1 through v2.1.3

**Impact**: Bundle now fully compliant with documented SOTA requirements from CLAUDE.md audit.

## Version 2.1.3 - Documented Patterns Enforcement (2025-10-30)

**Patch Release**: Path resolution and dependency cleanup

**Changes**:
- 🔧 RUNTIME_ROOT constants now follow documented pattern
  - All scripts use `RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"`
  - Added separate `ARTIFACTS_DIR` and `STORIES_DIR` variables
  - Updated 5 scripts: sprint_status.py, workflow_status.py, generate_architecture.py, create_story.py, generate_prd.py
  - Pattern now consistent with OpenSpec scripts and documented convention
- 📦 Removed Jinja2 external dependency (self-contained bundle)
  - Refactored 3 generation scripts to use Python's standard library
  - generate_architecture.py: Uses programmatic string building with loops/conditionals
  - create_story.py: Builds story content without template engine
  - generate_prd.py: Renders both PRD and epics documents natively
  - Bundle is now completely self-contained with zero external dependencies

**Impact**: All 12 skills validated successfully. All 39 tests pass.

## Version 2.1.2 - Critical Compliance Fixes (2025-10-29)

**Patch Release**: Validator and template compliance fixes

**Changes**:
- 🔍 Validator: Replace broken line parser with PyYAML for proper YAML parsing
  - quick_validate.py now uses yaml.safe_load() instead of ast.literal_eval()
  - Correctly handles YAML lists in metadata.triggers.patterns
  - All 12 skills now pass validation
- 📝 SKILL.md descriptions: Remove redundant 'Keywords:' suffix
  - Keywords already exist in metadata.triggers.keywords array
  - Cleaned all descriptions to be under 160 chars
  - Ensures valid YAML parsing (colons in strings were causing issues)
- 📄 OpenSpec templates: Rename to .md.jinja extension per style guide
  - archive-template.md → archive-template.md.jinja
  - execution-log-template.md → execution-log-template.md.jinja
  - proposal-template.md → proposal-template.md.jinja
  - spec-delta-template.md → spec-delta-template.md.jinja
  - tasks-template.md → tasks-template.md.jinja
  - Updated Python scripts to reference new .jinja extensions

**Impact**: All tests pass (39/39). Marketplace compliance improved.

## Version 2.1.1 - Template Discoverability (2025-10-29)

**Patch Release**: Progressive disclosure enhancement

**Changes**:
- 📖 Fixed template discoverability by adding explicit citations in SKILL.md for all templates in assets/ directories
- ✨ Ensures Claude can discover and load templates through progressive disclosure
- 📦 Published to NPM: bmad-skills@2.1.1 (131.7 kB, 422.6 kB unpacked)

**Install**: `npx bmad-skills --global`

## Version 2.1.0 - Proactive Skills (2025-10-28)

**Major UX Enhancement**: Skills now activate automatically based on conversation context

**New Features**:
- 🎯 Proactive auto-invocation: Claude detects user intent and invokes skills automatically
- 🗣️ Natural language triggers: No slash commands needed, just talk naturally
- 📊 Conversational triggers table: Clear mapping of phrases to skills
- ✨ All 7 skills updated with "When Claude Should Invoke This Skill" sections
- 📖 README updated with conversational examples and trigger documentation

**Changed Files**:
- All 7 skill YAML descriptions now include "Proactively activates when..."
- All 7 skills have new 🎯 sections with clear invocation triggers
- README shows natural conversation flows instead of manual commands

**Example**:
```
User: "I have an idea for a todo app"
Claude: [Automatically invokes bmad-analyst]
```

No more "/bmad-pm" or manual skill invocation. Just natural conversations.

## Version 2.0.0 - Complete Implementation (2025-10-28)

**Complete BMAD Method v6-alpha transformation**

**New Features**:
- ✅ Added bmad-analyst (Analysis phase)
- ✅ Added bmad-ux (UX Design)
- ✅ Added bmad-tea (Test Architecture)
- ✅ Added bmad-dev (Implementation)
- ✅ Refactored orchestrator with full state management
- ✅ Added workflow-status.md management
- ✅ Added sprint-status.yaml management
- ✅ Added story lifecycle tracking
- ✅ Added Python helpers for state management
- ✅ All 4 phases now complete
- ✅ All BMAD workflows covered

**Implementation Stats**:
- 7 Agent Skills implemented
- 2,919 lines of Skill documentation
- 2 Python state management helpers
- Workflow-status.md management
- Sprint-status.yaml management
- All BMAD phases covered
- Story lifecycle management
- BMAD agent personas preserved
- 100% faithful to BMAD v6-alpha

**Files Created**:
- 7 SKILL.md files
- 2 Python helpers
- 3 Python generators (PRD, Architecture, Story)
- 3 Jinja templates
- 1 comprehensive README

## Version 1.0.0 - Initial Release (2025-10-27)

**Features**:
- 3 Skills: PM, Architecture, Stories
- Basic orchestrator
- No state management

---

# Attribution & License

**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org

This implementation preserves BMAD v6-alpha agent personas, workflows, and output formats. It is a faithful vendoring of BMAD logic into Claude Code Skills, not a loose recreation.

**Agent Personas** (preserved from BMAD v6-alpha):
- Mary (Analyst) - Strategic Business Analyst
- John (PM) - Investigative Product Strategist
- Sally (UX Designer) - User Experience Designer
- Winston (Architect) - System Architect
- Murat (TEA) - Master Test Architect
- Bob (Scrum Master) - Technical Scrum Master
- Amelia (DEV) - Senior Implementation Engineer

**Important**: This is for internal/educational use. Do not redistribute without proper licensing from bmad-code-org.
