---
type: reference
title: "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned"
aliases:
  - "Voita et al. 2019"
  - "Voita (2019) Multi-Head Attention"
authors:
  - Elena Voita
  - David Talbot
  - Fedor Moiseev
  - Rico Sennrich
  - Ivan Titov
year: 2019
arxiv: "1905.09418"
url: https://arxiv.org/abs/1905.09418
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Analyzing Multi-Head Self-Attention

> [!info] Citation
> Elena Voita, David Talbot, Fedor Moiseev, Rico Sennrich, and Ivan Titov (2019). "Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned." ACL 2019. arXiv:1905.09418. <https://arxiv.org/abs/1905.09418>

## TL;DR

This paper shows that the heads of a multi-head transformer are **not interchangeable**: a small subset of heads do interpretable, specialized jobs — positional heads (attend to the adjacent token), syntactic heads (attend along specific dependency relations), and rare-token heads — while the majority are redundant and can be pruned with little loss. Using a differentiable $L_0$-style gate, the authors prune most heads and confirm that the survivors are the specialized ones.

## What it establishes

- A taxonomy of head roles: positional, syntactic (relation-specific), and rare-token heads carry most of the function.
- Most heads are prunable; performance is concentrated in a specialized minority.
- A differentiable head-gating method that both prunes and identifies the important heads.

## Why the project cites it

Head specialization is the empirical phenomenon a principled attention theory must explain, and PIFB ([[participatory-it-from-bit]]) cites Voita et al. as evidence on what attention heads actually do. The finding that some heads are **positional** (fixed-offset attention) and others **syntactic** (relation-specific) maps onto PIFB's decomposition of the coupling: positional heads are the abelian gauge-frame / distance-prior part (the RoPE and ALiBi mechanisms of [[su-2021-roformer-rope]] and [[press-2021-alibi]]), while relation-specific heads are the content-driven KL coupling between beliefs. That a specialized minority "does the heavy lifting" while the rest are redundant is congenial to the project's low-dimensional, no-extra-parameters stance — capacity concentrated in a few meaningful coupling channels rather than spread across many learned projections. This grounds the head-role reading under [[Mechanistic interpretability of attention]] and connects to the source-attribution interpretation of $\beta_{ij}$ tested by induction heads ([[olsson-2022-induction-heads]]) and BERT-attention analysis ([[clark-2019-bert-attention]]).

```bibtex
@inproceedings{voita2019analyzing,
  title         = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the
                   Heavy Lifting, the Rest Can Be Pruned},
  author        = {Voita, Elena and Talbot, David and Moiseev, Fedor and
                   Sennrich, Rico and Titov, Ivan},
  booktitle     = {Proceedings of the 57th Annual Meeting of the Association for
                   Computational Linguistics (ACL)},
  year          = {2019},
  eprint        = {1905.09418},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/1905.09418}
}
```
