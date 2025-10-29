#!/usr/bin/env bash
# Flatten a directory of source files into a single markdown document for review.
# Usage: ./code_flattener.sh <source_dir> <output_file>
set -euo pipefail
if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <source_dir> <output_file>"
  exit 1
fi
SRC="$1"
OUT="$2"
{
  find "$SRC" -type f -name '*.py' -o -name '*.ts' -o -name '*.js' | sort | while read -r file; do
    echo "# FILE: $file"
    echo '```'
    cat "$file"
    echo '```'
    echo
  done
} > "$OUT"
echo "Flattened files from $SRC into $OUT"
