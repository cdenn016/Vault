---
type: paper
title: "Complex networks: Structure and dynamics"
aliases: ["Boccaletti et al. 2006", "Complex networks: structure and dynamics"]
authors: ["Boccaletti S.", "Latora V.", "Moreno Y.", "Chavez M.", "Hwang D.-U."]
year: 2006
url: https://doi.org/10.1016/j.physrep.2005.10.009
tags: [cluster/social-physics, project/social-physics, field/physics, field/cs-ml, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# Complex networks: Structure and dynamics

> [!info] Citation
> Boccaletti, S., Latora, V., Moreno, Y., Chavez, M., & Hwang, D.-U. (2006). *Complex networks: Structure and dynamics*. Physics Reports, 424(4-5), 175-308. doi:10.1016/j.physrep.2005.10.009.

## TL;DR
This Physics Reports review surveys complex networks with the emphasis squarely on *dynamical processes that run on top of structure* rather than on topology alone. After cataloguing the standard structural measures and models, it devotes most of its length to how topology shapes collective dynamics: synchronization of coupled oscillators, epidemic and rumor spreading, opinion and game dynamics, and network resilience. Its distinctive contribution is to treat the interplay between graph spectra and collective states as the central object, making it the natural reference for "dynamics-on-networks" questions.

## What it establishes
For synchronization the review centers the Master Stability Function formalism: a network of identical oscillators with Laplacian coupling synchronizes when the eigenratio of the Laplacian spectrum,
$$\frac{\lambda_N}{\lambda_2},$$
falls inside the stability interval of the single-node dynamics, where $\lambda_2$ is the algebraic connectivity (the spectral gap) and $\lambda_N$ the largest Laplacian eigenvalue. This cleanly separates the contribution of node dynamics from that of topology — the same network either locks into a coherent collective state or fragments depending purely on its spectrum. The review applies the same spectral lens to spreading thresholds and to consensus/opinion processes, tying assortativity, modularity, and degree heterogeneity to whether collective dynamics cohere.

## Relevance to this research
The synchronization-on-networks material is the closest classical analogue to belief synchronization and consensus under the model's gauge coupling: the Master Stability Function and the Laplacian spectral gap $\lambda_2$ are exactly the objects one would compute to predict whether the coupled belief dynamics lock into agreement or split into fragments. This ties the influence-graph spectrum to the model's consensus-versus-fragmentation transition, making the review strong for the dynamics-on-graph side, though the mapping from oscillator phase to Gaussian belief is analogical rather than an identity. See [[Network structure — small-world and scale-free]], [[Opinion dynamics]], and [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Network structure — small-world and scale-free]]
- Related sources: [[newman-2003-structure-function]], [[albert-barabasi-2002-statistical-mechanics]], [[watts-strogatz-1998-small-world]]

## BibTeX
```bibtex
@article{boccaletti2006complex,
  author  = {Boccaletti, S. and Latora, V. and Moreno, Y. and Chavez, M. and Hwang, D.-U.},
  title   = {Complex networks: Structure and dynamics},
  journal = {Physics Reports},
  year    = {2006},
  volume  = {424},
  number  = {4-5},
  pages   = {175--308},
  doi     = {10.1016/j.physrep.2005.10.009}
}
```
