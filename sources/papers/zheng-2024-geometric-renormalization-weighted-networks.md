---
type: paper
title: "Geometric renormalization of weighted networks"
aliases:
  - "Zheng et al. 2024"
  - "Weighted geometric renormalization"
  - "GRW"
  - "phi-GRW"
  - "sup-GRW"
authors:
  - Zheng, Muhua
  - Garcia-Perez, Guillermo
  - Boguna, Marian
  - Serrano, M. Angeles
year: 2024
arxiv: "2307.00879"
url: https://doi.org/10.1038/s42005-024-01589-7
tags:
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
  - project/social-physics
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-08-16
updated: 2026-08-16
---

# Geometric renormalization of weighted networks

> [!info] Citation
> Zheng, M., Garcia-Perez, G., Boguna, M., & Serrano, M. A. (2024). "Geometric renormalization of weighted networks." *Communications Physics* **7**, 97. DOI: [10.1038/s42005-024-01589-7](https://doi.org/10.1038/s42005-024-01589-7). Preprint: [arXiv:2307.00879](https://arxiv.org/abs/2307.00879).

## TL;DR

The paper extends geometric network renormalization from binary topology to weighted links. Nodes are first grouped into consecutive sectors in a latent similarity geometry. The links between two supernodes are then assigned an aggregate weight from a one-parameter rescaled norm,

$$
\omega'_{IJ}
=C\left(\sum_{e\in E(I,J)}\omega_e^\phi\right)^{1/\phi},
$$

where the exponent is fixed by the weighted hidden-variable model. The sum rule is the case $\phi=1$, while the supremum or maximum rule is recovered as $\phi\to\infty$. Across twelve empirical weighted networks, the maximum-weight protocol often preserves rescaled weight, strength, and disparity statistics better than simple summation. The transformation composes as a semigroup. These are model- and protocol-relative closure results, not evidence that every renormalizable network statistic must be additive.

## Setting and method

The binary scaffold is the geometric soft configuration model on a latent similarity sphere, equivalently a hyperbolic representation. Each node carries a hidden degree, a hidden strength, and a similarity coordinate. A coarse step groups nonoverlapping consecutive nodes in the latent angular order. Two supernodes are linked when at least one microscopic link connects their blocks.

The weighted model couples link strength to hidden degree, hidden strength, and latent distance. Requiring the hidden strength-degree relation to retain its form under blocking determines the exponent $\phi$ of the aggregate. The paper compares three prescriptions: theoretical $\phi$-GRW, maximum-weight sup-GRW, and additive sum-GRW. It also shows the composition law needed for repeated blocking.

The empirical claim is narrower than a universal network theorem. Self-similarity is assessed in rescaled distributions and strength-degree relations for the studied networks. The theoretical closure belongs to the declared weighted geometric hidden-variable family.

## Relevance to the two-channel graph-VFE program

This paper corrects an overbroad reading of the multiscale-network literature. [[garuccio-2023-multiscale-network-renormalization]] identifies additivity as the closure mechanism for its independent-edge family under an OR graph map. Zheng and coauthors exhibit a different closed weighted aggregation family in which addition is only one exponent and the maximum is another limit. “Renormalizability is additivity” is therefore not a protocol-independent rule.

The graph-VFE construction nevertheless has an internal reason to use linear aggregation for its directed edge-event measures. If $\eta$ is a probability measure and $K$ is an input-independent Markov endpoint kernel, then

$$
\sum_{I,J}\sum_{i,j}\eta_{ij}K(I,J\mid i,j)=1.
$$

This is ordinary linear pushforward. Within the paper's $\phi$-norm family, $\phi=1$ is the unique member representable as that fixed Markov-kernel pushforward. Applying a nonlinear norm and restoring normalization with a global constant can produce a normalized object, but it is no longer the same fixed-channel pushforward. The exact KL chain rule used by the graph-VFE construction depends on the latter structure.

> [!note] Editorial: candidate mechanism, not imported theorem. The program's effective-resistance or commute-time distance on a symmetrized directed conductance graph could propose graph-scale blocks without a physical embedding. A sup aggregation could then be tested as a fifth block-formation protocol. This does not import the paper's self-similarity result: effective resistance does not reproduce consecutive angular sectors, the weighted hidden-degree model, or its parameter recursion. Symmetrization also discards directionality, so a genuinely directed extension remains open.

The paper's conclusion explicitly identifies directionality as future work. That boundary matches the present program's two directed edge layers $\beta$ and $\gamma$, but does not solve them. The most defensible use is as a closure and semigroup template for an alternative coarse edge statistic, kept distinct from the linear $\eta$ pushforward required by the exact VFE decomposition.

## Boundaries

The construction assumes a latent metric geometry and externally prescribed consecutive blocks. It does not learn partitions from variational free-energy descent, does not treat two coupled directed row-stochastic channels, does not carry gauge-valued edge transports or holonomy, and does not prove persistence of a hierarchy under evolving beliefs and models. Its maximum-weight rule is not a probability-measure pushforward and does not by itself preserve an evidence or relative-entropy chain rule.

## Cross-links

- Concepts: [[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Coarse Graining]], [[Community detection and modularity]], [[Graph synchronization and connection Laplacians]]
- Related sources: [[garuccio-2023-multiscale-network-renormalization]], [[gabrielli-2025-network-renormalization]], [[villegas-2023-laplacian-renormalization-group]], [[serrano-2008-self-similarity]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{zheng2024geometric,
  author        = {Zheng, Muhua and Garcia-Perez, Guillermo and Boguna, Marian and Serrano, M. Angeles},
  title         = {Geometric renormalization of weighted networks},
  journal       = {Communications Physics},
  volume        = {7},
  pages         = {97},
  year          = {2024},
  doi           = {10.1038/s42005-024-01589-7},
  eprint        = {2307.00879},
  archivePrefix = {arXiv},
  primaryClass  = {physics.soc-ph},
}
```
