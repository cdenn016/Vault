---
type: concept
title: Holonomy
aliases:
  - Holonomy group
  - Anholonomy
  - Gauge holonomy
tags:
  - cluster/gauge-theory
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-06-19
---

# Holonomy

## Definition

Holonomy measures the failure of a connection to be path-independent. Given a manifold equipped with a connection (a rule for [[Parallel transport]] — moving a vector, frame, or belief along a curve while keeping it "as constant as the geometry allows"), transporting an object around a **closed loop** generally does not return it unchanged: it comes back rotated, scaled, or otherwise transformed by some group element. That net transformation is the **holonomy** of the loop. The set of all such transformations, taken over all loops based at a point, forms a group — the **holonomy group** — which is a subgroup of the connection's structure (gauge) group.

Concretely, if a connection is specified by a Lie-algebra-valued one-form (a "gauge potential") `A`, the holonomy of a loop `γ` is the path-ordered exponential

```
Hol(γ) = P exp( -∮_γ A )  ∈ G,
```

an element of the structure group `G`. The connection is **flat** (curvature zero) exactly when the holonomy of every contractible loop is the identity; then transport is path-independent and the geometry is said to be **holonomic**. Nontrivial holonomy is equivalently the integrated effect of **curvature**: by the non-abelian Stokes / Ambrose–Singer theorem, the holonomy around an infinitesimal loop is the curvature two-form evaluated on the loop's area. Holonomy is therefore the global, observable shadow of local curvature.

## Why it matters here

The VFE transformer is built as a **gauge theory over per-token state**: each token carries a Gaussian belief `(mu, Sigma)` living in a local frame, and the architecture moves these beliefs between tokens and across layers using connection-like operations rather than naive copying. Wherever there is a connection and [[Parallel transport]], holonomy is the diagnostic for whether that transport is consistent. Two facts make it central here:

1. **The gauge group is non-abelian.** The model's `gauge_group` is `block_glk` — the block general-linear group GL(k) — whose elements generally do not commute. For non-commuting groups, the order of transport matters, so closed-loop transport accumulates a nontrivial holonomy. This is precisely the regime where holonomy is informative rather than vacuous.

2. **Covariances live on a curved manifold.** Each `Sigma` is a symmetric-positive-definite (SPD) matrix, and the model's `spd_affine` retraction uses the affine-invariant Riemannian metric, whose [[Parallel transport]] is genuinely curved (see [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). Transporting a belief covariance around a loop on the SPD cone returns a congruence-transformed matrix, not the original — again a holonomy effect.

In gauge-equivariant networks the central design principle is that *features are only meaningful relative to a frame*, and any operation comparing features at different points must transport them with the connection so the result is independent of arbitrary local frame choices ([[cohen-2019-gauge-cnn]], [[bronstein-2021-geometric-deep-learning]]). Holonomy is what is left over after you demand that consistency: it is the frame-independent, physically real part of the geometry. The "cocycle relaxation" in the model is, in this language, a soft constraint pushing certain holonomies toward the identity so that transported beliefs agree.

## Details

**Holonomy and curvature.** For a connection with curvature `F`, the holonomy of a small loop bounding an oriented area element `Σ` is

```
Hol ≈ exp( -∮ F )  ≈  I - F(Σ) + ...,
```

so curvature is the *density* of holonomy and holonomy is its *integral*. A connection is flat iff `F = 0` iff all contractible-loop holonomies vanish. This is the geometric content behind a **cocycle condition**: a consistent assignment of frame-to-frame transport maps (transition functions / cocycles) is one whose loop compositions are trivial; relaxing it allows controlled nontrivial holonomy. The textbook-grade statement of this transport rule and of the cocycle/holonomy conditions — derived from first principles by demanding coordinate-independence plus weight-sharing, which together *force* local-gauge equivariance with full G-structure and parallel-transport bookkeeping — is [[weiler-2021-coordinate-independent-cnns]].

