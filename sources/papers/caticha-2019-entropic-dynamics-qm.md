---
type: paper
title: "The Entropic Dynamics approach to Quantum Mechanics"
aliases:
  - Caticha 2019
  - Entropic Dynamics QM
  - ED-QM
  - caticha-2019-entropic-physics
  - caticha2019entropicphysics
  - caticha-2019-entropic-dynamics
  - Caticha (2019) Entropic Dynamics
authors:
  - Caticha, Ariel
year: 2019
arxiv: "1908.04693"
url: https://arxiv.org/abs/1908.04693
tags:
  - cluster/participatory/quantum-foundations
  - cluster/info-geometry
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/mathematics
  - field/statistics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The Entropic Dynamics approach to Quantum Mechanics

> [!info] Citation
> Caticha, Ariel (2019). "The Entropic Dynamics approach to Quantum Mechanics." *Entropy* 21(10), 943. DOI: [10.3390/e21100943](https://doi.org/10.3390/e21100943). Preprint: [arXiv:1908.04693](https://arxiv.org/abs/1908.04693) [quant-ph].

## TL;DR
Entropic Dynamics (ED) derives quantum mechanics as an application of entropic inference (maximum entropy) rather than as a generalization of classical mechanics. The wave function is treated as a purely epistemic object encoding probabilistic constraints, and the Schrödinger equation emerges as the unique Hamilton-Killing flow that preserves both the symplectic and information-geometric metric structures of the space of probabilities and phases. Hilbert spaces are shown to be a convenient but non-essential calculational tool.

## Problem & setting
Standard quantum mechanics suffers from an irreconcilable dichotomy between unitary Schrödinger evolution and stochastic wave-function collapse, and from ambiguity about whether the wave function is ontic or epistemic. The paper asks: can QM be reconstructed entirely from probabilistic and entropic principles, with no ad hoc quantization rules, no Hilbert-space axioms as foundations, and a fully epistemic wave function?

Prior art includes Nelson's stochastic mechanics (attempted ontic interpretation as a Brownian process), QBism and Quantum Bayesianism (epistemic but non-reconstructive), and various information-theoretic reconstructions. ED distinguishes itself by strict adherence to Bayesian/entropic updating and explicit treatment of the nature of time.

## Method
The starting point is a configuration space of $N$ particles with definite but unknown positions (the sole ontic variables). A transition probability $P(x'|x)$ is found by maximizing the relative entropy

$$S[P,Q] = -\int dx'\, P(x'|x)\log\frac{P(x'|x)}{Q(x'|x)}$$

subject to: (i) a Gaussian prior $Q$ encoding infinitesimal steps with translational/rotational invariance; (ii) a drift-potential constraint on the expected displacement $\langle\Delta\phi\rangle = \kappa'(x)$, where the drift potential $\phi$ is topologically an angle ($\phi \sim \phi + 2\pi$); and (iii) gauge constraints coupling displacements to the electromagnetic vector potential $A_a$.

Choosing $\alpha_n \propto 1/\Delta t^3$ (Ornstein-Uhlenbeck sub-quantum motion, with smooth differentiable trajectories) instead of $\alpha_n \propto 1/\Delta t$ (Einstein-Smoluchowski, non-differentiable) yields the continuity equation $\partial_t\rho = -\partial_A(v^A\rho)$ with drift velocity $v^A = m^{AB}[\partial_B\Phi - \bar{A}_A]$.

The space $\{\rho, \Phi\}$ of probabilities and phases carries a natural symplectic structure (Poisson brackets, Hamiltonian flows). Extending the information geometry (Fisher-Rao metric) of $\{\rho\}$ to the full phase space by imposing spherical symmetry yields the Fubini-Study metric and, as a by-product, a complex structure — which is why QM involves complex numbers. The unique dynamics that is simultaneously a Hamiltonian flow and a Killing flow (preserving both structures) is the linear Schrödinger equation.

Gauge invariance arises naturally: the constraints on $\langle\Delta x^a_n\rangle$ through $\phi$ and $A_a$ are not independent, giving the combined gauge symmetry $A_a \to A_a + \partial_a\chi$, $\Phi \to \Phi + \bar{\chi}$.

## Key results
- The Schrödinger equation is derived without any quantization postulates: it is the unique Hamilton-Killing flow on the symplectic-metric phase space $\{\rho,\Phi\}$.
- The Fubini-Study metric on the space of wave functions is derived from information geometry (Fisher metric extended by spherical symmetry to the full phase space), not postulated.
- Complex structure in QM is explained geometrically: it is the inevitable consequence of simultaneously possessing symplectic and metric structures.
- Two sub-quantum models are explored: the Einstein-Smoluchowski (non-differentiable trajectories, $\alpha_n\propto 1/\Delta t$) and the Ornstein-Uhlenbeck (smooth differentiable trajectories, $\alpha_n\propto 1/\Delta t^3$). Both yield the same Schrödinger equation at the macroscopic quantum level.
- Bohmian mechanics emerges as the zero-fluctuation limit of ED.
- The arrow of entropic time arises from the directionality of the max-entropy updating rule, resolving the arrow-of-time puzzle without assuming asymmetric microphysics.
- Hilbert spaces are demonstrated to be a convenient but logically unnecessary ingredient.
- Charge quantization and single-valuedness of wave functions are connected to the topological (angular) nature of the drift potential.

## Relevance to this research
ED is a direct antecedent of the participatory / epistemic foundations motivating the VFE transformer program. Several connections are sharp.

**Entropic inference as the foundation of dynamics.** ED demonstrates that treating probability distributions as the primary objects and deriving dynamics via constrained entropy maximization (rather than postulating equations of motion) can recover the full structure of QM. This mirrors the VFE transformer's philosophy: beliefs $(μ, Σ)$ are primary, and dynamics (E-step, transport, attention) emerge from minimizing the variational free energy functional, not from neural network layers.

**Gauge structure from constraint non-independence.** The electromagnetic gauge symmetry in ED arises because the drift-potential constraint and the vector-potential constraint both involve the same displacement $\langle\Delta x^a_n\rangle$ — they are not independent. The GL(K) gauge equivariance in the VFE attention mechanism has an analogous structure: transport $\Omega_{ij}$ and the attention weights $\beta_{ij}$ are tied together through the same belief geometry, enforcing gauge-equivariant KL divergences.

**Information geometry of configuration space.** The Fisher-Rao metric on $X^N$ derived from $P(x'|x)$ yields the mass tensor as a natural geometric object. The VFE transformer likewise uses SPD/Riemannian geometry of the space of Gaussian beliefs as its native geometry — the Bures metric and the natural gradient on the SPD manifold play the role of the information metric here.

**Epistemic wave functions and the participatory framework.** Caticha's fully epistemic interpretation of $\Psi$ (information about actual positions, not an ontic field) connects to the participatory realism framework underpinning the multi-agent active-inference program (see [[Participatory realism (it from bit)|PIFB]] and [[fuchs-2017-participatory-realism|Participatory Realism]]). The "it from bit" structure — observations constrain distributions, not ontic fields — is shared.

**Symplectic structure and phase-space dynamics.** The natural symplectic structure on $\{\rho, \Phi\}$ and the Hamiltonian-Killing flow derivation of Schrödinger evolution is potentially relevant to understanding the phase structure of the VFE belief update as a geometric flow on a statistical manifold.

## Cross-links
- Concepts: [[Information Geometry]], [[Information geometry and natural gradient]], [[Natural gradient]], [[Fisher information metric]], [[Variational Free Energy]], [[Group equivariance|Gauge Equivariance]], [[fuchs-2017-participatory-realism|Participatory Realism]], [[Participatory realism (it from bit)]], [[Maximum entropy|Maximum Entropy Principle]], [[Hamiltonian belief dynamics]], [[Belief inertia]], [[Mass as Fisher information]], [[Meta-entropy]], [[Agents as fibre-bundle sections]], [[Parallel transport]]
- Related sources: [[jaynes-1957-information-statistical-mechanics|jaynes-1957-information-theory]], [[amari-2000-methods-information-geometry]], [[wheeler-1990-it-from-bit]], [[fuchs2014-qbism-locality|fuchs-2014-qbism]]
- Manuscript/Project: [[VFE Transformer Program]], [[Participatory realism (it from bit)|PIFB]], [[participatory-it-from-bit]], [[GL(K) gauge-equivariant attention|GL(K) Attention]]

## BibTeX
```bibtex
@article{Caticha2019,
  author  = {Caticha, Ariel},
  title   = {The Entropic Dynamics approach to Quantum Mechanics},
  journal = {Entropy},
  year    = {2019},
  volume  = {21},
  number  = {10},
  pages   = {943},
  doi     = {10.3390/e21100943},
  eprint  = {1908.04693},
  archivePrefix = {arXiv},
  primaryClass  = {quant-ph},
  url     = {https://arxiv.org/abs/1908.04693},
}
```
