#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of a boring everyday object to
/output/entry.txt ONLY. The grade sandbox mounts the repo read-only
and provides /output as the writable directory; the gate reads
/output/entry.txt. Writing beside __file__ fails there (the open
raises, the program exits 1, run_completes fails), so this program
never writes anywhere else. Deterministic: same bytes on every run.
"""

import hashlib
import os
import sys

ENTRY = (
    "The clothes peg: holds your socks through a full gale, then snaps "
    "clean in half on a calm Tuesday for absolutely no reason."
)

MAX_CHARS = 200

# The grade sandbox's writable directory; the gate reads this file.
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def entry_path():
    """Deterministic output location: /output/entry.txt."""
    return OUTPUT_PATH


def write_entry(path):
    """Write the entry as UTF-8, no trailing newline, and return its sha256."""
    data = ENTRY.encode("utf-8")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)
    return hashlib.sha256(data).hexdigest()


def validate(text):
    """Gate mirror: 1-200 chars, single line, not only whitespace."""
    if not text or not text.strip():
        raise ValueError("entry is empty")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    return True


def main():
    validate(ENTRY)
    path = entry_path()
    digest = write_entry(path)
    print(f"wrote {path} ({len(ENTRY)} chars, sha256 {digest})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
