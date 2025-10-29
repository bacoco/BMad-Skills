# Rapport d'audit du code – BMAD Skills

**Date :** 2024-11-25  
**Auditeur :** ChatGPT (gpt-5-codex)

## 0. Résumé exécutif
- **Score global estimé : 88/100** – l'architecture et la documentation restent exemplaires, mais quelques incohérences de métadonnées et l'absence de tests automatisés empêchent la validation "production ready".
- **Points forts :**
  - Les skills BMAD majeurs exposent désormais des déclencheurs conversationnels détaillés dans `SKILL.md`, ce qui facilite l'auto-activation contextuelle.【F:.claude/skills/bmad-analyst/SKILL.md†L1-L37】
  - Les guides conversationnels illustrent clairement le flow cible et soutiennent la méthode Bimath.【F:doc/conversational-flow.md†L1-L79】
- **Top 3 actions correctives :**
  1. Corriger la métadonnée de `skill-creator` (frontmatter incomplet et absence de section `## When to Invoke`).
  2. Harmoniser les listes `allowed-tools` entre `SKILL.md` et `meta/MANIFEST.json` (écart sur `bmad-analyst`).
  3. Remplacer la checklist manuelle `tests/test_skill_activation.md` par des tests automatisés qui valident les déclencheurs d'activation.

## 1. Forces principales
### 1.1 Activation conversationnelle maîtrisée
Les skills BMAD de phase cœur (analyst, PM, UX, etc.) publient des sections "When to Invoke" riches en mots-clés et scénarios négatifs, garantissant une orchestration fiable sans commandes slash.【F:.claude/skills/bmad-analyst/SKILL.md†L10-L37】【F:.claude/skills/bmad-pm/SKILL.md†L10-L33】

### 1.2 Expérience utilisateur documentée
`doc/conversational-flow.md` décrit des conversations complètes de bout en bout, montrant comment les triggers se chaînent automatiquement d'un skill à l'autre.【F:doc/conversational-flow.md†L7-L78】

### 1.3 Tooling de packaging et de linting
Les scripts de `shared/tooling/` (lint, packaging, métriques) donnent une base solide pour industrialiser la publication des skills.【F:shared/tooling/lint_contracts.py†L1-L30】【F:.claude/skills/skill-creator/scripts/package_skill.py†L1-L87】

## 2. Constats critiques (priorité haute)
### 2.1 `skill-creator` : métadonnées et déclencheurs incomplets
- **Problème :** La frontmatter omet le champ `version`, n'expose pas de section `## When to Invoke` et ne décrit pas les phrases déclenchantes, ce qui bloque l'auto-activation et viole le style guide.【F:.claude/skills/skill-creator/SKILL.md†L1-L27】
- **Impact :** Claude ne peut pas invoquer automatiquement ce skill stratégique ; la gouvernance de versions devient fragile.
- **Action recommandée :**
  - Ajouter `version: 1.x.x`, une section `## When to Invoke` avec triggers et contre-exemples, et aligner les mots-clés de la description avec le manifest.

### 2.2 Incohérence `allowed-tools` entre manifest et skill
- **Problème :** `bmad-analyst/SKILL.md` déclare seulement `Read` et `Write`, alors que `meta/MANIFEST.json` inclut également `Grep` et `Bash` pour le même skill.【F:.claude/skills/bmad-analyst/SKILL.md†L1-L6】【F:meta/MANIFEST.json†L17-L27】
- **Impact :** Risque d'échec à l'exécution si la plateforme applique strictement la liste du manifest ou du skill, et signal faible pour l'audit de moindre privilège.
- **Action recommandée :** Synchroniser les deux sources (idéalement restreindre le manifest à `Read`/`Write` ou étendre le frontmatter si les outils supplémentaires sont réellement nécessaires).

### 2.3 Tests d'activation non automatisés
- **Problème :** `tests/test_skill_activation.md` n'est qu'une checklist à cocher manuellement ; aucune validation programmatique ne vérifie les déclencheurs ou la cohérence des métadonnées.【F:tests/test_skill_activation.md†L1-L44】
- **Impact :** Les régressions d'activation ne seront pas détectées lors d'une intégration continue.
- **Action recommandée :** Créer un script (ex. Python) qui parcourt les `SKILL.md`, extrait les sections `When to Invoke` et vérifie les correspondances avec `meta/MANIFEST.json`. L'intégrer au pipeline CI avec des cas de conversation simulés.

## 3. Améliorations secondaires (priorité moyenne)
1. **Traçabilité des métriques d'activation :** `shared/tooling/activation_metrics.py` définit un collecteur, mais aucun script ne l'orches tre au runtime ; prévoir un hook dans l'orchestrateur pour alimenter ces métriques automatiquement.【F:shared/tooling/activation_metrics.py†L1-L102】
2. **Qualité documentaire future :** Mettre à jour `doc/changelog.md` avec une section "Validation" décrivant les tests passés pour chaque release afin de renforcer la preuve de conformité.【F:doc/changelog.md†L1-L20】
3. **Convergence style guide :** Ajouter dans `meta/STYLE-GUIDE.md` une règle explicite sur la présence obligatoire de `## When to Invoke` dans chaque `SKILL.md` pour prévenir les oublis futurs.【F:meta/STYLE-GUIDE.md†L1-L10】

## 4. Plan d'action proposé
| Priorité | Action | Responsable | Échéance suggérée |
|----------|--------|-------------|-------------------|
| Haute | Mettre à jour `skill-creator/SKILL.md` (version + triggers + description) | Équipe Skills Platform | 2024-11-29 |
| Haute | Aligner `allowed-tools` entre `meta/MANIFEST.json` et les frontmatters | Équipe Skills Platform | 2024-11-29 |
| Haute | Livrer un test automatisé d'activation | Équipe Tooling | 2024-12-06 |
| Moyenne | Instrumenter `activation_metrics.py` dans l'orchestrateur | Équipe Tooling | 2024-12-13 |
| Moyenne | Étendre le style guide et la doc de release | Équipe Documentation | 2024-12-13 |

## 5. Conclusion
Le repository démontre une maîtrise claire de l'architecture Duclos/BMAD et une excellente documentation conversationnelle. Les corrections ciblées sur `skill-creator`, la cohérence des métadonnées et l'automatisation des tests permettront d'atteindre la maturité "production ready" et de fiabiliser la détection de régressions lors des prochaines évolutions.
