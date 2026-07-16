# DECISIONS LOG

- P0: CREDIT_BUDGET=AUTO resolved to 63.3 credits (60% of 105.5 starting balance).
- P0: apt mirror 404s on first ffmpeg install → fixed with `apt-get update` then reinstall; imagemagick skipped (ffmpeg covers downscale/contact-sheet needs).
- P0: WebFetch of youtube.com returns 403 (datacenter block) → channel research will run through WebSearch snippets + third-party stat sites; every claim still gets a source URL.
- P0: Assembly path = Higgsfield `video-explainer` workflow (single narrator over stylized blocks, optional mascot — exact match for our avatar-hosted explainer).
- P0: gemini_omni (workflow default) = 30cr/clip → 900cr for 30 blocks. Impossible under 63.3 cap → degraded per Rule 4: cheapest model (seedance1_5 480p 2.4-4.8cr/clip) + local ffmpeg assembly instead of server explainer_video (free either way, but local honors the ≤3s cut rule and adds free kinetic text).
- P0: TTS pricing scales with length → voice in segment-sized takes; seed_speech variant (1.4cr/120w) chosen over minimax (2.1) and seed_audio (4.2).
- P0: Lip-sync dropped (sync_so extra cost + a flat 2D mascot reads fine with prompted mouth movement). Logged as budget degradation, not quality loss.
- P0: presets_show + full animation_actions catalogs skipped: both target image-to-video motion presets / 3D rigs irrelevant to the locked 2D pipeline, and their catalogs would burn significant context. Assembly path chosen from get_workflow_instructions instead.
- P0: Brief's warm-up says approvals cluster; imagemagick+fonts installed during Phase 0 (only install window). Anton font fetched from google/fonts GitHub (first attempt 195-byte stub → retried raw.githubusercontent URL, OK).
