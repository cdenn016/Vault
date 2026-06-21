---
type: paper
title: "Attention Is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth"
aliases:
  - "Dong et al. 2021"
  - "Dong (2021) Rank Collapse"
authors:
  - Yihe Dong
  - Jean-Baptiste Cordonnier
  - Andreas Loukas
year: 2021
arxiv: "2103.03404"
url: https://arxiv.org/abs/2103.03404
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/mathematics
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# Attention Is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth

> [!info] Citation
> Yihe Dong, Jean-Baptiste Cordonnier, and Andreas Loukas (2021). "Attention Is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth." ICML 2021. arXiv:2103.03404. <https://arxiv.org/abs/2103.03404>

## TL;DR

This paper proves that a transformer built from **self-attention alone** — no skip connections, no feed-forward layers — degenerates: its output converges **doubly exponentially in depth** to a rank-1 matrix, meaning every token row becomes the same vector. The pathology is **token uniformity** (also called over-smoothing or rank collapse). Skip connections and the per-token MLP are precisely what counteract it; they are not incidental but load-bearing. The paper thereby identifies the failure mode that any all-attention or attention-as-consensus architecture must defend against.

## Problem & setting

The authors ask what self-attention does on its own, stripped of the other transformer components. They define a "residual" measuring distance from the rank-1 (constant-across-tokens) subspace and track it through depth in a network of stacked pure-attention blocks.

## Method

A path-decomposition of the network expresses the output as a sum over compositions of attention heads; bounding the residual along each path shows multiplicative contraction toward rank-1 at every layer. The contraction compounds super-exponentially because each layer's attention matrix is itself a stochastic (row-normalized) operator. They then re-introduce skip connections and MLP nonlinearities and show these arrest the collapse.

## Key results

- Pure stacked self-attention converges to rank-1 at a **doubly exponential** rate in depth; the token representations become indistinguishable.
- **Skip connections** are the dominant counterforce — removing them is catastrophic — while the per-token MLP and multiple heads also slow the collapse.
- The analysis gives a principled account of over-smoothing in deep attention stacks and a diagnostic (the rank-1 residual) for it.

## Relevance to this research

This result is the mechanistic explanation for why PIFB ([[participatory-it-from-bit]]) **needs its entropy regularizer**. PIFB reads stacked attention as iterated belief consensus; left unchecked, consensus dynamics drive every agent to the same belief — the "heat death" the manuscript warns of, which is exactly Dong et al.'s rank-1 collapse expressed in belief coordinates. The attention-entropy term $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ in the [[Variational free energy]] functional is the project's structural defense: it keeps the coupling distribution from sharpening into a degenerate consensus, the same role skip connections and MLPs play here. This connects directly to the consensus-collapse limit proved analytically in [[geshkovski-2023-mathematical-transformers]] (their single-cluster limit is this rank-1 state) and motivates the metastable, multi-cluster regime PIFB actually wants for [[Meta-agents and hierarchical emergence]]. Because PIFB observes the no-neural-network constraint — no MLP, only a linear decode — it cannot lean on the per-token feed-forward layer that Dong et al. identify as a secondary brake; the entropy term and the gauge transport $\Omega_{ij}$ (which makes the consensus target token-dependent rather than a single global mean) have to do that work instead. The paper is the empirical/theoretical foil establishing that an entropy-free $\sum\beta\,\mathrm{KL}$ surrogate would collapse.

## Cross-links

- Concepts: [[Variational free energy]], [[Meta-agents and hierarchical emergence]], [[Attention mechanisms — theory and positional structure]]
- Sources: [[geshkovski-2023-mathematical-transformers]], [[vaswani-2017-attention]], [[ramsauer2021hopfield|ramsauer-2021-hopfield]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@inproceedings{dong2021attention,
  title         = {Attention Is Not All You Need: Pure Attention Loses Rank
                   Doubly Exponentially with Depth},
  author        = {Dong, Yihe and Cordonnier, Jean-Baptiste and Loukas, Andreas},
  booktitle     = {Proceedings of the 38th International Conference on Machine Learning (ICML)},
  year          = {2021},
  eprint        = {2103.03404},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2103.03404}
}
```
