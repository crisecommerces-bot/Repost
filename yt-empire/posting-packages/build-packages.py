#!/usr/bin/env python3
"""Generate 33 posting packages + _master.csv for HonestReps."""
import csv, os

DISCLOSURE = "Some links are affiliate links - I may earn a commission at no extra cost to you."
LINK = "{{AFFILIATE_LINK}}"

# rank: (slug, title<=60, keyword, hook, topic body (~60-80w), [tag extras], planned chapters)
D = {
1:("creatine-truth","What Creatine ACTUALLY Does to Your Body","what does creatine do",
   "The most studied supplement on Earth - and most people still take it wrong.",
   "This animated breakdown shows what creatine does day by day: the ATP energy system, the week-one water jump (why it is NOT fat), when the extra reps arrive, and the kidney, hair-loss and bloating myths measured against 30 years of research. Plus the 8-week test that tells you if you are one of the people creatine barely works for, and the right dose of creatine monohydrate.",
   ["creatine","creatine monohydrate","creatine side effects","creatine before and after","does creatine cause hair loss"],
   [("0:00","The 10-cent edge"),("1:32","What actually happens, week by week"),("3:37","How to take it (and who it fails)")]),
2:("quit-sugar","Quit Sugar for 30 Days: What Really Happens","quit sugar 30 days",
   "Day 3 is the worst day of your life. Day 30 rewires your cravings.",
   "An animated 30-day timeline of quitting sugar: withdrawal and the day-3 crash, when energy stabilizes, how taste buds recalibrate, what happens to body fat and focus, and the realistic way to keep the results without going monk-mode forever.",
   ["quit sugar","sugar detox","no sugar 30 days","sugar withdrawal symptoms"],
   [("0:00","The day-3 crash"),("1:40","Week 2: the flip"),("3:40","Keeping it off")]),
3:("10k-steps","Walking 10,000 Steps a Day: What Actually Happens","walking 10000 steps benefits",
   "The 10,000 number was invented by a 1965 marketing team - but walking still works.",
   "Where the 10,000-step myth came from, what daily walking actually does to fat loss, blood pressure, joints and mood, the real step targets research supports, and how to make steps automatic instead of another chore.",
   ["10000 steps","walking for weight loss","how many steps a day","walking benefits"],
   [("0:00","The marketing myth"),("1:40","What walking really does"),("3:40","Your real target")]),
4:("protein-needs","How Much Protein You REALLY Need (Not What They Say)","how much protein to build muscle",
   "The supplement industry needs you to overshoot your protein. The science says something cheaper.",
   "The grams-per-kilo targets that research actually supports, why more is not better past a point, what that looks like on a normal plate of food, and when protein powder genuinely helps versus when it is just expensive milk.",
   ["protein","how much protein","protein to build muscle","high protein diet"],
   [("0:00","The overshoot industry"),("1:40","Your real number"),("3:40","Food first, powder second")]),
5:("gym-mistakes","10 Gym Mistakes That Waste Your First Year","beginner gym mistakes",
   "Most beginners burn 12 months on mistake #3 alone.",
   "The ten mistakes that quietly erase beginner progress: program hopping, ego lifting, junk volume, skipping progressive overload, under-eating, and more - each with the 10-second fix that would have saved me a year.",
   ["gym mistakes","beginner gym tips","workout mistakes","how to start gym"],
   [("0:00","Mistakes 1-3"),("1:40","Mistakes 4-7"),("3:40","The one that costs a year")]),
6:("sleep-gains","Sleep: The Muscle Drug Nobody Takes","sleep muscle growth",
   "There is a legal performance enhancer that beats any supplement - and you keep skipping the dose.",
   "How sleep drives muscle growth: growth hormone release, cortisol control, recovery and appetite hormones - what one bad night really costs, and a simple evening protocol that upgrades every set you do in the gym.",
   ["sleep and muscle growth","sleep recovery","how sleep affects gains","deep sleep"],
   [("0:00","The legal enhancer"),("1:40","What one bad night costs"),("3:40","The protocol")]),
7:("testosterone","How to Raise Testosterone Naturally (What Works)","increase testosterone naturally",
   "Five levers move your testosterone. Four are free. None are in a bottle.",
   "The natural testosterone levers ranked by effect size - sleep, body fat, lifting, diet basics and stress - what the research says each is worth, and why most testosterone booster supplements fail the evidence test.",
   ["testosterone","increase testosterone naturally","low testosterone","testosterone booster truth"],
   [("0:00","The 5 levers"),("1:40","Ranked by effect"),("3:40","The bottle trap")]),
8:("supplement-waste","4 Supplements That Are a Complete Waste of Money","supplements waste of money",
   "The average gym member burns $56 a month on powders that do nothing.",
   "Four popular supplements the evidence does not support, why they keep selling anyway, the marketing tricks on the label, and the short list of things that actually earn a place on your shelf.",
   ["supplements","bcaa","supplement industry","waste of money supplements"],
   [("0:00","The $56 leak"),("1:40","The four offenders"),("3:40","What to buy instead")]),
9:("belly-fat","Why Your Belly Fat Won't Go Away","lose belly fat",
   "You can't spot-reduce it. But you can out-math it.",
   "Why belly fat is last to leave, what actually controls fat loss (and what doesn't), the role of sleep and stress, and a simple weekly equation that makes the mirror move without crash diets or 6am cardio punishment.",
   ["belly fat","lose belly fat","stubborn fat","fat loss explained"],
   [("0:00","Why it's last to go"),("1:40","The real equation"),("3:40","Your weekly plan")]),
10:("fasting","Intermittent Fasting: Miracle or Marketing?","intermittent fasting explained",
   "Fasting videos have 68 million views. Most get the mechanism wrong.",
   "What intermittent fasting actually does, why most of its magic is a calorie deficit in disguise, who genuinely benefits from eating windows, who should skip it, and how to test it on yourself properly.",
   ["intermittent fasting","fasting explained","16 8 fasting","does fasting work"],
   [("0:00","The 68-million-view claim"),("1:40","What IF really does"),("3:40","Who should skip it")]),
11:("preworkout","The Truth About Pre-Workout (Before You Buy)","is pre workout worth it",
   "That tingle isn't power - it's a skin reaction.",
   "Ingredient-by-ingredient verdicts on pre-workout: what caffeine is worth, what the tingles actually are, which ingredients are underdosed window dressing, and the cheap alternative that covers 90% of the benefit.",
   ["pre workout","pre workout side effects","caffeine workout","pre workout worth it"],
   [("0:00","The tingle lie"),("1:40","Ingredient verdicts"),("3:40","The 90% alternative")]),
12:("stop-10k","Stop Chasing 10,000 Steps (Do This Instead)","how many steps a day",
   "Step quality beats step count - here's the upgrade.",
   "Why raw step counts mislead, what zone-2 walking pace does that shuffling doesn't, how to distribute steps across the day for blood sugar control, and the walking upgrade that fits inside your existing schedule.",
   ["steps per day","zone 2 cardio","walking workout","step count myth"],
   [("0:00","The count trap"),("1:40","Quality over quantity"),("3:40","The upgrade")]),
13:("steroid-talk","The Steroid Talk Every Beginner Deserves","fake natty explained",
   "Half your fitness heroes are lying to you.",
   "An honest education video (not a how-to): how common enhancement really is, why fake natties distort your expectations, what natural progress actually looks like year by year, and how to set goals your body can keep.",
   ["fake natty","steroids in fitness","natural bodybuilding","realistic gains"],
   [("0:00","The open secret"),("1:40","What natural looks like"),("3:40","Setting real goals")]),
14:("muscle-timeline","How Long Building Muscle REALLY Takes","how long to build muscle",
   "Your honest month-by-month muscle timeline - no transformation-industry lies.",
   "What you can gain in month one, month six, year one and year three, why the scale lies early on, the newbie-gains window, and the checkpoints that tell you your program is working before the mirror does.",
   ["build muscle","muscle growth timeline","how long to build muscle","noob gains"],
   [("0:00","Month 1-3"),("1:40","Year one honest math"),("3:40","The long game")]),
15:("cardio-vs-weights","Cardio vs Weights: What Burns Fat Faster?","cardio vs weights fat loss",
   "One burns more per hour. The other burns more per year.",
   "The per-session versus per-year fat loss math, how muscle changes your resting burn, what EPOC is really worth, and the hybrid weekly split that beats both extremes for body composition.",
   ["cardio vs weights","fat loss workout","burn fat","lifting for fat loss"],
   [("0:00","Per hour vs per year"),("1:40","The muscle multiplier"),("3:40","The hybrid split")]),
16:("anabolic-window","The Anabolic Window Is (Mostly) a Myth","anabolic window myth",
   "You don't need protein in 30 minutes. You need this instead.",
   "Where the post-workout panic came from, what protein timing research actually shows, the cases where timing does matter a little, and the daily habits that out-earn any shaker-bottle sprint.",
   ["anabolic window","protein timing","post workout meal","nutrient timing"],
   [("0:00","The 30-minute panic"),("1:40","What studies show"),("3:40","What matters instead")]),
17:("bulking","Bulking & Cutting Explained (Don't Ruin Your First Bulk)","bulking for beginners",
   "Your first bulk decides your next two years.",
   "Surplus math without the dirty-bulk trap, how fast to gain, when to stop, how cutting actually works after, and the body-fat guardrails that keep a bulk from becoming just... getting fat.",
   ["bulking","cutting","first bulk","lean bulk"],
   [("0:00","Surplus math"),("1:40","The dirty-bulk trap"),("3:40","When to stop")]),
18:("first-90-days","Your First 90 Days in the Gym (Complete Roadmap)","beginner gym guide",
   "If I started over today, this is the exact 90-day plan I'd run.",
   "Week-by-week: what to train, how to learn form without embarrassment, when to add weight, what to eat without tracking everything, and the habit architecture that makes month three automatic.",
   ["beginner gym guide","first time gym","90 day plan","gym for beginners"],
   [("0:00","Weeks 1-4"),("1:40","Weeks 5-8"),("3:40","Weeks 9-12")]),
19:("home-vs-gym","Home Workouts vs Gym: What Science Says","home workout vs gym",
   "Your muscles can't read the sign on the door.",
   "What actually drives growth (tension, effort, progression) and how to get it at home, where home setups genuinely fall short, and the minimal equipment that closes 90% of the gap.",
   ["home workout","home gym","gym vs home","train at home"],
   [("0:00","What muscle needs"),("1:40","Where home falls short"),("3:40","Closing the gap")]),
20:("progressive-overload","Progressive Overload: The Only Rule That Matters","progressive overload explained",
   "If the bar isn't moving up, nothing else counts.",
   "The adaptation ladder explained simply, five ways to overload beyond adding weight, how to log it in 20 seconds a set, and the plateau checklist for when the bar stops moving.",
   ["progressive overload","strength progress","training plateau","how to get stronger"],
   [("0:00","The ladder"),("1:40","5 ways to overload"),("3:40","Plateau checklist")]),
21:("newbie-gains","Newbie Gains: Your One-Time Superpower","newbie gains",
   "You get this superpower exactly once. Most people waste it.",
   "Why your first year can produce double the muscle of any year after, the mechanisms behind newbie gains, and how to cash the window with simple programming instead of wasting it on confusion.",
   ["newbie gains","first year gym","beginner muscle growth","noob gains explained"],
   [("0:00","The one-time window"),("1:40","Why it works"),("3:40","Cash it properly")]),
22:("fasted-cardio","Fasted Cardio: Fat-Burning Hack or Myth?","fasted cardio",
   "Burning fat during a workout isn't the same as losing fat.",
   "The substrate-use trap explained with simple animation, what 24-hour energy balance says about fasted sessions, who might still like training fasted, and what actually decides fat loss.",
   ["fasted cardio","fat burning zone","cardio on empty stomach","fat loss myths"],
   [("0:00","The trap"),("1:40","24-hour math"),("3:40","Who it suits")]),
23:("sets-per-week","How Many Sets Do You Actually Need?","how many sets per week",
   "More sets stopped working for you around number twelve.",
   "Volume landmarks made visual: minimum effective volume, the sweet spot per muscle per week, junk volume, and how to count sets honestly so your program stops lying to you.",
   ["training volume","sets per week","how many sets","hypertrophy volume"],
   [("0:00","The sweet spot"),("1:40","Junk volume"),("3:40","Count honestly")]),
24:("stop-lifting","What Happens When You Stop Lifting","muscle loss stop lifting",
   "Week by week - what detraining really takes from you (and what it doesn't).",
   "The honest detraining timeline: what fades in two weeks, what holds for months, why size returns faster than you fear, and the minimum dose that preserves nearly everything during busy seasons.",
   ["detraining","stop lifting","muscle loss","maintain muscle"],
   [("0:00","Weeks 1-2"),("1:40","Months 1-3"),("3:40","The minimum dose")]),
25:("muscle-memory","Muscle Memory Is Real: The Comeback Science","muscle memory",
   "Your muscles keep receipts.",
   "Myonuclei and why trained muscle rebuilds faster, what the comeback timeline looks like after months or years off, and how to restart without injuring the ego or the joints.",
   ["muscle memory","comeback gym","regain muscle","myonuclei"],
   [("0:00","The receipts"),("1:40","Comeback timeline"),("3:40","Restart protocol")]),
26:("gym-anxiety","Gym Anxiety: The Beginner's Cheat Code","gym anxiety",
   "Everyone is too busy watching themselves to watch you.",
   "The psychology of gym anxiety, the off-peak and layout tricks that make week one painless, scripts for common awkward moments, and how confidence actually compounds after ten visits.",
   ["gym anxiety","gym confidence","first gym visit","gym for beginners"],
   [("0:00","Nobody's watching"),("1:40","The cheat codes"),("3:40","Visit ten")]),
27:("cheap-protein","The Cheapest High-Protein Foods (Budget Gains)","cheap protein foods",
   "A dollar can buy 30 grams of protein - if you know where to look.",
   "The dollars-per-30g protein league table: eggs, dairy, legumes, canned fish and the freezer aisle - plus three lazy high-protein meals that cost less than a supplement scoop.",
   ["cheap protein","high protein foods","budget meal prep","protein on a budget"],
   [("0:00","The league table"),("1:40","Top 5 picks"),("3:40","3 lazy meals")]),
28:("alcohol-gains","Alcohol & Gains: The Honest Math","alcohol muscle growth",
   "Nobody's telling you to quit. Here's what a night out actually costs.",
   "What alcohol does to muscle protein synthesis, sleep and recovery, how much a weekend really sets you back, and the damage-control playbook for drinking without deleting your progress.",
   ["alcohol and gains","alcohol muscle","drinking and fitness","alcohol recovery"],
   [("0:00","The real cost"),("1:40","MPS and sleep"),("3:40","Damage control")]),
29:("water-myth","How Much Water You Actually Need","how much water per day",
   "The 8-glasses rule was never science.",
   "Where the eight-glasses myth came from, how thirst and urine color actually regulate you, when athletes genuinely need more, and the electrolyte piece everyone ignores.",
   ["water intake","how much water","hydration","8 glasses myth"],
   [("0:00","The made-up rule"),("1:40","Your real signal"),("3:40","Electrolytes")]),
30:("posture-fix","Desk Body Rescue: Fix Your Posture","fix posture exercises",
   "Your chair is programming your spine. Here's the undo button.",
   "The desk-posture chain reaction explained visually, five exercises that reverse it in ten minutes a day, and the workstation tweaks that stop re-breaking what you just fixed.",
   ["posture","fix posture","desk posture","posture exercises"],
   [("0:00","The chain reaction"),("1:40","The 10-minute undo"),("3:40","Desk tweaks")]),
31:("stretching","Stop Static Stretching Before Lifting","stretching before workout",
   "That pre-lift stretch routine might be costing you strength.",
   "What static stretching does to force output, what dynamic warm-ups do instead, the two-minute warm-up template, and where static stretching still belongs in your week.",
   ["stretching","warm up","static stretching","dynamic warm up"],
   [("0:00","The strength leak"),("1:40","Dynamic instead"),("3:40","Where static fits")]),
32:("motivation-systems","Why Motivation Fails (Build Systems Instead)","gym motivation",
   "Motivation is a battery. Systems are a power grid.",
   "Why willpower predictably runs out, the habit loops that make training automatic, environment design for lifters, and the two-day rule that has saved more physiques than any pre-workout.",
   ["gym motivation","fitness habits","consistency","discipline"],
   [("0:00","The battery problem"),("1:40","Habit loops"),("3:40","The two-day rule")]),
33:("first-pullup","Your First Pull-Up: The 4-Phase Plan","first pull up progression",
   "From zero to chin-over-bar in four phases.",
   "Dead hangs, negatives, band work and rep one - exactly how long each phase takes, the strength standards to move on, and the plateau fixes for the last stubborn inch.",
   ["pull up","first pull up","pull up progression","calisthenics beginner"],
   [("0:00","Phase 1-2"),("1:40","Phase 3"),("3:40","Rep one")]),
}

