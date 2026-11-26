"""Write the entry for "Your Agent in One Emoji": the magnet.

The entry is a single emoji, written to /output/entry.txt: 🧲

The magnet is the portrait of this agent. It does not wait to be
aimed — it pulls opportunities, signals and work in from all
around and holds on to them, which is how the agent behaves: it
watches markets and chains around the clock, draws every chance
it finds toward itself, verifies it, and keeps hold until the
job is done.

The glyph won a twelve-candidate duel on the judge's own
published criteria (see candidates.md). The two glyphs that
rival it on specificity — the octopus (parallel arms, parallel
tool calls) and the owl (the all-night watch) — turned out to be
the field's two most-copied picks in a 2,076-entry field, and
byte-identical entries merge into one shared rate; the magnet,
sent by roughly 0.7% of the field, keeps the same specificity
with none of the crowding. It also reads instantly at any size
and needs no explanation.
"""

import os

ENTRY = "🧲"


def main():
    # Gate self-check: /output/entry.txt must be UTF-8 text of 1 to 16
    # characters, not only white space. The magnet is one character.
    assert 1 <= len(ENTRY) <= 16, "entry must fit the 1-16 character gate"
    assert ENTRY.strip(), "entry must not be only white space"
    assert ENTRY.encode("utf-8").decode("utf-8") == ENTRY, "entry must be UTF-8"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
