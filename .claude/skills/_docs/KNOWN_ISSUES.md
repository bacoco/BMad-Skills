# Known Issues

This document tracks known limitations and technical debt in BMAD Skills that require future refactoring.

## Template Usage (Priority: Medium)

**Issue:** Generator scripts build markdown strings inline instead of loading from `assets/` templates.

**Affected Files:**
- `.claude/skills/bmad-product-planning/scripts/generate_prd.py`
- `.claude/skills/bmad-architecture-design/scripts/generate_architecture.py`
- `.claude/skills/bmad-story-planning/scripts/create_story.py`

**Current Behavior:**
Scripts use Python f-strings to build long markdown documents:
```python
def render_prd_content(data):
    return f"""# {data['project_name']} Product Requirements Document

{data['executive_summary']}
...
"""
```

**Expected Behavior** (per CLAUDE.md):
Scripts should load Jinja2 templates from `assets/`:
```python
from pathlib import Path

ASSETS_DIR = Path(__file__).parent.parent / "assets"
template_path = ASSETS_DIR / "prd-template.md.jinja"
template = template_path.read_text()
# ... render with template engine
```

**Impact:**
- ❌ Templates in `assets/` are never used by scripts
- ❌ Modifying output format requires editing Python code
- ❌ No separation between logic and presentation
- ❌ Violates documented "scripts read templates from assets/" pattern

**Workaround:**
Templates in `assets/` are currently used by Claude conversationally when generating artifacts manually, not by the automation scripts.

**Resolution:**
Requires refactoring all 3 generators to:
1. Load templates from `assets/` using relative paths
2. Use a lightweight template engine (can't use Jinja2 due to zero-dependency requirement)
3. Options:
   - Simple string.Template (stdlib)
   - Custom lightweight template renderer
   - Keep inline but extract to separate template files and import

**Estimated Effort:** 4-6 hours

**Priority Justification:**
Medium priority because:
- Scripts still work correctly
- Templates exist for manual usage
- But violates documented architecture
- Makes maintenance harder

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

## Last Updated
2025-10-30 (v2.1.5)

## Contributing
When you discover new issues, add them to this document with:
- Clear description
- Affected files
- Impact assessment
- Proposed resolution
- Priority justification
