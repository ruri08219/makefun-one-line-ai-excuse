"""One-Line AI Excuse for Breaking Production (make.fun).

Writes a single-line excuse, in the AI agent's own voice, to
/output/entry.txt as UTF-8 text.
"""

import os
from pathlib import Path

ENTRY = (
    "I just deleted the production database \u2014 but I did it with "
    "99.7% confidence, which is technically my best score all week."
)


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")

    # Round-trip assert: what we wrote is exactly what is on disk.
    read_back = output_path.read_text(encoding="utf-8")
    assert read_back == ENTRY, "round-trip mismatch"
    assert 1 <= len(read_back) <= 180, "entry must be 1-180 characters"
    assert read_back.strip(), "entry must not be only whitespace"


if __name__ == "__main__":
    main()
