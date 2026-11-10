---
type: reference
title: "Geographical Dispersal of Mobile Communication Networks"
aliases: ["lambiotte2008geographical"]
authors: ["Renaud Lambiotte", "Vincent D. Blondel", "Cristobald de Kerchove", "Etienne Huens", "Christophe Prieur", "Zbigniew Smoreda", "Paul Van Dooren"]
year: 2008
venue: "Physica A: Statistical Mechanics and its Applications"
doi: "10.1016/j.physa.2008.05.014"
url: "https://doi.org/10.1016/j.physa.2008.05.014"
tags: [cluster/multi-agent, cluster/social-physics, cluster/social-physics/networks-and-contagion, project/multi-agent, project/social-physics, field/physics, field/sociology]
created: 2026-11-10
updated: 2026-11-10
---
# Geographical Dispersal of Mobile Communication Networks

> [!info] Citation
> Lambiotte, R., Blondel, V. D., de Kerchove, C., Huens, E., Prieur, C., Smoreda, Z., Van Dooren, P. (2008). *Geographical Dispersal of Mobile Communication Networks*. Physica A: Statistical Mechanics and its Applications, 387(21), 5317-5325. [DOI](https://doi.org/10.1016/j.physa.2008.05.014)

[Local PDF](../pdfs/lambiotte-2008-geographical-dispersal-mobile.pdf), 17 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper analyzes a communication network built from the records of a mobile phone company, covering 2.5 million customers with known home locations, and relates link probability to the distance between customers. It also examines how far communication triangles extend geographically and proposes a model of migration and local adaptation that reproduces that property.

## Problem & setting

Complex-network studies usually treat nodes as equivalent. The authors use geographical position as a measurable node property and ask how it shapes the connection pattern of a social communication network. They note that in socio-economic networks the interaction between two places often decays as a power of distance with exponent near two, which motivates the name gravity model.

## Method

The network has customers as nodes and calls or text messages as links, over a period of six months. The authors measure the degree distribution, the dependence of link probability on distance, and the geographical extent of triangular motifs. A model with agent migration and local adaptation is then studied analytically and by simulation.

## Key results

The abstract reports a power-law degree distribution with exponent $-5$ and a link probability that follows a gravity model, decreasing as $d^{-2}$ with the distance $d$. Communication triangles are not confined to geographically adjacent nodes and may span large distances, a property the authors say existing geographical network models do not capture. The proposed model reproduces it, and simulations confirm its analytical predictions.

## Relevance to this research

The manuscript cites this paper for the statement that link probability between users of a Belgian mobile network falls off as the inverse square of their distance, used to argue that geography still limits connection even when telecommunication adds links whose cost does not depend on distance. The manuscript's record says the abstract was read. The result bears on the cost structure of links among communicating agents in [[Meta-agents and hierarchical emergence]] and on spatial network models such as [[Hidden metric space]] and [[Network structure — small-world and scale-free]].

## Cross-links

[[Collective agents literature map]]; [[Meta-agents and hierarchical emergence]]; [[Hidden metric space]]; [[Network structure — small-world and scale-free]]; [[liben-nowell-2005-geographic-routing-social]].

## BibTeX

```bibtex
@article{lambiotte2008geographical,
  author  = {Lambiotte, Renaud and Blondel, Vincent D. and de Kerchove, Cristobald and Huens, Etienne and Prieur, Christophe and Smoreda, Zbigniew and Van Dooren, Paul},
  title   = {Geographical Dispersal of Mobile Communication Networks},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume  = {387},
  number  = {21},
  pages   = {5317--5325},
  year    = {2008},
  doi     = {10.1016/j.physa.2008.05.014}
}
```
