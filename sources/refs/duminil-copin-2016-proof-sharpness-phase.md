---
type: reference
title: "A New Proof of the Sharpness of the Phase Transition for Bernoulli Percolation and the Ising Model"
aliases: ["duminilcopin2016new"]
authors: ["Hugo Duminil-Copin", "Vincent Tassion"]
year: 2016
venue: "Communications in Mathematical Physics"
doi: "10.1007/s00220-015-2480-z"
url: "https://doi.org/10.1007/s00220-015-2480-z"
tags: [cluster/multi-agent, project/multi-agent, field/mathematics, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# A New Proof of the Sharpness of the Phase Transition for Bernoulli Percolation and the Ising Model

> [!info] Citation
> Duminil-Copin, H., Tassion, V. (2016). *A New Proof of the Sharpness of the Phase Transition for Bernoulli Percolation and the Ising Model*. Communications in Mathematical Physics, 343(2), 725-745. [DOI](https://doi.org/10.1007/s00220-015-2480-z); [arXiv](https://arxiv.org/abs/1502.03050)

[Local PDF](../pdfs/duminil-copin-2016-proof-sharpness-phase.pdf), 23 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A new proof of sharpness of the phase transition for Bernoulli percolation and the Ising model, valid for infinite-range models on locally finite transitive infinite graphs.

## Problem & setting

Couplings are invariant under a group acting transitively on a locally finite infinite graph. Percolation is defined with bond $\{x,y\}$ open with probability $1-e^{-\beta J_{x,y}}$, and $\beta_c$ is the critical parameter.

## Method

The proof works with a quantity $\phi_\beta(S)$, the expected number of open boundary edges of a finite set $S$ that are connected to the origin inside $S$, and a differential inequality obtained by differentiating the connection probability in $\beta$. The Ising section is stated to be independent of the percolation proof but analogous.

## Key results

For percolation, the susceptibility is finite for $\beta<\beta_c$ and a mean-field lower bound holds above $\beta_c$. For finite-range models the probability of an open path to distance $n$ decays exponentially for $\beta<\beta_c$. For the Ising model, the susceptibility is finite below $\beta_c$, a mean-field lower bound holds above, and for finite-range models two-point correlations decay exponentially in distance below $\beta_c$.

## Relevance to this research

The Collective Agents manuscript cites the paper in its scale section for exponential smallness, in the distance to a set of agents, of the information that observations carry about one agent's convention below the critical point on transitive graphs. It connects to [[Critical Phenomena]] and [[Phase transitions in social systems]].

## Cross-links

[[Collective agents literature map]]; [[Critical Phenomena]]; [[Phase transitions in social systems]]; [[ding-2023-correlation-length-two]].

## BibTeX

```bibtex
@article{duminilcopin2016new,
  author  = {Duminil-Copin, Hugo and Tassion, Vincent},
  title   = {A New Proof of the Sharpness of the Phase Transition for {Bernoulli} Percolation and the {Ising} Model},
  journal = {Communications in Mathematical Physics},
  volume  = {343},
  number  = {2},
  pages   = {725--745},
  year    = {2016},
  doi     = {10.1007/s00220-015-2480-z}
}
```
