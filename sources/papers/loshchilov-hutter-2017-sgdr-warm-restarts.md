---
type: paper
title: "SGDR: Stochastic Gradient Descent with Warm Restarts"
aliases:
  - "Loshchilov & Hutter 2017 — SGDR"
  - SGDR
  - Cosine annealing with warm restarts
authors:
  - Ilya Loshchilov
  - Frank Hutter
year: 2017
arxiv: "1608.03983"
url: https://arxiv.org/abs/1608.03983
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# SGDR: Stochastic Gradient Descent with Warm Restarts

> [!info] Citation
> Ilya Loshchilov and Frank Hutter (2017). *SGDR: Stochastic Gradient Descent with Warm Restarts.* International Conference on Learning Representations (ICLR). arXiv:1608.03983. [arxiv.org/abs/1608.03983](https://arxiv.org/abs/1608.03983)

## TL;DR

SGDR is a learning-rate **schedule**, not a new optimizer: it anneals the step size along a cosine curve from a maximum down toward a minimum, then abruptly **restarts** it back to the maximum and repeats over successively longer cycles. Within cycle $i$ the rate is $\eta_t = \eta_{\min} + \tfrac{1}{2}(\eta_{\max}-\eta_{\min})\bigl(1 + \cos(\pi\, T_{\text{cur}}/T_i)\bigr)$, where $T_{\text{cur}}$ counts epochs since the last restart and $T_i$ is the (geometrically growing) cycle length. The warm restarts let the iterate jump out of a sharp basin and explore, while the cosine decay anneals it into a good minimum within each cycle; checkpoints taken at the end of each cycle also furnish a cheap ensemble ("snapshot" ensembling). It reaches competitive image-classification accuracy in noticeably fewer epochs than a fixed step-decay schedule.

## Relevance to this research

General deep-learning training context: the cosine-annealing-with-restarts schedule is a standard tool for the gradient-based outer loop, and the ML-engineer debate lens cites it as background for how the VFE transformer's learned-scalar and learned-table toggles (the default-OFF nn.Parameter exceptions) could be scheduled during training. The model's *capacity*, by contrast, comes from inner-loop VFE minimization over the Gaussian belief tuples $(\mu, \Sigma, \phi)$, not from this schedule, so SGDR sits strictly in the optimizer-hyperparameter periphery rather than the theoretical core.

> [!note] Editorial: The "warm restart" idea is unrelated to the program's belief-inertia / warm-start of the per-token variational E-step; the shared word is coincidental. SGDR restarts the *outer* learning rate, whereas belief inertia carries the *inner* posterior across steps.

## Cross-links

- Theme: [[Transformer interpretability and scaling]]
- Related sources: [[vaswani-2017-attention]] (the Transformer baseline such schedules train), [[amari-1998-natural-gradient]] and [[martens-2015-kfac]] (the natural-gradient / Fisher-preconditioning lineage the M-step prefers over plain SGD), [[bonnabel-2013-riemannian-sgd]] (manifold-aware stochastic descent).
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{loshchilov2017sgdr,
  title     = {{SGDR}: Stochastic Gradient Descent with Warm Restarts},
  author    = {Loshchilov, Ilya and Hutter, Frank},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2017},
  eprint    = {1608.03983},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url       = {https://arxiv.org/abs/1608.03983}
}
```
