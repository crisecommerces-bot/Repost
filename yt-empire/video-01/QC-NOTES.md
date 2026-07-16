# QC Notes — video-01/final.mp4 (REVIEW BEFORE UPLOADING)

**Cut:** 285.6s (4:46) · 1280×720 @30fps · 100 beats, max hold 3.0s · AAC audio.

## What I verified programmatically/visually
- Spot-checked 13 frames across the timeline: brand palette consistent, kinetic text spelled correctly, avatar identical across shots, end card clean
- Audio: 8 segment takes muxed, no truncation (S6 clipping bug found and fixed), 0.90× pitch-safe pacing
- Cold open starts on the scoop-slam action shot; outro hard-cuts to a 10s silent branded end-screen card (space for YouTube end-screen elements)

## What YOU should review before publish (in order)
1. **Watch the full video once.** AI clips (V1–V6) can contain small motion artifacts I can't hear/see from frames — especially check the mascot's hands in the bench-press clip and the myth-chop sequence.
2. **Listen for TTS artifacts** at segment boundaries (S3→S4 ~1:32, S5→S6 ~3:14) and any mispronunciations ("phosphocreatine", "creatinine").
3. **Fact spot-check (all standard consensus, but verify numbers):** +5–15% performance; 20–40% store increase; ~1–2kg water in week 1; ~1 in 4 low-responders; 2009 DHT/rugby study (Van der Merwe et al.) never replicated; no kidney damage in healthy users; 3–5 g/day monohydrate.
4. **Affiliate beat (3:14–3:37):** says "Speediance smart gym" — only upload after your affiliate approval, or re-record/trim that line if you pick a different program.
5. **Pacing taste check:** the video uses ~28s of visual-only pauses; if any beat feels slow, the assembler (`assemble.py`) re-renders the whole cut in ~3 min after editing PAD values.
6. **Silence under end card** (last 10s) is intentional — YouTube overlays end-screen elements there; add music in an editor if you prefer.
7. **AI-content disclosure:** tick YouTube's altered/synthetic content box on upload (this is AI-generated).

## Known compromises (logged in DECISIONS.md)
- 480p AI clips lanczos-upscaled to 720p (flat vector art hides this well; check on a large screen)
- No lip-sync on the mascot (budget); mascot reads as animated host, not talking head
- Silence (no music bed): add a -14 LUFS low-key track in an editor if desired — I could not generate music (no standalone music model on this MCP)
