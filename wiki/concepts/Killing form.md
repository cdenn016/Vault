---
type: concept
title: Killing form
aliases:
  - Killing-form
  - Killing metric
  - Killing-form preconditioning
tags:
  - cluster/gauge-theory
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: draft
created: 2026-06-18
updated: 2026-07-09
---

# Killing form

## Definition

The **Killing form** is the canonical symmetric bilinear form attached to a Lie algebra $\mathfrak{g}$. For elements $X, Y \in \mathfrak{g}$ it is defined through the adjoint representation $\operatorname{ad}_X(Z) = [X, Z]$ as

$$
B(X, Y) \;=\; \operatorname{tr}\!\big(\operatorname{ad}_X \,\operatorname{ad}_Y\big),
$$

the trace of the composition of the two adjoint endomorphisms. It is manifestly **symmetric** ($B(X,Y) = B(Y,X)$, since $\operatorname{tr}(AB) = \operatorname{tr}(BA)$) and **bilinear**. Its defining structural property is **ad-invariance**, also called associativity or invariance under the bracket:

$$
B([X, Y], Z) \;=\; B(X, [Y, Z]),
$$

equivalently $B(\operatorname{ad}_W X, Y) + B(X, \operatorname{ad}_W Y) = 0$ for every $W$. This says the adjoint action is skew with respect to $B$, so the connected group acts on $\mathfrak{g}$ by $B$-isometries; the Killing form is preserved by every automorphism of $\mathfrak{g}$ and, in particular, by the adjoint action $\operatorname{Ad}_g$ of the group.

Two textbook facts make the form a structural diagnostic. **Cartan's criterion**: $\mathfrak{g}$ is semisimple if and only if $B$ is nondegenerate. And the compactness refinement: a semisimple real Lie algebra is **compact** (the algebra of a compact group) if and only if $B$ is **negative-definite**, in which case $-B$ is a genuine positive-definite inner product. These are stated here as standard Lie theory; the subtlety relevant to this project is what happens when $\mathfrak{g}$ is *not* semisimple, treated below.

## Why it matters here

The literal Killing form remains a useful Lie-algebra diagnostic, but the configured frame object must be described more narrowly. The regularized Cartan/Killing construction is an optional optimizer preconditioner; audited runs use plain AdamW for the frame table, so this conditioner and the heavy-ball field are inactive. It is not the Fisher geometry of the Gaussian beliefs. [[gl-k-attention-2026-07-09-review-revision]]

For $\mathfrak{gl}(k)$, $\operatorname{tr}(XY)$ is adjoint-invariant but indefinite, while the positive Frobenius form $\operatorname{tr}(X^\top Y)$ is invariant only under orthogonal, more precisely conformal-orthogonal, conjugations. No positive-definite choice here supplies full-$\mathrm{GL}(K)$ gauge invariance or a Fisher natural gradient. [[gl-k-attention-2026-07-09-review-revision]]

## Details

**An ad-invariant form is a bi-invariant metric.** Because $B$ is $\operatorname{Ad}$-invariant, transporting it from the identity tangent space (the algebra) around the group by left and right translation yields a single, consistently defined **bi-invariant (pseudo-)metric** on the Lie group itself. On a compact semisimple group, where $-B$ is positive-definite, this is an honest Riemannian metric whose geodesics through the identity are the one-parameter subgroups $t \mapsto \exp(tX)$. This is precisely the structure one wants for optimizing over group-valued parameters: the algebra carries a coordinate-free inner product, and the exponential map turns straight lines in the algebra into geodesics on the group. It is the geometric backbone behind handling gauge elements in logarithmic ($\phi$) coordinates and recovering group elements by $\exp$, the device shared with [[LieConv]] ([[finzi-2020-lieconv]]).

**The $\mathfrak{gl}(k)$ subtlety — be honest about degeneracy.** The gauge algebra here is $\mathfrak{gl}(k)$, which is **reductive, not semisimple**. It splits as $\mathfrak{gl}(k) = \mathfrak{sl}(k) \oplus \mathbb{R}\,I$, the traceless matrices plus the one-dimensional center of scalar matrices. The Killing form of $\mathfrak{gl}(k)$ is **degenerate**: a direct computation gives

