#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, subprocess, sys
from pathlib import Path

BASE = Path(__file__).resolve().parent

def run(script: str, *args: str) -> list[dict]:
    proc = subprocess.run([sys.executable, str(BASE / script), *args], capture_output=True, text=True, check=True)
    return json.loads(proc.stdout)


def dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for r in rows:
        key = (r.get('pmid') or '', r.get('doi') or '', (r.get('title') or '').strip().lower())
        if key in seen:
            continue
        seen.add(key)
        out.append(r)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description='Collect candidate sources from PubMed and Europe PMC.')
    ap.add_argument('--question', required=True)
    ap.add_argument('--retmax', type=int, default=10)
    args = ap.parse_args()

    q = args.question
    pubmed_query = f'({q}) AND (guideline OR systematic review OR meta-analysis OR review OR randomized)'
    epmc_query = f'({q}) AND (GUIDELINE OR REVIEW OR "SYSTEMATIC REVIEW" OR "META-ANALYSIS")'

    rows = []
    try:
        rows.extend(run('search_pubmed.py', '--query', pubmed_query, '--retmax', str(args.retmax)))
    except Exception:
        pass
    try:
        rows.extend(run('search_europepmc.py', '--query', epmc_query, '--page-size', str(args.retmax)))
    except Exception:
        pass

    rows = dedupe(rows)
    rows.sort(key=lambda x: (x.get('year') or 0), reverse=True)
    print(json.dumps(rows[: max(5, min(20, args.retmax * 2))], ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
