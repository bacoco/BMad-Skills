# Workflow — Security Review

This workflow guides the skill from scoping through remediation planning. Follow steps sequentially unless noted.

1. **Intake & Scoping**
   - Clarify objectives: certification, launch readiness, targeted review, or incident response.
   - Identify critical assets, data classifications, and user roles.
   - Collect existing documentation (architecture diagrams, PRDs, compliance matrices).

2. **Context Deep Dive**
   - Map system components and integrations into a current data flow diagram.
   - Inventory authentication, authorization, secrets, and key management approaches.
   - Review infrastructure as code, deployment pipelines, and runtime configurations.

3. **Threat Modeling Workshop**
   - Enumerate trust boundaries and attack surfaces.
   - Apply STRIDE/LINDDUN heuristics to each component.
   - Record threats, impact, likelihood, mitigations, and detection mechanisms.

4. **Vulnerability Analysis**
   - Inspect dependency manifests (package.json, requirements.txt, SBOMs) for known CVEs.
   - Evaluate infrastructure hardening (network rules, patches, encryption, logging).
   - Cross-check findings against OWASP Top 10, ASVS, and relevant compliance controls.

5. **Remediation Backlog Creation**
   - Translate findings into actionable stories with acceptance criteria and owner.
   - Sequence work by severity and effort, noting quick wins vs. long-term initiatives.
   - Define verification approach (automated tests, manual penetration tests, policy updates).

6. **Review & Sign-off**
   - Summarize results in executive-friendly report with residual risk matrix.
   - Recommend go/no-go or conditional release with follow-up tasks.
   - Sync with orchestrator so roadmap and story planning reflect security obligations.

## Supporting Resources
- Templates in `assets/` for threat modeling, risk register, and remediation backlog.
- Security reference links in `REFERENCE.md` for common standards.
