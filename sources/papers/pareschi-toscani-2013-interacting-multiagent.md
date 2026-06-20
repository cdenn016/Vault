---
type: reference
title: "Interacting Multiagent Systems: Kinetic Equations and Monte Carlo Methods"
aliases: ["Pareschi & Toscani 2013", "Interacting Multiagent Systems (book)"]
authors: ["Pareschi L.", "Toscani G."]
year: 2013
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Interacting Multiagent Systems: Kinetic Equations and Monte Carlo Methods

> [!info] Citation
> Pareschi, L. & Toscani, G. (2013). *Interacting Multiagent Systems: Kinetic Equations and Monte Carlo Methods*. Oxford University Press (ISBN 9780199655465).

## TL;DR
This is the authoritative monograph for the kinetic theory of large interacting-agent systems. It develops, from the ground up, how microscopic binary-interaction rules over a population of many agents pass — in the limit of many agents — to mean-field Boltzmann-type and Fokker-Planck partial differential equations for the one-agent density, and it lays out the Monte Carlo (Direct Simulation Monte Carlo, DSMC-style) numerical machinery for solving them efficiently. The same formalism is applied across opinion formation, wealth and economic exchange, traffic and crowd flow, and collective animal behavior, presenting them as instances of one kinetic methodology rather than disconnected models.

## What it establishes
The central object is the evolution of a density $f(x,t)$ of agents over a state variable $x$ (an opinion, a wealth, a velocity). Agents update through conservative or near-conservative binary interactions $(x,x_*) \to (x',x'_*)$, and the density obeys a Boltzmann-type equation of the schematic form
$$ \partial_t f(x,t) = Q(f,f)(x,t), $$
where $Q$ is a bilinear collision operator integrating over interaction partners. In the **grazing / quasi-invariant limit** — small individual interaction strength accumulated over many encounters — $Q$ reduces to a nonlinear Fokker-Planck operator
$$ \partial_t f = \partial_x\!\big[ \mathcal{B}[f]\, f \big] + \tfrac{1}{2}\,\partial_x^2\!\big[ D(x)\, f \big], $$
with a drift encoding average compromise toward consensus and a diffusion encoding the stochastic spread of individual updates. The book gives the conditions for mass and momentum conservation, computes stationary states in closed form for canonical models, and pairs each PDE with a stochastic-particle Monte Carlo solver whose cost scales favorably with population size.

## Relevance to this research
This is the reference textbook for the entire kinetic-opinion lineage and supplies the methodological backbone the SocialPhysics program needs for any thermodynamic-limit argument. The microscopic-to-mean-field passage it formalizes — finite population of pairwise-updating agents to a continuum density obeying a PDE — is exactly the $N \to \infty$ limit the program's meta-entropy / configuration-counting bridge invokes for the gauge-VFE belief population. The overdamped first-order regime of [[Belief inertia]] is the gradient-flow analogue of the compromise-plus-noise Fokker-Planck structure derived here. Honestly, the book is methodological scaffolding rather than machinery the VFE functional itself uses: it operates on scalar opinions in a flat state space, not on Gaussian beliefs $(\mu,\Sigma,\phi)$ on an information-geometric fibre bundle, so the gauge transport $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$ has no counterpart here. Its value is as the rigorous continuum-limit template against which the program must justify its own mean-field claims.

## Cross-links
- Concept: [[Kinetic theory of opinion dynamics]]
- Related sources: [[toscani-2006-kinetic-opinion]], [[albi-2017-recent-advances-opinion-modeling]], [[cordier-pareschi-toscani-2005-kinetic-market]]

## BibTeX
```bibtex
@book{pareschi2013interacting,
  author    = {Pareschi, Lorenzo and Toscani, Giuseppe},
  title     = {Interacting Multiagent Systems: Kinetic Equations and Monte Carlo Methods},
  publisher = {Oxford University Press},
  year      = {2013},
  isbn      = {9780199655465}
}
```
