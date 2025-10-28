# BMAD + OpenSpec Workflow Skills for Claude

**Version**: 3.0.0 - Dual Workflow System
**Sources**:
- [BMAD Method v6-alpha](https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)
- [OpenSpec by Fission-AI](https://github.com/Fission-AI/OpenSpec)

**Two workflows, one orchestrator**: BMAD for complex projects (L2-4), OpenSpec for simple changes (L0-1).

---

## 🎉 What's This?

**Intelligent workflow system** that automatically chooses the right approach based on your project's complexity:

### 🚀 OpenSpec (Level 0-1: Simple Changes)
- ✅ **Lightweight & Fast** - Hours instead of days
- ✅ **3 Simple Stages** - Propose → Implement → Archive
- ✅ **Perfect for** - Bug fixes, small features, simple modifications
- ✅ **Minimal Overhead** - Just proposal + tasks, no PRD/Architecture

### 🏗️ BMAD (Level 2-4: Complex Projects)
- ✅ **Comprehensive & Structured** - Complete planning and architecture
- ✅ **7 Agent Skills** - Analyst, PM, UX, Architect, TEA, Scrum Master, Dev
- ✅ **4-Phase Workflow** - Analysis → Planning → Solutioning → Implementation
- ✅ **State Management** - Tracks phases, stories, progress
- ✅ **BMAD Agent Personas** - Mary, John, Sally, Winston, Murat, Bob, Amelia

### 🎯 Automatic Routing
- ✅ **Proactive Auto-Invocation** - Claude detects complexity and chooses workflow
- ✅ **No manual decisions** - Just describe what you want, Claude handles the rest

## 🚀 How It Works

**No slash commands. Just talk naturally.** Claude detects complexity and routes to the right workflow.

### Simple Change → OpenSpec

```
You: "Add search filters to the profile page"

Claude: This is a Level 1 change - perfect for OpenSpec!
        Let me create a lightweight proposal...
        [openspec-propose activates - creates proposal + tasks]

        Ready in minutes, not days.
```

### Complex Project → BMAD

```
You: "I want to build a REST API for user authentication"

Claude: Level 2-3 project - using BMAD workflow.
        Let me create a complete PRD...
        [bmad-pm activates - creates PRD and epics]

        Full planning and architecture included.
```

### Architecture Needed → BMAD

```
You: "How should we architect this microservices system?"

Claude: Complex architecture required - BMAD workflow.
        Let me invoke bmad-architecture...
        [Architecture skill activates - creates ARCHITECTURE.md]
```

**Claude analyzes complexity automatically** and chooses the optimal workflow.

---

## 📚 Documentation

### Getting Started
- **[Quick Start](doc/quickstart.md)** - Start using BMAD/OpenSpec in 5 minutes
- **[Architecture Overview](doc/overview.md)** - Skills, triggers, structure
- **[OpenSpec Workflow](doc/openspec.md)** - Lightweight workflow for simple changes (L0-1)

### Deep Dive
- **[BMAD Phases](doc/phases.md)** - Analysis → Planning → Solutioning → Implementation
- **[Skill Details](doc/skills.md)** - All 7 BMAD skills + 3 OpenSpec skills explained
- **[Workflow Example](doc/workflow-example.md)** - Complete e-commerce project walkthrough
- **[State Management](doc/state-management.md)** - workflow-status.md & sprint-status.yaml

### Reference
- **[Best Practices](doc/best-practices.md)** - Tips, patterns, troubleshooting
- **[Changelog](doc/changelog.md)** - Version history, attribution, license

---

## 🎯 The 10 Skills (7 BMAD + 3 OpenSpec)

### Orchestration
| Skill | Workflow | What It Does | Triggers |
|-------|----------|--------------|----------|
| **bmad-orchestrator** | Both | Intelligent routing: BMAD (L2-4) or OpenSpec (L0-1) | "What's next?", "Start new project" |

### OpenSpec Skills (L0-1: Simple Changes)
| Skill | Stage | What It Does | Triggers |
|-------|-------|--------------|----------|
| **openspec-propose** | 1 | Create lightweight change proposals | "Add a...", "Fix the...", "Change the..." |
| **openspec-implement** | 2 | Implement approved proposals | "Approved", "Implement it" |
| **openspec-archive** | 3 | Archive deployed changes | "Deployed", "Archive this" |

### BMAD Skills (L2-4: Complex Projects)
| Skill | Phase | What It Does | Triggers |
|-------|-------|--------------|----------|
| **bmad-analyst** | 1 | Brainstorming, product briefs, research | "I have an idea...", "Help me think through..." |
| **bmad-pm** | 2 | PRD, epics breakdown | "I want to build...", "Create PRD" |
| **bmad-ux** | 2 | UX design specifications | "What should the UI look like?" |
| **bmad-architecture** | 3 | Tech stack, architecture decisions | "How should we build this?" |
| **bmad-tea** | Any | Test strategy, ATDD, automation | "How should we test?" |
| **bmad-stories** | 4 | Developer-ready story creation | "Break into stories" |
| **bmad-dev** | 4 | Code implementation, testing | "Implement story X", "Let's code" |

See [Skill Details](doc/skills.md) and [OpenSpec Workflow](doc/openspec.md) for complete documentation.

---

## ⚡ Quick Start

1. **Install dependencies**:
   ```bash
   pip install jinja2 pyyaml
   ```

2. **Start a conversation**:
   ```
   You: "I want to start a new project for an expense tracker"

   Claude: [Invokes bmad-orchestrator automatically]
   ```

3. **Follow the natural flow**:
   - Claude will guide you through Analysis → Planning → Solutioning → Implementation
   - Just describe what you want in natural language
   - Claude invokes the right skill automatically

See [Quick Start Guide](doc/quickstart.md) for detailed walkthrough.

---

## 🔄 Complete Workflow

1. **Start Project** → Orchestrator initializes workflow
2. **Brainstorm** → Analyst helps explore ideas (optional)
3. **Plan** → PM creates PRD and epics
4. **Design UX** → UX Designer creates UX spec (optional)
5. **Architect** → Architect defines tech stack and patterns
6. **Test Strategy** → TEA sets up testing (optional)
7. **Create Stories** → Scrum Master breaks down epics
8. **Implement** → Dev codes, tests, and delivers

See [Workflow Example](doc/workflow-example.md) for complete e-commerce project.

---

## 📊 Project Levels

| Level | Scope | Workflow |
|-------|-------|----------|
| 0 | Bug fix | Skip BMAD |
| 1 | Small feature | Tech-spec only |
| 2 | MVP feature | Planning → Solutioning → Implementation |
| 3 | Product | (Analysis) → Planning → Solutioning → Implementation |
| 4 | Platform | Analysis → Planning → Solutioning → Implementation |

---

## 🛠️ State Management

BMAD tracks your progress with two files:

- **`docs/bmm-workflow-status.md`** - Current phase, artifacts, next actions
- **`docs/sprint-status.yaml`** - Story statuses (backlog → drafted → in-progress → done)

See [State Management](doc/state-management.md) for details.

---

## 🎓 Best Practices

1. **Let Claude invoke skills** - Don't manually invoke, let Claude detect context
2. **Check status often** - "What's next?" keeps you on track
3. **Complete phases in order** - Don't skip Planning or Solutioning
4. **Story learnings matter** - Each story builds on previous learnings
5. **Tests are mandatory** - Dev won't mark complete until 100% tests pass

See [Best Practices](doc/best-practices.md) for complete guide.

---

## 📦 What's Included

```
.claude/skills/
├── bmad-orchestrator/    # Intelligent routing: BMAD or OpenSpec
│   └── helpers/          # Python state management
│
├── OpenSpec Skills (L0-1)
├── openspec-propose/     # Stage 1: Create proposals
├── openspec-implement/   # Stage 2: Implement tasks
├── openspec-archive/     # Stage 3: Archive changes
│
└── BMAD Skills (L2-4)
    ├── bmad-analyst/         # Phase 1: Analysis
    ├── bmad-pm/              # Phase 2: Planning (PRD generator)
    ├── bmad-ux/              # Phase 2: UX Design
    ├── bmad-architecture/    # Phase 3: Solutioning (Architecture generator)
    ├── bmad-tea/             # Cross-phase: Testing
    ├── bmad-stories/         # Phase 4: Story creation (Story generator)
    └── bmad-dev/             # Phase 4: Implementation

doc/                      # Complete documentation
├── overview.md           # Architecture overview
├── quickstart.md         # Getting started guide
├── openspec.md           # OpenSpec workflow guide (NEW)
├── phases.md             # BMAD phase details
├── skills.md             # All skill details
├── workflow-example.md   # Complete BMAD example
├── state-management.md   # State files
├── best-practices.md     # Tips & troubleshooting
└── changelog.md          # Version history
```

---

## 🙏 Attribution

**Source**: [BMAD Method v6-alpha](https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)
**License**: Internal/educational use - BMAD Method is property of bmad-code-org

This implementation preserves BMAD v6-alpha agent personas, workflows, and output formats exactly.

**Agent Personas**: Mary, John, Sally, Winston, Murat, Bob, Amelia

See [Changelog](doc/changelog.md) for complete attribution.

---

## 🚀 Start Building

```
You: "I want to start a new project"

Claude: [Invokes bmad-orchestrator automatically]
        Let me help you get started with BMAD...
```

From idea → product brief → PRD → architecture → stories → implementation.

**All 7 agents. All 4 phases. Fully automated.**

Let BMAD guide you from 0 to production. 🎉
