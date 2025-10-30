# Stratégie de Test BMAD Skills

## 🎯 Philosophie

BMAD Skills est un système **conversationnel interactif**. La stratégie de test reflète cette réalité :
- **90% automatisés** : Ce qui est déterministe (structure, metadata, scripts)
- **10% manuels** : Ce qui est conversationnel (workflows, génération artefacts)

---

## ✅ Tests Automatisés

### Tests Statiques (Actuel : 56 tests ✅)

```bash
npm test
```

**Ce qu'on teste :**
- ✅ Metadata YAML valide (frontmatter de SKILL.md)
- ✅ Cohérence allowed-tools (SKILL.md ↔ MANIFEST.json)
- ✅ Templates présents dans assets/
- ✅ Descriptions cohérentes
- ✅ Version alignment (package.json ↔ MANIFEST.json)
- ✅ Structure skills (SKILL.md, REFERENCE.md, WORKFLOW.md, CHECKLIST.md)

**Commandes spécifiques :**
```bash
pytest tests/test_skill_metadata.py       # Metadata validation
pytest tests/test_manifest_consistency.py # Manifest coherence
pytest tests/test_template_assets.py      # Templates present
```

### Tests Unitaires Python (À implémenter)

```bash
pytest tests/unit/
```

**Ce qui doit être testé :**
- [ ] `workflow_status.py` - Lecture/écriture YAML status
- [ ] `sprint_status.py` - Parsing epics → stories
- [ ] `activation_metrics.py` - Collecte métriques
- [ ] Gestion d'erreurs (YAML corrompu, fichiers manquants)

**Priorité P0** selon IMPROVEMENTS.md

---

## 🧪 Tests Manuels Conversationnels

### Pourquoi Manuels ?

**Les workflows BMAD sont conversationnels** : les skills posent des questions, l'utilisateur répond, le contexte s'accumule. **Impossible à automatiser.**

Voir `tests/WHY_NO_E2E_TESTS.md` pour l'explication complète.

### Workflows À Tester Manuellement

#### 1. Workflow BMAD Complet (L2-4)

```bash
claude  # Mode interactif
```

**Scénario :** App de budget pour étudiants

```
> Je veux créer une app de budget pour étudiants

Claude (Discovery): Quels sont les principaux problèmes de vos utilisateurs ?
> Ils oublient leurs dépenses et dépassent leur budget

Claude (Discovery): Quelles features prioritaires ?
> Tracking dépenses, alertes budget, catégories

Claude: Compris. Voulez-vous un PRD ?
> Oui

Claude (PM): [génère PRD.md]
```

**Vérifications :**
- [ ] PRD.md créé dans `.claude/skills/_runtime/workspace/artifacts/`
- [ ] Contient sections : Goals, Features, Metrics, Requirements
- [ ] Contenu pertinent (mentionne étudiants, budget, etc.)
- [ ] Qualité : Complet, cohérent, actionnable

**Continuer avec :**
```
> Design l'architecture technique

Claude (Architect): [génère architecture-decisions.md]
```

**Vérifications :**
- [ ] architecture-decisions.md créé
- [ ] Stack technique défini
- [ ] Composants identifiés
- [ ] Data flow documenté

**Continuer avec :**
```
> Break down en developer stories

Claude (Stories): [génère story-001.md, story-002.md, etc.]
```

**Vérifications :**
- [ ] story-*.md créés dans `.claude/skills/_runtime/workspace/stories/`
- [ ] Chaque story a acceptance criteria
- [ ] Stories couvrent les features du PRD
- [ ] Estimations présentes

**Résultat attendu :** ✅ Workflow complet validé

---

#### 2. Workflow OpenSpec (L0-1)

```
> Fix: Le timeout de session est trop court (15min → 60min)

Claude (OpenSpec Proposal): [génère proposal.md]
```

**Vérifications :**
- [ ] proposal.md créé dans `.claude/skills/_runtime/workspace/changes/`
- [ ] Problem statement clair
- [ ] Solution proposée
- [ ] Tasks.md avec tâches

```
> Implémente ce changement

Claude (OpenSpec Implementation): [génère execution-log.md]
```

**Vérifications :**
- [ ] execution-log.md mis à jour
- [ ] Change implémenté ou documenté
- [ ] Status actualisé

---

### Fréquence Tests Manuels

- **Avant chaque release majeure** : Workflow BMAD complet
- **Avant chaque release mineure** : Workflow OpenSpec
- **Ad-hoc** : Si changement majeur dans un skill

### Documentation Tests Manuels

