---
type: reference
title: "Efficient Bayesian Learning in Social Networks with Gaussian Estimators"
aliases: ["mossel2016efficient"]
authors: ["Elchanan Mossel", "Noah Olsman", "Omer Tamuz"]
year: 2016
venue: "2016 54th Annual Allerton Conference on Communication, Control, and Computing (Allerton)"
doi: "10.1109/ALLERTON.2016.7852262"
arxiv: "1002.0747"
url: "https://doi.org/10.1109/ALLERTON.2016.7852262"
tags: [cluster/multi-agent, project/multi-agent, field/economics, field/cs-ml, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# Efficient Bayesian Learning in Social Networks with Gaussian Estimators

> [!info] Citation
> Mossel, E., Olsman, N., Tamuz, O. (2016). *Efficient Bayesian Learning in Social Networks with Gaussian Estimators*. 2016 54th Annual Allerton Conference on Communication, Control, and Computing (Allerton), 425-432. IEEE. [DOI](https://doi.org/10.1109/ALLERTON.2016.7852262); [arXiv](https://arxiv.org/abs/1002.0747)

[Local PDF](../pdfs/mossel-2016-efficient-bayesian-learning.pdf), 8 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

A group of Bayesian agents on a connected graph each holds a Gaussian private signal of a common real-valued state, repeatedly announces its current estimate to its neighbors, and updates by Bayes' rule. The paper shows that this process reaches the full-information belief, that each agent's computation is efficient, and gives convergence bounds in terms of the number of agents and the graph diameter.

## Problem & setting

The model has $N$ agents on an undirected connected graph with diameter $D$ and a state $\theta\in\mathbb R$. Each agent receives an independent signal drawn from a normal distribution centered at $\theta$. The introduction separates rational models, in which agents choose optimal actions, from rule-of-thumb models in which they follow a fixed heuristic, and places this work in the first class while asking for computationally tractable agent calculations. It notes that an essentially identical model was studied earlier by DeMarzo, Vayanos and Zweibel, who did not treat computation.

## Key results

The abstract and introduction state that all agents converge to the belief they would hold with access to every private signal, that the process converges within $2ND$ steps on any graph and within $D$ steps on trees and distance-transitive graphs, and that on those graph classes most agents learn little about the private signals of most others. The extract confirms that $D$ is a lower bound on convergence time in any graph.

## Relevance to this research

The manuscript cites this paper in its agency and related-work sections as a known result on exact aggregation by Bayesian agents who exchange estimates, and as an open comparison: whether the protocol coincides with exact fusion of posterior messages in the manuscript's setting is left open. The manuscript's reading record says it read the abstract only, so any claim beyond the abstract and the opening pages of the extract is not established here. The topic bears on [[Decentralized Bayesian inference]], [[Non-Bayesian social learning]] and [[Common knowledge and Bayesian agreement]], and on inferential closure of a collective in [[Collective active inference]].

## Cross-links

[[Collective agents literature map]]; [[Decentralized Bayesian inference]]; [[Non-Bayesian social learning]]; [[Common knowledge and Bayesian agreement]]; [[Collective active inference]]; [[olfati-saber-2005-distributed-kalman-filter]].

## BibTeX

```bibtex
@inproceedings{mossel2016efficient,
  author        = {Mossel, Elchanan and Olsman, Noah and Tamuz, Omer},
  title         = {Efficient {Bayesian} Learning in Social Networks with {Gaussian} Estimators},
  booktitle     = {2016 54th Annual Allerton Conference on Communication, Control, and Computing (Allerton)},
  pages         = {425--432},
  publisher     = {IEEE},
  address       = {Monticello, IL, USA},
  year          = {2016},
  doi           = {10.1109/ALLERTON.2016.7852262},
  eprint        = {1002.0747},
  archivePrefix = {arXiv}
}
```
