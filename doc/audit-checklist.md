# BMAD Skills Repository Audit Checklist

This checklist is designed for an automated static auditor that validates the Duclos-style Claude Skill conversion of BMAD. Each block describes the objective, concrete automated checks, and failure signals that must be emitted when the checks do not pass.

## 1. Structure globale du repo
**Objectif**
: Vérifier que l'architecture Duclos est respectée à la racine du dépôt.

**Vérifications automatiques**
- La racine contient au minimum `skills/`, `shared/`, `meta/`, `README.md`, et `expansion/` si des packs existaient dans BMAD.
- Aucun répertoire legacy de type `agents/`, `workflows/`, `playbooks/`, ni fichier `*.workflow.yaml` ou équivalent n'est présent.

**Échec si**
- Un dossier clé est absent.
- Des artefacts legacy BMAD subsistent.

## 2. Structure interne de chaque skill
**Objectif**
: Garantir qu'un skill est un paquet autonome conforme aux conventions.

**Vérifications automatiques**
- Pour chaque dossier direct dans `skills/` et `expansion/*/` :
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
- `meta/MANIFEST.json` est valide et référence chaque skill de `skills/` et `expansion/`.
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

## 9. Packs d'expansion
**Objectif**
: Vérifier que les packs facultatifs sont convertis en skills cohérents.

**Vérifications automatiques**
- Si `expansion/` existe, chaque sous-capacité suit la même structure qu'un skill standard.
- Les noms de dossiers décrivent des compétences métiers (ex. `market-analysis`) et non des personas.

**Échec si**
- Restes d'agents personnalisés ou structure non conforme dans les packs.

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

## Format attendu pour le rapport de l'IA
L'IA doit retourner un JSON simple. Chaque bloc utilise une clé stable et fournit `status` (`PASS` ou `FAIL`). En cas d'échec, la valeur `problems` détaille le chemin concerné, la règle violée et une suggestion courte.

```json
{
  "structure_repo": {"status": "PASS"},
  "skill_layout": {
    "status": "FAIL",
    "problems": [
      {
        "skill": "skills/product-requirements",
        "issue": "Missing CHECKLIST.md",
        "fix": "Add CHECKLIST.md with quality gates and reference it from SKILL.md"
      }
    ]
  },
  "frontmatter": {"status": "PASS"},
  "progressive_disclosure": {"status": "PASS"},
  "assets_consistency": {"status": "FAIL", "problems": [...]},
  "scripts_consistency": {"status": "PASS"},
  "manifest_consistency": {"status": "PASS"},
  "style_and_versioning": {"status": "PASS"},
  "expansion_packs": {"status": "PASS"},
  "bmad_coverage": {"status": "PASS"}
}
```

Cette checklist peut être fournie telle quelle à un auditeur automatisé pour valider le respect des conventions Duclos-style du dépôt.
