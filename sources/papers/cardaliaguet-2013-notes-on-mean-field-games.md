---
type: reference
title: "Notes on mean field games (from P.-L. Lions' lectures at Collège de France)"
aliases: ["Cardaliaguet 2013", "Notes on Mean Field Games"]
authors: ["Cardaliaguet P."]
year: 2013
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/economics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Notes on mean field games (from P.-L. Lions' lectures at Collège de France)

> [!info] Citation
> Cardaliaguet, P. (2013). *Notes on mean field games (from P.-L. Lions' lectures at Collège de France)*. Lecture notes, CEREMADE / Université Paris-Dauphine (canonical PDF at ceremade.dauphine.fr/~cardaliaguet).

## TL;DR
These are the widely used pedagogical lecture notes that systematized the analytic theory of mean field games from Pierre-Louis Lions' lectures at the Collège de France. They give a self-contained, careful derivation of the coupled Hamilton–Jacobi–Bellman / Fokker–Planck system, prove existence of solutions, and lay out the monotonicity structure that yields uniqueness. For more than a decade they have served as the standard entry point into MFG analysis for newcomers, because they organize the heuristics (the $N\to\infty$ decoupling of a symmetric game) and the rigorous PDE arguments in one place.

## What it establishes
The notes derive and analyze the stationary and time-dependent MFG systems, in the time-dependent case the forward–backward pair
$$
\begin{aligned}
-\partial_t u - \Delta u + H(x,\nabla u) &= F(x,m), \\
\partial_t m - \Delta m - \operatorname{div}\!\bigl(m\,\partial_p H(x,\nabla u)\bigr) &= 0,
\end{aligned}
$$
with $u(\cdot,T)$ and $m(\cdot,0)$ given. The cleanest contribution for the working reader is the explicit statement and use of the Lasry–Lions monotonicity condition: when the coupling $F(\cdot,m)$ is monotone (increasing) in $m$, a comparison/energy argument shows the equilibrium is unique. The notes also treat the heuristic derivation from $N$-player games, regularity of solutions, and the variational (potential MFG) case where the system is the optimality condition of a single convex functional over densities.

## Relevance to this research
This is adjacent reference value: the standard, most accessible bridge for anyone in the program learning the continuum-control formalism, rather than machinery the belief-inertia functional itself uses. Its specific usefulness is the clean statement of the monotonicity (Lasry–Lions) condition guaranteeing a unique consensus-like equilibrium — the condition the program would need to check if it wants to argue that its VFE-derived mean-field coupling has a unique fixed point rather than multiple polarized equilibria. The notes' treatment of the *potential/variational* MFG case is also the most relevant point of contact, since that is the regime where the forward–backward system is the Euler–Lagrange condition of a single functional, mirroring the program's free-energy-functional stance. Honest framing: a pedagogical gateway and a source for the uniqueness condition, not a result the program builds on directly. See [[Mean-field games and continuum limits]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Mean-field games and continuum limits]]
- Related sources: [[lasry-lions-2007-mean-field-games]], [[carmona-delarue-2018-probabilistic-theory-mean-field-games]], [[huang-malhame-caines-2006-nash-certainty-equivalence]]

## BibTeX
```bibtex
@misc{cardaliaguet2013notes,
  author = {Cardaliaguet, Pierre},
  title  = {Notes on Mean Field Games (from P.-L. Lions' lectures at Coll\`ege de France)},
  year   = {2013},
  note   = {Lecture notes, CEREMADE / Universit\'e Paris-Dauphine},
  howpublished = {\url{https://www.ceremade.dauphine.fr/~cardaliaguet/MFG20130420.pdf}}
}
```
