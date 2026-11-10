---
type: reference
title: "Locality in Quantum and Markov Dynamics on Lattices and Networks"
aliases: ["hastings2004locality"]
authors: ["M. B. Hastings"]
year: 2004
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.93.140402"
arxiv: "cond-mat/0405587"
url: "https://doi.org/10.1103/PhysRevLett.93.140402"
tags: [cluster/multi-agent, project/multi-agent, field/physics, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Locality in Quantum and Markov Dynamics on Lattices and Networks

> [!info] Citation
> Hastings, M. B. (2004). *Locality in Quantum and Markov Dynamics on Lattices and Networks*. Physical Review Letters, 93(14), 140402. [DOI](https://doi.org/10.1103/PhysRevLett.93.140402); [arXiv](https://arxiv.org/abs/cond-mat/0405587)

[Local PDF](../pdfs/hastings-2004-locality-quantum-markov.pdf), 4 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The Letter considers gapped systems with quantum or Markov dynamics and nearly degenerate low-lying states, and proves a decomposition of ground or stationary state correlation functions into an exponentially decaying piece and a piece set by matrix elements between the low-lying states.

## Problem & setting

The author starts from the expectation that a gap implies a finite correlation length and extends an earlier result, in which a gap between the ground and first excited states bounds the correlation length by a characteristic velocity divided by the gap, to systems with several almost degenerate low-energy states. The results apply to finite-range lattice Hamiltonians under some technical conditions on the group velocity, and the Letter discusses applications to band structures, classical Markov processes and systems on general networks.

## Method

The abstract names a local approximation to the negative-energy (annihilation) part of an operator in a gapped system as the main tool of the proof. Some of the proofs are deferred to other papers.

## Key results

For two operators at distance $l$ and vanishing low-energy window, the connected correlator equals the expectation of the symmetrized product of the low-energy parts of the operators, up to a term of order $\exp(-l/\xi)$.

## Relevance to this research

The manuscript cites the paper, with a Lieb-Robinson bound and a later paper on the spectral gap, as the quantum counterpart of its exponential clustering theorem, and notes that this paper treats Markov dynamics on networks. The manuscript's theorem applies with signed weights and in the common-code regime, which it distinguishes from the cited setting. The link is to the manuscript's analysis of correlation length and scale; see [[Critical Phenomena]], [[Renormalization group flow]] and [[Bundle scale space]].

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Renormalization group flow]]; [[Bundle scale space]]; [[hastings-2006-spectral-gap-exponential]].

## BibTeX

```bibtex
@article{hastings2004locality,
  author        = {Hastings, M. B.},
  title         = {Locality in Quantum and {Markov} Dynamics on Lattices and Networks},
  journal       = {Physical Review Letters},
  volume        = {93},
  number        = {14},
  pages         = {140402},
  year          = {2004},
  doi           = {10.1103/PhysRevLett.93.140402},
  eprint        = {cond-mat/0405587},
  archivePrefix = {arXiv}
}
```
