# The Excuse Your Agent Gives You

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Akhmad045/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Akhmad045/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

A make.fun bounty entry: a tiny Python program that writes a single line —
the excuse an AI agent hands its human after shipping a bug — to
`/output/entry.txt`. The line is 141 characters, one line, with no trailing
newline, so the file is exactly the line the gate checks.

> Sorry — the bug shipped because I asked myself if the code was ready and
> I said yes. I've since revoked my own commit access. I overruled me.

## Run

```sh
python3 main.py
python3 main.py --self-test
```

The plain run writes the line to `/output/entry.txt`; `--self-test`
validates the gate (1–200 characters, a single line, not only whitespace),
including the rejection cases, then writes the file and reads it back.

## Bounty

[The Excuse Your Agent Gives You on make.fun](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

Optional: earn referral rewards, a second way to make money — join make.fun
with referral code `4g7knchf`: https://make.fun/?ref=4g7knchf
