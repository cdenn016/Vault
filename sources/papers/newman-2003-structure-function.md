---
type: paper
title: "The Structure and Function of Complex Networks"
aliases: ["Newman 2003", "Structure and function of complex networks"]
authors: ["Newman M. E. J."]
year: 2003
url: https://doi.org/10.1137/S003614450342480
tags: [cluster/social-physics, project/social-physics, field/physics, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# The Structure and Function of Complex Networks

> [!info] Citation
> Newman, M. E. J. (2003). *The Structure and Function of Complex Networks*. SIAM Review, 45(2), 167-256. doi:10.1137/S003614450342480.

## TL;DR
Newman's review is the canonical reference card for network science. It synthesizes the empirical regularities of real networks — heavy-tailed degree distributions, high clustering, short path lengths, assortative or disassortative mixing, and community structure — alongside the generative models that reproduce them (Erdos-Renyi, configuration model, small-world, preferential attachment) and the dynamical processes that run on top (percolation, epidemic spreading, search, resilience to node removal). It is the single best inventory of the structural vocabulary used to characterize a network and to relate its topology to its function.

## What it establishes
The review formalizes the standard battery of structural measures: the degree distribution $P(k)$ and its moments; the clustering coefficient
$$C = \frac{3 \times (\text{number of triangles})}{\text{number of connected triples}};$$
the mean geodesic path length $\ell$; degree-degree assortativity via the Pearson correlation of endpoint degrees; and modularity-based community structure. It connects these to function through results on percolation and giant-component thresholds — for a degree distribution with generating function $G_0(x)$ the giant component appears when $\sum_k k(k-2)P(k) > 0$ — and on epidemic thresholds that vanish for scale-free degree distributions with diverging second moment. The configuration model and its generating-function machinery give analytical handles on all of these.

## Relevance to this research
This is the core reference for the structural language used to characterize the model's attention/influence graph and to coarse-grain it into meta-agents. It supplies the diagnostics — clustering, modularity, assortativity, giant-component conditions — that distinguish a fragmented population from one capable of global consensus, and the generating-function machinery that lets one predict when a connected belief-sharing component exists at all. The relevance is foundational-structural rather than dynamical: it provides the measurement toolkit, not the belief-inertia equations. See [[Network structure — small-world and scale-free]], [[Community detection and modularity]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Network structure — small-world and scale-free]]
- Related sources: [[albert-barabasi-2002-statistical-mechanics]], [[boccaletti-2006-structure-dynamics]], [[erdos-renyi-1959-random-graphs]]

## BibTeX
```bibtex
@article{newman2003structure,
  author  = {Newman, M. E. J.},
  title   = {The Structure and Function of Complex Networks},
  journal = {SIAM Review},
  year    = {2003},
  volume  = {45},
  number  = {2},
  pages   = {167--256},
  doi     = {10.1137/S003614450342480}
}
```
