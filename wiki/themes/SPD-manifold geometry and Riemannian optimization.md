---
type: theme
title: SPD-manifold geometry and Riemannian optimization
aliases:
  - SPD geometry
  - Symmetric positive-definite manifold
  - Covariance manifold
  - Affine-invariant metric
  - Riemannian optimization
  - "SPD Manifold"
  - "SPD manifold"
  - "SPD Belief Geometry"
  - "spdbeliefgeometry"
  - "SPD manifold geometry"
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
status: stable
created: 2026-06-18
updated: 2026-07-10
---

# SPD-manifold geometry and Riemannian optimization

## The big picture

The full covariance space is the SPD cone, but the live `gaussian_diagonal` family occupies only its diagonal subset. General $\mathrm{GL}(K)$ congruence leaves that subset unless the transport is monomial, so realized transport uses projection or approximation outside that subgroup. [[gl-k-attention-2026-07-09-review-revision]]

The organizing object is the SPD manifold equipped with a Riemannian metric.
The affine-invariant Riemannian metric (AIRM) is congruence-invariant on full
SPD, while the Log-Euclidean metric maps SPD matrices through the matrix
logarithm into a flat space. For mutually commuting SPD matrices, including the
live positive diagonal family, their restricted distances, geodesics, and means
coincide exactly. They differ for noncommuting full covariances. The
`spd_affine` name selects the AIRM-side covariance update; it does not imply that
the model implements Log-Euclidean or Fréchet value aggregation.

The second pillar is Riemannian optimization of beliefs. It supports covariance retractions and vector transports but does not turn the audited frame update into a Fisher/Riemannian natural gradient. At each recorded source SHA, the stored configuration routes frames through AdamW; dirty provenance prevents byte-level reconstruction of the executed optimizer. Heavy-ball belongs only to the disabled custom outer frame optimizer, BCH/retraction only to disabled in-E-step frame revision, and the pullback preconditioner is inactive because both optional routes are off. [[gl-k-attention-2026-07-09-review-revision]]

The third pillar is architectural background: networks that compute on SPD
matrices. [[huang-2017-spdnet]] develops SPD-preserving spectral layers, and
[[wang-2023-riemannian-self-attention-spd]] defines attention with SPD affinities
and weighted Fréchet aggregation. The latter is a comparison method; vfe3 does
not compute an AIRM Fréchet mean of covariance-valued attention values.

## Key threads

**Thread 1 — The metric defines the geometry.** AIRM uses
`<A, B>_Sigma = tr(Sigma⁻¹ A Sigma⁻¹ B)` and is invariant under invertible
congruence on full SPD. The Log-Euclidean metric is a different exact metric,
obtained by pulling the Frobenius metric back through the matrix logarithm. It
is invariant under orthogonal congruence and inversion, but not under arbitrary
invertible congruence. AIRM and Log-Euclidean distances, geodesics, and means
coincide exactly for mutually commuting SPD matrices, including the positive
diagonal family, and differ in general for noncommuting SPD matrices.

> [!note] Editorial (2026-07-10): diagonal beliefs do not acquire exact off-diagonal covariance while remaining in the live family; general congruence is projected back. Full-SPD AIRM statements remain valid for a full-covariance path. [[gl-k-attention-2026-07-09-review-revision]]

**Thread 2 — Retractions and transports make steps tractable.** A retraction is
a smooth tangent-to-manifold map satisfying first-order conditions, and vector
transport moves tangent vectors between tangent spaces
([[absil-2008-optimization-matrix-manifolds]]). The covariance update uses an
SPD retraction. A truncated BCH series instead returns a local algebra
coordinate for a composed frame update; exponentiation or another group-valued
map is still required, and the name alone does not verify the retraction
conditions. These operations share vocabulary but not one optimizer: the
Gaussian covariance Fisher block is one-half conventional AIRM, while audited
frames use plain AdamW.
Matrix-exponential accuracy and conditioning remain governed by
[[al-mohy-higham-2009-scaling-squaring-matrix-exp]] and
[[moler-vanloan-2003-nineteen-dubious-ways]].

