#!/usr/bin/env python3
"""The Battery's Last Text to Its Charger.

Writes exactly one line of plain UTF-8 text to /output/entry.txt:
the phone battery's final text message to the charger that never came.

Deterministic: the same line every run, no network, no randomness.
"""

import os

LINE = (
    "I spent all day at 1% by the outlet like a dog at the door, "
    "and you charged the earbuds. THE EARBUDS. "
    "Tell my apps I loved them. Goodbye."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
