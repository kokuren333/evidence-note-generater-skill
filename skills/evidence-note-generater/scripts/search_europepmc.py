#!/usr/bin/env python3
"""Minimal Europe PMC search helper.

Usage:
  search_europepmc.py 'hyponatremia initial evaluation' --page-size 10
"""
from __future__ import annotations

import argparse
import json
import urllib.parse
import urllib.request

BASE_URL = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--page-size", type=int, default=10)
    args = parser.parse_args()

    params = {
        "query": args.query,
        "format": "json",
        "pageSize": args.page_size,
        "sort": "RELEVANCE",
    }
    url = f"{BASE_URL}?{urllib.parse.urlencode(params)}"
    with urllib.request.urlopen(url, timeout=30) as resp:
        payload = json.loads(resp.read().decode("utf-8"))

    items = []
    for row in payload.get("resultList", {}).get("result", []):
        items.append(
            {
                "id": row.get("id"),
                "source": row.get("source"),
                "title": row.get("title"),
                "authorString": row.get("authorString"),
                "journalTitle": row.get("journalTitle"),
                "pubYear": row.get("pubYear"),
                "isOpenAccess": row.get("isOpenAccess"),
                "doi": row.get("doi"),
                "pmid": row.get("pmid"),
                "pmcid": row.get("pmcid"),
            }
        )

    print(json.dumps({"query": args.query, "results": items}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
