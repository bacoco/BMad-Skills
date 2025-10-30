# Known Issues

This document tracks known limitations and technical debt in BMAD Skills that require future refactoring.

## ~~Template Usage~~ (RESOLVED)

**Status:** ✅ FIXED

**Resolution:** All 3 generator scripts now load templates from `assets/` using `string.Template` (stdlib):
- `.claude/skills/bmad-product-planning/scripts/generate_prd.py` → loads from `assets/`
- `.claude/skills/bmad-architecture-design/scripts/generate_architecture.py` → loads from `assets/`
- `.claude/skills/bmad-story-planning/scripts/create_story.py` → loads from `assets/`

New template files created:
- `prd-script-template.md.template`
- `epics-wrapper-template.md.template`
- `architecture-script-template.md.template`
- `story-script-template.md.template`

Implementation:
- Uses `string.Template` (stdlib-only, maintains zero-dependency goal)
- Templates loaded via `ASSETS_DIR / "template-name.md.template"`
- Logic/loops kept in Python, presentation in template files
- Proper separation of concerns achieved

---

## Simple YAML Parser Limitations (Priority: Low)

**Issue:** Custom `simple_yaml.py` parser doesn't support full YAML spec.

**Current Limitations:**
- ❌ Multi-line strings (block scalars |, >)
- ❌ Anchors and aliases (&, *)
- ❌ Complex nested structures
- ❌ YAML 1.2 features

**Supported Features:**
- ✅ Scalars (strings, numbers, booleans, null)
- ✅ Lists (inline and multi-line)
- ✅ Nested dictionaries
- ✅ Comments
- ✅ All SKILL.md frontmatter patterns

**Impact:**
- Current: No impact - all skill frontmatter uses supported subset
- Future: May need enhancement if skills require complex YAML

**Workaround:**
SKILL.md frontmatter is intentionally simple and within supported subset.

**Resolution:**
If needed in future:
1. Enhance simple_yaml.py to support additional features
2. Or switch to vendored PyYAML (violates zero-dependency goal)
3. Or restrict SKILL.md schema to simple_yaml capabilities

**Priority Justification:**
Low priority because:
- All current skills work fine
- Frontmatter schema is intentionally simple
- Zero-dependency goal is valuable

---

## Historical Version References (Priority: Low)

**Issue:** Some legacy comments and docstrings reference older BMAD versions.

**Examples:**
- Comments mentioning "BMAD v1.0"
- Old documentation links
- Deprecated pattern references

**Impact:**
- Minor confusion for new contributors
- No functional impact

**Resolution:**
Periodic cleanup during major version bumps.

---

## Distribution Strategy Documentation (Priority: Low)

**Issue:** Multiple distribution methods (npm, bundle, marketplace) lack unified documentation.

**Current State:**
- npm publish works
- Bundle ZIP exists
- Marketplace strategy unclear
- Installation methods documented separately

**Needed:**
- Single source of truth for distribution
- Clear marketplace vs npm strategy
- Installation comparison table
- Update instructions

**Resolution:**
Create comprehensive DISTRIBUTION.md in repository root.

---

## Contributing
When you discover new issues, add them to this document with:
- Clear description
- Affected files
- Impact assessment
- Proposed resolution
- Priority justification
