#!/usr/bin/env python3
"""Render markdown from a validated evidence-note JSON payload."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


def bullet_list(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items) if items else "- None noted"


def format_included(items: list[dict[str, Any]]) -> str:
    lines = []
    for item in items:
        lines.append(
            f"- [{item['source_id']}] {item['citation']} ({item['doc_type']}, {item['year']}) — {item['why_included']}"
        )
    return "\n".join(lines) if lines else "- None"


def format_excluded(items: list[dict[str, Any]]) -> str:
    lines = []
    for item in items:
        lines.append(f"- {item['citation_or_query']} — {item['reason']}")
    return "\n".join(lines) if lines else "- None"


def format_source_map(items: list[dict[str, Any]]) -> str:
    lines = []
    for item in items:
        suffix_parts = []
        for key in ("doi", "pmid", "pmcid", "url"):
            value = item.get(key)
            if value:
                suffix_parts.append(f"{key.upper()}: {value}")
        suffix = f" ({'; '.join(suffix_parts)})" if suffix_parts else ""
        lines.append(f"{item['source_id']}. {item['vancouver']} [{item['source_type']}]" + suffix)
    return "\n".join(lines)


def render(payload: dict[str, Any]) -> str:
    return f"""# {payload['title']}
## Clinical question
{payload['clinical_question']}

## Bottom line
{bullet_list(payload['bottom_line'])}

## Why this matters
{payload['why_this_matters']}

## Scope and intended use
{payload['scope_and_intended_use']}

## Key definitions
{bullet_list(payload['key_definitions'])}

## Evidence base
### Search strategy
{bullet_list(payload['search_strategy'])}

### Included evidence
{format_included(payload['included_evidence'])}

### Excluded / deprioritized evidence
{format_excluded(payload['excluded_or_deprioritized_evidence'])}

## What is known
### Pathophysiology / background
{payload['pathophysiology_background']}

### Diagnosis / assessment
{payload['diagnosis_assessment']}

### Management principles
{payload['management_principles']}

### Harms / pitfalls
{payload['harms_pitfalls']}

## What remains uncertain
{payload['what_remains_uncertain']}

## Practical takeaways for residents
{bullet_list(payload['practical_takeaways_for_residents'])}

## Source map
{format_source_map(payload['source_map'])}

## Caveats
{bullet_list(payload['caveats'])}

## Last updated
{payload['last_updated']}
"""


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: render_note.py input.json output.md", file=sys.stderr)
        return 1
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    markdown = render(payload)
    Path(sys.argv[2]).write_text(markdown, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
