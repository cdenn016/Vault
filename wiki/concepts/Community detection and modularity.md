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
updated: 2026-06-19
---

# Community detection and modularity

## Definition

**Community detection** is the problem of partitioning the vertices of a graph into groups that are densely connected internally and sparsely connected to the rest. Its standard quality functional is the **modularity**
$$
Q = \frac{1}{2m}\sum_{ij}\Big(A_{ij} - \frac{k_i k_j}{2m}\Big)\,\delta(c_i, c_j),
$$
where $A_{ij}$ is the adjacency (or weight) matrix, $k_i=\sum_j A_{ij}$ the degree, $m=\tfrac12\sum_i k_i$ the total edge weight, and $\delta(c_i,c_j)=1$ when $i,j$ share a community. $Q$ measures the excess of within-community edges over a degree-preserving random null model. A complementary, spectral, characterization comes from the graph Laplacian $L = D - A$: its smallest nonzero eigenvalue $\lambda_2$, the **Fiedler value** or **algebraic connectivity**, measures how hard the graph is to cut, and the associated **Fiedler eigenvector** supplies a spectral bipartition. The size of the **spectral gap** $\lambda_2$ also sets the convergence rate of Laplacian (consensus) dynamics $\dot{x} = -Lx$, whose solutions average toward agreement at rate $\lambda_2$.

## Why it matters here

This is the graph-theoretic substrate that the [[Gauge-Theoretic Multi-Agent VFE Model]] re-derives from variational free energy. The model's **cluster detector** (`ConsensusDetector`, see [[Meta-agents and hierarchical emergence]]) is a community-detection routine in disguise: it builds a pair-edge graph from the post-transport belief-coherence score $\Gamma(\{i,j\},x)$ and takes connected components as candidate meta-agents, exactly the dense-subgraph logic modularity formalizes. The **culture-closure ratio** (internal versus boundary $\gamma$-weighted KL) is a per-cluster, gauge-weighted analogue of the modularity criterion: a block is a legitimate coarse-graining target when within-cluster disagreement is small relative to its boundary. And the **constrained spectral gap** $\lambda_{I,w}$ computed from a cluster's belief-coupling Laplacian, with parent "mass" $m_I = \lambda_{I,w}\,\lambda_{\min}(F(q_I))$, is precisely the Fiedler value adapted to the belief graph. Laplacian consensus convergence is the dynamical picture behind condensation: agents whose belief graph has a large spectral gap average toward agreement quickly, justifying their replacement by a single meta-agent. These threads close the participatory coarse-graining loop of [[participatory-it-from-bit]].

## Details

The resolution limit ([[fortunato-2010-community-detection]]) is the pitfall most relevant to threshold-based meta-agent formation: modularity maximization cannot resolve communities smaller than a scale set by $\sqrt{2m}$, so genuinely distinct small clusters get fused. Any fixed $\Gamma_{\min}$ / fixed-threshold blocking inherits the same defect — the right resolution is scale-dependent, which is why the model's coarse-graining is iterated as an RG sweep ([[Renormalization-group flow of beliefs]]) rather than applied once at a single threshold. The spectral and modularity views connect through the Fiedler eigenvector ([[fiedler-1973-algebraic-connectivity]]) and the Newman-Girvan generative null model ([[newman-girvan-2004-community-structure]]); the consensus dynamics whose rate $\lambda_2$ governs are the multi-agent counterpart of opinion-averaging on networks ([[olfati-saber-2007-consensus]]).

## Sources

- [[newman-girvan-2004-community-structure]] — modularity $Q$ and the degree-preserving null model; the divisive community-detection benchmark.
- [[fortunato-2010-community-detection]] — survey of community-detection methods and the resolution-limit pitfall that bears on fixed-threshold meta-agent formation.
- [[fiedler-1973-algebraic-connectivity]] — algebraic connectivity $\lambda_2$, the Fiedler value and eigenvector; spectral cut and the constrained spectral gap.
- [[olfati-saber-2007-consensus]] — Laplacian consensus dynamics and convergence rate set by the spectral gap, the dynamical basis of condensation.

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Renormalization-group flow of beliefs]]
- [[participatory-it-from-bit]]
- [[Multi-agent variational free energy]]
- [[Fisher information metric]]
- [[Gauge-Theoretic Multi-Agent VFE Model]]
