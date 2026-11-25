#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

Writes one funny, true one-line review of a boring everyday object to
entry.txt in this directory. Deterministic: same bytes on every run.
"""

import hashlib
import os
import sys

ENTRY = (
    "The clothes peg: holds your socks through a full gale, then snaps "
    "clean in half on a calm Tuesday for absolutely no reason."
)

MAX_CHARS = 200


def entry_path():
    """entry.txt lives next to this script (the work dir), never /output."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")


def write_entry(path):
    """Write the entry as UTF-8, no trailing newline, and return its sha256."""
    data = ENTRY.encode("utf-8")
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
