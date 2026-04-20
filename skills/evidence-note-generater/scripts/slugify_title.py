#!/usr/bin/env python3
"""Create a filesystem-safe kebab-case filename stem from an English title."""
from __future__ import annotations

import re
import sys
import unicodedata


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    text = re.sub(r"-{2,}", "-", text)
    return text or "evidence-note"


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: slugify_title.py 'Initial Evaluation of Adult Hyponatremia'", file=sys.stderr)
        return 1
    print(slugify(" ".join(sys.argv[1:])))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
