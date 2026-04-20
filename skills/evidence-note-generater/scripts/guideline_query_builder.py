#!/usr/bin/env python3
"""Build site-targeted guideline queries for public web search providers."""
from __future__ import annotations

import argparse
import json

DOMAINS = [
    "minds.jcqhc.or.jp",
    "mhlw.go.jp",
    "j-circ.or.jp",
    "jsicm.org",
    "jspn.or.jp",
    "jsn.or.jp",
    "jsge.or.jp",
]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("question")
    args = parser.parse_args()

    queries = [f'site:{domain} {args.question} guideline OR ガイドライン' for domain in DOMAINS]
    print(json.dumps({"question": args.question, "queries": queries}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
