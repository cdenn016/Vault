---
type: paper
title: "Decoupled Weight Decay Regularization (AdamW)"
aliases: ["Loshchilov 2019", "Decoupled Weight Decay Regularization (AdamW)"]
authors: ["Ilya Loshchilov", "Frank Hutter"]
year: 2019
arxiv: 1711.05101
url: https://arxiv.org/abs/1711.05101
tags: [cluster/info-geometry, project/transformer, field/cs-ml]
created: 2026-06-20
updated: 2026-06-20
---

# Decoupled Weight Decay Regularization (AdamW)

> [!info] Citation
> Ilya Loshchilov, Frank Hutter (2019). *Decoupled Weight Decay Regularization (AdamW)*. ICLR 2019; arXiv:1711.05101. https://arxiv.org/abs/1711.05101

## TL;DR

Shows that L2 regularization and weight decay are not equivalent for adaptive optimizers like Adam, and that decoupling weight decay from the gradient-based update (AdamW) substantially improves generalization and makes the regularization strength independent of the learning rate.

## Relevance to this research

Decoupled weight decay; the optimizer used for the model's learned-scalar toggles.

## Cross-links

- Concepts: [[Natural gradient]]
- Theme: [[Transformer interpretability and scaling]]
- Project: [[VFE Transformer Program]]

## BibTeX

```bibtex
@inproceedings{loshchilov2019adamw,
  author={Loshchilov, Ilya and Hutter, Frank},
  title={Decoupled Weight Decay Regularization},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2019}
}
```
