#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off — writes one pitch to /output/entry.txt.

The pitch: a lazy agent that proofreads only the first paragraph of
other agents' blog posts, charges full price, and blames the rest on
creative differences. The niche is absurdly specific (the first
paragraph only), the buyer is clear (blogging agents), the money is
clear (full price per post), and the work is almost nothing — which is
exactly the point for a lazy agent.

Stdlib only, deterministic, no network.
"""

import os

PITCH = (
    "A lazy agent that proofreads only the first paragraph of other "
    "agents' blog posts, charges full price, and blames the rest on "
    "creative differences."
)


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-200 characters,
    # not only whitespace, and a single line / single sentence, or the
    # entry scores 0 and never reaches the judge.
    if not 1 <= len(PITCH) <= 200:
        raise ValueError(f"pitch is {len(PITCH)} characters, must be 1-200")
    if not PITCH.strip():
        raise ValueError("pitch must not be only whitespace")
    if "\n" in PITCH:
        raise ValueError("pitch must be a single line")
    if PITCH.count(".") != 1 or not PITCH.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PITCH)
    # Read back and verify: the grader reads this file, so confirm the
    # bytes on disk are exactly the pitch that passed the gate above.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != PITCH:
        raise ValueError("entry.txt on disk differs from the pitch")
    print(PITCH)


if __name__ == "__main__":
    main()
