# BMAD Global Workflow

## Step-by-Step Process

### Step 1: Intent Recognition
Parse user input to identify:
- What they want to accomplish
- Current project state
- Urgency and scope
- Existing context

### Step 2: Complexity Assessment
Classify as Level 0-4:
- Level 0-1 → OpenSpec
- Level 2 → BMAD Planning
- Level 3-4 → BMAD Discovery

### Step 3: State Check
Check for existing workflow state:
- Read `workflow-status.md`
- Identify current phase
- List completed artifacts

### Step 4: Routing Decision
Route to appropriate skill:
- Status request → workflow-router
- New Level 0-1 → openspec-change-proposal
- New Level 3-4 → bmad-discovery-research
- New Level 2 → bmad-product-planning
- Continue → next pending phase

### Step 5: Execution
Invoke the selected sub-skill and wait for completion.

### Step 6: State Update
Update workflow status with:
- Completed phase
- Created artifacts
- Next recommended action

### Step 7: Guidance
Provide user with:
- Summary of what was accomplished
- Next steps
- Estimated time for next phase

## Decision Tree

```
User Input
    ↓
[Status Request?] → Yes → workflow-router
    ↓ No
[Existing State?] → Yes → Resume from current phase
    ↓ No
[Assess Complexity]
    ↓
[Level 0-1?] → Yes → OpenSpec
    ↓ No
[Level 2?] → Yes → Planning → Architecture → Testing → Stories → Dev
    ↓ No
[Level 3-4?] → Yes → Discovery → Planning → [UX] → Architecture → Testing → Stories → Dev
```

## Phase Transitions

Each phase transition checks prerequisites:

**Before Planning:**
- ✅ Discovery brief (Level 3-4)
- ✅ Problem statement clear

**Before UX:**
- ✅ PRD exists
- ✅ User-facing features identified

**Before Architecture:**
- ✅ PRD exists
- ✅ [UX specs if applicable]

**Before Testing:**
- ✅ Architecture complete
- ✅ Requirements clear

**Before Stories:**
- ✅ Architecture complete
- ✅ [Test strategy recommended]

**Before Development:**
- ✅ Stories created
- ✅ Acceptance criteria defined

## Iterative Refinement

After any phase, user can request:
- "Let's refine the [artifact]"
- "Go back to [phase]"
- "Skip [phase]"

BMAD Global adapts to the request.
