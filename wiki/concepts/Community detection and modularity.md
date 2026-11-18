---
type: concept
title: "Community detection and modularity"
aliases:
  - "Modularity Q"
  - "Newman-Girvan modularity"
  - "Algebraic connectivity"
  - "Fiedler value"
  - "Spectral gap"
  - "Graph community detection"
  - "Community Structure"
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - cluster/methodology
  - project/multi-agent
status: draft
created: 2026-06-19
updated: 2026-11-18
---

# Community detection and modularity

## Definition

**Community detection** is the problem of partitioning the vertices of a graph into groups that are densely connected internally and sparsely connected to the rest. Its standard quality functional is the **modularity**
$$
Q = \frac{1}{2m}\sum_{ij}\Big(A_{ij} - \frac{k_i k_j}{2m}\Big)\,\delta(c_i, c_j),
$$
where $A_{ij}$ is the adjacency (or weight) matrix, $k_i=\sum_j A_{ij}$ the degree, $m=\tfrac12\sum_i k_i$ the total edge weight, and $\delta(c_i,c_j)=1$ when $i,j$ share a community. $Q$ measures the excess of within-community edges over a degree-preserving random null model. A complementary, spectral, characterization comes from the graph Laplacian $L = D - A$: its smallest nonzero eigenvalue $\lambda_2$, the **Fiedler value** or **algebraic connectivity**, measures how hard the graph is to cut, and the associated **Fiedler eigenvector** supplies a spectral bipartition. The size of the **spectral gap** $\lambda_2$ also sets the convergence rate of Laplacian (consensus) dynamics $\dot{x} = -Lx$, whose solutions average toward agreement at rate $\lambda_2$.

## Details

The resolution limit ([[fortunato-2010-community-detection]]) is the central pitfall of threshold-based blocking: modularity maximization cannot resolve communities smaller than a scale set by $\sqrt{2m}$, so genuinely distinct small clusters get fused. The spectral and modularity views connect through the Fiedler eigenvector ([[fiedler-1973-algebraic-connectivity]]) and the Newman-Girvan generative null model ([[newman-girvan-2004-community-structure]]); the consensus dynamics whose rate $\lambda_2$ governs are the multi-agent counterpart of opinion-averaging on networks ([[olfati-saber-2007-consensus]]).

## Sources

- [[newman-girvan-2004-community-structure]] — modularity $Q$ and the degree-preserving null model; the divisive community-detection benchmark.
- [[fortunato-2010-community-detection]] — survey of community-detection methods and the resolution-limit pitfall.
- [[fiedler-1973-algebraic-connectivity]] — algebraic connectivity $\lambda_2$, the Fiedler value and eigenvector; spectral cut.
- [[olfati-saber-2007-consensus]] — Laplacian consensus dynamics and convergence rate set by the spectral gap.

## See also

- [[Renormalization group flow]]
- [[Fisher information metric]]
