# Guide des Flows Conversationnels BMAD

Ce document montre des exemples de conversations naturelles et comment les skills BMAD s'activent automatiquement selon la méthode Bimath.

---

## Principe Fondamental

**Avec les corrections d'activation automatique**, l'utilisateur discute naturellement avec Claude, et les skills appropriés s'activent automatiquement basés sur:
- Les mots-clés détectés dans la conversation
- Le contexte du projet (phase actuelle)
- Les déclencheurs conversationnels définis

**Plus besoin de dire** "Initialize BMAD workflow" ou "Invoke bmad-analyst" - **tout est automatique**.

---

## Scénario 1: Nouvelle Idée → PRD → Architecture → Implémentation

### Conversation Complète

**User:** "J'ai une idée pour une app de gestion de budget"

**Claude:** [bmad-orchestrator détecte "idée" → bmad-analyst activé automatiquement]
```
Super! Je vais vous aider à structurer cette idée avec le BMAD Analyst.
Commençons par un brainstorming. Parlez-moi plus de votre app de budget:
- Quel problème cherchez-vous à résoudre?
- Qui sont vos utilisateurs cibles?
- Qu'est-ce qui vous a donné cette idée?
```

**User:** "Je veux aider les gens à suivre leurs dépenses quotidiennes facilement. L'app serait pour les jeunes professionnels."

**Claude:** [bmad-analyst continue le brainstorming]
```
Excellent contexte! Je vois plusieurs directions possibles:
1. Suivi automatique via connexion bancaire
2. Saisie manuelle simplifiée
3. Catégorisation intelligente des dépenses
4. Alertes budget

Explorons ces directions...
[continue brainstorming]

Voulez-vous que je crée un product brief formel maintenant?
```

**User:** "Oui, créons le PRD"

**Claude:** [bmad-orchestrator détecte "PRD" → vérifie phase → bmad-pm activé]
```
Parfait! Le brainstorming est terminé. Je passe maintenant au BMAD PM pour créer votre PRD.

Basé sur notre discussion, voici le PRD:
[génère docs/PRD.md]

Maintenant, décomposons en epics:
[génère docs/epics.md]

PRD et epics créés! Prêt pour l'architecture?
```

**User:** "Oui, quelle architecture recommandez-vous?"

**Claude:** [bmad-orchestrator détecte "architecture" → vérifie PRD existe → bmad-architecture activé]
```
Je vais maintenant travailler sur l'architecture avec le BMAD Architect.

Analysons les besoins techniques:
- App mobile (iOS + Android)
- Backend API
- Base de données pour transactions
[...]

[génère docs/ARCHITECTURE.md]

Architecture définie! Voulez-vous que je crée les stories pour commencer l'implémentation?
```

---

## Scénario 2: Check Status Mid-Project

**User:** "Où en suis-je dans mon projet?"

**Claude:** [bmad-orchestrator activé automatiquement]
```
Je vérifie votre statut BMAD...

[lit docs/bmad-workflow-status.md]

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

**Prochaine action recommandée:**
Continuer Story #3 ou démarrer Story #4 si Story #3 est bloquée.

Que voulez-vous faire?
```

---

## Scénario 3: Question Architecture Sans Context

**User:** "How should I build a REST API?"

**Claude:** [bmad-orchestrator détecte "build" + "API" → vérifie context]
```
Je peux vous aider avec l'architecture! Mais d'abord, quelques questions:

1. Avez-vous un projet BMAD en cours? (Je peux vérifier votre workflow-status)
2. Ou voulez-vous commencer un nouveau projet?
3. Avez-vous déjà un PRD pour cette API?

Si c'est un nouveau projet, je recommande de commencer par:
- Définir le problème (bmad-analyst)
- Créer un PRD (bmad-pm)
- Puis l'architecture (bmad-architecture)

Ou si c'est une simple question d'architecture générale, je peux répondre directement sans activer le workflow BMAD complet.

Que préférez-vous?
```

---

## Scénario 4: Implémentation Directe

**User:** "Implement story #3"

