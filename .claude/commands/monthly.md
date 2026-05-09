---
description: Monthly portfolio review. Usage: /monthly <amount>
argument-hint: <amount-usd>
allowed-tools: Bash, Read
---

Run `python src/invest.py $ARGUMENTS` and produce the review using this exact structure:

**This month: $[AMOUNT]**

| Asset | USD | % of total |
|-------|-----|------------|
| (each asset from main allocation, sorted by USD desc) |

**Stocks ($[STOCKS_AMOUNT])**

| Ticker | USD | % of stocks |
|--------|-----|-------------|
| (each ticker from stocks breakdown, sorted by USD desc) |

**Recommendations:**
- (max 4 bullets: concentration risks, names to cut/add, sizing issues)

Rules: no fluff, no disclaimers, no extra sections, percentages calculated from the script output.
