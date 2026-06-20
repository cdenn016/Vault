---
type: paper
title: "Mean field games"
aliases: ["Lasry & Lions 2007", "Lasry-Lions mean field games"]
authors: ["Lasry J.-M.", "Lions P.-L."]
year: 2007
url: https://doi.org/10.1007/s11537-007-0657-8
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/economics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Mean field games

> [!info] Citation
> Lasry, J.-M. & Lions, P.-L. (2007). *Mean field games*. Japanese Journal of Mathematics, 2(1), 229–260. DOI: 10.1007/s11537-007-0657-8.

## TL;DR
This is the founding mathematical paper of mean field games. Lasry and Lions consider a continuum of identical rational agents, each choosing a control to minimize its own cost, where the only coupling between agents is through the statistical distribution of the whole population. In the $N \to \infty$ limit an individual agent has negligible effect on the aggregate, so each agent best-responds to a *fixed* population distribution; demanding that the distribution produced by all agents' optimal play coincide with the one they responded to yields a coupled pair of partial differential equations. The forward equation transports the population mass; the backward equation propagates each agent's optimal value function. The paper also isolates a monotonicity condition under which the equilibrium is unique.

## What it establishes
The equilibrium of the continuum game is characterized by the coupled forward–backward MFG system: a backward Hamilton–Jacobi–Bellman equation for the value $u(x,t)$ and a forward Fokker–Planck (Kolmogorov) equation for the density $m(x,t)$,
$$
\begin{aligned}
-\partial_t u - \nu\,\Delta u + H(x, \nabla u) &= f(x, m), \\
\partial_t m - \nu\,\Delta m - \operatorname{div}\!\bigl(m\,\partial_p H(x,\nabla u)\bigr) &= 0,
\end{aligned}
$$
with $u$ specified at the terminal time and $m$ at the initial time. The HJB equation gives each agent's optimal feedback through $\nabla u$; the Fokker–Planck equation pushes the mass forward under that optimal drift. Existence follows from fixed-point/PDE arguments, and the Lasry–Lions monotonicity condition (the coupling $f(x,m)$ increasing in $m$, penalizing crowding) yields uniqueness of the equilibrium. The system is the rigorous $N\to\infty$ closure of a population of optimally controlled, mass-coupled agents.

## Relevance to this research
This is the mathematical home of the thermodynamic-limit side of belief-inertia. The forward–backward MFG pair is the rigorous $N\to\infty$ analogue of a population of VFE agents whose individual control couples only through the aggregate belief distribution: the Fokker–Planck equation is exactly the evolution of the belief-density field, and the HJB equation is the variational/optimality side that the program's free-energy minimization would supply. The program's mean-field continuum should be positioned explicitly against this canon, including the question of whether a VFE-derived coupling satisfies a Lasry–Lions-type monotonicity that would guarantee a unique consensus equilibrium. The honest distinction: MFG is built on optimal control with an exogenous cost and a Hamiltonian, whereas the program's dynamics descend from a free-energy gradient flow with gauge-transported divergences; the correspondence is structural (forward density transport plus backward optimality) rather than a term-by-term identity. See [[Mean-field games and continuum limits]], [[Multi-agent variational free energy]], [[Renormalization-group flow of beliefs]].

## Cross-links
- Concept: [[Mean-field games and continuum limits]]
- Related sources: [[huang-malhame-caines-2006-nash-certainty-equivalence]], [[cardaliaguet-2013-notes-on-mean-field-games]], [[carmona-delarue-2018-probabilistic-theory-mean-field-games]]

## BibTeX
```bibtex
@article{lasry2007mean,
  author  = {Lasry, Jean-Michel and Lions, Pierre-Louis},
  title   = {Mean field games},
  journal = {Japanese Journal of Mathematics},
  year    = {2007},
  volume  = {2},
  number  = {1},
  pages   = {229--260},
  doi     = {10.1007/s11537-007-0657-8}
}
```
