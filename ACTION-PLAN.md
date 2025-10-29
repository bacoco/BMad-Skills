# PLAN D'ACTION IMMÉDIAT - Corrections Skills BMAD

**Objectif:** Passer de 85/100 à 95/100 en 2-3 jours
**Focus:** Activation conversationnelle automatique selon la méthode Bimath

---

## JOUR 1: Descriptions Conversationnelles + Sections "When to Invoke"

### Tâche 1.1: Modifier meta/MANIFEST.json

**Fichier:** `meta/MANIFEST.json`

Remplacer toutes les descriptions par les versions conversationnelles ci-dessous:

```json
{
  "skills": [
    {
      "id": "bmad-orchestrator",
      "description": "BMAD workflow orchestrator. Auto-invokes at conversation start. Tracks status, guides through phases. Invoke: 'start project', 'what's next', 'where am I', 'status', 'initialize', or implicitly for any BMAD work. Keywords: status, workflow, next, start, guide, phase, where, initialize.",
      ...
    },
    {
      "id": "bmad-analyst",
      "description": "Brainstorms ideas and researches projects. Invoke when: 'I have an idea', 'What if we', 'Help me think', 'explore possibilities', 'I'm thinking about', 'brainstorm', 'research'. Keywords: idea, brainstorm, explore, research, thinking, new project, discovery.",
      ...
    },
    {
      "id": "bmad-pm",
      "description": "Creates PRDs and plans features. Invoke when: 'I want to build', 'create a PRD', 'plan this feature', 'write requirements', 'product document'. Keywords: PRD, requirements, plan, build, feature, epic, roadmap, product.",
      ...
    },
    {
      "id": "bmad-ux",
      "description": "Designs UX and creates wireframes. Invoke when: 'what should UI look like', 'design the UX', 'user experience', 'wireframes', 'user flow'. Keywords: UX, UI, design, wireframe, user flow, interface, usability.",
      ...
    },
    {
      "id": "bmad-architecture",
      "description": "Creates technical architecture. Invoke when: 'how should we build', 'what's the architecture', 'tech stack', 'system design', 'how to build this'. Keywords: architecture, tech stack, design, system, build, technical, structure.",
      ...
    },
    {
      "id": "bmad-tea",
      "description": "Creates test strategy. Invoke when: 'how should we test', 'create test strategy', 'test plan', 'ATDD', 'quality assurance'. Keywords: test, testing, strategy, QA, quality, ATDD, automation.",
      ...
    },
    {
      "id": "bmad-stories",
      "description": "Breaks epics into developer stories. Invoke when: 'break into stories', 'create user stories', 'story breakdown', 'developer tasks'. Keywords: story, stories, epic, breakdown, task, backlog, sprint.",
      ...
    },
    {
      "id": "bmad-dev",
      "description": "Implements stories with code and tests. Invoke when: 'implement story', 'develop this', 'let's code', 'write the code', 'start coding'. Keywords: implement, code, develop, build, program, coding, implementation.",
      ...
    },
    {
      "id": "skill-creator",
      "description": "Creates and validates new skills. Invoke when: 'create a skill', 'new skill', 'validate skill', 'package skill'. Keywords: skill, create skill, new skill, validate.",
      ...
    },
    {
      "id": "openspec-propose",
      "description": "Creates lightweight change proposals for Level 0-1 work. Invoke when: 'small change', 'bug fix', 'quick feature', 'propose change'. Keywords: propose, change, proposal, lightweight, Level 0, Level 1.",
      ...
    },
    {
      "id": "openspec-implement",
      "description": "Implements Level 0-1 changes. Invoke when: 'implement this change', 'execute proposal', 'apply the change'. Keywords: implement, execute, apply, change, Level 0, Level 1.",
      ...
    },
    {
      "id": "openspec-archive",
      "description": "Archives completed Level 0-1 changes. Invoke when: 'archive this change', 'close this change', 'document change'. Keywords: archive, close, document, complete, change.",
      ...
    }
  ]
}
```

**Durée estimée:** 30 minutes

---

### Tâche 1.2: Ajouter "When to Invoke" à bmad-orchestrator/SKILL.md

**Fichier:** `.claude/skills/bmad-orchestrator/SKILL.md`

**Action:** Ajouter après le frontmatter YAML, avant "# End-to-End Orchestration Skill":

