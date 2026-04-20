# Repository instructions

## Purpose
This repository houses a Codex-native skill that creates bilingual evidence notes for resident/general internal medicine topics.

## Core execution model
Codex itself is the reasoning engine, planner, synthesizer, translator, and file writer.
Do not introduce Gemini or any other external LLM API unless the user explicitly asks for that.
Use the helper scripts only to support search, routing, rendering, and validation.

## Working rules
- Treat `skills/evidence-note-generater/SKILL.md` as the primary workflow contract.
- Keep final deliverables limited to two markdown notes saved under `output/<topic-folder>/`.
- Do not emit extra summary files unless explicitly requested.
- Prefer trustworthy, recent secondary evidence and current guidelines, then landmark primary studies.
- Never fabricate citations, guideline names, PMID, DOI, URL, or access dates.
- If a high-quality guideline cannot be verified, proceed with journal evidence and state the limitation under `## Caveats`.
- If internet access is unavailable, do not invent references; state the limitation and stop.

## Recommended helper scripts
- `skills/evidence-note-generater/scripts/collect_sources.py`
- `skills/evidence-note-generater/scripts/search_pubmed.py`
- `skills/evidence-note-generater/scripts/search_europepmc.py`
- `skills/evidence-note-generater/scripts/guideline_query_builder.py`
- `skills/evidence-note-generater/scripts/select_topic_folder.py`
- `skills/evidence-note-generater/scripts/slugify_title.py`
- `skills/evidence-note-generater/scripts/render_note.py`
- `skills/evidence-note-generater/scripts/validate_note.py`