**Anholonomy and the geometric (Berry-type) phase.** Holonomy is sometimes called *anholonomy* to stress that the closed-loop transport fails to close on itself in the fiber. The classic intuition is parallel-transporting a vector around a spherical triangle: it returns rotated by an angle equal to the enclosed solid angle (the sphere's curvature times area). Abelian holonomy reduces to such a phase/scale factor; the non-abelian GL(k) case generalizes this to a full matrix.

**Relation to the Lie-algebra parameterization.** The model parameterizes gauge elements in the Lie algebra (a `phi` field) and maps back to the group via exponentiation, composing transports with the **[[Baker-Campbell-Hausdorff formula|Baker–Campbell–Hausdorff]] (BCH)** formula — the algebra-first recipe used by Lie-group-equivariant networks such as [[finzi-2020-lieconv]]. Because `exp(X) exp(Y) = exp(X + Y + ½[X,Y] + ...)`, the BCH commutator terms are exactly the source of non-abelian holonomy: when `[X,Y] ≠ 0`, the round-trip `exp(X)exp(Y)exp(-X)exp(-Y)` is not the identity, and its leading term is the commutator — the infinitesimal curvature. Holonomy is thus directly readable from how the model composes its `phi`-generated transports. The map back to the group is a matrix exponential `exp(phi)`, whose numerics matter: when `phi` is symmetric rather than skew the frames leave the orthogonal regime and `exp(phi)` can become ill-conditioned, exactly the eigenvalue-method breakdown for non-normal/defective matrices catalogued in [[moler-vanloan-2003-nineteen-dubious-ways]].

**Holonomy group as a representation-theoretic object.** The holonomy group sits inside the structure group and acts on features that are organized into [[Irreducible representation]]s. Equivariant architectures route information through irreps and couple them with [[Clebsch-Gordan coefficients]] ([[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]]); the holonomy is the concrete group element that acts on each irrep block as a belief is transported, so its effect decomposes block-by-block across the model's irrep bookkeeping.

> [!note] Editorial: The sources below establish parallel transport, connections, and the curved SPD/GL(k) geometry individually; the synthesis that closed-loop transport in this specific architecture yields a measurable GL(k)/SPD holonomy is the editor's framing, not a claim made verbatim in any one paper.

## In this work

Holonomy surfaces wherever the config commits to a connection or to non-commuting transport:

- **`gauge_group: block_glk` (GL(k)) with Lie-algebra `phi` and BCH retraction.** The non-abelian group and BCH composition are the direct source of nontrivial loop holonomy; the commutator terms in BCH are its infinitesimal generator. See [[Parallel transport]] and [[Gauge transformation]].
- **Parallel transport / holonomy of beliefs.** The architecture transports per-token Gaussian beliefs between frames; holonomy quantifies whether a belief returns to itself after a closed circuit of transports, and is the consistency check the gauge construction must respect ([[cohen-2019-gauge-cnn]], [[bronstein-2021-geometric-deep-learning]]).
- **`spd_affine` retraction on covariances.** Transporting `Sigma` under the affine-invariant metric on the SPD cone is curved, so loop transport induces SPD-side holonomy ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]); retractions and vector transports are used as cheap surrogates for the exact geodesic transport ([[absil-2008-optimization-matrix-manifolds]]).
- **Cocycle relaxation.** Softly enforcing trivial composition of transition maps is a relaxation of the flatness/zero-holonomy condition, trading exact frame consistency for trainability.
- **[[Killing form|Killing-form]] per-block preconditioning.** Conditioning the GL(k) updates with the Killing form is the natural-gradient-style metric on the gauge group that makes transport (and hence holonomy) reparameterization-invariant, echoing the information-geometric preconditioning of [[ollivier-2015-riemannian-metrics-nn]] and [[amari-1998-natural-gradient]].

## Sources

- [[cohen-2019-gauge-cnn]] — gauge equivariance on manifolds: the kernel constraint and the parallel-transport rule whose closed-loop composition is holonomy.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-Program synthesis providing the gauge / connection / parallel-transport scaffolding.
- [[finzi-2020-lieconv]] — Lie-algebra (log-coordinate) parameterization with exp recovery, the BCH-style composition underlying non-abelian holonomy.
- [[weiler-2021-coordinate-independent-cnns]] — monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with textbook-grade transport rule and cocycle/holonomy conditions.
- [[moler-vanloan-2003-nineteen-dubious-ways]] — conditioning of the matrix exponential `exp(phi)` and the eigenvalue-method breakdown for non-normal/defective matrices (the regime when `phi` is symmetric rather than skew).
- [[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]] — irrep-structured features and Clebsch–Gordan coupling on which the holonomy group acts block-by-block.
- [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]] — the curved affine-invariant SPD geometry whose transport is non-flat.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and vector transports as first-order surrogates for geodesic transport.
- [[ollivier-2015-riemannian-metrics-nn]], [[amari-1998-natural-gradient]] — metric/Fisher preconditioning that makes transport reparameterization-invariant.
- [[bleecker-1981-gauge-theory-variational-principles]] — canonical bundle-connection-and-variational-principle reference behind the gauge formalism (connections, curvature, and holonomy on principal bundles).

## See also

- [[Parallel transport]]
- [[Gauge transformation]]
- [[Lattice gauge theory]] — Wilson loops are lattice holonomy (the trace of transport around a plaquette)
- [[Group equivariance]]
- [[Irreducible representation]]
- [[Clebsch-Gordan coefficients]]
- [[Gauge equivariant CNN]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[Gauge equivariance and geometric deep learning]]