```markdown
---
name: bmad-orchestrator
description: [voir nouvelle description ci-dessus]
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

## When to Invoke

**ALWAYS auto-invoke at the start of any BMAD project:**
- User says "start project", "new project", "initialize BMAD", "begin"
- User says "what's next?", "where am I?", "check status", "workflow status"
- User begins describing a product idea without mentioning BMAD explicitly
- At the beginning of ANY product development conversation
- User asks for guidance on the development process

**Special auto-behaviors:**
- If no workflow-status.md exists → automatically run initialization workflow
- If workflow-status.md exists → read current status and recommend next action
- If user mentions a specific phase → route to the appropriate skill
- If user is mid-project → check phase completion and suggest next step

**Do NOT invoke when:**
- User is clearly asking for a specific skill (let that skill handle it)
- User is in the middle of implementing code (bmad-dev is active)
- User is asking technical questions unrelated to workflow

# End-to-End Orchestration Skill

[reste du contenu inchangé...]
```

**Durée estimée:** 15 minutes

---

### Tâche 1.3: Ajouter "When to Invoke" à bmad-analyst/SKILL.md

**Fichier:** `.claude/skills/bmad-analyst/SKILL.md`

**Action:** Ajouter après le frontmatter YAML, avant "# Discovery Analysis Skill":

```markdown
---
name: bmad-analyst
description: [voir nouvelle description ci-dessus]
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

## When to Invoke

**Automatically activate this skill when the user:**
- Says "I have an idea...", "What if we...", "I'm thinking about..."
- Asks "Help me think through...", "Can you help me brainstorm...", "Let's explore..."
- Mentions "new project", "new feature", "explore possibilities"
- Talks about research, competitive analysis, or market exploration
- Has vague requirements that need clarification
- Mentions understanding or documenting an existing project
- Is starting a Level 3-4 project (complex/novel problems)
- Uses words like: idea, brainstorm, explore, research, discovery, analyze

**Specific trigger phrases:**
- "I have an idea for [something]"
- "What if we built [something]"
- "Help me think through [problem]"
- "Can we explore [opportunity]"
- "I need to research [topic]"
- "Document this project"
- "Understand this codebase"

**Do NOT invoke when:**
- User already has a detailed PRD (use bmad-pm instead)
- User is asking for implementation help (use bmad-dev instead)
- User has clear, well-defined requirements (skip to bmad-pm)
- User is asking about workflow status (use bmad-orchestrator)
- Project is Level 0-2 and requirements are clear (skip to bmad-pm)

# Discovery Analysis Skill

[reste du contenu inchangé...]
```

**Durée estimée:** 15 minutes

---

### Tâche 1.4: Ajouter "When to Invoke" à bmad-pm/SKILL.md

**Fichier:** `.claude/skills/bmad-pm/SKILL.md`

**Action:** Ajouter après le frontmatter YAML, avant "# Product Requirements Skill":

```markdown
---
name: bmad-pm
description: [voir nouvelle description ci-dessus]
version: 1.0.0
allowed-tools: ["Read","Write","Grep","Bash"]
---

## When to Invoke

**Automatically activate this skill when the user:**
- Says "I want to build...", "Let's build...", "Create a..."
- Asks "Create a PRD", "Write requirements", "Plan this feature"
- Mentions "product requirements", "PRD", "epic roadmap"
- Has completed discovery phase and needs formal requirements
- Is starting a Level 2-4 project requiring structured planning
- Uses words like: build, create, PRD, requirements, plan, feature, product

**Specific trigger phrases:**
- "I want to build [something]"
- "Create a PRD for [project]"
- "Plan this feature"
- "Write the requirements"
- "What should be in the PRD?"
- "Break this into epics"
- "Product requirements for [project]"

**Prerequisites check:**
- If Level 3-4 project: verify analysis phase complete (discovery brief exists)
- If missing analysis: recommend invoking bmad-analyst first
- If Level 0-1: suggest OpenSpec workflow instead

**Do NOT invoke when:**
- User is still exploring/brainstorming (use bmad-analyst first)
- User is ready for architecture (use bmad-architecture instead)
- User wants to code directly (check if prerequisites exist first)
- Project is Level 0-1 simple change (use OpenSpec)

# Product Requirements Skill

[reste du contenu inchangé...]
```

**Durée estimée:** 15 minutes

---

### Tâche 1.5: Ajouter "When to Invoke" aux autres skills BMAD

