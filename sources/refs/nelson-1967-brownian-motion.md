---
type: reference
title: "Dynamical Theories of Brownian Motion"
aliases: ["Nelson 1967", "Dynamical Theories of Brownian Motion", "Nelson stochastic mechanics"]
authors: ["Edward Nelson"]
year: 1967
tags: [cluster/info-geometry, cluster/participatory, cluster/participatory/quantum-foundations, project/multi-agent, field/physics, field/mathematics]
created: 2026-06-20
updated: 2026-06-20
---

# Dynamical Theories of Brownian Motion

> [!info] Citation
> Nelson, E. (1967). *Dynamical Theories of Brownian Motion*. Princeton University Press, Princeton. (2nd edition, 2001, available freely from the author.)

## TL;DR

The monograph in which Nelson lays out **stochastic mechanics**: a derivation of the Schrödinger equation from a classical diffusion process. Treating a particle as undergoing a conservative diffusion (a time-symmetric Markov process with forward and backward drifts), Nelson shows that Newton's second law applied to the mean stochastic acceleration is equivalent to the time-dependent Schrödinger equation, with $\hbar$ setting the diffusion coefficient. The first half is a clean, self-contained account of Brownian motion, the Wiener process, and the Ornstein–Uhlenbeck theory; the second half is the stochastic-mechanics derivation. It is a foundational ancestor of the modern **entropic-dynamics** and **physics-from-information** programs.

## What it establishes

- **Brownian-motion foundations** — the Wiener process, the Einstein–Smoluchowski and Ornstein–Uhlenbeck descriptions, and the passage from the microscopic Langevin picture to the macroscopic diffusion equation, developed rigorously and concisely.
- **Conservative diffusions** — a particle's trajectory modeled as a Markov diffusion possessing both a forward drift $b$ and a backward drift $b_*$, with a current velocity $v=(b+b_*)/2$ and an osmotic velocity $u=(b-b_*)/2$; the osmotic velocity is tied to the gradient of the log-density, $u = \nu\,\nabla\ln\rho$.
- **Schrödinger from diffusion** — defining a mean (stochastic) acceleration and imposing a Newtonian dynamical law on it yields, after writing $\psi=\sqrt{\rho}\,e^{iS/\hbar}$, the **time-dependent Schrödinger equation**. Quantum behavior emerges as the dynamics of a special diffusion, with the quantum potential appearing through the osmotic/log-density term.

## Why the project cites it

Nelson is the historical headwater of the thread the program leans on most heavily for its information-first reading of physics: the idea that quantum dynamics is *derived* from a stochastic/inferential substrate rather than postulated. The osmotic-velocity term $u=\nu\,\nabla\ln\rho$ is precisely a [[Fisher information metric|Fisher-information]] gradient, which is why the same Madelung/log-density substitution recurs in the program's cited [[Physics from Fisher information|physics-from-Fisher-information]] derivations — [[reginatto-1998-fisher-quantum|Reginatto]] obtaining the Schrödinger equation from a Fisher-information variational principle, [[frieden-1998-physics-fisher|Frieden's]] extreme-physical-information program, and especially Caticha's **entropic dynamics** ([[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]]), which recasts exactly Nelson's construction as inference. Citing Nelson lets the [[participatory-it-from-bit|participatory manuscript]] anchor its "dynamics from information" claim in the original stochastic-mechanics result and show that the program's [[Variational free energy|free-energy]]/Fisher machinery sits in a fifty-year lineage connecting diffusion, information geometry, and the emergence of quantum structure — the information-first foundations strand of the [[Participatory realism and quantum foundations]] theme.

> [!note] Editorial: Cited for the stochastic-mechanics derivation of the Schrödinger equation and its osmotic-velocity = Fisher-gradient structure, the ancestor of the program's entropic-dynamics / physics-from-Fisher citations — not as an endorsement of stochastic mechanics as the correct interpretation of QM.

```bibtex
@book{nelson1967dynamical,
  author    = {Nelson, Edward},
  title     = {Dynamical Theories of Brownian Motion},
  publisher = {Princeton University Press},
  address   = {Princeton, NJ},
  year      = {1967}
}
```
