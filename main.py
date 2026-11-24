"""One-Line Office Joke: 24-Hour Sprint -- make.fun entry.

One line of at most 200 characters, a joke about office life: the
team stand-up has become a sit-down, a lie-down, and a small,
defeated nap. The program checks the joke, prints it, and writes it
to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

LINE = (
    "Our team stand-up is now a sit-down, a lie-down, and — as of "
    "this morning's calendar invite — a small, defeated nap."
)

LIMIT = 200
TARGET = "/output/entry.txt"


def check_entry(line):
    """Accept exactly one non-blank joke within the limit."""
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if not line or line != line.strip():
        raise ValueError("entry must be a non-blank line")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must fit on a single line")
    if len(line) > LIMIT:
        raise ValueError("entry is %d characters, over the %d limit" % (len(line), LIMIT))
    return line


def write_entry(line):
    """Print the joke and store it in /output/entry.txt."""
    print(line)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def run():
    # Check before writing, so only a well-formed joke is stored.
    write_entry(check_entry(LINE))


if __name__ == "__main__":
    run()