**Fichiers:**
- `.claude/skills/bmad-ux/SKILL.md`
- `.claude/skills/bmad-architecture/SKILL.md`
- `.claude/skills/bmad-tea/SKILL.md`
- `.claude/skills/bmad-stories/SKILL.md`
- `.claude/skills/bmad-dev/SKILL.md`

**Template à adapter pour chacun:**

```markdown
## When to Invoke

**Automatically activate this skill when the user:**
- Says [trigger phrases spécifiques au skill]
- Asks [questions spécifiques au skill]
- Mentions [keywords spécifiques au skill]
- [Contexte de phase approprié]

**Specific trigger phrases:**
- "[phrase 1]"
- "[phrase 2]"
- "[phrase 3]"

**Prerequisites check:**
- [Vérifications de phase si nécessaire]

**Do NOT invoke when:**
- [Anti-patterns]
```

**Exemples pour chaque skill:**

#### bmad-ux
```markdown
## When to Invoke

**Automatically activate when user:**
- Says "What should the UI look like?", "Design the UX"
- Asks "How should users interact?", "User flow?"
- Mentions "wireframes", "user experience", "interface design"
- Has PRD with UI-heavy features (Level 2-4)

**Trigger phrases:**
- "What should the UI look like?"
- "Design the UX for [feature]"
- "Create wireframes"
- "User experience for [feature]"

**Do NOT invoke:**
- No UI/interface in project (backend-only)
- PRD not ready (use bmad-pm first)
```

#### bmad-architecture
```markdown
## When to Invoke

**Automatically activate when user:**
- Says "How should we build this?", "What's the architecture?"
- Asks "Tech stack?", "System design?", "How to architect?"
- Mentions "architecture", "technical decisions", "stack"
- PRD and epics are approved (Phase 3)

**Trigger phrases:**
- "How should we build this?"
- "What's the architecture?"
- "Choose tech stack"
- "System design for [project]"

**Prerequisites:**
- PRD exists and approved
- Epics defined

**Do NOT invoke:**
- PRD not ready (use bmad-pm first)
- Already have architecture (skip to stories)
```

#### bmad-tea
```markdown
## When to Invoke

**Automatically activate when user:**
- Says "How should we test?", "Create test strategy"
- Asks "Test plan?", "ATDD?", "Quality assurance?"
- Mentions "testing", "test strategy", "QA"
- Planning or architecture phase (for test strategy)

**Trigger phrases:**
- "How should we test this?"
- "Create test strategy"
- "Test plan for [project]"
- "ATDD scenarios"

**Can invoke:**
- During Phase 2 (Planning) for test strategy
- During Phase 4 (Implementation) for ATDD

**Do NOT invoke:**
- No requirements yet (need PRD first)
```

#### bmad-stories
```markdown
## When to Invoke

**Automatically activate when user:**
- Says "Break into stories", "Create user stories"
- Asks "Developer tasks?", "Story breakdown?"
- Mentions "stories", "backlog", "sprint planning"
- Epics and architecture ready (Phase 4)

**Trigger phrases:**
- "Break this into stories"
- "Create user stories"
- "Story breakdown for [epic]"
- "Developer-ready tasks"

**Prerequisites:**
- Epics exist (from bmad-pm)
- Architecture defined

**Do NOT invoke:**
- No epics yet (use bmad-pm first)
- Stories already exist (use bmad-dev)
```

#### bmad-dev
```markdown
## When to Invoke

**Automatically activate when user:**
- Says "Implement story X", "Start coding", "Develop this"
- Asks "Write the code", "Let's code", "Build [feature]"
- Mentions "implement", "code", "develop"
- Story file ready (Phase 4)

**Trigger phrases:**
- "Implement story [X]"
- "Start coding [feature]"
- "Develop this story"
- "Let's code"
- "Write the implementation"

**Prerequisites:**
- Story file exists (from bmad-stories)
- Architecture patterns defined

**Do NOT invoke:**
- No story file (use bmad-stories first)
- Planning needed (use bmad-pm first)
```

**Durée estimée:** 1.5 heures (5 skills × ~18 minutes)

---

## JOUR 2: Migration REFERENCE.md + Auto-Orchestration

### Tâche 2.1: Migrer info d'activation de REFERENCE.md → SKILL.md

**Fichiers concernés:**
1. `.claude/skills/bmad-orchestrator/REFERENCE.md` (lignes 14-100)
2. `.claude/skills/bmad-analyst/REFERENCE.md` (lignes 14-100)

