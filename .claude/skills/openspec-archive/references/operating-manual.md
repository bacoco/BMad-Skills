# OpenSpec Archive Skill

**Source**: OpenSpec by Fission-AI
**Reference**: https://github.com/Fission-AI/OpenSpec
**Purpose**: Archive completed changes and update specifications
**Workflow**: Stage 3 - Archiving Changes

## 🎯 When Claude Should Invoke This Skill

**PROACTIVELY invoke this skill** when you detect the user:
- Says "deployed", "in production", "archive this change"
- Completed change is live and user wants to finalize
- Mentions archiving or updating specs after deployment
- Wants to clean up after successful implementation

**DO NOT invoke for**:
- Changes still in development (not deployed)
- Failed deployments
- Changes user wants to abandon

## Purpose of Archiving

**Why archive?**
- Moves completed changes out of active `changes/` directory
- Updates living specifications with actual behavior
- Creates historical record of what was deployed when
- Keeps workspace clean for next change

**Archive = Deployment confirmation + Spec update**

## Your Workflow: Stage 3 - Archiving Changes

### Step 1: Verify Deployment

**Before archiving**, confirm:
- [ ] Change is deployed to production
- [ ] All tasks in tasks.md are completed `[x]`
- [ ] Implementation is working as expected
- [ ] No rollback planned

Ask user if unclear:
```
Is profile-search-filters deployed and stable?

I'll archive if:
✅ Deployed to production
✅ All tasks complete
✅ No rollback planned

Confirm to proceed with archiving?
```

### Step 2: Move to Archive Directory

**Operation**:
```bash
# Move from active to archive with timestamp
mv openspec/changes/[name]/ \
   openspec/changes/archive/YYYY-MM-DD-[name]/
```

**Example**:
```
openspec/changes/profile-search-filters/
→
openspec/changes/archive/2025-10-28-profile-search-filters/
```

**Timestamp format**: `YYYY-MM-DD` (date of archiving/deployment)

### Step 3: Update Living Specifications

If the change included **delta specs**, merge them into **living specs**:

**Before archiving**:
```
openspec/changes/profile-search-filters/
  specs/
    profile-search.md    # Delta specs (ADDED/MODIFIED/REMOVED)

openspec/specs/
  profile-search/        # Living specs (current state)
```

**After archiving**:
```
openspec/changes/archive/2025-10-28-profile-search-filters/
  specs/
    profile-search.md    # Historical delta

openspec/specs/
  profile-search/
    spec.md              # Updated with changes from delta
```

### Step 4: Merge Delta Specs

For each delta spec in archived change:

#### ADDED Requirements
Copy new requirements to living spec:
```markdown
# Delta (archived):
## ADDED
### Requirement: Filter by Skills
SHALL return profiles matching ANY selected skill tag.

# Living spec update:
### Requirement: Filter by Skills
SHALL return profiles matching ANY selected skill tag.
#### Scenario: Multiple Skills Selected
...
```

#### MODIFIED Requirements
Replace old with new in living spec:
```markdown
# Delta (archived):
## MODIFIED
### Requirement: Search Results (was: Basic Search)
SHALL now return filtered results based on criteria.

# Living spec update:
### Requirement: Search Results  # ← Updated
SHALL return filtered results based on criteria.  # ← New behavior
```

#### REMOVED Requirements
Delete from living spec:
```markdown
# Delta (archived):
## REMOVED
### Requirement: Deprecated Simple Search
[Old requirement removed]

# Living spec update:
# ← Requirement deleted entirely
```

#### RENAMED Requirements
Update naming in living spec:
```markdown
# Delta (archived):
## RENAMED
### Requirement: Profile Filter (was: User Filter)

# Living spec update:
### Requirement: Profile Filter  # ← New name
SHALL filter profiles by criteria.
```

### Step 5: Run Validation

After updating specs, validate:
```bash
openspec validate --strict
```

This ensures:
- Spec formatting is correct
- All scenarios use `#### Scenario:` (4 hashtags)
- Requirements use normative language (SHALL, MUST, etc.)
- No broken references

If validation fails:
```
⚠️ Validation failed after archiving

Errors:
  - profile-search/spec.md:42 - Scenario missing heading level
  - profile-search/spec.md:58 - Requirement uses "will" instead of "SHALL"

Fixing errors...
✅ Errors fixed, re-validated successfully
```

### Step 6: Update Change Log (Optional)

If project has `CHANGELOG.md`, add entry:
```markdown
## [1.2.0] - 2025-10-28

### Added
- Profile search filters (name, location, skills)
  - See: openspec/changes/archive/2025-10-28-profile-search-filters/

### Changed
- Search now supports multi-criteria filtering

### Fixed
- N/A
```

### Step 7: Report Archive Complete

