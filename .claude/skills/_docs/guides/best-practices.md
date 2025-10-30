# Best Practices

## 1. Always Start with Orchestrator

```
User: "Initialize BMAD workflow"
```

Don't skip initialization - it sets up state management.

## 2. Check Status Frequently

```
User: "What's my BMAD status?"
```

Orchestrator reads state files and recommends next action.

## 3. Complete Phases in Order

- Phase 1: Analysis (optional)
- Phase 2: Planning (required L2-4)
- Phase 3: Solutioning (required L2-4)
- Phase 4: Implementation (iterative)

## 4. Let Orchestrator Manage State

Don't manually edit workflow-status.md or sprint-status.yaml. Let orchestrator and skills update them.

## 5. Story Learnings are Critical

bmad-story-planning ALWAYS checks previous story. This prevents:
- Recreating existing code
- Ignoring technical debt
- Missing architectural decisions

## 6. Dev Agent Record is Mandatory

bmad-development-execution MUST update Dev Agent Record as implementation progresses. Next story depends on it.

## 7. Tests are Not Optional

bmad-development-execution will NOT mark story complete unless:
- All tests written
- All tests passing 100%
- No cheating

---

# Troubleshooting

## "Workflow status file not found"

**Problem**: No workflow-status.md exists

**Solution**: Run workflow initialization:
```
Initialize BMAD workflow
```

## "Sprint status file not found"

**Problem**: No sprint-status.yaml exists

**Solution**: Orchestrator should initialize after epics created. Or manually:
```
Initialize sprint status
```

## "Story has no previous learnings"

**Problem**: Story doesn't reference previous story

**Solution**: bmad-story-planning should automatically check. If missing, manually read previous story and include learnings.

## "Tests not running"

**Problem**: bmad-development-execution not executing tests

**Solution**: Ensure test framework initialized (bmad-test-strategy). Verify tests exist. Dev agent MUST run tests, no exceptions.
