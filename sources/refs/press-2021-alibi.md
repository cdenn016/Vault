---
type: reference
title: "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation"
aliases:
  - "Press et al. 2021"
  - "Press (2021) ALiBi"
authors:
  - Ofir Press
  - Noah A. Smith
  - Mike Lewis
year: 2021
arxiv: "2108.12409"
url: https://arxiv.org/abs/2108.12409
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation

> [!info] Citation
> Ofir Press, Noah A. Smith, and Mike Lewis (2021). "Train Short, Test Long: Attention with Linear Biases Enables Input Length Extrapolation." ICLR 2022. arXiv:2108.12409. <https://arxiv.org/abs/2108.12409>

## TL;DR

ALiBi (Attention with Linear Biases) removes positional embeddings entirely and instead adds, to each query-key attention score, a **bias that is linear in the distance** between the two positions: score $\to$ score $- m\,|i-j|$, with a fixed per-head slope $m$. This is a static, learning-free recency prior — nearer tokens are favored, distant ones penalized in proportion to distance — and it lets a model trained on short sequences extrapolate to much longer ones at inference, where learned absolute embeddings fail.

## What it establishes

- A simple distance-proportional penalty on attention logits, with geometrically spaced per-head slopes, replaces positional embeddings.
- Trained on length $L$, ALiBi models retain low perplexity at lengths well beyond $L$, solving the length-extrapolation problem cheaply.
- The bias is a fixed monotone-in-distance prior; no parameters are added and inference cost is unchanged.

## Why the project cites it

PIFB ([[participatory-it-from-bit]]) **derives ALiBi** as a consequence of its entropy-regularized consensus prior rather than treating it as an engineering trick. In the [[Variational free energy]] functional, the attention term carries an entropy regularizer $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ with a prior coupling $\pi_{ij}$ over which sources agent $i$ may attend to. If that prior is taken to decay with distance — a recency prior on belief coupling — then minimizing the entropy-regularized objective shifts each attention logit by $\log\pi_{ij}$, and a log-prior linear in distance is exactly ALiBi's additive linear bias. The per-head slope $m$ is then read as the strength of the distance prior, and the temperature $\tau = \kappa\sqrt{K}$ sets its scale. ALiBi is thus cited as the empirically successful positional scheme that falls out of the project's consensus-with-entropy construction, complementing the multiplicative gauge-frame reading of RoPE ([[su-2021-roformer-rope]]) with an additive log-prior reading; both are organized under [[Attention mechanisms — theory and positional structure]].

```bibtex
@inproceedings{press2022train,
  title         = {Train Short, Test Long: Attention with Linear Biases Enables
                   Input Length Extrapolation},
  author        = {Press, Ofir and Smith, Noah A. and Lewis, Mike},
  booktitle     = {10th International Conference on Learning Representations (ICLR)},
  year          = {2022},
  eprint        = {2108.12409},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2108.12409}
}
```
