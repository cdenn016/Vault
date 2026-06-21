---
type: paper
title: "Learning and Relearning in Boltzmann Machines"
aliases:
  - "hinton-sejnowski-1986-boltzmann"
  - "hintonsejnowski1986boltzmann"
  - "Hinton & Sejnowski 1986"
authors:
  - "Hinton, Geoffrey E."
  - "Sejnowski, Terrence J."
year: 1986
url: https://dl.acm.org/doi/10.5555/104279.104291
venue: "Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1, MIT Press"
tags:
  - cluster/vfe
  - project/transformer
  - field/cs-ml
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Learning and Relearning in Boltzmann Machines

> [!info] Citation
> Hinton, Geoffrey E., Sejnowski, Terrence J. (1986). "Learning and Relearning in Boltzmann Machines." Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Vol. 1, MIT Press. https://dl.acm.org/doi/10.5555/104279.104291

## TL;DR
Introduces the Boltzmann machine, a stochastic energy-based neural network whose units settle to a Boltzmann distribution. Learning uses a contrastive two-phase (wake/sleep, positive/negative) procedure that adjusts weights to match clamped and free-running statistics, minimizing a KL divergence between data and model distributions.

## Relevance to this research
An energy-based, contrastive learning rule that is a conceptual ancestor of variational free-energy minimization and of Hinton's forward-forward algorithm; its positive/negative phase structure parallels the local goodness contrast used in the program's biologically plausible learning discussions.

## Cross-links
[[hinton-2022-forward-forward]]

## BibTeX
```bibtex
@incollection{hinton-sejnowski-1986-boltzmann,
  title={Learning and Relearning in Boltzmann Machines},
  author={Hinton, Geoffrey E. and Sejnowski, Terrence J.},
  booktitle={Parallel Distributed Processing: Explorations in the Microstructure of Cognition, Volume 1: Foundations},
  editor={Rumelhart, David E. and McClelland, James L.},
  pages={282--317},
  publisher={MIT Press},
  year={1986}
}
```
