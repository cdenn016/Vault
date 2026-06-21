# Empty / ghost graph-node investigation — findings (2026-06-21)

## Symptom
A "shitload of empty nodes" in the Obsidian graph after zooming out (graph `scale`
dropped to 0.019 — the user's live view, left untouched).

## Root cause
Obsidian renders a faint "ghost" node for every `[[wikilink]]` whose target file does
not exist, and the graph has **`hideUnresolved: false`** (so ghosts are visible).

- **762 md files scanned, 12,379 wikilink instances.**
- **492 unique unresolved link targets → 492 ghost nodes.**
- **763 unresolved link instances, ALL of them in `sources/`** (0 in `wiki/`, `templates/`, `inbox/`).
- **467 source notes carry a "Cross-links" section** — the LLM-authored navigation block
  added at ingest. These cite concepts/sources by *loose, non-canonical names* and by
  *bibtex keys*, none reconciled against the real page titles/filenames.

### Trigger
Recent commit `5fe9be9 ingest(sources): bulk PDF-sourced source notes for all
references.bib papers` bulk-created source notes, each with an unreconciled Cross-links
block. This is a **recurrence** of the problem already fixed in
`1a37002 fix(graph): eliminate empty/ghost nodes from reversed cross-links` and
`572e01e fix(graph): remove remaining empty/ghost nodes` — the bulk ingest reintroduced it.

## The 492 targets, categorized (fuzzy-matched to nearest real page)

| Bucket | Targets | Link instances | Nature |
|---|---|---|---|
| **alias_to_existing** | 72 | 157 | Target IS a real page, just a name/casing/slug variant (e.g. `Free Energy Principle`→`Free-energy principle`; `vaswani2017attention`→`vaswani-2017-attention.md`; `MAgent Model`→`MAgent_Model`) |
| **missing_source** | 177 | 198 | bibtex-key / slug for a paper with no note. Some are slug-variants of an existing note (`friston-2010-free-energy`→`friston-2010-free-energy-principle`); most are papers never ingested (`shannon1948mathematical`, `jaynes-2003-probability`, `lord-1979-biased-assimilation`, …) |
| **missing_concept** | 243 | 404 | Title-Case concept with no page. Many alias to a near page (`Attention Mechanism`→`Attention mechanisms — theory and positional structure`; `SPD Manifold`→`SPD-manifold geometry…`; `Markov Blanket`→`Markov blanket interpretation debate`); some are genuine gaps (`Decoherence`, `Mutual information`, `Softmax`, `Kalman Filter`, `Born Rule`) |

### Highest-impact single targets
- `PIFB` (43) + `PIFB Manuscript` (6) + `PIFB.tex` (1) = **50 instances** → the
  Participatory-it-from-bit manuscript (`manuscripts/PIFB.tex` exists; theme page
  `Participatory realism and quantum foundations` exists). One hub page/alias fixes all 50.
- `Attention Mechanism` (22) → `Attention mechanisms — theory and positional structure`.
- `MAgent Model` (25) → `MAgent_Model` (project page exists).
- `vaswani2017attention` (13) → `vaswani-2017-attention.md` exists (bibtex-key vs slug).

## Note: false fuzzy-matches (need judgment, not blind apply)
The fuzzy matcher is a *hint* and has wrong hits, e.g. `Gauge Theory`→`ABI gauge theory`
(wrong), `amari-2016-information-geometry`→`ay-2017-information-geometry` (wrong author/year),
`Entropy`→`Wald entropy` (wrong). Resolution must be verified per-target.

## Separate, minor: 3 empty `.md` files (real empty nodes, not ghosts)
`inbox/GL(K) attention manuscript.md`, `inbox/Reaction Time Distributions.md`,
`inbox/kingma2014vae.md` — untracked, 0 bytes, the user's own new WIP inbox stubs.
Left untouched pending instruction (prior precedent deleted *accidental* empty inbox dupes).

## Precedent for the fix (commit 1a37002)
Prior fix edited the source Cross-links to target real filenames
(`[[slug|Display]]`), deleted empty stub dupes, and backticked residual illustrative
dangling links — explicitly "no prose/facts changed." That establishes: **editing the
Cross-links nav block (not the TL;DR/Method/Results/Relevance prose) is the sanctioned
ghost-node fix in this vault.**
