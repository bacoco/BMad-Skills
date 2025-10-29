# OpenSpec Runtime Workspace

This directory stores active and archived OpenSpec artifacts produced by the skills in `expansion/openspec/`.

```
openspec/
  changes/   # In-flight proposals, tasks, delta specs, and execution logs per change-id
  specs/     # Canonical specification files kept in sync via the archive skill
```

The scripts shipped with each OpenSpec skill read and write to this structure using relative paths so the workflow works offline and without API keys.
