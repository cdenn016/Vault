---
type: paper
title: "Aggregation-diffusion equations: dynamics, asymptotics, and singular limits"
aliases: ["Carrillo, Craig & Yao 2019", "Aggregation-diffusion equations"]
authors: ["Carrillo J. A.", "Craig K.", "Yao Y."]
year: 2019
url: https://doi.org/10.1007/978-3-030-20297-2_3
tags: [cluster/social-physics, cluster/vfe, project/social-physics, field/mathematics, field/physics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Aggregation-diffusion equations: dynamics, asymptotics, and singular limits

> [!info] Citation
> Carrillo, J. A., Craig, K. & Yao, Y. (2019). *Aggregation-diffusion equations: dynamics, asymptotics, and singular limits*. In Active Particles, Vol. 2 (Birkhäuser/Springer), pp. 65–108. arXiv:1810.03634.

## TL;DR
This is an authoritative review of aggregation-diffusion partial differential equations, the continuum models that arise as mean-field limits of large populations of particles interacting through nonlocal forces while also undergoing local diffusion. The unifying theme is the competition between nonlocal attraction (which concentrates mass) and local repulsion or diffusion (which spreads it out), and the review's organizing principle is that the whole class possesses a gradient-flow structure: solutions evolve as steepest descent of a free-energy functional in the Wasserstein metric. The survey catalogs the resulting phenomenology — steady states, long-time asymptotics, and the dichotomy between global existence and finite-time blow-up — and treats the singular limits connecting different regimes.

## What it establishes
The canonical equation is
$$
\partial_t \rho = \nabla \cdot \bigl( \rho\, \nabla [\, U'(\rho) + W * \rho \,] \bigr),
$$
the Wasserstein gradient flow of the free energy
$$
\mathcal{E}[\rho] = \int U(\rho)\,dx \;+\; \frac{1}{2}\iint W(x-y)\,\rho(x)\,\rho(y)\,dx\,dy,
$$
where the local term $U(\rho)$ encodes diffusion/internal energy and the nonlocal interaction kernel $W$ encodes attraction/repulsion. The review shows how the balance between the convex (diffusive) and concentrating (aggregative) parts of $\mathcal{E}$ determines whether mass disperses, settles into a compactly supported steady state, or collapses to a singular measure in finite time, and it makes the gradient-flow (JKO / minimizing-movement) structure the central analytical tool. This is the continuum image of attraction-versus-noise in an interacting population.

## Relevance to this research
This is the closest continuum analogue to the program's free-energy-functional viewpoint, which is why it carries the cluster/vfe tag. The program treats belief evolution as descent of a variational free energy; aggregation-diffusion equations make exactly that idea precise at the population level by realizing the dynamics as Wasserstein gradient flow of an energy $\mathcal{E}[\rho]$ whose two competing pieces — nonlocal attraction and local diffusion — are the continuum face of consensus-versus-dispersion in a belief population. The mapping is structural and genuinely illuminating: the program's coupling term ($\beta_{ij}$-weighted transported divergences pulling beliefs together) plays the role of the attractive $W * \rho$, while the entropy/noise that keeps beliefs from collapsing plays the role of $U(\rho)$. The honest caveat: the belief state lives on a curved statistical (GL(K)) manifold rather than $\mathbb{R}^d$, so a direct port would require a Wasserstein-gradient-flow formulation over measures on that manifold, with gauge transport in the interaction kernel — a target, not an established identity. See [[Renormalization-group flow of beliefs]], [[Mean-field games and continuum limits]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Renormalization-group flow of beliefs]]
- Related sources: [[carrillo-fornasier-toscani-vecil-2010-particle-kinetic-hydrodynamic-swarming]], [[degond-motsch-2008-continuum-limit-self-driven-particles]]

## BibTeX
```bibtex
@incollection{carrillo2019aggregation,
  author    = {Carrillo, Jos\'e A. and Craig, Katy and Yao, Yao},
  title     = {Aggregation-diffusion equations: dynamics, asymptotics, and singular limits},
  booktitle = {Active Particles, Volume 2},
  publisher = {Birkh\"auser/Springer},
  year      = {2019},
  pages     = {65--108},
  doi       = {10.1007/978-3-030-20297-2_3},
  note      = {arXiv:1810.03634}
}
```
