---
type: paper
title: "A universal test for gravitational decoherence"
aliases:
  - "Pfister 2016"
  - "universal gravitational decoherence test"
authors:
  - Pfister, C.
  - Kaniewski, J.
  - Tomamichel, M.
  - Mantri, A.
  - Schmucker, R.
  - McMahon, N.
  - Milburn, G.
  - Wehner, S.
year: 2016
arxiv: null
url: https://doi.org/10.1038/ncomms13022
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/cs-ml
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# A universal test for gravitational decoherence

> [!info] Citation
> Pfister, C., Kaniewski, J., Tomamichel, M., Mantri, A., Schmucker, R., McMahon, N., Milburn, G., & Wehner, S. (2016). "A universal test for gravitational decoherence." *Nature Communications*, 7, 13022. https://doi.org/10.1038/ncomms13022

## TL;DR
This paper proposes a theory-agnostic method for estimating gravitational decoherence that remains valid even if quantum mechanics must be modified. The key idea is to embed any decoherence experiment inside a Bell (CHSH) test: monogamy of non-signalling correlations then yields a quantitative upper bound on the decoherence Dec(A|E) from the measured Bell parameter beta alone, without assuming quantum mechanics. As a concrete application, the authors analyze an optomechanical cavity experiment that could falsify Diosi's gravitational decoherence model.

## Problem & setting
Quantum mechanics and gravity are incompatible, and it is unknown whether gravity causes decoherence. Existing experimental proposals for testing gravitational decoherence all rely on quantum mechanics as a calculational framework — yet quantum mechanics itself may need modification to accommodate gravitational effects. Prior theoretical models (Penrose, Diosi, GRW/CSL collapse models) are many and mutually inconsistent, while experiments are largely exploratory. The challenge is to design a test whose conclusions do not presuppose quantum mechanics.

## Method
The authors define a theory-independent notion of decoherence Dec(A|E) — the degree to which an environment E becomes correlated with a system A — using the fidelity between the post-process state and the set of maximally correlated states (which reduces to the standard quantum min-entropy H_min(A|E) = -log dA Dec(A|E) within QM). They then prove:

Dec(A|E) ≤ h(beta)

where beta is the measured CHSH correlator and h is a function derived by linear programming over all no-signalling probability distributions satisfying the observed Bell violation. The argument uses monogamy of non-signalling correlations: a high Bell violation between A and B implies low correlation between A and E, bounding decoherence from above. In the quantum case the bound is tightened using Bell-diagonal state symmetry and Lagrange multipliers. The method is fully device-independent and operates in any physical theory where no-signalling holds between A, B, and E.

## Key results
The main theorem establishes Dec(A|E) ≤ h(beta) for any no-signalling theory, where h(beta) is non-trivial for all beta > 2 (i.e., any genuine Bell violation gives information about decoherence). The quantum bound is strictly tighter. Applied to Diosi's model in an optomechanical system (a movable mirror in a harmonic potential), the gravitational decoherence rate is Lambda_grav = (2pi/3)(G Delta/omega_m), which is approximately 10^{-8} s^{-1} for suspended mirrors. Numerical simulations show that at temperatures T = 1-50 nK the gap between Dec(A|E) with and without gravitational decoherence is large enough to potentially falsify Diosi's model. The bound holds even for generalized probabilistic theories (GPTs) with super-quantum correlations (beta > 2sqrt(2)).

## Relevance to this research
This paper is relevant primarily through its connection to participatory quantum foundations and the physical interpretation of decoherence in theories that go beyond standard quantum mechanics. The framework of generalized probabilistic theories (GPTs) and the use of the no-signalling principle as the sole assumption resonates with the participatory realism / "it from bit" program (Wheeler), where physical reality emerges from information-theoretic constraints rather than from a pre-given quantum Hilbert space. The information-theoretic decoherence measure Dec(A|E) — defined operationally via fidelity between probability distributions over measurement outcomes — is in spirit aligned with the VFE program's emphasis on belief geometries and divergence measures as fundamental quantities. The monogamy-of-correlations argument (strong correlations between A-B imply weak A-E entanglement) has structural parallels to the attention-mediated belief coupling in the VFE transformer, where coupling between token pairs competes for a shared "resource." The optomechanical experiment design (entangled cavities probing decoherence) is not directly relevant to the transformer code, but the foundational stance — deriving bounds from operational/information-theoretic principles without assuming a specific physical theory — is directly in the spirit of the participatory and information-geometric foundations of the VFE research.

## Cross-links
- Concepts: [[Participatory Realism]], [[Generalized Probabilistic Theories]], [[Quantum Decoherence]], [[Bell Inequality]], [[No-Signalling Principle]]
- Related sources: [[Pfister2013]] (prior work by same author on information-theoretic principle implying classicality)
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Pfister2016,
  author  = {Pfister, C. and Kaniewski, J. and Tomamichel, M. and Mantri, A. and Schmucker, R. and McMahon, N. and Milburn, G. and Wehner, S.},
  title   = {A universal test for gravitational decoherence},
  journal = {Nature Communications},
  year    = {2016},
  volume  = {7},
  pages   = {13022},
  doi     = {10.1038/ncomms13022},
}
```
