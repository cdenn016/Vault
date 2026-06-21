---
type: paper
title: "Optomechanics with Levitated Particles"
aliases:
  - "Millen 2020"
  - "levitated optomechanics review"
authors:
  - Millen, James
  - Monteiro, Tania S.
  - Pettit, Robert
  - Vamivakas, A. Nick
year: 2020
arxiv: "1907.08198"
url: https://doi.org/10.1088/1361-6633/ab8bernull
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
  - field/mathematics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Optomechanics with Levitated Particles

> [!info] Citation
> Millen, J., Monteiro, T. S., Pettit, R., & Vamivakas, A. N. (2020). "Optomechanics with Levitated Particles." arXiv:1907.08198v2 [physics.optics].

## TL;DR
This is a comprehensive review of levitated optomechanics — the use of tightly focused optical fields to trap micro- and nano-particles in vacuum, isolating them from thermal contact with the environment. The central thrust is that levitated particles constitute ultra-low-dissipation oscillators (quality factors reaching ~10^8 at 10^{-6} mbar) that can be cooled to sub-millikelvin temperatures via feedback or cavity coupling, opening a realistic pathway to quantum superposition of macroscopic (>10^6 amu) objects. The review covers the classical stochastic mechanics of the trapped oscillator, thermodynamics and stochastic heat engines at the nanoscale, active and parametric feedback cooling, force sensing at the zeptonewton level, and quantum-regime proposals including interferometry, decoherence testing, and wavefunction-collapse models.

## Problem & setting
Standard solid-state nanomechanical oscillators (tethered resonators) suffer mechanical quality factors that scale as the cube root of volume and require cryogenic operation to reduce thermal noise. Levitated optomechanics breaks this constraint: the mechanical mode is centre-of-mass motion of an isolated particle, so clamping losses vanish entirely and only gas collisions and photon shot noise remain as dissipation channels, both of which are suppressed in vacuum. The key challenge addressed is cooling the levitated oscillator from room temperature to near the motional ground state, enabling force sensing, thermodynamic experiments, and tests of macroscopic quantum mechanics.

## Method
The review builds from first principles. The optical gradient force on a sub-wavelength dielectric sphere is derived from its complex polarizability

$$\alpha(\omega_L) = 4\pi\epsilon_0 R^3 \frac{\epsilon_r(\omega_L)-1}{\epsilon_r(\omega_L)+2},$$

yielding a harmonic restoring force with spring constants $k_q \propto \alpha' P_\text{opt}/w_q^2$. The equation of motion for each centre-of-mass coordinate is a damped harmonic oscillator driven by Gaussian noise (Langevin equation), with total damping $\Gamma_\text{CM}$ receiving contributions from gas collisions (Epstein formula, transitioning to Knudsen-regime linear-in-pressure scaling at $P_\text{gas} \lesssim 54.4$ mbar/$R[\mu\text{m}]$) and photon recoil noise. The power spectral density $S_{qq}(\omega) \propto \Gamma_\text{CM}/[(ω^2-ω_q^2)^2 + \Gamma_\text{CM}^2 \omega^2]$ serves as the primary experimental observable for extracting $T_\text{CM}$.

Feedback cooling enters by adding a term $u_\text{fb}(t) = G_{\dot{q}}\dot{q}(t)$ (cold damping) or $G_\text{nl} q(t)\dot{q}(t)$ (parametric/nonlinear feedback) to the Langevin equation, reducing the effective temperature to $T_\text{eff} = T_0 \,\Gamma_\text{CM}/(\Gamma_\text{CM}+\delta\Gamma)$. For nonlinear feedback, the phonon occupation satisfies a nonlinear rate equation $\langle\dot{n}_m\rangle = B\langle n_m\rangle^2 - C\langle n_m\rangle + A$, predicting that ground-state cooling is achievable at pressures $\lesssim 10^{-5}$ mbar. The minimum detectable force is $F_\text{min} = \sqrt{4k_BT_\text{CM}M\Gamma_\text{CM}b}$, achieved by levitated systems at the $10^{-21}$ N Hz$^{-1/2}$ scale.

## Key results
Levitated nanoparticles achieve mechanical quality factors $Q_m \sim 10^8$ at $10^{-6}$ mbar, far exceeding the cube-root-of-volume trend of tethered resonators. Parametric feedback cooling has cooled a 70 nm nanoparticle to 50 mK. Linear feedback with Coulomb actuation has reached occupancies below 20 phonons. Force sensitivities of 1.6 aN Hz$^{-1/2}$ have been demonstrated with charged levitated microspheres, with averaging reaching the 6 zN level. The photon recoil heating rate $\Gamma_\text{rad}$ was directly measured and confirmed as the dominant damping mechanism below $10^{-6}$ mbar. The Kramers turnover — the transition between underdamped and overdamped escape rates — was first experimentally verified in a levitated system. The review also surveys quantum interferometry proposals, decoherence models (Continuous Spontaneous Localization, Diósi-Penrose gravitational collapse), and spin-mechanical coupling via NV centres in levitated nanodiamonds.

## Relevance to this research
The connection to the VFE transformer / GL(K) gauge-equivariant attention program is indirect. Levitated optomechanics is not related to gauge theory, information geometry, or variational free energy in any direct sense. The tangential relevances are: (1) stochastic oscillator dynamics under a Langevin equation is mathematically analogous to diffusion in belief space that underlies predictive-coding and VFE update rules — both are Ornstein-Uhlenbeck-type processes with noise-temperature tradeoffs; (2) the stochastic heat-engine and Kramers-escape literature overlaps with the fluctuation-theorem / non-equilibrium thermodynamics perspective that informs some active-inference formulations of free energy; (3) proposals for macroscopic quantum superposition and wavefunction-collapse testing (CSL, Diósi-Penrose) are adjacent to participatory-realism and quantum-foundations discussions in the PIFB manuscript. In summary, this paper is primarily relevant as background reading for the quantum-foundations / participatory cluster, not for the VFE attention mechanism itself.

## Cross-links
- Concepts: [[Stochastic Thermodynamics]], [[Quantum Foundations]], [[Free Energy]]
- Related sources: [[participatory-realism]]
- Manuscript/Project: [[PIFB]]

## BibTeX
```bibtex
@article{Millen2020,
  author  = {Millen, James and Monteiro, Tania S. and Pettit, Robert and Vamivakas, A. Nick},
  title   = {Optomechanics with Levitated Particles},
  journal = {arXiv preprint},
  year    = {2020},
  eprint  = {1907.08198},
  archivePrefix = {arXiv},
  primaryClass  = {physics.optics},
}
```
