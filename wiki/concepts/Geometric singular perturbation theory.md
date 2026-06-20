---
type: concept
title: "Geometric singular perturbation theory"
aliases:
  - "GSPT"
  - "Fenichel theory"
  - "Slow manifold reduction"
  - "Fast-slow systems"
  - "Singular perturbation"
tags:
  - cluster/methodology
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-19
updated: 2026-06-19
---

# Geometric singular perturbation theory

## Definition

**Geometric singular perturbation theory (GSPT)** is the dynamical-systems framework, due principally to Fenichel, for analyzing systems that evolve on two widely separated timescales. A fast-slow system in standard form reads $\dot x = f(x,y,\epsilon)$, $\dot y = \epsilon\,g(x,y,\epsilon)$, where $x$ are fast variables, $y$ are slow variables, and $0<\epsilon\ll 1$ measures the timescale ratio. Setting $\epsilon=0$ collapses the fast dynamics onto the **critical manifold** $\mathcal{M}_0 = \{f(x,y,0)=0\}$, the locus where the fast subsystem is at equilibrium. Fenichel's invariant-manifold theorems state that whenever $\mathcal{M}_0$ is *normally hyperbolic* — the eigenvalues of $\partial f/\partial x$ stay bounded away from the imaginary axis — there exists, for sufficiently small $\epsilon>0$, a nearby **slow manifold** $\mathcal{M}_\epsilon$ that is locally invariant, $O(\epsilon)$-close to $\mathcal{M}_0$, and inherits its smoothness and stable/unstable foliation. The full flow is then rigorously reducible to the lower-dimensional slow flow restricted to $\mathcal{M}_\epsilon$, with the fast directions slaved to it.

## Why it matters here

GSPT is the mathematical backbone of the timescale separation that organizes the entire [[participatory-it-from-bit]] program. The model's **fast E-step / slow M-step** split (see CLAUDE.md "Timescales") is exactly a fast-slow system: belief inference $q=(\mu,\Sigma,\phi)$ relaxes quickly within each forward pass (the fast $x$), while prior/model parameters $(p,s)$ and gauge couplings drift slowly under backprop (the slow $y$). Fenichel theory is what licenses treating the E-step as having reached its slow manifold — the variational fixed point — before the M-step takes a step, rather than this being a mere computational convenience. The same logic underwrites the **Schur-complement parent flow** in [[Ouroboros multi-scale dynamics]]: coarse-graining a cluster of fast constituent agents into a slow meta-agent is an adiabatic elimination of fast degrees of freedom, and the parent's effective dynamics are the slow flow obtained after the fast block equilibrates (the Schur complement is the algebraic shadow of integrating out the fast sub-block). Across scales this is precisely the picture [[Renormalization-group flow of beliefs]] formalizes: each blocking step eliminates a normally-hyperbolic fast manifold and reads off the slow effective theory.

## Details

Normal hyperbolicity is the load-bearing hypothesis: where it fails (fold points, canards, bifurcations of the critical manifold) the simple slow reduction breaks and richer behavior appears, which flags exactly where the E-step's "instantaneous equilibration" assumption could be unsafe. The asymptotic-integral methods of [[wong-2001-asymptotic-integrals]] and [[bender-orszag-1999-asymptotic-methods]] are the complementary analytic toolkit: Laplace's method, the method of steepest descent, matched asymptotic expansions, and WKB give the $\epsilon$-expansions that evaluate the closure integrals appearing when fast modes are integrated out, supplying the leading-order corrections to the slow flow and to the RG-closure of belief couplings. Together they connect the inertial, second-order belief dynamics of [[Hamiltonian belief dynamics]] (where a precision-as-mass term sets the natural fast/slow ratio) to a controlled reduction rather than an ad hoc separation.

## Sources

- [[fenichel-1979-geometric-singular-perturbation]] — Fenichel's invariant-manifold theorems: existence, persistence, and smoothness of the slow manifold under normal hyperbolicity; the rigorous justification of fast-slow reduction.
- [[wong-2001-asymptotic-integrals]] — Laplace/steepest-descent asymptotics of integrals, supporting the RG-closure integral evaluations.
- [[bender-orszag-1999-asymptotic-methods]] — matched asymptotics, boundary layers, and WKB for singularly perturbed problems; the practical $\epsilon$-expansion machinery.

## See also

- [[Renormalization-group flow of beliefs]]
- [[Hamiltonian belief dynamics]]
- [[Ouroboros multi-scale dynamics]]
- [[participatory-it-from-bit]]
