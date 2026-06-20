---
type: paper
title: "Long-Range Order in a Two-Dimensional Dynamical XY Model: How Birds Fly Together"
aliases: ["Toner & Tu 1995", "Toner-Tu flocking hydrodynamics"]
authors: ["Toner J.", "Tu Y."]
year: 1995
url: https://doi.org/10.1103/PhysRevLett.75.4326
tags: [cluster/social-physics, project/social-physics, field/physics, field/biology, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Long-Range Order in a Two-Dimensional Dynamical XY Model: How Birds Fly Together

> [!info] Citation
> Toner, J., & Tu, Y. (1995). *Long-Range Order in a Two-Dimensional Dynamical XY Model: How Birds Fly Together*. Physical Review Letters, 75(23), 4326–4329. DOI 10.1103/PhysRevLett.75.4326.

## TL;DR
Toner and Tu derive the continuum hydrodynamic theory of flocking — the coarse-grained field theory whose microscopic origin is the Vicsek model — and prove a striking result: self-propelled flocks can sustain true long-range orientational order even in two dimensions. This violates the equilibrium Mermin–Wagner theorem, which forbids spontaneous breaking of a continuous symmetry in 2D; the violation is possible precisely because the flock is a driven, nonequilibrium system in which advective nonlinearities suppress the destructive fluctuations.

## What it establishes
Coarse-graining the discrete alignment dynamics yields equations of motion for a coarse density $\rho(\mathbf{r},t)$ and a velocity (polarization) field $\mathbf{v}(\mathbf{r},t)$, schematically
$$ \partial_t \mathbf{v} + \lambda(\mathbf{v}\cdot\nabla)\mathbf{v} = \alpha\mathbf{v} - \beta|\mathbf{v}|^2\mathbf{v} - \nabla P + D\nabla^2\mathbf{v} + \mathbf{f}, \qquad \partial_t\rho + \nabla\cdot(\rho\mathbf{v}) = 0, $$
where the $\alpha,\beta$ terms drive a nonzero mean speed (broken rotational symmetry), $P(\rho)$ is a pressure, and $\mathbf{f}$ is noise. The advective term $\lambda(\mathbf{v}\cdot\nabla)\mathbf{v}$ is absent in equilibrium XY models and is what stabilizes long-range order in 2D. A dynamical renormalization-group analysis yields anomalous scaling exponents for the velocity and density fluctuations, establishing flocking as a distinct nonequilibrium universality class.

## Relevance to this research
This is the continuum field theory of collective motion and the rigorous coarse-graining of microscopic alignment rules into an order-parameter field, which makes it the natural physics template for the program's renormalization-group coarse-graining of beliefs from discrete agents to a continuum order parameter. The explicit use of dynamical RG to extract scaling exponents is directly relevant to the program's meta-entropy / continuum-limit machinery and its [[Renormalization-group flow of beliefs]]. The relevance is methodological and strong on the coarse-graining side, while the specific advective hydrodynamics is an analogy rather than an equation the belief functional contains. See [[Renormalization-group flow of beliefs]], [[Collective motion and flocking]], [[Meta-entropy]].

## Cross-links
- Concept: [[Renormalization-group flow of beliefs]]
- Related sources: [[vicsek-1995-self-driven-particles]], [[vicsek-zafeiris-2012-collective-motion]], [[bialek-2012-statistical-mechanics-flocks]]

## BibTeX
```bibtex
@article{toner1995longrange,
  author  = {Toner, John and Tu, Yuhai},
  title   = {Long-Range Order in a Two-Dimensional Dynamical XY Model: How Birds Fly Together},
  journal = {Physical Review Letters},
  volume  = {75},
  number  = {23},
  pages   = {4326--4329},
  year    = {1995},
  doi     = {10.1103/PhysRevLett.75.4326}
}
```
