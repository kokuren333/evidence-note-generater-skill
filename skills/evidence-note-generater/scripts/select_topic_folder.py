#!/usr/bin/env python3
"""Suggest the most likely output folder from a question string."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parents[1]
CONFIG = BASE / "config" / "topic_folders.yaml"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    text = args.text.lower()

    data = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    scored = []
    for folder, meta in data.items():
        score = sum(1 for kw in meta.get("keywords", []) if kw in text)
        scored.append({"folder": folder, "score": score})
    scored.sort(key=lambda x: x["score"], reverse=True)
    print(json.dumps(scored, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
