# 🚀 Quick Start: Install BMAD Skills

**Transform your Claude Code experience with a complete product development workflow.**

## Installation (Choose One)

### Option 1: NPX (Recommended - Fastest)

```bash
# Install globally (works in all projects)
npx bmad-skills --global

# Or install to current project only
npx bmad-skills
```

### Option 2: Direct Script

```bash
# Install globally
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-home.sh | bash

# Or install to current project
curl -fsSL https://raw.githubusercontent.com/bacoco/bmad-skills/main/scripts/install-to-project.sh | bash
```

## What You Get

After installation, 12 specialized skills will automatically activate in your Claude Code conversations:

**💡 Just talk naturally:**
- "I have an idea..." → Analyst activates
- "Create a PRD" → PM activates
- "How should we build this?" → Architecture activates
- "Break this into stories" → Stories activates
- "Implement story 1" → Dev activates

**No commands. No configuration. Just conversation.**

## Verification

After installation, verify with:

```bash
# Check global installation
ls -la ~/.claude/skills/

# Or check project installation
ls -la ./.claude/skills/
```

You should see 12 skill directories:
- `main-workflow-router`
- `bmad-discovery-research`
- `bmad-product-planning`
- `bmad-ux-design`
- `bmad-architecture-design`
- `bmad-test-strategy`
- `bmad-story-planning`
- `bmad-development-execution`
- `openspec-change-proposal`
- `openspec-change-implementation`
- `openspec-change-closure`
- `core-skill-creation`

## Next Steps

**Try it now in Claude Code:**

```
You: "I have an idea for a habit tracking app"
```

That's it! The orchestrator will guide you through the entire workflow automatically.

## Documentation

- **Full README**: [github.com/bacoco/bmad-skills](https://github.com/bacoco/bmad-skills)
- **NPM Package**: [npmjs.com/package/bmad-skills](https://npmjs.com/package/bmad-skills)
- **Issues**: [github.com/bacoco/bmad-skills/issues](https://github.com/bacoco/bmad-skills/issues)

## Help

If skills aren't activating:
1. Restart Claude Code
2. Check installation directory exists
3. See [Troubleshooting Guide](./.claude/skills/_docs/activation/troubleshooting.md)

---

**Version 2.1.5** | [Changelog](./.claude/skills/_docs/changelog.md) | MIT License
