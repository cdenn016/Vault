---
type: paper
title: "Understanding the Difficulty of Training Deep Feedforward Networks"
aliases:
  - "Glorot & Bengio 2010 — Xavier init"
  - "Glorot (2010) Xavier Initialization"
authors:
  - Xavier Glorot
  - Yoshua Bengio
year: 2010
url: https://proceedings.mlr.press/v9/glorot10a.html
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Understanding the Difficulty of Training Deep Feedforward Networks

> [!info] Citation
> Xavier Glorot and Yoshua Bengio (2010). "Understanding the Difficulty of Training Deep Feedforward Networks." Proceedings of the 13th International Conference on Artificial Intelligence and Statistics (AISTATS), PMLR 9:249–256. <https://proceedings.mlr.press/v9/glorot10a.html>

## TL;DR

This paper diagnoses why deep feedforward nets trained poorly under the standard practices of the time: activation saturation and a depth-dependent collapse of activation and gradient variance, traced to a mismatch between the initialization scale and the layer fan-in/fan-out. The remedy is the **normalized "Xavier" (Glorot) initialization** $W \sim \mathcal{U}[-\sqrt{6/(n_{\text{in}}+n_{\text{out}})}, +\sqrt{6/(n_{\text{in}}+n_{\text{out}})}]$, chosen so the variance of forward activations and back-propagated gradients is preserved across layers. It established variance-preservation as the design principle behind weight initialization.

## Relevance to this research

General deep-learning-training background only: the VFE transformer is the no-neural-network path, so its capacity comes from iterative VFE minimization over belief tuples $(\mu, \Sigma, \phi)$ rather than from trained weight matrices, and it does not use Xavier initialization. The expert panels (the ML-engineering review lens) cite it as canonical context for initialization and the variance-preservation heuristic when discussing the small set of default-OFF learned-scalar/table toggles and the float32 numerical conditioning of the SPD kernels.

## Cross-links

- Theme: [[Transformer interpretability and scaling]]
- Sources: [[he-2015-delving-deep-rectifiers]], [[vaswani-2017-attention]], [[kaplan-2020-scaling-laws]]
- Project: [[VFE Transformer Program]]

```bibtex
@inproceedings{glorot2010understanding,
  title     = {Understanding the Difficulty of Training Deep Feedforward Neural Networks},
  author    = {Glorot, Xavier and Bengio, Yoshua},
  booktitle = {Proceedings of the 13th International Conference on Artificial Intelligence and Statistics (AISTATS)},
  series    = {Proceedings of Machine Learning Research},
  volume    = {9},
  pages     = {249--256},
  year      = {2010},
  publisher = {PMLR},
  url       = {https://proceedings.mlr.press/v9/glorot10a.html}
}
```
