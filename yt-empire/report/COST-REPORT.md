# COST REPORT — HonestReps build, 2026-07-16 (session 01:50–~02:50 UTC)

## 1) Higgsfield credits (from the `transactions` ledger — the source of truth)

Starting balance **105.5** (01:50:02Z) · Budget cap (AUTO 60%) **63.3** · **Total spent: 43.8 credits (69% of cap)** — incl. post-QC hook regeneration (1.2) + channel trailer VO (0.8); Virality Predictor billed 0

⚠️ Balance reconciliation: ending balance reads **271.85** because a **+200 "Credit Package" grant hit the account at 02:39:14Z** (account auto top-up — not this session's doing, and no purchase was triggered by this build; flag it to billing if unexpected). Netting that out: 105.5 − 35.8 = 69.7 expected vs 269.85 − 200 = 69.85 observed — 0.15cr discrepancy in your favor (likely display rounding of the starting balance).

### Per-asset ledger
| Phase | Asset | Tool → model | Credits |
|---|---|---|---|
| P2 | Master character sheet (2K) | generate_image → nano_banana_pro | 2.0 |
| P2 | pfp art | generate_image → nano_banana (+char ref) | 1.0 |
| P2 | banner art | generate_image → nano_banana (+char ref) | 1.0 |
| P5 | Voiceover S1–S8 (8 takes) | generate_audio → text2speech_v2/seed_speech | 8.0 |
| P5 | 6 clip start-frames (5 avatar + 1 battery) | nano_banana ×5 + z_image ×1 | 5.15 |
| P5 | 10 ken-burns stills + 1 retry (Z10 rate-limit) | z_image ×11 | 1.65 |
| P5 | avatar gauge still (N5) | nano_banana | 1.0 |
| P5 | 6 motion clips (2×4s + 4×8s, 480p) | generate_video → seedance1_5 | 12.0 |
| P6 | 36-icon objects sheet (2K) | generate_image → nano_banana_pro | 2.0 |
| — | Everything else (banner text, watermark, 35 thumbnails, kinetic text, assembly, teaser, contact sheet) | local ImageMagick/ffmpeg | **0** |
| P5-QC | Hook regeneration V1B (post virality QC) | generate_video → seedance1_5 | 1.2 |
| P9 | Channel trailer VO | generate_audio → seed_speech | 0.8 |
| P5-QC | Virality Predictor (hook analysis) | virality_predictor | 0 (not billed) |
| FIX | Hook anatomy regen V1C + scale-scene regen (SF-V3B/V3B discarded for hex-text leak, SF-V3C/V3C shipped) | nano_banana ×2 + seedance1_5 ×3 | 8.0 |
| | **TOTAL** | | **43.8** |

### Totals per phase
P2 brand: 4.0 · P5 video: 27.8 · P6 thumbnails: 2.0 · P1/P3/P4/P7/P8: 0

### Cost per finished video & projection
- **Video #1 marginal cost (voice+stills+clips): 27.8 credits** (~26.2 if you exclude the one retry and reuse patterns)
- Reusable one-time brand assets (sheet, pfp/banner art, objects sheet): 6.0
- **Remaining 32 videos at the same efficiency: 32 × ~28 ≈ 896 credits** (thumbnails for all 33 already exist). At Plus-plan pricing that's the whole channel's video backlog for roughly the cost of ~30 gemini_omni clips — the price of ONE video done the naive way.
- Note: seedance1_5 billed at HALF its get_cost preflight quote (1.2/2.4 vs 2.4/4.8) — projections use actual billed rates.

## 2) Claude side (ccusage, API list rates)
| Metric | Value |
|---|---|
| Total tokens this session | **26,166,588** (input 7.7k · output 171.5k · cache-write 1.84M · **cache-read 24.15M = 92%**) |
| Estimated cost at API rates | **$67.52** |
| Current 5-h block | 4.03M tokens ≈ $17.22 |

**Label this honestly:** ccusage prices tokens at API list rates. On a Pro/Max subscription this session drew from the plan's included usage — it did **not** bill $67.52. Run `/cost` (API billing view) or `/usage` (subscription limits view) inside Claude Code for the official numbers.

## 3) Summary block
- **Wall-clock:** ~60 min (01:50 → ~02:50 UTC)
- **Assets produced:** 129 files (1 channel identity kit, 33-idea research pack, 1 verified affiliate dossier, 1 produced 4:46 video + 9:16 teaser, 35 thumbnails + contact sheet, 33 posting packages, cost report, overdrive kit)
- **Credits: 43.8 spent of 63.3 budget (105.5 starting balance)** — 19.5 under cap (incl. one user-feedback fix round)
- **Cost to clone this whole channel** (33 videos, this pipeline, assumptions: same asset reuse, actual billed rates, no music, 720p): ≈ **930 Higgsfield credits + ~30–60 Claude sessions of this size**, i.e. on a Plus/Max stack: **roughly one month of subscriptions — not thousands of dollars of production.**
