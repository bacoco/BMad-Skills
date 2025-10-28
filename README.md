# BMAD-Style Workflow Skills for Claude

**Version**: 1.0.0
**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha

---

## Overview

This repository implements BMAD (Boring Made Amazing Development) Method v6-alpha as Claude Code Skills. It brings BMAD's structured, agent-driven methodology into Claude, enabling deterministic workflows for feature development from idea to implementation.

**What is BMAD?**

BMAD is a multi-phase delivery model using specialized agents (PM, Architect, Scrum Master, Dev) and structured workflows to move from idea → product spec → architecture → stories → implementation. It ensures consistent artifacts and prevents the chaos of unstructured AI-driven development.

**Why Skills (Not Commands)?**

Per Claude Code's architecture, Skills use progressive disclosure - they load only when needed, keeping context lean. This implementation preserves BMAD's actual agent prompts, workflows, and output formats as vendored Skills, not loose recreations.

---

## Problem This Solves

**Without BMAD Skills**:
- Claude can think and code, but has no deterministic pipeline
- No canonical files acting as handoff memory
- No reuse of proven BMAD agent/command logic
- Inconsistent outputs, ad-hoc formatting

**With BMAD Skills**:
- Structured workflow: Planning → Architecture → Stories → Implementation
- Canonical files on disk: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `stories/*.md`
- BMAD v6-alpha agent logic preserved and reusable
- Deterministic outputs following BMAD templates

---

## Repository Structure

```
.claude/
  skills/
    bmad-orchestrator/        # Workflow sequencing and phase gates
      SKILL.md
    bmad-pm/                  # Product Manager - Planning phase
      SKILL.md
      generate_prd.py
      prd_template.md.jinja
      epics_template.md.jinja
    bmad-architecture/        # Architect - Solutioning phase
      SKILL.md
      generate_architecture.py
      architecture_template.md.jinja
    bmad-stories/             # Scrum Master - Story creation
      SKILL.md
      create_story.py
      story_template.md.jinja

docs/                         # Generated planning and architecture docs
  PRD.md                      # Product Requirements Document (generated)
  epics.md                    # Epic breakdown with stories (generated)
  ARCHITECTURE.md             # Decision Architecture (generated)

stories/                      # Generated story files
  {epic}-{story}-{title}.md   # Individual story files (generated)
```

---

## Prerequisites

1. **Claude Code** or **Claude CLI** installed
2. **Python 3.7+** with Jinja2:
   ```bash
   pip install jinja2
   ```
3. **Git** (for version control)

---

## Quick Start

### 1. Start a New Feature

Tell Claude:
```
I want to build a feature where users can [description].
Use BMAD workflow.
```

Claude will:
1. Load `bmad-orchestrator` skill
2. Assess project complexity (Level 0-4)
3. Guide you through phases

### 2. Follow the Workflow

**Phase 1: Planning** (bmad-pm skill)
- Claude asks clarifying questions about your feature
- Gathers requirements, goals, user stories
- Generates `docs/PRD.md` and `docs/epics.md`

**Phase 2: Solutioning** (bmad-architecture skill)
- Claude reads your PRD
- Makes architectural decisions (tech stack, patterns, structure)
- Discovers starter templates
- Generates `docs/ARCHITECTURE.md`

**Phase 3: Story Creation** (bmad-stories skill)
- Claude creates developer-ready story files
- Each story: `stories/{epic}-{story}-{title}.md`
- Stories include acceptance criteria, tasks, dev notes

**Phase 4: Implementation** (your Dev agent or human)
- Implement stories one by one
- Update "Dev Agent Record" in story file as you go
- Mark tasks complete

---

## Detailed Usage

### Project Level Assessment

BMAD adapts to project scale:

| Level | Scope | FRs | Epics | Stories | Use BMAD? |
|-------|-------|-----|-------|---------|-----------|
| 0-1 | Bug fix / small change | N/A | N/A | N/A | ❌ Overkill |
| 2 | New feature (MVP) | 8-15 | 1-2 | 5-15 | ✅ Yes |
| 3 | Comprehensive product | 12-25 | 2-5 | 15-40 | ✅ Yes |
| 4 | Enterprise platform | 20-35+ | 5-10+ | 40-100+ | ✅ Yes |

