---
type: reference
title: "Hierarchy of Linear Light Cones with Long-Range Interactions"
aliases: ["tran2020hierarchy"]
authors: ["Minh C. Tran", "Chi-Fang Chen", "Adam Ehrenberg", "Andrew Y. Guo", "Abhinav Deshpande", "Yifan Hong", "Zhe-Xuan Gong", "Alexey V. Gorshkov", "Andrew Lucas"]
year: 2020
venue: "Physical Review X"
doi: "10.1103/PhysRevX.10.031009"
arxiv: "2001.11509"
url: "https://doi.org/10.1103/PhysRevX.10.031009"
tags: [cluster/multi-agent, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Hierarchy of Linear Light Cones with Long-Range Interactions

> [!info] Citation
> Tran, M. C., Chen, C.-F., Ehrenberg, A., Guo, A. Y., Deshpande, A., Hong, Y., Gong, Z.-X., Gorshkov, A. V., Lucas, A. (2020). *Hierarchy of Linear Light Cones with Long-Range Interactions*. Physical Review X, 10(3), 031009. [DOI](https://doi.org/10.1103/PhysRevX.10.031009), [arXiv](https://arxiv.org/abs/2001.11509)

[Local PDF](../pdfs/tran-2020-hierarchy-linear-light.pdf), 36 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages.

## TL;DR

For quantum many-body systems with power-law interactions decaying as $1/r^\alpha$, the paper proves that different information-processing tasks obey linear light cones at different thresholds of $\alpha$, and that these thresholds are tight.

## Problem & setting

With finite-range interactions, a linear light cone bounds the spread of information. Earlier work had proved a linear Lieb-Robinson light cone for $\alpha > 2d+1$ in $d$ dimensions. The paper asks whether this can be tightened and whether the Lieb-Robinson bounds constrain other measures of spreading, such as state transfer and scrambling.

## Method

Operator growth is bounded through commutator norms and, for the Frobenius norm, through a many-body quantum walk interpretation of operator evolution combined with classical probability techniques. Explicit Hamiltonians and a single-particle state-transfer protocol show tightness.

## Key results

The paper establishes three linear light cones with sharp thresholds. In one dimension these are the Lieb-Robinson cone for $\alpha > 3$ (all states), the Frobenius cone for $\alpha > 5/2$ (typical random states), and the free cone for $\alpha > 2$ (non-interacting systems). The Lieb-Robinson and free results generalize to arbitrary dimension, with the free threshold at $\alpha > d+1$. The Frobenius cone also bounds universal state transfer and many-body chaos. The bounds are stated to be optimal up to subalgebraic corrections.

## Relevance to this research

The manuscript cites this paper twice. In its scale analysis it notes that its threshold coincides with the free-particle light cone for interactions decaying faster than $r^{-(D+1)}$, because linear message passing propagates a single tangent vector, while the many-body thresholds of the hierarchy have no analog. In its related-work section it lists the hierarchy among bounds on how far correlations spread. See [[Bundle scale space]], [[Quantum information]] and [[Meta-agents and hierarchical emergence]].

## Cross-links

[[Collective agents literature map]]; [[Bundle scale space]]; [[Quantum information]]; [[Meta-agents and hierarchical emergence]].

## BibTeX

```bibtex
@article{tran2020hierarchy,
  author        = {Tran, Minh C. and Chen, Chi-Fang and Ehrenberg, Adam and Guo, Andrew Y. and Deshpande, Abhinav and Hong, Yifan and Gong, Zhe-Xuan and Gorshkov, Alexey V. and Lucas, Andrew},
  title         = {Hierarchy of Linear Light Cones with Long-Range Interactions},
  journal       = {Physical Review X},
  volume        = {10},
  number        = {3},
  pages         = {031009},
  year          = {2020},
  doi           = {10.1103/PhysRevX.10.031009},
  eprint        = {2001.11509},
  archivePrefix = {arXiv}
}
```
