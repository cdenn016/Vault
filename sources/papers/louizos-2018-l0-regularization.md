---
type: paper
title: "Learning Sparse Neural Networks through L0 Regularization"
aliases:
  - "louizos-2018-l0"
  - "louizos2018l0"
authors:
  - "Louizos, Christos"
  - "Welling, Max"
  - "Kingma, Diederik P."
year: 2018
url: https://arxiv.org/abs/1712.01312
venue: "ICLR 2018"
tags:
  - cluster/attention
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Learning Sparse Neural Networks through L0 Regularization

> [!info] Citation
> Louizos, Christos, Welling, Max, Kingma, Diederik P. (2018). "Learning Sparse Neural Networks through L0 Regularization." ICLR 2018. https://arxiv.org/abs/1712.01312

## TL;DR
Introduces a practical method for L0 (count-of-nonzero) regularization of neural-network weights using a differentiable hard-concrete relaxation of stochastic gates, enabling end-to-end gradient-based learning of sparse, pruned networks. The technique yields true zeros and computational savings without post-hoc thresholding.

## Relevance to this research
Voita et al. (2019) use this L0 relaxation to prune attention heads, identifying specialized versus prunable heads — directly relevant to analyzing and sparsifying the attention structure of the VFE transformer.

## Cross-links
[[Attention mechanisms — theory and positional structure]]

## BibTeX
```bibtex
@inproceedings{louizos2018l0,
  title={Learning Sparse Neural Networks through $L_0$ Regularization},
  author={Louizos, Christos and Welling, Max and Kingma, Diederik P.},
  booktitle={International Conference on Learning Representations (ICLR)},
  year={2018},
  eprint={1712.01312},
  archivePrefix={arXiv}
}
```
