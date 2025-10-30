# Quick Start : Tests E2E avec Validation Manuelle

## 🎯 Ce Que Vous Avez Maintenant

Un système de tests E2E qui :
1. ✅ Appelle **réellement** `claude` CLI
2. ✅ Active **réellement** les skills
3. ✅ Génère **réellement** des fichiers (PRD.md, stories, etc.)
4. ✅ **PAUSE** avant de nettoyer pour que vous puissiez vérifier les fichiers

---

## 💰 Coût : GRATUIT avec Claude Max

Vous avez Claude Max = **0€ de coût API** ✅

---

## 🚀 3 Façons de Lancer les Tests

### Mode 1️⃣ : Standard (Cleanup Automatique)

```bash
npm run test:e2e:smoke
```

- ✅ Rapide (2-3 tests)
- ✅ Cleanup automatique
- ✅ Bon pour CI/CD

**Quand l'utiliser :** Vérification rapide que tout marche

---

### Mode 2️⃣ : Inspection Manuelle ⭐ (RECOMMANDÉ POUR VOUS)

```bash
./tests/e2e/run-with-inspection.sh
```

**Ce qui se passe :**

```
Test: test_prd_creation_workflow
Running... ⏳

✅ Test passed

======================================================================
🔍 PAUSED FOR MANUAL INSPECTION
======================================================================
Test: test_prd_creation_workflow
Workspace: /Users/loic/.claude/skills/_runtime/workspace

Generated files are available for inspection:
  - /Users/loic/.claude/skills/_runtime/workspace/artifacts
  - /Users/loic/.claude/skills/_runtime/workspace/stories
  - docs/

👉 Press ENTER to cleanup and continue, or Ctrl+C to abort...
======================================================================
```

**À ce moment :**
1. 🔍 Ouvrez les fichiers dans VSCode/Terminal
2. ✅ Vérifiez que le PRD est bon
3. ✅ Vérifiez la structure
4. ⏎ **Appuyez sur ENTER** → fichiers supprimés, test suivant
5. 🛑 **Ou Ctrl+C** → fichiers gardés, tests arrêtés

**Exemples :**
```bash
# Tous les tests avec pause
./tests/e2e/run-with-inspection.sh

# Seulement smoke tests avec pause
./tests/e2e/run-with-inspection.sh -m smoke

# Un seul test avec pause
./tests/e2e/run-with-inspection.sh test_bmad_workflows.py::test_prd_creation
```

---

### Mode 3️⃣ : Garder Tout (Pas de Cleanup du Tout)

```bash
./tests/e2e/run-keep-artifacts.sh
```

- ✅ Tous les tests s'exécutent
- ✅ AUCUN cleanup
- ✅ Tous les fichiers restent après
- ✅ Vous nettoyez manuellement quand prêt

**Quand l'utiliser :** Vous voulez tous les fichiers d'un coup pour analyse batch

**Cleanup manuel après :**
```bash
rm -rf .claude/skills/_runtime/workspace/artifacts/*.md
rm -rf .claude/skills/_runtime/workspace/stories/*.md
rm -rf docs/
```

---

## 📂 Où Sont les Fichiers Générés ?

```
.claude/skills/_runtime/workspace/
├── artifacts/
│   ├── PRD.md                    # ← Généré par bmad-product-planning
│   ├── discovery-brief.md        # ← Généré par bmad-discovery-research
│   ├── architecture-decisions.md # ← Généré par bmad-architecture-design
│   └── user-flows.md            # ← Généré par bmad-ux-design
├── stories/
│   ├── story-001.md             # ← Généré par bmad-story-planning
│   └── story-002.md
└── changes/
    └── change-xyz/              # ← Généré par openspec-change-proposal
        ├── proposal.md
        └── tasks.md

docs/  # ← Parfois créé par les skills
├── PRD-TodoApp.md
└── epics-TodoApp.md
```

---

## 🧪 Exemple Complet : Tester la Création de PRD

### Étape 1 : Lancer le test avec inspection

```bash
cd /Users/loic/develop/BMad-Skills
./tests/e2e/run-with-inspection.sh test_bmad_workflows.py::test_prd_creation_workflow
```

### Étape 2 : Test s'exécute

