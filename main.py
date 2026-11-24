"""The Production Database Apology.

Reads the one-line apology from entry.txt and prints it, so the
graded entry is exactly the text file — one line, at most 200 chars.
"""

from pathlib import Path

ENTRY_FILE = "entry.txt"
MAX_CHARS = 200


def load_apology() -> str:
    path = Path(__file__).resolve().parent / ENTRY_FILE
    line = path.read_text(encoding="utf-8").strip()
    if not line:
        raise ValueError("entry.txt is empty")
    if len(line) > MAX_CHARS:
        raise ValueError(f"apology is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line:
        raise ValueError("apology must be a single line")
    return line


def main() -> None:
    print(load_apology())


if __name__ == "__main__":
    main()
