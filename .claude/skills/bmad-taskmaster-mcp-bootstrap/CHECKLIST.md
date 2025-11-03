# TaskMaster MCP Bootstrap Checklist

Run this checklist before declaring the setup complete. Every item must be answered "Yes" (or N/A where noted) with evidence in the session notes.

---

## Environment & Prerequisites

- [ ] Node.js ≥ 18.x available (`node -v`).
- [ ] npm ≥ 9.x available (`npm -v`).
- [ ] git ≥ 2.40 available (`git --version`).
- [ ] Target data directory for `TASK_MASTER_DATA_DIR` exists and is writable.
- [ ] Required API keys gathered (Anthropic and any others requested by operator).

## Installation

- [ ] Installation mode documented (`npx` or git clone path).
- [ ] TaskMaster package reachable (version captured from `--version` or git commit hash recorded).
- [ ] Dependencies installed successfully (`npm install` exit 0 or `npx` run with no errors).
- [ ] If using helper script, execution log captured or summarized.

## Configuration

- [ ] `.env` file or MCP `env` block created with placeholders replaced by operator-provided values.
- [ ] `TASK_MASTER_TOOLS` option confirmed (all/standard/core/custom list).
- [ ] `TASK_MASTER_DATA_DIR` points to the intended repository or shared folder.
- [ ] Sensitive files protected (permissions or storage guidance given).

## Validation

- [ ] `task-master-ai status` executed with expected tools listed.
- [ ] `task-master-ai board --format markdown` (or equivalent) succeeds against the chosen data directory.
- [ ] Any warnings (missing keys, disabled tools) acknowledged or resolved.
- [ ] Start/stop instructions provided for the deployment target.

## Hook Integration

- [ ] Hook 1 (save updates) plan documented (e.g., Git commit automation details or TODO recorded).
- [ ] Hook 2 (session start) plan documented (how latest `tasks.md` is loaded).
- [ ] Optional Hook 3 (scheduled sync/reporting) addressed (configured or explicitly deferred).

## Handover

- [ ] Operator received summary with version, locations, and commands.
- [ ] Follow-up actions or open questions captured.
- [ ] Troubleshooting references shared.

Only mark the skill complete after every applicable item is satisfied.
