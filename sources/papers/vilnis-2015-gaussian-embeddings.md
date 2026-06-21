---
type: paper
title: "Word Representations via Gaussian Embedding"
aliases:
  - "vilnis-2015-gaussian-embeddings"
  - "vilnis2015gaussianembeddings"
  - "Vilnis 2015"
  - "Gaussian embeddings"
authors:
  - "Vilnis, Luke"
  - "McCallum, Andrew"
year: 2015
url: https://arxiv.org/abs/1412.6623
venue: "International Conference on Learning Representations (ICLR)"
tags:
  - cluster/info-geometry
  - cluster/cs-ml
  - project/transformer
  - field/cs-ml
  - field/statistics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Word Representations via Gaussian Embedding

> [!info] Citation
> Vilnis, Luke, McCallum, Andrew (2015). "Word Representations via Gaussian Embedding." International Conference on Learning Representations (ICLR). https://arxiv.org/abs/1412.6623

## TL;DR
Represents words as Gaussian densities (mean and covariance) rather than point vectors, so that each embedding carries an explicit notion of uncertainty and supports asymmetric, entailment-like comparisons via KL divergence between distributions. Trained with energy-based ranking objectives, the covariance captures specificity/breadth of word meaning.

## Relevance to this research
A direct precursor to the VFE program's representation of tokens/beliefs as Gaussians (mu, Sigma) with KL-based comparison; grounds the use of distribution-valued embeddings and SPD covariance geometry in attention/belief computation.

## Cross-links
[[SPD-manifold geometry and Riemannian optimization]], [[Variational Free Energy]]

## BibTeX
```bibtex
@inproceedings{vilnis2015gaussianembeddings,
  author    = {Vilnis, Luke and McCallum, Andrew},
  title     = {Word Representations via {Gaussian} Embedding},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2015},
  eprint    = {1412.6623},
  archivePrefix = {arXiv}
}
```
