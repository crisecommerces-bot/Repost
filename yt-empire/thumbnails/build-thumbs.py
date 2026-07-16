#!/usr/bin/env python3
"""Composite 33 thumbnails + 2 A/B variants from: master-sheet busts (identical
avatar everywhere), the 6x6 objects sheet, Anton typography, brand palette.
All local => zero credits, zero spelling defects, pixel-identical branding."""
import subprocess, os, sys

NAVY, CORAL, MINT, WHITE = "#1B2440", "#FF6B35", "#2EE6A8", "#FFFFFF"
FONT = "../channel-identity/fonts/Anton-Regular.ttf"
BUSTS = "../video-01/busts"
os.makedirs("objects", exist_ok=True)

def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    if r.returncode: print(r.stderr[-800:]); sys.exit(c[:120])

# ---- slice 6x6 objects sheet (2048x2048, 341.33px cells) ----
for i in range(36):
    r, c = divmod(i, 6)
    x, y = round(c*341.33)+10, round(r*341.33)+10
    sh(f"convert _objects-sheet.png -crop 321x321+{x}+{y} +repage -fuzz 5% -transparent white -trim +repage objects/o{i+1:02d}.png")

# rank -> (slug, punch words, bust, text color)
T = {
 1:("creatine-truth","TAKE IT\nRIGHT","shock",WHITE), 2:("quit-sugar","DAY 3:\nHELL","shock",CORAL),
 3:("10k-steps","THE 10K\nLIE","think",WHITE), 4:("protein-needs","TOO\nMUCH?","think",MINT),
 5:("gym-mistakes","YEAR ONE,\nWASTED","shock",CORAL), 6:("sleep-gains","LEGAL\nDOPING","excited",MINT),
 7:("testosterone","4 ARE\nFREE","point",WHITE), 8:("supplement-waste","\\$56\nGONE","shock",CORAL),
 9:("belly-fat","THE REAL\nREASON","think",WHITE), 10:("fasting","MIRACLE\nOR MYTH?","think",MINT),
 11:("preworkout","JUST\nCAFFEINE?","shock",WHITE), 12:("stop-10k","STOP\nCOUNTING","point",CORAL),
 13:("steroid-talk","WHO'S\nLYING?","think",WHITE), 14:("muscle-timeline","MONTH BY\nMONTH","neutral",MINT),
 15:("cardio-vs-weights","HOUR VS\nYEAR","point",WHITE), 16:("anabolic-window","RELAX.","neutral",MINT),
 17:("bulking","FIRST BULK\nRULES","point",CORAL), 18:("first-90-days","DAY 1\nTO 90","excited",WHITE),
 19:("home-vs-gym","SAME\nMUSCLE?","think",MINT), 20:("progressive-overload","ONE\nRULE","point",CORAL),
 21:("newbie-gains","USE IT\nONCE","excited",WHITE), 22:("fasted-cardio","HACK OR\nTRAP?","think",CORAL),
 23:("sets-per-week","12 IS\nENOUGH?","think",WHITE), 24:("stop-lifting","WEEK BY\nWEEK","shock",MINT),
 25:("muscle-memory","IT\nREMEMBERS","excited",WHITE), 26:("gym-anxiety","NOBODY'S\nWATCHING","neutral",MINT),
 27:("cheap-protein","\\$1 = 30G","excited",CORAL), 28:("alcohol-gains","WORTH\nIT?","think",WHITE),
 29:("water-myth","8 IS\nMADE UP","shock",MINT), 30:("posture-fix","UNDO\nTHE DESK","point",WHITE),
 31:("stretching","STOP\nTHIS","point",CORAL), 32:("motivation-systems","SYSTEMS\nWIN","excited",MINT),
 33:("first-pullup","PHASE 1\nOF 4","excited",WHITE),
}

def thumb(fname, obj, words, bust, color):
    sh(f"""convert -size 1280x720 xc:"{NAVY}" \
      -fill none -stroke "{CORAL}" -strokewidth 26 -draw "circle 1050,340 1050,60" \
      -stroke "{MINT}" -strokewidth 12 -draw "circle 160,640 160,600" \
      \\( {BUSTS}/{bust}.png -resize x540 \\) -gravity southeast -geometry +30-10 -composite \
      -stroke none -fill "#27335A" -draw "circle 205,545 205,400" \
      \\( objects/o{obj:02d}.png -resize 270x270 -background none -rotate -8 \\) -gravity southwest -geometry +70+40 -composite \
      -stroke none -fill "{CORAL}" -draw "rectangle 56,50 76,350" \
      -background none -stroke none -fill "{color}" -font {FONT} -size 690x330 -gravity northwest caption:"{words}" -geometry +100+42 -composite \
      "{fname}" """)

for rank,(slug,words,bust,color) in T.items():
    thumb(f"{rank:02d}-{slug}.png", rank, words, bust, color)
# A/B variants for idea #1
thumb("01A-creatine-truth.png", 1, "10 CENT\nSUPERPOWER", "excited", MINT)
thumb("01B-creatine-truth.png", 1, "MYTHS,\nBUSTED", "point", CORAL)

# 168px legibility check sample
sh("convert 01-creatine-truth.png -resize 168x94 _legibility-168px.png")
# contact sheet
files = " ".join(f"{r:02d}-{s}.png" for r,(s,_,_,_) in sorted(T.items())) + " 01A-creatine-truth.png 01B-creatine-truth.png"
sh(f"montage {files} -tile 6x6 -geometry 300x169+4+4 -background '#0e1526' _contact-sheet.png")
print("thumbnails:", len(T)+2)
