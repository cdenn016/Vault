---
type: paper
title: "Adam: A Method for Stochastic Optimization"
aliases: ["Kingma 2015", "Adam: A Method for Stochastic Optimization"]
authors: ["Diederik P. Kingma", "Jimmy Ba"]
year: 2015
arxiv: 1412.6980
url: https://arxiv.org/abs/1412.6980
tags: [cluster/info-geometry, project/transformer, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Adam: A Method for Stochastic Optimization

> [!info] Citation
> Diederik P. Kingma, Jimmy Ba (2015). *Adam: A Method for Stochastic Optimization*. ICLR 2015; arXiv:1412.6980. https://arxiv.org/abs/1412.6980

## TL;DR

Adam is a first-order stochastic optimizer that maintains exponential moving averages of the gradient and its elementwise square, using bias-corrected first/second moment estimates to form a per-parameter adaptive step. It is the de facto default optimizer for deep models.

## Relevance to this research

Adaptive first-order optimizer; diagonal-preconditioning baseline against which the model's Fisher/Killing natural-gradient M-step is contrasted.

## Cross-links

- Concepts: [[Natural gradient]]
- Theme: [[Transformer interpretability and scaling]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{kingma2015adam,
  author={Kingma, Diederik P. and Ba, Jimmy},
  title={Adam: A Method for Stochastic Optimization},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2015}
}
```
