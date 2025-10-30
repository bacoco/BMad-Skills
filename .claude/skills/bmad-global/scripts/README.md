# Scripts Directory - bmad-global

## Purpose

This directory is reserved for future automation scripts related to global workflow orchestration.

## Current Status

BMAD Global currently operates through intelligent routing and conversation orchestration. No automation scripts are required at this time because:

1. **Routing logic** is implemented conversationally based on user intent
2. **State management** is handled by the main-workflow-router sub-skill
3. **Sub-skill invocation** happens through Claude's skill system
4. **Workflow coordination** is managed through conversation flow

## Future Enhancements

Potential scripts that may be added in future versions:

### workflow_analyzer.py
Analyze completed workflows to provide insights:
- Average duration per phase
- Most common phase sequences
- Bottleneck identification
- Success rate by complexity level

### auto_router.py
Automated routing logic that can be tested independently:
- Input: User intent + current state
- Output: Recommended skill + confidence score
- Useful for testing routing decisions

### workflow_validator.py
Validate workflow state consistency:
- Check all prerequisites met
- Verify artifact existence
- Validate phase transitions
- Detect incomplete workflows

### bulk_status.py
Generate status reports for multiple projects:
- Aggregate status across projects
- Team-level progress tracking
- Resource allocation insights

## Contributing

When adding scripts to this directory, follow the BMAD path resolution standards:

```python
from pathlib import Path

SKILLS_ROOT = Path(__file__).resolve().parents[2]  # .claude/skills/
RUNTIME_ROOT = SKILLS_ROOT / "_runtime" / "workspace"
ARTIFACTS_DIR = RUNTIME_ROOT / "artifacts"
```

All workflow artifacts should be written to the `_runtime/workspace/artifacts/` directory.

## Integration Points

Scripts should integrate with:
- Sub-skill status files
- Workflow status tracking
- Artifact storage
- State management

## Testing

Scripts should be testable independently using:
```bash
pytest .claude/skills/bmad-global/scripts/test_*.py
```
