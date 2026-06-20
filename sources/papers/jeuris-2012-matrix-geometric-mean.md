---
type: paper
title: "A Survey and Comparison of Contemporary Algorithms for Computing the Matrix Geometric Mean"
aliases:
  - "Jeuris, Vandebril & Vandereycken 2012"
  - "Jeuris et al. (2012) Matrix Geometric Mean Survey"
authors:
  - Ben Jeuris
  - Raf Vandebril
  - Bart Vandereycken
year: 2012
arxiv: null
url: https://etna.math.kent.edu/volumes/2011-2020/vol39/abstract.php?vol=39&pages=379-402
tags:
  - cluster/spd-geometry
  - project/transformer
  - project/multi-agent
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# A Survey and Comparison of Contemporary Algorithms for Computing the Matrix Geometric Mean

> [!info] Citation
> Ben Jeuris, Raf Vandebril, and Bart Vandereycken (2012). "A Survey and Comparison of Contemporary Algorithms for Computing the Matrix Geometric Mean." *Electronic Transactions on Numerical Analysis* 39, 379–402. URL: https://etna.math.kent.edu/volumes/2011-2020/vol39/abstract.php?vol=39&pages=379-402

## TL;DR

A practical numerical survey of how to actually compute the affine-invariant geometric (Karcher) mean of several SPD matrices, comparing the leading algorithmic families on accuracy, cost, and how well they preserve the axiomatic properties of a geometric mean. It contrasts the Ando–Li–Mathias and Bini–Meini–Poloni recursive constructions against direct Riemannian optimization (gradient descent, conjugate gradient, BFGS, and Newton/trust-region methods) on the SPD manifold, giving the cost/quality trade-off that matters when one must repeatedly average covariances at scale.

## Problem & setting

The Karcher mean of $n>2$ SPD matrices has no closed form (see [[moakher-2005-geometric-mean]]); it is defined by a variational fixed-point and must be computed iteratively. Different definitions and algorithms ("geometric means" satisfying various subsets of the ALM axioms) proliferated, with very different per-iteration costs and convergence behavior. The paper standardizes the comparison: which method to use when $n$ and the matrix dimension vary, and what one sacrifices by choosing a cheaper surrogate.

## Method

The authors implement and benchmark recursive geometric-mean constructions (Ando–Li–Mathias, and the cheaper Bini–Meini–Poloni variants) alongside Riemannian-manifold optimizers — steepest descent, conjugate gradient, and quasi-Newton/Newton methods that use the SPD exponential, logarithm, and parallel transport. They measure iteration counts, floating-point cost (dominated by repeated matrix exp/log/sqrt and eigendecompositions), and accuracy against a high-precision reference.

## Key results

- Riemannian optimization (especially conjugate-gradient and trust-region/Newton) typically reaches the true Karcher mean fastest in iterations, but each step is dominated by costly matrix-function evaluations.
- Recursive ALM-type means are simple but expensive as $n$ grows; cheaper recursive variants trade some axiomatic fidelity for speed.
- There is no universally best algorithm: the choice depends on the number of matrices, their dimension, and the accuracy required, with clear regimes where a cheap approximate mean suffices.

## Relevance to this research

PIFB's coarse-graining averages many constituent covariances into one meta-agent covariance every time a meta-agent forms, at every scale of the Ouroboros tower. This paper quantifies exactly what that costs if done *properly* as an affine-invariant Karcher mean versus the model's one-shot sandwich-average shortcut. It is the numerical companion to [[moakher-2005-geometric-mean]]: Moakher says the true mean exists and is unique; Jeuris et al. say computing it is iteration-heavy and dominated by matrix exp/log/sqrt, which is precisely why the program adopts a cheap first-order pool by default and treats the exact Karcher barycenter as an opt-in correctness check. It grounds the cost side of the SPD-pooling design choice in [[Meta-agents and hierarchical emergence]] and [[SPD-manifold geometry and Riemannian optimization]].

## Cross-links

- Definition and uniqueness of the SPD geometric mean: [[moakher-2005-geometric-mean]], [[karcher-1977-center-of-mass]]
- SPD geometry and metrics: [[bhatia-2007-positive-definite-matrices]], [[pennec-2006-affine-invariant-tensor]], [[arsigny-2006-log-euclidean]]
- Manifold optimization machinery: [[absil-2008-optimization-matrix-manifolds]], [[bonnabel-2013-riemannian-sgd]]
- Meta-agent pooling cost: [[Meta-agents and hierarchical emergence]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{jeuris2012survey,
  title   = {A Survey and Comparison of Contemporary Algorithms for Computing the Matrix Geometric Mean},
  author  = {Jeuris, Ben and Vandebril, Raf and Vandereycken, Bart},
  journal = {Electronic Transactions on Numerical Analysis},
  volume  = {39},
  pages   = {379--402},
  year    = {2012}
}
```
