---
type: theme
title: "Staged hierarchy formation and RG composability"
aliases:
  - "staged assembly"
  - "typed cocycle RG"
  - "composability of coarse-graining"
tags:
  - cluster/multi-agent
  - cluster/social-physics
  - project/multi-agent
  - project/social-physics
status: draft
created: 2026-08-17
updated: 2026-08-17
---

# Staged hierarchy formation and RG composability

Two literatures meet at one question the multi-agent program can now measure: does it matter in
what stages a hierarchy is built? The kinetic literature says the *path* matters for what forms;
the renormalization literature says the *description* of the aggregate depends on the path taken
to coarse-grain it. On 2026-08-17 the MultiAgentELBO finite laboratory measured both halves of
this on its own declared system, and this page records the synthesis.

## The kinetic strand: hierarchies are built in stages

[[simon-1962-architecture-complexity]] is the founding argument: assembly through stable
subassemblies (the watchmakers parable) is overwhelmingly faster than all-at-once assembly, so
the complex systems that exist are nearly-decomposable hierarchies built stagewise.
[[maynard-smith-1995-major-transitions]] is the same claim as evolutionary history: every major
transition formed higher-level units from previously stabilized lower-level units, never de
novo. Empirically, [[palla-2007-social-group-evolution]] finds real social groups growing by
gradual accretion, with small groups persisting through stable cores and large ones through
turnover, and [[zhou-2005-discrete-hierarchy-group-sizes]] finds human group sizes layered in a
geometric hierarchy with preferred branching ratio near three. The physics prototype of staged
growth is binary-merger kinetics, [[smoluchowski-1916-coagulation]]; and
[[mengistu-2016-evolutionary-origins-hierarchy]] adds the causal simulation result that
hierarchy emerges from *connection costs* — pricing structure is what produces it.

## The composability strand: coarse-graining is path-dependent

Exact composability of real-space RG maps is the exception. It holds for pure decimation, which
is marginalization and composes trivially; asymptotically at fixed points, where the couplings
outside the retained family have died; and on the hierarchical lattices of
[[berker-1979-hierarchical-lattice-rg]] and [[kadanoff-1976-migdal-recursion]], which compose
exactly because the substrate is built self-similarly, one recursion step undoing one
construction step. Away from these cases, [[griffiths-1979-rg-transformations]] and
[[van-enter-1993-rg-pathologies]] show real-space maps can fail even to produce well-defined
theories of the declared type. The probabilistic cousin is
[[kemeny-snell-1960-finite-markov-chains]]: lumpability of a Markov chain is an exceptional
condition, and generic coarse-grainings of generic chains are not Markov in the lumped states.

## What the laboratory measured (2026-08-17)

The finite categorical laboratory's rescaling map (design and amendments in
`MultiAgentELBO/docs/superpowers/specs/2026-08-17-rescaling-map-design.md`) made this concrete
on the declared two-channel gauge system:

- **C3, compatibility, refuted.** Blocking six agents at once versus in stages disagrees by
  $0.204$ in sup norm against a pre-registered $10^{-10}$ criterion, with a provably lossless
  intermediate projection — the defect is the Bayes kernel composition itself. The flow is a
  **typed cocycle**, not an autonomous semigroup, and the composition defect is order one
  ($0.12$–$0.19$) at every accessible depth, including the $2{\times}3$ versus $3{\times}2$
  panel on a homogeneous 6-cycle.
- **Per-ratio fixed structures exist and are factorized.** Each declared ratio's reduced
  self-map (blocking plus self-similar re-tiling) is a measured local contraction (spectral
  radius $\approx 0.78$–$0.83$) onto a fixed structure whose pairwise block is machine zero —
  the factorized subspace is provably invariant (the block-local Bayes kernel sends factorized
  theories to factorized theories) and measured attracting, with pair-sector eigenvalues near
  $0.17$.
- **Even the endpoints are typed.** The ratio-two and ratio-three fixed structures differ by
  $0.81$ relative sup: pairs-first and triples-first aggregation settle into different
  equilibrium potentials.
- **The triviality is architectural.** Single-boundary-agent towers are quasi-one-dimensional
  (Perron–Frobenius transfer-matrix argument on rings), so decoupled fixed structures are the
  expected 1D outcome; hierarchical lattices show that boundary multiplicity — bundles of
  parallel cross-links per coarse edge — is what sustains interacting fixed structures. For a
  directed $\beta_{ij}$ agent network, the lattice question "in what dimension does interaction
  survive" becomes "**which architectures renormalize to interacting fixed structures**".

## The synthesis

The two strands are one phenomenon seen from two sides. Because coarse descriptions are
path-dependent (composability strand, C3), *which* aggregation path a system takes is physically
meaningful — and the kinetic strand says real systems take staged paths. The program's own
version of the question is now internal: the partition posterior assigns free energies to
blockings, so whether staged aggregation is free-energy-favored over direct aggregation is a
measurement, not an imported analogy. The externally calibrating lesson runs the other way too:
`Theory/07b`'s autonomous-semigroup claim was stronger than standard RG lore warrants, since
even classical real-space RG composes only at fixed points or on self-similar substrates, and
the laboratory correctly caught that.

> [!note] Editorial: as a formal home for staged, typed composition — maps composing only along
> a tower of levels, with typed slots — operads are the standard algebraic structure (May's
> *Geometry of Iterated Loop Spaces*, 1972); this is a pointer, not yet a used tool, and the
> citation has not been verified against the primary source.

> [!note] Editorial: the 1D triviality argument (Perron–Frobenius uniqueness of the transfer
> matrix's top eigenvalue for strictly positive finite-range weights, hence no phase transition
> on rings) is textbook material asserted from memory; it should be pinned to a standard text
> before entering a manuscript.

## Open measurements this frames

Whether the composition defect contracts under iteration on deeper flows (asymptotic semigroup)
or persists (irreducibly typed); the pair-sector contraction rate as a function of boundary
multiplicity in bundled towers, whose crossing of one would be the architecture analog of a
lower critical dimension; and the staged-versus-direct free-energy comparison under the
partition posterior — the model's own "nine humans do not suddenly form a gang".

## See also

- [[Renormalization group flow]] · [[Renormalization-group flow of beliefs]]
- [[Meta-agents and hierarchical emergence]] · [[Coarse Graining]]
- [[Ouroboros multi-scale dynamics]]
- [[garuccio-2023-multiscale-network-renormalization]] — closure relative to a declared family
  and aggregation protocol, the network-science form of the same lesson
- [[csiszar-1975-i-divergence-geometry]] — the I-projection theorem behind the laboratory's
  variational coupling read-back
- [[Gauge-Theoretic Multi-Agent VFE Model]]
