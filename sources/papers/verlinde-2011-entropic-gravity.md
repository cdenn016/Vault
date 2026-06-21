---
type: paper
title: "On the Origin of Gravity and the Laws of Newton"
aliases:
  - "Verlinde 2011"
  - "entropic gravity"
authors:
  - Verlinde, Erik
year: 2011
arxiv: "1001.0785"
url: https://doi.org/10.1007/JHEP04(2011)029
tags:
  - cluster/participatory/quantum-foundations
  - cluster/gauge-theory
  - project/multi-agent
  - field/physics
  - field/mathematics
  - field/philosophy
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# On the Origin of Gravity and the Laws of Newton

> [!info] Citation
> Verlinde, Erik (2011). "On the Origin of Gravity and the Laws of Newton." *JHEP* 04 (2011) 029. doi:10.1007/JHEP04(2011)029. arXiv:1001.0785.

## TL;DR
Verlinde argues that gravity is not a fundamental force but an entropic force arising from the tendency of a holographic system to increase its information-theoretic entropy. Starting from holographic screens that store information proportionally to their area, equipartition of energy over those bits, and a Bekenstein-inspired entropy-change postulate, Newton's law of gravitation and inertia emerge essentially unavoidably. A relativistic generalization of the same heuristic arguments leads directly to the Einstein equations.

## Problem & setting
The deep resemblance between the laws of gravity and the laws of thermodynamics has long lacked a clear explanation. Verlinde sets out to derive Newton's laws — and ultimately general relativity — from first principles without assuming gravity is fundamental, using only space-independent concepts (energy, entropy, temperature) together with the holographic principle. Prior art includes Bekenstein's black hole entropy, Unruh radiation, and the AdS/CFT correspondence, all of which point toward a deep connection between information and spacetime geometry.

## Method
The derivation rests on three core assumptions: (i) information is stored on holographic screens proportionally to their area, $N = Ac^3/(G\hbar)$; (ii) energy is distributed evenly over the bits via equipartition, $E = \tfrac{1}{2} N k_B T$; and (iii) an entropy change $\Delta S = 2\pi k_B (mc/\hbar)\,\Delta x$ is associated with a particle of mass $m$ displaced by $\Delta x$ near a screen, motivated by Bekenstein's thought experiment. Combining (iii) with the Unruh temperature $k_B T = \hbar a / (2\pi c)$ yields Newton's second law $F = ma$ as an entropic force $F\,\Delta x = T\,\Delta S$. Closing the sphere and using $E = Mc^2$ then gives Newton's law of gravitation $F = GMm/R^2$. For general matter distributions, equipartition on an arbitrary equipotential surface produces Gauss's law and hence the Poisson equation $\nabla^2\Phi = 4\pi G\rho$. The Newton potential is identified as a coarse-graining (RG-scale) variable, with holographic screens located at equipotential surfaces and coarse-graining proceeding in the direction of $\nabla\Phi$.

## Key results
Newton's second law ($F = ma$) and Newton's law of gravitation ($F = GMm/R^2$) are derived from entropic-force reasoning with holographic screens — no prior assumption of a gravitational field. The Poisson equation for general matter distributions follows from equipartition on equipotential-surface screens. The Newton potential is identified as an information-coarse-graining variable analogous to the RG scale in AdS/CFT, with black hole horizons ($-2\Phi/c^2 = 1$) marking maximal coarse-graining. A relativistic extension leads to the Einstein equations, though that derivation is more schematic. The paper establishes that inertia too is entropic: a particle at rest experiences no entropy gradient, and hence no force.

## Relevance to this research
This paper is directly relevant to the VFE transformer program in several ways. First, the identification of the Newton potential with a coarse-graining (RG-scale) variable resonates with the role of the free-energy functional $F$ in the VFE hierarchy ($h \to s \to p \to q \to$ observations): both are information-accounting devices that track entropy depletion across levels of description. Second, the holographic screen picture — in which information stored on a boundary determines emergent bulk geometry — is structurally analogous to how gauge-equivariant attention transports belief states $q_i$ across tokens via holonomy $\Omega_{ij}$, with the attention weights $\beta_{ij}$ playing the role of the entropic coupling. Third, the entropic-force derivation is a concrete instantiation of the participatory-realist programme ([[Participatory It-from-Bit]]): space and gravity are not given but emerge from information processing, echoing Wheeler's "it from bit." Fourth, the coarse-graining foliation by equipotential surfaces is reminiscent of the nested belief hierarchy in active inference, where each level integrates out finer-scale degrees of freedom. Finally, the paper's approach to inertia — as an absence of entropy gradients rather than a primitive — may inform how the VFE transformer should treat positional encoding and transport in the emergent-space limit.

## Cross-links
- Concepts: [[Entropic Force]], [[Holographic Principle]], [[Variational Free Energy]], [[Information Geometry]], [[Coarse Graining]]
- Related sources: [[bekenstein-1973-black-holes]], [[unruh-1976-notes]], [[maldacena-1997-large-n]]
- Manuscript/Project: [[VFE Transformer Program]], [[Participatory It-from-Bit]]

## BibTeX
```bibtex
@article{Verlinde2011,
  author  = {Verlinde, Erik},
  title   = {On the Origin of Gravity and the Laws of Newton},
  journal = {JHEP},
  volume  = {04},
  pages   = {029},
  year    = {2011},
  doi     = {10.1007/JHEP04(2011)029},
  eprint  = {1001.0785},
  archivePrefix = {arXiv},
}
```
