---
type: paper
title: "Continuum dynamics of the intention field under weakly cohesive social interaction"
aliases: ["Degond, Liu, Merino-Aceituno & Tardiveau 2017", "Intention field continuum dynamics"]
authors: ["Degond P.", "Liu J.-G.", "Merino-Aceituno S.", "Tardiveau T."]
year: 2017
url: https://doi.org/10.1142/S021820251740005X
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Continuum dynamics of the intention field under weakly cohesive social interaction

> [!info] Citation
> Degond, P., Liu, J.-G., Merino-Aceituno, S. & Tardiveau, T. (2017). *Continuum dynamics of the intention field under weakly cohesive social interaction*. Mathematical Models and Methods in Applied Sciences, 27(1), 159–182. DOI: 10.1142/S021820251740005X; arXiv:1607.06372.

## TL;DR
This paper derives the macroscopic evolution of a mean opinion/intention field directly from individual-level social interactions, in the regime where those interactions are weakly cohesive. Starting from a stochastic agent model in which each individual carries an "intention" variable and is gently pulled toward the local social consensus, the authors take a grazing-collision (small-jump, high-frequency) limit that reduces the kinetic description to a Fokker–Planck equation, and then extract the continuum dynamics of the mean intention field. The analysis characterizes the equilibria of this field, including nontrivial (non-uniform) ones, showing how weak cohesion can still organize the population into structured opinion states.

## What it establishes
The micro model is coarse-grained through a grazing-collision asymptotic into a Fokker–Planck equation for the one-particle distribution $f(x, \omega, t)$ over intention $\omega$, of schematic form
$$
\partial_t f + \dots = \nabla_\omega \cdot \bigl[ \, D\,\nabla_\omega f + (\omega - \Omega[f])\, f \,\bigr],
$$
where $\Omega[f]$ is the locally averaged (consensus) intention and $D$ the diffusion from individual fluctuation. In the weakly cohesive scaling the paper closes this into an evolution equation for the macroscopic mean intention field and analyzes its equilibrium manifold, identifying conditions under which the trivial uniform state loses stability and structured equilibria appear. It is a complete kinetic-to-macroscopic derivation of an opinion field with explicit characterization of the resulting steady states.

## Relevance to this research
This is the strongest single template in the batch for what a belief-field continuum equation derived from the VFE micro-model should look like. The object of study — a continuum "intention field" produced from weakly cohesive individual interactions via a kinetic-to-macroscopic reduction — is essentially the program's own target: the continuum belief field obtained from a population of locally coupled VFE agents. The grazing-collision Fokker–Planck route is directly analogous to how a population of small, frequent belief updates ($\beta_{ij}$-weighted transported pulls toward neighbors) would aggregate into a continuum equation for the mean belief, and the paper's equilibrium analysis is the kind of consensus-versus-structured-state characterization the program needs. The honest caveat: the intention variable here lives on a simple state space and the cohesion is a plain attraction, whereas the program's beliefs are Gaussian tuples on a GL(K) manifold coupled through gauge-transported KL divergences; Degond et al. supply the derivation pattern and the equilibrium-analysis style, not a ready-made belief-field PDE. See [[Opinion dynamics]], [[Mean-field games and continuum limits]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Opinion dynamics]]
- Related sources: [[degond-motsch-2008-continuum-limit-self-driven-particles]], [[motsch-tadmor-2014-heterophilious-dynamics-consensus]]

## BibTeX
```bibtex
@article{degond2017continuum,
  author  = {Degond, Pierre and Liu, Jian-Guo and Merino-Aceituno, Sara and Tardiveau, Thomas},
  title   = {Continuum dynamics of the intention field under weakly cohesive social interaction},
  journal = {Mathematical Models and Methods in Applied Sciences},
  year    = {2017},
  volume  = {27},
  number  = {1},
  pages   = {159--182},
  doi     = {10.1142/S021820251740005X},
  note    = {arXiv:1607.06372}
}
```
