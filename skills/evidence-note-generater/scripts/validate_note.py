#!/usr/bin/env python3
"""Validate high-level structure rules for an evidence note JSON payload."""
from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_KEYS = [
    "title",
    "clinical_question",
    "bottom_line",
    "why_this_matters",
    "scope_and_intended_use",
    "key_definitions",
    "search_strategy",
    "included_evidence",
    "excluded_or_deprioritized_evidence",
    "pathophysiology_background",
    "diagnosis_assessment",
    "management_principles",
    "harms_pitfalls",
    "what_remains_uncertain",
    "practical_takeaways_for_residents",
    "source_map",
    "caveats",
    "last_updated",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_note.py evidence_note.json", file=sys.stderr)
        return 1
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    missing = [k for k in REQUIRED_KEYS if k not in data]
    if missing:
        print(f"Missing required keys: {', '.join(missing)}", file=sys.stderr)
        return 1
    source_count = len(data.get("included_evidence", []))
    if not 5 <= source_count <= 15:
        print(f"included_evidence must contain 5-15 items; got {source_count}", file=sys.stderr)
        return 1
    mapped_count = len(data.get("source_map", []))
    if mapped_count != source_count:
        print(
            f"source_map count must match included_evidence count; got {mapped_count} vs {source_count}",
            file=sys.stderr,
        )
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
