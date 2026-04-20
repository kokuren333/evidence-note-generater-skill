#!/usr/bin/env python3
"""Minimal PubMed search helper using NCBI E-utilities.

Usage:
  search_pubmed.py "hyponatremia initial evaluation systematic review" --retmax 10
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from typing import Any

BASE_ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
BASE_ESUMMARY = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"


def fetch_json(url: str) -> dict[str, Any]:
    with urllib.request.urlopen(url, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def build_url(base: str, params: dict[str, Any]) -> str:
    return f"{base}?{urllib.parse.urlencode(params)}"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    parser.add_argument("--retmax", type=int, default=10)
    parser.add_argument("--mindate", default=None)
    parser.add_argument("--maxdate", default=None)
    args = parser.parse_args()

    api_key = os.getenv("NCBI_API_KEY")
    params: dict[str, Any] = {
        "db": "pubmed",
        "term": args.query,
        "retmode": "json",
        "retmax": args.retmax,
        "sort": "relevance",
    }
    if api_key:
        params["api_key"] = api_key
    if args.mindate or args.maxdate:
        params["datetype"] = "pdat"
        if args.mindate:
            params["mindate"] = args.mindate
        if args.maxdate:
            params["maxdate"] = args.maxdate

    esearch = fetch_json(build_url(BASE_ESEARCH, params))
    ids = esearch.get("esearchresult", {}).get("idlist", [])
    if not ids:
        print(json.dumps({"query": args.query, "results": []}, ensure_ascii=False, indent=2))
        return 0

    summary_params: dict[str, Any] = {
        "db": "pubmed",
        "id": ",".join(ids),
        "retmode": "json",
    }
    if api_key:
        summary_params["api_key"] = api_key
    esummary = fetch_json(build_url(BASE_ESUMMARY, summary_params))
    result = esummary.get("result", {})

    items = []
    for pmid in ids:
        row = result.get(pmid, {})
        items.append(
            {
                "pmid": pmid,
                "title": row.get("title"),
                "pubdate": row.get("pubdate"),
                "source": row.get("source"),
                "authors": [a.get("name") for a in row.get("authors", [])],
                "articleids": row.get("articleids", []),
            }
        )

    print(json.dumps({"query": args.query, "results": items}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
