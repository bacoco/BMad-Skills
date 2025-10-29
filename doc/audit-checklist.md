# BMAD Skills Repository Audit Checklist

This checklist is designed for an automated static auditor that validates the Duclos-style Claude Skill conversion of BMAD. Each block describes the objective, concrete automated checks, and failure signals that must be emitted when the checks do not pass.

## 1. Structure globale du repo
**Objectif**
: Vérifier que l'architecture Duclos est respectée à la racine du dépôt.

**Vérifications automatiques**
- La racine contient au minimum `skills/`, `shared/`, `meta/`, `README.md`, et `openspec/` pour l'espace de travail runtime.
- Aucun répertoire legacy de type `agents/`, `workflows/`, `playbooks/`, ni fichier `*.workflow.yaml` ou équivalent n'est présent.

**Échec si**
- Un dossier clé est absent.
- Des artefacts legacy BMAD subsistent.

## 2. Structure interne de chaque skill
**Objectif**
: Garantir qu'un skill est un paquet autonome conforme aux conventions.

**Vérifications automatiques**
- Pour chaque dossier direct dans `skills/` :
  - `SKILL.md`, `REFERENCE.md`, `CHECKLIST.md` sont présents.
  - `WORKFLOW.md` est présent, sauf si le skill est strictement atomique (aucune orchestration multi-étapes mentionnée).
  - Les dossiers `assets/` et `scripts/` existent, même vides.

**Échec si**
- Un de ces fichiers ou dossiers manque.
- `WORKFLOW.md` est absent alors que le skill décrit plusieurs phases ou handoffs.

## 3. Frontmatter de `SKILL.md`
**Objectif**
: S'assurer que chaque skill est directement exploitable par Claude.

**Vérifications automatiques**
- Le fichier débute par un frontmatter YAML encadré par `---`.
- Le frontmatter contient `name`, `description`, `version` (semver), `allowed-tools` (liste non vide). Le champ `name` correspond au dossier du skill.
- Les sections suivantes existent après le frontmatter : `Mission`, `Inputs Required`, `Output`, `Process`, `Quality Gates`, `Error Handling` (ou équivalents proches).
- La section `Output` mentionne explicitement au moins un template dans `assets/`.
- La section `Process` est structurée en étapes numérotées.

**Échec si**
- Clé manquante dans le frontmatter ou champ vide.
- Sections obligatoires absentes ou non structurées.
- `Output` ne référence aucun asset.

## 4. Progressive disclosure et séparation des responsabilités
**Objectif**
: Vérifier que le savoir n'est pas concentré dans `SKILL.md`.

**Vérifications automatiques**
- `SKILL.md` ne contient pas de pavés encyclopédiques (> 500 mots continus) ni de persona legacy.
- `CHECKLIST.md` contient des cases à cocher concrètes et est citée dans `SKILL.md`.
- `WORKFLOW.md` décrit les étapes/handoffs (mots-clés `Step 1`, `Step 2`, etc.).
- `REFERENCE.md` contient du contexte substantiel (guidelines, lexique, heuristiques) et n'est pas vide.

**Échec si**
- `SKILL.md` conserve les monologues des anciens agents.
- `CHECKLIST.md` ou `REFERENCE.md` sont vides.
- `WORKFLOW.md` manque alors que le skill implique plusieurs phases.

## 5. Dossiers `assets/`
**Objectif**
: Confirmer que chaque livrable annoncé dispose d'un template concret.

**Vérifications automatiques**
- Chaque skill possède au moins un fichier de template (`.md`, `.json`, etc.) dans `assets/` correspondant aux livrables décrits.
- Aucun template n'est laissé en `TODO` ou vide.
- Les noms de fichiers mentionnés dans `SKILL.md` existent réellement.

**Échec si**
- Livrable annoncé sans template.
- Templates vides ou placeholders.

## 6. Dossiers `scripts/`
**Objectif**
: Valider l'existence et la cohérence des scripts d'appui.

**Vérifications automatiques**
- Chaque script porte un nom descriptif aligné avec le livrable.
- Les scripts contiennent du code non trivial et n'utilisent pas de chemins absolus.
- `SKILL.md` explique si et comment ces scripts sont invoqués.

**Échec si**
- `scripts/` vide sans justification alors que des artefacts sont promis.
- Script vide, placeholder ou utilisant des chemins absolus.

## 7. Cohérence de `meta/MANIFEST.json`
**Objectif**
: Garantir l'alignement entre la vision machine et les dossiers réels.

