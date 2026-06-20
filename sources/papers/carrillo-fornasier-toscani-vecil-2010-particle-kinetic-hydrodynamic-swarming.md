---
type: reference
title: "Particle, kinetic, and hydrodynamic models of swarming"
aliases: ["Carrillo, Fornasier, Toscani & Vecil 2010", "Particle, kinetic, and hydrodynamic models of swarming"]
authors: ["Carrillo J. A.", "Fornasier M.", "Toscani G.", "Vecil F."]
year: 2010
url: https://doi.org/10.1007/978-0-8176-4946-3_12
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, field/biology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Particle, kinetic, and hydrodynamic models of swarming

> [!info] Citation
> Carrillo, J. A., Fornasier, M., Toscani, G. & Vecil, F. (2010). *Particle, kinetic, and hydrodynamic models of swarming*. In Mathematical Modeling of Collective Behavior in Socio-Economic and Life Sciences (Birkhäuser, Boston), pp. 297–336. DOI: 10.1007/978-0-8176-4946-3_12.

## TL;DR
This survey lays out the three-level modeling hierarchy for swarming and collective behavior and the asymptotic limits that connect the levels. At the bottom are individual-based (particle) models — ordinary differential equations for each agent's position and velocity under self-propulsion, friction, and pairwise attraction–repulsion. Averaging over many agents gives the kinetic (mean-field) description, a Vlasov-type equation for the one-particle distribution. A further hydrodynamic scaling produces macroscopic equations for density and momentum. The survey's value is in presenting all three levels with a common notation and explaining which limit produces which model, making the multiscale tower of collective behavior coherent in one place.

## What it establishes
The canonical particle model has the second-order form
$$
\dot{x}_i = v_i, \qquad
\dot{v}_i = (\alpha - \beta\,\lVert v_i\rVert^2)\,v_i - \frac{1}{N}\sum_{j\ne i}\nabla U(\lVert x_i - x_j\rVert),
$$
combining a self-propulsion/friction term (the Cucker-Smale-type or Rayleigh–Helmholtz term) with a gradient of a pairwise interaction potential $U$ (Morse-type attraction–repulsion). The mean-field limit sends this to a Vlasov equation $\partial_t f + v\cdot\nabla_x f + \nabla_v\cdot(F[f]\,f) = 0$ with the self-consistent force $F[f]$, and the hydrodynamic limit yields Euler-type equations for $\rho$ and the mean velocity. The survey catalogs the patterns (mills, flocks, double mills) these models produce and the rigorous and formal limits linking the scales.

## Relevance to this research
This is adjacent but genuinely valuable: the clearest single exposition of the multiscale tower (micro → kinetic → macro) that the program's Ouroboros coarse-graining and meta-agent hierarchy mirror. Where the survey passes from individual particles to a kinetic field to a hydrodynamic description through rigorous limits, the program stacks single-scale VFE functionals into a tower whose scale-$s+1$ meta-agents are gauge-covariant coarse-grainings of scale-$s$ clusters; the survey frames how such a scale tower could be organized with principled inter-scale limits rather than ad hoc pooling. It is the right reference for understanding what "doing the coarse-graining rigorously" would demand. The honest caveat: the swarming hierarchy coarse-grains over physical positions and velocities in $\mathbb{R}^d$, whereas the program coarse-grains beliefs on a GL(K) fibre bundle with gauge transport and coherence-weighted pooling; the kinship is in the three-level architecture and the limit-based philosophy, not in shared equations. See [[Meta-agents and hierarchical emergence]], [[Mean-field games and continuum limits]], [[Renormalization-group flow of beliefs]].

## Cross-links
- Concept: [[Meta-agents and hierarchical emergence]]
- Related sources: [[carrillo-craig-yao-2019-aggregation-diffusion-equations]], [[degond-motsch-2008-continuum-limit-self-driven-particles]], [[motsch-tadmor-2014-heterophilious-dynamics-consensus]]

## BibTeX
```bibtex
@incollection{carrillo2010particle,
  author    = {Carrillo, Jos\'e A. and Fornasier, Massimo and Toscani, Giuseppe and Vecil, Francesco},
  title     = {Particle, kinetic, and hydrodynamic models of swarming},
  booktitle = {Mathematical Modeling of Collective Behavior in Socio-Economic and Life Sciences},
  publisher = {Birkh\"auser, Boston},
  year      = {2010},
  pages     = {297--336},
  doi       = {10.1007/978-0-8176-4946-3_12}
}
```
