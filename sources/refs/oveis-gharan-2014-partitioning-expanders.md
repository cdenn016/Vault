---
type: reference
title: "Partitioning into Expanders"
aliases: ["oveisgharan2014partitioning"]
authors: ["Shayan Oveis Gharan", "Luca Trevisan"]
year: 2014
venue: "Proceedings of the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2014)"
doi: "10.1137/1.9781611973402.93"
arxiv: "1309.3223"
url: "https://doi.org/10.1137/1.9781611973402.93"
tags: [cluster/multi-agent, project/multi-agent, field/cs-ml, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Partitioning into Expanders

> [!info] Citation
> Oveis Gharan, S., Trevisan, L. (2014). *Partitioning into Expanders*. Proceedings of the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2014), 1256--1266. [DOI](https://doi.org/10.1137/1.9781611973402.93), [arXiv](https://arxiv.org/abs/1309.3223)

[Local PDF](../pdfs/oveis-gharan-2014-partitioning-expanders.pdf), 18 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper proves a robust version of the fact that the $k$-th smallest eigenvalue of the normalized Laplacian is positive exactly when the graph has fewer than $k$ components, and gives a simple spectral algorithm that finds the corresponding partition.

## Problem & setting

For an undirected graph with normalized Laplacian eigenvalues $\lambda_1\le\lambda_2\le\dots$, a set of small conductance need not be a good cluster, because it can be loosely connected inside or even disconnected. The paper asks for a partition into sets that have low conductance in the graph and high conductance as induced subgraphs.

## Method

The algorithm is a local search that calls spectral partitioning as a subroutine and does not use higher-order eigenfunctions. The analysis also works with the order-$k$ conductance constant $\rho(k)$, the smallest value of the maximum conductance over $k$ disjoint subsets.

## Key results

If $\lambda_k>0$, then for some $\ell\le k-1$ the vertex set splits into $\ell$ parts with outer conductance bounded in terms of $\lambda_\ell$ and inner conductance of order $\lambda_k/k^2$. When $\lambda_{k+1}$ is at least polynomial in $k$ times $\lambda_k^{1/4}$, the algorithm returns a $k$-partition whose induced subgraphs have markedly larger conductance than the parts have in the whole graph. A technical lemma replaces an earlier assumption of an exponential-in-$k$ gap between $\rho(k)$ and $\rho(k+1)$ by a gap factor $1+\epsilon$.

## Relevance to this research

The manuscript cites the theorem as the converse direction of a spectral-gap statement: a gap forces a partition into sets with high internal and low external conductance, for the normalized combinatorial Laplacian under a quantitative gap condition. It states that the transfer of this result to diffusive precisions with grounding is not established, and that the paper is known to it from the abstract. The result bears on how a collective of communicating agents is delimited in a graph; see [[Spectral graph theory]], [[Graph Laplacian]] and [[Community detection and modularity]].

## Cross-links

[[Collective agents literature map]]; [[Spectral graph theory]]; [[Graph Laplacian]]; [[Community detection and modularity]].

## BibTeX

```bibtex
@inproceedings{oveisgharan2014partitioning,
  author        = {{Oveis Gharan}, Shayan and Trevisan, Luca},
  title         = {Partitioning into Expanders},
  booktitle     = {Proceedings of the Twenty-Fifth Annual ACM-SIAM Symposium on Discrete Algorithms (SODA 2014)},
  pages         = {1256--1266},
  publisher     = {Society for Industrial and Applied Mathematics},
  address       = {Philadelphia, PA},
  year          = {2014},
  doi           = {10.1137/1.9781611973402.93},
  eprint        = {1309.3223},
  archivePrefix = {arXiv}
}
```
