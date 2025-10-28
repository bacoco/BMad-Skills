# Complete Workflow Example

## Scenario: E-commerce Product Catalog (Level 3)

### 1. Initialize

```
User: "Initialize BMAD workflow for E-commerce Product Catalog"

Orchestrator:
- Asks questions (what, how complex, timeline)
- Determines: Level 3, Greenfield
- Creates workflow-status.md
- Recommends: "Start with Planning (bmad-pm)"
```

### 2. Planning

```
User: "Create PRD and epics"

bmad-pm:
- Asks clarifying questions
- Gathers: Goals, FRs, NFRs, User Journeys
- Generates PRD: 15 FRs, 3 Epics
- Generates Epics:
  - Epic 1: Foundation & Auth (5 stories)
  - Epic 2: Product Management (8 stories)
  - Epic 3: Shopping Cart (7 stories)
- Total: 20 stories
- Saves: docs/PRD.md, docs/epics.md

Orchestrator:
- Marks Planning complete
- Updates phase to Solutioning
- Recommends: "Create Architecture (bmad-architecture)"
```

### 3. Solutioning

```
User: "Create architecture"

bmad-architecture:
- Reads PRD completely
- Searches for Next.js starter (WebSearch)
- Makes decisions:
  - Stack: Next.js 15, TypeScript, Prisma, tRPC
  - Structure: /app router, /lib utilities
  - Patterns: Server actions, optimistic updates
  - Error handling: Structured responses
  - Testing: Vitest + Playwright
- Generates: docs/ARCHITECTURE.md

Orchestrator:
- Marks Solutioning complete
- Initializes sprint-status.yaml from epics.md
- 20 stories loaded, all "backlog"
- Updates phase to Implementation
- Recommends: "Create first story (bmad-stories)"
```

### 4. Story Creation

```
User: "Create next story"

Orchestrator: Next backlog story is "1-1-project-setup"

bmad-stories:
- Loads PRD, Architecture, Epics
- No previous story (first in epic)
- Extracts Story 1.1 from epics
- Creates tasks from ACs
- Writes dev notes with architecture patterns
- Generates: stories/1-1-project-setup.md

Orchestrator:
- Updates sprint-status: 1-1-project-setup → "drafted"
- Recommends: "Implement story 1-1-project-setup (bmad-dev)"
```

### 5. Implementation (Story 1.1)

```
User: "Implement story 1-1-project-setup"

bmad-dev:
- Loads story file completely
- Loads architecture patterns
- No previous story
- Implements:
  - Runs Next.js create command
  - Configures TypeScript
  - Sets up Prisma
  - Initializes tests
  - Configures ESLint/Prettier
- Writes tests
- Runs tests → All passing
- Updates Dev Agent Record:
  - Files created: package.json, tsconfig.json, prisma/schema.prisma, etc.
  - Patterns established: Server actions pattern
  - Technical debt: None
  - Warnings for next: "Database URL must be configured"
- Marks story "in-progress" → "done"

Orchestrator:
- Updates sprint-status: 1-1-project-setup → "done"
- Recommends: "Create next story 1-2-user-authentication (bmad-stories)"
```

### 6. Story Creation (Story 1.2)

```
User: "Create next story"

bmad-stories:
- Loads Story 1.1 file completely
- Extracts Previous Story Learnings:
  - Server actions pattern established
  - Prisma schema exists
  - Warning: DB URL needed
- Creates Story 1.2 with:
  - Learnings section referencing 1.1
  - Tasks use existing patterns
  - Notes about DB configuration
- Generates: stories/1-2-user-authentication.md

Orchestrator:
- Updates sprint-status: 1-2-user-authentication → "drafted"
```

### 7. Continue...

Repeat steps 5-6 for all 20 stories across 3 epics.

### 8. Done!

```
Orchestrator: "All stories complete! 🎉 Project done."
```
