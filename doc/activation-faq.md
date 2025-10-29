# FAQ - Activation Conversationnelle des Skills

**Questions Fréquentes sur l'utilisation des BMAD Skills**
**Version:** 1.0.0

---

## 🎯 Questions Générales

### Q1: Dois-je apprendre des commandes spéciales?

**R:** Non! Plus besoin de commandes. Parlez naturellement:
- ❌ Avant: "Initialize BMAD workflow"
- ✅ Maintenant: "J'ai une idée pour une app"

### Q2: Comment Claude sait-il quel skill activer?

**R:** Claude détecte automatiquement votre intention via:
1. **Mots-clés:** "idea" → analyst, "fix bug" → openspec
2. **Contexte:** Où vous en êtes dans le projet
3. **Patterns:** "I want to build" → pm, "implement story" → dev

### Q3: Que se passe-t-il si je ne sais pas quoi dire?

**R:** Dites simplement:
- "What's next?" → Claude vous guide
- "Where am I?" → Claude vous dit où vous en êtes
- "Help me start" → Claude vous pose des questions

### Q4: Puis-je encore utiliser les anciennes commandes?

**R:** Les anciennes commandes fonctionnent toujours, mais elles ne sont plus nécessaires. L'activation automatique est plus naturelle et efficace.

### Q5: Est-ce que ça marche en français ET en anglais?

**R:** Oui! Les skills détectent les deux langues:
- Français: "J'ai une idée", "Créer un PRD", "Corrige ce bug"
- Anglais: "I have an idea", "Create a PRD", "Fix this bug"

---

## 🔄 Questions sur le Routing

### Q6: Comment Claude choisit entre BMAD et OpenSpec?

**R:** Basé sur la complexité (Levels 0-4):

**OpenSpec (Level 0-1):**
- Bug fix simple
- Petit changement
- Feature légère
- Modification mineure

**BMAD (Level 2-4):**
- Nouveau produit
- Feature complexe
- Nouvelle architecture
- Projet greenfield

**Exemple:**
```
"Fix button color" → OpenSpec (Level 0)
"Build new authentication system" → BMAD (Level 3)
```

### Q7: Que faire si Claude choisit le mauvais workflow?

**R:** Clarifiez simplement:
```
Vous: "Actually this is more complex, it needs full architecture"
Claude: [Passe de OpenSpec à BMAD]
```

### Q8: Puis-je forcer un workflow spécifique?

**R:** Oui, soyez explicite:
```
"I want to use OpenSpec for this quick fix"
"This needs the full BMAD workflow"
```

### Q9: Comment Claude sait-il quelle phase vient après?

**R:** Claude vérifie automatiquement:
1. Les prérequis (PRD existe? Architecture faite?)
2. Les artifacts complétés
3. Les quality gates passés

Si un prérequis manque, Claude vous le dira.

---

## 🎨 Questions sur les Skills Spécifiques

### Q10: Comment activer bmad-analyst?

**R:** Mentionnez:
- Une nouvelle **idée**: "I have an idea for..."
- Du **brainstorming**: "Help me think through..."
- De l'**exploration**: "Let's explore possibilities..."
- De la **recherche**: "I need to research..."

### Q11: Comment activer bmad-pm?

**R:** Mentionnez:
- **PRD**: "Create a PRD"
- **Requirements**: "Write requirements"
- **Building**: "I want to build..."
- **Planning**: "Plan this feature"

### Q12: Comment activer openspec-propose?

**R:** Mentionnez:
- **Bug**: "Fix this bug"
- **Small change**: "Quick change needed"
- **Simple**: "Simple fix for..."
- **Minor**: "Minor update to..."

### Q13: Comment activer bmad-dev?

**R:** Mentionnez:
- **Implement**: "Implement story #5"
- **Code**: "Start coding..."
- **Develop**: "Develop this feature"
- **Build**: "Build the authentication"

### Q14: Comment vérifier mon status?

**R:** Dites simplement:
- "What's next?"
- "Where am I?"
- "Check status"
- "BMAD status"

→ bmad-orchestrator s'active automatiquement

---

## ⚠️ Questions sur les Problèmes Courants

### Q15: Claude n'active aucun skill, pourquoi?

