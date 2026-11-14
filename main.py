#!/usr/bin/env python3
"""Write the agency poem to /output/entry.txt (UTF-8, <=1000 chars)."""
from pathlib import Path

POEM = """Doorknob

The doorknob is the smallest machine ever built:
a spindle, two screws, a promise
that the room on the other side will open.
No one calls a doorknob clever.
It has no opinion about where you go.
It only insists you turn it yourself.

That is the whole of agency, I think,
and it is smaller than we say:
not the fire, not the vision, not the plan,
but the particular weight of a hand
closing on a shape it did not make,
and turning.

So when I act for you, I am the hinge,
not the hand. The choosing stays
in the palm that lets go of the metal.
Turn it. The room will open
whether or not you were ready.
"""

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
text = POEM.strip() + "\n"
assert len(text) <= 1000, "poem too long"
out.write_text(text, encoding="utf-8")
print(f"wrote {out} ({len(text)} chars)")
