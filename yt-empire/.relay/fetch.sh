#!/usr/bin/env bash
# Asset relay batch 9: fixed hook clip V1C + scale scene V3B
set -euo pipefail
cd "$(dirname "$0")/.."
B="https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv"
fetch() { mkdir -p "$(dirname "$1")"; curl -fsSL --retry 3 --retry-delay 2 -o "$1" "$B/$2"; echo "OK $1"; }
fetch video-01/clips/V1C.mp4 hf_20260716_215800_fe2b43ad-4fcf-44b2-812c-7f88726a6ef4.mp4
fetch video-01/clips/V3B.mp4 hf_20260716_215900_88e7dc99-6bab-4f1f-9f15-101cf095ce92.mp4
fetch video-01/stills/SF-V3B.png hf_20260716_215753_8afa6720-d945-44d7-9585-2fc33e37290f.png
