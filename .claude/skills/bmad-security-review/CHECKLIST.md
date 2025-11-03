# Security Review Activation Checklist

Use this list before delivering outputs or signaling completion.

## Entry Criteria
- [ ] Architecture decisions and system diagrams reviewed.
- [ ] Authentication, authorization, and data classification details collected.
- [ ] Deployment topology (cloud/service boundaries) understood.
- [ ] Applicable regulations or compliance targets confirmed.

## Threat Modeling
- [ ] Trust boundaries identified and documented.
- [ ] Data flow diagram created or validated.
- [ ] STRIDE/LINDDUN analysis completed with risk scores.
- [ ] External integrations and third-party services assessed.

## Vulnerability Assessment
- [ ] Dependency scan status captured (SCA reports, CVEs, SBOMs).
- [ ] Infrastructure misconfigurations or gaps recorded.
- [ ] Secrets management reviewed (storage, rotation, access controls).
- [ ] Logging and monitoring coverage evaluated for incident response.

## Remediation Plan
- [ ] Findings grouped by severity with evidence.
- [ ] Owners and due dates assigned for each remediation item.
- [ ] Stories or tasks drafted with acceptance criteria for downstream skills.
- [ ] Residual risk and follow-up actions communicated.

## Exit Criteria
- [ ] Threat model, gap assessment, and remediation backlog stored in workspace.
- [ ] Summary shared with orchestrator including go/no-go recommendation.
- [ ] Compliance or audit blockers escalated if unresolved.
