---
type: reference
title: "The rate of convergence in the method of alternating projections"
aliases: ["badea2012rate"]
authors: ["Catalin Badea", "Sophie Grivaux", "Vladimir Müller"]
year: 2012
venue: "St. Petersburg Mathematical Journal"
doi: "10.1090/S1061-0022-2012-01202-1"
arxiv: "1006.2047"
url: "https://doi.org/10.1090/S1061-0022-2012-01202-1"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# The rate of convergence in the method of alternating projections

> [!info] Citation
> Badea, C., Grivaux, S., Müller, V. (2012). *The rate of convergence in the method of alternating projections*. St. Petersburg Mathematical Journal, 23(3), 413-434. [DOI](https://doi.org/10.1090/S1061-0022-2012-01202-1) / [arXiv](https://arxiv.org/abs/1006.2047)

[Local PDF](../pdfs/badea-2012-rate-convergence-method.pdf), 23 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper generalizes the cosine of the Friedrichs angle between two subspaces to a parameter for several closed subspaces of a Hilbert space and uses it to study the rate of the von Neumann-Halperin cyclic alternating projections.

## Problem & setting

For two closed subspaces $M_1, M_2$ of a Hilbert space, von Neumann showed that $(P_{M_2}P_{M_1})^n$ converges strongly to the projection onto $M_1\cap M_2$, and Halperin extended this to $N$ subspaces. The introduction recalls that for $N=2$ the rate is described through the Friedrichs angle, defined as the angle whose cosine is the supremum of $|\langle x,y\rangle|$ over unit-ball vectors of $M_1\cap M^\perp$ and $M_2\cap M^\perp$, with $M=M_1\cap M_2$.

## Method

The authors define a multi-subspace analogue of the Friedrichs cosine and apply it, with spectral theory, to cyclic alternating projections in Hilbert and in uniformly convex Banach spaces.

## Key results

Dichotomy theorems are proved: under stated conditions, either convergence is quick and uniform or it is arbitrarily slow, and several meanings of "arbitrarily slow" are proposed. The introduction's account of the two-subspace case is the part used by the manuscript.

## Relevance to this research

The manuscript cites this paper as its source for the two-subspace rate: the upper bound is credited to [[aronszajn-1950-reproducing-kernels]] and the equality to Kayalar and Weinert, both as stated in Section 1B here. It also places the paper beside von Neumann and Halperin for noiseless relays of fixed codes in a common metric, which are alternating projections onto the intersection. The use is in the scale analysis of shared content under [[Coarse Graining]] and [[Renormalization group flow]], and in [[Meta-agents and hierarchical emergence]].

## Cross-links

[[Collective agents literature map]]; [[Coarse Graining]]; [[Renormalization group flow]]; [[Meta-agents and hierarchical emergence]]; [[aronszajn-1950-reproducing-kernels]].

## BibTeX

```bibtex
@article{badea2012rate,
  author        = {Badea, Catalin and Grivaux, Sophie and M{\"u}ller, Vladimir},
  title         = {The rate of convergence in the method of alternating projections},
  journal       = {St. Petersburg Mathematical Journal},
  volume        = {23},
  number        = {3},
  pages         = {413--434},
  year          = {2012},
  doi           = {10.1090/S1061-0022-2012-01202-1},
  eprint        = {1006.2047},
  archivePrefix = {arXiv}
}
```
