---
type: concept
title: "Physics from Fisher information"
aliases:
  - "Extreme Physical Information"
  - "EPI"
  - "Fisher-information physics"
  - "Entropic dynamics"
  - "Physics from information geometry"
tags:
  - cluster/info-geometry
  - cluster/participatory
  - project/multi-agent
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Physics from Fisher information

## Definition

**Physics from Fisher information** names a family of research programs that attempt to *derive* (or at least strongly constrain) the equations of physics by extremizing or constraining an information measure — most often the Fisher information of a probability distribution, sometimes the Shannon/Gibbs entropy. The unifying claim is inferential rather than mechanical: the form of a physical law is read off from a variational principle on a statistical manifold, with the [[Fisher information metric]] supplying the relevant geometry. Four strands are canonical. Frieden's **Extreme Physical Information (EPI)** posits a universal principle $K = I - J \to \text{extremum}$, where $I$ is the Fisher information in the measured data and $J$ the "bound" information of the source; extremizing $K$ is claimed to reproduce the Schrödinger, Klein–Gordon, and Dirac equations and Maxwell's equations alike ([[frieden-1998-physics-fisher]]). Reginatto showed more narrowly that the time-dependent Schrödinger equation follows (via the Madelung hydrodynamic substitution) from minimizing Fisher information subject to the relevant constraints, with $\hbar^2$ entering as the Lagrange multiplier weighting the Fisher term ([[reginatto-1998-fisher-quantum]]). Caticha's **entropic dynamics** derives quantum and gravitational structure from entropic inference plus a metric/symplectic structure on the space of distributions ([[caticha-bartolomeo-reginatto-2015-entropic-dynamics]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], [[johnson-2011-entropic-dynamics-measurement|johnson-caticha-2011-measurement-problem]]). All of these descend from Jaynes's foundational move of treating statistical mechanics as **MaxEnt inference** rather than mechanics ([[jaynes-1957-information-statistical-mechanics]]).

## Details

The strands differ in how much they claim. Jaynes ([[jaynes-1957-information-statistical-mechanics]]) is the weakest and most secure: equilibrium statistical mechanics *is* MaxEnt inference under macroscopic constraints, no new physics asserted. Reginatto ([[reginatto-1998-fisher-quantum]]) is a clean, limited derivation — minimum Fisher information plus an energy constraint gives Schrödinger, which is genuinely suggestive but does not fix the dynamics uniquely. Caticha's entropic dynamics ([[caticha-bartolomeo-reginatto-2015-entropic-dynamics]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]) is a sustained framework in which short-step entropic updating, a Fisher metric, and a symplectic structure together reconstruct the Schrödinger equation, and the measurement problem is recast as ordinary Bayesian updating of the agent's state of knowledge ([[johnson-2011-entropic-dynamics-measurement|johnson-caticha-2011-measurement-problem]]) — a reading congenial to the participatory/QBist sympathies of the surrounding cluster. Frieden's EPI ([[frieden-1998-physics-fisher]]) is the most ambitious and the most contested: critics charge that the choice of $J$ is reverse-engineered to the desired equation, so the "derivation" smuggles in its target. A complementary geometric thread is Crooks's **thermodynamic length** ([[crooks-2007-thermodynamic-length]]), where dissipation in a finite-time process is bounded by a Fisher-Rao path length on the manifold of thermodynamic states — an explicit instance of Fisher distance carrying physical (entropic) cost.

## Sources

- [[frieden-1998-physics-fisher]] — Extreme Physical Information; the universalist claim.
- [[reginatto-1998-fisher-quantum]] — Schrödinger equation from minimum Fisher information under an energy constraint.
- [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]] — entropic dynamics reconstructing quantum theory from inference plus geometry.
- [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]] — entropic-dynamics review.
- [[johnson-2011-entropic-dynamics-measurement|johnson-caticha-2011-measurement-problem]] — the quantum measurement problem as Bayesian/entropic updating.
- [[jaynes-1957-information-statistical-mechanics]] — statistical mechanics as MaxEnt inference, the root of the whole lineage.
- [[crooks-2007-thermodynamic-length]] — Fisher-Rao thermodynamic length bounding dissipation; Fisher distance as physical cost.
- [[nelson-1967-brownian-motion]] — stochastic mechanics: the Schrödinger equation derived from a conservative diffusion, with osmotic velocity $u=\nu\,\nabla\ln\rho$ a Fisher-information gradient; the historical headwater of the entropic-dynamics lineage.

## See also

- [[Fisher information metric]]
- [[Natural gradient]]
- [[Participatory realism (it from bit)]]
