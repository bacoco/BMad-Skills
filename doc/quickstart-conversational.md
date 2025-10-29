# Guide de Démarrage Rapide - Activation Conversationnelle

**Pour utilisateurs de BMAD Skills avec Claude**
**Version:** 1.0.0
**Date:** 2025-10-29

---

## 🚀 Démarrage en 30 Secondes

### Étape 1: Installation (Si pas déjà fait)
```bash
# Copiez les skills dans votre projet
cp -r .claude/skills ~/.claude/skills/
cp -r shared ~/.claude/shared/
cp -r meta ~/.claude/meta/
```

### Étape 2: Commencez à Parler Naturellement!

**C'est tout!** Plus besoin de commandes spéciales. Parlez naturellement:

```
Vous: "J'ai une idée pour une app de budget"
Claude: [Auto-active bmad-analyst] "Super! Parlons-en..."
```

---

## 💡 Exemples par Cas d'Usage

### Cas 1: Nouvelle Idée de Produit

**Vous dites simplement:**
```
"J'ai une idée pour une app qui aide les gens à suivre leurs dépenses"
```

**Ce qui se passe automatiquement:**
1. ✅ bmad-orchestrator s'active
2. ✅ Détecte "nouvelle idée" + complexité Level 3
3. ✅ Route vers bmad-analyst
4. ✅ Commence brainstorming

**Claude répond:**
```
Great! Je vais vous aider à structurer cette idée avec le BMAD Analyst.

Parlons de votre app de suivi des dépenses:
- Quel problème spécifique voulez-vous résoudre?
- Qui sont vos utilisateurs cibles?
- Qu'est-ce qui vous a donné cette idée?

[Commence le brainstorming structuré]
```

---

### Cas 2: Bug Fix Rapide

**Vous dites simplement:**
```
"Fix this bug: le bouton de login ne fonctionne pas sur mobile"
```

**Ce qui se passe automatiquement:**
1. ✅ bmad-orchestrator s'active
2. ✅ Détecte "fix bug" + Level 0-1
3. ✅ Route vers openspec-propose
4. ✅ Crée proposition légère

**Claude répond:**
```
Je vais créer une proposition de changement léger avec OpenSpec.

**Proposition: Login Button Mobile Fix**
- Problème: Bouton non cliquable sur mobile
- Solution: Fix CSS touch events
- Niveau: 0 (simple bug fix)
- Temps estimé: 1-2h

Proposition créée! Voulez-vous que je l'implémente maintenant?
```

---

### Cas 3: Vérifier le Status

**Vous dites simplement:**
```
"Où en suis-je dans mon projet?"
```

**Ce qui se passe automatiquement:**
1. ✅ bmad-orchestrator s'active
2. ✅ Lit workflow-status.md
3. ✅ Retourne status complet

**Claude répond:**
```
Voici votre statut BMAD:

**Projet:** Budget Tracker App
**Phase:** Implementation (Phase 4)
**Progression:**
- ✅ Analysis: Complete
- ✅ Planning: Complete (PRD, Epics)
- ✅ Architecture: Complete
- 🔄 Implementation: 3/5 stories done

**Prochaine action:** Implement Story #4: Budget Alerts

Voulez-vous commencer Story #4?
```

---

## 🎯 Phrases Magiques par Objectif

### Pour Brainstormer
- "J'ai une idée pour..."
- "What if we built..."
- "Help me think through..."
- "I'm thinking about..."

→ **Auto-active:** bmad-analyst

### Pour Créer un PRD
- "I want to build..."
- "Create a PRD for..."
- "Plan this feature..."
- "Write requirements..."

→ **Auto-active:** bmad-pm

### Pour l'Architecture
- "How should I build this?"
- "What's the architecture?"
- "Choose tech stack..."
- "System design for..."

→ **Auto-active:** bmad-architecture

### Pour Coder
- "Implement story #5"
- "Start coding..."
- "Develop this feature..."
- "Let's code..."

→ **Auto-active:** bmad-dev

### Pour un Bug Fix
- "Fix this bug: ..."
- "Small change needed..."
- "Quick fix for..."

→ **Auto-active:** openspec-propose

### Pour Checker le Status
- "What's next?"
- "Where am I?"
- "Check status"
- "BMAD status"

→ **Auto-active:** bmad-orchestrator

---

## 📋 Flow Complet: Exemple Réel

### Scénario: Créer une App de Todo List

**Session Complète (10 minutes de conversation naturelle):**

```
👤 Vous: "J'ai une idée pour une app de todo list"

🤖 Claude: [bmad-analyst activé]
Great! Parlons-en. Qu'est-ce qui rend votre todo list différente?

👤 Vous: "Elle utilise l'IA pour prioriser automatiquement les tâches"

🤖 Claude: Intéressant! Je documente ça...
[Crée docs/brainstorm-notes.md]
Voulez-vous que je crée un PRD maintenant?

👤 Vous: "Oui, créons le PRD"

🤖 Claude: [bmad-pm activé]
Parfait! Basé sur notre brainstorming...
[Génère docs/PRD.md et docs/epics.md]
PRD créé! Prêt pour l'architecture?

👤 Vous: "Oui, quelle architecture recommandez-vous?"

🤖 Claude: [bmad-architecture activé]
Pour votre app de todo list avec IA...
[Génère docs/ARCHITECTURE.md]
- Frontend: React Native
- Backend: Node.js + Express
- AI: OpenAI API
- Database: PostgreSQL
Architecture définie! Créons les stories maintenant?

👤 Vous: "Oui, breakdown en stories"

🤖 Claude: [bmad-stories activé]
Je crée les stories...
[Génère stories/*.md]
✅ 8 stories créées!
Story #1 est prête. Voulez-vous l'implémenter?

👤 Vous: "Oui, implémente story #1"

🤖 Claude: [bmad-dev activé]
J'implémente Story #1: User Authentication...
[Code, tests, documentation]
✅ Story #1 complète! Tests passent à 100%.
Prêt pour Story #2?
```

