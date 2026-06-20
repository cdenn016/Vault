---
type: reference
title: "Training Compute-Optimal Large Language Models (Chinchilla)"
aliases:
  - "Hoffmann et al. 2022"
  - "Chinchilla"
authors:
  - Jordan Hoffmann
  - Sebastian Borgeaud
  - Arthur Mensch
  - Elena Buchatskaya
  - Trevor Cai
  - Eliza Rutherford
  - Diego de Las Casas
  - Lisa Anne Hendricks
  - Johannes Welbl
  - Aidan Clark
  - Tom Hennigan
  - Eric Noland
  - Katie Millican
  - George van den Driessche
  - Bogdan Damoc
  - Aurelia Guy
  - Simon Osindero
  - Karen Simonyan
  - Erich Elsen
  - Jack W. Rae
  - Oriol Vinyals
  - Laurent Sifre
year: 2022
arxiv: "2203.15556"
url: https://arxiv.org/abs/2203.15556
tags:
  - cluster/methodology
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - field/cs-ml
created: 2026-06-19
updated: 2026-06-19
---

# Training Compute-Optimal Large Language Models (Chinchilla)

> [!info] Citation
> Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, et al. (2022). "Training Compute-Optimal Large Language Models." NeurIPS 2022. arXiv:2203.15556. <https://arxiv.org/abs/2203.15556>

## TL;DR

Chinchilla **revises** the compute-optimal scaling prescription of [[kaplan-2020-scaling-laws|Kaplan et al.]]: for a fixed training-compute budget, model size $N$ and training-token count $D$ should be scaled in roughly **equal proportion** — earlier large models were badly under-trained on too little data. The authors fit a parametric loss law $L(N, D) = E + A/N^{\alpha} + B/D^{\beta}$, find $\alpha \approx \beta \approx 0.5$, and validate it by training Chinchilla (70B parameters on ~1.4T tokens), which outperforms the 4x-larger Gopher under matched compute.

## What it establishes

- A loss surface $L(N,D) = E + A N^{-\alpha} + B D^{-\beta}$ with an **irreducible term $E$** (the entropy of natural text) plus separate finite-size penalties in parameters and data.
- Compute-optimal training requires $N$ and $D$ to grow together (roughly $D \propto N$), correcting Kaplan's bias toward huge under-trained models.
- Empirical confirmation: a smaller, better-fed model beats a larger one at equal compute.

## Why the project cites it

Chinchilla is PIFB's ([[participatory-it-from-bit]]) **named comparison anchor** for its inverse-$K$ scaling claim. PIFB predicts how the attainable free-energy floor falls as the belief dimension $K$ grows, and it frames this against the Chinchilla loss law: the parametric form $L = E + A N^{-\alpha} + \dots$ is the template PIFB recapitulates with capacity = belief dimension $K$ in place of parameter count $N$. The **irreducible term $E$** is especially load-bearing for the manuscript: it is the empirical signature of a capacity-independent floor, which PIFB interprets through its [[Information bottleneck]] reading as the residual free energy that no amount of compression budget can remove — the entropy of the data conditional on the best representation. Citing Chinchilla rather than Kaplan reflects that PIFB is matching the corrected, two-resource law with an explicit floor term; the founding form of the genre is recorded separately in [[kaplan-2020-scaling-laws]], and both sit under [[Neural scaling laws]].

```bibtex
@inproceedings{hoffmann2022training,
  title         = {Training Compute-Optimal Large Language Models},
  author        = {Hoffmann, Jordan and Borgeaud, Sebastian and Mensch, Arthur and
                   Buchatskaya, Elena and Cai, Trevor and Rutherford, Eliza and
                   de Las Casas, Diego and Hendricks, Lisa Anne and Welbl, Johannes and
                   Clark, Aidan and Hennigan, Tom and Noland, Eric and Millican, Katie and
                   van den Driessche, George and Damoc, Bogdan and Guy, Aurelia and
                   Osindero, Simon and Simonyan, Karen and Elsen, Erich and
                   Rae, Jack W. and Vinyals, Oriol and Sifre, Laurent},
  booktitle     = {Advances in Neural Information Processing Systems 35 (NeurIPS)},
  year          = {2022},
  eprint        = {2203.15556},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL},
  url           = {https://arxiv.org/abs/2203.15556}
}
```
