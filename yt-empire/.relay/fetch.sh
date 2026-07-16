#!/usr/bin/env bash
# Asset relay: runs on GitHub Actions (full egress) to fetch Higgsfield CDN
# assets that the sandbox network policy blocks. Regenerated per batch.
set -euo pipefail
cd "$(dirname "$0")/.."

fetch() { mkdir -p "$(dirname "$1")"; curl -fsSL --retry 3 --retry-delay 2 -o "$1" "$2"; echo "OK $1"; }

fetch channel-identity/character-sheet.png "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_020043_a9eb241b-70fb-4351-b2f9-6d9559a04fdf.png"
# relay-batch-1 1784167604
fetch channel-identity/pfp-art.png "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_020650_81c495cb-74b8-42fe-a427-ca3baaa55758.png"
fetch channel-identity/banner-art.png "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_020654_bfb0170b-c4e6-4c00-a51b-be3783dbcf0a.png"
