---
type: paper
title: First-order Methods for Geodesically Convex Optimization
aliases:
  - "Zhang, Sra 2016"
  - "First-order Methods for Geodesically Convex Optimization"
authors:
  - Hongyi Zhang
  - Suvrit Sra
year: 2016
arxiv: 1602.06053
url: https://arxiv.org/abs/1602.06053
tags:
  - cluster/spd-geometry
  - cluster/methodology
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# First-order Methods for Geodesically Convex Optimization

> [!info] Citation
> Zhang, H., & Sra, S. (2016). First-order Methods for Geodesically Convex Optimization. Proceedings of the 29th Conference on Learning Theory (COLT 2016), PMLR 49:1617-1638. arXiv:1602.06053.

## TL;DR

Classical convex optimization rests on the linear structure of $\mathbb{R}^n$: a function is convex if it lies below its chords, and (sub)gradient descent converges because each step contracts the squared Euclidean distance to the optimum. On a curved manifold neither the chord nor the squared-distance contraction survives unchanged, so the textbook proofs break. Zhang and Sra give the first *global* iteration-complexity analysis of first-order methods for geodesically convex (g-convex) functions on Hadamard manifolds — complete, simply-connected Riemannian manifolds of nonpositive curvature, the class to which the affine-invariant SPD cone belongs. Their central device is a curvature-aware law-of-cosines comparison inequality that replaces the Euclidean "$\|x_{s+1}-x^*\|^2 \le \|x_s-x^*\|^2 - \dots$" step with a geodesic version carrying a single explicit curvature penalty $\zeta(\kappa,c)$. With that inequality in hand they recover the familiar rates of the flat theory — $O(1/\sqrt{t})$ for nonsmooth g-convex Lipschitz objectives via projected subgradient, with sharper behaviour under geodesic strong convexity and smoothness — now multiplied by a factor that degrades gracefully as the curvature lower bound and the domain diameter grow. The paper turned Riemannian first-order optimization from a collection of asymptotic, almost-sure convergence statements into a quantitative complexity theory.

## Problem & setting

The objects of study are functions $f:\mathcal{X}\to\mathbb{R}$ defined on a geodesically convex set $\mathcal{X}$ inside a Hadamard manifold $\mathcal{M}$. A function is **geodesically convex** if, for every minimizing geodesic $\gamma(t)$ joining two points, $f(\gamma(t)) \le (1-t)f(\gamma(0)) + t\,f(\gamma(1))$; equivalently, in the smooth case, $f(y) \ge f(x) + \langle \operatorname{grad} f(x),\, \operatorname{Exp}_x^{-1}(y)\rangle$, with the Euclidean displacement $y-x$ replaced by the logarithm map $\operatorname{Exp}_x^{-1}(y)$ — the tangent vector at $x$ pointing along the geodesic toward $y$. A function is **geodesically strongly convex** with modulus $\mu$ if this lower bound is strengthened by $\tfrac{\mu}{2}\,d^2(x,y)$, and **geodesically $L$-smooth** if its gradient is Lipschitz along geodesics. The prior art was almost entirely asymptotic: Udriște and the manifold-optimization texts of Absil, Mahony and Sepulchre established convergence in the limit, and Bonnabel (2013) proved *almost-sure* convergence of Riemannian stochastic gradient descent without a rate. What was missing — and what this paper supplies — is the finite-$t$ complexity, the manifold analogue of Nesterov's and Nemirovski's flat-space bounds, together with an explicit accounting of how curvature inflates the constants. Two structural assumptions carry the analysis: a lower bound $\kappa \le 0$ on the sectional curvature over the working domain, and an a-priori diameter bound, so that the curvature penalty stays finite.

## Method

