---
type: paper
title: "Deep Learning via Hessian-Free Optimization"
aliases:
  - "Martens 2010 — Hessian-Free Optimization"
  - "HF"
authors:
  - James Martens
year: 2010
url: https://www.cs.toronto.edu/~jmartens/docs/Deep_HessianFree.pdf
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
created: 2026-06-20
updated: 2026-06-20
---

# Deep Learning via Hessian-Free Optimization

> [!info] Citation
> James Martens (2010). "Deep Learning via Hessian-Free Optimization." *Proceedings of the 27th International Conference on Machine Learning (ICML 2010)*, pp. 735–742. <https://www.cs.toronto.edu/~jmartens/docs/Deep_HessianFree.pdf>

## TL;DR

This paper revives truncated-Newton ("Hessian-free") optimization for deep networks: it minimizes a local quadratic model of the loss by running conjugate gradient against curvature-vector products, computed exactly via the Pearlmutter R-operator, so the curvature matrix is never formed or stored. Using the positive-semidefinite Gauss–Newton matrix `G` in place of the indefinite Hessian, plus Tikhonov damping and CG-preconditioning, it trains deep autoencoders from scratch without layer-wise pretraining — a then-surprising result that put second-order, curvature-aware methods back on the deep-learning table.

## Relevance to this research

General second-order-optimization background, not VFE theory the no-NN model uses directly. It is the truncated-Newton antecedent in the curvature-aware preconditioning lineage that the project's [[Natural gradient|natural-gradient]] / [[Fisher information metric|Fisher]]-preconditioned M-step belongs to, where the Gauss–Newton matrix coincides with the Fisher information for the model's exponential-family beliefs; the gauge-theory and ML-engineer debate lenses cite it as the historical root of the K-FAC line ([[martens-2015-kfac]]) that makes such curvature preconditioning tractable block-by-block.

## Cross-links

- Concept: [[Natural gradient]]
- Theme: [[Information geometry and natural gradient]]
- Sources: [[martens-2015-kfac]], [[martens-2020-natural-gradient-insights]], [[amari-1998-natural-gradient]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{martens2010hessianfree,
  title     = {Deep Learning via Hessian-Free Optimization},
  author    = {Martens, James},
  booktitle = {Proceedings of the 27th International Conference on Machine Learning (ICML)},
  pages     = {735--742},
  year      = {2010},
  url       = {https://www.cs.toronto.edu/~jmartens/docs/Deep_HessianFree.pdf}
}
```
