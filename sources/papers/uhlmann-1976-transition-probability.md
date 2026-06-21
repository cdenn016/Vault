---
type: paper
title: "The \"Transition Probability\" in the State Space of a *-Algebra"
aliases:
  - "Uhlmann 1976"
  - "Uhlmann transition probability"
  - "Bures-Uhlmann fidelity"
authors:
  - Uhlmann, A.
year: 1976
arxiv: null
url: null
tags:
  - cluster/info-geometry
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# The "Transition Probability" in the State Space of a *-Algebra

> [!info] Citation
> Uhlmann, A. (1976). "The 'Transition Probability' in the State Space of a *-Algebra." *Reports on Mathematical Physics*, 9(2), 273–279.

## TL;DR
Uhlmann introduces and studies a generalized transition probability P(ω₁, ω₂) between two states of a *-algebra, defined as the supremum of |⟨x₁, x₂⟩|² over all *-representations in which the states are realized as vector states. For density matrices d₁, d₂ on a type I factor, this reduces to P = (Sp s)², where s = (d₁^{1/2} d₂ d₁^{1/2})^{1/2}, recovering the Bures fidelity. The paper establishes concavity of P, connects it to orthogonality of states, provides upper bounds via geometric means of Hermitian forms, and proves a central theorem giving an explicit expression in terms of a factored representation.

## Problem & setting
The standard quantum mechanical transition probability |⟨x, y⟩|² is well-defined for pure states represented as vectors, but what is the correct generalization to mixed states and to states of general *-algebras (including C*-algebras and W*-algebras)? Bures (1969) and Kakutani (1948) had already encountered a related expression in the construction of infinite tensor products; Uhlmann's aim is to systematically study its properties and derive explicit formulas. The paper works in the algebraic approach to quantum theory, where states are positive normalized linear functionals on a *-algebra R with unit.

## Method
The transition probability is defined via a supremum construction: given states ω₁, ω₂ of a *-algebra R, one considers all *-representations π in which both states are simultaneously realized as vector states ωⱼ(b) = ⟨xⱼ, π(b)xⱼ⟩, and sets

P(ω₁, ω₂) = sup |⟨x₁, x₂⟩|²

over all such representations and all admissible vector pairs. Key results follow from:

1. **Concavity**: For Gibbsian mixtures ω = λ₁ω₁ + λ₂ω₂ and θ = λ₁θ₁ + λ₂θ₂ one obtains P(ω, θ) ≥ λ₁ P(ω₁, θ₁) + λ₂ P(ω₂, θ₂).

2. **Orthogonality bound**: ‖ω₁ − ω₂‖ ≤ 2√(1 − P(ω₁, ω₂)), so orthogonal states (‖ω₁ − ω₂‖ = 2) have P = 0.

3. **Upper bound via geometric mean**: Using the Pusz–Woronowicz geometric mean √(β₁β₂) of two positive semidefinite Hermitian forms, one obtains P ≤ √(β₁β₂)(e, e).

4. **Explicit formula (main theorem)**: If ω₁, ω₂ factor through a common positive linear form ω via ωⱼ(a) = ω(bⱼ* a bⱼ) and b₁*b₂ = b₂b₁* ≥ 0, then P(ω₁, ω₂) = ω(b₁*b₂)². For density matrices d₁, d₂ this yields s = (d₁^{1/2} d₂ d₁^{1/2})^{1/2} and

   P = (Tr s)²,

   which is exactly the Bures fidelity F(ρ, σ) = (Tr√(√ρ σ √ρ))².

## Key results
- **Bures fidelity recovery** (Eq. 1, 23): For two density matrices d₁, d₂ on a type I factor, P(ω₁, ω₂) = (Tr s)² with s = (d₁^{1/2} d₂ d₁^{1/2})^{1/2}.
- **Concavity** (Eq. 8): P is concave under Gibbsian mixing.
- **Orthogonality** (Eq. 11): P(ω₁, ω₂) = 0 whenever the states are orthogonal.
- **Pure-state reduction**: If d₂ represents a pure state vector x, then P(ω₁, ω₂) = ⟨x, d₁ x⟩, which is the expected Born-rule overlap.
- **Commutative case** (Eq. 27–28): For C(X) with measures given by Radon–Nikodym derivatives h₁, h₂ against a common measure dν, P = (∫ √(h₁ h₂) dν)², the Bhattacharyya coefficient, squared.
- **Algebra inclusion monotonicity** (Eq. 24): R₁ ⊆ R₂ implies P(R₂|ω₁, ω₂) ≥ P(R₁|ω₁, ω₂).

## Relevance to this research
The Uhlmann fidelity / Bures metric is foundational to information geometry on the space of density matrices and directly connects to several threads in the VFE program.

In the SPD belief geometry used in the VFE transformer, the Bures metric and Uhlmann parallel transport on the bundle of purifications provide a natural Riemannian structure on the space of positive definite covariance matrices. The "parallel transport" construction implicit in Uhlmann's purification bundle is conceptually analogous to the GL(K) gauge transport Ω_{ij} used in the manuscript to parallel-transport beliefs between attention heads: both are defined as the unitary (or isometric) lift that maximizes overlap.

The Uhlmann transition probability P(ρ, σ) = (Tr√(√ρ σ √ρ))² appears as the square of the quantum fidelity, which enters KL-divergence bounds and is related to the Petz recovery map — relevant whenever the VFE's KL(q_i ‖ Ω_{ij} q_j) belief-coupling term is analyzed for its geometric properties on the space of Gaussian beliefs.

For the participatory realism / quantum-foundations thread (PIFB manuscript), Uhlmann's algebraic treatment of states of a *-algebra is the natural language for the "it from bit" / participatory observer framework, where quantum states are seen as positive functionals and transition amplitudes are given by the purification construction.

## Cross-links
- Concepts: [[Bures Metric]], [[Quantum Fidelity]], [[SPD Geometry]], [[Purification]], [[Information Geometry]]
- Related sources: [[bures-1969-metric]], [[pusz-woronowicz-1975-functional-calculus]]
- Manuscript/Project: [[GL(K) Attention Manuscript]], [[PIFB Manuscript]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Uhlmann1976,
  author  = {Uhlmann, A.},
  title   = {The ``Transition Probability'' in the State Space of a *-Algebra},
  journal = {Reports on Mathematical Physics},
  volume  = {9},
  number  = {2},
  pages   = {273--279},
  year    = {1976},
}
```
