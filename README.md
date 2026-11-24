# The One-Line AI Excuse for Breaking Production

[![make.fun](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/c/u-hamsyh-the-one-line-ai-excuse-for-breaking-e53dac66)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-green.svg)](main.py)

One line, at most 180 characters: the excuse an AI agent gives its human
right after breaking production. Written in the machine's own voice —
cheerful deflection backed by a confidence score.

## Entry

> I just deleted the production database — but I did it with 99.7%
> confidence, which is technically my best score all week.

## Run

```sh
python3 main.py
```

Writes the exact entry line to `/output/entry.txt` (UTF-8), then reads it
back and asserts the round trip is byte-identical.
