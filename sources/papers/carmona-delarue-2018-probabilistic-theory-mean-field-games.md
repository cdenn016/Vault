---
type: reference
title: "Probabilistic Theory of Mean Field Games with Applications I & II"
aliases: ["Carmona & Delarue 2018", "Probabilistic Theory of Mean Field Games"]
authors: ["Carmona R.", "Delarue F."]
year: 2018
url: https://doi.org/10.1007/978-3-319-58920-6
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/economics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Probabilistic Theory of Mean Field Games with Applications I & II

> [!info] Citation
> Carmona, R. & Delarue, F. (2018). *Probabilistic Theory of Mean Field Games with Applications I & II*. Probability Theory and Stochastic Modelling, Vols. 83 & 84, Springer. DOI: 10.1007/978-3-319-58920-6 (Vol. I) and 10.1007/978-3-319-56436-4 (Vol. II).

## TL;DR
This is the definitive two-volume monograph on mean field games developed through the probabilistic, rather than the analytic-PDE, lens. Instead of working directly with the Hamilton–Jacobi–Bellman / Fokker–Planck pair, Carmona and Delarue formulate the representative-agent equilibrium via forward–backward stochastic differential equations (FBSDEs) of McKean–Vlasov type, where the dynamics depend on the law of the solution itself. Volume I builds the underlying stochastic-control and mean-field-SDE machinery and establishes existence/uniqueness of equilibria; Volume II extends to common noise, the master equation on the space of probability measures, and the rigorous convergence of $N$-player Nash equilibria to the mean field limit.

## What it establishes
The probabilistic equilibrium is cast as a McKean–Vlasov FBSDE,
$$
dX_t = b\bigl(X_t, \mathcal{L}(X_t), \alpha_t\bigr)\,dt + \sigma\,dW_t, \qquad
dY_t = -f\bigl(X_t, \mathcal{L}(X_t), \alpha_t\bigr)\,dt + Z_t\,dW_t,
$$
where $\mathcal{L}(X_t)$ is the law of the state and the optimal control $\alpha_t$ is recovered from the adjoint $(Y_t, Z_t)$ via the stochastic maximum principle; the fixed-point requirement is that the controlled law reproduce the $\mathcal{L}(X_t)$ used in the coefficients. The monograph develops the master equation — a PDE on the Wasserstein space $\mathcal{P}_2(\mathbb{R}^d)$ whose characteristics are the FBSDE — and proves, with quantitative rates, that finite-$N$ Nash equilibria converge to the mean field solution. It is the authoritative repository of the McKean–Vlasov SDE, common-noise, and master-equation tools.

## Relevance to this research
This is the reference-shelf canon for the rigorous MFG side of the continuum-limit story, not machinery the belief-inertia functional currently uses. Its value to the program is as the home of the probabilistic tools — McKean–Vlasov SDEs and the master equation on measure space — that any genuinely rigorous representative-belief-agent limit would need: if the program wants to prove that its finite population of VFE agents converges to a continuum belief field, the convergence-of-Nash-equilibria and master-equation results here are the template. The honest framing: this is reference canon for *how to make the limit rigorous*, adjacent to rather than embedded in the program's current derivations, which proceed through free-energy gradient flow and meta-entropy configuration counting rather than FBSDEs. See [[Mean-field games and continuum limits]], [[Multi-agent variational free energy]], [[Meta-entropy]].

## Cross-links
- Concept: [[Mean-field games and continuum limits]]
- Related sources: [[lasry-lions-2007-mean-field-games]], [[huang-malhame-caines-2006-nash-certainty-equivalence]], [[cardaliaguet-2013-notes-on-mean-field-games]]

## BibTeX
```bibtex
@book{carmona2018probabilistic,
  author    = {Carmona, Ren\'e and Delarue, Fran\c{c}ois},
  title     = {Probabilistic Theory of Mean Field Games with Applications I \& II},
  series    = {Probability Theory and Stochastic Modelling},
  volume    = {83 and 84},
  publisher = {Springer},
  year      = {2018},
  doi       = {10.1007/978-3-319-58920-6}
}
```
