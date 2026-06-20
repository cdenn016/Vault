---
type: reference
title: "The Deterministic Information Bottleneck"
aliases:
  - "Strouse & Schwab 2017"
  - "Deterministic Information Bottleneck"
authors:
  - DJ Strouse
  - David J. Schwab
year: 2017
arxiv: "1604.00268"
url: https://arxiv.org/abs/1604.00268
tags:
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/statistics
created: 2026-06-19
updated: 2026-06-19
---

# The Deterministic Information Bottleneck

> [!info] Citation
> DJ Strouse and David J. Schwab (2017). "The Deterministic Information Bottleneck." *Neural Computation* 29(6): 1611–1630. arXiv:1604.00268. <https://arxiv.org/abs/1604.00268>

## TL;DR

The deterministic information bottleneck (DIB) replaces the compression cost $I(X;T)$ in the [[Information bottleneck]] with the **entropy $H(T)$** of the representation. Because penalizing $H(T)$ rewards using fewer distinct codes rather than merely noisier ones, the optimal DIB encoder is a **hard (deterministic) clustering** $t = f(x)$, not the soft stochastic assignment of the original IB. The result is a sharper, more interpretable compression that directly minimizes representational description length.

## What it establishes

- The DIB objective $\min\, H(T) - \beta\,I(T;Y)$ and its self-consistent solution, which collapses to a deterministic encoder.
- An iterative algorithm yielding hard clusterings, contrasted against the soft IB assignment of [[tishby-1999-information-bottleneck]].
- A principled link between bottleneck compression and minimum-description-length coding.

## Why the project cites it

The DIB is the **hard-assignment** end of the IB spectrum, and PIFB ([[participatory-it-from-bit]]) lives on that spectrum. The project's attention weights and coarse-graining can run from soft (high-temperature, diffuse coupling) to hard (low-temperature, near-deterministic source selection), governed by $\tau = \kappa\sqrt{K}$. The DIB names the deterministic limit and shows what objective it optimizes — entropy-of-code rather than mutual-information compression — which clarifies what the project's low-temperature attention and crisp meta-agent membership are minimizing. The hard-clustering optimum is also the cleanest analogue of crisp [[Meta-agents and hierarchical emergence]] formation: assigning each constituent agent to exactly one meta-agent is a deterministic bottleneck on the population, and the DIB supplies the variational account of when that hard assignment is optimal. It complements the soft IB ([[tishby-1999-information-bottleneck]]) and the agglomerative coarse-graining cousin ([[slonim-2000-agglomerative-ib]]).

```bibtex
@article{strouse2017deterministic,
  title         = {The Deterministic Information Bottleneck},
  author        = {Strouse, DJ and Schwab, David J.},
  journal       = {Neural Computation},
  volume        = {29},
  number        = {6},
  pages         = {1611--1630},
  year          = {2017},
  eprint        = {1604.00268},
  archivePrefix = {arXiv},
  primaryClass  = {cs.IT},
  url           = {https://arxiv.org/abs/1604.00268}
}
```
