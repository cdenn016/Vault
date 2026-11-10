---
type: reference
title: "The Decay of Impact with Network Distance in Linear Diffusion Processes"
aliases: ["murraywatters2026decay"]
authors: ["Alexander Murray-Watters", "Cheng Wang", "John R. Hipp", "Cynthia Lakon", "Carter T. Butts"]
year: 2026
arxiv: "2604.23034"
url: "https://arxiv.org/abs/2604.23034"
tags: [cluster/social-physics, cluster/social-physics/opinion-dynamics, project/multi-agent, project/social-physics, field/sociology, field/statistics]
created: 2026-11-10
updated: 2026-11-10
---
# The Decay of Impact with Network Distance in Linear Diffusion Processes

> [!info] Citation
> Murray-Watters, A., Wang, C., Hipp, J. R., Lakon, C., Butts, C. T. (2026). *The Decay of Impact with Network Distance in Linear Diffusion Processes*. arXiv preprint. [arXiv](https://arxiv.org/abs/2604.23034)

[Local PDF](../pdfs/murray-watters-2026-decay-impact-network.pdf), 19 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

The paper derives an approximation to the total equilibrium impact of one node on another in forced linear diffusion models, showing that to first order it is a product of eigenvector centralities times a factor that falls exponentially with network distance at a rate set by the graph spectrum.

## Problem & setting

Forced linear diffusion models update each node's state as a weighted average of its neighbors' states plus an exogenous forcing term. The abstract lists the Friedkin-Johnsen model of social influence, Katz and Bonacich status and power scores, and the network autocorrelation model as examples. Influence along any single walk falls exponentially with walk length, but the total impact at equilibrium sums over walks of all lengths, whose number depends on global structure, so the dependence of total impact on distance is not obvious.

## Method

The authors derive a first-order spectral approximation and show how higher-order eigenvectors of the adjacency matrix refine it. They then test it numerically on friendship networks from educational settings.

## Key results

The approximation is reported to decline exponentially with distance, with node-specific factors given by eigenvector centrality. The numerical study reports an average exponential decline in impact on the networks studied, and that the first-order approximation is often a good proxy for the exact total impact; the introduction adds that the second term gives only modest further gains.

## Relevance to this research

The manuscript cites this preprint in its related-work discussion of decay length: approximately exponential decay of influence has already been reported for forced linear diffusion models, so the manuscript does not present an exponential decay length of the standard massive lattice Green's function as new. The connection is to [[Opinion dynamics]], to Friedkin-Johnsen-type updating, and to [[Spectral graph theory]] and [[Graph Laplacian]] methods for influence on networks. The manuscript's reading record only confirms the arXiv record.

## Cross-links

[[Collective agents literature map]]; [[Opinion dynamics]]; [[Spectral graph theory]]; [[Graph Laplacian]]; [[Social influence and conformity]].

## BibTeX

```bibtex
@misc{murraywatters2026decay,
  author        = {Murray-Watters, Alexander and Wang, Cheng and Hipp, John R. and Lakon, Cynthia and Butts, Carter T.},
  title         = {The Decay of Impact with Network Distance in Linear Diffusion Processes},
  year          = {2026},
  eprint        = {2604.23034},
  archivePrefix = {arXiv}
}
```
