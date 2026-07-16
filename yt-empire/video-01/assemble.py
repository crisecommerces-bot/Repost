#!/usr/bin/env python3
"""HonestReps video #1 assembler.
Implements script/beat-map.md: per-segment beat lists scaled to the (slowed)
voice-take durations, every beat <= 3.0s, rendered as uniform .ts parts and
concatenated; per-segment audio muxed with head/tail pauses; branded end card.
"""
import subprocess, json, os, sys

V = "clips"; G = "gfx"; S = "stills"; A = "audio"; W = "work"
os.makedirs(W, exist_ok=True)
FPS, WI, HE = 30, 1280, 720
ATEMPO = 0.90  # pitch-safe slowdown (seed_speech reads fast)

def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:]); sys.exit(f"FAILED: {cmd[:140]}")
    return r.stdout

def dur(f):
    return float(sh(f"ffprobe -v error -show_entries format=duration -of csv=p=0 '{f}'").strip())

# ---- 1. slow audio ----
seg_audio, seg_adur = {}, {}
for i in range(1, 9):
    src, out = f"{A}/S{i}.mp3", f"{W}/S{i}.wav"
    if not os.path.exists(out):
        sh(f"ffmpeg -y -v error -i {src} -filter:a atempo={ATEMPO} -ar 44100 -ac 2 {out}")
    seg_audio[i], seg_adur[i] = out, dur(out)
print("audio slowed:", {k: round(v,2) for k,v in seg_adur.items()})

# ---- 2. beat definitions ----
# modes: clip(src,in,crop) | kb(img, z=in/out) | card(img)
def C(src, tin, w=1.0, crop=None):   return dict(m="clip", src=f"{V}/{src}", tin=tin, w=w, crop=crop)
def KB(img, w=1.0, z="in"):          return dict(m="kb", src=f"{S}/{img}", w=w, z=z)
def CA(img, w=1.0, src_dir=G):       return dict(m="card", src=f"{src_dir}/{img}", w=w)
def B(name, w=1.0):                  return dict(m="kb", src=f"{G}/bust-{name}.png", w=w, z="in")

SEG = {
 1: [C("V1C.mp4",0.0,1.0), C("V1C.mp4",1.4,0.9,"z"), C("V1C.mp4",2.4,0.9), CA("K1.png",0.8), CA("K2.png",0.8), CA("K3.png",0.9), B("shock",0.8)],
 2: [B("think",0.9), CA("K4.png",1.1), KB("Z10.png",0.9), KB("Z6.png",1.0), KB("Z6.png",0.8,"out"), CA("K5.png",1.0), B("point",0.9), CA("KRING.png",0.7)],
 3: [CA("K6.png",0.9), KB("Z1.png",1.1), KB("Z2.png",1.1), KB("Z3.png",1.1), CA("K7.png",1.0), KB("Z4.png",1.1),
     C("V2.mp4",0.0,1.1), C("V2.mp4",2.8,1.1), C("V2.mp4",5.4,1.1), C("V4.mp4",0.0,1.0,"z"), B("shock",0.8), B("excited",0.9),
     C("V2.mp4",4.0,1.0,"z"), KB("Z4.png",0.9,"out"), CA("K8.png",1.0), KB("N5.png",1.1), C("V4.mp4",3.0,1.1,"z"), KB("Z11.png",1.1), B("think",0.9), CA("K9b.png",1.0)],
 4: [CA("K9.png",1.1), B("neutral",0.9), KB("Z4.png",1.0,"out"), C("V3B.mp4",0.0,1.1), CA("K10.png",1.0), B("point",0.9),
     C("V3B.mp4",3.0,1.1), C("V3B.mp4",5.2,1.1,"z"), KB("Z4.png",0.9), KB("N5.png",1.0,"out"), C("V4.mp4",0.0,1.1),
     C("V4.mp4",3.0,1.1), CA("K11.png",1.0), KB("Z11.png",1.0), C("V4.mp4",5.4,1.0,"z"), KB("Z11.png",0.9,"out"), B("think",0.8), C("V4.mp4",1.5,1.1)],
 5: [B("shock",0.9), C("V5.mp4",0.0,1.1), C("V5.mp4",2.6,1.0), CA("K12a.png",0.8), CA("K5.png",1.0), B("think",0.9),
     KB("Z6.png",1.0), KB("Z6.png",0.9,"out"), C("V5.mp4",1.8,1.1,"z"), CA("K12b.png",0.8), KB("Z7.png",1.1), KB("Z7.png",0.9,"out"),
     C("V5.mp4",3.8,1.1), CA("K12c.png",0.8), C("V3B.mp4",3.2,1.0), KB("Z8.png",1.1), C("V5.mp4",5.6,1.1)],
 6: [B("point",0.9), C("V4.mp4",1.0,1.0), B("neutral",0.8), C("V6.mp4",0.0,1.0,"zl"), C("V6.mp4",1.6,1.0,"zl"), C("V6.mp4",0.6,1.0,"zl"), B("excited",0.8), C("V6.mp4",0.3,1.0,"z"), CA("KCTA.png",1.0)],
 7: [B("excited",0.9), CA("K13.png",1.0), CA("KANY.png",0.9), CA("KEVERY.png",0.9), KB("Z9.png",1.1), KB("Z9.png",0.9,"out"),
     CA("K2.png",0.8), B("point",0.9), CA("K4.png",0.9), KB("Z3.png",1.0), KB("Z10.png",1.1), CA("K1IN4.png",1.0),
     B("excited",0.8), CA("K14.png",1.0), C("V4.mp4",3.4,1.0,"z"), CA("KFLAT.png",1.1), CA("K2.png",0.7)],
 8: [B("neutral",0.9), C("V6.mp4",1.2,1.1,"zl"), KB("Z9.png",0.8,"out"), B("wave",1.0), CA("KNEXT.png",0.9)],
}
# head/tail visual-only padding per segment (sums to ~28s of designed pauses)
PAD = {1:(0.3,0.7), 2:(0.4,1.8), 3:(0.5,5.4), 4:(0.5,5.6), 5:(0.5,6.4), 6:(0.4,2.2), 7:(0.5,5.4), 8:(0.3,0.2)}

