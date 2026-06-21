---
type: paper
title: "Near-field interferometry of a free-falling nanoparticle from a point-like source"
aliases:
  - "Bateman 2014"
  - "Bateman nanoparticle interferometry"
authors:
  - Bateman, James
  - Nimmrichter, Stefan
  - Hornberger, Klaus
  - Ulbricht, Hendrik
year: 2014
arxiv: null
url: https://doi.org/10.1038/ncomms5788
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Near-field interferometry of a free-falling nanoparticle from a point-like source

> [!info] Citation
> Bateman, J., Nimmrichter, S., Hornberger, K., & Ulbricht, H. (2014). "Near-field interferometry of a free-falling nanoparticle from a point-like source." *Nature Communications*, 5:4788. https://doi.org/10.1038/ncomms5788

## TL;DR
This paper proposes a near-field (Talbot-effect) matter-wave interferometry scheme for silicon nanoparticles of approximately one million atomic mass units, delocalized over 4150 nm. An optically trapped and feedback-cooled particle is released, diffracted by a single standing-wave laser pulse, and its arrival position recorded on a glass slide. Full decoherence analysis shows the scheme is feasible with present-day technology and is already sensitive to wave-function collapse models such as CSL.

## Problem & setting
Testing the quantum superposition principle at macroscopic mass scales requires delocalization of objects far heavier than molecules, but environmental decoherence (gas collisions, thermal blackbody radiation) destroys coherence rapidly at large masses. Prior proposals for nanoparticle interferometry either required motional ground-state cooling (experimentally very demanding) or involved silica particles where radiative decoherence is severe. The authors seek a scheme requiring only moderate motional cooling and operating at room temperature.

## Method
The scheme uses the single-source near-field Talbot effect. A silicon nanoparticle (~10^6 AMU, radius ~100 nm) is optically trapped at 1550 nm, parametric feedback-cooled to T = 20 mK along the horizontal axis, then released to free-fall 125 mm before encountering a phase grating formed by a retro-reflected 355 nm nanosecond laser pulse. The grating imprints a phase φ(x) = φ₀ cos²(πx/d) on the matter wave. After a further 126 ms free fall the particle deposits on a glass slide and its position is recorded with 100 nm optical-microscopy accuracy.

The theoretical framework works in the Wigner/characteristic-function representation. The initial Gaussian thermal state evolves freely, is acted on by the grating (Talbot coefficients B_n expressed in Bessel functions), evolves freely again, and yields the fringe density

w(x) ∝ Σ_n B_n[n t₁ t₂ / (t_T (t₁+t₂))] exp[2πinx/D − 2π²n²σ_x²t₂² / (d²(t₁+t₂)²)]

with geometric magnification D = d(t₁+t₂)/t₁. Decoherence from residual gas collisions, blackbody absorption/emission, and photon scattering is incorporated multiplicatively as Fourier-mode reduction factors R_n. Silicon is chosen because its low blackbody emissivity keeps radiative decoherence negligible up to internal temperatures of ~1000 K, in contrast to silica which requires cryogenic cooling.

## Key results
Simulated fringe visibilities reach up to 75–83% for 10^6 AMU silicon particles under realistic experimental parameters (10^{-10} mbar vacuum, T_initial = 20 mK, φ₀ = 1.4π). The quantum and classical (ballistic) fringe patterns are clearly distinguishable in their φ₀-dependence. The scheme corresponds to a macroscopicity value m = 18, exceeding all present matter-wave experiments. A successful interference demonstration with visibility > 42% would bound the CSL localization rate to λ_CSL < 1.4 × 10^{-11} Hz, constraining current CSL parameter estimates.

## Relevance to this research
This paper is primarily an experimental quantum optics proposal. Its direct relevance to the VFE/gauge-theoretic program is peripheral but real: it bears on the quantum-foundations context motivating participatory realism and the measurement problem. The paper probes precisely the regime where wave-function collapse models (CSL) become testable, which is the macroscopic quantum-to-classical transition that participatory and relational interpretations of quantum mechanics aim to explain ontologically. It also uses quantum phase-space (Wigner/characteristic-function) methods analogous to the Gaussian belief geometry used throughout the VFE framework.

## Cross-links
- Concepts: [[Quantum superposition|Quantum Superposition Principle]], [[Wave-Function Collapse]], [[CSL model|Continuous Spontaneous Localization]]
- Related sources: [[bassi-2013-collapse-models]]
- Manuscript/Project: [[participatory-it-from-bit|Participatory It from Bit]]

## BibTeX
```bibtex
@article{Bateman2014,
  author  = {Bateman, James and Nimmrichter, Stefan and Hornberger, Klaus and Ulbricht, Hendrik},
  title   = {Near-field interferometry of a free-falling nanoparticle from a point-like source},
  journal = {Nature Communications},
  year    = {2014},
  volume  = {5},
  pages   = {4788},
  doi     = {10.1038/ncomms5788},
}
```