```
[ClaudeClient] Executing: claude -p ...
[ClaudeClient] Response: 5000 chars, $0.00 (free with Max), 45000ms
✅ Test passed
```

### Étape 3 : PAUSE pour inspection

```
🔍 PAUSED FOR MANUAL INSPECTION
Press ENTER to cleanup...
```

### Étape 4 : Vérifier les fichiers

```bash
# Dans un autre terminal
open .claude/skills/_runtime/workspace/artifacts/PRD.md
```

**Vérifier :**
- ✅ Le PRD contient bien "Goals", "Features", etc.
- ✅ Le contenu parle bien de "todo app"
- ✅ La structure est correcte
- ✅ Pas de texte générique/placeholder

### Étape 5 : Valider

- ✅ Si bon → **Appuyez ENTER** (fichiers supprimés)
- ❌ Si problème → **Ctrl+C** (fichiers gardés pour debugging)

---

## 🔍 Workflow Typique pour Vous

```bash
# 1. Lancer les smoke tests avec inspection
./tests/e2e/run-with-inspection.sh -m smoke

# 2. Pour chaque test :
#    - Le test génère des fichiers
#    - Vous vérifiez les fichiers
#    - Vous appuyez ENTER si OK
#    - Test suivant démarre

# 3. Si un test produit des fichiers incorrects :
#    - Ctrl+C pour stopper
#    - Inspecter les fichiers
#    - Identifier le problème du skill
#    - Corriger le skill
#    - Relancer
```

---

## 🐛 Debugging

### Test échoue : "Skill not activated"

```bash
# Vérifier que les skills sont installés
ls -la .claude/skills/ | grep bmad

# Vérifier les permissions
cat .claude/skills/bmad-product-planning/SKILL.md | grep allowed-tools
```

### Fichiers pas générés

```bash
# Lancer en mode keep pour voir tous les fichiers
./tests/e2e/run-keep-artifacts.sh -m smoke

# Ensuite inspecter
ls -la .claude/skills/_runtime/workspace/artifacts/
```

### Test trop lent

```bash
# Normal : Claude peut prendre 30-60 secondes par réponse
# Avec skills activés : peut aller jusqu'à 2-3 minutes
```

---

## 📊 Ce Qui Est Testé

### Tests BMAD (test_bmad_workflows.py)
1. ✅ `test_new_idea_activates_discovery` - Idée → Discovery
2. ✅ `test_prd_creation_workflow` - Idée → PRD
3. ✅ `test_full_bmad_workflow` - Discovery → Planning → Architecture → Stories
4. ✅ `test_orchestrator_routing` - Workflow status

### Tests OpenSpec (test_openspec_workflows.py)
1. ✅ `test_bug_fix_activates_proposal` - Bug → Proposal
2. ✅ `test_openspec_proposal_to_implementation` - Proposal → Implementation
3. ✅ `test_complete_openspec_cycle` - Propose → Implement → Archive
4. ✅ `test_small_feature_uses_openspec` - Small feature → OpenSpec (not BMAD)

### Tests Transitions (test_skill_transitions.py)
1. ✅ `test_discovery_to_planning_transition` - Context maintenu
2. ✅ `test_planning_to_architecture_transition` - Handoff propre
3. ✅ `test_architecture_to_stories_transition` - Références correctes
4. ✅ `test_multi_skill_workflow_coherence` - Thème maintenu

---

## ✅ Checklist Avant de Lancer

- [ ] Skills installés : `ls .claude/skills/ | grep bmad`
- [ ] Python deps : `pip install -r requirements.txt`
- [ ] Claude CLI marche : `claude --version`
- [ ] Claude Max actif : `claude` (doit pas demander API key)

---

## 🚀 Commande Recommandée pour Vous

```bash
./tests/e2e/run-with-inspection.sh -m smoke -v
```

**Pourquoi :**
- `-m smoke` = Seulement 2-3 tests rapides
- `-v` = Verbose (voir tout)
- Pause après chaque test
- Gratuit avec Claude Max
- Vous voyez exactement ce que les skills génèrent

---

**Prêt à tester ?** Lancez :
```bash
./tests/e2e/run-with-inspection.sh -m smoke
```

Et vérifiez les fichiers générés manuellement ! 🎉