**Thread 3 — Belief-side Riemannian optimization.** For a zero-mean Gaussian,
the covariance Fisher metric is one-half conventional AIRM. This supports the
belief update up to a constant gradient scale; it does not license joint frame
training as Riemannian SGD or identify the frame conditioner with that metric.
[[gl-k-attention-2026-07-09-review-revision]]

**Thread 4 — Networks that live on the cone.** [[huang-2017-spdnet]] demonstrates that a covariance can be the activation itself, not just an output: BiMap layers apply a learned congruence `W Sigma Wᵀ` (with `W` constrained to the Stiefel manifold to preserve positive-definiteness), ReEig rectifies eigenvalues to stay safely positive, and LogEig maps to the flat tangent space at the identity for a final Euclidean classifier. Each operation is differentiable through its eigendecomposition. The canonical derivation of that adjoint-matrix backpropagation through eigendecomposition and SVD is [[ionescu-2015-matrix-backpropagation]], which exposes the eigenvalue-gap denominator `1/(lambda_i - lambda_j)` that diverges to NaN when eigenvalues coincide — precisely the `eigh`-backward failure mode the vfe3 codebase pins for its ReEig/LogEig and matrix-log operations. This is the template the VFE transformer follows in treating `Sigma` as a propagated, transformed, learnable object rather than a fixed hyperparameter.

**Thread 5 — Attention on the SPD manifold.**
[[wang-2023-riemannian-self-attention-spd]] replaces dot-product affinities with
SPD distances and Euclidean value sums with weighted Fréchet means. This is a
distinct architecture and a useful comparison, not a description of vfe3. The
current transformer uses precision-informed pairwise belief interactions but
does not aggregate covariance-valued attention outputs by an AIRM Fréchet mean.

## How it lands in this work

In the transformer, the covariance belief update uses the Gaussian covariance
Fisher block, equal to one-half conventional AIRM. The parameter M-step is
separate, and the frame update has no established Riemannian/Fisher identity.
[[gl-k-attention-2026-07-09-review-revision]]

The AIRM is congruence-invariant on full SPD. The live diagonal projection breaks exact general-$\mathrm{GL}(K)$ closure, so this ambient theorem must not be conflated with realized-family equivariance. [[gl-k-attention-2026-07-09-review-revision]]

Precision informs the transformer's belief-side interactions and covariance
updates. This should not be conflated with Wang et al.'s SPD-valued attention:
vfe3 does not compute their AIRM affinity-plus-Fréchet-value aggregation. Its
spectral SPD operations maintain valid covariances, while value aggregation
follows the model's own non-Fréchet path.

## Open questions / gaps

- **Affine-invariant versus Log-Euclidean in practice.** On the commuting positive-diagonal family, AIRM and Log-Euclidean geometry coincide exactly. A trade-off appears only after admitting noncommuting full or block covariances.
- **Differentiating through eigen-operations at scale.** SPDNet-style ReEig/LogEig layers ([[huang-2017-spdnet]]) require backpropagating through eigendecompositions, which is numerically delicate when eigenvalues cluster. Whether this is stable for thousands of per-token covariances per forward pass is unestablished.
- **Riemannian means in attention.** [[wang-2023-riemannian-self-attention-spd]] computes weighted Fréchet means. Adding that distinct operation to vfe3 would require a new design and cost analysis; it is not a current implementation gap in an already wired path.
- **Scope of the invariances.** Full-SPD AIRM is congruence invariant, the
  Gaussian Fisher vector field is coordinate invariant, and gauge equivariance
  is a separate model property. Live diagonal projection and distinct optimizers
  prevent these facts from being treated as one automatically consistent
  invariance theorem.
- **Convergence across separate optimizers.** Bonnabel's theorem applies under its stated Riemannian-SGD assumptions. The deployed covariance, frame, and decode updates use different objectives or optimizers, so no joint-product-manifold convergence claim follows.

## Sources synthesized

