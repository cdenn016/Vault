---
type: reference
title: "Stability of Mixed-State Quantum Phases via Finite Markov Length"
aliases: ["sang2025stability"]
authors: ["Shengqi Sang", "Timothy H. Hsieh"]
year: 2025
venue: "Physical Review Letters"
doi: "10.1103/PhysRevLett.134.070403"
arxiv: "2404.07251"
url: "https://doi.org/10.1103/PhysRevLett.134.070403"
tags: [cluster/multi-agent, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---

# Stability of Mixed-State Quantum Phases via Finite Markov Length

> [!info] Citation
> Sang, S., Hsieh, T. H. (2025). *Stability of Mixed-State Quantum Phases via Finite Markov Length*. Physical Review Letters, 134(7), 070403. [DOI](https://doi.org/10.1103/PhysRevLett.134.070403), [arXiv](https://arxiv.org/abs/2404.07251)

[Local PDF](../pdfs/sang-2025-stability-mixed-state.pdf), 12 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The authors propose the Markov length, the scale at which quantum conditional mutual information decays exponentially, as the mixed-state analog of the energy gap for characterizing phases and transitions.

## Problem & setting

For pure states, two states are in the same phase when local unitary evolution relates them, and the energy gap controls correlation decay and stability under perturbation. For mixed states the operational definition is conversion by local Lindbladian evolution, but Lindbladian evolution is generally non-invertible, so each direction must be established separately. The paper asks for a stability criterion that does not rely on a Hamiltonian.

## Method

The conditional mutual information $I(A:C|B)$ is examined as a function of the width $r$ of the region $B$ separating $A$ from $C$; the length scale of its exponential decay is the Markov length $\xi$.

## Key results

The authors argue that if $\xi$ stays finite along evolution under a local Lindbladian, a quasi-local Lindbladian evolution can reverse it, so the states lie in one phase. Applied to the toric code under decoherence, $\xi$ is finite everywhere except at the decodability transition, where it diverges, and the conditional mutual information maps to the free-energy cost of point defects in the random-bond Ising model. The word "argue" is the authors'; the first pages do not present this as a rigorous theorem.

## Relevance to this research

The manuscript adapts the Markov length to define a decay length for conditional dependence across a blanket in its theory of collectives, and cites this paper for the quantum origin of the notion. Related vault pages are [[Markov Blanket]], [[Mutual information]] and [[Coarse Graining]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Mutual information]]; [[Coarse Graining]]; [[raz-2009-estimating-lieb-robinson]].

## BibTeX

```bibtex
@article{sang2025stability,
  author        = {Sang, Shengqi and Hsieh, Timothy H.},
  title         = {Stability of Mixed-State Quantum Phases via Finite {Markov} Length},
  journal       = {Physical Review Letters},
  volume        = {134},
  number        = {7},
  pages         = {070403},
  year          = {2025},
  doi           = {10.1103/PhysRevLett.134.070403},
  eprint        = {2404.07251},
  archivePrefix = {arXiv}
}
```