**Temps total: 10 minutes**
**Artefacts générés:**
- ✅ brainstorm-notes.md
- ✅ PRD.md
- ✅ epics.md
- ✅ ARCHITECTURE.md
- ✅ 8 story files
- ✅ Code + tests pour Story #1

**0 commandes manuelles nécessaires!**

---

## ⚡ Conseils Pro

### 1. Soyez Naturel
❌ **Mauvais:** "Initialize BMAD workflow then invoke bmad-analyst"
✅ **Bon:** "I have an idea for an app"

### 2. Soyez Spécifique
❌ **Mauvais:** "Do something"
✅ **Bon:** "Create a PRD for my budget tracker app"

### 3. Utilisez les Mots-Clés Naturellement
Les mots-clés sont dans votre langage naturel:
- "idea", "brainstorm" → Analyst
- "build", "PRD" → PM
- "architecture", "tech stack" → Architecture
- "fix", "bug" → OpenSpec

### 4. Laissez Claude Guider
Claude va vous poser des questions pour clarifier:
```
Claude: "Est-ce un projet complexe (BMAD) ou un simple changement (OpenSpec)?"
```
Répondez naturellement!

### 5. Suivez le Flow
Claude vous dira toujours ce qui vient après:
```
Claude: "PRD créé! Prêt pour l'architecture?"
```
Vous pouvez dire simplement "oui" ou "yes"!

---

## 🔍 Dépannage Rapide

### "Claude ne détecte pas mon intention"

**Problème:** Vous dites "work on the project" mais rien ne se passe.

**Solution:** Soyez plus explicite:
- Au lieu de: "work on project"
- Dites: "implement story #3" ou "create PRD" ou "fix this bug"

### "Je veux changer de phase"

**Pas besoin de commande spéciale!**
```
Vous: "Actually, I want to go back and update the PRD"
Claude: [Détecte "update PRD" → bmad-pm activé]
```

### "Je veux savoir où je suis"

**Dites simplement:**
```
Vous: "What's next?" ou "Where am I?" ou "Status?"
Claude: [bmad-orchestrator activé → lit status → répond]
```

### "Claude active le mauvais skill"

**Clarifiez votre intention:**
```
Vous: "I mean implement the story, not create a new one"
Claude: [Corrige et active bmad-dev au lieu de bmad-stories]
```

---

## 📚 Ressources Supplémentaires

### Documentation Complète
- **Flow conversationnel:** [doc/conversational-flow.md](conversational-flow.md) - 6 scénarios détaillés
- **Tests d'activation:** [tests/test_skill_activation.md](../tests/test_skill_activation.md) - 55 cas de test
- **FAQ:** [doc/activation-faq.md](activation-faq.md) - Questions fréquentes
- **Troubleshooting:** [doc/troubleshooting.md](troubleshooting.md) - Guide de dépannage

### Référence Rapide des Skills
- **bmad-orchestrator:** Status, routing, guidance
- **bmad-analyst:** Brainstorm, research, discovery
- **bmad-pm:** PRD, epics, planning
- **bmad-ux:** UX design, wireframes
- **bmad-architecture:** Tech stack, system design
- **bmad-tea:** Test strategy, QA
- **bmad-stories:** Story breakdown
- **bmad-dev:** Implementation, coding
- **openspec-propose:** Bug fixes, small changes
- **openspec-implement:** Execute fixes
- **openspec-archive:** Close changes

---

## ✅ Checklist de Réussite

Après avoir lu ce guide, vous devriez pouvoir:

- [ ] Démarrer une nouvelle idée sans commandes manuelles
- [ ] Créer un PRD complet en conversation naturelle
- [ ] Fixer un bug rapidement avec OpenSpec
- [ ] Vérifier votre status à tout moment
- [ ] Naviguer entre les phases naturellement
- [ ] Comprendre pourquoi Claude active tel ou tel skill

**Si vous cochez toutes les cases: Bravo! Vous maîtrisez l'activation conversationnelle! 🎉**

---

## 🚀 Prochaines Étapes

1. **Essayez maintenant:** Ouvrez Claude et dites "J'ai une idée pour..."
2. **Explorez:** Testez différentes phrases pour voir les activations
3. **Partagez:** Montrez à votre équipe comment ça marche
4. **Feedback:** Notez les cas où ça ne marche pas comme prévu

---

**Questions? Consultez la [FAQ](activation-faq.md) ou le [Troubleshooting Guide](troubleshooting.md)!**

**Version:** 1.0.0 | **Dernière mise à jour:** 2025-10-29
