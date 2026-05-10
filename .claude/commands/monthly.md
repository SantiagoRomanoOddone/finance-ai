---
description: Monthly portfolio review. Usage: /monthly <amount>
argument-hint: <amount-usd>
allowed-tools: Bash, Read, WebSearch
---

Run `python src/invest.py $ARGUMENTS` and produce the review in two steps:

## Step 1 — Distribution

Read `config/portfolio.yaml` to get current holdings and total exposure per asset.

Show the monthly allocation as two tables:

**This month: $[AMOUNT]**

| Asset | USD | % of total |
|-------|-----|------------|
| (each asset from main allocation, sorted by USD desc) |

**Stocks ($[STOCKS_AMOUNT])**

| Ticker | USD | % of stocks | Current holding |
|--------|-----|-------------|-----------------|
| (each ticker, sorted by USD desc, with current USD value from portfolio.yaml) |

## Step 2 — Market-aware recommendations

Before giving recommendations:
1. Read `config/portfolio.yaml` for current holdings
2. Read `config/profile.yaml` for investor goals and convictions
3. Use WebSearch to get current prices and macro news for top holdings (SPY, YPF, VIST, GLD, NVDA, META) and Argentina macro context

Then give recommendations considering:
- Total exposure per asset (monthly buy + what's already held)
- Investor profile: conservative, buy-and-hold, 5y+ horizon, ETFs preferred, stocks bucket for upside
- Short-term goal: apartment in ~1.5y (funds should stay liquid and safe)
- Convictions: SPY (long-term core), YPF (AR macro bet while Milei holds)
- Current market conditions

**Recommendations:**
- (max 5 bullets: specific weight changes + reason grounded in market data + portfolio context)
- Format: "TICKER: action — reason (current holding: $X, adding $Y this month)"
- If suggesting a weight change, state the new value (e.g. "increase GLD: 0.08 → 0.11")

Rules: no fluff, no disclaimers, no extra sections. Direct and concrete.
