---
type: paper
title: "Von Neumann algebra automorphisms and time-thermodynamics relation in general covariant quantum theories"
aliases:
  - Connes Rovelli 1994
  - thermal time hypothesis
  - Connes & Rovelli 1994
authors:
  - Connes, Alain
  - Rovelli, Carlo
year: 1994
arxiv: gr-qc/9406019
url: https://arxiv.org/abs/gr-qc/9406019
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Von Neumann algebra automorphisms and time-thermodynamics relation in general covariant quantum theories

> [!info] Citation
> Connes, A. & Rovelli, C. (1994). "Von Neumann algebra automorphisms and time–thermodynamics relation in generally covariant quantum theories." *Classical and Quantum Gravity*, 11(12), 2899–2917. DOI: [10.1088/0264-9381/11/12/007](https://doi.org/10.1088/0264-9381/11/12/007). Preprint: arXiv:gr-qc/9406019.

## TL;DR
Connes and Rovelli propose the "thermal time hypothesis": in a generally covariant quantum theory, there is no preferred time flow, and physical time emerges from the thermodynamical state of the system via the Tomita-Takesaki modular automorphism group. Given any faithful state over a von Neumann algebra, the Tomita-Takesaki theorem defines a canonical one-parameter group of automorphisms (the modular group) that is postulated to be the physical time flow. The Cocycle Radon-Nikodym theorem further implies a state-independent canonical outer automorphism group intrinsic to the algebra itself.

## Problem & setting
General covariant theories (general relativity, background-independent quantum gravity) possess no preferred time flow — the "issue of time" in quantum gravity. When thermodynamics or quantum superpositions of geometries are included, even the weaker notion of proper time along timelike worldlines is lost. The question is: what singles out a particular flow as the physical time? Prior approaches rely on selecting an "internal time" variable from the dynamical fields, but no such choice is canonical and each introduces unitarity difficulties. The paper addresses this fundamental impasse.

## Method
The core technical machinery is the Tomita-Takesaki theorem from von Neumann algebra theory. Given a von Neumann algebra $\mathcal{R}$ acting on a Hilbert space $\mathcal{H}$ with a cyclic and separating vector $|\Psi\rangle$, define the operator $S$ by $SA|\Psi\rangle = A^\star|\Psi\rangle$. Its polar decomposition $S = J\Delta^{1/2}$ yields the modular operator $\Delta$, and the theorem states that

$$\alpha_t A = \Delta^{-it} A \Delta^{it}$$

defines a one-parameter group of automorphisms of $\mathcal{R}$ — the modular group of the state $\omega$. The thermal time hypothesis postulates that this modular flow is the physical time flow when the system is in state $\omega$.

In the classical limit, a thermal (Gibbs) state $\rho = e^{-\beta H}$ determines a modular flow that coincides with the Hamiltonian flow, recovering ordinary thermodynamics. In a generally covariant quantum theory where no Hamiltonian is given, the state alone determines the time via the Tomita-Takesaki theorem. The KMS condition connects the formalism to equilibrium statistical mechanics: any faithful state is automatically a KMS state at inverse temperature $\beta = 1$ with respect to its own modular group. The Cocycle Radon-Nikodym theorem ensures that the modular group up to inner automorphisms — the outer automorphism group $\widetilde{\alpha}_t \in \mathrm{Out}(\mathcal{R})$ — is independent of the state, furnishing a state-independent, intrinsic notion of "time" for the algebra.

## Key results
The thermal time hypothesis is shown to reduce to standard Hamiltonian dynamics for non-generally covariant theories in Gibbs states. Applied to quantum field theory in curved spacetime, the Unruh temperature and Hawking radiation are shown to be direct consequences of the postulate: the modular group of the Minkowski vacuum state, restricted to the Rindler wedge, generates precisely the Lorentz boost — corresponding to the thermal time experienced by an accelerated observer. Temperature is reinterpreted as the ratio between thermal time and geometric time, defined only when the latter exists. The FRW cosmological time is recovered as the thermal time of the cosmological background radiation state in a covariantly formulated cosmological model. The Cocycle Radon-Nikodym theorem provides a canonical, state-independent outer automorphism one-parameter group as an intrinsic "clock" built into the algebraic structure of observables.

## Relevance to this research
The thermal time hypothesis directly informs the participatory realism / "it from bit" / consciousness-theoretic thread of the VFE research program. The identification of time flow with the modular automorphism of a thermal state resonates with the VFE framework's treatment of beliefs as thermodynamic states and free energy minimization as the dynamical principle — in both, thermodynamics and dynamics are unified through a state-dependent flow. The Tomita-Takesaki modular group is an operator-algebraic counterpart to the belief-geometry structures in SPD manifolds: a faithful state on a von Neumann algebra plays the role of a positive-definite covariance matrix $\Sigma$, and the modular operator $\Delta$ encodes the information geometry of that state. The state-independence of the outer automorphism group (via Cocycle Radon-Nikodym) parallels the gauge-invariance requirement in the GL(K) attention framework — the canonical "time" is the invariant structure independent of the choice of representative state, just as gauge-invariant quantities are independent of the choice of basis. The paper also anchors the philosophical claim in PIFB.tex that physical time is observer-relative and thermodynamically constituted — a participatory, relational view of time that underpins the theoretical motivations for the VFE active inference program.

## Cross-links
- Concepts: [[Thermal Time Hypothesis]], [[Tomita-Takesaki Theorem]], [[Modular Automorphism]], [[KMS States]], [[Von Neumann Algebras]], [[Information Geometry]], [[Participatory realism (it from bit)]], [[Emergent spacetime and holography]]
- Related sources: [[rovelli-1996-relational-qm]], [[friston-2019-free-energy]], [[page-wootters-1983]]
- Manuscript/Project: [[VFE Transformer Program]], [[PIFB manuscript]], [[participatory-it-from-bit]]

> [!note] Why the project cites it (observer-relative time cluster, from manuscript-citation note)
> The thermal time hypothesis completes the program's *observer-relative time* cluster: time is the modular flow of the observer's state. It sits beside the relational reading of [[rovelli-1996-relational-qm]] and the observer-internal time of the Page–Wootters mechanism ([[page-wootters-1983]]) as the three pillars, reinforcing that "when/how things evolve" is a state-dependent, [[Variational free energy]]-driven inference notion within the [[Emergent spacetime and holography]] theme.

## BibTeX
```bibtex
@article{ConnesRovelli1994,
  author  = {Connes, Alain and Rovelli, Carlo},
  title   = {Von {N}eumann algebra automorphisms and time--thermodynamics relation
             in generally covariant quantum theories},
  journal = {Classical and Quantum Gravity},
  year    = {1994},
  volume  = {11},
  number  = {12},
  pages   = {2899--2917},
  doi     = {10.1088/0264-9381/11/12/007},
  eprint  = {gr-qc/9406019},
  archivePrefix = {arXiv},
  primaryClass  = {gr-qc},
}
```
