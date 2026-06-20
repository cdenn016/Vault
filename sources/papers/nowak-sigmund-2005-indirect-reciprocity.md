---
type: paper
title: "Evolution of Indirect Reciprocity"
aliases: ["Nowak & Sigmund 2005", "Reputation and indirect reciprocity"]
authors: ["Nowak M. A.", "Sigmund K."]
year: 2005
url: https://doi.org/10.1038/nature04131
tags: [cluster/social-physics, project/social-physics, field/biology, field/economics, cluster/social-physics/evolutionary-and-cultural]
created: 2026-06-19
updated: 2026-06-19
---

# Evolution of Indirect Reciprocity

> [!info] Citation
> Nowak, M. A., & Sigmund, K. (2005). *Evolution of Indirect Reciprocity*. Nature 437(7063):1291–1298. DOI: [10.1038/nature04131](https://doi.org/10.1038/nature04131).

## TL;DR
This review surveys indirect reciprocity, the mechanism by which cooperation is sustained among unrelated individuals who may never meet again, through reputation. Unlike direct reciprocity (helping those who helped you), indirect reciprocity rests on "I help you, someone else helps me": an agent's propensity to receive help depends on its reputation, built from observed past behavior toward third parties. The authors review image-scoring and standing/assessment models, the conditions under which reputation-tracking strategies are evolutionarily stable, and the resulting selection pressure for the cognitive and linguistic capacities to acquire, store, and communicate reputational information — connecting indirect reciprocity to the evolution of moral judgment and social norms.

## What it establishes
The canonical analytic result is that indirect reciprocity can favor cooperation when the probability $q$ of knowing a recipient's reputation exceeds the cost-to-benefit ratio of the cooperative act,
$$q > \frac{c}{b},$$
a reputation-based analogue of Hamilton's rule and the discounted-future condition of direct reciprocity. The review distinguishes first-order assessment (judging by the last action) from higher-order assessment (judging in light of the recipient's own reputation), showing that more sophisticated norms ("leading eight" strategies) are needed for stability against defectors who exploit naive image scoring. Reputation, not relatedness or repeated pairing, becomes the carrier of cooperative incentive.

## Relevance to this research
Reputation-based cooperation introduces belief-about-others — image and reputation as the state driving social behavior — which is conceptually adjacent to the program's representation of agents by belief distributions over a shared space. The connection is honest but loose: the program's beliefs are Gaussian tuples $(\mu, \Sigma, \phi)$ updated by VFE minimization with gauge transport, whereas reputation here is a scalar score updated by behavioral observation, and there is no information-geometric or gauge structure. It is an adjacent reference that rounds out the cooperation-mechanism neighborhood (it is one of Nowak's five rules) rather than machinery the belief-inertia functional uses. See [[Evolutionary game theory and cooperation]], [[Collective active inference]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Evolutionary game theory and cooperation]]
- Related sources: [[nowak-2006-five-rules-cooperation]], [[axelrod-hamilton-1981-evolution-of-cooperation]], [[perc-jordan-rand-wang-boccaletti-szolnoki-2017-statistical-physics-cooperation]]

## BibTeX
```bibtex
@article{nowak2005indirect,
  author  = {Nowak, Martin A. and Sigmund, Karl},
  title   = {Evolution of Indirect Reciprocity},
  journal = {Nature},
  volume  = {437},
  number  = {7063},
  pages   = {1291--1298},
  year    = {2005},
  doi     = {10.1038/nature04131}
}
```