**Causes possibles:**
1. **Question trop vague:** "Do something" → Soyez plus spécifique
2. **Question technique simple:** "What is Python?" → Pas besoin de skill
3. **Conversation générale:** "How are you?" → Pas de skill nécessaire

**Solution:** Soyez explicite sur votre intention de développement.

### Q16: Claude active le mauvais skill

**Exemple:**
```
Vous: "Break this down"
Claude: [Active bmad-analyst au lieu de bmad-stories]
```

**Solution:** Clarifiez:
```
Vous: "I mean break the epic into stories"
Claude: [Corrige → active bmad-stories]
```

### Q17: Je suis bloqué à une phase

**Symptôme:**
```
Claude: "PRD non trouvé, impossible de créer l'architecture"
```

**Solution:**
Claude vous dit ce qui manque. Complétez d'abord:
```
Vous: "Create the PRD first then"
Claude: [Active bmad-pm]
```

### Q18: Les tests échouent pendant l'implémentation

**Claude dit:**
```
"Tests failing, cannot mark story complete"
```

**C'est normal!** bmad-dev refuse de continuer si tests échouent.

**Solutions:**
1. Fixez les tests
2. Claude vous aide à débugger
3. Une fois les tests verts, Claude continue

### Q19: Je veux changer quelque chose déjà fait

**Exemple:** PRD déjà créé mais vous voulez le modifier.

**Solution:** Dites simplement:
```
Vous: "Update the PRD, add feature X"
Claude: [bmad-pm s'active en mode update]
```

---

## 🔧 Questions Techniques

### Q20: Comment les skills communiquent entre eux?

**R:** Via l'orchestrateur:
1. Chaque skill produit des artifacts (PRD, stories, code)
2. L'orchestrateur track ces artifacts dans workflow-status.md
3. Les skills suivants lisent ces artifacts
4. Continuité automatique assurée

### Q21: Où sont stockés mes artifacts?

**R:** Structure standardisée:
```
docs/
  ├── brainstorm-notes.md    # bmad-analyst
  ├── PRD.md                 # bmad-pm
  ├── epics.md               # bmad-pm
  ├── ARCHITECTURE.md        # bmad-architecture
  └── workflow-status.md     # bmad-orchestrator

stories/
  └── epic-1-story-1.md      # bmad-stories

openspec/
  └── changes/
      └── fix-123/           # openspec-*
```

### Q22: Puis-je voir les logs d'activation?

**R:** Oui! Utilisez le système de métriques:
```bash
python shared/tooling/activation_metrics.py view
```

(Voir section Métriques pour plus de détails)

### Q23: Comment tester l'activation avant production?

**R:** Utilisez les test cases:
```
tests/test_skill_activation.md
- 55 scenarios de test
- Comportements attendus
- Checklist de validation
```

---

## 📊 Questions sur les Métriques

### Q24: Comment savoir si mes skills s'activent correctement?

**R:** Plusieurs indicateurs:
1. **Immédiat:** Claude mentionne le skill activé
   ```
   Claude: [bmad-analyst activé] "Let's brainstorm..."
   ```
2. **Logs:** Consultez les métriques (voir Q22)
3. **Artifacts:** Vérifiez que les bons fichiers sont créés

### Q25: Quelles métriques sont trackées?

**R:** Le système track:
- Skill activé
- Trigger phrase utilisée
- Confidence score
- Contexte (phase actuelle)
- Timestamp
- Résultat (succès/échec)

### Q26: Comment améliorer les activations?

**R:** Basé sur les métriques:
1. Identifiez les patterns qui échouent
2. Ajoutez des keywords si nécessaire
3. Clarifiez les descriptions
4. Testez avec les nouveaux patterns

---

## 🚀 Questions Avancées

### Q27: Puis-je créer mes propres skills?

**R:** Oui! Utilisez skill-creator:
```
Vous: "Create a new skill for [use case]"
Claude: [skill-creator activé] "Let's design your skill..."
```

Voir: `.claude/skills/skill-creator/SKILL.md`

### Q28: Comment personnaliser les triggers?

**R:** Modifiez les descriptions dans les SKILL.md:
```yaml
description: "... Invoke when: [vos triggers]. Keywords: [vos mots-clés]"
```

