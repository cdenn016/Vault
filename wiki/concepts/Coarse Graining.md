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
updated: 2026-11-11
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

## Memory of a coarse variable that is not closed, November 11, 2026

A coarse variable of a linear system is closed exactly when the kernel of the coarse map is invariant under the dynamics. When it is not, the summary obeys a closed recursion plus a defect, and the size of that defect can be bounded through the structure of the fine update. For the average of agents that fuse messages literally with fixed gains, [[dennis-2026-collective-agents-approximate-meta-agent]] bounds the defect through the dispersions of the row sums and of the column sums of the update of the members' means and a mixing constant on their deviations, and shows that the one-step closure defect in information form has a floor that mixing does not lower, so that the energy of the defect and the kernel weights are the better measures of memory. The synthesis is [[Approximate meta-agent theorem]].

## Markov error of a retained coordinate without reversibility, November 11, 2026

A second measure of the memory of a coarse variable is its Markov error, the largest distance over lags between the autocorrelation of the variable and the geometric sequence of the slowest mode of the fine dynamics. For one coordinate of a stable linear recursion, [[dennis-2026-collective-agents-approximate-blanket-conditions]] bounds it without assuming reversibility, under a power bound on the block of the deviations and a gap between the retained coefficient and the rate of that block whose square exceeds four times the constant of the power bound times the product of the row and column dispersions. The coordinate is a first-order autoregression driven by the deviations through the column dispersion, so equal column sums give an exact autoregression for every noise; for isotropic noise, white deviations and equal row sums the bound also vanishes whatever the column dispersion, a case in which the one-step closure defect is positive. For isotropic noise the error is of second order in the row and column dispersions, with the constant of the power bound entering to the second power. For anisotropic noise it is of first order in the column dispersion, and neither that order nor the powers of the constant can be lowered. The same source records a way in which a summary fails that does not involve the dynamics: a coarse sensory state that is not sufficient for the finer record it summarizes sets an information term in the error of any belief computed from it. Both are placed in [[Approximate meta-agent theorem]].

## What a memoryless elimination of internal states loses, November 11, 2026

Eliminating internal variables by substituting their conditional expectation given the retained ones is a coarse-graining step whose error can be computed in the linear-Gaussian case. For a stable linear diffusion split into retained and internal states, [[dennis-2026-collective-agents-renormalization-results]] records that the residual of the internal states about their regression on the retained ones is a state with dynamics of its own. The retained states therefore obey a generalized Langevin equation in the sense of [[zwanzig-1961-memory-effects]] and [[mori-1965-transport-collective-motion]], and the elimination drops its memory kernel, an initial-state term and the color of the force. The retained process is Markov with a transition law independent of the initial law exactly when the retained states do not read the internal ones.

The size of what is dropped is proved under the hypothesis that the noise factors of both groups of states are invertible. A reduction that keeps the stationary covariance of the retained states must use their own noise intensity, and it then matches the exact autocovariance in value and in first derivative at lag zero. The error of the autocovariance at every lag is an explicit double integral of the dropped kernel, and relative to the stationary covariance it is at most the product of the relaxation time of the reduction and the integrated norm of the kernel; this bound holds for every stable drift and is not sharp. When the internal rows of the drift and the internal noise intensity are both multiplied by a speed factor $\mathsf s$, and the internal block and the quasi-static drift are stable, the error is $\mathsf c_{\mathrm F}/\mathsf s$ to leading order, uniformly in the lag, with a coefficient computed from two Lyapunov equations. The coefficient is nonzero in the reversible family, whose drift is a symmetric positive definite precision and whose noise factor is the identity, whenever a retained state is coupled to an internal one. For a non-reversible drift it can vanish, and the error is then of order $\mathsf s^{-2}$. If the internal noise matrix, and not its intensity, is multiplied by $\mathsf s$, the error tends to a positive limit whenever the retained states read the internal ones, $M_{\mathrm{ri}}\ne0$.

The expansions in the ratio of timescales of [[vankampen-1985-elimination-fast-variables]] and [[geigenmuller-1983-elimination-fast-variables]] are the classical background. The first-order rate was a numerical observation in the manuscript before it was proved, and the instances behind that observation were not tested against the hypotheses of the proposition. The proposition covers one step of the reduction of a particular partition ([[friston-2023-path-integrals-particular]]); the blanket condition between particles, the projection onto the slow modes of each blanket and the correlations among the induced fluctuations add errors that it does not bound. The fast-slow reading is on [[Geometric singular perturbation theory]].

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

## Collective agents references, November 10, 2026

[[Collective agents literature map]] groups the references ingested on November 10, 2026. Its sections on closure, lumpability and model reduction and on renormalization, aggregation and long memory hold the sources closest to this page, among them [[givon-2004-extracting-macroscopic-dynamics]], [[koch-janusz-2018-mutual-information-neural]], [[gordon-2021-relevance-renormalization-group]] and [[meshulam-2019-coarse-graining-fixed]].
