# BMAD Skills: Your AI Product Team

**Transform ideas into shipped products through natural conversation with Claude.**

From "I have an idea..." to production-ready code, BMAD guides you through research, planning, design, architecture, testing, and implementation—automatically.

---

## 💡 What is BMAD?

Imagine having a complete product team that activates instantly when you need them:

```
You: "I have an idea for a budget tracking app"

Claude (analyst): "Great! Let's explore this together. What problems are your users facing
                  with current budgeting tools?"

[30 minutes of brainstorming later...]

You: "Create a PRD for this"

Claude (PM): "I'll create a comprehensive PRD. Based on our discussion, here are the
              core features..."
              📄 Generates: product-requirements-document.md

You: "What should the UI look like?"

Claude (UX): "Let me design the user flows and wireframes..."
             🎨 Generates: user-flows.md, wireframes.md

You: "How should we build this?"

Claude (architect): "Here's the technical architecture..."
                    🏗️ Generates: architecture-decisions.md

You: "Break this into stories"

Claude (stories): "I've created 12 developer-ready stories with acceptance criteria..."
                  📋 Generates: 12 story files

You: "Implement story 1"

Claude (dev): "Implementing authentication system with tests..."
              💻 Generates: working code + tests
```

**All through natural conversation. No commands. No manual switching. Just talk.**

---

## 🎯 Why BMAD?

### The Problem

Building products is complex:
- ❌ Jumping between research, planning, design, and coding fragments your thinking
- ❌ Missing steps leads to rework and technical debt
- ❌ Context loss when switching between tasks
- ❌ Documentation falls behind implementation
- ❌ No consistent workflow across projects

### The Solution

BMAD is a complete workflow ecosystem that:
- ✅ **Guides you through the right process** automatically based on your needs
- ✅ **Maintains context** across all phases of development
- ✅ **Generates documentation** as you go, not after the fact
- ✅ **Adapts to project complexity** - lightweight for bugs, comprehensive for features
- ✅ **Works through conversation** - no commands, no configuration

---

## 🚀 Real-World Examples

### Example 1: Building a New Feature

**Scenario:** You want to add social login to your app

```
You: "I want to add Google and GitHub login to my app"

Claude (orchestrator): "This is a Level 2 feature. Let me activate the right skills..."

Claude (analyst): "Let's research OAuth best practices and security requirements..."
                  [Researches, documents findings]

Claude (architecture): "Here's how we'll integrate OAuth securely..."
                       [Designs auth flow, token management, security]

Claude (tea): "Here's the test strategy for authentication..."
              [Defines test scenarios, security tests, edge cases]

Claude (stories): "I've broken this into 4 stories:
                   1. OAuth provider setup
                   2. Login flow implementation
                   3. Token management
                   4. Security hardening"

You: "Implement story 1"

Claude (dev): "Setting up OAuth providers..."
              [Writes code, tests, documentation]
```

**Result:** Production-ready feature with architecture docs, test coverage, and security best practices baked in.

### Example 2: Quick Bug Fix

**Scenario:** Login timeout is too short

```
You: "Fix the login timeout - users are getting logged out too quickly"

Claude (openspec-propose): "I'll create a lightweight proposal for this Level 0 change..."
                           📄 proposal.md: Increase session timeout from 15min to 60min
                           ✅ tasks.md: Update config, test, document

You: "Implement it"

Claude (openspec-implement): "Updating session timeout configuration..."
                             [Makes change, tests, logs execution]

You: "Archive this"

Claude (openspec-archive): "Documented and archived. Session timeout fix is complete."
```

**Result:** Quick fix with full traceability - no ceremony, just results.

### Example 3: Exploring a New Idea

**Scenario:** You have a vague idea for an app

```
You: "I'm thinking about an app for freelancers to manage their time and invoicing"

Claude (analyst): "Interesting! Let's explore this together:
                   - Who are your target users?
                   - What pain points are they facing?
                   - What's different from existing tools like Harvest or Toggl?"

[Conversation continues - Claude asks smart questions, researches competitors,
 identifies opportunities, documents insights]

Claude: "I've documented our findings in discovery-notes.md.
         Key insight: Freelancers want integrated time tracking + invoicing +
         project management. Current tools require 3 separate subscriptions.

         Ready to create a PRD?"

You: "Yes"

Claude (pm): "Creating comprehensive PRD..."
```

**Result:** Clear product direction validated through research before writing a single line of code.

---

## ✨ Key Features

### 🎭 12 Specialized Skills, One Seamless Experience

**BMAD Workflow (8 skills):**
- 💡 **Analyst** - Brainstorming, research, competitive analysis
- 📋 **PM** - PRD creation, feature planning, roadmapping
- 🎨 **UX** - User flows, wireframes, design systems
- 🏗️ **Architecture** - Technical design, decision documentation
- 🧪 **TEA** - Test strategy, ATDD scenarios, quality gates
- 📝 **Stories** - Developer-ready story breakdown
- 💻 **Dev** - Implementation with tests and documentation
- 🎯 **Orchestrator** - Workflow coordination and guidance

**OpenSpec (3 skills):**
- 📄 **Propose** - Lightweight change proposals
- ⚡ **Implement** - Quick implementations
- 📦 **Archive** - Change documentation and closing

**Skill Creator:**
- 🛠️ **Create Skills** - Build custom skills for your workflow

### 🧠 Intelligent Workflow Routing

