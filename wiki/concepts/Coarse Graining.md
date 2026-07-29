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
updated: 2026-07-28
---

# Coarse Graining

Coarse graining is the procedure of integrating out or aggregating microscopic degrees of freedom to obtain an effective description at a larger scale, discarding detail while preserving relevant macroscopic behavior. It is the operational heart of statistical mechanics, the [[Renormalization group flow|renormalization group]], and emergent (entropic) descriptions of dynamics, and underlies the program's meta-agent hierarchy and [[Renormalization-group flow of beliefs|renormalization-group flow of beliefs]].

## Three operations that are routinely conflated

The MAgent exact-ELBO white paper's coarse-graining chapter makes a distinction the rest of the literature usually leaves implicit, and it is the sharpest available statement of what "coarse-graining" can mean inside a variational bound.

| Operation | Evidence $\log p(o)$ | Achievable bound |
|---|---|---|
| **Restriction** of the recognition family (e.g. tying a cluster to a common value) | unchanged | **lowered** |
| **Exact marginalization** of generative latents | unchanged (Fubini) | **raised** (collapsed VB) |
| **Model replacement** — discarding rather than integrating | **changed** | not comparable |

Only the third moves the evidence, and it is misspecification rather than coarse-graining: a bound computed for one model stands in no order relation to the evidence of a replaced model. The first two move the bound in *opposite* directions, which is the sharpest demonstration that they are not two descriptions of one procedure.

## Renormalizability is additivity of the defining parameter

Two literatures reach the same criterion independently, and it is the most portable fact on this page.

**Networks.** [[garuccio-2023-multiscale-network-renormalization]] proves that the *unique* edge-independent random-graph model form-invariant under **every** node partition is $p_{ij} = 1 - e^{-\delta x_i x_j f(d_{ij})}$, with node fitness $x_i$ additive under aggregation and the density parameter $\delta$ exactly invariant. The corresponding failure taxonomy is quotable: the configuration model, degree-corrected SBM and preferential attachment are non-renormalizable *because* their defining quantity (the degree) "is neither preserved nor additively transformed upon renormalization." A corollary worth carrying: **scale-free** and **scale-invariant** are different, largely orthogonal properties.

**Beliefs.** The white paper's closure proposition is the same principle with a matrix-valued parameter. Tying a cluster is a congruence $\Lambda_c = S^\top \Lambda S$ by the $0/1$ aggregation matrix, under which the within-cluster Laplacian contributions cancel identically and

$$(\Lambda_c)_{IJ} = -\sum_{i\in I,\, j\in J} W_{ij}, \qquad (\Lambda_c)_{II} = \sum_{i\in I} A_i + \sum_{i \in I,\, j\notin I} W_{ij},$$

so **the coarse coupling is exactly the sum of the fine couplings on cut edges** — a renormalization rule that is derived rather than posited, requiring no conductance ansatz. Marginalization, by contrast, is a Schur complement, which manufactures couplings between previously uncoupled agents and need not preserve the sign structure. The complementarity is the practical conclusion: *marginalization preserves the evidence and breaks the form; tying preserves the form and costs bound.*

> [!note] Editorial: the open theorem. The white paper proves **closure**; [[garuccio-2023-multiscale-network-renormalization|MSM]] proves **uniqueness**. The natural next result is the MAgent analogue — that block-diagonal PSD self terms plus a PSD-matrix-weighted graph Laplacian is the *unique* family of Gaussian interaction precisions closed under $0/1$ congruence for every partition. Neither the network-RG literature (scalar throughout) nor the graph-reduction literature (Doerfler–Bullo, Loukas: explicitly scalar-weighted) covers matrix-weighted precisions, so this case is open in both.

## What is lossless, and what a scale even is

**Sufficiency.** With constituents linked to a parent by $y_i \mid b \sim \mathcal N(\Omega_i b, R_i)$, the likelihood factors so that $T(y) = \sum_i \Omega_i^\top R_i^{-1} y_i$ is *sufficient* for the parent and the quadratic-term matrix is the precision-addition rule. Reduction to $T$ therefore discards nothing, and minimal sufficient statistics are unique up to bijection, so the reduction is canonical. A transported arithmetic mean is not sufficient; the [[Fisher information metric|Fisher]] information gap between the two rules measures constituent heterogeneity, which is the precise sense in which averaging is safe on a coherent cluster and lossy otherwise.

**The direction of the flow.** [[berman-2023-bayesian-renormalization]] fixes the RG parameter as $\tau = 1/T$ with $T$ the observation count: coarse-graining *widens* the posterior, inference *narrows* it. Precision addition increases $T$. Combined with sufficiency, this says that **precision pooling is not a coarse-graining at all** — it is a change of coordinates that runs the flow toward the UV — and only the family restriction is a renormalization step. This resolves a recurring puzzle in the [[Ouroboros multi-scale dynamics|tower]]: a coarse agent is *more* certain than its constituents, which is backwards for a coarse-graining and correct for a sufficient statistic.

**Selecting the scale.** Two complementary criteria, developed in the MAgent repo at `docs/derivations/2026-07-28-renormalization-literature-application.md`. [[villegas-2023-laplacian-renormalization-group|Laplacian RG]] locates the scale spectrally, from peaks of the entropic susceptibility $C(\tau) = -dS/d\log\tau$ of the density matrix $e^{-\tau L}/Z$, and hands over the partition as diffusion-equivalence cells. [[berman-2023-bayesian-renormalization|Bayesian RG]] prices it: tying kills the within-cluster *difference* subspace, and forcing a direction to a point is cheap exactly when its precision is *large*, so the selection objective is $\max_S \tfrac12\log\det(B_\perp^\top \Lambda B_\perp)$ over the orthogonal complement of the tied subspace. Because the restriction cost is a pure log-determinant it is **observation-independent** — the price of coarsening is a property of the coupling structure, not of the data — which is what makes a resolution scale attach to a *model* rather than to a run.

> [!warning] Contradiction in orientation, and it is only apparent
> Laplacian/Wilsonian schemes renormalize the **sample space** and keep the **soft** (small-eigenvalue) modes. Bayesian/[[berman-2023-bayesian-renormalization|BKS]] schemes renormalize the **model space** and keep the **stiff** (large-Fisher) directions. On one and the same matrix these select opposite subspaces. They are dual constructions on different spaces, not rival answers; but a sentence of the form "coarse-graining keeps the relevant directions" is ambiguous between them and, read the wrong way, is false.

## Related

[[Renormalization group flow]], [[Renormalization-group flow of beliefs]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]], [[Fisher information metric]], [[Graph Laplacian]], [[Entropic Force]], [[Mean-Field Approximation]], [[Evidence lower bound (ELBO)]]

## Sources

- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant connection probability; additivity as the renormalizability criterion; the scale-free vs. scale-invariant demarcation.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector; diffusion-equivalence supernodes.
- [[gabrielli-2025-network-renormalization]] — the three-step program and the survey placing geometric, Laplacian and multiscale schemes against it.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; stiff/sloppy as relevant/irrelevant; $\tau = 1/T$ fixing the direction of the flow.
- [[beny-osborne-2015-info-geometric-rg]] — coarse-graining as metric contraction on a statistical manifold.
- [[garciaperez-2018-multiscale]] — geometric renormalization of real networks by latent-space proximity.
- [[verlinde-2011-entropic-gravity]] — coarse-graining and entropic descriptions of dynamics.
