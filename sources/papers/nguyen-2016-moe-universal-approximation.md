---
type: paper
title: "A Universal Approximation Theorem for Mixture-of-Experts Models"
aliases:
  - Nguyen 2016
  - Nguyen2016MoEUniversal
  - MoE universal approximation
authors:
  - Nguyen, Hien D.
  - Lloyd-Jones, Luke R.
  - McLachlan, Geoffrey J.
year: 2016
arxiv: "1602.03683"
doi: "10.1162/NECO_a_00892"
url: https://arxiv.org/abs/1602.03683
tags:
  - cluster/attention
  - project/transformer
  - field/statistics
  - field/cs-ml
created: 2026-10-28
---

# A Universal Approximation Theorem for Mixture-of-Experts Models

> [!info] Citation
> Nguyen, H. D., Lloyd-Jones, L. R., & McLachlan, G. J. (2016). *A universal approximation theorem for mixture-of-experts models*. Neural Computation 28(12), 2585–2593.

## TL;DR
The class of mixture-of-experts mean functions, with softmax gates whose logits are affine in the input, is dense in the continuous functions on any compact domain. Earlier results gave uniform convergence only for sufficiently differentiable Sobolev targets on the unit hypercube.

## Method
The proof applies the Stone–Weierstrass theorem to a subclass of mean functions that satisfies its algebra and separation conditions, then notes the subclass lies inside the full class. The result is for scalar outputs, gives no rate, and makes no claim about statistical estimation from data.

## Relevance to this research
With shared cue variances and a fixed record covariance, the [[Cue-result generative memory]] is a softmax-gated mixture of affine experts with affine logits and, with dense regressions, contains every such mixture; this theorem then gives a scalar, fixed-covariance approximation corollary for each coordinate of the block mean ([[dennis-2026-cue-result-memory]]).

## Cross-links
- Methods: [[Cue-result generative memory]], [[Template routing]]
- Related sources: [[jacobs-1991-mixtures-of-local-experts]], [[xu-1995-alternative-mixtures-of-experts]]

## BibTeX
```bibtex
@article{Nguyen2016MoEUniversal,
  author  = {Nguyen, Hien D. and Lloyd-Jones, Luke R. and McLachlan, Geoffrey J.},
  title   = {A Universal Approximation Theorem for Mixture-of-Experts Models},
  journal = {Neural Computation},
  volume  = {28},
  number  = {12},
  pages   = {2585--2593},
  year    = {2016},
  doi     = {10.1162/NECO_a_00892}
}
```
