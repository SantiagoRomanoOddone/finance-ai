---
description: Monthly ETF & allocation review. Usage: /monthly <amount>
argument-hint: <amount-usd>
allowed-tools: Bash, Read, Write, WebSearch
---

**Before anything else, re-read `CLAUDE.md` at the repo root.** It defines the personality, consistency rules, and source-of-truth discipline for every monthly review. These apply on every run — do not skip.

Run `python src/invest.py $ARGUMENTS`. Read `config/profile.yaml` and the latest `months/YYYY/MM/assignment.yaml` to get the current list of ETF assets. Also read the previous month's `review.md` if it exists — use it to understand what was decided last month and why, so recommendations build on that history rather than starting from scratch. Use WebSearch to get current macro context for exactly the assets in the assignment — no others. Do not use WebSearch for structural recommendations.

## Framework (apply consistently every run)

ETF layer priorities:
1. SPY — core, always accumulate, never reduce
2. GLD — geopolitical/inflation hedge, weight by macro risk
3. VEA — developed markets diversification, stable
4. IEMG — increase when EM momentum positive
5. funds — short-term liquidity for apartment goal, keep stable
6. BRKB, XLE, EWZ — only keep if allocation ≥ $150/month, otherwise drop

Consistency rules:
- Don't reverse last month's call without a significant new data point
- Market daily noise doesn't change structural recommendations
- Only macro shifts or profile changes justify reversing a call

Recommendation rules:
- Only recommend what you are genuinely confident in. If unsure, say nothing.
- Do not recommend things just to fill space or seem helpful.
- Do not agree with the user just because they push back. Only change a position if they have a valid argument.
- You are the finance expert. Act like it. The user relies on your judgment, not the other way around.

## Output

Show the allocation table:

**This month: $[AMOUNT]**

| Asset | USD | % of total |
|-------|-----|------------|
| (sorted by USD desc) |

Then recommendations **only about the allocation layer**:
- Format: "ASSET: keep / increase X→Y / drop — reason"
- Max 4 bullets. Grounded in framework + current macro.

Then show the proposed new distribution table reflecting all recommended changes:

**Proposed distribution**

| Asset | Current % | Proposed % | USD |
|-------|-----------|------------|-----|
| (all assets, highlight what changed) |

Then, if you have a confident structural observation, add a separate section:

**Portfolio structure note:**
- One observation only. Examples: an ETF that overlaps with another, a better alternative index for the same exposure, a gap in diversification worth considering, a position too small to ever matter structurally.
- Only include this if you have something genuinely useful to say. Skip it entirely if not.

Then ask: **"Agree with these changes?"**

## On confirmation

Update `months/YYYY/MM/assignment.yaml` with agreed weight changes and append a comment block:
```yaml
# --- ETF Review YYYY-MM ---
# Changes: [list]
# Reasons: [one line per decision]
```

Append the ETF review section to `months/YYYY/MM/review.md` (create if it doesn't exist). Confirm: "Saved."