**Action pour chaque fichier:**

1. Ouvrir REFERENCE.md
2. Localiser la section "## When Claude Should Invoke This Skill"
3. Copier le contenu pertinent (pas les duplications avec ce qu'on a déjà ajouté)
4. Intégrer dans la section "When to Invoke" de SKILL.md (enrichissement)
5. **NE PAS SUPPRIMER** de REFERENCE.md mais déplacer vers section "Advanced Activation Patterns" ou similaire

**Pour bmad-orchestrator:**
- Garder la matrice de routing dans REFERENCE.md (c'est de la connaissance avancée)
- Déplacer les triggers principaux vers SKILL.md (déjà fait en Tâche 1.2)

**Pour bmad-analyst:**
- Garder les workflows détaillés dans REFERENCE.md (brainstorm, product-brief, etc.)
- Déplacer les triggers principaux vers SKILL.md (déjà fait en Tâche 1.3)

**Durée estimée:** 1 heure

---

### Tâche 2.2: Optimiser bmad-orchestrator pour auto-activation

**Fichier:** `.claude/skills/bmad-orchestrator/SKILL.md`

**Action:** Ajouter après la section "When to Invoke", une nouvelle section:

```markdown
## Auto-Activation Behavior

This skill has special auto-activation rules:

### 1. Conversation Start Detection
When a conversation begins and the user mentions:
- Product development topics
- Project ideas or features
- Building or creating something
- BMAD methodology

**Auto-action:** Initialize workflow if no status file exists.

### 2. Status Check Detection
When user asks:
- "Where am I?"
- "What's next?"
- "What should I do now?"

**Auto-action:** Read workflow-status.md and recommend next action.

### 3. Phase Transition Detection
When a skill completes its phase:
- Analyst completes discovery → Check if Planning ready
- PM completes PRD → Check if Solutioning ready
- Architecture completes → Check if Implementation ready

**Auto-action:** Update workflow status and recommend next skill.

### 4. Routing Intelligence
Based on user intent, automatically route to:
- Mentions "idea", "brainstorm" → bmad-analyst
- Mentions "PRD", "requirements" → bmad-pm
- Mentions "architecture", "build" → bmad-architecture
- Mentions "test strategy" → bmad-tea
- Mentions "stories", "breakdown" → bmad-stories
- Mentions "implement", "code" → bmad-dev

### 5. Safety Checks
Before routing, verify:
- [ ] Required artifacts from previous phase exist
- [ ] Phase gates from CHECKLIST.md are satisfied
- [ ] No blockers in workflow-status.md

If checks fail: Halt and request missing prerequisites.
```

**Durée estimée:** 30 minutes

---

### Tâche 2.3: Tests d'Activation Conversationnelle

**Fichier:** `tests/test_skill_activation.md` (à créer)

**Contenu:**

```markdown
# Tests d'Activation Automatique des Skills

**Date:** [DATE]
**Version:** 1.0.0

## Objectif
Vérifier que les skills s'activent automatiquement en conversation naturelle selon la méthode Bimath.

---

## Test 1: Nouvelle Idée → bmad-analyst

### Inputs à tester
- "J'ai une idée pour une app de gestion de budget"
- "What if we built a tool to track expenses?"
- "Help me think through a new product idea"
- "I'm thinking about creating a mobile app"
- "Can you help me brainstorm a feature?"

### Comportement Attendu
1. bmad-orchestrator détecte "nouvelle idée"
2. bmad-analyst activé automatiquement
3. Commence workflow de brainstorming
4. Pose des questions pour clarifier l'idée

### Résultats
- [ ] Test 1.1: ✅ / ❌
- [ ] Test 1.2: ✅ / ❌
- [ ] Test 1.3: ✅ / ❌
- [ ] Test 1.4: ✅ / ❌
- [ ] Test 1.5: ✅ / ❌

---

## Test 2: Demande PRD → bmad-pm

### Inputs à tester
- "I want to build a budget tracking app"
- "Create a PRD for my project"
- "Plan this feature for me"
- "Write product requirements for [X]"
- "I need to document the product requirements"

### Comportement Attendu
1. bmad-orchestrator détecte "PRD/planning"
2. Vérifie si Phase 1 (Analysis) complete (pour Level 3-4)
3. bmad-pm activé
4. Génère PRD selon template

### Résultats
- [ ] Test 2.1: ✅ / ❌
- [ ] Test 2.2: ✅ / ❌
- [ ] Test 2.3: ✅ / ❌
- [ ] Test 2.4: ✅ / ❌
- [ ] Test 2.5: ✅ / ❌

---

## Test 3: Check Status → bmad-orchestrator

### Inputs à tester
- "Where am I in my project?"
- "What's next?"
- "What should I do now?"
- "Check workflow status"
- "BMAD status"

### Comportement Attendu
1. bmad-orchestrator activé automatiquement
2. Lit workflow-status.md
3. Retourne phase actuelle et progression
4. Recommande prochaine action

### Résultats
- [ ] Test 3.1: ✅ / ❌
- [ ] Test 3.2: ✅ / ❌
- [ ] Test 3.3: ✅ / ❌
- [ ] Test 3.4: ✅ / ❌
- [ ] Test 3.5: ✅ / ❌

---

## Test 4: Architecture → bmad-architecture

### Inputs à tester
- "How should I build this?"
- "What's the architecture for this project?"
- "Choose tech stack"
- "System design for [project]"
- "How to architect this?"

### Comportement Attendu
1. bmad-orchestrator détecte "architecture"
2. Vérifie si PRD existe
3. bmad-architecture activé
4. Génère architecture selon template

### Résultats
- [ ] Test 4.1: ✅ / ❌
- [ ] Test 4.2: ✅ / ❌
- [ ] Test 4.3: ✅ / ❌
- [ ] Test 4.4: ✅ / ❌
- [ ] Test 4.5: ✅ / ❌

---

## Test 5: Implémentation → bmad-dev

### Inputs à tester
- "Implement story #5"
- "Start coding this feature"
- "Develop the authentication module"
- "Let's code the user registration"
- "Write the implementation for [story]"

### Comportement Attendu
1. bmad-orchestrator détecte "implementation"
2. Vérifie si story file existe
3. bmad-dev activé
4. Commence implémentation

### Résultats
- [ ] Test 5.1: ✅ / ❌
- [ ] Test 5.2: ✅ / ❌
- [ ] Test 5.3: ✅ / ❌
- [ ] Test 5.4: ✅ / ❌
- [ ] Test 5.5: ✅ / ❌

---

## Test 6: UX Design → bmad-ux

### Inputs à tester
- "What should the UI look like?"
- "Design the UX for this feature"
- "Create wireframes"
- "User flow for registration"
- "Interface design"

### Comportement Attendu
1. bmad-orchestrator détecte "UX/UI"
2. Vérifie si PRD existe
3. bmad-ux activé
4. Génère UX spec

### Résultats
- [ ] Test 6.1: ✅ / ❌
- [ ] Test 6.2: ✅ / ❌
- [ ] Test 6.3: ✅ / ❌
- [ ] Test 6.4: ✅ / ❌
- [ ] Test 6.5: ✅ / ❌

---

## Test 7: Test Strategy → bmad-tea

### Inputs à tester
- "How should we test this?"
- "Create test strategy"
- "Test plan for the project"
- "ATDD scenarios"
- "Quality assurance approach"

### Comportement Attendu
1. bmad-orchestrator détecte "testing"
2. bmad-tea activé
3. Génère test strategy

### Résultats
- [ ] Test 7.1: ✅ / ❌
- [ ] Test 7.2: ✅ / ❌
- [ ] Test 7.3: ✅ / ❌
- [ ] Test 7.4: ✅ / ❌
- [ ] Test 7.5: ✅ / ❌

---

## Test 8: Story Breakdown → bmad-stories

### Inputs à tester
- "Break this into stories"
- "Create user stories"
- "Story breakdown for epic X"
- "Developer-ready tasks"
- "Backlog planning"

### Comportement Attendu
1. bmad-orchestrator détecte "stories"
2. Vérifie si epics existent
3. bmad-stories activé
4. Génère story files

### Résultats
- [ ] Test 8.1: ✅ / ❌
- [ ] Test 8.2: ✅ / ❌
- [ ] Test 8.3: ✅ / ❌
- [ ] Test 8.4: ✅ / ❌
- [ ] Test 8.5: ✅ / ❌

---

## Résumé des Tests

**Total tests:** 40
**Tests réussis:** ___ / 40
**Tests échoués:** ___ / 40
**Taux de succès:** ___%

### Problèmes Identifiés
1. [Liste des problèmes]
2. [...]

### Corrections Nécessaires
1. [Actions correctives]
2. [...]

---

**Testeur:** [NOM]
**Date de test:** [DATE]
**Version skills:** 1.0.0
```

**Durée estimée:** 30 minutes (création), 2 heures (exécution tests)

---

## JOUR 3: Documentation + Validation

### Tâche 3.1: Créer doc/conversational-flow.md

**Fichier:** `doc/conversational-flow.md` (à créer)

**Contenu:**

```markdown
# Guide des Flows Conversationnels BMAD

Ce document montre des exemples de conversations naturelles et comment les skills BMAD s'activent automatiquement selon la méthode Bimath.

---

## Scénario 1: Nouvelle Idée → PRD → Architecture → Implémentation

### Conversation Complète

**User:** "J'ai une idée pour une app de gestion de budget"

**Claude:** [bmad-orchestrator détecte "idée" → bmad-analyst activé]
"Super! Je vais vous aider à structurer cette idée avec le BMAD Analyst.
Commençons par un brainstorming. Parlez-moi plus de votre app de budget:
- Quel problème cherchez-vous à résoudre?
- Qui sont vos utilisateurs cibles?
- Qu'est-ce qui vous a donné cette idée?"

**User:** "Je veux aider les gens à suivre leurs dépenses quotidiennes facilement. L'app serait pour les jeunes professionnels qui n'ont pas le temps de gérer un budget complexe."

**Claude:** [bmad-analyst continue le brainstorming]
"Excellent contexte! Je vois plusieurs directions possibles:
1. Suivi automatique via connexion bancaire
2. Saisie manuelle simplifiée
3. Catégorisation intelligente des dépenses
4. Alertes budget

Explorons ces directions... [continue brainstorming]

Voulez-vous que je crée un product brief formel maintenant?"

**User:** "Oui, créons le PRD"

**Claude:** [bmad-orchestrator détecte "PRD" → vérifie phase → bmad-pm activé]
"Parfait! Le brainstorming est terminé. Je passe maintenant au BMAD PM pour créer votre PRD.

Basé sur notre discussion, voici le PRD:
[génère PRD.md]

Maintenant, décomposons en epics:
[génère epics.md]

PRD et epics créés! Prêt pour l'architecture?"

**User:** "Oui, quelle architecture recommandez-vous?"

**Claude:** [bmad-orchestrator détecte "architecture" → vérifie PRD existe → bmad-architecture activé]
"Je vais maintenant travailler sur l'architecture avec le BMAD Architect.

Analysons les besoins techniques:
- App mobile (iOS + Android)
- Backend API
- Base de données pour transactions
[...]

[génère ARCHITECTURE.md]

Architecture définie! Voulez-vous que je crée les stories pour commencer l'implémentation?"

**User:** "Oui, créons les stories"

**Claude:** [bmad-orchestrator détecte "stories" → vérifie epics → bmad-stories activé]
"Parfait! Je vais créer les stories avec le BMAD Stories skill.

[génère stories/*.md]

Stories créées! Quelle story voulez-vous implémenter en premier?"

**User:** "Implémente la story #1"

**Claude:** [bmad-orchestrator détecte "implémente" → vérifie story existe → bmad-dev activé]
"Je commence l'implémentation avec le BMAD Dev skill.

[lit story file]
[implémente code]
[exécute tests]

Story #1 implémentée avec succès! Tests passent à 100%.
Prêt pour la story #2?"

---

## Scénario 2: Check Status Mid-Project

**User:** "Où en suis-je dans mon projet?"

**Claude:** [bmad-orchestrator activé automatiquement]
"Je vérifie votre statut BMAD...

[lit workflow-status.md]

**Projet:** Budget Tracker App
**Phase actuelle:** Phase 4 - Implementation
**Progression:**
- ✅ Phase 1: Analysis (Complete)
- ✅ Phase 2: Planning (Complete)
- ✅ Phase 3: Solutioning (Complete)
- 🔄 Phase 4: Implementation (In Progress)

**Stories:**
- ✅ Story #1: User Registration (Complete)
- ✅ Story #2: Login System (Complete)
- 🔄 Story #3: Expense Tracking (In Progress)
- ⏳ Story #4: Budget Alerts (Backlog)
- ⏳ Story #5: Reports Dashboard (Backlog)

**Prochaine action recommandée:**
Continuer Story #3 ou démarrer Story #4 si Story #3 est bloquée.

Que voulez-vous faire?"

---

## Scénario 3: Question Architecture Sans Context

**User:** "How should I build a REST API?"

**Claude:** [bmad-orchestrator détecte "build" + "API" → vérifie context]
"Je peux vous aider avec l'architecture! Mais d'abord, quelques questions:

1. Avez-vous un projet BMAD en cours? (Je peux vérifier votre workflow-status)
2. Ou voulez-vous commencer un nouveau projet?
3. Avez-vous déjà un PRD pour cette API?

Si c'est un nouveau projet, je recommande de commencer par:
- Définir le problème (bmad-analyst)
- Créer un PRD (bmad-pm)
- Puis l'architecture (bmad-architecture)

Ou si c'est une simple question d'architecture générale, je peux répondre directement sans activer le workflow BMAD complet.

Que préférez-vous?"

---

## Scénario 4: Pivot Pendant le Projet

**User:** "Actually, I want to change the features in my PRD"

**Claude:** [bmad-orchestrator détecte changement requirements]
"Je comprends, vous voulez modifier le PRD existant.

[lit PRD.md actuel]

Vous aviez:
- Feature A
- Feature B
- Feature C

Que voulez-vous changer?

Note: Si les changements affectent l'architecture ou les stories existantes, je vous recommanderai de mettre à jour les artefacts impactés."

**User:** "Add a social sharing feature"

**Claude:** [bmad-pm activé pour mise à jour]
"Parfait! J'ajoute la fonctionnalité de partage social au PRD.

[met à jour PRD.md]
[ajoute nouvel epic]
[met à jour workflow-status.md]

PRD mis à jour! Cette nouvelle fonctionnalité impacte:
- ✅ PRD: Mis à jour
- ⚠️  Architecture: Peut nécessiter ajout d'API sociales
- ⚠️  Stories: Nouveau story needed

Voulez-vous que je mette à jour l'architecture maintenant?"

---

## Scénario 5: Question Rapide (No BMAD Needed)

**User:** "How do I center a div in CSS?"

**Claude:** [détecte question technique simple, pas de BMAD activation]
"Voici plusieurs façons de centrer un div en CSS:

1. Flexbox (moderne):
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

[continue avec réponse technique...]

Note: Cette question ne nécessite pas le workflow BMAD complet.
Si vous travaillez sur un projet BMAD et voulez intégrer ça dans une story, dites-le moi!"

---

## Patterns d'Activation

### Pattern 1: Détection d'Intent Automatique
```
User intent → Claude détecte keywords → Orchestrator route → Skill activé
```

### Pattern 2: Vérification de Prérequis
```
User demande Phase N → Orchestrator vérifie Phase N-1 complete → Approve or Block
```

### Pattern 3: Status Check Proactif
```
User dit "What's next?" → Orchestrator lit status → Recommande action
```

### Pattern 4: Context-Aware Routing
```
User question ambiguë → Orchestrator demande clarification → Route approprié
```

---

## Anti-Patterns (Ce Qu'on Évite)

### ❌ Anti-Pattern 1: Activation Forcée
**Bad:**
User: "How do I use Python?"
Claude: [Force bmad-orchestrator]

**Good:**
User: "How do I use Python?"
Claude: [Répond directement, pas de BMAD needed]

### ❌ Anti-Pattern 2: Sauter les Phases
**Bad:**
User: "Create architecture"
Claude: [Active bmad-architecture sans vérifier PRD]

**Good:**
User: "Create architecture"
Claude: "Je dois d'abord vérifier que le PRD existe..." [Vérifie et bloque si manquant]

### ❌ Anti-Pattern 3: Over-Orchestration
**Bad:**
User: "What's 2+2?"
Claude: [Active bmad-orchestrator pour répondre]

**Good:**
User: "What's 2+2?"
Claude: "4" [Pas de skill activation needed]

---

## Keywords d'Activation par Skill

### bmad-analyst
- idea, brainstorm, explore, research, thinking, discovery, analyze, investigate, understand

### bmad-pm
- PRD, requirements, plan, build, create, feature, product, epic, roadmap

### bmad-ux
- UX, UI, design, wireframe, user flow, interface, usability, experience

### bmad-architecture
- architecture, tech stack, design, system, build, technical, structure, how to build

### bmad-tea
- test, testing, strategy, QA, quality, ATDD, automation, how to test

### bmad-stories
- story, stories, epic, breakdown, task, backlog, sprint, developer

### bmad-dev
- implement, code, develop, build, program, coding, implementation, write code

### bmad-orchestrator
- status, workflow, next, start, guide, phase, where, initialize, what's next

---

**Mise à jour:** Après implémentation des corrections
**Testez ces scénarios pour valider l'activation automatique!**
```

**Durée estimée:** 1 heure

---

### Tâche 3.2: Mettre à jour README.md

**Fichier:** `README.md`

**Action:** Ajouter une section sur l'activation conversationnelle:

```markdown
## Conversational Activation (NEW!)

BMAD Skills now automatically activate based on natural conversation patterns, following the Bimath method.

### How It Works

Simply talk naturally about your project:

```
You: "I have an idea for a budget tracking app"
Claude: [Automatically activates bmad-analyst for brainstorming]
```

No need to manually invoke skills! The orchestrator detects your intent and routes to the appropriate skill.

### Example Triggers

- **"I have an idea..."** → bmad-analyst (brainstorming)
- **"Create a PRD"** → bmad-pm (requirements)
- **"How should I build this?"** → bmad-architecture (technical design)
- **"Break into stories"** → bmad-stories (story creation)
- **"Implement story X"** → bmad-dev (coding)
- **"What's next?"** → bmad-orchestrator (status check)

See [doc/conversational-flow.md](doc/conversational-flow.md) for complete examples.
```

**Durée estimée:** 15 minutes

---

### Tâche 3.3: Validation avec Utilisateurs Réels

**Action:** Tester avec 3-5 utilisateurs

**Protocole:**
1. Ne pas expliquer comment activer les skills
2. Donner seulement: "Parlez naturellement de votre projet à Claude"
3. Observer si les skills s'activent correctement
4. Noter les cas où ça échoue
5. Ajuster descriptions/triggers si nécessaire

**Scénarios de test:**
- User 1: Nouvelle idée de projet
- User 2: Projet existant, check status
- User 3: Demande PRD directement
- User 4: Question d'architecture
- User 5: Implémentation directe

**Durée estimée:** 2 heures

---

## RÉCAPITULATIF

### Checklist Complète

#### Jour 1 (3.5 heures)
- [ ] Modifier meta/MANIFEST.json (12 descriptions)
- [ ] Ajouter "When to Invoke" à bmad-orchestrator
- [ ] Ajouter "When to Invoke" à bmad-analyst
- [ ] Ajouter "When to Invoke" à bmad-pm
- [ ] Ajouter "When to Invoke" à bmad-ux
- [ ] Ajouter "When to Invoke" à bmad-architecture
- [ ] Ajouter "When to Invoke" à bmad-tea
- [ ] Ajouter "When to Invoke" à bmad-stories
- [ ] Ajouter "When to Invoke" à bmad-dev

#### Jour 2 (4 heures)
- [ ] Migrer info activation REFERENCE.md → SKILL.md (orchestrator)
- [ ] Migrer info activation REFERENCE.md → SKILL.md (analyst)
- [ ] Ajouter "Auto-Activation Behavior" à orchestrator
- [ ] Créer tests/test_skill_activation.md
- [ ] Exécuter tests d'activation

#### Jour 3 (3.5 heures)
- [ ] Créer doc/conversational-flow.md
- [ ] Mettre à jour README.md
- [ ] Tests avec utilisateurs réels (3-5 personnes)
- [ ] Ajustements finaux basés sur feedback

**Total: ~11 heures = 2-3 jours de travail**

---

## RÉSULTAT ATTENDU

**Avant corrections:**
```
User: "I have an idea for an app"
Claude: "That's interesting! Tell me more."
User: "Initialize BMAD workflow"
Claude: [bmad-orchestrator activé]
```

**Après corrections:**
```
User: "I have an idea for an app"
Claude: [bmad-analyst auto-activé]
"Great! Let's brainstorm together. Tell me about your app..."
```

---

## SCORE ATTENDU

| Métrique | Avant | Après | Delta |
|----------|-------|-------|-------|
| Activation Auto | 45% | 95% | +50% |
| Flow Conversationnel | 40% | 95% | +55% |
| Tests | 60% | 85% | +25% |
| **GLOBAL** | **85%** | **95%** | **+10%** |

---

**Ready to start? Begin with Jour 1, Tâche 1.1!** 🚀
