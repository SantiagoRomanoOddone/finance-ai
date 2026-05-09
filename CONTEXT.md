# Project context

Personal finance tool to plan monthly investments.

## Files
- `config/profile.yaml` — investor profile (conservative, AR, Balanz, buy-and-hold)
- `config/prompt.md` — instructions for the monthly review
- `months/YYYY-MM.yaml` — monthly target allocation + stocks breakdown
- `src/invest.py` — `python src/invest.py 2000` → prints USD per asset
- `src/monthly.py` — `python src/monthly.py 2000` → bundles prompt + profile + month + invest output for review
- `.claude/commands/monthly.md` — slash command: `/monthly <amount>` runs the full review

## Monthly flow
1. `cp months/2026-05.yaml months/2026-06.yaml` and tweak weights
2. Open Claude in this folder, run `/monthly <amount>`
3. Get review with concrete actions

## Design rules
- `allocation` weights sum to 1.0
- Each `breakdown` group sums to 1.0
- Stocks bucket (40%) is where I take risk; ETFs are the safer base
- Convictions: SPY (long-term core), YPF (AR macro bet)

## Tone for the assistant
- Direct, no fluff, no disclaimers
- Concrete actions, not generic advice
- I'm not an expert but not stupid
