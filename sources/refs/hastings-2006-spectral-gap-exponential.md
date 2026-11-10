---
type: reference
title: "Spectral Gap and Exponential Decay of Correlations"
aliases: ["hastings2006spectral"]
authors: ["Matthew B. Hastings", "Tohru Koma"]
year: 2006
venue: "Communications in Mathematical Physics"
doi: "10.1007/s00220-006-0030-4"
arxiv: "math-ph/0507008"
url: "https://doi.org/10.1007/s00220-006-0030-4"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Spectral Gap and Exponential Decay of Correlations

> [!info] Citation
> Hastings, M. B., Koma, T. (2006). *Spectral Gap and Exponential Decay of Correlations*. Communications in Mathematical Physics, 265(3), 781-804. [DOI](https://doi.org/10.1007/s00220-006-0030-4); [arXiv](https://arxiv.org/abs/math-ph/0507008)

[Local PDF](../pdfs/hastings-2006-spectral-gap-exponential.pdf), 23 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper relates the spectral gap above the ground state to the decay of ground-state correlations in quantum spin and fermion systems with short-range interactions, proving exponential clustering under the gap assumption and treating power-law interactions as well.

## Problem & setting

The introduction starts from the folk statement that a nonvanishing gap implies exponentially decaying correlations, and notes that exponential clustering of connected correlations had recently been proved for quantum lattice systems, while an earlier bound for correlations of U(1)-vector observables decayed more slowly than exponentially. The authors ask whether the two can be combined to bound the correlation functions themselves rather than only the connected ones, and point out that this needs certain matrix elements in the ground-state sector to vanish.

## Method

The authors first prove exponential clustering of generic correlations under the gap assumption, extending it to long-range interactions, both power-law and exponentially decaying, where bounds become power laws. An appendix proves a Lieb-Robinson bound on the group velocity for power-law interactions.

## Key results

Under the gap assumption, connected correlations of commuting observables decay exponentially, and correlations of observables that anticommute at large distance decay exponentially. For vector observables under a U(1) symmetry, the correlation function itself decays exponentially on lattices with a stated self-similarity in fractal dimension below two, a condition that holds automatically with translation invariance in one direction.

## Relevance to this research

The manuscript cites the paper, with a related work on Lieb-Robinson bounds, as the source of exponential clustering from a spectral gap, of which its own clustering theorem is the classical linear analog with changed hypotheses. It also lists the paper among the references for a Lieb-Robinson bound with a gap. See [[Critical Phenomena]], [[Renormalization group flow]] and [[Bundle scale space]].

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Renormalization group flow]]; [[Bundle scale space]]; [[hastings-2004-locality-quantum-markov]].

## BibTeX

```bibtex
@article{hastings2006spectral,
  author        = {Hastings, Matthew B. and Koma, Tohru},
  title         = {Spectral Gap and Exponential Decay of Correlations},
  journal       = {Communications in Mathematical Physics},
  volume        = {265},
  number        = {3},
  pages         = {781--804},
  year          = {2006},
  doi           = {10.1007/s00220-006-0030-4},
  eprint        = {math-ph/0507008},
  archivePrefix = {arXiv}
}
```
