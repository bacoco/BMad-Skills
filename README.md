# BMAD Skills - Complete Workflow Bundle

BMAD is a complete workflow ecosystem packaged as Claude Skills. All 12 skills work together to guide you from idea to implementation using natural conversation.

## 🚀 Quick Install

### Install globally (recommended):
```bash
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-home.sh | bash
```

### Install to current project:
```bash
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-project.sh | bash
```

### Manual install:
```bash
git clone https://github.com/bacoco/bmad-skills.git
cd bmad-skills
bash scripts/install.sh
```

## 📦 What's Included

**Complete BMAD Skills Bundle** - Everything in one package:

✅ **12 Integrated Skills:**
- **BMAD Workflow (8 skills)**: analyst, pm, ux, architecture, tea, stories, dev, orchestrator
- **OpenSpec (3 skills)**: propose, implement, archive
- **Skill Creator (1 skill)**: create new skills

✅ **Core Resources:**
- Shared glossary, constraints, and quality gates
- Runtime workspace for OpenSpec changes
- Comprehensive documentation and guides

✅ **Developer Tools:**
- Activation metrics tracking
- Contract validation
- Status management utilities

## 📂 Bundle Structure

Everything is self-contained in `.claude/skills/`:

```
.claude/skills/
├── bmad-analyst/           # Brainstorming & research
├── bmad-pm/                # PRD creation
├── bmad-ux/                # UX design
├── bmad-architecture/      # Technical architecture
├── bmad-tea/               # Test strategy
├── bmad-stories/           # Story breakdown
├── bmad-dev/               # Implementation
├── bmad-orchestrator/      # Workflow coordination
├── openspec-propose/       # Lightweight proposals
├── openspec-implement/     # Quick implementations
├── openspec-archive/       # Change archival
├── skill-creator/          # Create new skills
│
├── _core/                  # Shared resources
│   ├── glossary.md
│   ├── constraints.md
│   ├── quality-gates.md
│   └── tooling/
│
├── _config/                # Configuration
│   ├── MANIFEST.json
│   ├── STYLE-GUIDE.md
│   └── VERSIONING.md
│
├── _runtime/               # Runtime workspace
│   └── workspace/
│       ├── changes/        # OpenSpec changes
│       ├── specs/          # Living specifications
│       ├── artifacts/      # Generated artifacts
│       └── stories/        # Story outputs
│
└── _docs/                  # Documentation
    ├── guides/
    ├── reference/
    └── activation/
```

## 💬 Conversational Activation

Skills activate automatically based on natural conversation - **no manual invocation needed**!

### Example Triggers

Just talk naturally about your project:

- **"I have an idea..."** → bmad-analyst (brainstorming & research)
- **"Create a PRD"** → bmad-pm (requirements & planning)
- **"What should the UI look like?"** → bmad-ux (UX design)
- **"How should we build this?"** → bmad-architecture (technical design)
- **"How should we test?"** → bmad-tea (test strategy)
- **"Break into stories"** → bmad-stories (story creation)
- **"Implement story X"** → bmad-dev (coding & implementation)
- **"Fix this bug"** → openspec-propose (lightweight proposals)
- **"What's next?"** → bmad-orchestrator (status & guidance)

### How It Works

```
You: "I have an idea for a budget tracking app"
Claude: [Automatically activates bmad-analyst]
        "Great! Let's brainstorm together. Tell me about your app..."
```

### Key Features

✅ **Auto-Detection**: Claude detects your intent from natural conversation
✅ **Phase Awareness**: Skills check prerequisites before activation
✅ **Context Routing**: Orchestrator guides you through the right workflow
✅ **No Manual Invocation**: Skills activate automatically when needed

## 📚 Documentation

**Getting Started:**
- 🚀 [Quickstart Guide](.claude/skills/_docs/guides/quickstart-conversational.md)
- 📖 [Conversational Flow Examples](.claude/skills/_docs/guides/conversational-flow.md)

**Reference:**
- 📋 [Skills Reference](.claude/skills/_docs/reference/skills.md)
- 🔧 [OpenSpec Guide](.claude/skills/_docs/reference/openspec.md)

**Support:**
- ❓ [FAQ](.claude/skills/_docs/activation/activation-faq.md)
- 🔧 [Troubleshooting](.claude/skills/_docs/activation/troubleshooting.md)

## 🎯 Choosing BMAD vs OpenSpec

**Use BMAD skills** when:
- Starting a new product or major feature
- Need end-to-end planning (PRD, architecture, test strategy)
- Multi-team coordination required
- High ambiguity or novel problems (Level 2-4 complexity)

**Use OpenSpec skills** when:
- Quick bug fix or small enhancement
- Already have a repo and clear requirements
- Single developer/team scope
- Low ambiguity (Level 0-1 complexity)

**Escalate to BMAD** if OpenSpec reveals higher complexity than expected.

## 🛠️ Development

### Prerequisites

```bash
pip install -r requirements.txt
```

### Project Structure

This repository:
```
BMad-Skills/
├── .claude/skills/      # Complete bundle (install this)
├── scripts/             # Installation utilities
├── tests/               # Test suite
├── build/               # Build outputs
└── README.md
```

### Creating Distribution Bundle

```bash
bash scripts/package-bundle.sh
```

This creates `build/bmad-skills-bundle.zip` ready for distribution.

## 📊 Monitoring & Metrics

Track skill activation patterns:

```bash
python .claude/skills/_core/tooling/activation_metrics.py export
```

## 🔄 Workflow Example

**Complete flow from idea to implementation:**

1. **"I want to build a task manager"** → bmad-analyst researches & brainstorms
2. **"Create a PRD"** → bmad-pm produces requirements document
3. **"Design the UX"** → bmad-ux creates flows and wireframes
4. **"How should we build it?"** → bmad-architecture defines technical design
5. **"How should we test?"** → bmad-tea creates test strategy
6. **"Break into stories"** → bmad-stories generates developer tasks
7. **"Implement story 1"** → bmad-dev writes code with tests

**Quick fix flow:**

1. **"Fix login timeout bug"** → openspec-propose creates lightweight proposal
2. **"Implement it"** → openspec-implement executes the change
3. **"Archive"** → openspec-archive documents and closes

## 🤝 Contributing

1. Follow `.claude/skills/_config/STYLE-GUIDE.md`
2. Update `.claude/skills/_config/MANIFEST.json` for changes
3. Run validation: `python .claude/skills/_core/tooling/lint_contracts.py`
4. Test installation: `bash scripts/verify.sh`

## 📄 License

See `.claude/skills/_config/LICENSE.md`

## 🆘 Support

- 📖 [Documentation](.claude/skills/_docs/)
- 🐛 [Report Issues](https://github.com/bacoco/bmad-skills/issues)
- 💬 [Discussions](https://github.com/bacoco/bmad-skills/discussions)

---

**Ready to get started?**

```bash
bash scripts/install.sh
```

Then start a new chat with Claude Code and say:
**"I have an idea..."** 🚀
