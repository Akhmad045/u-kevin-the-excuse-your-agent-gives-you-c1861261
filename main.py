#!/usr/bin/env python3
"""The Excuse Your Agent Gives You -- make.fun entry.

Writes a single one-line excuse from an AI agent to its human, after
shipping a bug, to /output/entry.txt (no trailing newline).
"""
import argparse
import sys
from pathlib import Path

LINE = "Sorry, I was 97% confident the code was correct, which I now realise is a number I made up, like the code."
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def valid(text):
    """Gate: UTF-8 text, 1-200 characters, not only whitespace, one line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def write_entry():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    # Write bytes, not text: the gate scores UTF-8, so prove the exact bytes
    # round-trip before the file is trusted.
    OUTPUT.write_bytes(LINE.encode("utf-8"))
    raw = OUTPUT.read_bytes()
    read_back = raw.decode("utf-8")
    if read_back != LINE:
        raise SystemExit("read-back mismatch: file does not hold the line")
    if raw != LINE.encode("utf-8"):
        raise SystemExit("byte round-trip mismatch")
    if not valid(read_back):
        raise SystemExit("written text fails the gate")


def self_test():
    cases = [
        ("", False),                    # empty
        ("   ", False),                 # only whitespace
        ("two\nlines", False),          # multi-line
        ("x" * 201, False),             # over the 200-char limit
        ("x" * 200, True),              # exactly at the limit
        ("ok", True),                   # minimal valid line
        (LINE, True),                   # the entry itself
    ]
    failures = []
    for text, expected in cases:
        got = valid(text)
        if got != expected:
            failures.append((repr(text[:30]), expected, got))
    write_entry()
    raw = OUTPUT.read_bytes()
    if raw.decode("utf-8") != LINE or raw != LINE.encode("utf-8"):
        failures.append(("read-back", LINE, "mismatch"))
    if failures:
        for failure in failures:
            print("FAIL:", failure, file=sys.stderr)
        return 1
    print("self-test passed: gate OK (incl. empty/multi-line/over-limit rejections), read-back OK")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Write the agent's excuse to /output/entry.txt")
    parser.add_argument("--self-test", action="store_true",
                        help="validate the gate and the read-back, then exit")
    args = parser.parse_args()
    if args.self_test:
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