**Level 0-1**: Skip BMAD, just implement directly.
**Level 2-4**: Use full BMAD workflow.

### Phase 2: Planning (bmad-pm)

**When**: Starting a Level 2-4 project, no PRD exists

**What Claude Does**:
1. Asks 3-5 targeted questions about your feature
2. Structures requirements into BMAD PRD format
3. Breaks requirements into Epics and Stories
4. Generates two files:
   - `docs/PRD.md` - Strategic product requirements
   - `docs/epics.md` - Tactical story breakdown

**PRD Sections**:
- Goals
- Background Context
- Functional Requirements (FRs)
- Non-Functional Requirements (NFRs)
- User Journeys
- UX/UI Vision
- Epic List
- Out of Scope

**Epic/Story Rules**:
- Epic 1 MUST establish foundation (infra, CI/CD, core setup)
- Stories are vertical slices (complete, testable functionality)
- No forward dependencies
- AI-agent sized (2-4 hours each)

**Exit Criteria**:
- ✅ `docs/PRD.md` exists with all sections
- ✅ `docs/epics.md` exists with story breakdown
- ✅ User reviewed and approved

### Phase 3: Solutioning (bmad-architecture)

**When**: PRD complete, need architectural design

**What Claude Does**:
1. Reads PRD completely
2. Searches for starter templates (Next.js, Vite, etc.)
3. Makes architectural decisions:
   - Technology stack (with current versions via WebSearch)
   - Project structure
   - Naming conventions (critical for AI agent consistency)
   - Error handling strategy
   - Logging approach
   - Testing strategy
4. Designs novel patterns (if needed)
5. Generates `docs/ARCHITECTURE.md`

**Architecture Sections**:
- Executive Summary
- Decision Summary Table (with versions)
- Project Structure (complete tree)
- Epic to Architecture Mapping
- Technology Stack Details
- Integration Points
- Novel Pattern Designs (if any)
- Implementation Patterns
- Consistency Rules (naming, formatting, errors)
- Data Architecture
- API Contracts
- Security Architecture
- Performance Considerations
- Deployment Architecture
- Development Environment

**Critical**: Decision table MUST have specific versions (not "latest"). Claude will verify via WebSearch.

**Exit Criteria**:
- ✅ `docs/ARCHITECTURE.md` exists with all sections
- ✅ Every epic mapped to architecture components
- ✅ Implementation patterns defined (prevents agent conflicts)
- ✅ Project structure complete (no placeholders)
- ✅ User reviewed and approved

### Phase 4: Story Creation (bmad-stories)

**When**: PRD and Architecture complete, ready to prepare stories

**What Claude Does**:
1. Loads PRD, epics, and Architecture docs
2. For each story (in sequence):
   - Extracts story details from `docs/epics.md`
   - Checks previous story for context/learnings
   - Creates tasks mapped to acceptance criteria
   - Writes dev notes with architecture guidance
   - Generates `stories/{epic}-{story}-{title}.md`

**Story File Sections**:
- Story statement (As a... I want... So that...)
- Acceptance Criteria (testable)
- Prerequisites
- Tasks / Subtasks
- Dev Notes:
  - Architecture patterns to follow
  - Project structure guidance
  - Testing requirements
  - Learnings from previous story
  - References (source citations)
- Dev Agent Record (empty - filled during implementation)