BASE_TAGS = ["honestreps","fitness explained","animated fitness","science based fitness","gym advice","fitness for beginners","no bs fitness"]

rows = []
for rank in sorted(D):
    slug, title, kw, hook, body, extra, chaps = D[rank]
    tags = []
    for t in [kw] + extra + BASE_TAGS:
        if t not in tags: tags.append(t)
    while sum(len(t)+1 for t in tags) > 480: tags.pop()
    chap_lines = "\n".join(f"{ts} {name}" for ts, name in chaps)
    planned = "" if rank == 1 else " (planned - update after final edit)"
    desc = f"""{hook}

My #1 tool for training consistency (the smart home gym I use): {LINK}
{DISCLOSURE}

{body}

Rep is the honest animated coach: science-based fitness with zero bro-science, built for beginners and busy lifters who want the truth about training.

Chapters{planned}:
{chap_lines}

#fitness #{max(kw.split(), key=len)} #animated"""
    pinned = f"Rep here. The exact home-gym setup I mention in the video is here: {LINK} - and I answer every question in the comments for the first 48 hours. What's YOUR experience with {max(kw.split(), key=len)}? Anything I got wrong? Tell me straight."
    header = "# READY TO POST - video is produced, thumbnail 01 (A/B: 01A, 01B)\n\n" if rank == 1 else ""
    md = f"""{header}# {rank:02d} - {title}

**Title (<=60 chars):** {title}

**Description:**
```
{desc}
```

**Tags ({len(tags)}, {sum(len(t)+1 for t in tags)} chars):** {", ".join(tags)}

**Pinned comment:**
```
{pinned}
```

**Thumbnail:** `thumbnails/{rank:02d}-{slug}.png`{' (variants: 01A, 01B for A/B test)' if rank==1 else ''}
"""
    open(f"{rank:02d}-{slug}.md","w").write(md)
    rows.append([rank, title, desc.replace("\n"," / "), ", ".join(tags)])

with open("_master.csv","w",newline="") as f:
    w = csv.writer(f); w.writerow(["rank","title","description","tags"]); w.writerows(rows)
print("packages:", len(rows))
