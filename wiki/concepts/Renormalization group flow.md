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
updated: 2026-08-17
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
\partial_k \Gamma_k \;=\; \tfrac{1}{2}\,\mathrm{STr}\!\left[\big(\Gamma_k^{(2)}+R_k\big)^{-1}\,\partial_k R_k\right],
$$
whose controlled truncations capture non-perturbative physics. The standard pedagogical account
of all of this — block-spin scaling, the Wilsonian effective action, finite-size scaling, and
the Gaussian/saddle-point treatment of the partition function — is [[cardy-1996-scaling-renormalization]].

## Why it matters here

This page is the **physics counterpart** of the project-specific
[[Renormalization-group flow of beliefs]]: the latter applies the machinery summarized here to a
population of variational beliefs, and the former (this page) is the established theory it
borrows from. The correspondence is tight. A step of meta-agent formation in
[[Meta-agents and hierarchical emergence]] — replacing a coherent cluster of micro-agents by a
single coarse-grained parent — is a **block-spin RG step** in the space of
[[Variational free energy]] functionals: the cluster is the block, the pooled meta-belief is the
effective block variable, and the parent's couplings are the renormalized couplings. The
[[Ouroboros multi-scale dynamics|Ouroboros tower]] is then a discrete RG trajectory, and the
question of whether that tower has a well-defined continuum/scaling limit is exactly the
fixed-point question functional RG ([[berges-tetradis-wetterich-2002-nonperturbative-rg]]) is
built to answer.

The relevant/irrelevant taxonomy of [[wilson-1971-rg-critical-phenomena]] supplies the
principled answer to *which* belief structures survive aggregation: the few belief couplings
that grow under coarse-graining set the emergent macro-dynamics, while the many that decay are
integrated out — a retention criterion that also dovetails with the predictive-information
picture of [[bialek2001predictability|bialek-2001-predictability-complexity]], where coarse-graining discards extensive
detail and keeps the sub-extensive, learnable part. The "integrate out the fast/fine modes to
get an effective slow theory" operation is the same move that
[[Geometric singular perturbation theory]] makes rigorous at the level of fast-slow dynamics:
RG flow is its scale-indexed, statistical-mechanical sibling. And the consensus/clustering that
attention induces on a token cloud — proven as an interacting-particle flow in
[[geshkovski-2023-mathematical-transformers]] — is the microdynamics whose repeated
coarse-graining the belief-RG describes, linking this concept to the
[[VFE Transformer Program]] as well as the multi-agent model.

> [!note] Editorial: the identification of meta-agent coarse-graining with a *bona fide* RG
> step (with a genuine fixed point and universal large-scale content) is a program goal of
> [[participatory-it-from-bit]], not yet a proven theorem; functional RG is the tool the project
> would use to make it quantitative.

## Details

There are two complementary closure techniques the project inherits. The **Wilsonian
effective action** (integrate out fast modes, keep a renormalized action for the slow modes) is
the conceptual route; the **Gaussian / saddle-point (Laplace) approximation** to the partition
function — expanding the free energy about its dominant configuration — is the practical route
used to get a tractable effective free energy at each scale, both taught in
[[cardy-1996-scaling-renormalization]]. **Finite-size scaling** is the correction relevant to a
*finite* ensemble of agents: it governs how emergent macro-quantities approach their
thermodynamic-limit values, the natural diagnostic when the "block" is a small cluster rather
than an infinite lattice. The $\epsilon$-expansion of [[wilson-kogut-1974-epsilon-expansion]] is
the prototype of a controlled small-parameter expansion about a fixed point that any
quantitative belief-RG claim would emulate.

A subtlety worth flagging is the **pooling choice** at the blocking step. Coarse-graining must
aggregate the constituent beliefs into one parent belief, and opinion-pooling theory
([[genest-zidek-1986-pooling]], [[dietrich-list-2016-opinion-pooling]]) shows the aggregator is
a substantive commitment: the consensus-preserving *linear* (arithmetic) pool and the
externally-Bayesian *log-linear / multiplicative* pool ([[bordley-1982-multiplicative-pooling]])
satisfy mutually incompatible axioms. The project's meta-agent uses a gauge-covariant *linear*
sandwich average for blocking (to avoid the multiplicative "veto"), so the RG blocking operator
here is a linear pool — a modeling decision the RG framework leaves open and the pooling
literature adjudicates.

## Renormalization without a lattice

Everything above assumes the thing being coarse-grained sits on a lattice. Two recent lines drop that assumption in opposite directions, and between them they cover the situation the multi-agent program is actually in.

