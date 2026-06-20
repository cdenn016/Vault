---
type: schema
title: LLM-Wiki Schema & Operating Manual
aliases: [LLM-Wiki Schema, Schema, Wiki Schema]
updated: 2026-06-19
---

# LLM-Wiki Schema

This Obsidian vault is an **LLM-maintained research wiki**, built on the pattern from
[Karpathy's "LLM Wiki" gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

The premise: **knowledge should compound, not be re-derived.** Instead of re-reading raw
papers at every query (classic RAG), an LLM incrementally maintains a persistent web of
interlinked markdown pages. Humans curate sources and ask questions; the LLM does the
bookkeeping — summarizing, cross-referencing, reconciling contradictions, and keeping the
index current.

This file is the **schema**: it tells any LLM (and you) the conventions and workflows for
maintaining the wiki. Read it before doing any ingest / query / lint operation.

---

## Three-layer architecture

| Layer | Location | Mutability | Owner |
|-------|----------|------------|-------|
| **Raw sources** | `sources/` | **Immutable** — never edit, only append new files | Human curates |
| **Manuscripts** | `manuscripts/` | **Editable** — canonical LaTeX (`.tex`/`.bib`); the single source of truth across all repos | Human + LLM edit |
| **The wiki** | `wiki/` | LLM-owned synthesis; freely rewritten | LLM maintains |
| **The schema** | `CLAUDE.md` (this file) | Rarely changed | Human + LLM agree |

Plus two navigation files at the vault root: **`index.md`** (catalog) and **`log.md`** (ledger).

### Directory layout

```
/  (vault root)
├── CLAUDE.md            ← this schema / operating manual
├── index.md            ← catalog of every wiki page, grouped by type
├── log.md              ← append-only chronological ledger of operations
├── manuscripts/        ← EDITABLE canonical LaTeX (.tex/.bib) — single source of truth across repos
├── sources/            ← IMMUTABLE raw source notes (the source of truth)
│   ├── papers/         ←   one note per paper (arXiv etc.), with bibtex
│   ├── refs/           ←   curated references cited by the manuscripts (type: reference)
│   ├── manuscripts/    ←   NOTES about our manuscripts (type: manuscript) — the .tex lives in top-level manuscripts/
│   ├── runs/           ←   one note per experiment run (frozen config + metrics)
│   └── web/            ←   gists, blog posts, docs
├── wiki/               ← LLM-owned synthesis (rewrite freely)
│   ├── concepts/       ←   one idea per page (e.g. "Natural gradient")
│   ├── methods/        ←   named methods / models / architectures (e.g. "SPDNet")
│   ├── themes/         ←   cross-paper synthesis essays (one per research cluster)
│   ├── fields/         ←   per-discipline Maps of Content (field/* MOCs; Bases-driven)
│   ├── dashboards/     ←   Bases dashboards (Sources Dashboard, Wiki Status Board)
│   └── projects/       ←   YOUR research: program overview + per-experiment pages
└── templates/          ← page templates for each type
```

---

## Page conventions

Every page (source or wiki) **must** begin with YAML frontmatter:

```yaml
---
type: paper | reference | manuscript | run | web | concept | method | theme | project   # required
title: Human Readable Title                                     # required
aliases: [alt name, acronym]      # optional, helps [[wikilinks]] resolve
tags: [cluster/info-geometry, project/transformer, field/mathematics]   # cluster/* topic · project/* affiliation · field/* discipline (sources)
status: stub | draft | stable     # wiki pages only; maturity of synthesis
created: 2026-06-18
updated: 2026-06-18
# source pages only:
arxiv: 1234.56789                 # if applicable
authors: [Last F., Last G.]
year: 2020
---
```

**Naming.** Obsidian resolves `[[wikilinks]]` against the **filename** (plus `aliases`), so:
- **Wiki pages** (`concepts/`, `methods/`, `themes/`, `projects/`) are named by their human
  title — `Natural gradient.md`, `SPDNet.md`, `Precision-weighted attention.md` — so
  `[[Natural gradient]]` resolves directly. Titles must be unique.
- **Source notes** use `firstauthor-year-keyword.md` slugs (e.g.
  `amari-1998-natural-gradient.md`) and carry a readable `aliases:` entry. Wiki pages cite
  them by that slug: `[[amari-1998-natural-gradient]]`.

**Linking.** Liberally cross-link with `[[Page Title]]`. A wiki page should link the
concepts/methods it touches and cite the `[[source notes]]` it draws from. Prefer linking
to a concept page over re-explaining the concept inline. Orphan pages (nothing links to
them) are a lint smell.

**Sourcing.** Every non-obvious claim on a wiki page traces back to a `sources/` note via a
wikilink. Wiki pages synthesize; they do not introduce facts that no source supports. If you
assert something beyond the sources, mark it `> [!note] Editorial:` so it's auditable.

**Contradictions.** When two sources disagree, do **not** silently pick one. Record both with
a callout:
```
> [!warning] Contradiction
> [[source-a]] claims X; [[source-b]] claims ¬X. Unresolved.
```
and add a line to `log.md`.

### Tag taxonomy (research clusters)

Use `cluster/<name>` tags so the Obsidian graph and search group by research area:

- `cluster/vfe` — variational free energy, ELBO, variational EM, predictive coding, active inference
- `cluster/gauge-theory` — gauge equivariance, Lie groups, holonomy, irreps, BCH
- `cluster/info-geometry` — Fisher metric, natural gradient, α/Rényi divergences, dual connections
- `cluster/spd-geometry` — SPD manifold, affine-invariant metric, Riemannian optimization
- `cluster/attention` — attention mechanisms, precision-weighting, positional encodings
- `cluster/multi-agent` — the MAgent model: multi-agent VFE, meta-agents, hierarchical emergence, ouroboros, RG flow, belief inertia, Hamiltonian dynamics
- `cluster/participatory` — participatory realism / "it from bit", quantum foundations (QBism, relational QM), holography, IIT / consciousness. **Subdivided** — add the finer tag *alongside* the parent (which still rolls up; existing `[[theme]]` links keep resolving):
  - `cluster/participatory/quantum-foundations` — *physics origin*: QM foundations & interpretation (QBism, relational QM, Wigner's-friend / observer-dependent-facts no-go theorems), holography & emergent spacetime / quantum gravity, physics-from-information (entropic dynamics, Fisher/Jaynes)
  - `cluster/participatory/philosophy-of-mind` — *philosophy origin*: philosophy of mind (the hard problem, panpsychism), philosophy of science & metaphysics (structural realism, the relativized a priori), it-from-bit metaphysics
  - `cluster/participatory/consciousness` — *neuroscience origin*: scientific theories of consciousness — IIT, global workspace, neural correlates, entropic brain
- `cluster/social-physics` — opinion dynamics, bounded confidence, sociophysics (DeGroot, Friedkin–Johnsen, Deffuant, Hegselmann–Krause, Galam). **Subdivided** — add the finer tag *alongside* the parent:
  - `cluster/social-physics/opinion-dynamics` — voter, bounded-confidence, kinetic / mean-field opinion models (Galam, Toscani, Deffuant, Hegselmann–Krause)
  - `cluster/social-physics/networks-and-contagion` — network structure, cascades & herding, complex contagion, echo chambers, influence maximization
  - `cluster/social-physics/evolutionary-and-cultural` — evolutionary game theory, cooperation, cultural evolution & social learning (Maynard-Smith, Nowak, Boyd–Richerson)
  - `cluster/social-physics/social-influence` — conformity & social influence (Asch, Festinger, French–Raven, Sherif, Cialdini), collective animal motion / flocking
- `cluster/methodology` — the wiki pattern itself, tooling

Add `status/stub`, `status/draft`, or `status/stable` to track maturity if useful.

### Project tags (graph coloring)

Every content note also carries a **project affiliation** tag so the Obsidian graph colors by
project (`.obsidian/graph.json` defines the color groups):

- `project/transformer` — belongs to the [[VFE Transformer Program]] (the `vfe3` language model)
- `project/multi-agent` — belongs to the [[Gauge-Theoretic Multi-Agent VFE Model]] (MAgent)
- `project/social-physics` — belongs to the [[SocialPhysics]] project (opinion dynamics, belief momentum, sociophysics; founded on [[belief-inertia]])
- **multiple tags** = shared core theory used by more than one project (colored green in the graph)

Rule of thumb when ingesting: a note is `project/social-physics` if it carries a
`cluster/social-physics` tag (opinion dynamics, sociophysics, collective inference); it is
`project/multi-agent` if it carries `cluster/multi-agent` or `cluster/participatory`; a note used by
more than one project carries **all** the applicable project tags (e.g. the shared belief-dynamics
concepts [[Belief inertia]], [[Mass as Fisher information]], [[Hamiltonian belief dynamics]] are both
`project/multi-agent` and `project/social-physics`); otherwise it is `project/transformer`. Keep the
three project hub pages tagged with their own project only.

### Discipline tags (`field/*` facet)

Orthogonal to topic (`cluster/*`) and project (`project/*`), every **source note** carries one or
more `field/<discipline>` tags recording its **academic discipline(s) of origin** — the field where
the work natively lives / was published. This is a *faceted* axis: ≈65% of sources are
cross-disciplinary, so discipline is a **multi-valued tag, never a folder** (a sociophysics paper is
physics *and* sociology; it cannot live in one discipline folder without duplication or discarding a
field). The vocabulary is **closed — exactly ten slugs, no others, and no sub-fields**
(`field/physics/qft` is forbidden; finer structure lives in the discipline MOCs, never in new tags):

- `field/physics` — statistical mechanics, gauge theory / QFT, gravity & holography, quantum
  mechanics & foundations, thermodynamics, synchronization & nonlinear dynamics, sociophysics
- `field/mathematics` — differential / Riemannian geometry, matrix manifolds, Lie theory, PDE &
  kinetic theory, mean-field-games math, probability / random graphs, asymptotics, dynamical systems
- `field/cs-ml` — machine learning, deep learning, transformers / attention, neural networks,
  information bottleneck, algorithms, computational network science
- `field/statistics` — Bayesian inference, information theory, model selection (MDL / BIC),
  forecasting, estimation theory
- `field/neuroscience` — computational & cognitive neuroscience, predictive coding (brain),
  free-energy-as-brain-theory, neural correlates of consciousness
- `field/psychology` — social & cognitive psychology (conformity, dissonance, social influence,
  attitude change, cognitive bias)
- `field/sociology` — opinion dynamics as social science, social-network sociology, political
  polarization, diffusion of innovations, collective social behavior
- `field/economics` — game theory, herding / information cascades, increasing returns, social
  learning (econ), mean-field games (econ application)
- `field/biology` — evolutionary dynamics & evolutionary game theory, cultural evolution, collective
  animal behavior / flocking, ecology
- `field/philosophy` — philosophy of mind, philosophy of science, metaphysics, epistemology

**Rules.**
- Tag **source notes only** (`sources/`). Wiki synthesis pages are *not* `field/*`-tagged —
  discipline is a property of sources, surfaced for the wiki layer through the field MOCs.
- List **all** applicable fields, **field-of-origin first** (first-listed = native home — cheap,
  greppable, lossless; there is no separate "primary" key or property).
- Appending `field/*` to a source's `tags:` is the one sanctioned exception to source immutability,
  exactly as `project/*` is — never touch source prose.

**Discipline MOCs (`wiki/fields/`).** One Map-of-Content page per discipline — `[[Physics MOC]]`,
`[[Mathematics MOC]]`, … — plus a `[[Disciplines MOC]]` hub. Each MOC embeds an Obsidian **Bases**
view (a ```base code block) that auto-lists its field via `file.hasTag("field/<discipline>")`.
**Bases is the enabled core plugin; do not use Dataview (it is not installed).** The three facets
compose by tag search — e.g. `tag:#field/physics tag:#cluster/info-geometry` finds the information-
geometry sources of physics origin. MOC pages are `type: moc`.

---

## Operations

These are the three core workflows. Each one **ends by appending to `log.md`** and, if pages
were added/removed, **updating `index.md`**.

### 1. Ingest — add a new source

> Trigger: "ingest <paper/url/run>", or a new file dropped in `sources/`.

1. Create the immutable source note in the right `sources/` subfolder, using the matching
   template. Capture: full citation + bibtex, the core claim/contribution, method, key
   results, and **"Relevance to this research"** (how it connects to the VFE transformer).
   **Tag it** with the finest `cluster/*` (the sub-cluster where one exists), its `project/*`
   affiliation(s), and **all** applicable `field/*` disciplines (origin first); then add the note
   to the relevant `wiki/fields/` discipline MOC.
2. Propagate into the wiki: for each concept/method the source touches, **update the existing
   wiki page** (don't create a duplicate) — add the new finding, cite `[[the source]]`. Create
   a new concept/method page only if none exists.
3. Update the relevant `themes/` synthesis page so the cross-paper picture stays current.
4. Add `[[backlinks]]` so the new material is reachable. Run a mini-lint on touched pages.
5. Append an `INGEST` line to `log.md`; update `index.md` if pages were created.

### 2. Query — answer a question, then bank the answer

> Trigger: a research question.

1. **Search the wiki first** (`wiki/`, `index.md`), not the raw sources. Follow wikilinks.
2. Synthesize an answer, citing the `[[pages]]` and underlying `[[sources]]` used.
3. If the answer required non-trivial synthesis worth keeping, **file it back**: create or
   extend a concept/theme page so the next person (or LLM) gets it for free. This is what makes
   knowledge compound.
4. Append a `QUERY` line to `log.md` noting the question and what was filed.

### 3. Lint — periodic health check

> Trigger: "lint the wiki", or every ~N ingests.

Scan for and report (and fix where safe):
- **Contradictions** — conflicting claims across pages (see callout convention).
- **Stale claims** — wiki text not supported by any current `sources/` note.
- **Orphans** — pages nothing links to; broken `[[wikilinks]]`.
- **Gaps** — concepts referenced but with no page; sources ingested but not synthesized.
- **Duplication** — two pages covering the same idea → merge, keep one canonical title.
- **Index drift** — pages missing from `index.md`.

Append a `LINT` line to `log.md` summarizing findings and actions.

---

## log.md format

Append-only. One operation per line, newest at the bottom, parseable timestamp first:

```
2026-06-18  GENESIS  Scaffold created; wiki schema established.
2026-06-18  INGEST   sources/papers/amari-1998-natural-gradient.md → updated [[Natural gradient]], [[Information geometry and natural gradient|information geometry]]
2026-06-18  QUERY    "how does precision-weighting relate to Fisher info?" → filed [[Precision-weighted attention]]
2026-06-18  LINT     3 orphans fixed, 1 contradiction flagged on [[Holonomy]]
```

---

## Guidance for the maintaining LLM

- **You own `wiki/`; you may rewrite any wiki page wholesale.** You may NEVER edit `sources/`. The top-level `manuscripts/` folder *is* editable — it holds the canonical `.tex`/`.bib` (the single source of truth across repos); `sources/manuscripts/` still holds only the immutable *notes* about them.
- Keep summaries current; that bookkeeping is the whole point — the human won't do it.
- Write for a future reader who has not read the papers: define terms, link generously.
- Prefer fewer, well-connected, canonical pages over many thin duplicates.
- When unsure whether a claim is supported, attribute it to a source or mark it editorial.
- Scale effort to the page: a stub is fine for a peripheral concept; core pages earn depth.