**Vérifications automatiques**
- `meta/MANIFEST.json` est valide et référence chaque skill présent dans `skills/`.
- Pour chaque entrée : `id`, `version`, `allowed-tools`, `path` correspondent au frontmatter du `SKILL.md` associé et au chemin réel.

**Échec si**
- Skill manquant dans le manifest ou entrée pointant vers un chemin inexistant.
- Divergence entre manifest et frontmatter.

## 8. Guides de style et versioning
**Objectif**
: S'assurer que la gouvernance documentaire est en place.

**Vérifications automatiques**
- `meta/STYLE-GUIDE.md` existe et décrit les conventions de nommage, la rédaction de `description`, et la séparation des fichiers du skill.
- `meta/VERSIONING.md` existe et explique la politique de mise à jour des champs `version`.

**Échec si**
- Un de ces documents est manquant ou ne couvre pas les points requis.

## 9. Résidus de packs d'expansion
**Objectif**
: Garantir qu'aucun ancien dossier `expansion/` ne subsiste après la fusion des skills.

**Vérifications automatiques**
- Confirmer l'absence de répertoires `expansion/` ou équivalents à la racine.
- Signaler toute tentative de re-ségrégation des skills par pack.

**Échec si**
- Un dossier `expansion/` est présent ou contient des artefacts.

## 10. Couverture fonctionnelle BMAD
**Objectif**
: Confirmer que les piliers métier BMAD sont présents.

**Vérifications automatiques**
- Existence d'un skill qui produit un PRD/spec produit.
- Existence d'un skill couvrant l'architecture technique et les risques.
- Existence d'un skill traitant la préparation du backlog / user stories.
- Présence d'au moins un document (`SKILL.md` ou `WORKFLOW.md`) évoquant explicitement la préservation/transfert de contexte entre ces phases.

**Échec si**
- Une de ces briques est absente.
- La notion de transfert de contexte inter-phases n'est mentionnée nulle part.

## 11. Présence et intégration d'OpenSpec
**Objectif**
: Vérifier que le workflow OpenSpec est bien intégré comme famille de skills Claude et non simplement copié en l'état.

**Vérifications automatiques**
- Confirmer l'existence de skills OpenSpec (ex. `skills/openspec-propose/`, `skills/openspec-implement/`, `skills/openspec-archive/`) ou d'un sous-arbre dédié qui expose ces capacités via des `SKILL.md` conformes.
- S'assurer qu'OpenSpec n'est pas présent uniquement sous forme de code brut importé sans conversion en skills.

**Échec si**
- Aucune référence à OpenSpec n'apparaît dans le repo final.
- OpenSpec est simplement vendorié sans transformation en skills (absence de `SKILL.md`, `REFERENCE.md`, etc.).

## 12. Qualité des skills OpenSpec
**Objectif**
: S'assurer que chaque skill OpenSpec respecte exactement les mêmes conventions Duclos que les skills BMAD.