BMAD automatically chooses the right approach based on complexity:

| Complexity | Example | Workflow | Skills Used |
|-----------|---------|----------|-------------|
| **Level 0** | Config change | OpenSpec | 3 skills |
| **Level 1** | Small feature | OpenSpec | 3 skills |
| **Level 2** | Medium feature | BMAD | 5-7 skills |
| **Level 3** | New product area | BMAD | All 8 skills |
| **Level 4** | Novel innovation | BMAD | All 8 skills + research |

### 💬 Conversational Activation

No commands to remember. Just talk naturally:

| You Say | Skill Activated | What Happens |
|---------|----------------|--------------|
| "I have an idea..." | Analyst | Brainstorming session |
| "Create a PRD" | PM | Requirement document |
| "Design the UX" | UX | User flows + wireframes |
| "How should we build this?" | Architecture | Technical design |
| "How should we test this?" | TEA | Test strategy |
| "Break into stories" | Stories | Developer tasks |
| "Implement story X" | Dev | Code + tests |
| "Fix this bug" | OpenSpec | Quick fix workflow |
| "What's next?" | Orchestrator | Status + guidance |

### 📊 Full Traceability

Every decision, every change, fully documented:

```
project/
├── docs/
│   ├── discovery/              # Research & brainstorming
│   ├── requirements/           # PRD & feature specs
│   ├── design/                 # UX flows & wireframes
│   ├── architecture/           # Technical decisions
│   ├── testing/                # Test strategy
│   └── stories/                # Implementation stories
├── .claude/skills/_runtime/
│   └── workspace/
│       ├── changes/            # OpenSpec proposals
│       └── specs/              # Living specifications
└── [your code]
```

---

## 🎬 How It Works

### 1. Natural Conversation

You talk to Claude naturally about what you want to build or fix. No special syntax, no commands.

### 2. Automatic Skill Activation

Claude detects your intent and activates the right skill:
- **Idea exploration** → Analyst
- **Planning** → PM
- **Design** → UX
- **Technical questions** → Architecture
- **Implementation** → Dev

### 3. Context-Aware Guidance

Each skill knows:
- What came before (maintains full context)
- What needs to happen next (guides your workflow)
- What artifacts to create (generates documentation)
- When to hand off (seamless transitions)

### 4. Progressive Complexity

Start simple, scale as needed:
- Quick fixes use OpenSpec (3 skills, 5 minutes)
- Features use BMAD (8 skills, guided process)
- New products use full workflow (end-to-end)

---

## 🏆 Benefits

### For Solo Developers
- ✅ Get the structure and discipline of a full team
- ✅ Don't skip important steps (architecture, testing, documentation)
- ✅ Ship higher quality features faster
- ✅ Build a portfolio of well-documented projects

### For Teams
- ✅ Consistent workflow across all developers
- ✅ Better handoffs with complete documentation
- ✅ Faster onboarding (workflow is built-in)
- ✅ Scalable process from bugs to features

### For Founders
- ✅ Validate ideas before coding (analyst + PM)
- ✅ Make better technical decisions (architecture)
- ✅ Ship with confidence (test strategy)
- ✅ Move fast without breaking things (quality gates)

---

## 📦 What's Included

**Complete self-contained bundle:**
- 12 specialized AI skills that work together
- Shared glossary, constraints, and quality standards
- Runtime workspace for proposals and specs
- Comprehensive guides and troubleshooting docs
- Activation metrics and monitoring tools

**Everything works out of the box.** No configuration needed.

---

## 🚀 Get Started

### Install (2 minutes)

```bash
# Install globally (recommended)
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-home.sh | bash

# Or manually
git clone https://github.com/bacoco/bmad-skills.git
cd bmad-skills
bash scripts/install.sh
```

### Start Building

```bash
# Open Claude Code and just start talking:
"I have an idea for a meditation timer app"
```

That's it. BMAD takes it from there.

---

## 📚 Learn More

- 🚀 **[Quickstart Guide](.claude/skills/_docs/guides/quickstart-conversational.md)** - Get started in 5 minutes
- 📖 **[Conversational Flow Examples](.claude/skills/_docs/guides/conversational-flow.md)** - 6 complete scenarios
- 🔧 **[Skills Reference](.claude/skills/_docs/reference/skills.md)** - Detailed skill documentation
- ❓ **[FAQ](.claude/skills/_docs/activation/activation-faq.md)** - Common questions answered

---

## 🤝 Contributing

BMAD is open source and welcomes contributions:

1. Follow the [Style Guide](.claude/skills/_config/STYLE-GUIDE.md)
2. Run tests: `bash scripts/verify.sh`
3. Submit PRs with clear descriptions

See [Contributing Guidelines](.claude/skills/_docs/guides/contributing.md) for details.

---

## 📄 License

MIT License - See [LICENSE](.claude/skills/_config/LICENSE.md)

---

## 🆘 Support

- 📖 [Documentation](.claude/skills/_docs/)
- 🐛 [Report Issues](https://github.com/bacoco/bmad-skills/issues)
- 💬 [Discussions](https://github.com/bacoco/bmad-skills/discussions)
- 🌟 [Star on GitHub](https://github.com/bacoco/bmad-skills)

---

<div align="center">

**Stop context-switching. Start shipping.**

[Get Started →](#-get-started) | [See Examples →](#-real-world-examples) | [Learn More →](#-learn-more)

</div>
