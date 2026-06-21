---
type: paper
title: "Algebraic Connectivity of Graphs"
aliases:
  - Fiedler 1973
  - Fiedler vector
  - Fiedler (1973) Algebraic Connectivity
authors:
  - Fiedler, Miroslav
year: 1973
arxiv: null
url: http://dml.cz/dmlcz/101168
tags:
  - cluster/social-physics/networks-and-contagion
  - cluster/multi-agent
  - project/social-physics
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Algebraic Connectivity of Graphs

> [!info] Citation
> Fiedler, Miroslav (1973). "Algebraic Connectivity of Graphs." *Czechoslovak Mathematical Journal*, 23(2), 298–305. DOI: [10.21136/CMJ.1973.101168](https://doi.org/10.21136/CMJ.1973.101168). http://dml.cz/dmlcz/101168

## TL;DR
This paper introduces the concept of the *algebraic connectivity* of a graph, defined as the second smallest eigenvalue $a(G)$ of the graph Laplacian matrix $\hat{A}(G)$. Fiedler establishes that $a(G) > 0$ if and only if the graph is connected, and derives tight inequalities relating $a(G)$ to classical vertex and edge connectivities. The paper is the founding reference for what is now called the Fiedler value and Fiedler vector in spectral graph theory.

## Problem & setting
The paper studies how well an eigenvalue of the Laplacian matrix of a graph captures the combinatorial connectivity of the graph. Prior work (Hoffman, Doob, Ray-Chaudhuri, Seidel) had characterized graphs via adjacency spectra; Fiedler's contribution is to isolate the second smallest Laplacian eigenvalue as the natural algebraic analogue of vertex and edge connectivity. For a finite undirected graph $G = (V, E)$ with $n \ge 2$ vertices, the Laplacian $\hat{A}(G)$ is symmetric, positive semidefinite, and has $0$ as its smallest eigenvalue (with eigenvector $\mathbf{e} = (1,\ldots,1)^T$). The ordered eigenvalues are $0 = \lambda_1 \le \lambda_2 = a(G) \le \lambda_3 \le \cdots \le \lambda_n$.

## Method
The analysis uses the Courant–Fischer minimax characterization. Because $\hat{A}(G)\mathbf{e} = 0$, the second smallest eigenvalue satisfies
$$a(G) = \min_{\mathbf{x} \in W} \mathbf{x}^T \hat{A}(G)\, \mathbf{x}, \quad W = \{\mathbf{x} : \mathbf{x}^T\mathbf{x}=1,\; \mathbf{x}^T\mathbf{e}=0\}.$$
Key results are proved by constructing auxiliary graphs (adding or removing vertices/edges), using the superadditivity of $a(\cdot)$ on edge-disjoint unions, and relating eigenvalues of Kronecker-product (categorical product) graphs to those of the factors. The complementary graph $\bar{G}$ plays a central role: $\hat{A}(G)+\hat{A}(\bar{G}) = nI - J$, so $b(G) := n - a(G) = \max_{\mathbf{x}\in W} \mathbf{x}^T\hat{A}(G)\,\mathbf{x}$ equals the largest Laplacian eigenvalue of $G$.

## Key results
- **Connectivity criterion**: $a(G) = 0$ iff $G$ is disconnected (from Perron–Frobenius applied to $(n-1)I - \hat{A}(G)$).
- **Vertex cut bound (Theorem 4.1)**: For non-complete $G$, $a(G) \le v(G) \le e(G)$ where $v(G)$ and $e(G)$ are vertex and edge connectivities.
- **Vertex removal (Prop. 3.3)**: Removing $k$ vertices decreases $a$ by at most $k$: $a(G_1) \ge a(G) - k$.
- **Degree bound (Prop. 3.5)**: $a(G) \le \frac{n}{n-1}\min_i d_i \le \frac{2|E|}{n-1}$.
- **Edge connectivity bound (Theorem 4.3)**: $a(G) \ge 2\,e(G)(1 - \cos(\pi/n))$, with a sharper bound involving the maximum degree.
- **Exact values**: Path: $a = 2(1-\cos(\pi/n))$; circuit: $2(1-\cos(2\pi/n))$; star: $1$; complete graph $K_n$: $n$; $m$-cube: $2$.
- **Complete bipartite graph**: $a(K_{p,q}) = \min(p,q)$.

## Relevance to this research
The Fiedler value and its associated Fiedler vector are the canonical spectral tool for graph connectivity and spectral partitioning. In the social-physics strand of this research program, networks of agents or opinions are analyzed using graph Laplacians; $a(G)$ controls the rate of diffusion/consensus on the graph and governs the second-slowest mode of opinion dynamics. The Laplacian $\hat{A}(G)$ is structurally analogous to the precision-weighted belief-coupling term in the VFE functional: the off-diagonal $-1$ entries correspond to pairwise KL coupling weights $\beta_{ij}$, and $a(G)$ lower-bounds how rapidly coupled beliefs converge. The spectral partitioning intuition (Fiedler vector partitions the graph) is directly related to multi-agent community detection and to how the gauge-equivariant attention matrix $\beta_{ij}$ clusters tokens. The degree-bound $a(G) \le 2|E|/(n-1)$ also resembles the effective connectivity bounds one derives from the attention entropy term in the canonical free energy. In the multi-agent strand specifically, $\lambda_2$ of the agent coupling graph is the project's *constrained spectral gap* and a proxy for the "parent mass" (how strongly a coarse [[Meta-agents and hierarchical emergence|meta-agent]] binds its constituents): a large gap means a tightly bound cluster, while a small gap is the signal that a population is about to split into sub-communities along the Fiedler vector.

## Cross-links
- Concepts: [[Graph Laplacian]], [[Spectral Graph Theory]], [[Community detection and modularity|Algebraic Connectivity]]
- Related sources: [[anderson-morley-1971-laplacian-eigenvalues]]
- Manuscript/Project: [[VFE Transformer Program]], [[SocialPhysics|Social Physics]]

## BibTeX
```bibtex
@article{Fiedler1973,
  author  = {Fiedler, Miroslav},
  title   = {Algebraic Connectivity of Graphs},
  journal = {Czechoslovak Mathematical Journal},
  volume  = {23},
  number  = {2},
  pages   = {298--305},
  year    = {1973},
  doi     = {10.21136/CMJ.1973.101168},
  url     = {http://dml.cz/dmlcz/101168},
}
```
