---
type: paper
title: Optimizing Neural Networks with Kronecker-factored Approximate Curvature
aliases:
  - "Martens & Grosse 2015 — K-FAC"
  - K-FAC
authors:
  - James Martens
  - Roger Grosse
year: 2015
arxiv: "1503.05671"
url: https://arxiv.org/abs/1503.05671
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Optimizing Neural Networks with Kronecker-factored Approximate Curvature

> [!info] Citation
> James Martens and Roger Grosse (2015). *Optimizing Neural Networks with Kronecker-factored Approximate Curvature.* arXiv:1503.05671. [arxiv.org/abs/1503.05671](https://arxiv.org/abs/1503.05671)

## TL;DR

K-FAC makes [[Natural gradient|natural gradient]] descent practical for neural networks by approximating the [[Fisher information metric|Fisher information matrix]] as a block structure whose blocks are *Kronecker products* of two much smaller matrices — one from the layer's input activations and one from the backpropagated output gradients. Because a Kronecker product inverts as the Kronecker product of the inverses, the otherwise intractable Fisher inverse needed for a natural-gradient step becomes cheap, with storage and inversion cost independent of the mini-batch size. This non-diagonal yet tractable curvature approximation lets K-FAC make far more progress per update than well-tuned stochastic gradient descent with momentum.

## Problem & setting

The natural gradient (see [[amari-1998-natural-gradient]]) preconditions the ordinary gradient by the inverse of the Fisher information matrix `F`, yielding the steepest-descent direction in the parameter manifold's intrinsic (KL) geometry rather than in raw Euclidean coordinates. This is theoretically attractive — it is invariant to reparameterization and follows the model's information geometry — but `F` is a dense `N x N` matrix in the number of parameters `N`, so forming, storing, and inverting it is hopeless for modern networks. Diagonal or purely empirical approximations throw away the cross-parameter correlations that make the natural gradient valuable. The paper asks: is there an approximation of `F` that keeps rich off-diagonal structure yet remains cheap to invert and apply, and that behaves well in the *stochastic* (mini-batch) regime where second-order methods historically struggle?

## Method

K-FAC rests on a key structural observation. For a single layer, the Fisher block coupling that layer's weights factorizes (under an independence approximation) into a Kronecker product

```
F_layer  ≈  A ⊗ G
```

where `A` is the second-moment matrix of the layer's *input activations* and `G` is the second-moment matrix of the *gradients of the loss w.r.t. that layer's outputs* (the backpropagated signal). Both `A` and `G` are small — their sizes are set by the layer width, not the total parameter count. The Kronecker identity `(A ⊗ G)^{-1} = A^{-1} ⊗ G^{-1}` then turns the expensive inverse of a large block into two small inverses. The full Fisher is approximated as **block-diagonal** (one block per layer; the basic version) or **block-tridiagonal** (capturing adjacent-layer correlations via a more refined Gaussian-graphical-model derivation). The resulting preconditioned update is combined with a Tikhonov/Levenberg–Marquardt damping term and an adaptive learning-rate and momentum schedule derived from the local quadratic model, so the method stays stable when the curvature estimate is noisy. Critically, the activation and gradient statistics are accumulated as running averages, making cost independent of batch size.

## Key results

- On deep autoencoder benchmarks, K-FAC optimizes the training objective substantially faster (in wall-clock and in iterations) than carefully tuned SGD with momentum, especially in the later, ill-conditioned phase of training.
- The block-tridiagonal variant, which models correlations between neighboring layers, outperforms the simpler block-diagonal one, confirming that the captured off-diagonal curvature is doing real work.
- Performance degrades gracefully in the stochastic setting: because storage and inversion cost do not grow with batch size, K-FAC remains usable with realistic mini-batches, unlike classical Hessian-free / Gauss–Newton approaches.

## Relevance to this research

K-FAC is the practical template for the **per-block Fisher preconditioning** at the heart of this project's M-step. The VFE transformer's parameters live on a [[Gauge transformation|gauge]] structure organized as the block general-linear group GL(k): the Lie-algebra "phi" parameters are naturally grouped into blocks, and the architecture applies *Killing-form per-block preconditioning* when updating them. K-FAC supplies exactly the missing ingredient — a way to approximate and invert the curvature **block by block** rather than globally — so that a [[Natural gradient|natural-gradient]] / [[Fisher information metric|Fisher]]-preconditioned parameter update stays tractable at scale. The Kronecker factorization (input-side statistics ⊗ output-side statistics) is the concrete mechanism that makes the block GL(k) preconditioner cheap, mirroring how K-FAC factors each layer's Fisher.

Because the model is trained as a variational free-energy / variational-EM objective ([[neal-1998-variational-em]]), the M-step is precisely a parameter optimization over a probabilistic model, the regime where natural gradient and its Fisher geometry are best motivated (see also [[martens-2020-natural-gradient-insights]] and [[ollivier-2015-riemannian-metrics-nn]]). K-FAC connects that information-geometric ideal to an implementable update rule.

> [!note] Editorial: K-FAC's Kronecker/block view also rhymes structurally with the project's SPD-manifold preconditioning of the covariance `Sigma` — both replace a dense metric with a factored, manifold-aware one — though K-FAC itself addresses Euclidean parameters under a KL/Fisher metric, not the affine-invariant SPD metric.

## Cross-links

- [[Natural gradient]] — the update K-FAC is approximating.
- [[Fisher information metric]] — the curvature matrix being Kronecker-factored.
- [[amari-1998-natural-gradient]] — origin of natural gradient.
- [[martens-2020-natural-gradient-insights]] — later unifying perspective on natural gradient and its approximations.
- [[ollivier-2015-riemannian-metrics-nn]] — Riemannian/Fisher metrics for neural-network training.
- [[amari-2000-methods-information-geometry]] — information-geometry foundations.
- [[neal-1998-variational-em]] — the variational-EM setting whose M-step uses this preconditioning.
- Theme: [[Information geometry and natural gradient]].
- Project: [[VFE Transformer Program]].

## BibTeX

```bibtex
@article{martens2015kfac,
  title   = {Optimizing Neural Networks with Kronecker-factored Approximate Curvature},
  author  = {Martens, James and Grosse, Roger},
  journal = {arXiv preprint arXiv:1503.05671},
  year    = {2015},
  eprint  = {1503.05671},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url     = {https://arxiv.org/abs/1503.05671}
}
```
