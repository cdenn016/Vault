---
type: reference
title: "Lieb-Robinson Bounds and the Exponential Clustering Theorem"
aliases: ["nachtergaele2006lieb"]
authors: ["Bruno Nachtergaele", "Robert Sims"]
year: 2006
venue: "Communications in Mathematical Physics"
doi: "10.1007/s00220-006-1556-1"
arxiv: "math-ph/0506030"
url: "https://doi.org/10.1007/s00220-006-1556-1"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Lieb-Robinson Bounds and the Exponential Clustering Theorem

> [!info] Citation
> Nachtergaele, B., Sims, R. (2006). *Lieb-Robinson Bounds and the Exponential Clustering Theorem*. Communications in Mathematical Physics, 265(1), 119-130. [DOI](https://doi.org/10.1007/s00220-006-1556-1); [arXiv](https://arxiv.org/abs/math-ph/0506030)

[Local PDF](../pdfs/nachtergaele-2006-lieb-robinson-bounds.pdf), 12 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper proves a Lieb-Robinson bound on the group velocity for a broad class of discrete quantum systems on a vertex set with a metric, and uses it to show that a nonvanishing spectral gap implies exponential clustering of correlations in the ground state.

## Problem & setting

The introduction frames the claim as a folk theorem of quantum lattice models: a spectral gap goes with exponential decay of spatial correlations. One direction has known exceptions, namely models with exponential decay but no gap, and the paper supplies a rigorous proof of the other direction. In relativistic field theory a mass gap implies exponential decay because of strict locality; non-relativistic lattice models have a finite propagation speed up to exponentially small corrections, which the Lieb-Robinson bound captures. The authors describe their clustering proof as a rigorous version of an argument of Hastings.

## Method

The systems have a finite-dimensional Hilbert space at each vertex of a set $V$ with a metric $d$, an interaction $\Phi$ assigning a self-adjoint operator to each subset, and Hamiltonian $H=\sum_X\Phi(X)$. A norm $\|\Phi\|_\lambda$ weights interaction terms by an exponential in the diameter of their support. The bound controls the commutator $[\tau_t(A),B]$ for observables $A$ and $B$ supported far apart. The proof does not require an underlying lattice or translation invariance, so graphs and other metric spaces are covered.

## Relevance to this research

The manuscript cites this paper as the quantum source for exponential clustering from a Lieb-Robinson bound plus a gap, and presents its own light cone and clustering results as classical, discrete, finite-range counterparts of known forms, with changed hypotheses (signed weights and a common-code regime). The link to the vault is correlation length and locality in coarse-grained collectives, see [[Critical Phenomena]] and [[Coarse Graining]]. The related reference on the finite group velocity itself is not in this packet.

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Coarse Graining]]; [[ornstein-1914-accidental-deviations-density]].

## BibTeX

```bibtex
@article{nachtergaele2006lieb,
  author        = {Nachtergaele, Bruno and Sims, Robert},
  title         = {{Lieb-Robinson} Bounds and the Exponential Clustering Theorem},
  journal       = {Communications in Mathematical Physics},
  volume        = {265},
  number        = {1},
  pages         = {119--130},
  year          = {2006},
  doi           = {10.1007/s00220-006-1556-1},
  eprint        = {math-ph/0506030},
  archivePrefix = {arXiv}
}
```
