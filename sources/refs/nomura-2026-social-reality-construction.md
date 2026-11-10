---
type: reference
title: "Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity"
aliases: ["nomura2026social"]
authors: ["Kentaro Nomura", "Takato Horii"]
year: 2026
venue: "ALIFE 2026: Proceedings of the 2026 Artificial Life Conference"
doi: "10.1162/isal.a.1009"
arxiv: "2604.09026"
url: "https://doi.org/10.1162/isal.a.1009"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/cs-ml, field/sociology]
created: 2026-11-10
updated: 2026-11-10
---
# Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity

> [!info] Citation
> Nomura, K., Horii, T. (2026). *Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity*. ALIFE 2026: Proceedings of the 2026 Artificial Life Conference, 83. MIT Press. [DOI](https://doi.org/10.1162/isal.a.1009); [arXiv](https://arxiv.org/abs/2604.09026)

[Local PDF](../pdfs/nomura-2026-social-reality-construction.pdf), 9 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper proposes a multi-agent simulation model, grounded in active inference and run on a structured social network, in which agents form social priors by communicating with neighbors and also create new observations that others may adopt.

## Problem & setting

The introduction poses the problem of how bottom-up creative formation and top-down social regulation together produce norms that are stable yet evolving. It contrasts existing artificial-life models of convention formation, such as naming games and iterated learning, which treat agents as rule followers without internal generative models, with active-inference accounts of collective behavior, communication and norm acquisition, which address spatial coordination or internalization of existing expectations but not the feedback of agents' own creations. It links the gap to the missing bottom-up direction in niche construction theory.

## Method

Each agent holds an internal generative model, communicates with neighbors to form social priors, creates novel observations, and selectively incorporates others' creations into memory.

## Key results

From the abstract, in simulation: informationally cohesive groups emerge, with representational alignment following the network's cluster topology; social representations and the observation distribution constitute each other in a circular way through agents' creative acts; and creations propagate selectively and heterogeneously, unlike the stable diffusion of social representations. These are simulation findings reported by the authors.

## Relevance to this research

The manuscript cites this paper in its open-problems discussion as a model of the reciprocal development of social priors and environmental structure, next to work on mutual learning between individuals and an organizational code. In related work it lists the paper among those it has not read and asks whether the paper anticipates any part of the manuscript's combination of results. The manuscript's reading record confirms bibliographic data only. See [[Active Inference]], [[Collective active inference]], [[Niche Construction]] and [[Active inference communication and collective boundaries]].

## Cross-links

[[Collective agents literature map]]; [[Active Inference]]; [[Collective active inference]]; [[Niche Construction]]; [[Active inference communication and collective boundaries]].

## BibTeX

```bibtex
@inproceedings{nomura2026social,
  author        = {Nomura, Kentaro and Horii, Takato},
  title         = {Social Reality Construction via Active Inference: Modeling the Dialectic of Conformity and Creativity},
  booktitle     = {{ALIFE} 2026: Proceedings of the 2026 Artificial Life Conference},
  pages         = {83},
  publisher     = {MIT Press},
  address       = {Waterloo, Ontario, Canada and Online},
  year          = {2026},
  doi           = {10.1162/isal.a.1009},
  eprint        = {2604.09026},
  archivePrefix = {arXiv}
}
```
