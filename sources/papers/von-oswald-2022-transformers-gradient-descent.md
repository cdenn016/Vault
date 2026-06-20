---
type: paper
title: "Transformers Learn In-Context by Gradient Descent"
aliases:
  - "von Oswald et al. 2022"
  - "von Oswald (2023) In-Context GD"
authors:
  - Johannes von Oswald
  - Eyvind Niklasson
  - Ettore Randazzo
  - João Sacramento
  - Alexander Mordvintsev
  - Andrey Zhmoginov
  - Max Vladymyrov
year: 2023
arxiv: "2212.07677"
url: https://arxiv.org/abs/2212.07677
tags:
  - cluster/vfe
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Transformers Learn In-Context by Gradient Descent

> [!info] Citation
> Johannes von Oswald, Eyvind Niklasson, Ettore Randazzo, João Sacramento, Alexander Mordvintsev, Andrey Zhmoginov, and Max Vladymyrov (2023). "Transformers Learn In-Context by Gradient Descent." ICML 2023. arXiv:2212.07677. <https://arxiv.org/abs/2212.07677>

## TL;DR

This paper shows that a transformer's forward pass can **implement gradient descent**: for in-context regression, a single linear self-attention layer can be constructed to perform exactly one step of gradient descent on a least-squares loss defined by the context examples, and a stack of such layers performs the corresponding multi-step descent. Trained transformers are then shown to converge to weights that match these hand-built gradient-descent constructions. In-context learning is thus, mechanistically, an optimizer unrolled across depth — depth indexes iterations of an inner learning algorithm.

## Problem & setting

In-context learning — adapting to a task from examples in the prompt without weight updates — looks like meta-learning but its mechanism was unclear. The authors restrict to in-context linear regression and ask whether the layer-to-layer computation is recognizably an optimization procedure.

## Method

They construct explicit weights for linear self-attention layers that realize a gradient-descent update on the in-context loss, prove the construction is exact for the linear case, and then train transformers from scratch on the same task, comparing learned behavior, intermediate predictions, and sensitivity to the construction. They extend the analysis toward curvature-corrected (preconditioned) descent and to nonlinear cases.

## Key results

- One linear-attention layer = one gradient-descent step on the context least-squares loss; $L$ layers = $L$ steps (an unrolled optimizer).
- Trained transformers recover this solution: their per-layer intermediate predictions track those of the explicit gradient-descent transformer.
- The mechanism extends to preconditioned / curvature-aware descent and offers a lens on deeper, nonlinear in-context learning.

## Relevance to this research

This is the cleanest external warrant for the PIFB ([[participatory-it-from-bit]]) identity **depth = iterations of an inner optimization**. PIFB asserts that a forward pass is not feature extraction but **iterative variational free-energy minimization**: each layer is one E-step that descends the [[Variational free energy]] on the belief tuples $(\mu, \Sigma, \phi)$. von Oswald et al. independently establish, for the conventional transformer, that depth literally runs an optimizer — making the PIFB reading a special, principled case rather than an idiosyncratic reinterpretation, with the descended objective being a free energy on the [[Statistical manifold]] rather than a least-squares loss. The extension to *preconditioned* gradient descent is the precise hook for PIFB's geometry: the project descends $F$ along the **natural gradient** with respect to the Fisher / SPD metric on the belief manifold, which is exactly curvature-corrected descent. This ties the paper to [[Iterative amortized inference]] (a forward pass as amortized optimization of a variational objective; see [[marino-2018-iterative-amortized-inference]]) and to the natural-gradient machinery of [[amari-1998-natural-gradient]]. Where this project differs is that the inner objective and its geometry are specified a priori by the VFE construction rather than learned into the weights — but the structural claim, depth as unrolled inference, is the same.

## Cross-links

- Concepts: [[Iterative amortized inference]], [[Variational free energy]], [[Natural gradient]]
- Sources: [[marino-2018-iterative-amortized-inference]], [[amari-1998-natural-gradient]], [[vaswani-2017-attention]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@inproceedings{vonoswald2023transformers,
  title         = {Transformers Learn In-Context by Gradient Descent},
  author        = {von Oswald, Johannes and Niklasson, Eyvind and Randazzo, Ettore and
                   Sacramento, Jo{\~a}o and Mordvintsev, Alexander and
                   Zhmoginov, Andrey and Vladymyrov, Max},
  booktitle     = {Proceedings of the 40th International Conference on Machine Learning (ICML)},
  year          = {2023},
  eprint        = {2212.07677},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2212.07677}
}
```
