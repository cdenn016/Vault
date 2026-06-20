---
type: paper
title: "The spreading of misinformation online"
aliases: ["Del Vicario et al. 2016", "Spreading of misinformation online"]
authors: ["Del Vicario M.", "Bessi A.", "Zollo F.", "Petroni F.", "Scala A.", "Caldarelli G.", "Stanley H. E.", "Quattrociocchi W."]
year: 2016
url: https://doi.org/10.1073/pnas.1517441113
tags: [cluster/social-physics, project/social-physics, field/sociology, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# The spreading of misinformation online

> [!info] Citation
> Del Vicario, M., Bessi, A., Zollo, F., Petroni, F., Scala, A., Caldarelli, G., Stanley, H. E., & Quattrociocchi, W. (2016). *The spreading of misinformation online*. Proceedings of the National Academy of Sciences (PNAS) 113(3):554-559. DOI: [10.1073/pnas.1517441113](https://doi.org/10.1073/pnas.1517441113).

## TL;DR
A quantitative Facebook study of how users engage with two opposing narratives — science news versus conspiracy theory — showing that consumption and sharing are organized along a single dominant narrative for each user. Homogeneous, polarized communities form around each narrative, and confirmation bias, rather than content veracity, governs which information diffuses and how far. The authors fit a data-driven percolation/cascade model in which homogeneity and polarization are the principal determinants of cascade size and lifetime.

## What it establishes
Users are shown to be strongly segregated into two near-disjoint communities whose members consume almost exclusively within their preferred narrative. Cascade dynamics are modeled as a percolation-like process on this segregated substrate: the probability a piece of content propagates to a neighbor scales with shared leaning, so cascades grow large only inside homogeneous clusters. Letting $h_C$ denote the homogeneity of a community $C$ (fraction of same-narrative neighbors), the empirical cascade-size distribution is heavy-tailed within high-$h_C$ clusters and truncated across them, identifying confirmation-bias-driven homophily as the engine of viral spread.

## Relevance to this research
A strongly used empirical anchor for the echo-chamber prediction of belief inertia. Confirmation-bias-driven homophilic clustering is precisely the macroscopic signature the overdamped VFE flow should reproduce: agents up-weight narrative-consistent neighbors, the attention-weighted KL coupling $\beta_{ij}\,\mathrm{KL}(q_i\,\|\,\Omega_{ij}[q_j])$ becomes effectively block-diagonal, and the population freezes into mutually non-influencing belief clusters. The percolation/cascade framing also connects to the program's renormalization-group coarse-graining — cascades within a cluster are the within-block correlations a coarse-graining step would integrate out, and the cluster boundaries are where the gauge-transported coupling vanishes. This is mechanism the model targets directly, not adjacent context.

## Cross-links
- Concept: [[Echo chambers and polarization]]
- Related: [[Multi-agent variational free energy]], [[Renormalization-group flow of beliefs]], [[Community detection and modularity]]
- Related sources: [[cinelli-2021-echo-chamber-effect]], [[garrett-2009-echo-chambers-selective-exposure]], [[conover-2011-political-polarization-twitter]]

## BibTeX
```bibtex
@article{delvicario2016spreading,
  author  = {Del Vicario, Michela and Bessi, Alessandro and Zollo, Fabiana and Petroni, Fabio and Scala, Antonio and Caldarelli, Guido and Stanley, H. Eugene and Quattrociocchi, Walter},
  title   = {The spreading of misinformation online},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {113},
  number  = {3},
  pages   = {554--559},
  year    = {2016},
  doi     = {10.1073/pnas.1517441113}
}
```
