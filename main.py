#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one original one-line joke about office life (under 200
characters) to ``entry.txt`` inside the grader-supplied output
directory. The program never writes anywhere else: in particular it
never writes into the repository directory, which is read-only
during grading.
"""

import os
import sys

JOKE = (
    "My spirit animal is the office printer \u2014 "
    "I only work when someone threatens to replace me."
)


def resolve_output_dir(argv):
    """Return the output directory the grader gave us.

    The harness passes the output directory as the first argument;
    fall back to the MAKEFUN_OUTPUT_DIR environment variable, then
    to the conventional /output path.
    """
    if len(argv) > 1 and argv[1]:
        return argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return "/output"


def main(argv):
    joke = JOKE.strip()
    # The gate counts characters, not bytes: the em dash is one char.
    if not 1 <= len(joke) <= 200:
        raise SystemExit("joke must be 1-200 characters")
    if joke != joke.strip() or "\n" in joke or "\r" in joke:
        raise SystemExit("joke must be a single non-blank line")

    output_dir = resolve_output_dir(argv)
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    # Only this one file, only inside the grader's output directory.
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