**Format :**
```markdown
## Test Manuel - [Date]

**Testeur :** [Nom]
**Version :** [X.Y.Z]
**Workflow :** BMAD Complet

### Résultats

- ✅ Discovery → PRD : OK (PRD.md généré, qualité bonne)
- ✅ PRD → Architecture : OK (architecture-decisions.md complet)
- ✅ Architecture → Stories : OK (8 stories générées)
- ❌ Bug découvert : [Description si applicable]

### Artefacts Générés

- PRD.md (1234 bytes)
- architecture-decisions.md (2345 bytes)
- story-001.md → story-008.md

### Conclusion

✅ Workflow validé, fonctionne correctement
```

**Fichier :** `tests/manual/test-results-YYYY-MM-DD.md`

---

## 🚫 Ce Qu'On NE Teste PAS (Et Pourquoi)

### Tests E2E Automatisés ❌

**Pourquoi impossible :**
- Skills sont conversationnels (multi-tours, questions/réponses)
- Mode batch `claude -p` ne permet pas l'interaction
- Pas de mock possible (skills chargés par Claude, pas Python)
- Résultats non-déterministes (LLM)

**Voir :** `tests/WHY_NO_E2E_TESTS.md` pour détails complets

### Tests d'Intégration Skills ❌

**Pourquoi impossible :**
- Transitions entre skills nécessitent conversation
- Context cumulatif pas scriptable
- Handoffs basés sur contenu conversationnel

### Tests de Régression UI ❌

**Pourquoi non applicable :**
- Pas d'UI (CLI conversationnel)
- Interaction textuelle libre
- Pas de "clicks" ou "forms" à tester

---

## 📊 Couverture de Test

### Actuel

| Type | Couverture | Status |
|------|-----------|--------|
| Metadata/Structure | 100% | ✅ 56 tests |
| Scripts Python | 0% | ⚠️ À faire |
| Workflows conversationnels | Manuel | ✅ Validé |

### Cible (Score 100/100)

| Type | Couverture | Status |
|------|-----------|--------|
| Metadata/Structure | 100% | ✅ |
| Scripts Python | 80%+ | 🔜 P0 |
| Workflows conversationnels | Manuel | ✅ |

**Note :** Couverture "tests automatisés" ne peut jamais atteindre 100% pour un système conversationnel. **C'est normal et acceptable.**

---

## 🔄 CI/CD

### GitHub Actions (À implémenter - P0)

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  static-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: pytest tests/ -v  # Tests statiques + unitaires

  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: python3 .claude/skills/_core/tooling/lint_contracts.py
```

**Ce qui est testé en CI :**
- ✅ Tests statiques (metadata, structure)
- ✅ Tests unitaires Python
- ✅ Linting contracts

**Ce qui N'EST PAS testé en CI :**
- ❌ Workflows conversationnels (impossible à automatiser)

---

## 📝 Checklist Avant Release

### Tests Automatisés

- [ ] `npm test` passe (tests statiques)
- [ ] `pytest tests/unit/` passe (tests unitaires)
- [ ] `npm run lint` passe (contracts validation)
- [ ] CI/CD green (si implémenté)

### Tests Manuels

- [ ] Test workflow BMAD complet (voir section ci-dessus)
- [ ] Test workflow OpenSpec (voir section ci-dessus)
- [ ] Résultats documentés dans `tests/manual/`

### Validation Qualité

- [ ] Tous les skills ont SKILL.md, REFERENCE.md, WORKFLOW.md, CHECKLIST.md
- [ ] Templates présents dans assets/
- [ ] Scripts Python ont error handling
- [ ] MANIFEST.json synchronisés (meta/ et _config/)

---

## 🎓 Pour les Nouveaux Contributeurs

### "Pourquoi pas de tests E2E ?"

**Réponse courte :** Impossible, système conversationnel.

**Réponse longue :** Lire `tests/WHY_NO_E2E_TESTS.md`

### "Comment tester mes changements ?"

1. **Si vous modifiez metadata/structure :**
   ```bash
   npm test  # Doit passer
   ```

2. **Si vous modifiez scripts Python :**
   ```bash
   pytest tests/unit/test_[votre_script].py  # Écrire tests d'abord
   ```

3. **Si vous modifiez un skill (SKILL.md, etc.) :**
   ```bash
   # Test manuel conversationnel
   claude  # Mode interactif
   > [Tester le skill manuellement]
   ```

### "Mon PR peut-il être mergé sans tests E2E ?"

**OUI !** Les tests E2E ne sont pas requis (et impossibles).

**Requis :**
- ✅ Tests statiques passent
- ✅ Tests unitaires passent (si code Python modifié)
- ✅ Test manuel effectué (si skill modifié)
- ✅ Résultats documentés

---

## 📚 Références

- **WHY_NO_E2E_TESTS.md** : Explication détaillée impossibilité E2E
- **IMPROVEMENTS.md** : Roadmap avec priorités (tests unitaires P0)
- **tests/manual/** : Résultats des tests manuels conversationnels

---

*Stratégie validée : Oct 2025*
*Workflows testés manuellement et fonctionnent correctement* ✅