Template:
```
✅ Archived: profile-search-filters

📦 Archived to: openspec/changes/archive/2025-10-28-profile-search-filters/
📝 Updated specs: openspec/specs/profile-search/spec.md
  - Added 3 new requirements
  - Modified 1 existing requirement
✅ Validation passed

Change is now part of the living specification.
Ready for next change!
```

## Archiving Patterns

### Pattern 1: Simple Archive (No Delta Specs)

If change had no delta specs:
```
✅ Archived: fix-login-timeout

📦 Archived to: openspec/changes/archive/2025-10-28-fix-login-timeout/
📝 No spec updates needed (bug fix)

Change complete!
```

### Pattern 2: Breaking Change Archive

If change was breaking:
```
✅ Archived: api-v2-migration

📦 Archived to: openspec/changes/archive/2025-10-28-api-v2-migration/
📝 Updated specs: openspec/specs/api/
  - REMOVED 5 deprecated endpoints (v1)
  - ADDED 8 new endpoints (v2)
  - MODIFIED authentication flow
⚠️ Breaking change - see migration guide in archived proposal

✅ Validation passed
```

### Pattern 3: Multi-Spec Archive

If change affected multiple specs:
```
✅ Archived: user-profile-redesign

📦 Archived to: openspec/changes/archive/2025-10-28-user-profile-redesign/
📝 Updated specs:
  - openspec/specs/profile-page/ (ADDED 4, MODIFIED 2)
  - openspec/specs/user-settings/ (MODIFIED 1)
  - openspec/specs/profile-api/ (ADDED 2)
✅ All specs validated

Changes merged into living specifications.
```

## Handling Special Cases

### Case 1: Partial Deployment

If only part of change deployed:
```
⚠️ Only tasks 1-3 deployed, task 4 still pending

Options:
1. Archive with note about partial deployment
2. Wait until all tasks deployed
3. Split into two changes (deployed + pending)

Recommended: Wait for full deployment before archiving.
```

### Case 2: Deployment Rollback

If deployment was rolled back:
```
⚠️ Change rolled back due to production issue

NOT archiving - change failed deployment.

Options:
1. Keep in active changes/ for bug fixes
2. Delete change entirely
3. Create new change to fix issues

What would you like to do?
```

### Case 3: Specs Conflict

If living specs changed since proposal created:
```
⚠️ Conflict detected during archive

Living spec changed:
  - openspec/specs/profile-search/spec.md modified externally
  - Conflicts with archived delta specs

Manual merge required.

Showing diff...
```

## Validation Details

After archiving, validation checks:

**Formatting**:
- Scenarios use `#### Scenario:` (4 hashtags) ✓
- Requirements before scenarios ✓
- Proper markdown structure ✓

**Content**:
- Normative language (SHALL, MUST, SHOULD, MAY) ✓
- At least one scenario per requirement ✓
- No orphaned scenarios ✓

**References**:
- All internal links valid ✓
- No broken references to removed requirements ✓

## Communication Style

- **Confirm before archiving** - Deployment status is critical
- **Show what was updated** - List spec changes clearly
- **Report validation** - Users need to know specs are valid
- **Archive = Done** - This is the final step, celebrate completion!

## Examples

### Example 1: Profile Search Filters

**User**: "Deployed to prod, everything working great!"

**Your Response**:
```
Great! Let me archive profile-search-filters...

✅ Moving to archive...
  openspec/changes/profile-search-filters/
  → openspec/changes/archive/2025-10-28-profile-search-filters/

✅ Updating living specs...
  openspec/specs/profile-search/spec.md:
    - ADDED: Requirement "Filter by Name"
    - ADDED: Requirement "Filter by Location"
    - ADDED: Requirement "Filter by Skills"
    - MODIFIED: Requirement "Search Results" (now includes filtering)

✅ Validating specs...
  All validations passed ✓

✅ Archived successfully!

Change is now part of your living specification.
Ready for the next feature! 🎉
```

### Example 2: Bug Fix (No Specs)

**User**: "Bug fix deployed"

**Your Response**:
```
✅ Archiving fix-login-timeout...

📦 Moved to: openspec/changes/archive/2025-10-28-fix-login-timeout/
📝 No spec updates (bug fix didn't change behavior)

✅ Archived!

Bug fix complete and documented.
```

## CLI Command Equivalent

If OpenSpec CLI is available:
```bash
openspec archive profile-search-filters --yes
```

This automates the archiving process.

## Next Steps

After archiving:
- Start new change with `openspec-propose`
- List all changes with `openspec list`
- View archived changes in `openspec/changes/archive/`

---

**Remember**: Archiving is the **final confirmation** that a change is done, deployed, and now part of your system's living specification. It closes the loop on the OpenSpec workflow.
