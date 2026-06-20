---
type: paper
title: "Exposure to ideologically diverse news and opinion on Facebook"
aliases: ["Bakshy, Messing & Adamic 2015", "Ideologically diverse news on Facebook"]
authors: ["Bakshy E.", "Messing S.", "Adamic L. A."]
year: 2015
url: https://doi.org/10.1126/science.aaa1160
tags: [cluster/social-physics, project/social-physics, field/sociology, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Exposure to ideologically diverse news and opinion on Facebook

> [!info] Citation
> Bakshy, E., Messing, S., & Adamic, L. A. (2015). *Exposure to ideologically diverse news and opinion on Facebook*. Science 348(6239):1130-1132. DOI: [10.1126/science.aaa1160](https://doi.org/10.1126/science.aaa1160).

## TL;DR
A study of 10.1 million U.S. Facebook users with self-reported ideology that decomposes the filtering of cross-cutting (opposite-leaning) hard-news content into three sequential stages: the composition of one's social network (who one is friends with), the algorithmic ranking of the News Feed (what the feed surfaces), and individual choice (what one clicks). The headline finding is that homophilic network structure and, especially, individual selective clicking limit exposure to cross-cutting content more than the ranking algorithm does. (The study was conducted by Facebook researchers and has been critiqued for its non-random sample of ideology-disclosing users.)

## What it establishes
The pipeline is a multiplicative decomposition of the cross-cutting exposure rate. If $p_{\text{net}}$ is the share of cross-cutting content among what one's friends share, $p_{\text{feed}}$ the share after algorithmic ranking, and $p_{\text{click}}$ the share among items actually clicked, then each stage attenuates the cross-cutting fraction: $p_{\text{net}} > p_{\text{feed}} > p_{\text{click}}$. Quantitatively, network homophily already removes much cross-cutting content, the algorithm removes a modest additional increment, and individual choice removes a comparable or larger increment, so the dominant filters are structural and behavioral rather than algorithmic.

## Relevance to this research
A strong empirical decomposition that maps cleanly onto a distinction the program makes explicitly: the coupling graph (who is connected to whom — the network composition stage) versus the agent-level attention/confirmation weighting $\beta_{ij}$ (what each connected agent actually attends to — the choice stage). The model can encode network homophily as the support of the coupling matrix and selective clicking as the softmax attention that re-weights that support toward aligned neighbors, and the paper's three-stage attenuation gives an empirical budget for how much of the echo chamber lives in each. Honestly, this is calibration and structure rather than core dynamics, but it is directly probative of how to apportion the model's two filtering mechanisms.

## Cross-links
- Concept: [[Echo chambers and polarization]]
- Related: [[Multi-agent variational free energy]], [[Opinion dynamics]], [[Community detection and modularity]]
- Related sources: [[cinelli-2021-echo-chamber-effect]], [[guess-2023-feed-algorithms-election]], [[garrett-2009-echo-chambers-selective-exposure]]

## BibTeX
```bibtex
@article{bakshy2015exposure,
  author  = {Bakshy, Eytan and Messing, Solomon and Adamic, Lada A.},
  title   = {Exposure to ideologically diverse news and opinion on Facebook},
  journal = {Science},
  volume  = {348},
  number  = {6239},
  pages   = {1130--1132},
  year    = {2015},
  doi     = {10.1126/science.aaa1160}
}
```
