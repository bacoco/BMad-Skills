# Scripts Directory - bmad-ux-design

## Purpose

This directory is reserved for future automation scripts related to UX design and wireframing.

## Current Status

The bmad-ux-design skill currently creates design artifacts through template-based conversations. No automation scripts are required at this time because:

1. **User flows** are collaboratively designed through conversation with the user
2. **Wireframes** are described using ASCII art and markdown templates in `assets/`
3. **Design systems** are defined conversationally based on project requirements and brand guidelines

## Future Enhancements

Potential scripts that may be added in future versions:

- **generate_user_flows.py** - Auto-generate user flow diagrams from PRD requirements
- **wireframe_to_code.py** - Convert ASCII wireframes to HTML/React component scaffolds
- **design_system_validator.py** - Validate consistency across wireframes and design system
- **accessibility_checker.py** - Analyze UX artifacts for WCAG compliance

## Visual Design Tools

For more sophisticated visual wireframing, consider integrating with external tools:

- **Figma API** - Export wireframes from Figma designs
- **Excalidraw** - Generate SVG wireframes programmatically
- **PlantUML** - Create user flow diagrams

## Contributing

When adding scripts to this directory, follow the BMAD path resolution standards:

```python
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime"
DEFAULT_OUTPUT_DIR = RUNTIME_ROOT / "artifacts"
```

All UX artifacts should be written to the `_runtime/artifacts/` directory.
