---
type: paper
title: "The Law of Group Polarization"
aliases: ["Sunstein 2002", "The Law of Group Polarization"]
authors: ["Sunstein C. R."]
year: 2002
url: https://doi.org/10.1111/1467-9760.00148
tags: [cluster/social-physics, project/social-physics, field/psychology, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# The Law of Group Polarization

> [!info] Citation
> Sunstein, C. R. (2002). *The Law of Group Polarization*. Journal of Political Philosophy 10(2):175-195. DOI: [10.1111/1467-9760.00148](https://doi.org/10.1111/1467-9760.00148).

## TL;DR
A synthesis of the deliberation literature into a single empirical regularity: when like-minded people deliberate together, the group's post-deliberation position is more extreme, in the same direction, than the average of its members' pre-deliberation positions. Sunstein names this "group polarization" and attributes it to two mechanisms — limited argument pools (a homogeneous group hears disproportionately one-sided arguments) and social comparison / reputation (members shift toward the perceived group norm to maintain standing). He extends the idea to "enclave deliberation" and warns of its democratic costs.

## What it establishes
The law is a statement about the displacement of the group mean under within-cluster deliberation. If $\bar{x}_0$ is the pre-deliberation average of an enclave's positions and $\bar{x}_1$ the post-deliberation average, then $\bar{x}_1$ lies beyond $\bar{x}_0$ in the direction the group already leaned, $|\bar{x}_1| > |\bar{x}_0|$ with $\operatorname{sign}(\bar{x}_1)=\operatorname{sign}(\bar{x}_0)$ — extremization rather than mere consensus at the centroid. The two proposed mechanisms are an informational asymmetry (the available arguments are skewed toward the prevailing view) and a normative pull (conformity to the emerging group position), both reinforcing within a homogeneous cluster.

## Relevance to this research
A strong theoretical bridge between echo-chamber structure and the polarization prediction. The law states the mechanism — within-cluster reinforcement producing movement past the prior mean — that the program's homophilic attention coupling should generate endogenously: once $\beta_{ij}$ concentrates on aligned neighbors, the attention-weighted KL coupling pulls members toward a shared, already-extreme centroid, and in the inertial (underdamped) regime belief momentum can carry the cluster mean past that centroid into genuine overshoot, the dynamical signature of extremization that a first-order averaging flow (which can only contract toward, never beyond, the consensus point) cannot produce. This is conceptual machinery the program aims to derive, linking the echo-chamber and inertia threads.

## Cross-links
- Concept: [[Echo chambers and polarization]]
- Related: [[Bounded confidence]], [[Hamiltonian belief dynamics]], [[Multi-agent variational free energy]]
- Related sources: [[sunstein-2017-republic]], [[baldassarri-bearman-2007-political-polarization]], [[bail-2018-exposure-opposing-views]]

## BibTeX
```bibtex
@article{sunstein2002law,
  author  = {Sunstein, Cass R.},
  title   = {The Law of Group Polarization},
  journal = {Journal of Political Philosophy},
  volume  = {10},
  number  = {2},
  pages   = {175--195},
  year    = {2002},
  doi     = {10.1111/1467-9760.00148}
}
```
