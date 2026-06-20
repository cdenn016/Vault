---
type: reference
title: "A Kinetic View of Statistical Physics"
aliases: ["Krapivsky, Redner & Ben-Naim 2010", "A Kinetic View of Statistical Physics"]
authors: ["Krapivsky P. L.", "Redner S.", "Ben-Naim E."]
year: 2010
url: https://doi.org/10.1017/CBO9780511780516
tags: [cluster/social-physics, cluster/vfe, project/social-physics, field/physics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# A Kinetic View of Statistical Physics

> [!info] Citation
> Krapivsky, P. L., Redner, S., & Ben-Naim, E. (2010). *A Kinetic View of Statistical Physics*. Cambridge University Press. ISBN 978-0-521-85103-9.

## TL;DR
A graduate textbook on nonequilibrium statistical physics organized around kinetic, time-dependent thinking rather than equilibrium ensembles. It develops the master-equation and rate-equation toolkit for a wide range of stochastic many-body processes — random walks, aggregation and fragmentation, coarsening, reaction-diffusion, spin dynamics, and population models — and applies the same analytical machinery (mean-field rate equations, scaling and self-similarity, exact one-dimensional solutions, and asymptotic analysis) throughout. Notably for this program, it treats the voter model, coarsening spin systems, and related opinion-like dynamics directly, deriving their consensus times and coarsening laws from first principles.

## What it establishes
The book's unifying object is the master equation for the probability of a configuration, $\partial_t P(\sigma,t) = \sum_{\sigma'}[W_{\sigma'\to\sigma}P(\sigma',t) - W_{\sigma\to\sigma'}P(\sigma,t)]$, and its mean-field reduction to closed rate equations for densities and moments. Using these, the authors derive the coarsening dynamics of the voter and Ising-Glauber models, the growth of correlated domains, the dimension dependence of consensus, and the scaling forms of cluster-size distributions. The methodological emphasis is on extracting universal large-time, large-scale behaviour — the continuum and thermodynamic limits — from microscopic stochastic rules, including the configuration-counting and extensivity arguments that bridge discrete particle systems to continuum field descriptions.

## Relevance to this research
This is the authoritative analytical toolkit behind the discrete opinion models in this batch: it provides the master equations, mean-field rate equations, and coarsening analysis needed to derive their continuum and thermodynamic limits. That continuum/extensivity bridge is precisely what the program's meta-entropy and renormalization-group-coarse-graining strands pursue — passing from a finite population of discrete agents to a continuum free-energy description, with configuration-counting underwriting the extensivity (Kac-style) arguments the meta-entropy note tracks. Honestly, this is a reference textbook supplying standard machinery rather than a result the belief-inertia functional uses; its role is to give the program rigorous, off-the-shelf methods for taking the limits its claims of subsumption require. See [[Meta-entropy]], [[Renormalization-group flow of beliefs]], [[Voter model]].

## Cross-links
- Concept: [[Kinetic theory of opinion dynamics]]
- Related sources: [[noorazar-2020-opinion-dynamics-survey]], [[holley-liggett-1975-voter-model-ergodic]]

## BibTeX
```bibtex
@book{krapivsky2010kinetic,
  author    = {Krapivsky, Pavel L. and Redner, Sidney and Ben-Naim, Eli},
  title     = {A Kinetic View of Statistical Physics},
  publisher = {Cambridge University Press},
  year      = {2010},
  isbn      = {978-0-521-85103-9}
}
```