**Critical**: Always check previous story for:
- New services/patterns created (REUSE, don't recreate)
- Files created/modified
- Architectural decisions made
- Technical debt deferred
- Review findings

**Exit Criteria**:
- ✅ Story file created in `stories/` directory
- ✅ Acceptance criteria clear and testable
- ✅ Tasks map to ACs
- ✅ Dev notes include architecture patterns
- ✅ Previous story learnings included
- ✅ All sources cited

---

## Workflow Rules

### Rule 1: No Skipping Phases (Level 2-4)
Complete phases in order:
1. Planning (PRD + Epics)
2. Solutioning (Architecture)
3. Story Creation
4. Implementation

### Rule 2: No Code Before Stories
Do NOT implement until:
- At least one story file exists
- Story contains acceptance criteria and architecture guidance

### Rule 3: Phase Gate Validation
Before advancing:
- Planning → Verify PRD and epics exist
- Solutioning → Verify Architecture exists with decisions
- Story Creation → Verify story file has all sections

### Rule 4: Sequential Story Creation
Within an epic:
- Create stories in order (1.1, 1.2, 1.3, etc.)
- Always check previous story for context
- Maintain continuity (reuse patterns)

### Rule 5: Scale Adaptation
- Level 1: Architecture may be brief/skipped
- Level 2: Full workflow, lighter touch
- Level 3-4: Comprehensive workflow

---

## Skills Reference

### bmad-orchestrator

**Purpose**: Workflow sequencing and phase gates

**Load When**:
- Starting new project
- Unsure which phase to use
- Want workflow status check

**Does NOT**: Execute phases (just guides)

### bmad-pm

**Purpose**: Planning phase - PRD and Epic creation

**Load When**:
- Level 2-4 project
- No PRD exists
- Need requirements structuring

**Outputs**: `docs/PRD.md`, `docs/epics.md`

**Agent Persona**: BMAD PM (Investigative Product Strategist)

### bmad-architecture

**Purpose**: Solutioning phase - Architecture design

**Load When**:
- PRD exists
- Need architectural decisions
- Ready for technical design

**Precondition**: `docs/PRD.md` must exist

**Outputs**: `docs/ARCHITECTURE.md`

**Agent Persona**: BMAD Architect (System Architect + Technical Design Leader)

### bmad-stories

**Purpose**: Story creation - Developer-ready specs

**Load When**:
- PRD and Architecture exist
- Ready to prepare stories
- Need next story created

**Preconditions**: `docs/PRD.md` and `docs/ARCHITECTURE.md` must exist

**Outputs**: `stories/{epic}-{story}-{title}.md`

**Agent Persona**: BMAD Scrum Master (Technical SM + Story Preparation Specialist)

---

## Troubleshooting

### Claude doesn't load the skill

**Problem**: Claude says "I don't see that skill"

**Solution**:
1. Verify files exist: `.claude/skills/bmad-pm/SKILL.md` etc.
2. Restart Claude session
3. Tell Claude: "Check `.claude/skills/` directory for BMAD skills"

### Python script fails

**Problem**: `ModuleNotFoundError: No module named 'jinja2'`

**Solution**:
```bash
pip install jinja2
```

### Generated files have placeholders

**Problem**: Output has `{{variable}}` or `TODO:` placeholders

**Solution**:
- This is intentional for unknown information
- Fill placeholders before proceeding to next phase
- Or provide more information to Claude during phase execution

### Architecture has no versions

**Problem**: Decision table shows "latest" instead of specific versions

**Solution**:
- This is a validation failure
- Claude should use WebSearch to verify current stable versions
- Tell Claude: "Verify technology versions via WebSearch"

---

## Attribution & License

**Source**: BMAD Method v6-alpha
**Reference**: https://github.com/bmad-code-org/BMAD-METHOD/tree/v6-alpha
**License**: Internal use - BMAD Method is property of bmad-code-org

This implementation preserves BMAD v6-alpha agent personas, workflows, and output formats. It is not a loose recreation but a faithful vendoring of BMAD logic into Claude Code Skills.

**Important**: This is for internal/educational use. Do not redistribute without proper licensing from bmad-code-org.

---

## Version History

**v1.0.0** (2025-10-28)
- Initial release
- Four Skills: Orchestrator, PM, Architecture, Stories
- Python generators with Jinja2 templates
- Full BMAD v6-alpha workflow support
- Preserves BMAD agent personas and principles

---

**Happy Building with BMAD!** 🚀
