#!/usr/bin/env bash
# Asset relay batch 10: V3C (no text-leak scale scene)
set -euo pipefail
cd "$(dirname "$0")/.."
curl -fsSL --retry 3 --retry-delay 2 -o video-01/clips/V3C.mp4 "https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv/hf_20260716_220344_1f4d4f91-5975-4aec-b82f-23cb71c21e85.mp4"
echo OK
