---
type: paper
title: Positive Definite Matrices
aliases:
  - "Bhatia 2007 — Positive Definite Matrices"
  - "bhatia-2009-positive-definite"
authors:
  - Rajendra Bhatia
year: 2007
arxiv: null
url: https://press.princeton.edu/books/paperback/9780691168258/positive-definite-matrices
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Positive Definite Matrices

> [!info] Citation
> Rajendra Bhatia. *Positive Definite Matrices*. Princeton Series in Applied Mathematics, Princeton University Press, 2007. ISBN 978-0-691-16825-8.
> URL: https://press.princeton.edu/books/paperback/9780691168258/positive-definite-matrices

## TL;DR

A graduate-level monograph that develops the analysis and geometry of positive definite matrices as a unified subject. Its central object is the cone of symmetric (or Hermitian) positive definite (SPD) matrices, which Bhatia equips with a natural Riemannian structure: the **affine-invariant** (canonical) metric whose geodesics, distance, and midpoint (the matrix geometric mean) all have closed forms. The book ties together operator-monotone and operator-convex functions, matrix means, the geometry of the SPD cone, and a suite of matrix inequalities. It is the standard mathematical reference for every operation one performs on a covariance matrix viewed as a point on a curved manifold.

## Problem & setting

The set of $n \times n$ SPD matrices, $\mathbb{P}_n$, is an open convex cone inside the vector space of Hermitian matrices, but treating it as a flat convex set discards essential structure: it is not closed under the operations one actually wants (e.g. the arithmetic mean of two SPD matrices is SPD, but it is not the "right" average; inversion sends the cone to itself but is not affine). Bhatia's program is to study $\mathbb{P}_n$ both as a metric/Riemannian space and through the lens of **operator monotonicity** and **operator convexity** — properties of scalar functions $f$ that lift consistently to matrices via the spectral calculus. The setting is functional analysis and matrix analysis, with constant attention to how scalar inequalities (AM–GM, Cauchy–Schwarz, Jensen) acquire noncommutative, matrix-valued forms.

## Method

The book builds its theory in layers:

- **Positivity and order.** The Löwner partial order $A \preceq B$ (meaning $B - A$ is positive semidefinite) organizes the subject. Operator-monotone functions are exactly those preserving this order; Löwner's theorem characterizes them via integral representations and analytic continuation to the upper half-plane.
- **Matrix means.** The geometric mean $A \# B = A^{1/2}\!\left(A^{-1/2} B A^{-1/2}\right)^{1/2} A^{1/2}$ is constructed and shown to be the unique operator mean with the expected symmetry and monotonicity. This is the metric midpoint of $A$ and $B$.
- **Riemannian geometry of the cone.** $\mathbb{P}_n$ carries the **affine-invariant metric** $\langle X, Y\rangle_A = \operatorname{tr}\!\left(A^{-1} X A^{-1} Y\right)$ at base point $A$. Under this metric the geodesic from $A$ to $B$ is $A^{1/2}\!\left(A^{-1/2} B A^{-1/2}\right)^{t} A^{1/2}$, the midpoint ($t=\tfrac12$) is the geometric mean, and the geodesic distance is
$$\delta(A,B) = \left\lVert \log\!\left(A^{-1/2} B A^{-1/2}\right) \right\rVert_F = \Big(\textstyle\sum_i \log^2 \lambda_i(A^{-1} B)\Big)^{1/2}.$$
  The metric is invariant under the **congruence (sandwich) action** $A \mapsto G A G^{*}$ for any invertible $G$, which is the property the name "affine-invariant" refers to and which makes the geometry compatible with linear reparameterization.
- **Inequalities and exponential metric increasing.** The cone has nonpositive curvature; consequences include the exponential metric increasing (EMI) property and convexity of the distance, which underpin existence and uniqueness of Riemannian (Karcher/Fréchet) means.

## Key results

- A self-contained derivation of the affine-invariant Riemannian metric on $\mathbb{P}_n$, its geodesics, and the closed-form geodesic distance $\delta(A,B)$ above.
- Identification of the matrix geometric mean as the geodesic midpoint, with its axiomatic characterization and monotonicity.
- The nonpositive-curvature (CAT(0) / Hadamard-type) character of the SPD cone under this metric, giving uniqueness of weighted geometric means and Riemannian barycenters.
- A complete account of operator-monotone and operator-convex functions and the matrix inequalities (Löwner, Lieb, Ando) that flow from them.

## Relevance to this research

In the VFE transformer, each token's belief is a Gaussian whose covariance $\Sigma$ is an SPD matrix; every geometric operation the model performs on $\Sigma$ is governed precisely by the structure this book formalizes.

- **`spd_affine` retraction and the affine-invariant metric.** The model's `spd_affine` map is the exponential map of exactly Bhatia's affine-invariant metric, and the per-token covariance distance / regularization uses the closed-form geodesic distance $\delta(\Sigma_1,\Sigma_2)$. This is the rigorous grounding for [[SPD-manifold geometry and Riemannian optimization]].
- **Congruence invariance meets the gauge group.** The metric's invariance under $\Sigma \mapsto G\,\Sigma\,G^{*}$ is precisely what makes SPD geometry compatible with the **block GL(k)** gauge action: a [[Gauge transformation]] of the frame acts on $\Sigma$ by congruence, and the affine-invariant distance is unchanged, so belief geometry is gauge-covariant by construction.
- **Geometric means for belief fusion.** Precision-weighted combination of Gaussian beliefs (the E-step's information-form updates and any averaging of covariances across heads or transported frames) is naturally a weighted matrix geometric mean / Riemannian barycenter, whose existence and uniqueness rest on the cone's nonpositive curvature established here.
- **Natural-gradient and Fisher geometry.** For a zero-mean Gaussian the Fisher metric on the covariance coincides with the affine-invariant metric studied here, linking this monograph directly to [[Fisher information metric]]–based [[Natural gradient]] updates on $\Sigma$.
- **Reference frame for log-Euclidean alternatives.** The affine-invariant geometry is the benchmark against which the cheaper log-Euclidean surrogate is judged; see [[arsigny-2006-log-euclidean]] and the affine-invariant tensor framework of [[pennec-2006-affine-invariant-tensor]].

> [!note] Editorial: The config term `spd_affine` denotes the affine-invariant retraction specifically (as opposed to a log-Euclidean or Bures–Wasserstein choice); this monograph is the canonical source for the formulas that retraction implements.

## Cross-links

Concepts and themes: [[SPD-manifold geometry and Riemannian optimization]] · [[Fisher information metric]] · [[Natural gradient]] · [[Gauge transformation]] · [[Parallel transport]] · [[Information geometry and natural gradient]]

Related sources: [[pennec-2006-affine-invariant-tensor]] · [[arsigny-2006-log-euclidean]] · [[absil-2008-optimization-matrix-manifolds]] · [[bonnabel-2013-riemannian-sgd]] · [[huang-2017-spdnet]] · [[wang-2023-riemannian-self-attention-spd]]

Project: [[VFE Transformer Program]]

```bibtex
@book{bhatia2007positive,
  author    = {Bhatia, Rajendra},
  title     = {Positive Definite Matrices},
  series    = {Princeton Series in Applied Mathematics},
  publisher = {Princeton University Press},
  year      = {2007},
  isbn      = {9780691168258},
  url       = {https://press.princeton.edu/books/paperback/9780691168258/positive-definite-matrices}
}
```