- [[pennec-2006-affine-invariant-tensor]] — the affine-invariant Riemannian metric making the SPD cone a complete manifold; the geometry behind `spd_affine`.
- [[arsigny-2006-log-euclidean]] — the Log-Euclidean metric; fast, commutative, closed-form means and interpolation for SPD matrices.
- [[bhatia-2007-positive-definite-matrices]] — standard monograph on SPD geometry: geodesics, geodesic distance, matrix geometric mean, operator-monotone functions.
- [[absil-2008-optimization-matrix-manifolds]] — definitions and conditions for retractions and vector transports; shared vocabulary does not identify the SPD and frame optimizers.
- [[bonnabel-2013-riemannian-sgd]] — stochastic Riemannian-gradient convergence under stated assumptions, not a license for the mixed deployed schedule.
- [[zhang-sra-2016-geodesically-convex-optimization]] — iteration-complexity theory for geodesically convex first-order optimization on Hadamard manifolds; general full-SPD background, not a rate theorem for the deployed mixed schedule.
- [[boumal-2023-optimization-smooth-manifolds]] — computation-forward successor to Absil: concrete retractions, vector transport, and second-order error / convergence-rate analysis for SPD and Stiefel steps.
- [[skovgaard-1984-riemannian-geometry-normal-model]] — Fisher-Rao geometry of the full Gaussian model (mean and covariance jointly); geodesic ODEs and Rao distance for the object a token belief `(mu, Sigma)` is.
- [[ionescu-2015-matrix-backpropagation]] — canonical adjoint-matrix backpropagation through eigendecomposition and SVD; the eigenvalue-gap denominator behind the `eigh`-backward NaN failure mode.
- [[al-mohy-higham-2009-scaling-squaring-matrix-exp]] — scaling and squaring with Padé approximation for matrix exponentials used in gauge transport and after algebra-coordinate updates.
- [[moler-vanloan-2003-nineteen-dubious-ways]] — canonical survey of matrix-exponential computation and its pitfalls; the eigenvalue-method breakdown for non-normal / defective gauge frames `exp(phi)`.
- [[huang-2017-spdnet]] — SPDNet, the prototype deep network operating directly on SPD matrices via differentiable spectral layers.
- [[wang-2023-riemannian-self-attention-spd]] — SPD affinity and weighted Fréchet-value attention, a comparison architecture not implemented by vfe3.
- [[moakher-2005-geometric-mean]] — differential-geometric construction of the SPD geometric mean as a Riemannian (Fréchet) mean under the affine-invariant metric.
- [[karcher-1977-center-of-mass]] — Riemannian center of mass (the Karcher/Fréchet mean) and its existence and uniqueness on manifolds of nonpositive curvature, underpinning means on the SPD cone.
- [[milnor-1976-left-invariant-metrics]] — curvatures of left-invariant metrics on Lie groups, the homogeneous-space backdrop for the SPD cone viewed as GL(k)/O(k).
- [[higham-2008-functions-of-matrices]] — stable computation of matrix exp, log, and square root used by many exact SPD maps and metric operations.
- [[horn-johnson-2013-matrix-analysis]] — standard reference for positive-definite matrices, congruence, and the spectral and eigenvalue facts the SPD geometry rests on.
- [[golub-vanloan-2013-matrix-computations]] — the factorization and eigendecomposition algorithms behind the SPD covariance operations (Cholesky, symmetric eigensolvers, matrix square roots).
- [[trefethen-bau-1997-numerical-linear-algebra]] — conditioning, SVD geometry, and backward stability underlying the SPD eigenvalue and retraction kernels.
- [[higham-2002-accuracy-stability-numerical-algorithms]] — finite-precision error analysis and conditioning backing the SPD covariance and transport numerics.

## See also

- [[Symmetric spaces and the SPD cone]] — the SPD cone as the symmetric space GL(k)/O(k), placing the affine-invariant geometry in its homogeneous-space setting.

Cross-cluster links drawn above: [[amari-1998-natural-gradient]] and the [[Fisher information metric]] / [[Natural gradient]] (information geometry); [[rao-1999-predictive-coding]] and [[friston-2010-free-energy-principle]] (precision weighting); [[vaswani-2017-attention]] and [[tsai-2019-kernel-attention]] (attention baselines); and the sibling themes [[Information geometry and natural gradient]], [[Gauge equivariance and geometric deep learning]], and [[Attention mechanisms — theory and positional structure]].
