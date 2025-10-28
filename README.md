# BMAD-Style Workflow Skills for Claude

**Version**: 2.1.0 - Proactive Skills
**Source**: [BMAD Method v6-alpha](https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha)

Complete, faithful implementation of BMAD Method v6-alpha as Claude Code Skills with automatic, proactive skill invocation.

---

## 🎉 What's This?

**All 7 BMAD agents** transformed into Claude Skills that activate **automatically** when you talk to Claude:

- ✅ **Proactive Auto-Invocation** - Claude detects what you need and invokes skills automatically
- ✅ **7 Agent Skills** - Analyst, PM, UX, Architect, TEA, Scrum Master, Dev
- ✅ **Complete Workflow** - Analysis → Planning → Solutioning → Implementation
- ✅ **State Management** - Tracks phases, stories, progress
- ✅ **BMAD Agent Personas** - Mary, John, Sally, Winston, Murat, Bob, Amelia

## 🚀 How It Works

**No slash commands. Just talk naturally.**

```
You: "I have an idea for a collaborative todo app"

Claude: I detect you're starting a new project with a vague idea.
        Let me invoke bmad-analyst to help you explore this...
        [Analyst skill activates - helps brainstorm]
```

```
You: "I want to build a REST API for user authentication"

Claude: You're describing a Level 2-3 project.
        Let me invoke bmad-pm to create a PRD...
        [PM skill activates - creates PRD and epics]
```

```
You: "How should we architect this?"

Claude: I detect you need architectural planning.
        Let me invoke bmad-architecture...
        [Architecture skill activates - creates ARCHITECTURE.md]
```

**Claude analyzes your conversation** and invokes the right skill at the right time.

---

## 📚 Documentation

### Getting Started
- **[Quick Start](doc/quickstart.md)** - Start using BMAD in 5 minutes
- **[Architecture Overview](doc/overview.md)** - Skills, triggers, structure

### Deep Dive
- **[BMAD Phases](doc/phases.md)** - Analysis → Planning → Solutioning → Implementation
- **[Skill Details](doc/skills.md)** - All 7 skills explained
- **[Workflow Example](doc/workflow-example.md)** - Complete e-commerce project walkthrough
- **[State Management](doc/state-management.md)** - workflow-status.md & sprint-status.yaml

### Reference
- **[Best Practices](doc/best-practices.md)** - Tips, patterns, troubleshooting
- **[Changelog](doc/changelog.md)** - Version history, attribution, license

---

## 🎯 The 7 Skills

| Skill | Phase | What It Does | Triggers |
|-------|-------|--------------|----------|
| **bmad-orchestrator** | All | Workflow management, status tracking | "What's next?", "Start new project" |
| **bmad-analyst** | 1 | Brainstorming, product briefs, research | "I have an idea...", "Help me think through..." |
| **bmad-pm** | 2 | PRD, epics breakdown | "I want to build...", "Create PRD" |
| **bmad-ux** | 2 | UX design specifications | "What should the UI look like?" |
| **bmad-architecture** | 3 | Tech stack, architecture decisions | "How should we build this?" |
| **bmad-tea** | Any | Test strategy, ATDD, automation | "How should we test?" |
| **bmad-stories** | 4 | Developer-ready story creation | "Break into stories" |
| **bmad-dev** | 4 | Code implementation, testing | "Implement story X", "Let's code" |

See [Skill Details](doc/skills.md) for complete documentation.

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
├── bmad-orchestrator/    # Workflow management + Python helpers
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
├── phases.md             # Phase details
├── skills.md             # Skill details
├── workflow-example.md   # Complete example
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
