# Scripts Directory - bmad-discovery-research

## Purpose

This directory is reserved for future automation scripts related to research and ideation.

## Current Status

The bmad-discovery-research skill currently operates through collaborative conversation using templates in `assets/`. No automation scripts are required at this time because:

1. **Brainstorming sessions** are most effective when done collaboratively through conversation
2. **Product briefs** are generated using Jinja2 templates from user input
3. **Research dossiers** compile information gathered through interactive discussion

## Future Enhancements

Potential scripts that may be added in future versions:

- **market_research.py** - Automated competitor analysis and market data gathering
- **trend_analyzer.py** - Analyze industry trends from external data sources
- **idea_scorer.py** - Score and rank brainstormed ideas based on defined criteria
- **research_aggregator.py** - Aggregate research findings from multiple sources

## Contributing

When adding scripts to this directory, follow the BMAD path resolution standards:

```python
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
ARTIFACTS_DIR = RUNTIME_ROOT / "artifacts"
```

All research artifacts should be written to the `_runtime/workspace/artifacts/` directory.
