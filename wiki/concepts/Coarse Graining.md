---
type: concept
title: "Coarse Graining"
aliases:
  - "Coarse-graining"
  - "Blocking"
  - "Aggregation invariance"
tags:
  - cluster/info-geometry
  - cluster/multi-agent
  - cluster/social-physics/networks-and-contagion
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-10-20
---

# Coarse Graining

## Three operations that are routinely conflated

Three operations have different effects on a variational bound.

| Operation | Evidence $\log p(o)$ | Achievable bound |
|---|---|---|
| **Restriction** of the recognition family (e.g. tying a cluster to a common value) | unchanged | **lowered** |
| **Exact marginalization** of generative latents | unchanged (Fubini) | **raised** (collapsed VB) |
| **Model replacement** — discarding rather than integrating | **changed** | not comparable |

Only the third moves the evidence, and it is misspecification rather than coarse-graining: a bound computed for one model stands in no order relation to the evidence of a replaced model. The first two move the bound in *opposite* directions, which is the sharpest demonstration that they are not two descriptions of one procedure.

## Additive closure under a declared aggregation rule

**Networks.** [[garuccio-2023-multiscale-network-renormalization]] treats independent Bernoulli edges in binary undirected graphs, retaining self-loops. OR aggregation over nonoverlapping partitions preserves the specified fitness/dyadic family,
$$
p_{ij}=1-e^{-\delta x_i x_j F_{ij}},\quad i\ne j,\qquad
p_{ii}=1-e^{-\delta x_i^2F_{ii}/2}.
$$
For positive block fitnesses,
$$
X_I=\sum_{i\in I}x_i,\qquad
F_{IJ}=\frac{\sum_{i\in I,j\in J}x_i x_jF_{ij}}{X_I X_J}.
$$
Here $F=f(d)$ and $\delta$ is unchanged. Internal unordered edges and loops contribute once to a coarse self-loop. The reported uniqueness is conditional on the declared parameterization and additive fitness. [Published paper, Section II, Eqs. (1)–(7), Appendix A](https://journals.aps.org/prresearch/pdf/10.1103/PhysRevResearch.5.043101). The [retained PDF](../../sources/pdfs/garuccio-2023-multiscale-network-renormalization-arxiv-v3.pdf) is arXiv v3.

## Recovery and partition selection

Losslessness has at least three strengths. A statistic can preserve one law, a channel can preserve
one tangent or score direction, or one parameter-independent recovery kernel can reconstruct an
entire statistical experiment. [[blackwell-1953-experiment-comparison]] supplies the last and
strongest comparison; [[Statistical experiment comparison and deficiency]] records quantitative
relaxations when exact recovery fails.

For finite Markov dynamics, [[geiger-2013-kl-aggregation]] proposes a KL-divergence-rate objective
and information-bottleneck search for candidate partitions, while
[[geiger-temmel-2013-information-preserving-aggregation]] gives conditions for lossless aggregation
in its declared finite-chain setting. [[ahn-2018-bucket-renormalization]] is a complementary
factor-graph/tensor-network approximate-inference comparator.

## Related

[[Renormalization group flow]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]], [[Graph Laplacian]], [[Cellular sheaves and sheaf Laplacians]] (sheaf Kron reduction and its failure), [[Entropic Force]], [[Mean-Field Approximation]], [[Evidence lower bound (ELBO)]]

## Sources

- [[blackwell-1953-experiment-comparison]] — experiment-level comparison by common
  parameter-independent garbling/recovery kernels.
- [[geiger-2013-kl-aggregation]] — KL-rate Markov aggregation and an information-bottleneck
  partition-search baseline.
- [[geiger-temmel-2013-information-preserving-aggregation]] — lossless finite-chain aggregation
  under explicit structural conditions.
- [[ahn-2018-bucket-renormalization]] — bucket-renormalization approximate inference as a
  factor-graph/RG comparator.

- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant connection probability; additivity as the renormalizability criterion; the scale-free vs. scale-invariant demarcation.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector; diffusion-equivalence supernodes.
- [[gabrielli-2025-network-renormalization]] — the three-step program and the survey placing geometric, Laplacian and multiscale schemes against it.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; stiff/sloppy as relevant/irrelevant; $\tau = 1/T$ fixing the direction of the flow.
- [[beny-osborne-2015-info-geometric-rg]] — coarse-graining as metric contraction on a statistical manifold.
- [[garciaperez-2018-multiscale]] — geometric renormalization of real networks by latent-space proximity.
- [[verlinde-2011-entropic-gravity]] — coarse-graining and entropic descriptions of dynamics.