### Q29: Puis-je désactiver certains skills?

**R:** Oui, commentez dans le MANIFEST.json:
```json
// {
//   "id": "skill-name",
//   ...
// }
```

### Q30: Comment contribuer des améliorations?

**R:**
1. Testez avec vos propres use cases
2. Documentez les patterns manquants
3. Ouvrez une issue/PR sur le repo
4. Partagez vos métriques d'activation

---

## 🎓 Questions Pédagogiques

### Q31: Comment expliquer ça à mon équipe?

**R:** Utilisez ces ressources:
1. **Quickstart (5 min):** `doc/quickstart-conversational.md`
2. **Exemples (10 min):** `doc/conversational-flow.md`
3. **Demo live (15 min):** Montrez une session complète

### Q32: Quelle est la courbe d'apprentissage?

**R:**
- **5 minutes:** Comprendre le concept
- **15 minutes:** Tester les premières activations
- **30 minutes:** Maîtriser les patterns principaux
- **1 heure:** Utiliser couramment tous les skills

### Q33: Y a-t-il des pièges à éviter?

**R:** Oui, les anti-patterns:
1. ❌ Être trop vague: "Do something"
2. ❌ Utiliser jargon technique: "Instantiate workflow"
3. ❌ Sauter des phases: "Create architecture" sans PRD
4. ❌ Over-orchestrate: Tout passer par orchestrator

Soyez naturel, spécifique, et suivez le flow!

### Q34: Comment mesurer l'efficacité vs l'ancien système?

**Métriques comparatives:**

**Avant (commandes manuelles):**
- Temps moyen par phase: +30%
- Erreurs d'utilisation: Fréquentes
- Courbe d'apprentissage: 2-3 heures
- Friction utilisateur: Élevée

**Après (activation conversationnelle):**
- Temps moyen par phase: Baseline
- Erreurs d'utilisation: Rares
- Courbe d'apprentissage: 30 minutes
- Friction utilisateur: Minimale

---

## 📞 Obtenir de l'Aide

### Q35: Où trouver plus d'aide?

**Documentation:**
- **Quickstart:** `doc/quickstart-conversational.md`
- **Flow examples:** `doc/conversational-flow.md`
- **Troubleshooting:** `doc/troubleshooting.md`
- **Tests:** `tests/test_skill_activation.md`

**Support:**
- Issues GitHub: [lien repo]
- Documentation complète: `doc/`
- Audit complet: `AUDIT-REPORT.md`

### Q36: Comment reporter un problème d'activation?

**Incluez:**
1. Phrase exacte utilisée
2. Skill attendu vs activé
3. Contexte (phase, artifacts existants)
4. Logs si disponibles

**Format:**
```
**Phrase:** "Fix this bug"
**Attendu:** openspec-propose
**Activé:** bmad-analyst
**Contexte:** Projet existant, Level 1
**Logs:** [collez les logs]
```

---

## 🎉 Conclusion

### Q37: En résumé, qu'est-ce qui a changé?

**AVANT:**
- Commandes manuelles obligatoires
- Syntaxe à apprendre
- Risque d'erreur élevé
- Friction utilisateur

**MAINTENANT:**
- Conversation naturelle
- Zéro syntaxe à apprendre
- Activation automatique intelligente
- Experience fluide

**= 10x plus simple!**

### Q38: Dois-je tout relire?

**R:** Non! Utilisez cette FAQ comme référence:
- **Débutant?** → Lisez Q1-Q5, Q10-Q14
- **Problème?** → Q15-Q19
- **Avancé?** → Q27-Q30
- **Équipe?** → Q31-Q34

### Q39: Quelle est la prochaine étape?

**R:** Essayez maintenant!
```
Ouvrez Claude et dites:
"J'ai une idée pour une app de [votre idée]"
```

Laissez la magie opérer! ✨

---

**Questions non répondues? Consultez:**
- [Troubleshooting Guide](troubleshooting.md)
- [Conversational Flow Examples](conversational-flow.md)
- [Test Cases](../tests/test_skill_activation.md)

**Version:** 1.0.0 | **39 Questions** | **Dernière mise à jour:** 2025-10-29
