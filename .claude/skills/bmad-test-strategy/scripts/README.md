# Scripts Directory - bmad-test-strategy

## Purpose

This directory is reserved for future automation scripts related to test strategy and quality assurance.

## Current Status

The bmad-test-strategy skill currently generates test artifacts through template-based conversation workflows. No automation scripts are required at this time because:

1. **Test strategy documents** are created using Jinja2 templates in `assets/`
2. **ATDD scenarios** are defined through conversational refinement with the user
3. **Quality checklists** are tailored to each project's specific requirements

## Future Enhancements

Potential scripts that may be added in future versions:

- **generate_test_strategy.py** - Auto-generate test strategy from architecture decisions
- **validate_atdd_scenarios.py** - Lint and validate ATDD scenario syntax
- **quality_metrics.py** - Aggregate quality metrics from test results and coverage reports
- **test_gap_analyzer.py** - Identify untested code paths and suggest test cases

## Contributing

When adding scripts to this directory, follow the BMAD path resolution standards:

```python
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime"
DEFAULT_OUTPUT_DIR = RUNTIME_ROOT / "artifacts"
```

All test artifacts should be written to the `_runtime/artifacts/` directory.
