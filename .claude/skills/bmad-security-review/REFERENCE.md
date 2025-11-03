# Reference — Security Review

Quick-access resources for running comprehensive security assessments.

## Core Frameworks
- **OWASP ASVS v4.0.3** — Application security verification requirements.
- **OWASP Top 10 2021** — Common web application risks.
- **NIST SP 800-53 Rev. 5** — Security and privacy controls for information systems.
- **ISO 27001 Annex A** — Control catalogue for information security management.
- **STRIDE/LINDDUN** — Threat modeling heuristics for security and privacy.

## Templates & Artifacts
- `assets/threat-model-canvas.md.template`
- `assets/security-gap-report.md.template`
- `assets/remediation-backlog.csv.template`
- `assets/compliance-matrix.md.template`

## Conversation Prompts
- "Walk me through how data moves between services."
- "What are the authentication and authorization paths?"
- "Where are secrets stored, rotated, and audited?"
- "Which third parties have access to production data?"
- "What happens when a dependency vulnerability is disclosed?"

## Common Pitfalls
- Assuming staging/test environments mimic production hardening.
- Missing logging for security-relevant events (auth failures, policy changes).
- Treating vulnerability scans as complete coverage without threat modeling.
- Neglecting privacy-by-design when handling personal data.
- Postponing remediation until after launch with no accountability owner.

## Escalation Triggers
- Critical/High findings without immediate mitigation path.
- Absence of IAM or least-privilege enforcement.
- Data at rest/in transit lacks encryption or key rotation.
- No incident response process documented or tested.
- Legal/compliance obligations unmet (GDPR DSR, HIPAA logging, PCI DSS segmentation).
