---
type: manuscript
title: "MultiAgentELBO Literature-Gap Review: 2026-08-10 Ingest Record"
aliases:
  - "MultiAgentELBO literature review 2026-08-10"
  - "MultiAgentELBO literature-gap ingest"
authors:
  - Robert C. Dennis
year: 2026
status: in preparation
tags:
  - cluster/vfe
  - cluster/multi-agent
  - cluster/gauge-theory
  - cluster/info-geometry
  - cluster/social-physics
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
  - project/social-physics
  - field/mathematics
  - field/statistics
  - field/cs-ml
  - field/physics
created: 2026-08-10
updated: 2026-08-10
---

# MultiAgentELBO Literature-Gap Review: 2026-08-10 Ingest Record

## Scope and provenance

This immutable record banks the source-selection and correction map produced by the
MultiAgentELBO literature-gap review. The reviewed code and theory revision was
`fcb2c49efdca2ad3ee502dc08fbb82fc285e7a05` on `origin/main`. The read-only Research-vault
baseline was `b4f8b204168eb317717180f137a33b01f0a28143`. Pre-existing uncommitted vault work was
excluded from the ingest worktree and was not modified.

The durable review artifacts are
`docs/reviews/2026-08-10-multiagentelbo-literature-gap-review.md` and
`docs/reviews/evidence/2026-08-10-literature-gap-search-matrix.tsv` on the review branch
`codex/multiagentelbo-literature-gap-review-20260810`. Their SHA-256 digests are respectively
`747a414bd60428a2bda31bab461cbefffa0b29e30f74a08bc9f5643f91e57fe6` and
`2bb611db9b00215b333ae9155c6ad5e739f19e55274bc6bd21d451bf76ac1da9`.

Three independent specialist searches covered structured variational and active inference;
gauge, information geometry, and coarse graining; and decentralized Bayesian inference, social
learning, and population limits. Exact-title, author-title, identifier, and semantic checks were
run against the pinned repository and accessible vault corpus. The review also retained four
present controls to test the absence procedure: structured SVI, spectral cellular sheaves,
generalized belief propagation, and classical variational message passing.

## Main finding

The vault's strongest coverage is the exact finite ELBO, correlated recognition laws, standard
variational inference, information geometry, gauge-equivariant modeling, opinion pooling,
collective active inference, and finite renormalization. The important gaps lie at the interfaces
needed to turn an exact finite oracle into an inference system and to state recovery, quotient,
communication, synchronization, social-learning, and continuum assumptions without overreach.

The resulting ingest therefore adds source clusters around [[Process-space variational inference]],
[[Decentralized Bayesian inference]], [[Statistical experiment comparison and deficiency]],
[[Graph synchronization and connection Laplacians]], [[Singular statistical models]],
[[Quotient Bayesian learning]], [[Communication-constrained inference]],
[[Conservative information fusion]], [[Graphon limits of agent networks]],
[[Propagation of chaos]], [[Non-Bayesian social learning]],
[[Common knowledge and Bayesian agreement]], [[O-information]], and
[[Partial information decomposition]]. It also corrects or extends [[Expected Free Energy]],
[[Gaussian Belief Propagation]], [[Probabilistic opinion pooling]],
[[Collective active inference]], and [[Mean-field games and continuum limits]].

## Boundaries retained by the ingest

- The repository remains an exact finite oracle and diagnostic laboratory. Literature on BP,
  EP, VMP, decentralized filtering, or active inference does not make those algorithms present in
  the code.
- Ordinary sum-product BP is exact on trees under its usual hypotheses. Constrained mean-field
  VMP and EP variants can remain approximate even on trees; locally consistent pseudomarginals
  are not the repository's exact global recognition law.
- Graphical-model factor reparameterization called a *gauge* is not automatically the passive
  principal-bundle `GL(K)` gauge used by the project.
- Connection-Cheeger and vector-diffusion results assume compact or orthogonal connection data.
  Applying them to noncompact `GL^+(2)` links requires a chosen fiber metric and separate
  self-adjointness, positive-semidefiniteness, and comparison theory.
- Expected-free-energy critiques establish limits of particular derivational routes, not a
  universal refutation of every expected-free-energy model.
- Graphon and propagation-of-chaos results apply only after a declared stochastic indexed model,
  topology, scaling, regularity, and initialization route. Deterministic graph limits have
  different hypotheses.
- O-information has a compact algebraic definition, but high-dimensional entropy estimation can
  be biased and sample intensive. Partial information decomposition is not unique, and some
  multivariate axiom systems are inconsistent.
- Citations do not construct the missing continuum section law, DLR specification, regular
  quotient, common recovery kernel, intrinsic partition selector, or measurable integrable RG
  cocycle. Those obligations remain open.

## Research consequence

The exact finite oracle should remain the invariant center. Approximate inference, communication,
policy selection, and continuum limits should enter as separately typed layers, each carrying the
assumptions, negative controls, and error measures supplied by its literature. The immediate
experimental ladder is an exact tree-BP oracle, separate constrained-approximation tests, loopy and
Gaussian-BP controls, conservative decentralized fusion with communication accounting, declared
partition benchmarks, and only then a gated large-population or policy layer.

## Related

[[Gauge-Theoretic Multi-Agent VFE Model]] · [[Multi-agent variational free energy]] ·
[[Inference machinery — variational EM and filtering]] ·
[[Information geometry and natural gradient]] ·
[[Gauge equivariance and geometric deep learning]] ·
[[Statistical physics of social systems and collective behavior]]
