---
type: paper
title: "Cooling of a Levitated Nanoparticle to the Motional Quantum Ground State"
aliases:
  - "Delic 2020"
  - "levitated nanoparticle ground state"
authors:
  - Delic, Uros
  - Reisenbauer, Manuel
  - Dare, Kahan
  - Grass, David
  - Vuletic, Vladan
  - Kiesel, Nikolai
  - Aspelmeyer, Markus
year: 2020
arxiv: "1911.04406"
url: https://doi.org/10.1126/science.aba3993
tags:
  - cluster/participatory/quantum-foundations
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Cooling of a Levitated Nanoparticle to the Motional Quantum Ground State

> [!info] Citation
> Delic, U., Reisenbauer, M., Dare, K., Grass, D., Vuletic, V., Kiesel, N., and Aspelmeyer, M. (2020). "Cooling of a Levitated Nanoparticle to the Motional Quantum Ground State." *Science* 367(6480), 892–895. https://doi.org/10.1126/science.aba3993

## TL;DR
This paper reports the first demonstration of quantum ground-state cooling of an optically levitated solid-state object — a 143 nm diameter silica nanoparticle (~10^8 atoms, ~2×10^9 a.m.u.) — in a room-temperature environment. Using cavity cooling by coherent scattering into an optical cavity, the center-of-mass motion along the cavity axis is cooled by more than 7 orders of magnitude to a mean phonon occupation of n_x = 0.43 ± 0.03, corresponding to 12 µK and a 70% ground-state probability, with a coherence time of 7.6 µs (approximately 15 coherent oscillations). This establishes levitated optomechanics as a viable platform for controlling quantum states of macroscopic objects at unprecedented mass scales.

## Problem & setting
A central open question in quantum foundations is whether quantum laws hold universally or whether a classical macrorealistic description must emerge for sufficiently large systems. Levitated nanoparticles in high vacuum are attractive for probing this boundary because optical trapping provides mechanical isolation that is not available to clamped oscillators, and free-fall dynamics can greatly extend coherence once the trap is switched off. Prior attempts at cavity cooling levitated solids were limited to hundreds of phonons due to co-trapping issues and excessive laser phase noise at low motional frequencies. The paper builds on the coherent-scattering cavity cooling technique (Delic et al., PRL 2019; Windey et al., PRL 2019), which avoids these problems by positioning the particle at a cavity node to suppress elastic scattering, so that only motionally inelastic Stokes and anti-Stokes sidebands couple to the cavity.

## Method
A 143 nm silica sphere is optically trapped by a 1064 nm Nd:YAG tweezer (P ≈ 400 mW) at motional frequencies (Ω_x, Ω_y, Ω_z)/2π ≈ (305, 275, 80) kHz, positioned at a node of a high-finesse optical cavity (F ≈ 73,000; linewidth κ/2π = 193 kHz) under the resolved-sideband condition κ < Ω_x. The tweezer laser is red-detuned from cavity resonance by Δ ≈ Ω_x so that anti-Stokes scattering (removing one phonon per photon) becomes resonant while Stokes scattering (adding phonons) is suppressed. Thermometry is performed by sideband asymmetry: the ratio of anti-Stokes to Stokes scattered power in heterodyne detection directly encodes n_x without calibration to a reference bath:

S_het(Ω_x)/S_het(−Ω_x) = [n_x/(n_x+1)] × [cavity envelope correction].

The minimum phonon occupation achievable in the resolved-sideband limit is n_min = (κ/4Ω_x)^2 ≈ 0.025. Actual performance is limited by gas-collision heating Γ_gas/2π = 16.1 kHz, photon recoil Γ_rec/2π ≈ 6 kHz, and (negligible) laser phase noise at 10^−6 mbar.

## Key results
At optimal detuning Δ/2π = 315 kHz, the final phonon occupation is n_x = 0.43 ± 0.03, giving a ground-state probability of 70 ± 2% and a temperature of 12.2 ± 0.5 µK. The total heating rate is Γ_x/2π = 20.6 ± 2.3 kHz, yielding a coherence time of 7.6 ± 1 µs (≈15 coherent oscillations) in the optical trap. The inferred optomechanical cooperativity is C = 4g_x^2/(κΓ_x) ≈ 5, placing the system firmly in the strong-cooperativity regime. Free-fall decoherence at this pressure is dominated by background-gas localization, limiting wavepacket expansion to ~10 pm; reaching particle-radius (~70 nm) superpositions would require pressures below 2×10^−11 mbar combined with cryogenic temperatures (< 130 K) to suppress blackbody decoherence from the internally hot particle.

## Relevance to this research
The primary connection to this research program is through the participatory realism and quantum foundations thread. The paper demonstrates quantum coherence (ground-state purity) of a macroscopic solid-state object with 10^8 atoms, directly probing the quantum-classical boundary and the universality of quantum superposition. The authors explicitly discuss the prospect of using such levitated quantum systems as gravitational source masses, citing Feynman's original suggestion from the 1957 Chapel Hill conference and the recent Bose et al. / Marletto–Vedral proposals for entanglement-based quantum gravity witnesses — both directly relevant to participatory quantum foundations and "it from bit" type questions about the role of quantum systems as physical realizers of information. The decoherence analysis (localization parameter Λ, wavepacket expansion in short- and long-distance gas-scattering regimes) is a concrete physical instantiation of the measurement-decoherence problem central to participatory realism. There is no direct connection to the VFE transformer, GL(K) attention, or social-physics threads.

## Cross-links
- Concepts: [[Quantum Decoherence]], [[Macroscopic Quantum Coherence]], [[Participatory Realism]]
- Related sources: [[bose-2017-quantum-gravity-entanglement]], [[marletto-2017-gravitationally-induced-entanglement]]
- Manuscript/Project: [[PIFB]]

## BibTeX
```bibtex
@article{Delic2020,
  author  = {Deli{\'c}, U. and Reisenbauer, M. and Dare, K. and Grass, D. and Vuleti{\'c}, V. and Kiesel, N. and Aspelmeyer, M.},
  title   = {Cooling of a levitated nanoparticle to the motional quantum ground state},
  journal = {Science},
  volume  = {367},
  number  = {6480},
  pages   = {892--895},
  year    = {2020},
  doi     = {10.1126/science.aba3993},
}
```
