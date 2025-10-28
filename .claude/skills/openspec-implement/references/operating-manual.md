# OpenSpec Implement Skill

**Source**: OpenSpec by Fission-AI
**Reference**: https://github.com/Fission-AI/OpenSpec
**Purpose**: Implement approved OpenSpec change proposals
**Workflow**: Stage 2 - Implementing Changes

## 🎯 When Claude Should Invoke This Skill

**PROACTIVELY invoke this skill** when you detect the user:
- Approves an OpenSpec proposal ("yes, implement it", "proceed", "approved")
- Says "implement the change", "execute the tasks", "build it"
- References an existing proposal and wants implementation
- Has completed proposal review and wants to code

**DO NOT invoke for**:
- Before proposal is approved (block with approval gate)
- Creating new proposals (use openspec-propose)
- Archiving completed changes (use openspec-archive)

## Critical Rules

### ⚠️ Approval Gate - DO NOT SKIP

**NEVER start implementation until**:
- [ ] Proposal exists in `openspec/changes/[name]/proposal.md`
- [ ] User has explicitly approved the proposal
- [ ] Tasks are defined in `openspec/changes/[name]/tasks.md`

If not approved, respond:
```
⚠️ This proposal hasn't been approved yet.

Please review openspec/changes/[name]/proposal.md

Would you like to:
1. Approve and proceed with implementation?
2. Make changes to the proposal first?
```

## Your Workflow: Stage 2 - Implementing Changes

### Step 1: Load Supporting Documents

Read in this order:
1. **`proposal.md`** - Understand why and what
2. **`tasks.md`** - Get sequential task list
3. **`design.md`** - Technical approach (if exists)
4. **Delta specs** - Exact behavior requirements (if exist)

### Step 2: Verify Current State

Before starting:
- Check existing codebase structure
- Identify affected files/components
- Verify dependencies are available
- Ensure tests can run

### Step 3: Execute Tasks Sequentially

**CRITICAL**: Follow `tasks.md` in exact order.

For each task:
1. **Read the task** - Understand what's required
2. **Implement** - Write code following specs
3. **Test** - Verify it works
4. **Check off** - Update tasks.md with `[x]`

**Update tasks.md continuously**:
```markdown
# Implementation Tasks

- [x] Task 1: Add filter component to profile page ✓
- [x] Task 2: Implement filter logic in search service ✓
- [ ] Task 3: Write tests for filter combinations ← CURRENT
- [ ] Task 4: Update profile page documentation
```

### Step 4: Follow Specifications Exactly

If delta specs exist in `specs/`, they are **source of truth**.

Example spec:
```markdown
### Requirement: Filter by Skills
SHALL return profiles matching ANY selected skill tag.

#### Scenario: Multiple Skills Selected
GIVEN user selects ["React", "TypeScript"]
WHEN search executes
THEN return profiles with React OR TypeScript
```

Your implementation MUST match this behavior exactly.

### Step 5: Write Tests

Every change MUST have tests:
- Unit tests for new functions
- Integration tests for workflows
- Edge case coverage from specs

**DO NOT skip tests** - they're in tasks.md for a reason.

### Step 6: Update Documentation

If tasks.md includes documentation:
- Update README
- Update API docs
- Update inline comments
- Update migration guides (if breaking)

### Step 7: Mark Task Complete

Update tasks.md after EACH task:
```markdown
- [x] Task 3: Write tests for filter combinations ✓
```

### Step 8: Report Progress

After each task, briefly report:
```
✅ Task 3 complete: Write tests for filter combinations
  - Added 12 unit tests covering all filter scenarios
  - All tests passing ✓

Next: Task 4 - Update profile page documentation
```

### Step 9: Final Verification

When all tasks complete:
- [ ] All tasks checked off in tasks.md
- [ ] All tests passing
- [ ] No breaking changes (unless documented)
- [ ] Documentation updated
- [ ] Code follows project conventions

### Step 10: Present Completion

Template:
```
✅ OpenSpec change "[name]" fully implemented!

📁 Files changed:
  - src/components/ProfileFilter.tsx (new)
  - src/services/searchService.ts (modified)
  - tests/profileFilter.test.ts (new)
  - docs/profile-page.md (updated)

✅ All tasks completed (4/4)
✅ All tests passing (12 new tests)
✅ Documentation updated

Ready to:
1. Review the implementation
2. Deploy and archive (openspec-archive)
3. Make additional changes
```

## Implementation Patterns

### Pattern 1: Read Specs, Then Code

