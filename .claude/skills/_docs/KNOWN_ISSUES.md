# Known Issues

This document tracks known limitations and technical debt in BMAD Skills that require future refactoring.

## ~~Template Usage Drift~~ (RESOLVED)

**Status:** ✅ FIXED

**Issue:** OpenSpec helper scripts were updated to look for `.md.template` assets after the repo cleanup, but the packaged bundle
still shipped stale `.md.jinja` filenames. Operators running `scaffold_change.py` or `update_execution_log.py` would hit
`FileNotFoundError` because the expected templates were missing, and documentation referenced the wrong extensions.

**Impact:** Blocked OpenSpec workflows (proposal scaffolding, execution log updates) and eroded trust in documentation vs. runtime
behavior.

**Resolution Implemented:**
1. ✅ All OpenSpec assets synchronized with script expectations (using `.md.template`)
2. ✅ Added regression test coverage: `tests/test_template_assets.py`
   - Validates all script-referenced templates exist
   - Prevents .jinja files from being re-introduced
   - Enforces stable template count (9 expected)
3. ✅ Added packaging pipeline validation: `bin/prepare.js`
   - Checks template assets before npm publish
   - Verifies no .jinja files in bundle
   - Fails publish if templates are missing
4. ✅ Documentation audited and aligned

**Status Updates:**
- 2025-10-30: Recreated `.md.template` assets for OpenSpec scripts and aligned code/documentation
- 2025-10-30: Added dual-layer protection (pytest + npm prepare hook) to prevent future regressions

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
