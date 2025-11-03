# TaskMaster MCP Reference

Use this file when you need deeper context, command snippets, or troubleshooting material that would bloat the main SKILL.md.

---

## Core Commands

| Command | Purpose | Notes |
| --- | --- | --- |
| `npx -y task-master-ai -- --version` | Confirm npm package availability and version. | Append `--tag <version>` to pin prerelease builds. |
| `npx -y task-master-ai status` | Lists enabled tools and checks API key coverage. | Mirrors `node bin/cli.js status` when installed locally. |
| `npx -y task-master-ai board --format markdown` | Dumps the canonical task board. | Use `--data-dir <path>` if `TASK_MASTER_DATA_DIR` not set. |
| `npx -y task-master-ai progress` | Summarizes task completion by status. | Great for Hook 3 scheduled reports. |
| `npm run build` | Prepares distributable build (clone installs). | Required before `npm link` in some environments. |

## Environment Variables

| Variable | Required? | Description |
| --- | --- | --- |
| `TASK_MASTER_TOOLS` | Optional | Set to `all`, `standard`, `core`, or comma-separated list of tool names to enable. Default: `standard`. |
| `TASK_MASTER_DATA_DIR` | Recommended | Directory where `tasks.md`, `tasks-archive.md`, and other stateful files are stored. |
| `ANTHROPIC_API_KEY` | Yes (unless using Claude Code CLI) | Enables Claude-based commands. |
| `OPENAI_API_KEY` | Optional | Enables OpenAI-backed commands. |
| `PERPLEXITY_API_KEY` | Optional | Enables research model. |
| `GOOGLE_API_KEY` | Optional | Enables Gemini provider. |
| `MISTRAL_API_KEY` | Optional | Enables Mistral provider. |
| `GROQ_API_KEY` | Optional | Enables Groq provider. |
| `OPENROUTER_API_KEY` | Optional | Enables OpenRouter aggregator. |
| `XAI_API_KEY` | Optional | Enables xAI provider. |
| `AZURE_OPENAI_API_KEY` | Optional | Enables Azure OpenAI provider. |
| `OLLAMA_API_KEY` | Optional | Enables Ollama provider. |

Store secrets in `.env` files excluded from version control (add to `.gitignore`) and restrict permissions with `chmod 600` (Unix) or ACL adjustments (Windows).

## Recommended Directory Layout

```
~/projects/
├── taskmaster-data/
│   ├── tasks.md
│   └── tasks-archive.md
└── taskmaster-mcp/
    ├── .env
    ├── package.json
    └── ...
```

Point `TASK_MASTER_DATA_DIR` at `~/projects/taskmaster-data`. Configure Hooks to commit that folder to GitHub or other storage.

## MCP Configuration Snippets

### Cursor / Windsurf / Q CLI

```json
{
  "mcpServers": {
    "task-master-ai": {
      "command": "npx",
      "args": ["-y", "task-master-ai"],
      "env": {
        "TASK_MASTER_TOOLS": "standard",
        "TASK_MASTER_DATA_DIR": "${HOME}/projects/taskmaster-data",
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

### VS Code (per-project)

```json
{
  "servers": {
    "task-master-ai": {
      "type": "mcp",
      "command": "node",
      "args": ["/srv/taskmaster-mcp/bin/cli.js"],
      "env": {
        "TASK_MASTER_TOOLS": "all",
        "TASK_MASTER_DATA_DIR": "/srv/taskmaster-data",
        "ANTHROPIC_API_KEY": "${ANTHROPIC_API_KEY}"
      }
    }
  }
}
```

Replace paths with the operator's actual locations. Encourage them to test the config by restarting the editor and verifying that the MCP server reports a non-zero tool count.

## Hook Integration Tips

- **Hook 1 (Save Updates)**: Monitor the data directory for file changes (`tasks.md`, `tasks-archive.md`). Trigger a Git commit + push, or invoke TaskMaster's own `export` commands if you maintain derived artifacts.
- **Hook 2 (Load on Session Start)**: Pull the latest repo, run `task-master-ai board --format markdown --data-dir <path>`, and inject the result into Claude's context before activating planning skills.
- **Hook 3 (Scheduled Sync)**: Combine `task-master-ai progress --format markdown` with email/Slack bots. Capture the timestamp in commit messages to maintain an audit trail.

## Troubleshooting

| Symptom | Likely Cause | Resolution |
| --- | --- | --- |
| `Error: No tools enabled` | Missing API keys or `TASK_MASTER_TOOLS` set to an empty list. | Confirm at least one provider is configured and restart the MCP client. |
| `Cannot find module 'task-master-ai'` during `npx` | Firewall or npm registry outage. | Retry, check corporate proxy, or switch to git clone path. |
| `tasks.md not found` warnings | `TASK_MASTER_DATA_DIR` incorrect or repo not cloned. | Create the directory and ensure the Markdown files exist (copy templates if needed). |
| MCP client fails to connect | Editor not restarted or config path wrong. | Double-check config file location and restart the editor/CLI. |
| Rate limit errors from providers | Excessive automation frequency. | Stagger hooks, add caching, or request higher quotas. |

## Useful Resources

- TaskMaster Docs: https://docs.task-master.dev
- GitHub Repo: https://github.com/eyaltoledano/claude-task-master
- Discord Support: https://discord.gg/taskmasterai

Use these references sparingly—load only the sections needed for the current task to preserve context budget.