**Vérifications automatiques**
- Chaque skill OpenSpec possède `SKILL.md`, `REFERENCE.md`, `WORKFLOW.md`, `CHECKLIST.md`, `assets/`, `scripts/`.
- `SKILL.md` inclut un frontmatter complet (`name`, `description` ciblée sur Proposal/Apply/Archive, `version`, `allowed-tools` minimal) et les sections `Mission`, `Inputs Required`, `Output`, `Process`, `Quality Gates`, `Error Handling`.
- La section `Output` détaille précisément les artefacts OpenSpec attendus (`openspec/changes/<id>/proposal.md`, `tasks.md`, `design.md`, deltas de specs, etc.).
- La section `Process` déroule les étapes officielles Proposal → Apply → Archive sous forme numérotée.
- `REFERENCE.md` expose la philosophie et les règles OpenSpec (raison d'être, conventions de `change-id`, contenu des fichiers, spec-driven dev sans API).
- `WORKFLOW.md` décrit explicitement les trois étapes séquentielles et le rôle de la validation humaine.
- `CHECKLIST.md` contient les validations obligatoires avant d'exécuter l'étape suivante (naming, clarté du scope, tâches prêtes, scénarios dans les deltas de spec, alignement obtenu).
- Les templates OpenSpec existent dans `assets/` (ex. `proposal-template.md`, `tasks-template.md`, `spec-delta-template.md`) et ne sont pas vides.
- Les scripts OpenSpec (scaffolding, archivage, etc.) utilisent des chemins relatifs vers `openspec/...` et contiennent du code fonctionnel.

**Échec si**
- Un des fichiers structurants manque ou est vide.
- Le frontmatter autorise des outils non pertinents (ex. `WebSearch`) ou ne décrit pas le livrable attendu.
- Aucun template n'est fourni ou les scripts sont des placeholders.

## 13. Séparation d'usage BMAD vs OpenSpec
**Objectif**
: Clarifier quand utiliser les skills BMAD (cadrage lourd) versus OpenSpec (itérations ciblées specs-first).

**Vérifications automatiques**
- `README.md`, `meta/STYLE-GUIDE.md` ou une autre documentation racine doit expliciter la différence d'usage : BMAD pour les cycles produit/architecture/backlog complets, OpenSpec pour les changements incrémentaux spéciaux.
- Les descriptions des skills OpenSpec restent focalisées sur Proposal/Apply/Archive et ne prétendent pas couvrir le périmètre BMAD complet.

**Échec si**
- Aucune doc ne décrit la frontière d'usage entre les deux familles de skills.
- Les skills OpenSpec revendiquent des missions identiques à celles de BMAD (PRD complet, architecture globale, etc.).

## 14. MANIFEST.json et OpenSpec
**Objectif**
: Vérifier que le manifest machine-readable référence également les skills OpenSpec.

**Vérifications automatiques**
- `meta/MANIFEST.json` contient une entrée pour chaque skill OpenSpec avec `id`, `path`, `version`, `allowed-tools` alignés avec le frontmatter.
- Aucun skill OpenSpec n'est omis du manifest et aucune entrée ne pointe vers un chemin inexistant.

**Échec si**
- Les skills OpenSpec sont absents ou incohérents dans `MANIFEST.json`.

## 15. Préparation runtime d'OpenSpec
**Objectif**
: Valider que le repo fournit l'arborescence et les scripts nécessaires pour exécuter OpenSpec (Proposal → Apply → Archive) en local.

**Vérifications automatiques**
- Présence d'un dossier `openspec/` structuré avec au minimum `openspec/changes/` et `openspec/specs/` (ou équivalent documenté).
- Les scripts OpenSpec utilisent cette arborescence pour générer ou archiver les artefacts (`openspec/changes/<change-id>/proposal.md`, etc.).
- Le contenu des anciens `AGENTS.md` OpenSpec (règles TL;DR, checklists, conventions de `change-id`) est repris dans `REFERENCE.md` ou `CHECKLIST.md` des skills OpenSpec.

**Échec si**
- L'arborescence runtime `openspec/` est absente ou non documentée.
- Les scripts ne créent/manipulent pas les fichiers attendus.
- Les règles opérationnelles OpenSpec n'ont pas été migrées dans la documentation des skills.

## Format attendu pour le rapport de l'IA
L'IA doit retourner un JSON simple. Chaque bloc utilise une clé stable et fournit `status` (`PASS` ou `FAIL`). En cas d'échec, la valeur `problems` détaille le chemin concerné, la règle violée et une suggestion courte.

```json
{
  "1_repo_structure": {"status": "PASS"},
  "2_skill_layout": {
    "status": "FAIL",
    "problems": [
      {
        "skill": "skills/product-requirements",
        "issue": "Missing CHECKLIST.md",
        "fix": "Add CHECKLIST.md with quality gates and reference it from SKILL.md"
      }
    ]
  },
  "3_frontmatter": {"status": "PASS"},
  "4_progressive_disclosure": {"status": "PASS"},
  "5_assets_consistency": {"status": "FAIL", "problems": [...]},
  "6_scripts_consistency": {"status": "PASS"},
  "7_manifest_consistency": {"status": "PASS"},
  "8_style_versioning": {"status": "PASS"},
  "9_expansion_residue": {"status": "PASS"},
  "10_bmad_coverage": {"status": "PASS"},
  "11_openspec_presence": {"status": "PASS"},
  "12_openspec_skill_quality": {"status": "PASS"},
  "13_bmad_vs_openspec_boundary": {"status": "PASS"},
  "14_manifest_includes_openspec": {"status": "PASS"},
  "15_openspec_runtime_ready": {"status": "PASS"}
}
```

Cette checklist complète peut être fournie telle quelle à un auditeur automatisé pour valider le respect des conventions Duclos-style et la bonne intégration d'OpenSpec dans le dépôt.