$$
B(X, Y) \;=\; 2k\,\operatorname{tr}(XY) \;-\; 2\,\operatorname{tr}(X)\,\operatorname{tr}(Y),
$$

so on the center (scalar matrices, where $X \propto I$) the two terms cancel and $B$ vanishes identically — Cartan's criterion failing exactly because $\mathfrak{gl}(k)$ is not semisimple. Restricted to the semisimple part $\mathfrak{sl}(k)$ (where $\operatorname{tr} X = 0$) it reduces to the nondegenerate $B(X,Y) = 2k\,\operatorname{tr}(XY)$. The practical consequence is that the *literal* Killing form cannot serve as a metric on all of $\mathfrak{gl}(k)$, because it assigns zero length to the scalar (overall-scale) direction. A nondegenerate replacement requires choosing between matrix pairings with different positivity and invariance properties:

$$
\langle X, Y\rangle \;=\; \operatorname{tr}(X^{\top} Y) \qquad\text{(or } \operatorname{tr}(XY)\text{)},
$$

The two displayed choices have different properties: $\operatorname{tr}(X^\top Y)$ is positive definite but not full-$\mathrm{GL}(K)$ adjoint-invariant, whereas $\operatorname{tr}(XY)$ is adjoint-invariant but indefinite. Neither is simultaneously a positive-definite, full-$\mathrm{GL}(K)$-invariant frame metric. [[gl-k-attention-2026-07-09-review-revision]]

> [!note] Editorial (2026-07-09): `killing_per_block` names a conditioning heuristic, not a proven invariant metric or a Fisher/K-FAC identification. [[gl-k-attention-2026-07-09-review-revision]]

**Relation to belief natural gradients.** Gaussian mean/covariance natural gradients are defined by the belief-family [[Fisher information metric]]. The frame conditioner comes from a chosen matrix-space form and is not thereby Fisher, K-FAC, left-invariant, or coordinate-free. The Frobenius pullback through $\exp$ is an extrinsic chart metric, positive definite only where $D\exp_\phi$ has full rank. [[gl-k-attention-2026-07-09-review-revision]]

## In this work

In this work, frame conditioning and belief natural gradients are separate mechanisms. The optional per-block conditioner can be compared empirically with heavy-ball or other frame updates, but it carries no full-$\mathrm{GL}(K)$ invariance or Fisher guarantee. The full-SPD AIRM and Gaussian Fisher statements remain valid on the belief side. [[gl-k-attention-2026-07-09-review-revision]]

## Sources

- [[amari-1998-natural-gradient]] — invariant-metric preconditioning as coordinate-free steepest descent; the statistical analogue of Killing-form preconditioning.
- [[amari-2000-methods-information-geometry]] — invariant metrics on parameter manifolds and the information-geometric framing.
- [[martens-2015-kfac]] — block-structured (Kronecker-factored) curvature preconditioning; template for the per-block gauge metric.
- [[absil-2008-optimization-matrix-manifolds]] — retractions and Riemannian steps on matrix manifolds, including Lie groups.
- [[bonnabel-2013-riemannian-sgd]] — convergence of stochastic Riemannian descent under an invariant metric.
- [[finzi-2020-lieconv]] — Lie-algebra (log) parameterization with $\exp$ recovery, the setting in which an algebra metric is the natural one.

## See also

- [[Gauge transformation]]
- [[Natural gradient]]
- [[Fisher information metric]]
- [[Baker-Campbell-Hausdorff formula]]
- [[Parallel transport]]
- [[Holonomy]]
- [[Group equivariance]]
- [[Irreducible representation]]
- [[LieConv]]
- [[Information geometry and natural gradient]]
- [[Gauge equivariance and geometric deep learning]]
- [[SPD-manifold geometry and Riemannian optimization]]
- [[VFE Transformer Program]]
