# BMAD Global - Complete Workflow System

**The entire BMAD ecosystem in a single skill.**

## What is BMAD Global?

BMAD Global is an **intelligent orchestrator** that provides the complete BMAD workflow experience through a single, unified skill. Instead of manually selecting which sub-skill to invoke, simply describe what you want to do - BMAD Global automatically routes your work through the right process.

## Key Features

- ✨ **Auto-routing** - Intelligent complexity assessment (Level 0-4)
- 🔄 **Two-track system** - OpenSpec for quick changes, BMAD for complex work
- 📊 **Progress tracking** - Always know where you are
- 🎯 **Phase management** - Automatic prerequisite checking
- 💬 **Natural language** - No commands needed
- 📦 **Complete workflow** - Discovery → Planning → UX → Architecture → Testing → Stories → Code

## Quick Start

### As a Standalone Skill

```bash
# Install globally
mkdir -p ~/.claude/skills
cp -r bmad-global ~/.claude/skills/

# Or in your project
mkdir -p .claude/skills
cp -r bmad-global .claude/skills/
```

### Usage

Just start talking:

```
"I have an idea for a todo app"
"I want to build user authentication"
"Help me fix this bug"
"What's next on my project?"
```

BMAD Global figures out the rest.

## Included Sub-Skills

When you install BMAD Global as part of the complete bundle, you get:

1. **main-workflow-router** - Status & orchestration
2. **bmad-discovery-research** - Idea exploration
3. **bmad-product-planning** - Requirements & PRDs
4. **bmad-ux-design** - User experience design
5. **bmad-architecture-design** - Technical decisions
6. **bmad-test-strategy** - Quality planning
7. **bmad-story-planning** - Task breakdown
8. **bmad-development-execution** - Implementation
9. **openspec-change-proposal** - Change proposals
10. **openspec-change-implementation** - Change execution
11. **openspec-change-closure** - Change archival

## Workflow Paths

### Quick Change (Level 0-1)
```
Idea → OpenSpec Proposal → Implementation → Done
```
**Duration:** 15-60 minutes

### Feature Addition (Level 2)
```
Idea → Planning → Architecture → Stories → Code
```
**Duration:** 4-8 hours

### Complex Feature (Level 3)
```
Idea → Discovery → Planning → UX → Architecture → Testing → Stories → Code
```
**Duration:** 2-3 days

### New Product (Level 4)
```
Idea → Discovery → Research → Planning → UX → Architecture → Testing → Stories → Iterative Development
```
**Duration:** 1-2 weeks+

## Example Conversations

### Example 1: New Feature
```
You: "I want to add authentication to my app"

BMAD Global:
- Assesses: Level 2 (defined feature)
- Routes to: Planning → Architecture → Stories
- Delivers: Implementation-ready stories
```

### Example 2: Bug Fix
```
You: "The login button is misaligned"

BMAD Global:
- Assesses: Level 0 (trivial fix)
- Routes to: OpenSpec
- Delivers: Fixed code in <30 min
```

### Example 3: New Product
```
You: "I have an idea for a project management tool"

BMAD Global:
- Assesses: Level 4 (new product)
- Routes to: Discovery → Full BMAD workflow
- Delivers: Complete product development path
```

## Installation Options

### Option 1: Standalone (This Skill Only)

Best for: Trying out BMAD, lightweight installation

```bash
# Clone or download this directory
cp -r bmad-global ~/.claude/skills/

# BMAD Global will guide you through workflow
# But won't have access to sub-skill automation
```

**Note:** Standalone mode uses conversational routing without specialized sub-skills.

### Option 2: Complete Bundle

Best for: Full features, team usage, production

```bash
# Install complete BMAD Skills bundle
npm install -g bmad-skills

# Or via direct download
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-home.sh | bash
```

**Includes:** All 11 sub-skills + bmad-global + automation scripts

### Option 3: Custom Installation

Best for: Specific needs, selective skills

```bash
# Install just the skills you need
mkdir -p ~/.claude/skills
cp -r bmad-global ~/.claude/skills/
cp -r ../main-workflow-router ~/.claude/skills/
cp -r ../bmad-discovery-research ~/.claude/skills/
# ... add others as needed
```

## Configuration

### Workspace Structure

BMAD Global uses:
```
_runtime/workspace/
├── artifacts/    # Planning docs, architecture, PRDs
├── stories/      # Developer stories
├── changes/      # OpenSpec change proposals
└── specs/        # OpenSpec specifications
```

### Customization

Edit `SKILL.md` to customize:
- Trigger patterns
- Routing logic
- Default complexity levels
- Phase order

## Troubleshooting

**"BMAD Global seems stuck"**
- Say: "What's the status?"
- Or: "Show me where we are"

**"Wrong phase selected"**
- Override: "Let's jump to [phase]"
- Or: "Skip [phase]"

**"Too much overhead"**
- Say: "This is a quick fix"
- Or: "Keep it simple"

## Documentation

- **SKILL.md** - Complete skill contract
- **REFERENCE.md** - Deep dive on all features
- **WORKFLOW.md** - Step-by-step process
- **CHECKLIST.md** - Quality gates

## Version

Current version: **2.1.5**

Compatible with: **Claude Skills v1.0**

## License

MIT License - See LICENSE file in repository root

## Support

- GitHub: https://github.com/bacoco/bmad-skills
- Issues: https://github.com/bacoco/bmad-skills/issues
- Docs: https://github.com/bacoco/bmad-skills/tree/main/.claude/skills/_docs

## Credits

Part of the **BMAD Skills** ecosystem - a complete workflow system for product development with Claude.

---

**Get started:** Just say "I have an idea..." and let BMAD Global guide you!
