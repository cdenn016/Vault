---
type: reference
title: "Path integrals, particular kinds, and strange things"
aliases: ["friston2023path"]
authors: ["Karl Friston", "Lancelot Da Costa", "Dalton A. R. Sakthivadivel", "Conor Heins", "Grigorios A. Pavliotis", "Maxwell Ramstead", "Thomas Parr"]
year: 2023
venue: "Physics of Life Reviews"
doi: "10.1016/j.plrev.2023.08.016"
arxiv: "2210.12761"
url: "https://doi.org/10.1016/j.plrev.2023.08.016"
tags: [cluster/vfe, cluster/multi-agent, project/multi-agent, field/physics, field/neuroscience, field/mathematics]
created: 2026-11-10
updated: 2026-11-10
---
# Path integrals, particular kinds, and strange things

> [!info] Citation
> Friston, K., Da Costa, L., Sakthivadivel, D. A. R., Heins, C., Pavliotis, G. A., Ramstead, M., Parr, T. (2023). *Path integrals, particular kinds, and strange things*. Physics of Life Reviews, 47, 35-62. [DOI](https://doi.org/10.1016/j.plrev.2023.08.016), [arXiv](https://arxiv.org/abs/2210.12761)

[Local PDF](../pdfs/friston-2023-path-integrals-particular.pdf), 40 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and manuscript reading record.

## TL;DR

The paper gives a path-integral formulation of the free energy principle, with densities over paths instead of states. Particles are defined by a partition into internal, external, active and sensory states, and the paper sorts particles into kinds: dissipative or conservative, inert or active, ordinary or strange.

## Problem & setting

The introduction positions the paper as one of a series restating the free energy principle in progressively simpler terms. It states that, unlike state-based formulations, the path formulation makes no assumption about the existence and functional form of a nonequilibrium steady state. The partition is defined by sparse coupling among external, sensory, active and internal states.

## Method

The dynamics of a random dynamical system are encoded by a Lagrangian that scores the implausibility of a path, and the work uses generalized coordinates of motion so that a path becomes a point. A variational free energy lemma states that the most likely autonomous paths minimize a free energy functional of beliefs about external paths. For active particles the Lagrangian of autonomous paths is the expected free energy, split into expected cost and expected information gain.

## Key results

The main results, as the abstract and introduction state them, are a principle of least action for particles in open exchange with their surroundings and a typology of particular kinds. Strange particles, whose active states do not influence internal states, are described as inferring their own actions.

## Relevance to this research

The manuscript cites this paper for its notion of paths and for the statement that internal and external paths are conditionally independent given blanket paths, obtained for flows that respect sparse coupling and independent fluctuations. According to the manuscript's reading record, the arXiv version was opened to check that statement, and its text does not mention conditioning on initial states; that conditioning comes from a later paper, and the published version was not opened. The paper also appears among the positive results that hold under stated hypotheses in the dispute on which independence a blanket means. See [[Markov Blanket]], [[Markov blanket interpretation debate]], [[Bayesian mechanics]] and [[Free-energy principle active inference]].

## Cross-links

[[Collective agents literature map]]; [[Markov Blanket]]; [[Markov blanket interpretation debate]]; [[Bayesian mechanics]]; [[Free-energy principle active inference]]; related notes: friston-2021-stochastic-chaos-markov, friston-2022-very-particular-comment.

## BibTeX

```bibtex
@article{friston2023path,
  author        = {Friston, Karl and Da Costa, Lancelot and Sakthivadivel, Dalton A. R. and Heins, Conor and Pavliotis, Grigorios A. and Ramstead, Maxwell and Parr, Thomas},
  title         = {Path integrals, particular kinds, and strange things},
  journal       = {Physics of Life Reviews},
  volume        = {47},
  pages         = {35--62},
  year          = {2023},
  doi           = {10.1016/j.plrev.2023.08.016},
  eprint        = {2210.12761},
  archivePrefix = {arXiv}
}
```
