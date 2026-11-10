---
type: reference
title: "Stochastic thermodynamics of bipartite systems: transfer entropy inequalities and a Maxwell's demon interpretation"
aliases: ["hartich2014stochastic"]
authors: ["D. Hartich", "A. C. Barato", "U. Seifert"]
year: 2014
venue: "Journal of Statistical Mechanics: Theory and Experiment"
doi: "10.1088/1742-5468/2014/02/P02016"
arxiv: "1402.0419"
url: "https://doi.org/10.1088/1742-5468/2014/02/P02016"
tags: [cluster/multi-agent, cluster/info-geometry, project/multi-agent, field/physics]
created: 2026-11-10
updated: 2026-11-10
---
# Stochastic thermodynamics of bipartite systems: transfer entropy inequalities and a Maxwell's demon interpretation

> [!info] Citation
> Hartich, D., Barato, A. C., Seifert, U. (2014). *Stochastic thermodynamics of bipartite systems: transfer entropy inequalities and a Maxwell's demon interpretation*. Journal of Statistical Mechanics: Theory and Experiment, 2014(2), P02016. [DOI](https://doi.org/10.1088/1742-5468/2014/02/P02016); [arXiv](https://arxiv.org/abs/1402.0419)

[Local PDF](../pdfs/hartich-2014-stochastic-thermodynamics-bipartite.pdf), 18 pages; retrieved November 10, 2026. Reading basis: local PDF, first pages and abstract.

## TL;DR

The paper studies the stationary state of a Markov process on a bipartite system, in which only one of two variables changes in any jump, and relates work extraction, transfer entropy and a Maxwell's demon interpretation of one subsystem.

## Problem & setting

A bipartite system is a Markov process whose states are pairs of variables, with transitions that change only one variable at a time. The authors take one subsystem as a Maxwell's demon acting on the other, which extracts work from a heat bath, so that the full thermodynamic cost is the standard entropy production of the bipartite system. They name stochastic models of cellular sensing as examples of such systems.

## Method

The authors define the entropy production rate of the external medium as a sum of a part caused by jumps in one variable and a part caused by jumps in the other, define the transfer entropy between the subsystems, and prove an integral fluctuation relation that involves it. They illustrate the inequalities with a four-state example.

## Key results

According to the abstract, the entropy decrease of the first subsystem bounds the rate of extracted work more tightly than either the transfer-entropy rate from that subsystem to the demon or the heat dissipated through the demon's dynamics. The latter two rates cannot be ordered by an inequality, which the four-state example shows.

## Relevance to this research

The manuscript cites the paper for the comparison between information flow and the transfer-entropy rate in a bipartite sensor model, of which one of its discrete-time inequalities is the analog. The reading record says only the arXiv abstract was opened, for the statement that in bipartite systems the transfer-entropy rate bounds the information flow from above, and that the conditions of that inequality were not read beyond the abstract; the manuscript proves its discrete-time inequality itself. See [[Stochastic Thermodynamics]], [[Mutual information]], [[Nonequilibrium steady state]] and [[Markov Blanket]].

## Cross-links

[[Collective agents literature map]]; [[Stochastic Thermodynamics]]; [[Mutual information]]; [[Nonequilibrium steady state]]; [[Markov Blanket]].

## BibTeX

```bibtex
@article{hartich2014stochastic,
  author  = {Hartich, D. and Barato, A. C. and Seifert, U.},
  title   = {Stochastic thermodynamics of bipartite systems: transfer entropy inequalities and a {M}axwell's demon interpretation},
  journal = {Journal of Statistical Mechanics: Theory and Experiment},
  volume  = {2014},
  number  = {2},
  pages   = {P02016},
  year    = {2014},
  doi     = {10.1088/1742-5468/2014/02/P02016},
  eprint  = {1402.0419},
  archiveprefix = {arXiv}
}
```
