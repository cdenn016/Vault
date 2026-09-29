---
type: paper
title: "Aggregation of Variables in Dynamic Systems"
aliases:
  - "Simon and Ando 1961"
  - "Simon-Ando aggregation"
  - "near decomposability (Simon-Ando)"
authors:
  - Simon H.A.
  - Ando A.
year: 1961
doi: "10.2307/1909285"
url: "https://doi.org/10.2307/1909285"
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/economics
  - field/mathematics
created: 2026-09-28
updated: 2026-09-28
---

# Aggregation of Variables in Dynamic Systems

> [!info] Citation
> Herbert A. Simon and Albert Ando (1961). "Aggregation of Variables in Dynamic Systems."
> *Econometrica* **29**(2), 111–138. DOI 10.2307/1909285 (JSTOR stable 1909285).
> Crossref lists the authors in the order Simon, Ando; the Econometric Society page lists Ando, Simon.

## Verification record

Existence and metadata verified on 2026-09-28 against the Crossref record for 10.2307/1909285
and the Econometric Society abstract page (volume 29, issue 2, pages 111–138, 1961). Access:
abstract only; the paper's internal stage structure was not read. Gathered by Claude Opus 5.5,
verified by Claude Fable 5.1.

## TL;DR (abstract level)

Nearly decomposable linear dynamic systems, whose matrix elements outside certain diagonal
submatrices approach zero in the limit, can be represented as a superposition of independent
within-block subsystems and an aggregate system with one variable per block. The
superposition separates short-run (within-block) dynamics from long-run (aggregate) dynamics
and justifies neglecting weak inter-block links in a restricted equilibrium analysis.

## Relevance to this research

This is the primary source for the idea that a coarse description keeps one aggregate per
block and discards the within-block configuration, and that it is valid only on a timescale
after the within-block short run has settled. In the four-agent cycle of
[[multiagentelbo-2026-09-28-early-parent]] the blocks are the pairs, the discarded coordinates
are the within-pair disagreements, and the kept aggregates are the slow shared coordinates.
The correspondence is interpretive: Simon–Ando obtain the separation from weak inter-block
coupling, whereas the model obtains it from strong within-pair restoring rates (4 to 8)
relative to slow drift, and Simon–Ando measure validity in state space, not in relative entropy,
so they say nothing about the temperature-dependent $\log(1/\epsilon)$ activation delay. See
[[Meta-agents and hierarchical emergence]] and [[Staged hierarchy formation and RG composability]];
the companion informal argument is [[simon-1962-architecture-complexity]].

## Cross-links

- Concepts: [[Meta-agents and hierarchical emergence]], [[Coarse Graining]]
- Themes: [[Staged hierarchy formation and RG composability]]
- Related sources: [[simon-1962-architecture-complexity]], [[geigenmuller-1983-elimination-fast-variables]], [[vankampen-1985-elimination-fast-variables]]

## BibTeX

```bibtex
@article{simon1961aggregation,
  author  = {Simon, Herbert A. and Ando, Albert},
  title   = {Aggregation of Variables in Dynamic Systems},
  journal = {Econometrica},
  volume  = {29},
  number  = {2},
  pages   = {111--138},
  year    = {1961},
  doi     = {10.2307/1909285}
}
```