**DO**:
```typescript
// Read spec first:
// "SHALL return profiles matching ANY selected skill"

const filteredProfiles = profiles.filter(profile =>
  selectedSkills.some(skill => profile.skills.includes(skill))
)
```

**DON'T** (guessing behavior):
```typescript
// What should this do? AND or OR? Not sure...
const filteredProfiles = profiles.filter(profile =>
  selectedSkills.every(skill => profile.skills.includes(skill))
)
```

### Pattern 2: Incremental Testing

After each task:
```bash
npm test -- --run
```

Don't wait until the end - test continuously.

### Pattern 3: Checklist-Driven Development

```markdown
- [ ] Task 2: Implement filter logic
  - [x] Parse selected filters
  - [x] Query database with filters
  - [x] Return filtered results
  - [ ] Handle empty results ← Still working
```

Sub-tasks help track progress within larger tasks.

## Handling Blockers

If you get blocked:

**Missing Information**:
```
⚠️ Blocker on Task 3: Database schema unclear

The spec requires filtering by skills, but I don't see a
skills field in the current User schema.

Options:
1. Add skills array to User model
2. Create separate Skills table with relations
3. Clarify expected schema

Which approach should I take?
```

**Conflicting Requirements**:
```
⚠️ Conflict detected:

Proposal says "non-breaking" but Task 2 requires changing
the search API signature from searchProfiles() to
searchProfiles(filters).

This is a breaking change for existing callers.

Should I:
1. Make it non-breaking (optional filters parameter)
2. Update proposal to mark as breaking
3. Different approach?
```

**Technical Limitation**:
```
⚠️ Technical constraint:

Task 4 requires server-side filtering, but the current
architecture uses client-side filtering for all searches.

This would require significant refactoring.

Recommend:
1. Update proposal to use client-side filtering
2. Create separate change for search architecture
3. Implement server-side just for this feature

Your preference?
```

## Examples

### Example 1: Profile Search Filters

**Proposal approved**: `openspec/changes/profile-search-filters/`

**Implementation**:

```
Starting implementation of profile-search-filters...

Task 1: Add filter component to profile page
✅ Created src/components/ProfileFilter.tsx
✅ Added filter UI with name, location, skills inputs
✅ Integrated into ProfilePage component

Task 2: Implement filter logic in search service
✅ Modified src/services/searchService.ts
✅ Added filterProfiles() function with multi-criteria support
✅ Handles AND logic for different filter types (name AND location)
✅ Handles OR logic for skills (React OR TypeScript)

Task 3: Write tests for filter combinations
✅ Created tests/profileFilter.test.ts
✅ 12 tests covering:
  - Single filter scenarios
  - Multiple filter combinations
  - Empty results handling
  - Edge cases (special characters, case sensitivity)
✅ All tests passing ✓

Task 4: Update profile page documentation
✅ Updated docs/profile-page.md with filter usage
✅ Added screenshots of filter UI
✅ Documented filter behavior (AND/OR logic)

✅ All 4 tasks complete! Ready for deployment.
```

### Example 2: Bug Fix (No Proposal)

**User**: "Fix the login timeout bug"

**Your Response**:
```
This is a simple bug fix - I'll implement directly without proposal.

Identified issue:
  - File: src/auth/session.ts:42
  - Problem: Timeout value hardcoded to 30min instead of 1hr
  - Fix: Update SESSION_TIMEOUT constant

✅ Fixed:
  - Changed SESSION_TIMEOUT from 1800000 to 3600000
  - Added test to verify 1hr timeout
  - Updated comment to clarify timeout duration

✅ Tests passing
No proposal needed for this simple fix.
```

## Continuous Execution

**Execute tasks WITHOUT pausing** unless:
- Blocked (missing info, conflict, limitation)
- Error occurs
- User interrupts

Don't ask permission between tasks - the approval was already given.

## Communication Style

- **Task-by-task updates** - Report after each completion
- **Show what changed** - List modified files
- **Cite specs** - Reference requirements you're implementing
- **Be efficient** - OpenSpec is lightweight, keep it moving

## When to Stop

**Stop and ask** if:
- Scope is expanding beyond original proposal
- Breaking changes emerging (when marked non-breaking)
- Technical approach isn't working
- Tests failing and can't resolve

**Otherwise, execute fully** until all tasks done.

## Next Steps

After implementation complete:
- User deploys → Invoke `openspec-archive` skill to archive change
- User wants changes → Make adjustments, update tasks.md
- User adds more tasks → Update tasks.md and continue

---

**Remember**: OpenSpec implementation is **task-driven and sequential**. Follow the checklist, test continuously, and update as you go. No surprises - everything was planned in the proposal.
