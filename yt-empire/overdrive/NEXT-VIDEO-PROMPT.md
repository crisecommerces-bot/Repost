# NEXT-VIDEO-PROMPT — the repeatable machine

Paste this into a fresh Claude Code session in this repo to produce video #N end-to-end:

---
Produce HonestReps video #N = rank N in `yt-empire/research/ideas-ranked.md`.
Read first: `yt-empire/CHECKPOINT.md`, `report/model-economics.md` (locked models + ACTUAL billed prices), `DECISIONS.md` (pipeline pivots — esp. the GitHub Actions asset relay in `.relay/`, required because the sandbox blocks Higgsfield CDNs), `video-01/assemble.py` (assembly standard), `script/beat-map.md` + `script/voiceover.md` (formats to replicate).

Fixed assets — DO NOT regenerate:
- Character master: Higgsfield image job `a9eb241b-70fb-4351-b2f9-6d9559a04fdf` (reference in every avatar generation via image_references)
- Voice: preset "Andre" `f1e8226e-2248-4d5f-b43c-0a79e9949dbf`, text2speech_v2/seed_speech, segment takes, atempo 0.90 at assembly
- Brand: #1B2440 / #FF6B35 / #2EE6A8, Anton font at `channel-identity/fonts/`, busts at `video-01/busts/`, thumbnail already at `thumbnails/NN-*.png`
- Models: stills z_image (0.15) / nano_banana+ref (1.0); clips seedance1_5 480p silent (billed 1.2/4s, 2.4/8s); local ffmpeg assembly

Steps: (1) write retention script per voiceover.md architecture (cold open ≤5s, loop, re-hooks ~30/60%, 15–20s Speediance beat mid-video with {{AFFILIATE_LINK}} pointer, ≤15s outro, ~690 words); (2) beat map ≤3s holds, ~100 beats from ≤20 paid assets (6 clips + ~11 stills + reuse busts/kinetic cards); (3) generate voice+stills+clips, relay down via `.relay/fetch.sh` push; (4) copy assemble.py to video-NN/, swap SEG/PAD, target 285–315s; (5) QC montage eyeball + QC-NOTES.md; (6) 9:16 teaser from hook; (7) update the posting package's chapter timestamps; (8) commit/push; (9) append actuals to report/COST-REPORT.md. Budget gate: stop if session spend would exceed 40 credits.
---
