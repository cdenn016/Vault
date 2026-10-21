---
type: concept
title: "Renormalization group flow"
aliases:
  - "RG flow"
  - "Renormalization group"
  - "Wilsonian RG"
  - "Block-spin renormalization"
  - "Functional renormalization group"
  - "Epsilon expansion"
tags:
  - cluster/social-physics
  - cluster/multi-agent
  - cluster/methodology
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-10-20
---

# Renormalization group flow

## Definition

The **renormalization group (RG)** is the physics framework for relating a system's
description across scales by repeatedly *coarse-graining* — integrating out short-distance
(high-momentum) degrees of freedom — and *rescaling* back to the original units. Each such
step is a map on the space of couplings $\{g_a\}$ of an effective Hamiltonian or action; the
sequence of maps is the **RG flow**. Following Kadanoff's block-spin intuition, Wilson turned
this picture into a concrete transformation ([[wilson-1971-rg-critical-phenomena]]): group the
microscopic variables into blocks, replace each block by a single effective variable, and read
off how the couplings of the blocked system differ from the original. Iterating produces a
trajectory in coupling space.

Two structural facts make the flow powerful. **Fixed points** $g^\star$ of the transformation
are scale-invariant theories; linearizing the flow about a fixed point sorts the
eigen-perturbations into **relevant** (eigenvalue $>1$, growing under coarse-graining and
controlling macroscopic physics), **marginal** ($=1$), and **irrelevant** ($<1$, decaying and
washing out). This relevant/irrelevant taxonomy explains **universality**: microscopically
different systems that flow to the same fixed point share the same large-scale behavior because
they differ only in irrelevant directions. The flow's linearization also yields the critical
exponents, which can be computed perturbatively via the **$\epsilon = 4-d$ expansion** around
the upper critical dimension ([[wilson-kogut-1974-epsilon-expansion]]). Modern formulations
recast the whole flow exactly: the **functional (non-perturbative) RG** of
[[berges-tetradis-wetterich-2002-nonperturbative-rg]] tracks a scale-dependent *effective
average action* $\Gamma_k$ — equal to the bare action at the UV cutoff and the full effective
action as $k\to 0$ — obeying the exact Wetterich flow
$$
\partial_k \Gamma_k = \tfrac{1}{2}\mathrm{STr}\left[\big(\Gamma_k^{(2)}+R_k\big)^{-1}\partial_k R_k\right],
$$
whose controlled truncations capture non-perturbative physics. The standard pedagogical account
of all of this — block-spin scaling, the Wilsonian effective action, finite-size scaling, and
the Gaussian/saddle-point treatment of the partition function — is [[cardy-1996-scaling-renormalization]].

## Renormalization without a lattice

Network and statistical constructions supply other choices of scale.

**Networks.** [[garuccio-2023-multiscale-network-renormalization]] supplies a model-specific independent-edge OR-aggregation benchmark. The parameterization, loop convention and uniqueness scope are recorded in [[Coarse Graining]]. Additivity is not a general criterion for every RG construction. [[gabrielli-2025-network-renormalization]] supplies the broader network-RG comparison.

**Scale from statistics rather than from space.** [[berman-2023-bayesian-renormalization]] derives the RG scale from the [[Fisher information metric]] instead of from a momentum cutoff. Writing $T$ for the number of observations and $\tau = 1/T$, the posterior flow of Bayesian updating is a Fokker–Planck equation structurally identical to the Polchinski ERG equation, with the Fisher metric as diffusion kernel: inference and renormalization are the same equation with the flow reversed. Because $D_{KL}$ is Fisher to second order, the metric measures distinguishability, and a distinguishability scale *is* a correlation length — one that exists even where no physical scale does. Relevant/irrelevant becomes stiff/sloppy, i.e. large/small Fisher eigenvalue.

> [!warning] The two schemes renormalize different spaces and keep opposite modes
> Wilsonian and Laplacian schemes act on the **sample space** and retain the **soft**, small-eigenvalue modes. Bayesian renormalization acts on the **model space** and retains the **stiff**, large-Fisher directions. Applied to one and the same operator they select complementary subspaces. They are dual constructions, not rival answers — but the phrase "coarse-graining keeps the relevant directions" is ambiguous between them.

## Composability is the exception, not the rule

A step of the flow and the *composability of steps* are different properties, and the second is
rarer than textbook pictures suggest. Exact composability of real-space maps holds for pure
decimation (marginalization composes trivially), asymptotically at fixed points where the
couplings outside the retained family have died, and on the hierarchical lattices of
[[berker-1979-hierarchical-lattice-rg]] and [[kadanoff-1976-migdal-recursion]], which compose
exactly because the substrate is built self-similarly. Away from those cases,
[[griffiths-1979-rg-transformations]] and [[van-enter-1993-rg-pathologies]] show that real-space
maps can fail even to produce well-defined renormalized theories; the probabilistic cousin is
the exceptional character of Markov-chain lumpability
([[kemeny-snell-1960-finite-markov-chains]]).

## Sources

- [[wilson-1971-rg-critical-phenomena]] — the RG transformation realizing Kadanoff block-spin scaling; fixed points and the relevant/irrelevant/marginal operator taxonomy.
- [[wilson-kogut-1974-epsilon-expansion]] — the long-form review; effective-action formalism and the $\epsilon = 4-d$ perturbative expansion of critical exponents.
- [[berges-tetradis-wetterich-2002-nonperturbative-rg]] — functional (non-perturbative) RG: the effective average action $\Gamma_k$ and the exact Wetterich flow; the language for the continuum-limit question.
- [[cardy-1996-scaling-renormalization]] — standard pedagogy: Wilsonian effective action, Gaussian/saddle-point closure, finite-size scaling.
- [[bialek2001predictability|bialek-2001-predictability-complexity]] — predictive information and its sub-extensive growth; the information-theoretic reading of what coarse-graining keeps versus discards.
- [[geshkovski-2023-mathematical-transformers]] — attention as an interacting-particle consensus flow producing clusters.
- [[gabrielli-2025-network-renormalization]] — RG on heterogeneous networks: the three-step program; geometric, Laplacian and multiscale frameworks compared.
- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant model; additivity as the renormalizability criterion; scale-free versus scale-invariant.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; inference as the inverse of exact RG flow.
- [[genest-zidek-1986-pooling]], [[dietrich-list-2016-opinion-pooling]], [[bordley-1982-multiplicative-pooling]] — opinion-pooling taxonomy fixing the aggregator used at the RG blocking step.
- [[griffiths-1979-rg-transformations]], [[van-enter-1993-rg-pathologies]] — rigorous limits of real-space RG: renormalized interactions need not exist; non-Gibbsian images.
- [[berker-1979-hierarchical-lattice-rg]], [[kadanoff-1976-migdal-recursion]] — hierarchical lattices, the self-similar substrates on which real-space RG composes exactly.
- [[kemeny-snell-1960-finite-markov-chains]] — lumpability as the exceptional condition for a coarse-grained Markov chain to stay Markov.
- [[csiszar-1975-i-divergence-geometry]] — I-projection and IPF convergence.

## See also

- [[Meta-agents and hierarchical emergence]]
- [[Ouroboros multi-scale dynamics]]
- [[Geometric singular perturbation theory]]
- [[Belief inertia]]
- [[participatory-it-from-bit]] · [[Gauge-Theoretic Multi-Agent VFE Model]] · [[VFE Transformer Program]]
