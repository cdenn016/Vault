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
updated: 2026-06-18
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

The VFE transformer's gauge group is the block general-linear group GL($k$) (`gauge_group: block_glk`), and its gauge parameters live in the Lie algebra $\mathfrak{gl}(k)$ as matrix-valued $\phi$, mapped to the group by $\exp$ (the `gauge_parameterization: phi` setting; see [[Gauge transformation]]). The M-step that updates $\phi$ does not move it in a bare Euclidean direction: the config sets `phi_precond_mode: killing_per_block`, meaning each GL($k$) block's update is preconditioned by a Killing-form / invariant trace-form metric on that block's copy of the Lie algebra. The Killing form is therefore the *metric* attached to the gauge update — the object that decides what "steepest descent on $\phi$" means in a frame-respecting way.

The reason an ad-invariant form is the right metric is exactly the reason gauge invariance is the organizing principle of the architecture. A [[Gauge transformation]] is free to re-choose the frame at each token; the learning dynamics must not depend on that arbitrary choice. An $\operatorname{Ad}$-invariant inner product on the algebra is, by construction, blind to the frame — conjugating $\phi$ by a group element leaves its norm unchanged — so preconditioning the gauge update with it makes the M-step *covariant under the gauge symmetry* rather than fighting it. This is the gauge-theoretic sibling of the [[Natural gradient]]: where natural gradient divides out the [[Fisher information metric]] to make belief updates reparameterization-invariant, Killing-form preconditioning divides out the invariant algebra metric to make gauge updates frame-invariant. Both are instances of the same demand that learning follow the geometry of the model, not the coordinates it happens to be written in.

## Details

**An ad-invariant form is a bi-invariant metric.** Because $B$ is $\operatorname{Ad}$-invariant, transporting it from the identity tangent space (the algebra) around the group by left and right translation yields a single, consistently defined **bi-invariant (pseudo-)metric** on the Lie group itself. On a compact semisimple group, where $-B$ is positive-definite, this is an honest Riemannian metric whose geodesics through the identity are the one-parameter subgroups $t \mapsto \exp(tX)$. This is precisely the structure one wants for optimizing over group-valued parameters: the algebra carries a coordinate-free inner product, and the exponential map turns straight lines in the algebra into geodesics on the group. It is the geometric backbone behind handling gauge elements in logarithmic ($\phi$) coordinates and recovering group elements by $\exp$, the device shared with [[LieConv]] ([[finzi-2020-lieconv]]).

**The $\mathfrak{gl}(k)$ subtlety — be honest about degeneracy.** The gauge algebra here is $\mathfrak{gl}(k)$, which is **reductive, not semisimple**. It splits as $\mathfrak{gl}(k) = \mathfrak{sl}(k) \oplus \mathbb{R}\,I$, the traceless matrices plus the one-dimensional center of scalar matrices. The Killing form of $\mathfrak{gl}(k)$ is **degenerate**: a direct computation gives

$$
B(X, Y) \;=\; 2k\,\operatorname{tr}(XY) \;-\; 2\,\operatorname{tr}(X)\,\operatorname{tr}(Y),
$$

so on the center (scalar matrices, where $X \propto I$) the two terms cancel and $B$ vanishes identically — Cartan's criterion failing exactly because $\mathfrak{gl}(k)$ is not semisimple. Restricted to the semisimple part $\mathfrak{sl}(k)$ (where $\operatorname{tr} X = 0$) it reduces to the nondegenerate $B(X,Y) = 2k\,\operatorname{tr}(XY)$. The practical consequence is that the *literal* Killing form cannot serve as a metric on all of $\mathfrak{gl}(k)$, because it assigns zero length to the scalar (overall-scale) direction. The honest and standard remedy is to use the **nondegenerate invariant trace form**

$$
\langle X, Y\rangle \;=\; \operatorname{tr}(X^{\top} Y) \qquad\text{(or } \operatorname{tr}(XY)\text{)},
$$

