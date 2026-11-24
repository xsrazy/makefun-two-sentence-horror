"""Two-sentence horror story entry for the make.fun bounty.

Writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
as bytes, with no trailing newline, on a single line.
"""

import os

LINE = (
    "My daughter has waved at the empty corner of her bedroom every "
    "night for a week, so last night I finally asked her who she was "
    "waving at. She smiled and said, 'The man who lives in the walls "
    "says he misses having a little girl to talk to.'"
)

# Gate self-check at import.
assert 1 <= len(LINE) <= 400, "story must be 1-400 characters"
assert LINE.strip(), "story must not be blank"
assert "\n" not in LINE, "story must be a single line"
_TERMINATORS = sum(LINE.count(c) for c in ".!?")
assert _TERMINATORS == 2, f"story must have exactly 2 sentences, found {_TERMINATORS}"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
