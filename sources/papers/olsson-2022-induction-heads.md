---
type: paper
title: "In-Context Learning and Induction Heads"
aliases:
  - "Olsson et al. 2022"
  - "Olsson (2022) Induction Heads"
authors:
  - Catherine Olsson
  - Nelson Elhage
  - Neel Nanda
  - Nicholas Joseph
  - Nova DasSarma
  - Tom Henighan
  - Ben Mann
  - Amanda Askell
  - Yuntao Bai
  - Anna Chen
  - Tom Conerly
  - Dawn Drain
  - Deep Ganguli
  - Zac Hatfield-Dodds
  - Danny Hernandez
  - Scott Johnston
  - Andy Jones
  - Jackson Kernion
  - Liane Lovitt
  - Kamal Ndousse
  - Dario Amodei
  - Tom Brown
  - Jack Clark
  - Jared Kaplan
  - Sam McCandlish
  - Chris Olah
year: 2022
arxiv: "2209.11895"
url: https://arxiv.org/abs/2209.11895
tags:
  - cluster/attention
  - project/transformer
  - project/multi-agent
  - field/cs-ml
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# In-Context Learning and Induction Heads

> [!info] Citation
> Catherine Olsson, Nelson Elhage, Neel Nanda, Nicholas Joseph, Nova DasSarma, et al. (2022). "In-Context Learning and Induction Heads." Anthropic / Transformer Circuits. arXiv:2209.11895. <https://arxiv.org/abs/2209.11895>

## TL;DR

This paper identifies **induction heads** — attention heads that implement the pattern "find an earlier occurrence of the current token, then attend to and copy whatever came next" — and argues they are the principal mechanism behind in-context learning in transformers. The emergence of induction heads coincides with a sharp phase-change bump in in-context-learning ability during training, and ablating them removes much of that ability. It is a flagship piece of mechanistic interpretability: a concrete, circuit-level account of *which heads attend to what and why*.

## Problem & setting

In-context learning improves abruptly during training; the authors seek the mechanistic cause by reverse-engineering specific attention circuits in small-to-medium transformers and correlating their formation with the macroscopic learning curve.

## Method

Circuit analysis (attention-pattern inspection, the QK/OV decomposition of the transformer-circuits framework), causal ablations of candidate heads, and tracking the formation of induction heads against the in-context-learning phase change across model scales.

## Key results

- Induction heads perform prefix-matching-and-copying via a two-head composition, and they form at a distinct point in training that aligns with the in-context-learning bump.
- Ablating induction heads substantially degrades in-context learning, supporting a causal role.
- The mechanism generalizes beyond literal token copying toward fuzzier pattern completion, offering a partial mechanistic story for in-context learning at scale.

## Relevance to this research

PIFB ([[participatory-it-from-bit]]) reads the attention weight $\beta_{ij}$ as a **source-attribution** quantity — how much agent $i$'s belief is sourced from agent $j$ — a mixture-of-sources interpretation of attention. Induction heads are the sharpest empirical foil for that reading: they are a documented case where $\beta_{ij}$ provably routes information from a specific earlier source (the prior occurrence) to the present token, exactly the "belief $i$ draws on source $j$" semantics PIFB wants attention to carry. They also test the limits of the reading, since their function is copy-and-complete rather than belief-averaging consensus, so they pose the question of whether the PIFB coupling term can express directed copy circuits or only diffusive consensus. This connects to [[Mechanistic interpretability of attention]] and to the head-specialization literature ([[voita-2019-attention-heads|voita-2019-multihead]], [[clark-2019-bert-attention]]); together these works supply the interpretability frame against which PIFB's source-attribution claim about $\beta_{ij}$ must be checked.

## Cross-links

- Concepts: [[Mechanistic interpretability of attention]], [[Attention mechanisms — theory and positional structure]]
- Sources: [[voita-2019-attention-heads|voita-2019-multihead]], [[clark-2019-bert-attention]], [[vaswani-2017-attention]]
- Project: [[participatory-it-from-bit]], [[Gauge-Theoretic Multi-Agent VFE Model]]

```bibtex
@article{olsson2022incontext,
  title         = {In-Context Learning and Induction Heads},
  author        = {Olsson, Catherine and Elhage, Nelson and Nanda, Neel and
                   Joseph, Nicholas and DasSarma, Nova and Henighan, Tom and
                   Mann, Ben and Askell, Amanda and Bai, Yuntao and Chen, Anna and
                   Conerly, Tom and Drain, Dawn and Ganguli, Deep and
                   Hatfield-Dodds, Zac and Hernandez, Danny and Johnston, Scott and
                   Jones, Andy and Kernion, Jackson and Lovitt, Liane and
                   Ndousse, Kamal and Amodei, Dario and Brown, Tom and
                   Clark, Jack and Kaplan, Jared and McCandlish, Sam and Olah, Chris},
  journal       = {arXiv preprint arXiv:2209.11895},
  year          = {2022},
  eprint        = {2209.11895},
  archivePrefix = {arXiv},
  primaryClass  = {cs.LG},
  url           = {https://arxiv.org/abs/2209.11895}
}
```
