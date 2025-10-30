# BMAD Skills - Improvements Roadmap to 100/100

## Current Score: 85/100

| Domaine | Actuel | Max | Gap |
|---------|--------|-----|-----|
| Architecture & expérience applicative | 22 | 25 | -3 |
| Qualité du code & automatisation | 18 | 20 | -2 |
| Documentation & DX | 19 | 20 | -1 |
| Tests & assurance qualité | 14 | 20 | -6 |
| Sécurité & packaging | 12 | 15 | -3 |

---

## 1. Tests & Assurance Qualité (+6 points : 14 → 20)

### Tests Unitaires Python (+2 points)

- [ ] Créer `tests/unit/test_workflow_status.py`
  - Test `workflow_status.py` initialization
  - Test status updates
  - Test corrupted YAML handling
  - Test file I/O edge cases

- [ ] Créer `tests/unit/test_sprint_status.py`
  - Test `sprint_status.py` initialization from epics
  - Test sprint status updates
  - Test YAML parsing edge cases
  - Test status transitions

- [ ] Créer `tests/unit/test_activation_metrics.py`
  - Test metrics collection
  - Test metrics export
  - Test dashboard generation
  - Test data aggregation

- [ ] Créer `tests/unit/test_cli.py`
  - Test `bin/cli.js` installation logic
  - Test backup creation
  - Test error handling
  - Test path resolution

### E2E Tests Fonctionnels (+2 points)

- [ ] Implémenter tests interactifs avec pexpect
  ```python
  # tests/e2e/test_interactive_activation.py
  - Test skill activation in interactive mode
  - Test multi-turn conversations
  - Test context maintenance
  ```

- [ ] OU créer Mock Claude Client pour tests rapides
  ```python
  # tests/e2e/helpers/mock_claude.py
  - Mock responses for each skill type
  - Fast deterministic testing
  ```

- [ ] Convertir les 8 scénarios manuels de `test_skill_activation.md` en tests automatisés

### CI/CD avec GitHub Actions (+1 point)

- [ ] Créer `.github/workflows/test.yml`
  - Job: static tests (pytest metadata/templates)
  - Job: unit tests (Python)
  - Job: E2E smoke tests (on main branch only)
  - Badge de status dans README

- [ ] Créer `.github/workflows/release.yml`
  - Auto-bump version
  - Run full test suite
  - Create GitHub release
  - Publish to npm

### Coverage Reporting (+1 point)

- [ ] Ajouter `pytest-cov` à requirements.txt
- [ ] Créer npm script `test:coverage`
- [ ] Configurer seuil minimal 80% coverage
- [ ] Ajouter badge coverage dans README
- [ ] Exclure fichiers non-testables du coverage (.template, assets)

---

## 2. Sécurité & Packaging (+3 points : 12 → 15)

### Checksums et Signatures (+1 point)

- [ ] Modifier `scripts/package-bundle.sh`
  - Générer SHA256SUMS après packaging
  - Optionnel: GPG signing des checksums

- [ ] Modifier `scripts/install-to-home.sh`
  - Vérifier checksum avant installation
  - Rejeter si checksum invalide
  - Ajouter flag `--skip-verify` pour dev

- [ ] Documenter processus de vérification dans README

### Rollback Atomique (+1 point)

- [ ] Réécrire `bin/cli.js` fonction `installSkills()`
  - Installer dans `.tmp` d'abord
  - Valider installation complète
  - Backup ancien si existe
  - Rename atomique
  - Rollback automatique en cas d'erreur

- [ ] Ajouter validation post-installation
  - Vérifier MANIFEST.json
  - Vérifier structure directories
  - Vérifier templates présents

- [ ] Logger toutes les étapes pour debugging

### Tests Scripts d'Installation (+1 point)

- [ ] Créer `tests/integration/test_install_scripts.sh`
  - Test `install-to-home.sh` success case
  - Test `install-to-project.sh` success case
  - Test `install-to-custom.sh` avec path custom
  - Test rollback en cas d'échec
  - Test backup/restore existant

- [ ] Créer `tests/integration/test_cli_install.js`
  - Test `npx bmad-skills` installation
  - Test flags `--global`, `--path`
  - Test détection repo BMAD existant

- [ ] Intégrer dans CI/CD pipeline

---

## 3. Qualité du Code & Automatisation (+2 points : 18 → 20)

### Linting et Formatting Automatique (+1 point)

- [ ] Ajouter à `requirements.txt`
  ```
  black>=23.0.0
  pylint>=3.0.0
  mypy>=1.7.0
  ```

- [ ] Créer `.pylintrc` configuration
- [ ] Créer `mypy.ini` configuration
- [ ] Ajouter npm scripts
  ```json
  "format": "black .claude/skills tests",
  "lint:python": "pylint .claude/skills/_core/tooling tests",
  "typecheck:python": "mypy .claude/skills/_core/tooling tests"
  ```

- [ ] Créer pre-commit hook `.git/hooks/pre-commit`
  - Run black formatting
  - Run pylint
  - Block commit si erreurs critiques

- [ ] Formatter tout le code existant

### Logging Structuré (+1 point)

- [ ] Créer `.claude/skills/_core/tooling/logger.py`
  - Setup logging avec niveaux (DEBUG, INFO, WARNING, ERROR)
  - Format uniforme avec timestamps
  - Option verbose mode

