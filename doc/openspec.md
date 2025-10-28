# OpenSpec Workflow

**Version**: 1.0.0
**Source**: [OpenSpec by Fission-AI](https://github.com/Fission-AI/OpenSpec)

OpenSpec is a **lightweight workflow for simple changes** - the fast alternative to BMAD when you don't need full PRD/Architecture/Stories.

---

## When to Use OpenSpec

Use OpenSpec instead of BMAD when:

✅ **Level 0-1 Projects**:
- Bug fixes
- Small features (1-5 functional requirements)
- Simple modifications to existing code
- Configuration changes
- Adding a filter, button, or simple UI element

❌ **Do NOT use for**:
- New products (use BMAD)
- Complex features with 8+ requirements (use BMAD)
- Greenfield projects needing architecture (use BMAD)
- Features requiring multiple epics (use BMAD)

---

## OpenSpec vs BMAD

| Aspect | OpenSpec (L0-1) | BMAD (L2-4) |
|--------|----------------|-------------|
| **Speed** | Hours to days | Days to weeks |
| **Documents** | Proposal, Tasks | PRD, Architecture, Epics, Stories |
| **Workflow** | 3 stages | 4 phases |
| **Overhead** | Minimal | Comprehensive |
| **Best for** | Existing projects, incremental changes | New products, complex features |
| **Skills** | 3 (propose, implement, archive) | 7 (analyst, pm, ux, arch, tea, stories, dev) |

---

## The 3 Stages

### Stage 1: Creating Changes (openspec-propose)

**Triggered by**: "Add a...", "Fix the...", "Change the..."

**Creates**:
```
openspec/changes/[feature-name]/
  ├── proposal.md        # Why, what, impact
  ├── tasks.md           # Sequential checklist
  ├── design.md          # Technical design (optional)
  └── specs/             # Delta specifications
      └── [spec].md      # ADDED/MODIFIED/REMOVED changes
```

**proposal.md** - The "Why":
- Problem statement
- Proposed solution
- Success criteria
- Breaking changes?
- Alternatives considered

**tasks.md** - The "How":
- Sequential, actionable tasks
- Each task = one testable action
- Includes tests and documentation tasks

**Delta specs** - The "What Exactly":
- ADDED: New requirements/scenarios
- MODIFIED: Changed requirements
- REMOVED: Deleted requirements
- RENAMED: Name changes

**Approval Gate**: ⚠️ Must be approved before implementation

### Stage 2: Implementing Changes (openspec-implement)

**Triggered by**: User approves proposal

**Process**:
1. Load proposal.md, tasks.md, design.md, delta specs
2. Execute tasks sequentially
3. Check off each task in tasks.md
4. Write tests for every change
5. Update documentation
6. Report progress after each task

**Critical Rule**: Follow tasks.md in exact order - no skipping

### Stage 3: Archiving Changes (openspec-archive)

**Triggered by**: Change deployed to production

**Process**:
1. Move `changes/[name]/` → `changes/archive/YYYY-MM-DD-[name]/`
2. Merge delta specs into living specs
3. Validate updated specs
4. Update changelog (optional)

**Result**: Change is now part of living specification

---

## Example: Add Profile Search Filters

### User Request
"Add search filters to the profile page - let users filter by name, location, and skills"

### Orchestrator Assessment
```
Analyzing request...

Complexity: Level 1 (simple feature, ~3 requirements)
Workflow: OpenSpec ✅

This is perfect for OpenSpec!
Let me create a change proposal...
```

### Stage 1: Proposal (openspec-propose)

**Creates**: `openspec/changes/profile-search-filters/`

**proposal.md**:
```markdown
# Proposal: Profile Search Filters

## Why
Users need to quickly find profiles matching specific criteria.
Currently all profiles are listed without filtering ability.

## What
Add filter UI to profile page with:
- Name text search
- Location dropdown
- Skills multi-select

Filter logic: AND between types (name AND location), OR within skills

## Impact
- **Breaking Changes**: No
- **Affected Components**: ProfilePage, SearchService
- **Dependencies**: None (use existing UI library)

## Success Criteria
- [ ] Users can filter by name (case-insensitive)
- [ ] Users can filter by location
- [ ] Users can filter by multiple skills (OR logic)
- [ ] Filters work together (AND logic)
- [ ] Empty results show "No matches found"
```

**tasks.md**:
```markdown
# Implementation Tasks

- [ ] Add ProfileFilter component to profile page UI
- [ ] Implement filterProfiles() in SearchService
- [ ] Add tests for all filter combinations
- [ ] Update profile page documentation
```

**Presents to user**:
```
I've created an OpenSpec proposal for profile-search-filters:

📋 Why: Users need to quickly find profiles
📋 What: Add filterable search (name, location, skills)
📋 Impact: Non-breaking, adds new feature

✅ 4 tasks total (UI, logic, tests, docs)

Approve to proceed with implementation?
```

### Stage 2: Implementation (openspec-implement)

**User**: "Approved, implement it"

```
Starting implementation...

Task 1: Add ProfileFilter component
✅ Created src/components/ProfileFilter.tsx
✅ Added filter UI with inputs
✅ Integrated into ProfilePage

Task 2: Implement filterProfiles()
✅ Modified src/services/searchService.ts
✅ AND logic between filter types
✅ OR logic for skills

Task 3: Add tests
✅ Created tests/profileFilter.test.ts
✅ 12 tests covering all scenarios
✅ All tests passing ✓

Task 4: Update documentation
✅ Updated docs/profile-page.md
✅ Added filter usage examples

✅ All 4 tasks complete!

Files changed:
  - src/components/ProfileFilter.tsx (new)
  - src/services/searchService.ts (modified)
  - tests/profileFilter.test.ts (new)
  - docs/profile-page.md (updated)

Ready for deployment!
```

### Stage 3: Archive (openspec-archive)

**User**: "Deployed to prod"

```
Archiving profile-search-filters...

✅ Moved to: openspec/changes/archive/2025-10-28-profile-search-filters/

✅ Updated living specs:
  openspec/specs/profile-search/spec.md:
    - ADDED: Requirement "Filter by Name"
    - ADDED: Requirement "Filter by Location"
    - ADDED: Requirement "Filter by Skills"
    - MODIFIED: Requirement "Search Results"

✅ Validation passed

✅ Archived successfully!
Change is now part of living specification.
```

---

## Key Concepts

### Spec-Driven Development

**Principle**: Agree on what to build BEFORE writing code

- Specs define expected behavior
- Implementation follows specs exactly
- Tests verify specs are met
- Living specs evolve with each change

### Delta Specifications

Changes are expressed as **deltas** to existing specs:

```markdown
## ADDED
### Requirement: New Feature X
SHALL do Y when Z.

## MODIFIED
### Requirement: Updated Feature (was: Old Feature)
SHALL now do Y2 instead of Y1.

## REMOVED
### Requirement: Deprecated Feature
[No longer supported]
```

### Living Specifications

Specs are **always current** with deployed code:

- Active changes in `openspec/changes/`
- Deployed changes in `openspec/changes/archive/YYYY-MM-DD-[name]/`
- Current behavior in `openspec/specs/`

After archiving, specs reflect what's actually in production.

### Normative Language

Requirements use precise language:

- **SHALL** / **MUST**: Required behavior
- **SHOULD**: Recommended behavior
- **MAY**: Optional behavior
- **SHALL NOT** / **MUST NOT**: Forbidden behavior

### Scenarios

Every requirement has ≥1 scenario:

```markdown
### Requirement: Filter by Skills
SHALL return profiles matching ANY selected skill.

#### Scenario: Multiple Skills Selected
GIVEN user selects ["React", "TypeScript"]
WHEN search executes
THEN return profiles with React OR TypeScript
```

Format: GIVEN-WHEN-THEN or narrative description

---

## Best Practices

### 1. Keep Changes Small

OpenSpec is for **incremental changes**:
- One feature at a time
- Clear scope in proposal
- If scope grows → consider BMAD instead

### 2. Sequential Tasks

Order tasks logically:
```markdown
- [ ] Add component
- [ ] Implement logic
- [ ] Write tests  ← Tests after implementation
- [ ] Update docs ← Docs last
```

### 3. Approval Gate

**NEVER skip approval**:
- User must explicitly approve proposal
- No assumptions
- If unclear, ask before implementing

### 4. Test Everything

Every change needs tests:
- Unit tests for new functions
- Integration tests for workflows
- Edge cases from scenarios

### 5. Document the Change

Update docs immediately:
- README changes
- API documentation
- Migration guides (if breaking)

### 6. Archive After Deployment

Only archive when:
- Change is deployed
- All tasks complete
- Working in production
- No rollback planned

---

## Commands

If OpenSpec CLI is available:

```bash
# List active changes
openspec list

# Validate changes
openspec validate [name] --strict

# Archive change
openspec archive <change-id> --yes
```

Otherwise, Claude manages files directly.

---

## Troubleshooting

### "Scope is growing"

If tasks keep multiplying:
```
⚠️ This change is growing in scope.

Originally: 4 tasks
Now: 12 tasks

Recommendation: Switch to BMAD workflow
  - Create PRD for complete planning
  - Define architecture properly
  - Break into multiple stories

Switch to BMAD?
```

### "Approval missing"

If implementation starts without approval:
```
⚠️ Proposal not approved yet

Please review openspec/changes/[name]/proposal.md

Approve before implementation?
```

### "Validation failed"

If specs don't validate:
```
⚠️ Validation errors:
  - Scenario missing #### heading (line 42)
  - Requirement uses "will" instead of "SHALL" (line 58)

Fixing automatically...
✅ Fixed and re-validated
```

---

## When to Switch to BMAD

Switch from OpenSpec to BMAD if:

- Scope grows beyond 5-7 requirements
- Need architectural decisions
- Multiple epics emerging
- Greenfield project (not brownfield modification)
- Complex system design required
- Multiple team coordination needed

Orchestrator will recommend switch when complexity increases.

---

## Files Created

### Active Changes
```
openspec/changes/
  └── [feature-name]/
      ├── proposal.md
      ├── tasks.md
      ├── design.md (optional)
      └── specs/
          └── [component].md
```

### Archived Changes
```
openspec/changes/archive/
  └── YYYY-MM-DD-[feature-name]/
      ├── proposal.md
      ├── tasks.md
      └── specs/
          └── [component].md (delta)
```

### Living Specs
```
openspec/specs/
  └── [component]/
      └── spec.md (current behavior)
```

---

## Next Steps

1. **Start a simple change**: Just describe what you want to add/fix
2. **Orchestrator assesses**: Determines if OpenSpec (L0-1) or BMAD (L2-4)
3. **Follow the flow**: Propose → Implement → Archive
4. **Keep iterating**: Each change adds to living specs

OpenSpec makes simple changes **fast and documented** without BMAD's overhead.
