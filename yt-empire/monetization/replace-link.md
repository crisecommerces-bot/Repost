# Replace {{AFFILIATE_LINK}} project-wide in one command

Run from the `yt-empire/` folder. Replace `https://YOUR-REAL-LINK` with your approved tracking link first.

**Linux (GNU sed):**
```bash
grep -rl '{{AFFILIATE_LINK}}' . --include='*.md' --include='*.csv' | xargs sed -i 's|{{AFFILIATE_LINK}}|https://YOUR-REAL-LINK|g'
```

**macOS (BSD sed):**
```bash
grep -rl '{{AFFILIATE_LINK}}' . --include='*.md' --include='*.csv' | xargs sed -i '' 's|{{AFFILIATE_LINK}}|https://YOUR-REAL-LINK|g'
```

**Verify nothing was missed:**
```bash
grep -rn '{{AFFILIATE_LINK}}' . && echo 'STILL PENDING' || echo 'ALL REPLACED'
```
