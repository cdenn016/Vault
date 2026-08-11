---
type: paper
title: "On Sparse Variational Methods and the Kullback-Leibler Divergence between Stochastic Processes"
aliases:
  - "Matthews et al. 2016 process-space KL"
authors:
  - Alexander G. de G. Matthews
  - James Hensman
  - Richard Turner
  - Zoubin Ghahramani
year: 2016
arxiv: 1504.07027
url: https://proceedings.mlr.press/v51/matthews16.html
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/statistics
  - field/mathematics
  - field/cs-ml
created: 2026-08-10
---

# On Sparse Variational Methods and the Kullback-Leibler Divergence between Stochastic Processes

> [!info] Citation
> Matthews, A. G. de G., Hensman, J., Turner, R., & Ghahramani, Z. (2016). On Sparse Variational Methods and the Kullback-Leibler Divergence between Stochastic Processes. In *Proceedings of the 19th International Conference on Artificial Intelligence and Statistics*, PMLR 51, 231-239. https://proceedings.mlr.press/v51/matthews16.html

## TL;DR

Matthews and colleagues place sparse Gaussian-process variational inference on a rigorously defined KL divergence between stochastic-process laws, including infinite index sets. Their augmentation analysis shows that matching the original marginal law is not sufficient to preserve the original variational problem: an additional conditional-law condition is required.

## Problem & setting

Sparse Gaussian-process methods introduce inducing variables or an enlarged index set. Earlier arguments often treated marginal consistency of the augmentation as enough to guarantee that optimization in the enlarged space was equivalent to optimization for the original process. The paper asks when the process-level KL and its augmented representation are actually the same variational objective.

## Method

The authors work with probability measures on stochastic-process spaces and use the KL chain rule on an augmented product space. If $U$ denotes added variables and $V$ the original variables, then

$$
D_{\mathrm{KL}}(Q_{U,V}\|P_{U,V})
=D_{\mathrm{KL}}(Q_V\|P_V)
+\mathbb E_{Q_V}D_{\mathrm{KL}}(Q_{U\mid V}\|P_{U\mid V}).
$$

Marginal consistency controls only the first term. Equality with the original variational objective additionally requires the conditional contribution to vanish under the relevant law.

## Key results

The paper gives a process-space interpretation of sparse variational inference for infinite index sets, permits inducing variables beyond observed inputs, and identifies the missing conditional requirement in marginally consistent augmentations. Its conclusions are about the specified process and augmentation setting; they do not construct arbitrary continuum field measures or settle tightness, regularity, or gauge compatibility.

## Relevance to this research

[[Process-space variational inference]] records the direct consequence for the gauge-VFE program. A compatible family of finite agent designs is necessary but does not alone define a continuum recognition law or preserve an augmented ELBO. The current finite [[Multi-agent variational free energy]] remains an oracle on declared finite laws; any continuum extension must separately establish the process law, projective compatibility, dominance/finite KL, and the conditional equivalence of auxiliary variables.

## Cross-links

- Concepts: [[Process-space variational inference]], [[Evidence lower bound (ELBO)]], [[Gaussian process]], [[Multi-agent variational free energy]]

## BibTeX

```bibtex
@inproceedings{matthews2016stochasticprocesskl,
  author    = {Matthews, Alexander G. de G. and Hensman, James and Turner, Richard and Ghahramani, Zoubin},
  title     = {On Sparse Variational Methods and the Kullback-Leibler Divergence between Stochastic Processes},
  booktitle = {Proceedings of the 19th International Conference on Artificial Intelligence and Statistics},
  series    = {Proceedings of Machine Learning Research},
  volume    = {51},
  pages     = {231--239},
  year      = {2016},
  url       = {https://proceedings.mlr.press/v51/matthews16.html}
}
```
