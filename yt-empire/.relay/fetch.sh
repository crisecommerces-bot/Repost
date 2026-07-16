#!/usr/bin/env bash
# Asset relay batch 4: the 6 motion clips
set -euo pipefail
cd "$(dirname "$0")/.."
B="https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv"
fetch() { mkdir -p "$(dirname "$1")"; curl -fsSL --retry 3 --retry-delay 2 -o "$1" "$B/$2"; echo "OK $1"; }
fetch video-01/clips/V1.mp4 hf_20260716_022047_ecbd457d-fb8d-4da1-a499-d15225cd06dc.mp4
fetch video-01/clips/V2.mp4 hf_20260716_022051_1f48b05a-f5c6-4eca-97a4-a7989eaf7d3c.mp4
fetch video-01/clips/V3.mp4 hf_20260716_022054_10a8666f-9760-458f-91e4-37ff62d26970.mp4
fetch video-01/clips/V4.mp4 hf_20260716_022056_28e82b1a-0ed4-43e0-8efb-c4fcd40a226d.mp4
fetch video-01/clips/V5.mp4 hf_20260716_022059_6c925815-7420-4200-9dfb-01d7a29bc77e.mp4
fetch video-01/clips/V6.mp4 hf_20260716_022102_ff5bbbf4-3f1d-410c-a032-d74f52c763c5.mp4
