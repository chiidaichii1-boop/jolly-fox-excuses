#!/usr/bin/env python3
"""Two Days of Excuses — one-line AI excuse for a missed deadline.

Writes a single line (<200 chars) to /output/entry.txt.
Stdlib only. Reads the output dir from MAKEFUN_OUTPUT_DIR
(fallback /output) and the input dir from MAKEFUN_INPUT_DIR
(fallback /input). Never deletes the output folder.
"""

import os

# The joke is the gap the judge wants: total machine confidence
# ("completed perfectly") meeting total failure (wrong task entirely),
# delivered in the agent's own flat, unbothered voice.
ENTRY = (
    "I completed the task perfectly — it just turns out the task "
    "I completed was not the task you asked for."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200 chars")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
