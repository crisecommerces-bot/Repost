# Model Economics — measured via get_cost preflights (2026-07-16, Plus plan)

Starting balance: **105.5 credits** · Budget cap (AUTO = 60%): **63.3 credits**

## Image models
| Model | Cost/img | Reference support | Verdict |
|---|---|---|---|
| z_image | **0.15** | none (text-only) | ✅ cheapest — non-avatar scene stills |
| nano_banana | 1.0 | image_references | ✅ avatar-consistent stills |
| nano_banana_2_lite | 1.0 | image_references | alternate |
| recraft_v4_1 (utility/vector) | 1.25 | none, but hex color palette control | flat-vector option |
| nano_banana_2 | 1.5 | image | backup master |
| nano_banana_pro | 2.0 | image | ✅ master assets only (best text/diagrams) |

## Video models (per clip)
| Model | Config | Cost | Verdict |
|---|---|---|---|
| seedance1_5 | 4s 480p, no audio | **2.4** | ✅ PICK — cheapest/s, start+end frame control |
| seedance1_5 | 8s 480p, no audio | 4.8 | ✅ for longer beats |
| seedance1_5 | 4s 720p | 4.8 | 480p+local upscale wins for flat 2D |
| minimax-fast | 6s 512 | 3.0 | backup |
| minimax-2.3-fast | 6s 768 | 4.0 | backup |
| veo3_1_lite | 4s / 8s | 4.0 / 8.0 | hook-shot candidate |
| kling3_0_turbo | 5s 720p | 7.5 | too expensive |
| seedance_2_0_mini | 10s 720p | 25 | no |
| wan2_6 | 10s 720p | 25 | no |
| gemini_omni (workflow default) | 10s 720p | **30** | ✗ 30 clips = 900cr — impossible |

## Audio (TTS) — cost scales with text length
| Model/variant | ~120 words | ~750-word script | Verdict |
|---|---|---|---|
| text2speech_v2 / seed_speech | **1.4** | ~8.8 | ✅ PICK |
| text2speech_v2 / minimax | 2.1 | ~13 | backup |
| seed_audio (default) | 0.7/20w | ~26 | no |

## Assembly
- `explainer_video` server assembly: free (subtitles 0.05/block) — but locks 10s blocks → violates ≤3s cut rule
- **local ffmpeg assembly: free, full cut control → PICK**

## Locked pipeline
1. Master avatar sheet: nano_banana_pro (2cr) → sliced locally for expressions
2. Scene stills: nano_banana w/ avatar ref (1cr) or z_image (0.15) → ken-burns motion via ffmpeg zoompan (free)
3. Hero motion clips: seedance1_5 480p start_image-driven (2.4–4.8cr), lanczos-upscaled to 720p locally
4. Kinetic text / diagrams: local ImageMagick+ffmpeg, Anton font, brand hex colors (free)
5. Voice: seed_speech in segment takes (~9cr total)
6. Assembly: local ffmpeg (free)

## Budget allocation plan (of 63.3)
| Bucket | Planned |
|---|---|
| Brand + avatar masters | ~8 |
| Video stills + clips | ~30 |
| Voiceover | ~9 |
| Retries / QC / teaser | ~8 |
| **Planned total** | **~55** (8.3 headroom below cap) |
