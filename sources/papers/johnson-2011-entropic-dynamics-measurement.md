---
type: paper
title: "Entropic Dynamics and the Quantum Measurement Problem"
aliases:
  - Johnson Caticha 2011
  - ED measurement problem
  - johnson-caticha-2011-measurement-problem
  - Johnson & Caticha 2011
  - Johnson-Caticha (2011) Measurement Problem
authors:
  - Johnson, David T.
  - Caticha, Ariel
year: 2011
arxiv: "1108.2550"
url: https://arxiv.org/abs/1108.2550
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

# Entropic Dynamics and the Quantum Measurement Problem

> [!info] Citation
> Johnson, D. T. & Caticha, A. (2011/2012). "Entropic Dynamics and the Quantum Measurement Problem." Presented at MaxEnt 2011, The 31st International Workshop on Bayesian Inference and Maximum Entropy Methods in Science and Engineering (July 10–15, 2011, Waterloo, Canada). In *AIP Conference Proceedings* **1443**, 104–116 (2012). DOI: 10.1063/1.3703626. arXiv:1108.2550.

## TL;DR
Within the Entropic Dynamics (ED) framework, quantum mechanics is recast as a theory of inference rather than a law of nature, dissolving the measurement problem. The dual modes of quantum evolution — continuous unitary evolution and abrupt wave-function collapse — are unified as two instances of entropic probability updating (continuous MaxEnt steps versus discrete Bayesian updates). Particles have definite but unknown positions; all other observables are informational attributes of the probability distribution, not of the particle, so the Born rule emerges naturally rather than being postulated.

## Problem & setting
The quantum measurement problem poses two intertwined difficulties: macroscopic entanglement (why superpositions are not observed at large scales) and definite outcomes (how a measurement selects a single result). Standard approaches — von Neumann's projection postulate, many-worlds, decoherence — either postulate collapse or save appearances without explaining why outcomes are definite. Johnson and Caticha revisit the problem from the perspective of Entropic Dynamics (Caticha 2011, J. Phys. A 44:225303; arXiv:1005.2357), which derives quantum mechanics from MaxEnt inference over particle positions.

## Method
Entropic Dynamics rests on three pillars. First, the subject matter is particle position x, with auxiliary variables y carrying entropy S(x) = -∫ dy p(y|x) log[p(y|x)/q(y)]. Second, the transition probability P(x'|x) for short steps is derived by constrained MaxEnt, yielding a Fokker-Planck equation for the position distribution ρ(x,t):

  ∂ρ/∂t = −∇·(ρ v),   v = (ℏ/m) ∇φ,   φ = S − log ρ^{1/2}.

Third, imposing conservation of a statistical energy functional E[ρ,S] forces the quantum Hamilton-Jacobi equation for φ. Together these two equations are equivalent to the Schrödinger equation for Ψ = ρ^{1/2} e^{iφ}. For measurement of generic observables, a complex detector device A implements a unitary U_A mapping eigenstates |a_i⟩ of an operator Â to position eigenstates |x_i⟩. Expanding an arbitrary state in the eigenbasis and applying the Born rule for position then yields the Born rule |⟨a|Ψ⟩|² for the generic observable — derived, not postulated. Amplification is handled purely by Bayesian inference on a pointer variable α correlated with position.

## Key results
Continuous unitary evolution and wave-function collapse are both special cases of entropic probability updating; no distinct postulate for collapse is needed. The Born rule for position is built into the formalism by construction (ρ = |Ψ|²); the Born rule for all other observables is derived from unitary evolution alone. Non-position observables (momentum, energy, angular momentum) are shown to be attributes of the probability distribution ρ and entropy S, not of the particle — their values are effectively created by the measurement interaction. The operator measured need not be Hermitian, only normal (ÂÂ† = Â†Â), since only orthogonality of eigenvectors is required. Amplification introduces no intrinsically quantum step: Bayesian inference on the pointer variable suffices.

## Relevance to this research
This paper is a primary reference for the participatory/informational interpretation of quantum mechanics that underlies the Participatory It-from-Bit (PIFB) manuscript. The entropic derivation of the Schrödinger equation — from MaxEnt inference over position with an energy conservation constraint — is a concrete worked example of how physical law emerges from inference principles, directly paralleling the PIFB program's thesis that reality is participatory and observer-constituted. The identification of non-position observables as attributes of probability distributions (not particles) resonates with the VFE transformer's treatment of beliefs (mu, Sigma, phi) as the primary objects, with classical "observables" emerging from variational inference. The unification of Bayesian and entropic updating under a single entropic inference scheme is also relevant to the VFE free-energy functional, where the E-step and M-step can be viewed as analogous alternating update modes. This is the physics precedent for PIFB's "collapse as consensus" claim: the abrupt entropic update of an agent's beliefs upon receiving information is read, in the multi-agent setting, as collective convergence — the social-physics counterpart of measurement, driven by the same MaxEnt updating that the project's entropy-regularized consensus dynamics perform on belief tuples.

## Cross-links
- Concepts: [[Physics from Fisher information|Entropic Dynamics]] · [[Maximum Entropy]] · [[Born Rule]] · [[Wave-Function Collapse|Wave Function Collapse]] · [[fuchs-2017-participatory-realism|Participatory Realism]]
- Related sources: [[caticha-2011-entropic-dynamics]] · [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-physics]]
- Manuscript/Project: [[Participatory realism (it from bit)|PIFB]] · [[VFE Transformer Program]]

## BibTeX
```bibtex
@inproceedings{JohnsonCaticha2011,
  author    = {Johnson, David T. and Caticha, Ariel},
  title     = {Entropic Dynamics and the {Q}uantum Measurement Problem},
  booktitle = {Bayesian Inference and Maximum Entropy Methods in Science and Engineering (MaxEnt 2011)},
  series    = {AIP Conference Proceedings},
  volume    = {1443},
  pages     = {104--116},
  year      = {2012},
  publisher = {AIP Publishing},
  doi       = {10.1063/1.3703626},
  note      = {arXiv:1108.2550},
}
```
