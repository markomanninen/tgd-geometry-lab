#!/usr/bin/env bash
# Run the TGD Geometry Software Lab test suite.
#   ./scripts/run_tests.sh                 # without Clifford tests
#   ./scripts/run_tests.sh /path/clifford  # with Prodanov's clifford package
# Exit status is non-zero if any test fails.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
CLI="${1:-${CLIFFORD_PATH:-}}"
PRE="tgd_root:\"$ROOT\"\$"
if [ -n "$CLI" ]; then PRE="$PRE clifford_path:\"$(cd "$CLI" && pwd)\"\$"; fi
LOG="$(mktemp)"
maxima --very-quiet --batch-string="$PRE batchload(\"$ROOT/tests/run-all.mac\")\$" 2>&1 \
  | grep -v -E 'help system|CL-INFO' | tee "$LOG" \
  | grep -E '^---|PASS|FAIL|SKIP|TGD_TESTS|Failed|error' || true
grep -q 'TGD_TESTS passed=[0-9]* failed=0' "$LOG"
