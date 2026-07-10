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
updated: 2026-07-09
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

Generic non-abelian connections and curved SPD manifolds can have nontrivial holonomy. The realized transformer Regime-I connection is more restrictive: $\Omega_{ij}=U_iU_j^{-1}$ telescopes on every closed loop, so $H=I$ exactly despite the noncommutativity of $\mathrm{GL}(K)$. Nontrivial model holonomy requires an independent-edge or otherwise nonflat Regime-II connection. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**Holonomy and curvature.** For a connection with curvature `F`, the holonomy of a small loop bounding an oriented area element `Σ` is

```
Hol ≈ exp( -∮ F )  ≈  I - F(Σ) + ...,
```

so curvature is the *density* of holonomy and holonomy is its *integral*. A connection is flat iff `F = 0` iff all contractible-loop holonomies vanish. This is the geometric content behind a **cocycle condition**: a consistent assignment of frame-to-frame transport maps (transition functions / cocycles) is one whose loop compositions are trivial; relaxing it allows controlled nontrivial holonomy. The textbook-grade statement of this transport rule and of the cocycle/holonomy conditions — derived from first principles by demanding coordinate-independence plus weight-sharing, which together *force* local-gauge equivariance with full G-structure and parallel-transport bookkeeping — is [[weiler-2021-coordinate-independent-cnns]].

**Anholonomy and the geometric (Berry-type) phase.** Holonomy is sometimes called *anholonomy* to stress that the closed-loop transport fails to close on itself in the fiber. The classic intuition is parallel-transporting a vector around a spherical triangle: it returns rotated by an angle equal to the enclosed solid angle (the sphere's curvature times area). Abelian holonomy reduces to such a phase/scale factor; the non-abelian GL(k) case generalizes this to a full matrix.

**Relation to Lie-algebra coordinates.** BCH commutators describe generic non-abelian group commutators, but they do not create holonomy in the realized vertex cocycle: the exact group products $U_iU_j^{-1}$ still telescope. Finite BCH truncation is only a local approximation, and any truncation residue is numerical/chart error rather than a Regime-I curvature observable. [[gl-k-attention-2026-07-09-review-revision]]

**Holonomy group as a representation-theoretic object.** The holonomy group sits inside the structure group and acts on features that are organized into [[Irreducible representation]]s. Equivariant architectures route information through irreps and couple them with [[Clebsch-Gordan coefficients]] ([[weiler-2019-e2-steerable]], [[kondor-2018-compact-group-conv]], [[thomas-2018-tensor-field-networks]]); the holonomy is the concrete group element that acts on each irrep block as a belief is transported, so its effect decomposes block-by-block across the model's irrep bookkeeping.

> [!note] Editorial (2026-07-09): generic holonomy definitions on this page remain valid. In this architecture, measurable nontrivial loop transport belongs only to an edge-relaxed/nonflat path; strict Regime I is exactly flat. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

Holonomy surfaces wherever the config commits to a connection or to non-commuting transport:

- **Regime-I vertex transport.** The cocycle gives $H=I$ exactly; noncommutativity alone does not change this. [[gl-k-attention-2026-07-09-review-revision]]
- **Parallel transport / holonomy of beliefs.** Closed-loop transport is a valid consistency diagnostic only for a connection that the architecture actually realizes. The Regime-I frame connection closes exactly; an edge-relaxed connection can be tested for nontrivial loop transport ([[cohen-2019-gauge-cnn]], [[bronstein-2021-geometric-deep-learning]]).
- **Generic SPD holonomy.** Levi-Civita parallel transport of tangent vectors around a closed path on the curved affine-invariant SPD manifold can have nontrivial holonomy ([[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]]). The deployed `spd_affine` covariance retraction updates covariance points; it does not by itself implement that closed-loop tangent-vector transport or establish SPD-side model holonomy.
- **Edge-relaxed transport.** Independent edge variables can produce nontrivial holonomy and are the appropriate target for loop diagnostics. [[gl-k-attention-2026-07-09-review-revision]]
- **Frame conditioning.** The configured Cartan/Killing object is an optimizer preconditioner, not a full-$\mathrm{GL}(K)$ Fisher metric and not a certificate that holonomy is reparameterization invariant. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[cohen-2019-gauge-cnn]] — gauge equivariance on manifolds: the kernel constraint and the parallel-transport rule whose closed-loop composition is holonomy.
- [[bronstein-2021-geometric-deep-learning]] — Erlangen-Program synthesis providing the gauge / connection / parallel-transport scaffolding.
- [[finzi-2020-lieconv]] — Lie-algebra (log-coordinate) parameterization with exp recovery, the BCH-style composition underlying non-abelian holonomy.
- [[weiler-2021-coordinate-independent-cnns]] — monograph deriving gauge equivariance from coordinate-independence plus weight-sharing, with textbook-grade transport rule and cocycle/holonomy conditions.
- [[moler-vanloan-2003-nineteen-dubious-ways]] — conditioning of the matrix exponential and the eigenvalue-method breakdown for non-normal or defective matrices; symmetric `phi` is normal and nondefective.
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
