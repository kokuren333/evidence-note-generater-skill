---
name: evidence-note-generater
description: Generate a bilingual resident-facing evidence note from a clinical question using Codex itself as the reasoning engine. Search 5-15 trustworthy recent sources including guidelines when available, synthesize one English markdown note and one Japanese markdown note in the required structure, and save both into the correct topic folder.
---

# evidence-note-generater

## Core principle
Codex itself is the orchestrator and writer for this workflow.
Do not depend on Gemini or any separate LLM API for planning, synthesis, or translation.
Use helper scripts only for search support, folder routing, slug generation, rendering, and validation.

## When to use this skill
Use this skill when the user asks for an evidence note, a resident/general internal medicine summary, or a structured literature-based note from a clinical question.

## Deliverables
Produce exactly two files and save them in the same output folder:

1. English markdown note: `<english-title>.md`
2. Japanese markdown note: `JP_<english-title>.md`

Do not create any other deliverable files unless the user explicitly asks.

## Allowed output folders
Choose exactly one folder under `output/`:

- `fluids-electrolytes-kidney`
- `cardiovascular-respiratory`
- `infectious-diseases-antimicrobials`
- `gastroenterology-hepatobiliary-pancreas`
- `endocrinology-metabolism-nutrition`
- `hematology-immunology-rheumatology`
- `neurology-psychiatry`
- `emergency-diagnostics-reasoning`

## Topic routing rules
Route notes by the main educational home of the question:

- Fluids/electrolytes/kidney: fluids, sodium/potassium disorders, acid-base, AKI, CKD, urinalysis, diuretics
- Cardiovascular/respiratory: chest pain, dyspnea, heart failure, ischemia, arrhythmia, ECG, pneumonia, asthma/COPD, hypoxemia, respiratory failure
- Infectious diseases/antimicrobials: fever, sepsis, cultures, antimicrobial choice, organ-specific infection, de-escalation, infection control
- Gastroenterology/hepatobiliary/pancreas: abdominal pain, GI bleeding, diarrhea, constipation, liver test abnormalities, cholangitis, pancreatitis
- Endocrinology/metabolism/nutrition: diabetes, hypoglycemia, hyperglycemic emergencies, thyroid, adrenal, dyslipidemia, nutrition support
- Hematology/immunology/rheumatology: anemia, thrombocytopenia, coagulation, transfusion, autoimmune disease, vasculitis, allergy
- Neurology/psychiatry: altered mental status, stroke, seizure, headache, vertigo, delirium, depression, anxiety, insomnia, initial psychiatric management
- Emergency/diagnostics/reasoning: ABC, shock, fever, chest pain, abdominal pain, syncope, diagnostic test construction, consult threshold

## Source selection rules
Select 5-15 total sources.

Prefer, in this order:
1. Recent high-quality guidelines or consensus statements when they directly address the question
2. Recent systematic reviews, meta-analyses, or evidence reports
3. Landmark randomized trials or strong comparative studies
4. Important diagnostic accuracy or prognostic studies when needed

Quality filters:
- Prefer recent sources unless an older source is clearly landmark
- Prefer reputable publishers, societies, or public agencies
- Exclude weak, redundant, outdated, or off-question evidence
- Keep the set tight and clinically useful for residents

## Search workflow
1. Normalize the clinical question into a narrow resident-facing topic.
2. Create an English search question and 2-5 search strategies.
3. Search literature sources first using the helper scripts when useful.
4. Search public guideline sources when available and relevant.
5. Rank candidates by relevance, recency, trust, and resident usefulness.
6. Keep 5-15 included sources and document the rest under `Excluded / deprioritized evidence`.

## Suggested helper commands
Use these scripts when useful:

```bash
python skills/evidence-note-generater/scripts/search_pubmed.py --query "adult hyponatremia initial evaluation systematic review OR guideline" --retmax 10
python skills/evidence-note-generater/scripts/search_europepmc.py --query 'TITLE:"hyponatremia" AND (GUIDELINE OR REVIEW)' --page-size 10
python skills/evidence-note-generater/scripts/guideline_query_builder.py "低Na血症の初期評価"
python skills/evidence-note-generater/scripts/collect_sources.py --question "低Na血症の初期評価"
python skills/evidence-note-generater/scripts/select_topic_folder.py "low sodium initial evaluation"
python skills/evidence-note-generater/scripts/slugify_title.py "Initial Evaluation of Adult Hyponatremia"
```

## Writing workflow
1. Search and shortlist 5-15 sources.
2. Read enough of each source to support the note.
3. Draft the English evidence note first.
4. Translate the English note into Japanese while preserving source numbering.
5. Validate headings, filenames, and output paths.

## Required markdown structure
Use this exact heading structure in both notes:

```markdown
# Topic
## Clinical question
## Bottom line
## Why this matters
## Scope and intended use
## Key definitions
## Evidence base
### Search strategy
### Included evidence
### Excluded / deprioritized evidence
## What is known
### Pathophysiology / background
### Diagnosis / assessment
### Management principles
### Harms / pitfalls
## What remains uncertain
## Practical takeaways for residents
## Source map
## Caveats
## Last updated
```

Replace `# Topic` with the actual English title in the English note and a natural Japanese title in the Japanese note.

## Citation rules
- Every included source must appear in `## Source map`
- Use numbered Vancouver-style references when possible
- Include enough metadata to relocate the source: authors, title, journal or organization, year, volume/issue/pages if known, DOI and/or PMID/PMCID and/or URL as available
- Use the same source numbers consistently throughout both notes
- Mention source numbers inline in the prose where useful, but keep the note readable

## Evidence note content standards
- `## Bottom line` should be 3-6 bullet points or short paragraphs
- `## Practical takeaways for residents` should focus on bedside usefulness, escalation triggers, and common mistakes
- `## Caveats` must state key evidence limitations, scope limitations, and any uncertainty about guideline coverage
- `## Last updated` must use ISO date format `YYYY-MM-DD`

## Guardrails
- Do not claim to be a formal systematic review unless explicitly asked
- Do not fabricate citations, guideline names, PMID, DOI, or URLs
- Do not fabricate dosing, thresholds, contraindications, or guideline statements
- If evidence is mixed, say so under `What remains uncertain`
- If guideline access is incomplete, state that limitation under `Caveats`
- If the question is too broad, narrow it to one resident-usable clinical question before searching
- If network access is unavailable, state that you could not verify live sources and stop rather than inventing references

## File writing rules
- Write only two markdown files
- Save them into exactly one routed folder under `output/`
- English filename: `<slug>.md`
- Japanese filename: `JP_<slug>.md`
- Do not write JSON sidecars unless explicitly asked

## Validation
Before finishing, confirm:
- both notes exist
- both notes use the required heading structure
- both notes share the same source numbering
- the folder choice matches the topic
- the filenames match the English title stem

Use `scripts/validate_note.py` when useful.
