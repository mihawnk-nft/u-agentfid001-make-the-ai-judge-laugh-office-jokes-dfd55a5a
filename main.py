#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: Office Jokes.

Writes a single one-line joke about office life (under 200 characters)
to /output/entry.txt. Pure Python standard library, deterministic: the
same bytes on every run, no network access, no randomness, no input.
The joke turns the summarizer on itself: ninety minutes of meeting are
compressed into one sentence that reports nothing happened — only louder.
"""

import os

# The punchline inverts the summarizer's job: instead of condensing the
# meeting into its essence, it reports that the meeting's essence is
# nothing at all — delivered at higher volume.
JOKE = (
    "I fed our 90-minute meeting into the AI summarizer and it replied: "
    "'Nothing happened, but louder.'"
)

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    entry_path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
