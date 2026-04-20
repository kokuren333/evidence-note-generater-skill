# evidence-note-generater (GitHub-ready)

This directory is a GitHub-ready export of the Codex-native skill for generating bilingual evidence notes for resident/general internal medicine topics.

## What is included
- `AGENTS.md`
- `requirements.txt`
- `generate_evidence_note.py`
- `skills/evidence-note-generater/`
- empty `output/` topic folders so the skill can be used immediately after cloning

## What is intentionally not included
- previously generated markdown notes
- extra repository history or unrelated working files

## Repository layout
```text
.
+-- AGENTS.md
+-- README.md
+-- requirements.txt
+-- generate_evidence_note.py
+-- skills/
|   +-- evidence-note-generater/
+-- output/
    +-- fluids-electrolytes-kidney/
    +-- cardiovascular-respiratory/
    +-- infectious-diseases-antimicrobials/
    +-- gastroenterology-hepatobiliary-pancreas/
    +-- endocrinology-metabolism-nutrition/
    +-- hematology-immunology-rheumatology/
    +-- neurology-psychiatry/
    +-- emergency-diagnostics-reasoning/
```

## Usage
Open this directory as its own repository in Codex and use the skill in:

```text
skills/evidence-note-generater
```

Typical prompt:

```text
Use the skill in skills/evidence-note-generater. Search 5-15 recent trustworthy sources including guidelines when available, then generate the bilingual evidence note and save the two markdown files in the correct output folder.
```

## Notes
- Codex itself is the orchestrator. The included Python scripts are helper utilities only.
- Internet access is required when live literature verification is needed.
- Output folders are empty by design so the repository is clean for first use and ready to push to GitHub.
