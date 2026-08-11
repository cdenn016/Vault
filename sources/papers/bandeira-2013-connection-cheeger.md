---
type: paper
title: A Cheeger Inequality for the Graph Connection Laplacian
aliases:
  - Bandeira Singer Spielman 2013
authors:
  - Afonso S. Bandeira
  - Amit Singer
  - Daniel A. Spielman
year: 2013
arxiv: "1204.3873"
url: https://doi.org/10.1137/120875338
tags:
  - cluster/gauge-theory
  - cluster/multi-agent
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# A Cheeger Inequality for the Graph Connection Laplacian

> [!info] Citation
> Afonso S. Bandeira, Amit Singer, and Daniel A. Spielman. “A Cheeger Inequality for the Graph Connection Laplacian.” *SIAM Journal on Matrix Analysis and Applications* 34(4):1611–1630, 2013. [doi:10.1137/120875338](https://doi.org/10.1137/120875338); [arXiv:1204.3873](https://arxiv.org/abs/1204.3873).

## TL;DR

For synchronization over $O(d)$, the paper proves a Cheeger-type relation between the smallest eigenvalues of a graph connection Laplacian and the minimum frustration of vertex assignments, yielding worst-case guarantees for a spectral synchronization algorithm.

## Problem & setting

Noisy edge measurements specify relative orthogonal transformations. The objective is to assign an orthogonal frame to every vertex while minimizing disagreement with those measurements. The connection-Laplacian spectrum is a natural relaxation, but it needs a rounding guarantee.

## Method

The authors formulate frustration constants for partial and full $O(d)$ synchronization, analyze eigenvectors of the normalized connection Laplacian, and round spectral solutions to group-valued vertex assignments. Cheeger-type inequalities relate spectral energy to achievable frustration.

## Key results

- The connection-Laplacian spectrum controls synchronization frustration in the stated $O(d)$ setting.
- The associated spectral method receives a worst-case approximation guarantee.
- The analysis separates partial synchronization/anchoring effects from full group synchronization.

## Relevance to this research

The result motivates a falsifiable recovery diagnostic: compare the lowest connection-Laplacian eigenvalues with directly optimized edge frustration and cycle holonomy. It is also a benchmark for whether a proposed “geometric coherence” statistic has a theorem behind it.

## Scope limits

> [!warning] Group mismatch
> The theorem is for compact orthogonal synchronization. It does **not automatically cover** noncompact $\mathrm{GL}^{+}(2)$, where Euclidean transpose is not group inverse, condition numbers can diverge, and the standard block Laplacian may fail to have the same bounded/self-adjoint structure. A project claim needs a compact reduction or a separately proved metric, adjoint, coercivity, and rounding theorem.

## Cross-links

- [[Graph synchronization and connection Laplacians]]
- [[Graph Laplacian]]
- [[Holonomy]]
- [[Gauge transformation]]

## BibTeX

```bibtex
@article{bandeira2013cheeger,
  title   = {A Cheeger Inequality for the Graph Connection Laplacian},
  author  = {Bandeira, Afonso S. and Singer, Amit and Spielman, Daniel A.},
  journal = {SIAM Journal on Matrix Analysis and Applications},
  volume  = {34},
  number  = {4},
  pages   = {1611--1630},
  year    = {2013},
  doi     = {10.1137/120875338},
  eprint  = {1204.3873},
  archivePrefix = {arXiv}
}
```
