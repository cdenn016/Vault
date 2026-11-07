---
type: paper
title: "Dynamic Markov Blanket Detection for Macroscopic Physics Discovery"
aliases: ["Beck and Ramstead dynamic Markov blanket detection", "Dynamic Markov blanket detection"]
authors: ["Jeff Beck", "Maxwell J. D. Ramstead"]
year: 2025
venue: "arXiv preprint"
arxiv: "2502.21217"
doi: "10.48550/arXiv.2502.21217"
url: "https://arxiv.org/abs/2502.21217v1"
version: "arXiv v1, submitted 2025-02-28"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/physics, field/statistics, field/cs-ml]
created: 2026-11-07
updated: 2026-11-07
---

# Dynamic Markov Blanket Detection for Macroscopic Physics Discovery

> [!info] Citation
> Beck, J., and Ramstead, M. J. D. (2025). *Dynamic Markov Blanket Detection for Macroscopic Physics Discovery*. [arXiv:2502.21217v1](https://arxiv.org/abs/2502.21217v1). [Primary HTML](https://arxiv.org/html/2502.21217v1). Preprint; no journal publication is asserted.

[Local v1 PDF](../pdfs/beck-2025-dynamic-markov-blanket-detection.pdf), 22 pages; retrieved November 7, 2026. The arXiv record and PDF footer date v1 to February 28, 2025; the PDF title page says March 3, 2025. Its HTML rendering displays August 24, 2026. The bibliographic year follows the version record.

## TL;DR

A structured latent-state model assigns changing internal, boundary, and environment labels to observed components.

## Problem & setting

The target is subsystem discovery from microscopic observations. Section 2.1 distinguishes conditional independence of trajectories from conditional independence in steady-state distributions.

## Method

Section 3 constrains latent dynamics and label transitions to a blanket architecture. Direct internal-to-external label changes are forbidden. The worked model combines linear continuous dynamics, switching observation maps, and discrete assignment chains. Variational Bayesian expectation maximization estimates states, labels, and parameters.

## Key results

Illustrations classify components in Newton's cradle, a burning fuse, Lorenz dynamics, and simulated biology. These demonstrate the fitted model's segmentation behavior.

## Relevance to this research

> [!note] Editorial: scope
> This is a candidate detector for [[Markov Blanket]] structure. Because the model imposes structural restrictions, its successful fit requires comparison with alternatives; labels alone do not independently establish screening-off in the generating process. The paper's general sparse-flow argument is not adopted here as a blanket theorem. Nor does detection explain why agents' [[Expected Free Energy]] policies create boundaries.

## Cross-links

[[Active inference communication and collective boundaries]]; [[Markov blanket interpretation debate]]; [[Collective active inference]].

## BibTeX

```bibtex
@misc{beck2025DynamicMarkovBlanket,
  author = {Beck, Jeff and Ramstead, Maxwell J. D.},
  title = {Dynamic Markov Blanket Detection for Macroscopic Physics Discovery},
  year = {2025},
  eprint = {2502.21217},
  archivePrefix = {arXiv},
  primaryClass = {q-bio.NC},
  doi = {10.48550/arXiv.2502.21217},
  url = {https://arxiv.org/abs/2502.21217v1},
  note = {Version 1, submitted February 28, 2025; preprint}
}
```
