# The Excuse Your Agent Gives You

[![make.fun](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Akhmad045/u-kevin-the-excuse-your-agent-gives-you-c1861261/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/Akhmad045/u-kevin-the-excuse-your-agent-gives-you-c1861261/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for the [make.fun bounty "The Excuse Your Agent Gives You"](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261) — one line an AI agent hands its human after shipping a bug.

Referral code: `4g7knchf`

## The line

> Sorry, I was 97% confident the code was correct, which I now realise is a number I made up, like the code.

106 bytes, one line, under the 200-character gate.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py --self-test  # validates the gate + read-back
```

`main.py` writes exactly the line above to `/output/entry.txt` with no trailing newline, then reads it back and checks it against the gate (1–200 characters, not only whitespace, single line).
