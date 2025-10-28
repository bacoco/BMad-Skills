# Changelog

## Version 2.1.0 - Proactive Skills (2025-10-28)

**Major UX Enhancement**: Skills now activate automatically based on conversation context

**New Features**:
- 🎯 Proactive auto-invocation: Claude detects user intent and invokes skills automatically
- 🗣️ Natural language triggers: No slash commands needed, just talk naturally
- 📊 Conversational triggers table: Clear mapping of phrases to skills
- ✨ All 7 skills updated with "When Claude Should Invoke This Skill" sections
- 📖 README updated with conversational examples and trigger documentation

**Changed Files**:
- All 7 skill YAML descriptions now include "Proactively activates when..."
- All 7 skills have new 🎯 sections with clear invocation triggers
- README shows natural conversation flows instead of manual commands

**Example**:
```
User: "I have an idea for a todo app"
Claude: [Automatically invokes bmad-analyst]
```

No more "/bmad-pm" or manual skill invocation. Just natural conversations.

## Version 2.0.0 - Complete Implementation (2025-10-28)

**Complete BMAD Method v6-alpha transformation**

**New Features**:
- ✅ Added bmad-analyst (Analysis phase)
- ✅ Added bmad-ux (UX Design)
- ✅ Added bmad-tea (Test Architecture)
- ✅ Added bmad-dev (Implementation)
- ✅ Refactored orchestrator with full state management
- ✅ Added workflow-status.md management
- ✅ Added sprint-status.yaml management
- ✅ Added story lifecycle tracking
- ✅ Added Python helpers for state management
- ✅ All 4 phases now complete
- ✅ All BMAD workflows covered

**Implementation Stats**:
- 7 Agent Skills implemented
- 2,919 lines of Skill documentation
- 2 Python state management helpers
- Workflow-status.md management
- Sprint-status.yaml management
- All BMAD phases covered
- Story lifecycle management
- BMAD agent personas preserved
- 100% faithful to BMAD v6-alpha

**Files Created**:
- 7 SKILL.md files
- 2 Python helpers
- 3 Python generators (PRD, Architecture, Story)
- 3 Jinja templates
- 1 comprehensive README

## Version 1.0.0 - Initial Release (2025-10-27)

**Features**:
- 3 Skills: PM, Architecture, Stories
- Basic orchestrator
- No state management

---

# Attribution & License

**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org

This implementation preserves BMAD v6-alpha agent personas, workflows, and output formats. It is a faithful vendoring of BMAD logic into Claude Code Skills, not a loose recreation.

**Agent Personas** (preserved from BMAD v6-alpha):
- Mary (Analyst) - Strategic Business Analyst
- John (PM) - Investigative Product Strategist
- Sally (UX Designer) - User Experience Designer
- Winston (Architect) - System Architect
- Murat (TEA) - Master Test Architect
- Bob (Scrum Master) - Technical Scrum Master
- Amelia (DEV) - Senior Implementation Engineer

**Important**: This is for internal/educational use. Do not redistribute without proper licensing from bmad-code-org.