which is positive-definite on all of $\mathfrak{gl}(k)$, agrees with the Killing form up to the scalar $2k$ on $\mathfrak{sl}(k)$, and is still $\operatorname{Ad}$-invariant under the relevant action. This is the working "Killing-type" metric that a per-block preconditioner actually uses; calling it "Killing" is a mild, conventional abuse — what is wanted is *an* ad-invariant nondegenerate trace form, and on a reductive algebra the trace form is the natural completion of the genuine Killing form on its semisimple part.

> [!note] Editorial: The config label `killing_per_block` names the *intent* — a per-block invariant trace-form metric on each $\mathfrak{gl}(k)$ block — rather than a claim that the literal, degenerate Killing form of $\mathfrak{gl}(k)$ is inverted. The identification of the working metric with $\operatorname{tr}(X^\top Y)$ as the nondegenerate completion of $B$ on the reductive algebra is the standard reading of these facts for this architecture, not a statement made verbatim in a registry source.

**Link to the natural-gradient / Fisher reading.** Viewing the gauge parameters as coordinates on a manifold, an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$ is an *invariant metric on parameter space*, and preconditioning the gradient by its inverse is structurally identical to a [[Natural gradient]] step preconditioned by the [[Fisher information metric]] (see [[amari-1998-natural-gradient]], [[amari-2000-methods-information-geometry]]). The difference is the source of the metric: Fisher comes from the statistical model's curvature, the Killing/trace form comes from the algebra's bracket structure — but both yield a coordinate-free steepest-descent direction. Doing this **per block** rather than over the whole parameter vector is exactly the block-structured curvature preconditioning of K-FAC ([[martens-2015-kfac]]): a large invariant metric is approximated by independent metrics on smaller blocks, here one $\mathfrak{gl}(k)$ block at a time. The Riemannian-optimization scaffolding — retractions standing in for exact group exponentials, with convergence guarantees — comes from [[absil-2008-optimization-matrix-manifolds]] and [[bonnabel-2013-riemannian-sgd]].

## In this work

Killing-form preconditioning is the gauge-side counterpart to natural-gradient preconditioning of the beliefs, and it surfaces in the config as:

- **`phi_precond_mode: killing_per_block`.** Each block of the block-GL($k$) gauge group carries its own invariant (Killing-type) trace-form metric, so the M-step update to that block's $\phi$ is a **per-block Riemannian / natural step** rather than a raw Euclidean one. The per-block factorization is the gauge analogue of the block-Kronecker Fisher approximation of [[martens-2015-kfac]], applied one GL($k$) block at a time.
- **Algebra-first parameterization.** Because gauge elements are stored as algebra-valued $\phi$ and recovered by $\exp$ (shared with [[finzi-2020-lieconv]]), the metric that governs their update naturally lives on the algebra — which is precisely where the Killing form is defined. The invariant trace form gives that tangent space a frame-independent inner product.
- **Composition by BCH.** Updates and positional gauges compose in the algebra through the [[Baker-Campbell-Hausdorff formula]] (`phi_retract_mode: bch`, `pos_phi_compose: bch`). The same bracket $[\cdot,\cdot]$ that drives the BCH series also *defines* the Killing form via $\operatorname{ad}$, so the metric and the composition law spring from one structure: the more non-abelian the block, the more both the BCH corrections and the off-diagonal Killing entries matter.
- **Reductive reality of GL($k$).** Because $\mathfrak{gl}(k)$ is reductive, the scalar (trace) direction has zero Killing length; using the nondegenerate $\operatorname{tr}(X^\top Y)$ keeps the overall-scale degree of freedom of each block preconditioned rather than left unmetered. This matters because the gauge congruence $\Sigma \mapsto g\,\Sigma\,g^{\top}$ acts on SPD covariances, and the scale component of $g$ genuinely moves the belief.

This sits alongside the matching design choices elsewhere in the architecture: the SPD covariance under the `spd_affine` retraction is updated by affine-invariant Riemannian descent, the beliefs by [[Natural gradient]], and the gauge by Killing-form preconditioning — three faces of one frame-invariant, geometry-respecting optimization philosophy, as catalogued in [[VFE Transformer Program]].

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
