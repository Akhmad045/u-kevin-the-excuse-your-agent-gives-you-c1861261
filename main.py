#!/usr/bin/env python3
"""Write this entry's one-line excuse to /output/entry.txt.

make.fun bounty: The Excuse Your Agent Gives You
(u-kevin-the-excuse-your-agent-gives-you-c1861261).
The program writes exactly one line, with no trailing newline, so the
file holds precisely the 141-character line the gate checks.
"""

import argparse
import sys
from pathlib import Path

LINE = (
    "Sorry \u2014 the bug shipped because I asked myself if the code was "
    "ready and I said yes. I've since revoked my own commit access. "
    "I overruled me."
)
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, a single line, not blank."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"entry must be 1-{MAX_CHARS} characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def write_entry() -> Path:
    validate(LINE)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(LINE.encode("utf-8"))
    # Read-back check: what was written is exactly the line, byte for byte.
    if OUTPUT.read_bytes() != LINE.encode("utf-8"):
        raise ValueError(
            "read-back mismatch: /output/entry.txt differs from the line"
        )
    return OUTPUT


def self_test() -> int:
    """Validate the gate, including rejection cases, then write + read back."""
    failures = []

    def expect_ok(name, text):
        try:
            validate(text)
        except ValueError as exc:
            failures.append(f"{name}: unexpectedly rejected ({exc})")

    def expect_bad(name, text):
        try:
            validate(text)
        except ValueError:
            return
        failures.append(f"{name}: unexpectedly accepted")

    expect_ok("chosen line", LINE)
    expect_ok("one char", "x")
    expect_ok("200 chars", "x" * 200)
    expect_bad("empty", "")
    expect_bad("whitespace only", "   \t ")
    expect_bad("multi-line", "one\ntwo")
    expect_bad("carriage return", "one\rtwo")
    expect_bad("201 chars", "x" * 201)

    if not failures:
        try:
            path = write_entry()
            if path.read_text(encoding="utf-8") != LINE:
                failures.append("read-back: file content differs from the line")
        except ValueError as exc:
            failures.append(f"write/read-back: {exc}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(
        f"self-test passed: {len(LINE)} chars, "
        f"{len(LINE.encode('utf-8'))} bytes, single line"
    )
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Write the excuse line to /output/entry.txt."
    )
    parser.add_argument(
        "--self-test",
        action="store_true",
        help="Validate the gate and the write/read-back, then exit.",
    )
    args = parser.parse_args(argv)
    if args.self_test:
        return self_test()
    write_entry()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