The engine of the paper is a single trigonometric distance-comparison inequality. In a space of constant curvature $\kappa < 0$, the hyperbolic law of cosines makes a geodesic triangle "fatter" than its Euclidean comparison triangle; bounding this discrepancy yields a curvature constant
$$ \zeta(\kappa, c) \;=\; \frac{\sqrt{|\kappa|}\,c}{\tanh\!\big(\sqrt{|\kappa|}\,c\big)}, $$
where $c$ is a bound on the geodesic distance traversed (the domain diameter, or $d(x_s, x^*)$ at step $s$). Note that $\zeta \to 1$ as $\kappa \to 0$ or $c \to 0$, recovering the Euclidean constant, and $\zeta \ge 1$ always, so curvature can only hurt, never help, in this bound. The comparison lemma then upgrades the Euclidean "one-step progress" identity to its geodesic form: for a subgradient step $x_{s+1} = \operatorname{Exp}_{x_s}\!\big(-\eta_s\,\operatorname{grad} f(x_s)\big)$,
$$ \langle -\operatorname{grad} f(x_s),\, \operatorname{Exp}_{x_s}^{-1}(x^*)\rangle \;\le\; \frac{1}{2\eta_s}\big(d^2(x_s, x^*) - d^2(x_{s+1}, x^*)\big) \;+\; \frac{\zeta(\kappa, c)}{2}\,\eta_s\,\|\operatorname{grad} f(x_s)\|^2 . $$
Telescoping the left side against the g-convexity inequality $f(x_s) - f(x^*) \le \langle \operatorname{grad} f(x_s), -\operatorname{Exp}_{x_s}^{-1}(x^*)\rangle$ reproduces the classical descent-lemma bookkeeping, but with every "gradient-squared" term scaled by $\zeta$. From this skeleton the authors derive deterministic and stochastic, smooth and nonsmooth, plain and strongly-convex variants, each by the standard step-size choice that balances the two terms on the right.

## Key results

The paper proves the first global iteration-complexity bounds for first-order g-convex optimization on Hadamard manifolds. For a nonsmooth g-convex $L_f$-Lipschitz objective, projected Riemannian subgradient descent attains an $O(1/\sqrt{t})$ rate on the optimality gap, with the constant inflated by $\zeta(\kappa, c)$ relative to the flat-space bound — i.e. the rate matches Euclidean subgradient descent up to a multiplicative curvature factor. Under geodesic smoothness the deterministic gradient method achieves the faster $O(1/t)$ behaviour, and under geodesic strong convexity the rate improves further (linear convergence in the smooth-and-strongly-convex regime), again with the curvature dependence isolated in $\zeta$. The stochastic Riemannian (sub)gradient method is shown to converge at the curvature-modulated $O(1/\sqrt{t})$ rate in expectation, giving a finite-time complement to Bonnabel's earlier almost-sure result. The evidence is a set of rigorous upper bounds, not benchmark experiments; the contribution is theoretical, and the strength of the guarantees is exactly that of the Euclidean templates they generalize, modulo the curvature constant and the two standing assumptions (curvature lower bound, diameter bound). Later work — including the authors' own Riemannian accelerated and SVRG analyses and the 2025 "Revisit" line of quasilinearization arguments — has since relaxed those assumptions while keeping the same rates, confirming the framework's durability.

## Relevance to this research

This paper is the quantitative convergence theory for the SPD-geometry **M-step** of the VFE transformer's variational EM, the layer where the covariance / precision parameters of the Gaussian belief tuples $(\mu, \Sigma, \phi)$ are updated. Under the affine-invariant metric, the SPD cone $\mathcal{P}(n)$ is a Hadamard manifold of nonpositive sectional curvature, so the free-energy terms that are geodesically convex in $\Sigma$ fall directly inside Zhang and Sra's hypotheses, and their $\zeta(\kappa, c)$-modulated $O(1/\sqrt{t})$ and $O(1/t)$ rates give a finite-time complexity statement that Bonnabel's almost-sure SGD convergence ([[bonnabel-2013-riemannian-sgd]]) leaves open. The curvature constant matters operationally: it quantifies how the affine-invariant cone's negative curvature and the spread of the iterates inflate the step-count, informing step-size schedules for Riemannian descent on $\Sigma$ and warning that wide-diameter trajectories pay a price. The affine-invariant structure these rates depend on is the same one catalogued under [[SPD-manifold geometry and Riemannian optimization]], built on the metric of [[pennec-2006-affine-invariant-tensor]], and the comparison lemma's logarithm-map machinery is exactly the geometry that the [[Parallel transport]] and exp/log operations in the transport layer assume.

## Cross-links

- Concepts / Themes: [[SPD-manifold geometry and Riemannian optimization]]
- Related sources: [[bonnabel-2013-riemannian-sgd]], [[pennec-2006-affine-invariant-tensor]], [[amari-1998-natural-gradient]]

## BibTeX

```bibtex
@inproceedings{zhangsra2016geodes,
  author    = {Zhang, Hongyi and Sra, Suvrit},
  title     = {First-order Methods for Geodesically Convex Optimization},
  booktitle = {Proceedings of the 29th Conference on Learning Theory (COLT)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {49},
  pages     = {1617--1638},
  year      = {2016},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v49/zhang16b.html},
  eprint    = {1602.06053},
  archivePrefix = {arXiv},
  primaryClass  = {math.OC}
}
```
