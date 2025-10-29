# Guide de Troubleshooting - Activation Conversationnelle

**Résolution des problèmes d'activation des BMAD Skills**
**Version:** 1.0.0

---

## 🔍 Diagnostic Rapide

### Identifiez votre problème:

| Symptôme | Section |
|----------|---------|
| Claude n'active aucun skill | [Pas d'Activation](#pas-dactivation) |
| Claude active le mauvais skill | [Mauvais Skill](#mauvais-skill-activé) |
| Skill bloqué/refuse de continuer | [Skill Bloqué](#skill-bloqué) |
| Tests échouent | [Problèmes de Tests](#problèmes-de-tests) |
| Artifacts manquants | [Artifacts Perdus](#artifacts-manquants) |
| Phase sautée | [Phases Manquées](#phases-sautées) |
| OpenSpec vs BMAD confusion | [Routing Confusion](#confusion-openspec-vs-bmad) |

---

## 🚫 Pas d'Activation

### Symptôme
```
Vous: "Do something with the project"
Claude: "I'd be happy to help! Can you be more specific?"
[Aucun skill ne s'active]
```

### Causes Possibles

#### Cause 1: Phrase Trop Vague

**Problème:** Pas assez de mots-clés pour détecter l'intention.

**Mauvais exemples:**
- "Work on this"
- "Do something"
- "Help me"
- "Continue"

**Solutions:**
- ✅ "I have an idea for an app" → bmad-analyst
- ✅ "Fix this bug: login fails" → openspec-propose
- ✅ "Create a PRD for my project" → bmad-pm
- ✅ "What's next?" → bmad-orchestrator

**Pattern:** [Action] + [Objet spécifique]

#### Cause 2: Question Technique Simple

**Problème:** Claude répond directement sans activer de skill.

**C'est normal pour:**
- "What is Python?"
- "How to center a div?"
- "Explain REST APIs"

**Ces questions n'ont pas besoin de skills!**

**Si vous voulez un skill:**
```
❌ "What is React?"
✅ "I want to build a React app" → bmad-pm/analyst
```

#### Cause 3: Contexte Manquant

**Problème:** Claude ne sait pas si c'est du développement.

**Exemple:**
```
Vous: "Break this down"
Claude: "Break what down?"
```

**Solution:** Ajoutez le contexte:
```
✅ "Break this epic into developer stories" → bmad-stories
✅ "Break down the requirements" → bmad-pm
```

### Solution Générale: La Formule Magique

**Utilisez:** [Verbe d'Action] + [Nom Technique] + [Contexte]

**Exemples:**
- **[Créer]** + **[PRD]** + **[pour mon app]** → bmad-pm
- **[Implémenter]** + **[story]** + **[#5]** → bmad-dev
- **[Fixer]** + **[bug]** + **[login button]** → openspec-propose

---

## ⚠️ Mauvais Skill Activé

### Symptôme
```
Vous: "Break this down"
Claude: [bmad-analyst activé au lieu de bmad-stories]
```

### Causes & Solutions

#### Cas 1: Ambiguïté dans la Phrase

**Problème:** "Break down" peut signifier:
- Analyser/Décomposer un problème → analyst
- Créer des stories → stories

**Solution: Soyez explicite**
```
❌ "Break this down"
✅ "Break this epic into stories" → bmad-stories
✅ "Break down this problem for analysis" → bmad-analyst
```

#### Cas 2: Mot-Clé Dominant

**Problème:** Certains mots-clés sont plus forts.

**Exemple:**
```
Vous: "I have an idea to implement story #5"
Claude: [bmad-analyst activé car "idea" est dominant]
```

**Solution: Inversez l'ordre**
```
✅ "Implement story #5 that we brainstormed" → bmad-dev
```

#### Cas 3: Mauvais Contexte Détecté

**Problème:** Claude se trompe sur le Level.

**Exemple:**
```
Vous: "Fix authentication"
Claude: [bmad-architecture activé → pense Level 3]
```

**Si c'est juste un bug:**
```
✅ "Quick fix for authentication bug" → openspec-propose
```

**Si c'est vraiment complexe:**
```
✅ "Build complete authentication system" → bmad-architecture
```

### Correction en Direct

**Vous pouvez toujours corriger:**
```
Claude: [bmad-analyst activé]
Vous: "No, I meant implement the story, not analyze"
Claude: [Corrige → bmad-dev activé]
```

---

## 🛑 Skill Bloqué

### Symptôme
```
Claude: "Cannot proceed: PRD not found"
[Skill refuse de continuer]
```

### Causes & Solutions

#### Blocage 1: Prérequis Manquants

**Problème:** Essai de sauter une phase.

**Exemple typique:**
```
Vous: "Create architecture"
Claude: "PRD not found. Need PRD first."
```

**Solution: Complétez les prérequis**
```
✅ Vous: "Create PRD first"
   Claude: [bmad-pm activé]
   [Après PRD terminé]
✅ Vous: "Now create architecture"
   Claude: [bmad-architecture activé - ça marche!]
```

**Ordre correct des phases:**
```
1. Idea → bmad-analyst (optionnel Level 3-4)
2. PRD → bmad-pm (obligatoire Level 2-4)
3. UX → bmad-ux (optionnel si UI-heavy)
4. Architecture → bmad-architecture (obligatoire Level 2-4)
5. Stories → bmad-stories
6. Implementation → bmad-dev
```

#### Blocage 2: Artifact Corrompu/Manquant

**Symptôme:**
```
Claude: "workflow-status.md is corrupted"
```

**Solution: Réinitialisation**
```
✅ "Initialize BMAD workflow fresh"
Claude: [Recrée workflow-status.md]
```

**Ou manuellement:**
```bash
rm docs/bmad-workflow-status.md
rm docs/sprint-status.yaml
# Puis recommencez
```

#### Blocage 3: Tests Échouent

**Symptôme:**
```
Claude: "Tests failing, cannot mark complete"
```

**C'est une FEATURE, pas un bug!**

bmad-dev refuse de continuer si tests échouent.

**Solutions:**
1. **Débugger les tests:**
   ```
   Vous: "Show me the test errors"
   Claude: [Affiche les erreurs]
   Vous: "Fix the failing test"
   Claude: [Fixe et relance]
   ```

2. **Si tests corrects mais échec:**
   ```
   Vous: "The test expectation is wrong, update it"
   Claude: [Met à jour le test]
   ```

3. **JAMAIS:** "Skip the tests" ← bmad-dev refusera!

---

## 🧪 Problèmes de Tests

### Symptôme 1: Tests ne Runs Pas

**Cause:** Framework de test pas initialisé.

**Solution:**
```
Vous: "Set up test framework"
Claude: [bmad-tea activé] "I'll set up testing..."
```

### Symptôme 2: Tests Toujours Échouent

**Diagnostic:**
```
Vous: "Run tests verbose"
Claude: [Affiche détails des erreurs]
```

**Solutions courantes:**
- Import manquant → Ajoutez l'import
- Chemin incorrect → Corrigez les paths
- Mock manquant → Ajoutez les mocks
- Async non awaité → Ajoutez await

### Symptôme 3: Tests Lents

**Si >30s pour tests unitaires:**
```
Vous: "Optimize tests, they're too slow"
Claude: [bmad-tea] "I'll parallelize/mock dependencies..."
```

---

## 📁 Artifacts Manquants

### Symptôme
```
Vous: "Continue with architecture"
Claude: "PRD.md not found in docs/"
```

### Vérification Rapide

**Où chercher:**
```bash
# BMAD artifacts
docs/
  ├── brainstorm-notes.md
  ├── PRD.md
  ├── epics.md
  ├── ARCHITECTURE.md
  ├── workflow-status.md
  └── sprint-status.yaml

# Stories
stories/
  └── epic-1-story-1.md

# OpenSpec
openspec/changes/
  └── fix-123/
      ├── proposal.md
      ├── tasks.md
      └── execution-log.md
```

### Solutions

#### Cas 1: Fichier Vraiment Absent

**Recréez-le:**
```
Vous: "Create the missing PRD"
Claude: [bmad-pm activé] "I'll create the PRD..."
```

#### Cas 2: Mauvais Emplacement

**Déplacez-le:**
```bash
# Si PRD est ailleurs
mv /path/to/PRD.md docs/PRD.md
```

#### Cas 3: Nom Incorrect

**BMAD attend des noms spécifiques:**
- ✅ `PRD.md` (pas "prd.md" ou "requirements.md")
- ✅ `ARCHITECTURE.md` (pas "arch.md")
- ✅ `epics.md` (pas "epics-list.md")

**Renommez si nécessaire.**

---

## 🔀 Phases Sautées

### Symptôme
```
Vous avez: Idée → directement Architecture
Claude: "PRD missing, cannot create architecture"
```

### Comprendre les Phases Obligatoires

**Level 0-1 (OpenSpec):**
```
propose → implement → archive
Tout est obligatoire!
```

**Level 2-4 (BMAD):**
```
Analysis  → Planning → Solutioning → Implementation
[optionnel] [REQUIRED] [REQUIRED]   [REQUIRED]
```

**Phases OBLIGATOIRES:**
- Planning (PRD + Epics)
- Solutioning (Architecture)
- Implementation (Stories + Code)

**Phases OPTIONNELLES:**
- Analysis (mais recommandé pour Level 3-4)
- UX (si UI-heavy)
- Testing Strategy (si projet complexe)

### Solution: Retour en Arrière

**Vous pouvez toujours revenir:**
```
Vous: "Go back and create the PRD"
Claude: [bmad-pm activé]
```

**Ou check status:**
```
Vous: "What am I missing?"
Claude: "You need: PRD, Epics, Architecture"
```

---

## 🔄 Confusion OpenSpec vs BMAD

### Symptôme
```
Vous: "Fix button color"
Claude: [Active bmad-pm au lieu de openspec]
```

### Règles de Routing

#### OpenSpec (Level 0-1) = Léger
- Un seul fichier changé
- Pas d'architecture change
- <2 heures de travail
- Codebase existant
- Pas de discovery needed

**Mots-clés OpenSpec:** bug, fix, small, quick, simple, minor

#### BMAD (Level 2-4) = Complexe
- Multiples fichiers
- Architecture needed
- >1 jour de travail
- Peut-être greenfield
- Discovery nécessaire

**Mots-clés BMAD:** build, create, new, architecture, system, product

### Forcer le Bon Workflow

**Pour OpenSpec:**
```
✅ "Quick OpenSpec fix for button color"
✅ "Small change, use OpenSpec"
```

**Pour BMAD:**
```
✅ "This needs full BMAD workflow"
✅ "Complex feature, use BMAD"
```

### Escalade OpenSpec → BMAD

**Si scope grandit en cours:**
```
Claude: "This is becoming complex (>Level 1).
         Escalate to BMAD?"
Vous: "Yes"
Claude: [Passe de OpenSpec à BMAD]
```

---

## 🔧 Problèmes Techniques

### Problème 1: Scripts Python Échouent

**Symptôme:**
```
Error running workflow_status.py
```

**Diagnostic:**
```bash
python --version  # Need Python 3.7+
pip install pyyaml  # Need dependencies
```

**Solution:**
```bash
# Install requirements
pip install -r requirements.txt  # Si existe
# Ou manuellement
pip install pyyaml jinja2
```

### Problème 2: Permissions

**Symptôme:**
```
Permission denied: docs/PRD.md
```

**Solution:**
```bash
chmod -R u+w docs/
chmod -R u+w stories/
chmod -R u+w openspec/
```

### Problème 3: Git Conflicts

**Symptôme:**
```
Conflict in docs/workflow-status.md
```

**Solution:**
```bash
# Keep yours
git checkout --ours docs/workflow-status.md

# Or regenerate
rm docs/workflow-status.md
# Then: "Initialize workflow"
```

---

## 📊 Utiliser les Métriques pour Débugger

### Voir les Activations Récentes

```bash
python shared/tooling/activation_metrics.py recent 20
```

**Analysez:**
- Quel skill a été activé?
- Quel était le trigger?
- Confidence score?
- Success ou échec?

### Identifier les Patterns

```bash
python shared/tooling/activation_metrics.py analyze
```

**Cherchez:**
- Skills avec beaucoup d'échecs
- Triggers à faible confidence
- Patterns d'activation anormaux

### Export Rapport Complet

```bash
python shared/tooling/activation_metrics.py export
```

**Génère:** `docs/activation-report.md` avec:
- Stats détaillées
- Patterns identifiés
- Recommandations d'amélioration

---

## 🆘 Quand Tout Échoue

### Reset Complet

**⚠️ Attention: Perd l'historique!**

```bash
# Backup d'abord!
cp -r docs docs.backup

# Reset BMAD
rm docs/bmad-workflow-status.md
rm docs/sprint-status.yaml

# Reset OpenSpec
rm -rf openspec/changes/*

# Reset Métriques
python shared/tooling/activation_metrics.py clear
```

**Puis recommencez:**
```
Vous: "Initialize BMAD workflow fresh"
Claude: [Repart de zéro]
```

### Support

**Si toujours bloqué:**

1. **Consultez les logs:**
   ```bash
   python shared/tooling/activation_metrics.py recent 50
   ```

2. **Exportez un rapport:**
   ```bash
   python shared/tooling/activation_metrics.py export
   ```

3. **Créez une issue avec:**
   - Phrase exacte utilisée
   - Skill attendu vs activé
   - Logs/métriques
   - État actuel (workflow-status.md)

---

## ✅ Checklist de Validation

Après résolution, vérifiez:

- [ ] Skill correct s'active avec phrase naturelle
- [ ] Prérequis tous présents
- [ ] Artifacts générés au bon endroit
- [ ] Tests passent si applicable
- [ ] Métriques montrent succès
- [ ] Pas de messages d'erreur
- [ ] Peut continuer au skill suivant

**Si toutes les cases cochées: Problème résolu! ✅**

---

## 📚 Ressources Additionnelles

- **FAQ:** [activation-faq.md](activation-faq.md)
- **Quickstart:** [quickstart-conversational.md](quickstart-conversational.md)
- **Flow Examples:** [conversational-flow.md](conversational-flow.md)
- **Tests:** [../tests/test_skill_activation.md](../tests/test_skill_activation.md)

---

**Problème non résolu? Ouvrez une issue avec les détails ci-dessus!**

**Version:** 1.0.0 | **Dernière mise à jour:** 2025-10-29
