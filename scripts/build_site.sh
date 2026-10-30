#!/usr/bin/env bash
# Build the public site into site/.  Extra arguments go to mkdocs,
# e.g. ./scripts/build_site.sh --strict
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
rm -rf docs/notebooks
mkdir -p docs/notebooks
cp notebooks/*.ipynb docs/notebooks/
mkdocs build "$@"
