---
type: paper
title: Bucket Renormalization for Approximate Inference
aliases:
  - Ahn et al. 2018 bucket renormalization
authors:
  - Sungsoo Ahn
  - Michael Chertkov
  - Adrian Weller
  - Jinwoo Shin
year: 2018
arxiv: "1803.05104"
url: https://proceedings.mlr.press/v80/ahn18a.html
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - field/cs-ml
  - field/physics
  - field/statistics
status: stable
created: 2026-08-10
updated: 2026-08-10
---

# Bucket Renormalization for Approximate Inference

> [!info] Citation
> Sungsoo Ahn, Michael Chertkov, Adrian Weller, and Jinwoo Shin. “Bucket Renormalization for Approximate Inference.” *Proceedings of the 35th International Conference on Machine Learning*, PMLR 80:109–118, 2018. [PMLR](https://proceedings.mlr.press/v80/ahn18a.html); [arXiv:1803.05104](https://arxiv.org/abs/1803.05104).

## TL;DR

Bucket renormalization combines bucket/mini-bucket elimination with tensor-network renormalization. Mini-bucket renormalization inserts local low-rank projections, while global bucket renormalization calibrates those projections using broader model information.

## Problem & setting

Exact variable elimination is exponential in induced width. Mini-bucket methods control cost by splitting buckets but discard dependencies; tensor-network renormalization suggests learned or optimized low-rank projections that retain more of the eliminated structure.

## Method

MBR sequentially inserts low-rank singular-value-based projections during elimination. GBR adds global calibration to improve those local choices. Both produce deterministic, finite-pass approximations rather than relying on convergence of iterative message passing.

## Key results

- The construction unifies ideas from graphical-model elimination and tensor-network/RG approximation.
- Local and globally calibrated variants trade computational cost for approximation quality.
- The paper reports strong empirical performance on synthetic and UAI benchmark models.

## Relevance to this research

It is a useful algorithmic comparator for hierarchical elimination/coarse-graining claims. Experiments can match computational budget and compare partition-function or marginal error against MBR/GBR, while ablations can isolate whether learned coarse maps outperform low-rank projection alone.

## Scope limits

“Renormalization” here names an approximate inference construction. The paper does not prove an exact Bayesian RG, a global recognition-law recovery kernel, or natural-gradient semiconjugacy across scales. Local SVD projections and global calibration remain approximations, and empirical accuracy is not an exact partition identity.

## Cross-links

- [[Coarse Graining]]
- [[Renormalization group flow]]
- [[Renormalization-group flow of beliefs]]
- [[Belief Propagation]]

## BibTeX

```bibtex
@inproceedings{ahn2018bucket,
  title     = {Bucket Renormalization for Approximate Inference},
  author    = {Ahn, Sungsoo and Chertkov, Michael and Weller, Adrian and Shin, Jinwoo},
  booktitle = {Proceedings of the 35th International Conference on Machine Learning},
  series    = {Proceedings of Machine Learning Research},
  volume    = {80},
  pages     = {109--118},
  year      = {2018},
  url       = {https://proceedings.mlr.press/v80/ahn18a.html},
  eprint    = {1803.05104},
  archivePrefix = {arXiv}
}
```
