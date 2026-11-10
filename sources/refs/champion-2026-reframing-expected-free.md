---
type: reference
title: "Reframing the Expected Free Energy: Four Formulations and a Unification"
aliases: ["champion2026reframing"]
authors: ["Théophile Champion", "Howard Bowman", "Dimitrije Marković", "Marek Grześ"]
year: 2026
venue: "Neural Computation"
doi: "10.1162/neco.a.1491"
arxiv: "2402.14460"
url: "https://doi.org/10.1162/neco.a.1491"
tags: [cluster/multi-agent, cluster/vfe, project/multi-agent, field/cs-ml, field/neuroscience]
created: 2026-11-10
updated: 2026-11-10
---
# Reframing the Expected Free Energy: Four Formulations and a Unification

> [!info] Citation
> Champion, T., Bowman, H., Marković, D., Grześ, M. (2026). *Reframing the Expected Free Energy: Four Formulations and a Unification*. Neural Computation, 38(3), 439-469. [DOI](https://doi.org/10.1162/neco.a.1491), [arXiv](https://arxiv.org/abs/2402.14460)

[Local PDF](../pdfs/champion-2026-reframing-expected-free.pdf), 17 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract. The local file is the first arXiv version (February 2024), which may differ from the journal version.

## TL;DR

The paper formalizes the problem of deriving the several known formulations of the expected free energy in active inference from one root definition, and analyzes two candidate root definitions. It finds that the more general one carries a constraint on which prior preferences are admissible.

## Problem & setting

Active inference selects policies by expected free energy, whose formulations (risk plus ambiguity, information gain plus pragmatic value, and others) are mostly justified by plausibility. The paper points out that the literature has no clear root definition from which the others follow, and that the symbol for prior preferences over observations also denotes the marginal likelihood.

## Method

The authors work in a partially observable Markov decision process and study two settings, one with expected free energy defined as risk over observations plus ambiguity, and one as risk over states plus ambiguity.

## Key results

In the first setting all formulations can be recovered, but only if the target likelihood equals the generative model's likelihood, and this restricts the prior preferences over observations to a limited class compatible with the likelihood mapping. In the second setting a justification of the root definition is known, but it accounts for only two formulations. The paper closes by discussing conditions under which a unification has been proposed, for systems without random fluctuations.

## Relevance to this research

The manuscript cites the paper in its open-problems section, as work distinguishing formulations of the expected free energy and their compatibility constraints. The manuscript's reading record says it was not read there, only checked against Crossref and arXiv metadata. See [[Expected Free Energy]], [[Active Inference]] and [[Free-energy principle active inference]].

## Cross-links

[[Collective agents literature map]]; [[Expected Free Energy]]; [[Active Inference]]; [[Free-energy principle active inference]].

## BibTeX

```bibtex
@article{champion2026reframing,
  author        = {Champion, Th{\'e}ophile and Bowman, Howard and Markovi{\'c}, Dimitrije and Grze{\'s}, Marek},
  title         = {Reframing the Expected Free Energy: Four Formulations and a Unification},
  journal       = {Neural Computation},
  volume        = {38},
  number        = {3},
  pages         = {439--469},
  year          = {2026},
  doi           = {10.1162/neco.a.1491},
  eprint        = {2402.14460},
  archivePrefix = {arXiv}
}
```
