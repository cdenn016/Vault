---
type: paper
title: "Renormalization Group for Critical Phenomena in Complex Networks"
aliases:
  - "Boettcher 2011"
  - "Hanoi networks RG"
authors:
  - Boettcher, Stefan
  - Brunson, C. T.
year: 2011
arxiv: null
url: https://doi.org/10.3389/fphys.2011.00102
tags:
  - cluster/social-physics/networks-and-contagion
  - project/social-physics
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Renormalization Group for Critical Phenomena in Complex Networks

> [!info] Citation
> Boettcher, S. and Brunson, C. T. (2011). "Renormalization group for critical phenomena in complex networks." *Frontiers in Physiology (Fractal Physiology)* 2:102. doi:10.3389/fphys.2011.00102

## TL;DR
This paper analyzes the Ising ferromagnet on a family of "Hanoi" networks — hierarchical graphs that embed small-world long-range bonds into a one-dimensional backbone — using an exact real-space renormalization group (RG). The central finding is that critical behavior in these networks is generically non-universal, but falls into exactly three distinct regimes characterized by the type of divergence in the correlation length: a non-universal power law, a BKT-like essential singularity, and a full essential singularity. A general cubic RG recursion with a root branch-point is proposed as a unifying classification of all three regimes across hierarchical and complex networks.

## Problem & setting
How do critical phenomena and phase transitions in statistical models (specifically the Ising ferromagnet) behave on complex networks that combine real-world geometry with small-world hierarchical shortcuts? Prior work had identified non-universal exponents on various hierarchical networks, as well as surprising BKT-like transitions in unrelated network models, but lacked a unified framework to classify these behaviors. This work addresses that gap using the Hanoi networks (HN3, HN5, and a one-parameter interpolating family), on which the renormalization group is exact.

## Method
The Hanoi networks are built on a 1D backbone where site $n$ is parameterized by a hierarchy level $i$ and offset $j$ via $n = 2^i(2j+1)$; small-world bonds are then added deterministically according to this hierarchical labeling. The RG proceeds by tracing out odd-labeled spins level by level, yielding closed recursion equations for the effective couplings $(\kappa, \lambda, \mu)$ (related to inverse activities). For HN3 the recursion closes on two couplings; for HN5 an additional long-range coupling $L_1$ is added as a bare feature of the network, altering the fixed-point structure. The interpolating family is parameterized by $y \in [0,1]$, which controls the relative strength of the small-world bonds. A general cubic model
$$\kappa_{n+1} = [\kappa_b + 1 + f(\mu)]\kappa_n + 2\kappa_b \kappa_n^2 - \kappa_n^3$$
is proposed to capture the root branch-point topology $\bar{\kappa}_\pm = \kappa_b \pm \sqrt{f(\mu)}$ that underlies all three critical regimes.

## Key results
Three distinct critical regimes are identified as a function of the parameter $y$ (equivalently, the relative strength of hierarchical long-range bonds):

1. **Non-universal power law** ($\xi \sim |\mu - \mu_c|^{-\nu}$ with non-universal $\nu$): the RG flow crosses the unstable fixed-point branch below the branch-point singularity, so critical behavior is governed by local properties of the unstable point alone.

2. **BKT-like essential singularity** ($\xi \sim \exp(\mathrm{const}/\sqrt{\mu_c - \mu})$): the RG flow passes through the branch-point singularity, which controls the transition via a boundary-layer analysis; critical at $y_c = \ln(3/2)/\ln 2 \approx 0.585$.

3. **Full essential singularity** ($\xi \sim \exp(\mathrm{const}/|\mu - \mu_c|)$): the branch-point lies outside the physical regime; the flow passes between two stable fixed-point lines without accessing the singularity, yielding an exponentially divergent correlation length.

The critical temperature for HN5 ($y=1$) involves the golden ratio $\phi$: $\mu_c = 1/\phi$, giving $kT_c/J \approx 4.156$. Similar behavior has been observed in percolation models on hierarchical networks and in social interaction networks with hierarchical structure.

## Relevance to this research
This paper is relevant to the social-physics dimension of the research program rather than the core VFE/gauge-theory transformer. The hierarchical network structure and the exact real-space RG are a formal analogue to multi-scale belief propagation and coarse-graining in hierarchical generative models; the fixed-point classification by regime mirrors the question of what universality class the VFE minimization flow belongs to under different coupling strengths. More directly, the Hanoi network's combination of local geometry with small-world long-range bonds is a structural model for social interaction graphs on which opinion dynamics or active inference agents might be studied. The BKT-like transition appearing generically from network topology (rather than from any lattice-specific mechanism) is of interest for understanding phase transitions in collective inference or belief synchronization in multi-agent systems. The "patchiness" phenomenon — persistent partial order in the disordered phase due to hierarchical long-range couplings — may be relevant to understanding metastable consensus states in agent networks.

## Cross-links
- Concepts: [[Renormalization Group]] | [[Phase Transitions]] | [[Small-World Networks]] | [[Critical Phenomena]]
- Related sources: [[dorogovtsev2008critical]]
- Manuscript/Project: [[VFE Transformer Program]] | [[Multi-Agent Active Inference]]

## BibTeX
```bibtex
@article{boettcher2012renormalization,
  author  = {Boettcher, Stefan and Brunson, C. T.},
  title   = {Renormalization group for critical phenomena in complex networks},
  journal = {Frontiers in Physiology},
  volume  = {2},
  pages   = {102},
  year    = {2011},
  doi     = {10.3389/fphys.2011.00102},
}
```
