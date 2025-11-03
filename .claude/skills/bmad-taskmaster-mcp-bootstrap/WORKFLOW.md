# TaskMaster MCP Bootstrap Workflow

Follow this sequence end-to-end. Only skip steps if the operator already completed them in this session and the state is unchanged.

---

## 0. Collect Context

1. Confirm desired deployment target:
   - **Local developer machine** (most common).
   - **Shared server/VM** (needs SSH access, systemd, reverse proxy decisions).
2. Identify editor(s) that will connect to TaskMaster (Cursor, Claude Code CLI, VS Code, etc.).
3. Gather secret sources (Anthropic, OpenAI, Perplexity, etc.) and decide which tools must be enabled.
4. Locate or create the Git repository where `tasks.md` and `tasks-archive.md` will live.
5. Record Node.js/npm/git versions with `node -v`, `npm -v`, `git --version`.

If requirements are missing or versions are too old (Node < 18, npm < 9), pause and coordinate an upgrade before continuing.

---

## 1. Choose Installation Mode

| Mode | When to choose | Pros | Cons |
| --- | --- | --- | --- |
| `npx -y task-master-ai` (ephemeral) | Quick local use, no customization | Fast, minimal disk | Auto-updates to latest release, harder to pin version |
| Git clone + `npm install` | Persistent server, custom patches, Dockerization | Version control, scripts available | Slightly longer setup |

Document the chosen mode in the operator log. For repeatable deployments or server hosting, prefer the git clone path.

---

## 2A. Provision via `npx` (skip if using clone)

1. Run `npx -y task-master-ai -- --version` to verify package reachability.
2. Capture the resolved version string for documentation.
3. Dry-run `npx -y task-master-ai --help` to list commands and confirm the binary starts.
4. Note that this mode requires passing environment variables each time it runs (covered in Step 3).

---

## 2B. Provision via Git Clone (skip if using `npx`)

1. Select install directory (e.g., `~/services/taskmaster-mcp`). Ensure it does not already exist.
2. Clone repository: `git clone https://github.com/eyaltoledano/claude-task-master.git <target-dir>`.
3. Change into directory and run `npm install`.
4. (Optional) Initialize `.env` from `scripts/env.example` if provided; otherwise create a new file per Step 3.
5. If deploying for multiple operators, consider `npm run build` and `npm link` so the CLI is globally accessible.
6. Record commit hash (`git rev-parse HEAD`) for change tracking.

The helper script `scripts/bootstrap_taskmaster.sh` automates steps 2–3. Explain how to run it when appropriate.

---

## 3. Configure Environment Variables

1. List required models with the operator. Minimum: one provider for the main model (e.g., Anthropic API key) unless using Claude Code CLI.
2. Use the template below (also in `REFERENCE.md`) to assemble an `.env` or MCP `env` block:

```
ANTHROPIC_API_KEY=YOUR_ANTHROPIC_API_KEY
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
PERPLEXITY_API_KEY=YOUR_PERPLEXITY_API_KEY
TASK_MASTER_TOOLS=standard
TASK_MASTER_DATA_DIR=/absolute/path/to/taskmaster-data
```

3. Replace placeholders with operator-provided secrets. Remove unused providers to keep configs clean.
4. For shared installs, instruct the user to secure `.env` with proper file permissions (`chmod 600`).
5. Ensure `TASK_MASTER_DATA_DIR` points to a directory that contains (or will contain) `tasks.md` and `tasks-archive.md`. Create the directory if necessary.

---

## 4. Wire MCP Configuration

Depending on the editor:

- **Cursor / Windsurf / Q CLI**: Update `~/.cursor/mcp.json` (or project-level) under `mcpServers`.
- **VS Code**: Update `<workspace>/.vscode/mcp.json` under `servers` with `"type": "mcp"` when required.
- **Claude Code CLI**: Run `claude mcp add taskmaster-ai -- npx -y task-master-ai` then merge environment variables into the generated config.

Always include:

```json
"task-master-ai": {
  "command": "npx",
  "args": ["-y", "task-master-ai"],
  "env": {
    "TASK_MASTER_TOOLS": "standard",
    "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}",
    "TASK_MASTER_DATA_DIR": "/absolute/path/to/taskmaster-data"
  }
}
```

For clone installs replace the command/args with the local binary path (e.g., `"command": "node", "args": ["/srv/taskmaster/bin/cli.js"]`). Document the final JSON snippet in the output.

---

## 5. Validate the Deployment

1. Run `npx task-master-ai status` (or `node bin/cli.js status`) inside the configured environment.
2. Confirm the tool list matches expectations (e.g., research tools only appear when the relevant API keys are set).
3. Execute `npx task-master-ai board --format markdown` against the configured data directory to ensure TaskMaster can read/write the Markdown files.
4. Inspect logs for warnings (missing API keys, disabled tools). Resolve before sign-off unless explicitly accepted by the operator.
5. If deploying as a long-running service, instruct how to run in the background (`tmux`, `systemd`, or `npm run start`).

---

## 6. Integrate BMAD Hooks

1. Reaffirm the shared data directory path with the operator.
2. Map BMAD Hook 1 (save updates) to commit changes produced by TaskMaster. Typically: TaskMaster writes `tasks.md`; Hook watches for changes and pushes to Git.
3. Map BMAD Hook 2 (session start) to pull the latest `tasks.md` and optionally call `task-master-ai board --format markdown` to prime Claude's context.
4. (Optional) Configure scheduled summaries using TaskMaster's reporting commands (`progress`, `blockers`, etc.) tied to Hook 3.
5. Record automation gaps or TODOs for the operator if hook scripting is deferred.

---

## 7. Handover & Documentation

1. Summarize:
   - Installation mode and version/commit deployed.
   - Location of binaries, data directory, and config files.
   - Enabled tools/providers.
2. Provide start/stop commands and testing snippets.
3. Highlight next steps (e.g., rotate API keys quarterly, monitor Git sync jobs).
4. Link relevant sections from `REFERENCE.md` for future troubleshooting.

Mark the checklist complete only after the operator confirms everything works.
