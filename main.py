"""Two-sentence horror story entry for the make.fun bounty.

Writes the story to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)
as bytes, with no trailing newline, on a single line.
"""

import os

LINE = (
    "I finally found the courage to look under my bed after months of "
    "hearing the scratching, and the claw marks were on the underside of "
    "the mattress. That is when I realized the thing had been sleeping "
    "right above me, pressed against the springs, waiting for me to fall "
    "asleep first."
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
