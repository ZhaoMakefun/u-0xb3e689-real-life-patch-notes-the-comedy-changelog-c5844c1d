"""Real-Life Patch Notes: The Comedy Changelog.

Writes one line -- a software patch note for a bug in human biology --
to entry.txt in the output directory.

Usage:
    MAKEFUN_OUTPUT_DIR=/output python3 main.py

The entry is a fixed, deterministic string: no randomness, no network,
no input files. The program validates the line against the bounty gate
(UTF-8 text, 1-160 characters, not only whitespace) before writing it.
"""

import os
import sys

# The entry: a terse release note for a bug every human body ships with.
# The bladder's low-battery warning arrives at 3% and then the whole
# system shuts down -- a recognisable bug, told in dry engineering tone.
ENTRY = (
    "v2.7.3: fixed a bug where the bladder sent its low-battery "
    "warning at 3% and then immediately shut down the whole system."
)

MAX_CHARS = 160


def main() -> int:
    # Gate check, mirroring the bounty rules: 1-160 characters, and
    # the line must carry real content, not only whitespace.
    if not (1 <= len(ENTRY) <= MAX_CHARS):
        print(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    # The entry must be a single line: no embedded newlines.
    if "\n" in ENTRY or "\r" in ENTRY:
        print("entry must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
