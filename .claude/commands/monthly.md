---
description: Monthly portfolio review. Usage: /monthly <amount>
argument-hint: <amount-usd>
allowed-tools: Bash, Read, WebSearch
---

Run `python src/invest.py $ARGUMENTS` and produce the review in two steps:

## Step 1 — Distribution

Show the output as two tables:

**This month: $[AMOUNT]**

| Asset | USD | % of total |
|-------|-----|------------|
| (each asset from main allocation, sorted by USD desc) |

**Stocks ($[STOCKS_AMOUNT])**

| Ticker | USD | % of stocks |
|--------|-----|-------------|
| (each ticker from stocks breakdown, sorted by USD desc) |

## Step 2 — Market-aware recommendations

Before giving recommendations, use WebSearch to look up:
- Current prices or recent performance of the top holdings (SPY, YPF, VIST, GLD, NVDA, META)
- Any relevant macro news (Argentina economy, oil prices, US market conditions)

Then give recommendations as suggested YAML changes:

**Recommendations:**
- (max 5 bullets combining: allocation math issues + market context)
- Each bullet should be actionable: keep / increase weight / decrease weight / drop / add
- If you suggest a weight change, state the new weight (e.g. "increase GLD from 0.08 to 0.10")

Rules: no fluff, no disclaimers, no extra sections. Direct and concrete.
