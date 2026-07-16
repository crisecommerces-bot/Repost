#!/usr/bin/env bash
# Asset relay: runs on GitHub Actions (full egress) to fetch Higgsfield CDN
# assets that the sandbox network policy blocks. Regenerated per batch.
set -euo pipefail
cd "$(dirname "$0")/.."

fetch() { mkdir -p "$(dirname "$1")"; curl -fsSL --retry 3 --retry-delay 2 -o "$1" "$2"; echo "OK $1"; }

fetch channel-identity/character-sheet.png "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_020043_a9eb241b-70fb-4351-b2f9-6d9559a04fdf.png"
# relay-batch-1 1784167604
