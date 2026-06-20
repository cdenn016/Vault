---
type: paper
title: "A simple model of global cascades on random networks"
aliases: ["Watts 2002", "Global cascade model"]
authors: ["Watts D. J."]
year: 2002
url: https://doi.org/10.1073/pnas.082090499
tags: [cluster/social-physics, project/social-physics, field/physics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# A simple model of global cascades on random networks

> [!info] Citation
> Watts, D. J. (2002). *A simple model of global cascades on random networks*. PNAS, 99(9), 5766-5771. doi:10.1073/pnas.082090499.

## TL;DR
Watts analyzes when a small initial perturbation — a handful of seed adopters — can trigger a global cascade that flips a finite fraction of the whole population, under a *fractional-threshold* rule on a random network. Each node adopts once the fraction of its neighbors who have adopted exceeds its individual threshold $\phi$, drawn from a distribution. The central result is a *cascade window*: cascades are possible only in an intermediate band of mean connectivity, bounded below by sparsity (the network is disconnected) and above by density (each node has so many neighbors that no single seed can move its fraction past threshold).

## What it establishes
The key analytical device is the set of *vulnerable* nodes — those that will adopt if even a single neighbor adopts, i.e. nodes with degree $k \le \lfloor 1/\phi \rfloor$. A global cascade requires the subgraph of vulnerable nodes to percolate, which yields, via generating functions, the condition that the cascade window is bounded by
$$\sum_k k(k-1)\, P(k)\, \rho_k = \langle k \rangle,$$
where $\rho_k$ is the probability a degree-$k$ node is vulnerable. Below the lower critical connectivity the vulnerable cluster does not span; above the upper critical connectivity individual influence is too diluted; only inside the window does a single seed reliably ignite a system-spanning cascade, and there the cascade-size distribution is bimodal — most seeds fizzle, a few go global.

## Relevance to this research
The cascade window predicts exactly when a few seed agents can flip the whole population's beliefs — the threshold-on-network analogue of the model's social-coupling-driven consensus transition. It connects the influence-graph's connectivity (and degree heterogeneity) to whether large belief cascades exist at all and how big they get, which is the network-theoretic face of the consensus-versus-fragmentation question the VFE dynamics confront. The tie is strong, with the caveat that Watts's rule is binary adoption rather than continuous Gaussian belief flow. See [[Threshold models and complex contagion]], [[Opinion dynamics]], and [[Echo chambers and polarization]].

## Cross-links
- Concept: [[Threshold models and complex contagion]]
- Related sources: [[granovetter-1978-threshold-models]], [[centola-macy-2007-complex-contagion]], [[kempe-kleinberg-tardos-2003-influence-maximization]]

## BibTeX
```bibtex
@article{watts2002cascades,
  author  = {Watts, Duncan J.},
  title   = {A simple model of global cascades on random networks},
  journal = {Proceedings of the National Academy of Sciences},
  year    = {2002},
  volume  = {99},
  number  = {9},
  pages   = {5766--5771},
  doi     = {10.1073/pnas.082090499}
}
```
