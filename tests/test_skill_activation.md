# Tests d'Activation Automatique des Skills

**Date:** 2025-10-29
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

## Test 9: Bug Fix (OpenSpec) → openspec-propose

### Inputs à tester
- "Fix this bug: login button not working"
- "Small change needed in the header component"
- "Quick fix for the validation error"
- "Simple bug: users can't submit form"
- "Minor update to the API endpoint"

### Comportement Attendu
1. bmad-orchestrator détecte "bug fix / small change"
2. Évalue comme Level 0-1
3. openspec-propose activé
4. Crée proposition légère dans openspec/changes/

### Résultats
- [ ] Test 9.1: ✅ / ❌
- [ ] Test 9.2: ✅ / ❌
- [ ] Test 9.3: ✅ / ❌
- [ ] Test 9.4: ✅ / ❌
- [ ] Test 9.5: ✅ / ❌

---

## Test 10: Apply Change → openspec-implement

### Inputs à tester
- "Implement this bug fix"
- "Apply the change from proposal-123"
- "Execute this fix"
- "Implement the proposed change"
- "Apply this quick fix"

### Comportement Attendu
1. bmad-orchestrator détecte "implement/apply"
2. Vérifie qu'une proposition OpenSpec existe
3. openspec-implement activé
4. Exécute les tâches définies

### Résultats
- [ ] Test 10.1: ✅ / ❌
- [ ] Test 10.2: ✅ / ❌
- [ ] Test 10.3: ✅ / ❌
- [ ] Test 10.4: ✅ / ❌
- [ ] Test 10.5: ✅ / ❌

---

## Test 11: Archive Change → openspec-archive

### Inputs à tester
- "Archive this change"
- "Close proposal-123"
- "Document the completed fix"
- "Finalize this change"
- "Mark this change as complete"

### Comportement Attendu
1. bmad-orchestrator détecte "archive/close"
2. Vérifie que le changement est implémenté
3. openspec-archive activé
4. Documente et archive le changement

### Résultats
- [ ] Test 11.1: ✅ / ❌
- [ ] Test 11.2: ✅ / ❌
- [ ] Test 11.3: ✅ / ❌
- [ ] Test 11.4: ✅ / ❌
- [ ] Test 11.5: ✅ / ❌

---

## Résumé des Tests

**Total tests:** 55 (8 BMAD skills + 3 OpenSpec skills = 11 scenarios × 5 tests)
**Tests réussis:** ___ / 55
**Tests échoués:** ___ / 55
**Taux de succès:** ___%

### Problèmes Identifiés
1. [Liste des problèmes]
2. [...]

### Corrections Nécessaires
1. [Actions correctives]
2. [...]

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

### openspec-propose
- bug, fix, small, quick, simple, minor, lightweight, Level 0, Level 1

### openspec-implement
- apply, execute, implement change, fix, proposal, Level 0, Level 1

### openspec-archive
- archive, close, document, finalize, complete, Level 0, Level 1

---

**Testeur:** [NOM]
**Date de test:** [DATE]
**Version skills:** 1.0.0
