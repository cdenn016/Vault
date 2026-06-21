---
type: paper
title: "Thermodynamics of Spacetime: The Einstein Equation of State"
aliases:
  - Jacobson 1995
  - Einstein equation of state
  - jacobson-1995-thermodynamics-spacetime
  - Thermodynamics of Spacetime
  - thermodynamicsofspacetime
authors:
  - Jacobson, Ted
year: 1995
arxiv: gr-qc/9504004
url: https://arxiv.org/abs/gr-qc/9504004
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

# Thermodynamics of Spacetime: The Einstein Equation of State

> [!info] Citation
> Jacobson, Ted (1995). "Thermodynamics of Spacetime: The Einstein Equation of State." *Physical Review Letters* **75**(7), 1260–1263. DOI: 10.1103/PhysRevLett.75.1260. arXiv:gr-qc/9504004.

## TL;DR
Jacobson derives the Einstein field equation from thermodynamic first principles alone — specifically from the proportionality of entropy to horizon area and the Clausius relation $\delta Q = T\,dS$ applied to all local Rindler causal horizons. The key insight is that demanding this relation hold for every spacetime point, with heat defined as energy flux across a causal horizon and temperature as the Unruh temperature seen by an accelerated observer, forces the spacetime curvature to satisfy the Einstein equation. Viewed this way, the Einstein equation is an equation of state of spacetime, not a fundamental field equation to be quantized.

## Problem & setting
Classical general relativity already encodes thermodynamic structure: the four laws of black hole mechanics mirror the four laws of thermodynamics, and Hawking radiation confirms that this analogy is an identity. Jacobson reverses the standard logic: instead of deriving thermodynamic laws from the Einstein equation, he asks whether the Einstein equation itself can be derived from thermodynamic principles, and shows the answer is yes. Prior art includes Bekenstein's entropy-area proportionality (1973), Hawking radiation (1975), and Unruh's result that uniformly accelerated observers see the Minkowski vacuum as a thermal state at temperature $T = \hbar\kappa/2\pi$.

## Method
The derivation proceeds in four steps. First, heat is defined as energy flux $\delta Q = \int_H T_{ab}\chi^a d\Sigma^b$ across a local Rindler horizon $H$, where $\chi^a$ is the approximate boost Killing field and $T_{ab}$ is the matter stress-energy tensor. Second, the entropy of the system beyond the horizon is taken proportional to horizon area: $dS = \eta\,\delta A$. Third, the Unruh temperature $T = \hbar\kappa/2\pi$ is assigned to the system. Fourth, demanding $\delta Q = T\,dS$ for all local Rindler horizons through every spacetime point leads, via the Raychaudhuri equation

$$\frac{d\theta}{d\lambda} = -\tfrac{1}{2}\theta^2 - \sigma^2 - R_{ab}k^ak^b,$$

to the requirement $T_{ab}k^ak^b = (\hbar\eta/2\pi)R_{ab}k^ak^b$ for all null $k^a$, which implies

$$R_{ab} - \tfrac{1}{2}Rg_{ab} + \Lambda g_{ab} = \frac{2\pi}{\hbar\eta}T_{ab}.$$

Newton's constant is identified as $G = (4\hbar\eta)^{-1}$, fixing the Planck-scale cutoff $\eta^{-1/2} \sim 2\ell_{\rm Pl}$.

## Key results
The Einstein equation emerges as a thermodynamic equation of state from (i) entropy proportional to area, (ii) $\delta Q = T\,dS$ with Unruh temperature, applied to all local Rindler horizons. The cosmological constant $\Lambda$ appears as an undetermined integration constant. Modifying the entropy functional (e.g., to a polynomial in the Ricci scalar) produces the corresponding higher-curvature field equations, suggesting a general correspondence between entropy density and gravitational action. The derivation implies that quantizing the Einstein equation may be as misguided as quantizing the wave equation for sound: gravity is a collective/hydrodynamic phenomenon at the thermodynamic level, not a fundamental quantum field.

## Relevance to this research
This paper is a foundational reference for the participatory/quantum-foundations cluster because it exemplifies the "physics from information" programme: macroscopic laws (gravity) emerge from microscopic information-theoretic or thermodynamic constraints rather than being independently fundamental. The derivation's structure — demanding a variational principle ($\delta Q = T\,dS$) hold everywhere and deriving field equations as its consequence — parallels the VFE programme's logic of deriving attention/transport equations as stationary points of a free-energy functional. The entropy-area proportionality and Unruh temperature are direct precursors to Verlinde's entropic gravity and to the holographic/entanglement perspectives that underlie participatory realism. The conclusion that the Einstein equation should not be canonically quantized resonates with the stance in the PIFB manuscript that certain macroscopic equations are emergent equations of state rather than fundamental quantum objects.

## Cross-links
- Concepts: [[jacobson-1995-einstein-equation-of-state|Thermodynamics of Spacetime]], [[Unruh Effect]], [[Horizon thermodynamics|Horizon Entropy]], [[Emergent spacetime and holography|Holographic Principle]], [[verlinde-2011-entropic-gravity|Entropic Gravity]], [[Emergent spacetime and holography]], [[Participatory realism (it from bit)]]
- Related sources: [[jacobson-2016-entanglement-equilibrium]], [[verlinde-2011-entropic-gravity]], [[padmanabhan-2010-thermodynamical-gravity|padmanabhan-2010-thermodynamic-gravity]], [[faulkner-2014-gravitation-from-entanglement]], [[wheeler-1990-it-from-bit]]
- Manuscript/Project: [[VFE Transformer Program]], [[Participatory realism (it from bit)|PIFB]]

## BibTeX
```bibtex
@article{Jacobson1995,
  author  = {Jacobson, Ted},
  title   = {Thermodynamics of Spacetime: {The} {Einstein} Equation of State},
  journal = {Physical Review Letters},
  volume  = {75},
  number  = {7},
  pages   = {1260--1263},
  year    = {1995},
  doi     = {10.1103/PhysRevLett.75.1260},
  eprint  = {gr-qc/9504004},
  archivePrefix = {arXiv},
  primaryClass  = {gr-qc},
}
```
