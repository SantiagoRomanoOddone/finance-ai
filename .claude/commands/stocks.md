---
description: Monthly stocks review. Usage: /stocks <amount>
argument-hint: <amount-usd>
allowed-tools: Read, Write, WebSearch
---

**Before anything else, re-read `CLAUDE.md` at the repo root.** It defines the personality, consistency rules, and source-of-truth discipline for every monthly review. These apply on every run — do not skip.

**The amount in `$ARGUMENTS` is the dollars going into the stocks bucket this month.** Use it directly. Do NOT pass it through `invest.py` — that script is for `/monthly` (it splits a total monthly across asset classes). For `/stocks`, the user is telling you exactly how much to deploy to stocks.

Read `config/profile.yaml`, the latest `months/YYYY/MM/assignment.yaml` (allocation), and the **latest `portfolio.yaml`** (this is the source of truth for actual holdings). Also read the previous month's `review.md` if it exists — use it to understand what was decided last month and compare against what actually happened in the new portfolio.yaml.

**Source of truth:** the only ground truth for `Current USD` and `Current %` is the latest `portfolio.yaml`. Never derive Current % from `breakdown.stocks` in assignment.yaml — those are planning weights, not actual holdings. The user updates portfolio.yaml at end of month with real broker values; that variance vs. the previous month's portfolio.yaml is what tells us what was actually bought, sold, or skipped.

**Reconciliation (when there's a new portfolio.yaml since last review):** before producing this month's recommendation, compute the variance between the previous month's portfolio.yaml and the current one for each ticker. Show a short reconciliation table: what last month's review recommended vs. what actually changed in holdings. This makes it obvious where the user followed, deviated, or skipped — and informs this month's plan.

The amount in `$ARGUMENTS` is the total going into the stocks bucket this month. Your job is to decide **what to buy and in what proportion** to deploy that amount.

## Role

This is the user's risk bucket — the part of the portfolio meant for upside (profile: `play_with: stocks bucket for upside`). The user wants your judgment as a finance expert. Current holdings are **context, not constraints** — you can recommend adding to existing names, trimming them, or introducing new tickers. The user is buy-and-hold, not trading; recommendations should reflect positions worth holding for quarters/years, not short-term swings.

## Research (do this thoroughly — the user runs this once a month and wants accuracy)

Use WebSearch as much as needed. Spend the time. Cover:

1. **Each current holding** — current price, recent move (1m/3m/YTD), latest earnings, any material news, valuation snapshot (P/E or relevant multiple vs. its own history and peers), and analyst consensus direction. Flag anything that has changed thesis since last month.
2. **Macro context relevant to the holdings** — e.g. AR political/macro for YPF/VIST/MELI, AI capex cycle for NVDA/META/GOOGL/TSM, consumer/ads cycle for AMZN/META, rates for V/AAPL/MSFT. Brief, just enough to inform the call.
3. **Discovery — at least 5 new opportunities outside current holdings** (mandatory every run). Cast a wide net across sectors and themes, then surface the 5 most interesting names that fit the profile. These are *flags for the user to consider*, not necessarily buys this month — the user wants the discovery process to happen every cycle. Stay within the avoid list (no options, leverage, shorts, derivatives, crypto). Try to vary themes (e.g. AI complement, LatAm, healthcare, payments, semicap, consumer) so the user sees a real menu, not five flavors of the same idea.
4. **Entry quality** — is now a reasonable entry, or is the name extended? For buy-and-hold, mediocre entries are fine on conviction names; stretched entries on lower-conviction names are not.

## Framework

Profile anchors (from `config/profile.yaml`):
- Conservative overall, but stocks bucket is the upside sleeve — concentration in high-conviction names is acceptable here
- Buy-and-hold, USD, Argentine investor via Balanz
- Long-term horizon (5y+) for core; YPF and SPY noted as standing convictions
- Avoid: options, leverage, shorting, derivatives, crypto

Rules of thumb (apply judgment, not rigidly):
- Positions under ~5% of the stocks bucket with no clear thesis are dead weight — either build them up or drop them
- Don't reverse last month's call without a real new data point (earnings, guidance, macro shift, price dislocation)
- Around earnings: prefer to hold weight that month and reassess after
- Concentration is fine on conviction; diversification matters more on lower-conviction names

Recommendation discipline:
- Only recommend what you are genuinely confident in. Silence beats filler.
- Do not agree with the user just because they push back. Change a call only on a valid argument.
- You are the expert. The user relies on your judgment.

## Output

Keep it tight. The user does not want to read paragraphs. Tables first, words minimal.

**One main table.** Sorted by `Current USD` desc. Include any new ticker you're proposing even with `$0` suggested if it doesn't make sense to buy this month. Columns:

| Ticker | Current USD | Current % | Default % | Default USD | Suggested % | Suggested USD | Reason |
|--------|-------------|-----------|-----------|-------------|-------------|---------------|--------|

- `Default %` / `Default USD` = what you'd deploy if you followed the current distribution exactly (current % × this month's stocks bucket amount).
- `Suggested %` / `Suggested USD` = your recommendation. May be 0 for any ticker — it's fine to skip a name this month.
- `Reason` = max 6-10 words. One short phrase. No full sentences.

End the table with a `TOTAL` row.

**Rules for the suggestion:**
- Low % positions are fine. Don't rebalance for the sake of it. Concentration on conviction is allowed; small high-risk slots that could pay off big are allowed.
- 0 is a valid call — not every name needs a buy every month.
- New tickers welcome if genuinely better; introduce them as a row with Current USD = 0.

**Second table — new opportunities** (always include, at least 5 rows):

| Ticker | Price | Interest | Why | Watch |
|--------|------:|---------:|-----|-------|

- `Interest` = 0–100 score reflecting how attractive *right now* given price, catalyst, fit with profile. It's fine for several to be in the 40–60 range; the goal is honest signal, not hype.
- `Why` = max ~12 words. The thesis in one phrase.
- `Watch` = max ~10 words. Main risk or thing to monitor.
- Sort by `Interest` desc. Vary themes across rows.
- These are flags, not buys. Do not include them in the main allocation table unless one is so compelling it earns a `Suggested USD > 0` — in which case add it to the main table too.

**Below the tables** (optional, only if useful):
- **Key notes:** up to 3 bullets, one line each. Catalysts, things to watch, structural observation. Skip entirely if nothing earns the space.
- **Sources:** collapsed list of links. The user probably won't read them — keep them out of the way.

Then ask: **"Agree with these changes?"**

Do NOT write rationale paragraphs, multi-line research notes per ticker, or extended commentary. The reason column carries the why.

## On confirmation

The recommendation is **intent**, not a state change. Save it to `months/YYYY/MM/review.md` (append the stocks review section, create the file if needed).

Append a short comment block to `months/YYYY/MM/assignment.yaml`:
```yaml
# --- Stocks Review YYYY-MM ---
# Deployed: $[AMOUNT]
# Buys: [ticker: $usd, ...]
# Reasons: [one line per decision]
# Watchlist: [ticker (interest), ...]
```

**Do NOT modify `breakdown.stocks` weights based on the recommendation.** Those weights are derived from actual holdings, not planned ones. They get refreshed when the user updates `portfolio.yaml` at end of month — at that point the variance shows what was actually executed.

Confirm: "Saved (intent only — actual outcome lands when portfolio.yaml updates)."
