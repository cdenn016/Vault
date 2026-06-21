---
type: paper
title: "Multiscale unfolding of real networks by geometric renormalization"
aliases:
  - "García-Pérez 2018"
  - "RGN"
authors:
  - García-Pérez, Guillermo
  - Boguñá, Marián
  - Serrano, M. Ángeles
year: 2018
arxiv: "1706.00394"
url: https://arxiv.org/abs/1706.00394
tags:
  - cluster/social-physics/networks-and-contagion
  - project/social-physics
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Multiscale unfolding of real networks by geometric renormalization

> [!info] Citation
> García-Pérez, G., Boguñá, M., & Serrano, M. Á. (2018). "Multiscale unfolding of real networks by geometric renormalization." *Nature Human Behaviour*, 2, 583–590. arXiv:1706.00394.

## TL;DR
The paper introduces a geometric renormalization group (RGN) for complex networks embedded in hidden metric spaces, proving that real scale-free networks are self-similar under this flow. By coarse-graining geometrically proximate nodes into supernodes on the S1 (circle) model, the authors unfold networks into a self-similar multilayer shell that reveals coexisting scales and their interplay. Two direct applications are demonstrated: high-fidelity "Mini-me" downscaled network replicas that faithfully reproduce critical dynamics, and a multiscale greedy-routing navigation protocol in hyperbolic space that substantially improves single-layer success rates.

## Problem & setting
Complex networks exhibit multiple coexisting scales, but the small-world property entangles them, making it difficult to define self-similarity or extract length-scale symmetries. Prior topological approaches (box-covering, shortest-path renormalization) failed to find full structural self-similarity or relied on non-geometric criteria that could not explain why self-similarity arises. The development of hidden metric space models (S1/H2) — which embed nodes in a low-dimensional geometric space and couple connection probability to popularity and angular similarity — opens the door to a genuinely geometric renormalization.

## Method
The authors define a geometric renormalization operator $F_r$ of resolution $r$ acting on a network map $\mathcal{M}(\mathcal{T}, \mathcal{G})$ (topology + geometry). Consecutive blocks of $r$ nodes on the S1 circle are coarse-grained into supernodes; inter-supernode links are drawn if any inter-block link existed. Supernode hidden degrees and angular positions are updated as the $\ell^\beta$-norm generalized center of mass:

$$\kappa_i^{(l+1)} = \left(\sum_{j=1}^{r} (\kappa_j^{(l)})^\beta\right)^{1/\beta}, \qquad \theta_i^{(l+1)} = \left(\frac{\sum_j (\theta_j \kappa_j)^\beta}{\sum_j \kappa_j^\beta}\right)^{1/\beta},$$

with global rescalings $\mu^{(l+1)} = \mu^{(l)}/r$ and $R^{(l+1)} = R^{(l)}/r$, while $\beta^{(l+1)} = \beta^{(l)}$. These recurrence relations are shown analytically to keep the renormalized network congruent with the S1 model, establishing renormalizability. The operator has abelian semigroup structure. Average degree flows as $\langle k \rangle^{(l+1)} = r^\nu \langle k \rangle^{(l)}$, with scaling exponent $\nu$ depending on $\gamma$ (degree exponent) and $\beta$ (clustering parameter), yielding three connectivity phases. The paper validates self-similarity on six real networks spanning technology, biology, transportation, and language. Mini-me replicas are produced by adding a geometric link-pruning step to match the original average degree. Multiscale navigation exploits the S1/H2 isomorphism for greedy hyperbolic routing across layers.

## Key results
Real scale-free networks (Internet AS, human metabolic, music chord transitions, world airports, human proteome, word-adjacency in Darwin) all exhibit self-similar degree distributions, degree-degree correlations, and clustering spectra along the RGN flow, with curves collapsing upon rescaling by the layer average degree. Community structure is preserved along the flow: the community partition at any coarse-grained layer induces a high-modularity partition of the original network, with high normalized mutual information. All six real networks fall in the small-world phase (phase I, $\nu > 0$), where the RGN flow tends toward a fully connected graph. Mini-me replicas reproduce the critical behavior of the Ising model, SIS epidemic spreading, and Kuramoto synchronization with high fidelity across all tested scales. Multiscale navigation raises the greedy routing success rate significantly over single-layer baselines with only a mild increase in average path stretch.

## Relevance to this research
The geometric renormalization framework is directly relevant to the multi-agent and social-physics components of this research program. The S1/H2 hidden metric space, in which node similarity is encoded as angular proximity and popularity as degree, is a concrete geometric realization of the kind of latent-space structure that underpins attention mechanisms in the VFE transformer: the connection probability $p_{ij} = (1 + \chi_{ij}^\beta)^{-1}$ with $\chi_{ij} = R\Delta\theta_{ij}/(\mu\kappa_i\kappa_j)$ is structurally analogous to a softmax attention kernel governed by similarity and scale. The renormalization semigroup structure — iterative coarse-graining that preserves the model family — parallels hierarchical message-passing or multi-scale belief propagation ideas relevant to active inference over networks. The community-structure preservation across scales is relevant to multi-agent opinion dynamics: it implies that mesoscopic cluster structure (social groups, epistemic communities) is stable under scale changes, which could constrain or inform the prior structure in multi-agent VFE models. The phase diagram ($\nu$ vs. $\gamma$, $\beta$) quantifying when networks flow toward full connectivity vs. ring-like sparsity is a concrete theoretical result about collective behavior that connects to social-physics questions about consensus and polarization.

## Cross-links
- Concepts: [[Hidden Metric Space]], [[Renormalization group flow|Renormalization Group]], [[Network structure — small-world and scale-free|Scale-Free Networks]], [[Hyperbolic Geometry]], [[Community detection and modularity|Community Structure]]
- Related sources: [[boguna-2010-sustaining|boguna2010sustaining]], [[serrano-2008-self-similarity|serrano2008self]]
- Manuscript/Project: [[VFE Transformer Program]], [[Gauge-Theoretic Multi-Agent VFE Model|MAgent Model]]

## BibTeX
```bibtex
@article{garciaperez2018multiscale,
  author  = {Garc{\'i}a-P{\'e}rez, Guillermo and Bogu{\~n}{\'a}, Mari{\'a}n and Serrano, M.~{\'A}ngeles},
  title   = {Multiscale unfolding of real networks by geometric renormalization},
  journal = {Nature Human Behaviour},
  volume  = {2},
  pages   = {583--590},
  year    = {2018},
  doi     = {10.1038/s41562-018-0418-2},
  eprint  = {1706.00394},
  archivePrefix = {arXiv},
}
```
