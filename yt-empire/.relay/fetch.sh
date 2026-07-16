#!/usr/bin/env bash
# Asset relay batch 5: trailer VO
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p overdrive
curl -fsSL --retry 3 --retry-delay 2 -o overdrive/trailer-vo.mp3 "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_120829_f43c45d7-8cba-490d-b375-38895e18d952.mp3"
echo "OK trailer-vo"
