---
type: paper
title: Renyi Divergence and Kullback-Leibler Divergence
aliases:
  - "van Erven & Harremoes 2014 — Renyi Divergence and KL"
authors:
  - Tim van Erven
  - Peter Harremoes
year: 2014
arxiv: "1206.2459"
url: https://arxiv.org/abs/1206.2459
tags:
  - cluster/info-geometry
  - project/transformer
  - field/statistics
  - field/mathematics
status: stub
created: 2026-06-18
updated: 2026-06-18
---

# Renyi Divergence and Kullback-Leibler Divergence

> [!info] Citation
> Tim van Erven and Peter Harremoes (2014). *Renyi Divergence and Kullback-Leibler Divergence.* IEEE Transactions on Information Theory 60(7), 3797-3820. arXiv:1206.2459. https://arxiv.org/abs/1206.2459

## TL;DR

This is the definitive survey of the Renyi divergence of order alpha, a one-parameter family of "distances" between probability distributions that interpolates through and generalizes the Kullback-Leibler (KL) divergence. The paper collects, unifies, and extends the analytic properties of the family: how it behaves as a function of its order alpha, when it is convex, when it is continuous, how it varies with sigma-algebras, and what extremal/Pythagorean geometry it satisfies. The single fact that anchors it for our purposes is that the order alpha -> 1 limit of [[Renyi divergence]] recovers exactly the ordinary KL divergence, so KL is not a separate object but one slice of the [[Alpha-divergence]] continuum.

## Problem & setting

For two probability measures P and Q and an order alpha in (0,1) union (1, infinity), the Renyi divergence of order alpha is

D_alpha(P || Q) = 1/(alpha - 1) * log integral p^alpha q^(1 - alpha) d mu,

a monotone transform of the alpha-th order Hellinger/chi-type integral. The family is indexed so that small alpha emphasizes the bulk where Q has mass (mode-covering / mass-covering behavior) and large alpha emphasizes the worst-case ratio p/q (mode-seeking behavior). Renyi divergence stands to Renyi entropy as KL divergence stands to Shannon entropy, but unlike KL it is not generally an f-divergence in the standard sense and its behavior across the order axis is subtle. The paper's aim is to give a single rigorous reference for these properties, valid on general measurable spaces (not only finite alphabets) and across the full range of orders including the boundary cases alpha = 0, 1, infinity.

## Method

The work is a unifying mathematical treatment rather than an experiment. The authors:

- Define D_alpha consistently for all orders in [0, infinity], filling in the limiting cases by continuity (notably alpha -> 1 giving KL, alpha -> 0 giving a log-probability-of-support quantity, and alpha -> infinity giving the worst-case max log-ratio).
- Establish monotonicity of alpha |-> D_alpha (the divergence is non-decreasing in the order) and characterize where it is continuous and where it can jump.
- Prove convexity statements: joint convexity / convexity in the second argument and the behavior of D_alpha under mixtures, which underwrites variational and minimax arguments.
- Generalize the information-geometric **Pythagorean inequality** to orders other than 1, describing how the alpha-projection of a distribution onto a convex set of distributions decomposes the divergence.
- Extend data-processing and the channel-capacity / minimax-redundancy correspondence to continuous inputs for all alpha.

## Key results

- **alpha -> 1 limit is KL.** D_1(P || Q) = KL(P || Q); the family is continuous through order 1, so KL is the distinguished member, not an exception.
- **Monotone in order.** D_alpha is non-decreasing in alpha, giving an ordered ladder of increasingly conservative divergences from the mass-covering small-alpha regime to the worst-case large-alpha regime.
- **Convexity.** D_alpha(P || Q) is jointly convex for alpha in (0,1] and convex in Q across the range, the property that makes alpha-divergence objectives amenable to optimization and to bounding via Jensen.
- **Pythagorean / projection geometry.** A Pythagorean inequality holds for general alpha, generalizing the alpha = 1 identity from classical information geometry and characterizing alpha-projections onto convex families.
- **Boundary and limiting cases.** Clean characterizations of alpha = 0, 1/2 (related to Hellinger affinity / Bhattacharyya), 1 (KL), 2 (related to the chi-square divergence), and infinity (max log-ratio).
- **Data processing.** D_alpha is non-increasing under stochastic maps (channels), extended here to continuous settings, so it is a legitimate contraction-respecting measure of information loss.

## Relevance to this research

Our model exposes a `divergence_family = "renyi"` knob: the variational objective is not pinned to KL but lives on the alpha axis, with KL recovered as the order alpha -> 1 limit. This paper is the rigorous backstop for that design choice. Three connections are concrete:

1. **The objective.** The ELBO / variational free energy in the model penalizes the divergence between the per-token Gaussian belief (mu, Sigma) and a prior. Replacing KL by D_alpha turns the standard bound into a Renyi variational bound; van Erven and Harremoes guarantee that this family is continuous through alpha = 1, so the Renyi objective degrades gracefully to the familiar KL free energy and we can anneal alpha without discontinuity. The variational use of this family is operationalized in [[li-turner-2016-renyi-vi]]; this paper supplies the underlying divergence theory those bounds rely on.

2. **Convexity and well-posedness.** The convexity and data-processing results tell us which alpha settings keep the objective convex in the variational parameters and contraction-respecting under the model's filtering updates, which matters for the stability of the E-step belief updates.

3. **Information-geometric coupling.** The Pythagorean inequality for general alpha is the alpha-generalization of the classical projection identity that sits behind [[Natural gradient]] and the dual-affine view of [[Fisher information metric]]. Because the model mixes Renyi divergences with natural-gradient / Fisher-preconditioned updates, the consistency of alpha-projection geometry is exactly what licenses treating the belief update as a projection onto a constraint family.

> [!note] Editorial: This paper is a theory reference, not a learning method; its role in the wiki is to certify that the "alpha as a dial, KL as alpha=1" picture used throughout the program is mathematically sound, including at the boundary and under the data-processing and convexity properties the optimizer implicitly assumes.

## Cross-links

- Concepts: [[Renyi divergence]], [[Alpha-divergence]], [[Fisher information metric]], [[Natural gradient]]
- Methods / applications: [[li-turner-2016-renyi-vi]] (Renyi-divergence variational inference), [[amari-2000-methods-information-geometry]] (information-geometric projection and dual connections), [[Variational free energy]], [[Evidence lower bound (ELBO)]]
- Program: [[VFE Transformer Program]]

```bibtex
@article{vanerven2014renyi,
  title   = {R\'enyi Divergence and Kullback-Leibler Divergence},
  author  = {van Erven, Tim and Harremo\"es, Peter},
  journal = {IEEE Transactions on Information Theory},
  volume  = {60},
  number  = {7},
  pages   = {3797--3820},
  year    = {2014},
  doi     = {10.1109/TIT.2014.2320500},
  eprint  = {1206.2459},
  archivePrefix = {arXiv},
  primaryClass  = {cs.IT},
  url     = {https://arxiv.org/abs/1206.2459}
}
```