**Claude:** [bmad-orchestrator détecte "implement" → vérifie story existe → bmad-dev activé]
```
Je commence l'implémentation avec le BMAD Dev skill.

[lit stories/expense-tracking.md]

**Story #3: Expense Tracking**
- Acceptation Criteria: [liste]
- Tasks: [liste]
- Architecture patterns: [références]

Je vais maintenant:
1. Créer les modèles de données pour les dépenses
2. Implémenter l'API d'enregistrement
3. Ajouter les tests
4. Mettre à jour le Dev Agent Record

Commençons...

[implémente code]
[exécute tests]

✅ Story #3 implémentée avec succès! Tests passent à 100%.
Prêt pour la story #4?
```

---

## Scénario 5: Question Rapide (No BMAD Needed)

**User:** "How do I center a div in CSS?"

**Claude:** [détecte question technique simple, pas de BMAD activation]
```
Voici plusieurs façons de centrer un div en CSS:

1. Flexbox (moderne):
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
}
```

2. Grid (moderne):
```css
.container {
  display: grid;
  place-items: center;
}
```

3. Position absolute (classique):
```css
.container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
```

Note: Cette question ne nécessite pas le workflow BMAD complet.
Si vous travaillez sur un projet BMAD et voulez intégrer ça dans une story, dites-le moi!
```

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
```
User: "How do I use Python?"
Claude: [Force bmad-orchestrator]
```

**Good:**
```
User: "How do I use Python?"
Claude: [Répond directement, pas de BMAD needed]
```

### ❌ Anti-Pattern 2: Sauter les Phases
**Bad:**
```
User: "Create architecture"
Claude: [Active bmad-architecture sans vérifier PRD]
```

**Good:**
```
User: "Create architecture"
Claude: "Je dois d'abord vérifier que le PRD existe..."
[Vérifie et bloque si manquant]
```

### ❌ Anti-Pattern 3: Over-Orchestration
**Bad:**
```
User: "What's 2+2?"
Claude: [Active bmad-orchestrator pour répondre]
```

**Good:**
```
User: "What's 2+2?"
Claude: "4" [Pas de skill activation needed]
```

---

## Keywords d'Activation par Skill

### bmad-analyst
**Keywords:** idea, brainstorm, explore, research, thinking, discovery, analyze

**Phrases:** "I have an idea", "What if we", "Help me think", "Let's explore"

### bmad-pm
**Keywords:** PRD, requirements, plan, build, create, feature, product, epic

**Phrases:** "Create a PRD", "I want to build", "Plan this feature", "Write requirements"

### bmad-ux
**Keywords:** UX, UI, design, wireframe, user flow, interface, usability

**Phrases:** "What should UI look like", "Design the UX", "Create wireframes", "User flow"

### bmad-architecture
**Keywords:** architecture, tech stack, design, system, build, technical

**Phrases:** "How should we build", "What's the architecture", "Choose tech stack", "System design"

### bmad-tea
**Keywords:** test, testing, strategy, QA, quality, ATDD, automation

**Phrases:** "How should we test", "Create test strategy", "Test plan", "ATDD"

### bmad-stories
**Keywords:** story, stories, epic, breakdown, task, backlog, sprint

**Phrases:** "Break into stories", "Create user stories", "Story breakdown", "Developer tasks"

### bmad-dev
**Keywords:** implement, code, develop, build, program, coding

**Phrases:** "Implement story", "Start coding", "Develop this", "Let's code", "Write code"

### bmad-orchestrator
**Keywords:** status, workflow, next, start, guide, phase, where, initialize

**Phrases:** "What's next", "Where am I", "Check status", "Start project", "Initialize"

---

## Conclusion

Avec ces corrections d'activation automatique:

✅ **L'utilisateur discute naturellement**
✅ **Claude détecte l'intention automatiquement**
✅ **Les skills s'activent sans invocation manuelle**
✅ **Le flow BMAD complet est fluide et conversationnel**

**C'est la méthode Bimath en action!**

---

**Version:** 1.0.0 (Post-corrections)
**Date:** 2025-10-29
