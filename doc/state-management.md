# State Management

## workflow-status.md Structure

```markdown
# BMM Workflow Status

**Project**: E-commerce Product Catalog
**Type**: Greenfield
**Level**: 3
**Created**: 2025-10-28
**Owner**: User

## Current Status

**Phase**: Implementation
**Status**: In Progress
**Last Updated**: 2025-10-28

## Phase Progress

### Phase 1: Analysis
Status: Skipped (Optional for Level 3)

### Phase 2: Planning
- [x] PRD
- [x] Epics Breakdown
Status: Complete

### Phase 3: Solutioning
- [x] Architecture
Status: Complete

### Phase 4: Implementation
- [x] Story Creation (ongoing)
- [ ] Story Implementation (in progress)
Status: In Progress

## Next Recommended Action

Create next story with bmad-stories skill

## Artifacts Created

- docs/PRD.md - Product Requirements Document (2025-10-28)
- docs/epics.md - Epic Breakdown (2025-10-28)
- docs/ARCHITECTURE.md - Technical Architecture (2025-10-28)
- docs/sprint-status.yaml - Sprint Tracking (2025-10-28)
- stories/1-1-project-setup.md - Story 1.1 (2025-10-28)
```

## sprint-status.yaml Structure

```yaml
project_metadata:
  created: '2025-10-28'
  last_updated: '2025-10-28'
  total_epics: 3
  total_stories: 20

epic_status:
  epic-1:
    title: Foundation & Auth
    total_stories: 5
    completed: 1
    in_progress: 1
    status: in-progress

development_status:
  1-1-project-setup:
    title: Project Setup
    status: done
    assigned_to: Claude
    started: '2025-10-28'
    completed: '2025-10-28'

  1-2-user-authentication:
    title: User Authentication
    status: drafted
    assigned_to: null
    started: null
    completed: null

  # ... (18 more stories)
```

## Python Helpers

### workflow_status.py

```bash
# Initialize workflow
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py init \
  "Project Name" "greenfield" 3 "User"

# Update phase
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py update-phase "Planning"

# Mark phase complete
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py mark-complete "Planning"

# Add artifact
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py add-artifact \
  "docs/PRD.md" "Product Requirements Document"

# Get current phase
python .claude/skills/bmad-orchestrator/helpers/workflow_status.py get-phase
```

### sprint_status.py

```bash
# Initialize from epics
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py init docs/epics.md

# Update story status
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py update \
  "1-1-project-setup" "in-progress" "Claude"

# Get next backlog story
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py next-backlog

# List stories by status
python .claude/skills/bmad-orchestrator/helpers/sprint_status.py list-status "backlog"
```