- [ ] Remplacer tous les `print()` par logging
  - `quick_validate.py`
  - `activation_metrics.py`
  - `sprint_status.py`
  - `workflow_status.py`

- [ ] Ajouter gestion d'erreurs explicite
  - Pas d'erreurs silencieuses
  - Log stack traces en DEBUG mode
  - Messages d'erreur utilisateur-friendly

- [ ] Ajouter `--verbose` flag à tous les scripts

---

## 4. Architecture & Expérience Applicative (+3 points : 22 → 25)

### Dashboard Métriques d'Activation (+1 point)

- [ ] Étendre `activation_metrics.py`
  - Méthode `export_dashboard(output='html')`
  - Graphiques skill usage over time
  - Success rate par skill
  - Cost tracking par skill
  - Transition patterns visualization

- [ ] Créer template HTML dashboard
  - Utiliser Plotly.js ou Chart.js
  - Graphiques interactifs
  - Export en PNG/PDF

- [ ] Ajouter npm script `metrics:dashboard`
- [ ] Documenter dans CLAUDE.md

### Validation Prérequis Automatique (+1 point)

- [ ] Ajouter section `prerequisites` au YAML frontmatter
  ```yaml
  metadata:
    prerequisites:
      - artifact: "PRD.md"
        location: "artifacts/"
        required: true
      - skill: "bmad-product-planning"
        must_have_run: true
  ```

- [ ] Créer `.claude/skills/_core/tooling/validate_prerequisites.py`
  - Lire prerequisites depuis SKILL.md
  - Vérifier artifacts existent
  - Vérifier skills précédents ont run
  - Retourner warnings/errors

- [ ] Intégrer validation dans workflow-router
  - Checker avant activation skill
  - Avertir utilisateur si prérequis manquants
  - Proposer actions correctives

### Auto-Repair Workspace (+1 point)

- [ ] Créer `scripts/repair-workspace.sh`
  - Détecter YAML invalides → Backup + régénération
  - Détecter fichiers manquants → Créer depuis templates
  - Détecter références cassées → Fix automatique
  - Détecter structures corrompues → Rebuild

- [ ] Créer `scripts/validate-workspace.sh`
  - Check structure directories
  - Check YAML parseable
  - Check templates présents
  - Check permissions correctes

- [ ] Ajouter npm scripts
  ```json
  "workspace:validate": "bash scripts/validate-workspace.sh",
  "workspace:repair": "bash scripts/repair-workspace.sh"
  ```

- [ ] Documenter usage dans troubleshooting

---

## 5. Documentation & DX (+1 point : 19 → 20)

### Guides Visuels (+0.5 point)

- [ ] Créer GIF démo workflow BMAD
  - Enregistrer session complète discovery → PRD → architecture → stories
  - Convertir en GIF optimisé (<5MB)
  - Ajouter dans README.md

- [ ] Créer GIF démo workflow OpenSpec
  - Enregistrer bug fix proposal → implement → archive
  - Ajouter dans README.md

- [ ] Optionnel: Vidéo YouTube tutorial (5-10 min)
  - Walkthrough complet
  - Lien dans README

### Diagnostic Tool (+0.5 point)

- [ ] Créer `bin/doctor.js`
  - Check: Skills installed correctement
  - Check: Workspace structure valide
  - Check: YAML files parseables
  - Check: Templates présents
  - Check: Python dependencies (pytest, pyyaml)
  - Check: Claude CLI disponible
  - Proposer fixes automatiques

- [ ] Ajouter à package.json
  ```json
  "scripts": {
    "doctor": "node bin/doctor.js"
  }
  ```

- [ ] Documenter `npx bmad-skills doctor` dans README
- [ ] Ajouter section "Troubleshooting" référençant doctor

---

## Roadmap Estimée

### Phase 1: Tests Solides (1 semaine) → +8 points (85 → 93)
- Tests unitaires Python
- E2E fonctionnels avec pexpect
- CI/CD GitHub Actions
- Coverage reporting 80%+

### Phase 2: Sécurité (3 jours) → +3 points (93 → 96)
- Checksums + GPG signing
- Rollback atomique
- Tests scripts installation

### Phase 3: Qualité Code (2 jours) → +3 points (96 → 99)
- Linting/formatting automatique
- Logging structuré
- Dashboard métriques

### Phase 4: Polish (1 jour) → +1 point (99 → 100)
- GIF/vidéos démos
- Doctor diagnostic tool
- Auto-repair workspace

**Total estimé: 2-3 semaines pour 100/100**

---

## Priorités Recommandées

### P0 - Critique (nécessaire pour 90+)
- [ ] Tests unitaires Python complets
- [ ] CI/CD GitHub Actions
- [ ] Rollback atomique installation

### P1 - Important (nécessaire pour 95+)
- [ ] E2E tests fonctionnels
- [ ] Coverage 80%+
- [ ] Logging structuré
- [ ] Checksums installation

### P2 - Nice to have (pour 100)
- [ ] Dashboard métriques
- [ ] Validation prérequis
- [ ] Auto-repair workspace
- [ ] Doctor diagnostic tool
- [ ] GIF/vidéos démos

---

**Note:** Ce fichier track les améliorations identifiées lors de l'audit qualité.
Cocher les items au fur et à mesure de l'implémentation.
