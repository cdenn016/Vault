---
type: paper
title: "Boltzmann and Fokker-Planck Equations Modelling Opinion Formation in the Presence of Strong Leaders"
aliases: ["Düring et al. 2009", "Opinion Formation with Strong Leaders"]
authors: ["Düring B.", "Markowich P. A.", "Pietschmann J.-F.", "Wolfram M.-T."]
year: 2009
url: https://doi.org/10.1098/rspa.2009.0239
tags: [cluster/social-physics, project/social-physics, field/mathematics, field/physics, field/sociology, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Boltzmann and Fokker-Planck Equations Modelling Opinion Formation in the Presence of Strong Leaders

> [!info] Citation
> Düring, B., Markowich, P. A., Pietschmann, J.-F. & Wolfram, M.-T. (2009). *Boltzmann and Fokker-Planck Equations Modelling Opinion Formation in the Presence of Strong Leaders*. Proceedings of the Royal Society A **465**(2112), 3687–3708. DOI: [10.1098/rspa.2009.0239](https://doi.org/10.1098/rspa.2009.0239).

## TL;DR
A kinetic model of opinion formation in a society split into two interacting populations: an ordinary mass of agents and a small set of **strong leaders** whose opinions are influential and comparatively rigid. The authors write coupled Boltzmann-type equations for the two opinion densities, with leader-follower, follower-follower, and leader-leader interaction kernels having different compromise and noise parameters, and pass to the quasi-invariant (grazing) limit to obtain coupled Fokker-Planck equations. They analyze the resulting stationary opinion distributions and show how the leaders bias and concentrate the followers' opinions, including regimes where leaders successfully drive consensus and regimes of persistent disagreement.

## What it establishes
Let $f(w,t)$ be the followers' opinion density and $g(w,t)$ the leaders' density on $w\in[-1,1]$. Each evolves by a Boltzmann equation summing the relevant interaction channels,
$$ \partial_t f = Q(f,f) + Q(f,g), \qquad \partial_t g = Q(g,g) + Q(g,f), $$
where the cross-term $Q(f,g)$ encodes asymmetric influence: leaders pull followers strongly, followers pull leaders weakly. The grazing limit yields a coupled nonlinear Fokker-Planck system with drift terms reflecting the asymmetric compromise and diffusion terms reflecting opinion noise (larger for followers, smaller for resolute leaders). Stationary states are computed numerically; the leader population's mean opinion acts as a moving attractor for the follower density, and the steady follower distribution concentrates around it when leader influence dominates noise.

## Relevance to this research
This is a clean kinetic-theory treatment of heterogeneous influence — leaders versus followers — which is the continuum counterpart of the program's anchoring and asymmetric attention weights. The leader-follower asymmetric kernel is the mean-field analogue of an attention matrix $\beta_{ij}$ that is deliberately non-symmetric, with a sparse set of agents receiving large incoming weight, and it is the PDE-level model the program can compare against when it argues its multi-scale **meta-agents act as continuum leaders** steering a population through transported shadow priors. The asymmetric, near-rigid leaders also gesture at the high-precision / high-inertia limit of [[Belief inertia]]. Honestly the link is by structural analogy: the leaders here have no gauge frame and the dynamics is first-order overdamped, so this is a comparison target and a heterogeneity reference, not a component of the VFE functional.

## Cross-links
- Concept: [[Kinetic theory of opinion dynamics]]
- Related sources: [[toscani-2006-kinetic-opinion]], [[albi-2017-recent-advances-opinion-modeling]], [[boudin-salvarani-2009-kinetic-opinion]]

## BibTeX
```bibtex
@article{during2009boltzmann,
  author  = {D\"{u}ring, Bertram and Markowich, Peter A. and Pietschmann, Jan-Frederik and Wolfram, Marie-Therese},
  title   = {Boltzmann and Fokker-Planck Equations Modelling Opinion Formation in the Presence of Strong Leaders},
  journal = {Proceedings of the Royal Society A},
  volume  = {465},
  number  = {2112},
  pages   = {3687--3708},
  year    = {2009},
  doi     = {10.1098/rspa.2009.0239}
}
```
