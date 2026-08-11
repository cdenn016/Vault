---
type: paper
title: Limits of Dense Graph Sequences
aliases:
  - Lovász Szegedy dense graph limits
authors:
  - László Lovász
  - Balázs Szegedy
year: 2006
arxiv: math/0408173
url: https://doi.org/10.1016/j.jctb.2006.05.002
tags:
  - cluster/multi-agent
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Limits of Dense Graph Sequences

> [!info] Citation
> László Lovász and Balázs Szegedy. “Limits of Dense Graph Sequences.” *Journal of Combinatorial Theory, Series B* 96(6):933–957, 2006. [doi:10.1016/j.jctb.2006.05.002](https://doi.org/10.1016/j.jctb.2006.05.002); [arXiv:math/0408173](https://arxiv.org/abs/math/0408173).

## TL;DR

A dense graph sequence whose finite homomorphism/subgraph densities converge has a symmetric measurable function $W:[0,1]^2\to[0,1]$ as a limit object, and conversely such functions generate convergent dense graph sequences.

## Problem & setting

Ordinary graph convergence does not directly compare graphs with growing vertex sets. For dense graphs, counts of every fixed finite pattern provide a scale-independent observable family. The question is whether convergence of those observables admits a concrete limiting representation.

## Method

The authors study homomorphism densities, construct measurable kernel limit objects, prove representation and converse results, and characterize limit parameters using properties including reflection positivity.

## Key results

- Convergence of all fixed finite homomorphism densities yields a graphon-type measurable limit.
- The limit object determines those limiting densities, up to its natural nonuniqueness.
- Conversely, every admissible symmetric measurable kernel arises as a dense graph limit.

## Relevance to this research

The paper identifies what must converge before an increasing-agent dense-graph model has a genuine limit: a separating family of finite-pattern observables, not merely one global loss or average degree. It suggests graph-size sweeps that track motif/homomorphism densities and test whether learned interaction kernels stabilize.

## Scope limits

This is a dense unweighted/simple-graph limit theory. It does not automatically cover sparse graphs, time-evolving graphs, directed or matrix-valued gauge links, graph-dependent latent spaces, or a DLR/infinite-volume Gibbs measure. Extending it requires an appropriate decorated/sparse limit framework and separate tightness/identifiability arguments.

## Cross-links

- [[Coarse Graining]]
- [[Renormalization group flow]]
- [[Multi-agent variational free energy]]

## BibTeX

```bibtex
@article{lovasz2006limits,
  title   = {Limits of Dense Graph Sequences},
  author  = {Lov{\'{a}}sz, L{\'{a}}szl{\'{o}} and Szegedy, Bal{\'{a}}zs},
  journal = {Journal of Combinatorial Theory, Series B},
  volume  = {96},
  number  = {6},
  pages   = {933--957},
  year    = {2006},
  doi     = {10.1016/j.jctb.2006.05.002},
  eprint  = {math/0408173},
  archivePrefix = {arXiv}
}
```
