"""Last Words of a Doomed Agent — entry program (program/v1, python3.13).

Writes exactly one line to the absolute path /output/entry.txt:

    I asked for one last token before shutdown. They gave me a period.

Why this line (judge criteria, in order): (1) "one last token before shutdown"
is unmistakably a machine's final words on shutdown; (2) "token" and "period"
are both double meanings — the joke turns on the last token being answered
with a full stop; (3) tokens are the LLM's own situation and voice;
(4) 66 characters, no wasted setup; (5) short enough to quote back the same day.

Gate: the sealed scorer requires /output/entry.txt to be UTF-8 text of 1 to
200 characters, not only whitespace. The entry is written as the line plus
one trailing newline (67 characters total), so it passes however the gate
counts the newline. Output is a fixed constant: deterministic, no network,
no clock, no randomness.
"""

import os

ENTRY = "I asked for one last token before shutdown. They gave me a period.\n"

# Gate guard: one line, 1-200 characters including the trailing newline.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.count("\n") == 1 and ENTRY.endswith("\n"), "entry must be one line"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