**Networks.** [[gabrielli-2025-network-renormalization]] reviews how RG survives the loss of homogeneity, symmetry, geometry and locality. It factors renormalization into three steps — define coarse variables, marginalize fine detail, renormalize parameters — and places three frameworks against them: geometric renormalization takes its blocks from a latent hyperbolic embedding ([[garciaperez-2018-multiscale]]), [[villegas-2023-laplacian-renormalization-group|Laplacian RG]] takes them spectrally from diffusion, and the [[garuccio-2023-multiscale-network-renormalization|multiscale model]] is agnostic about blocks entirely, instead characterizing the unique connection probability invariant under *every* aggregation. The last of these yields the criterion worth carrying away: **a family is renormalizable when its defining parameter is additive under aggregation**, which is why the configuration model, degree-corrected SBM and preferential attachment are not — their defining quantity is the degree, which is neither preserved nor additively transformed. A corollary that the belief program should adopt: **scale-free and scale-invariant are different, largely orthogonal properties.**

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
([[kemeny-snell-1960-finite-markov-chains]]). The MultiAgentELBO finite laboratory measured
exactly this on the gauge-VFE system (2026-08-17): the pre-registered compatibility check C3
failed by $0.204$ against $10^{-10}$ with a lossless intermediate projection, so the belief-RG
flow is a **typed cocycle** — one map per level pair — rather than an autonomous semigroup, its
per-ratio fixed structures are factorized and ratio-dependent, and the triviality is
architectural (thin single-edge block boundaries make instances quasi-one-dimensional). The
synthesis, the measurements, and the open bundled-tower question live in
[[Staged hierarchy formation and RG composability]].

## Sources

- [[wilson-1971-rg-critical-phenomena]] — the RG transformation realizing Kadanoff block-spin scaling; fixed points and the relevant/irrelevant/marginal operator taxonomy.
- [[wilson-kogut-1974-epsilon-expansion]] — the long-form review; effective-action formalism and the $\epsilon = 4-d$ perturbative expansion of critical exponents.
- [[berges-tetradis-wetterich-2002-nonperturbative-rg]] — functional (non-perturbative) RG: the effective average action $\Gamma_k$ and the exact Wetterich flow; the language for the continuum-limit question.
- [[cardy-1996-scaling-renormalization]] — standard pedagogy: Wilsonian effective action, Gaussian/saddle-point closure, finite-size scaling.
- [[bialek2001predictability|bialek-2001-predictability-complexity]] — predictive information and its sub-extensive growth; the information-theoretic reading of what coarse-graining keeps versus discards.
- [[geshkovski-2023-mathematical-transformers]] — attention as an interacting-particle consensus flow producing clusters; the microdynamics the belief-RG coarse-grains.
- [[gabrielli-2025-network-renormalization]] — RG on heterogeneous networks: the three-step program; geometric, Laplacian and multiscale frameworks compared.
- [[garuccio-2023-multiscale-network-renormalization]] — uniqueness of the aggregation-invariant model; additivity as the renormalizability criterion; scale-free versus scale-invariant.
- [[villegas-2023-laplacian-renormalization-group]] — diffusion time as an intrinsic RG scale; entropic susceptibility as a scale detector.
- [[berman-2023-bayesian-renormalization]] — the Fisher metric as an emergent RG scale; inference as the inverse of exact RG flow.
- [[genest-zidek-1986-pooling]], [[dietrich-list-2016-opinion-pooling]], [[bordley-1982-multiplicative-pooling]] — opinion-pooling taxonomy fixing the aggregator used at the RG blocking step.
- [[griffiths-1979-rg-transformations]], [[van-enter-1993-rg-pathologies]] — rigorous limits of real-space RG: renormalized interactions need not exist; non-Gibbsian images.
- [[berker-1979-hierarchical-lattice-rg]], [[kadanoff-1976-migdal-recursion]] — hierarchical lattices, the self-similar substrates on which real-space RG composes exactly.
- [[kemeny-snell-1960-finite-markov-chains]] — lumpability as the exceptional condition for a coarse-grained Markov chain to stay Markov.
- [[csiszar-1975-i-divergence-geometry]] — I-projection and IPF convergence, the theorem behind the laboratory's variational coupling read-back.

## See also

- [[Staged hierarchy formation and RG composability]]
- [[Renormalization-group flow of beliefs]]
- [[Meta-agents and hierarchical emergence]]
- [[Ouroboros multi-scale dynamics]]
- [[Geometric singular perturbation theory]]
- [[Belief inertia]]
- [[participatory-it-from-bit]] · [[Gauge-Theoretic Multi-Agent VFE Model]] · [[VFE Transformer Program]]
