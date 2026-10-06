---
type: paper
title: "Sheaf Attention Networks"
aliases:
  - "SheafAN"
  - "SheafANs"
  - "Barbero 2022 sheaf attention"
authors:
  - Federico Barbero
  - Cristian Bodnar
  - Haitz Sáez de Ocáriz Borde
  - Pietro Liò
year: 2022
url: https://neurips.cc/virtual/2022/60823
tags:
  - cluster/gauge-theory
  - cluster/attention
  - project/transformer
  - field/cs-ml
  - field/mathematics
created: 2026-10-06
---

# Sheaf Attention Networks

> [!info] Citation
> Barbero, F., Bodnar, C., Sáez de Ocáriz Borde, H., and Liò, P. (2022). *Sheaf Attention Networks.* Poster in the NeurIPS 2022 Workshop on Symmetry and Geometry in Neural Representations (NeurReps). Record: [neurips.cc/virtual/2022/60823](https://neurips.cc/virtual/2022/60823); OpenReview forum `LIDvgVjpkZr` ([link](https://openreview.net/forum?id=LIDvgVjpkZr)). No arXiv version was found.

> [!warning] Read status: abstract only
> The workshop PDF is hosted on OpenReview, which answered automated requests with an access challenge, so the full text was not downloaded or read; no PDF is stored in `sources/pdfs/`. Everything below is the public workshop abstract. Drop the PDF into `sources/pdfs/` as `Barbero2022SheafAttention.pdf` to upgrade this note.

## TL;DR

The abstract argues that Graph Attention Networks suffer the same pathologies as other graph neural networks, feature smoothing as layers stack and poor performance on heterophilic graphs, and that sheaf neural networks address both. The authors propose Sheaf Attention Networks (SheafANs), built on "a novel and more expressive attention mechanism equipped with geometric inductive biases," which they say generalizes popular attention-based graph networks to cellular sheaves. They report that SheafANs help with oversmoothing and heterophily and consistently outperform GAT on synthetic and real-world benchmarks.

## What the abstract does not say

It does not say how attention scores are formed (whether they depend on the restriction maps), whether the restriction maps are learned or precomputed, their group (orthogonal or general linear), or the benchmark sizes. None of these can be asserted from the abstract.

## Relevance to this research

This is the only item in the vault that combines attention weights with cellular-sheaf structure, so it is the nearest precedent for reading the GL(K) comparison cospan $E_i\to H^{\mathrm{cmp}}\leftarrow E_j$ of [[dennis-2026-glk-attention-v2-rework-2026-10-05]] as sheaf data attached to an attention mechanism. It is a graph-attention network on graphs with feature vectors, evaluated on node classification; nothing in the abstract concerns language models, probabilistic fibers, divergence-based routing, or gauge groups. Whether its attention mechanism already contains the per-edge linear transport of the GL(K) construction needs the full text.

Wiki pages: [[GL(K) gauge-equivariant attention]], [[Gauge equivariance and geometric deep learning]], [[Graph synchronization and connection Laplacians]].

## Cross-links

- Related sources: [[barbero-2022-sheaf-neural-networks-connection-laplacians]], [[bodnar-2022-neural-sheaf-diffusion]], [[hansen-2018-toward-a-spectral-theory-of-cellular-sheaves]]
- Concepts: [[Attention Mechanism]], [[Multi-head attention]]

## BibTeX

```bibtex
@inproceedings{Barbero2022SheafAttention,
  author    = {Barbero, Federico and Bodnar, Cristian and S{\'a}ez de Oc{\'a}riz Borde, Haitz and Li{\`o}, Pietro},
  title     = {Sheaf Attention Networks},
  booktitle = {NeurIPS 2022 Workshop on Symmetry and Geometry in Neural Representations},
  year      = {2022},
  url       = {https://openreview.net/forum?id=LIDvgVjpkZr}
}
```
