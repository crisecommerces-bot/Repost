#!/usr/bin/env bash
# Asset relay batch 3: voice takes + stills + objects sheet
set -euo pipefail
cd "$(dirname "$0")/.."
B="https://d8j0ntlcm91z4.cloudfront.net/user_3EppDFRklfazcc4fzUEIjYmm7tv"
fetch() { mkdir -p "$(dirname "$1")"; curl -fsSL --retry 3 --retry-delay 2 -o "$1" "$B/$2"; echo "OK $1"; }

fetch video-01/audio/S1.mp3 hf_20260716_021625_25908fce-3884-4841-919b-a6a4a46bcd39.mp3
fetch video-01/audio/S2.mp3 hf_20260716_021627_75624cd3-9d08-41cc-b065-26845b891cc0.mp3
fetch video-01/audio/S3.mp3 hf_20260716_021630_eca83679-5e57-4476-bbb1-78fbb127ff3e.mp3
fetch video-01/audio/S4.mp3 hf_20260716_021634_bba7524c-b800-4a44-a568-11d67539f755.mp3
fetch video-01/audio/S5.mp3 hf_20260716_021637_3e90b619-f5a0-4fcd-b776-3f92f6457501.mp3
fetch video-01/audio/S6.mp3 hf_20260716_021640_e3ea9355-d885-4905-9d11-e766cc344966.mp3
fetch video-01/audio/S7.mp3 hf_20260716_021642_ae5fcc0c-41ab-4a14-b7f0-5b6f2edb33f3.mp3
fetch video-01/audio/S8.mp3 hf_20260716_021643_8b39e82b-946e-480b-9485-3624251757e2.mp3

fetch video-01/stills/SF-V1.png hf_20260716_021719_9d35965c-5166-420d-a7cb-7f6886f55e74.png
fetch video-01/stills/SF-V2.png hf_20260716_021721_a8715cd7-ccff-4a59-857c-034ee5be9f99.png
fetch video-01/stills/SF-V3.png hf_20260716_021724_b44969a9-d040-41b2-b2b7-fa8bb5f06aec.png
fetch video-01/stills/SF-V4.png hf_20260716_021727_e0bbc23c-b805-4288-89ad-7c34cab5676c.png
fetch video-01/stills/SF-V5.png hf_20260716_021730_c637cd38-6843-4609-aead-6bc3013508d0.png
fetch video-01/stills/SF-V6.png hf_20260716_021733_36199841-347b-4e1b-9e78-d3c56f0cb562.png
fetch video-01/stills/N5.png  hf_20260716_021736_58c9af80-6a73-459d-a5b8-4b78da429faf.png
fetch video-01/stills/Z1.png  hf_20260716_021737_a0c86994-266a-41a5-9206-c52a763ed303.png
fetch video-01/stills/Z2.png  hf_20260716_021739_d432027a-79c2-4fd8-aef4-55c5692b1b3e.png
fetch video-01/stills/Z3.png  hf_20260716_021741_4951023b-589c-46e4-a8e7-550c3d75586d.png
fetch video-01/stills/Z4.png  hf_20260716_021743_c3c042aa-6e0f-43ba-800c-e68aeae2d17d.png
fetch video-01/stills/Z6.png  hf_20260716_021746_470b720f-89d5-4824-9a1b-da02054e84e1.png
fetch video-01/stills/Z7.png  hf_20260716_021748_469374f7-71a6-4aac-87c0-ad74aa92edc5.png
fetch video-01/stills/Z8.png  hf_20260716_021750_fc9d9766-9eeb-4309-b5a3-d4965dc2e611.png
fetch video-01/stills/Z9.png  hf_20260716_021752_c941a5b9-7649-4a44-b859-54477df34f73.png
fetch video-01/stills/Z10.png hf_20260716_021838_776b6ba0-ed70-4c57-a7ac-08bb8ac799c8.png
fetch video-01/stills/Z11.png hf_20260716_021756_53e157ce-3270-4acf-bb7f-7aab363f78bf.png
fetch thumbnails/_objects-sheet.png hf_20260716_022143_65afef11-a1bd-4899-a6ec-4cdd4fb3154b.png
