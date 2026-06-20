---
type: paper
title: Stochastic Gradient Descent on Riemannian Manifolds
aliases:
  - Bonnabel 2013 — Riemannian SGD
authors:
  - Silvère Bonnabel
year: 2013
arxiv: "1111.5280"
url: https://arxiv.org/abs/1111.5280
tags:
  - cluster/spd-geometry
  - project/transformer
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-18
updated: 2026-06-18
---

# Stochastic Gradient Descent on Riemannian Manifolds

> [!info] Citation
> Silvère Bonnabel (2013). *Stochastic Gradient Descent on Riemannian Manifolds*. IEEE Transactions on Automatic Control, 58(9), 2217–2229. arXiv:[1111.5280](https://arxiv.org/abs/1111.5280).

## TL;DR

This paper generalizes the classical Robbins–Monro stochastic gradient descent (SGD) algorithm from flat Euclidean space to a connected Riemannian manifold, and proves that the resulting iterates converge almost surely to a critical point of the expected cost. The update replaces the Euclidean step `x - η∇f` with a step along a geodesic (or, more generally, a retraction): one follows the Riemannian gradient of a noisy per-sample cost a short distance along the manifold using the exponential map. The headline theoretical payoff is that the familiar SGD convergence guarantees — under decreasing step sizes satisfying the Robbins–Monro conditions `Σηₜ = ∞`, `Σηₜ² < ∞` — survive the move to curved spaces, given mild bounds on curvature and gradient growth. A worked application is a "gossip" averaging algorithm on the manifold of covariance (symmetric positive-definite) matrices.

## Problem & setting

Many learning problems optimize a cost that is naturally a function on a curved space rather than on `Rⁿ`: rotations, fixed-rank or orthogonal matrices, and — central to this research program — symmetric positive-definite (SPD) covariance matrices. Naively running Euclidean SGD on coordinates of such objects ignores the geometry, can leave the constraint set (e.g. produce a non-PSD matrix), and uses a metric that does not respect the problem's invariances. Bonnabel asks: when the objective `f(x) = E[Q(x, z)]` is an expectation over data `z` of a per-sample cost `Q`, and `x` lives on a Riemannian manifold `M`, can one still descend `f` using only cheap, noisy single-sample gradient estimates, and does such a scheme converge?

## Method

The proposed algorithm is the Riemannian analogue of SGD. At each step `t`, given a fresh sample `zₜ`:

1. Compute the **Riemannian gradient** `gradQ(xₜ, zₜ)` — the tangent vector at `xₜ` representing the steepest ascent direction of the per-sample cost with respect to the manifold's metric (this builds in the metric, e.g. the affine-invariant metric on SPD matrices via [[Fisher information metric]]-style preconditioning).
2. Take a step of size `ηₜ` against that gradient and **map back onto the manifold** with the exponential map (a geodesic step): `x_{t+1} = exp_{xₜ}(-ηₜ gradQ(xₜ, zₜ))`. The paper notes the exponential map may be replaced by any computationally cheaper retraction.

The step sizes obey the Robbins–Monro conditions. Convergence is established by adapting stochastic-approximation arguments to the manifold: under assumptions that the iterates stay in a region of bounded curvature (or are confined to a compact set), that the gradient noise has bounded variance, and that the injectivity radius is controlled, the sequence `f(xₜ)` converges and `gradf(xₜ) → 0` almost surely, so the iterates approach a critical point. As in the Euclidean case, only convergence to a *critical* point (not a global minimum) is guaranteed for non-convex `f`.

## Key results

- **Almost-sure convergence on manifolds.** The Riemannian SGD iterates converge to a critical point of `f`, mirroring the classical Euclidean SGD guarantee.
- **Retraction flexibility.** Geodesic steps via `exp` can be swapped for any first-order retraction without breaking the convergence argument, which is what makes the scheme practical when the true exponential map is expensive.
- **Application to covariance matrices.** A novel decentralized "gossip" algorithm for averaging SPD/covariance matrices is derived and numerically validated, demonstrating the framework on exactly the manifold that matters for belief covariances.

## Relevance to this research

The VFE transformer carries two families of curved-manifold parameters that are updated by stochastic, mini-batch gradients, and this paper supplies the theoretical license for doing so.

First, the per-token covariance `Σ` of each Gaussian belief is an **SPD matrix**, optimized under the affine-invariant Riemannian metric with an `spd_affine` retraction. Bonnabel's theorem is precisely the statement that taking exponential-map / retraction steps of a noisy Riemannian gradient on the SPD cone converges — so the M-step (and the E-step belief updates) over `Σ` can use ordinary mini-batch estimates instead of full-batch gradients without forfeiting convergence guarantees. The retraction-flexibility result directly justifies substituting the cheaper `spd_affine` retraction for the exact SPD exponential map. This is the optimization counterpart to the geometric machinery in [[pennec-2006-affine-invariant-tensor]] and [[bhatia-2007-positive-definite-matrices]], and it complements the general manifold-optimization toolbox of [[absil-2008-optimization-matrix-manifolds]].

Second, the **gauge parameters** live on the block general-linear group GL(k) and are updated through a Lie-algebra ("phi") parameterization with a BCH retraction — again a manifold, again trained by stochastic gradients. Bonnabel's result extends to such matrix-Lie-group parameters: the exp/retraction-step convergence argument is agnostic to which manifold, so the same guarantee underwrites Riemannian SGD on the gauge frames, not just on `Σ`.

Third, because the natural-gradient direction is itself the Riemannian gradient under the [[Fisher information metric]], this paper is the stochastic-approximation foundation under [[Natural gradient]] training in the mini-batch regime — the convergence theory that the natural-gradient analyses of [[amari-1998-natural-gradient]] and [[martens-2020-natural-gradient-insights]] presuppose when applied online. Together with [[bonnabel-2013-riemannian-sgd]]'s SPD gossip example, this makes the paper the load-bearing citation for "train SPD beliefs and gauge parameters with Riemannian mini-batch SGD" in this program.

## Cross-links

- Manifolds, geometry, and SPD covariances: [[SPD-manifold geometry and Riemannian optimization]], [[absil-2008-optimization-matrix-manifolds]], [[pennec-2006-affine-invariant-tensor]], [[bhatia-2007-positive-definite-matrices]], [[arsigny-2006-log-euclidean]]
- Natural gradient and information geometry: [[Natural gradient]], [[Fisher information metric]], [[amari-1998-natural-gradient]], [[martens-2020-natural-gradient-insights]], [[ollivier-2015-riemannian-metrics-nn]]
- SPD-valued networks and attention this enables: [[huang-2017-spdnet]], [[wang-2023-riemannian-self-attention-spd]]
- Program context: [[VFE Transformer Program]]

```bibtex
@article{bonnabel2013stochastic,
  author  = {Bonnabel, Silv{\`e}re},
  title   = {Stochastic Gradient Descent on {Riemannian} Manifolds},
  journal = {IEEE Transactions on Automatic Control},
  year    = {2013},
  volume  = {58},
  number  = {9},
  pages   = {2217--2229},
  doi     = {10.1109/TAC.2013.2254619},
  note    = {arXiv:1111.5280}
}
```
