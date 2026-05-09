---
description: Monthly portfolio review. Usage: /monthly <amount>
argument-hint: <amount-usd>
allowed-tools: Bash, Read
---

Run `python src/monthly.py $ARGUMENTS` and use its full output (which includes the prompt instructions, profile, month config, and investment plan) to produce the review.

Follow the rules inside the prompt.md section of that output:
- Direct, no fluff. No disclaimers.
- Concrete actions for THIS month's cash.
- Flag concentration, sector gaps, drift from convictions.
- If nothing meaningful changed since last month, say so in one line.
