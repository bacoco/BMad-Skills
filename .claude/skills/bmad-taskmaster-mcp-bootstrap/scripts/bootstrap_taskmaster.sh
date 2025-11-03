#!/usr/bin/env bash
set -euo pipefail

REPO_URL="${1:-https://github.com/eyaltoledano/claude-task-master.git}"
TARGET_DIR="${2:-taskmaster-mcp}"

if [[ -d "${TARGET_DIR}" ]]; then
  echo "[taskmaster-bootstrap] Target directory '${TARGET_DIR}' already exists. Aborting to avoid overwriting." >&2
  exit 1
fi

echo "[taskmaster-bootstrap] Cloning ${REPO_URL} into ${TARGET_DIR}" >&2
git clone "${REPO_URL}" "${TARGET_DIR}"

cd "${TARGET_DIR}"

echo "[taskmaster-bootstrap] Installing npm dependencies" >&2
npm install

HASH=$(git rev-parse HEAD)
echo "[taskmaster-bootstrap] Installed commit ${HASH}" >&2

echo "[taskmaster-bootstrap] Done. Populate ${TARGET_DIR}/.env before running the server." >&2