# ---- 3. render beats ----
def render_beat(idx, b, d):
    out = f"{W}/p{idx:04d}.ts"
    frames = max(int(round(d * FPS)), 6)
    common = f"-r {FPS} -pix_fmt yuv420p -c:v libx264 -preset veryfast -crf 20 -an -f mpegts '{out}'"
    if b["m"] == "clip":
        cmap = {"z": "crop=712:400:71:40,", "zl": "crop=712:400:0:40,", "zr": "crop=712:400:142:40,"}
        crop = cmap.get(b.get("crop") or "", "")
        vf = f"{crop}scale={WI}:{HE}:flags=lanczos,setsar=1"
        sh(f"ffmpeg -y -v error -ss {b['tin']} -i '{b['src']}' -t {d} -vf \"{vf}\" {common}")
    else:
        zexpr = "min(zoom+0.0012,1.25)" if b.get("z","in")=="in" else "if(eq(on,1),1.25,max(zoom-0.0012,1.0))"
        vf = (f"scale=5120:-1,zoompan=z='{zexpr}':d={frames}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              f":s={WI*2}x{HE*2}:fps={FPS},scale={WI}:{HE}:flags=lanczos,setsar=1")
        sh(f"ffmpeg -y -v error -loop 1 -i '{b['src']}' -t {d} -vf \"{vf}\" {common}")
    return out, frames / FPS

manifest, t_cursor, chapters = [], 0.0, {}
idx = 0
seg_files = []
for s in range(1, 9):
    beats = SEG[s]
    head, tail = PAD[s]
    target = seg_adur[s] + head + tail
    assert len(beats)*3.0 >= target + 0.2, f"S{s}: {len(beats)} beats cannot fill {target:.1f}s"
    wsum = sum(b["w"] for b in beats)
    scale = target / wsum
    durs = [min(b["w"] * scale, 3.0) for b in beats]
    # redistribute clamp loss onto unclamped beats
    loss = target - sum(durs)
    while loss > 0.01:
        room = [i for i,dd in enumerate(durs) if dd < 3.0]
        if not room: break
        add = loss / len(room)
        for i in room: durs[i] = min(durs[i] + add, 3.0)
        loss = target - sum(durs)
    parts = []
    for b, dd in zip(beats, durs):
        out, real = render_beat(idx, b, dd); idx += 1
        parts.append(out)
    lst = f"{W}/seg{s}.txt"
    open(lst,"w").write("\n".join(f"file '{os.path.basename(p)}'" for p in parts))
    segv = f"{W}/seg{s}.ts"
    sh(f"cd {W} && ffmpeg -y -v error -f concat -safe 0 -i seg{s}.txt -c copy seg{s}.ts")
    vdur = dur(segv)
    # audio: head silence + take + tail padding to video length
    sega = f"{W}/seg{s}_a.wav"
    sh(f"ffmpeg -y -v error -i {seg_audio[s]} -af \"adelay={int(head*1000)}|{int(head*1000)},apad\" -t {vdur} {sega}")
    segav = f"{W}/seg{s}_av.ts"
    sh(f"ffmpeg -y -v error -i {segv} -i {sega} -c:v copy -c:a aac -b:a 160k -shortest -f mpegts {segav}")
    seg_files.append(segav)
    chapters[s] = t_cursor
    t_cursor += vdur
    print(f"S{s}: audio {seg_adur[s]:.1f}s -> video {vdur:.1f}s ({len(beats)} beats)")

# ---- 4. end card (10s, silent) ----
endv = f"{W}/end.ts"
sh(f"ffmpeg -y -v error -loop 1 -i {G}/KEND.png -f lavfi -i anullsrc=r=44100:cl=stereo -t 10 "
   f"-vf \"scale=5120:-1,zoompan=z='min(zoom+0.0008,1.12)':d={10*FPS}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={WI*2}x{HE*2}:fps={FPS},scale={WI}:{HE}:flags=lanczos,setsar=1\" "
   f"-r {FPS} -pix_fmt yuv420p -c:v libx264 -preset veryfast -crf 20 -c:a aac -b:a 160k -shortest -f mpegts {endv}")
seg_files.append(endv)

# ---- 5. final concat ----
open(f"{W}/final.txt","w").write("\n".join(f"file '{os.path.basename(p)}'" for p in seg_files))
sh(f"cd {W} && ffmpeg -y -v error -f concat -safe 0 -i final.txt -c:v copy -c:a aac -b:a 160k ../final.mp4")
total = dur("final.mp4")
print(f"FINAL: {total:.1f}s ({total/60:.2f} min)")
json.dump({"total_sec": total, "chapter_starts": {k: round(v,1) for k,v in chapters.items()}},
          open("assembly-result.json","w"), indent=2)
