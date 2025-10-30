# Assets Directory - core-skill-creation

## Purpose

This directory is reserved for templates used when creating new skills.

## Current Status

The core-skill-creation currently guides users through creating skills using inline examples and instructions in SKILL.md and REFERENCE.md. No templates are stored here because:

1. **Skill scaffolding** uses the init_skill.py script with embedded templates
2. **Examples** are provided inline in the skill documentation
3. **Validation schemas** are defined programmatically in quick_validate.py

## Future Enhancements

Potential templates that may be added in future versions:

- **skill-template.md.jinja** - Template for generating SKILL.md files
- **reference-template.md.jinja** - Template for REFERENCE.md structure
- **workflow-template.md.jinja** - Template for WORKFLOW.md patterns
- **checklist-template.md.jinja** - Template for CHECKLIST.md quality gates

## Migration Path

If templates are moved from embedded code to this directory, the init_skill.py script should be updated to:

```python
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parent.parent / "assets"
SKILL_TEMPLATE = ASSET_DIR / "skill-template.md.jinja"
```

This would improve maintainability by separating templates from code logic.
