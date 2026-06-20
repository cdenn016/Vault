---
type: paper
title: "Political Polarization on Twitter"
aliases: ["Conover et al. 2011", "Political Polarization on Twitter"]
authors: ["Conover M. D.", "Ratkiewicz J.", "Francisco M.", "Goncalves B.", "Flammini A.", "Menczer F."]
year: 2011
url: https://doi.org/10.1609/icwsm.v5i1.14126
tags: [cluster/social-physics, project/social-physics, field/cs-ml, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Political Polarization on Twitter

> [!info] Citation
> Conover, M. D., Ratkiewicz, J., Francisco, M., Goncalves, B., Flammini, A., & Menczer, F. (2011). *Political Polarization on Twitter*. Proceedings of the International AAAI Conference on Web and Social Media (ICWSM) 5(1):89-96 (ICWSM 2021 Test-of-Time Award). DOI: [10.1609/icwsm.v5i1.14126](https://doi.org/10.1609/icwsm.v5i1.14126).

## TL;DR
A network analysis of political communication on Twitter around the 2010 U.S. midterm elections, distinguishing two interaction modalities. The retweet network is highly segregated into two dense partisan clusters (left and right) with very few links bridging them, whereas the mention network is far more integrated, with users frequently engaging across ideological lines (often in argument). The paper is a seminal demonstration that the structure of online political discourse is sharply community-partitioned, and that the apparent polarization depends on which interaction type one measures.

## What it establishes
Treating retweets and mentions as separate directed graphs, the authors apply community detection and label propagation to assign political alignment. The retweet graph exhibits near-block-diagonal structure: high within-cluster modularity $Q$ and almost no cross-cluster edges, so endorsement flows stay inside ideological communities. The mention graph, by contrast, has low modularity and many cross-cutting ties, indicating that exposure (being mentioned) crosses lines even when endorsement (retweeting) does not. The contrast operationalizes a key distinction between the network of agreement and the network of contact.

## Relevance to this research
A strong empirical and network-structure anchor. The near-disconnected two-cluster retweet network is exactly the segregated coupling structure the program's community-detection / meta-agent emergence machinery aims to recover and the gauge-transported coupling aims to reproduce — high within-cluster $\beta_{ij}$ and near-zero across, yielding block-diagonal influence and emergent meta-agents at the cluster scale. The retweet-versus-mention split also concretely instantiates the program's separation between the endorsement coupling (which freezes into clusters) and the broader contact graph (which need not), informing how the model should distinguish exposure from influence. This is structural machinery the model targets, not loose analogy.

## Cross-links
- Concept: [[Community detection and modularity]]
- Related: [[Multi-agent variational free energy]], [[Echo chambers and polarization]], [[Sociophysics]]
- Related sources: [[cinelli-2021-echo-chamber-effect]], [[del-vicario-2016-misinformation-online]], [[baldassarri-bearman-2007-political-polarization]]

## BibTeX
```bibtex
@inproceedings{conover2011political,
  author    = {Conover, Michael D. and Ratkiewicz, Jacob and Francisco, Matthew and Goncalves, Bruno and Flammini, Alessandro and Menczer, Filippo},
  title     = {Political Polarization on Twitter},
  booktitle = {Proceedings of the International AAAI Conference on Web and Social Media (ICWSM)},
  volume    = {5},
  number    = {1},
  pages     = {89--96},
  year      = {2011},
  doi       = {10.1609/icwsm.v5i1.14126}
}
```
