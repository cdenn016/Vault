---
type: paper
title: "Towards Quantum Superpositions of a Mirror"
aliases:
  - "Marshall 2003"
  - "mirror superposition"
authors:
  - Marshall, William
  - Simon, Christoph
  - Penrose, Roger
  - Bouwmeester, Dik
year: 2003
arxiv: quant-ph/0210001
url: https://arxiv.org/abs/quant-ph/0210001
tags:
  - cluster/participatory/quantum-foundations
  - project/multi-agent
  - field/physics
status: stable
created: 2026-06-20
updated: 2026-06-20
---

# Towards Quantum Superpositions of a Mirror

> [!info] Citation
> Marshall, W., Simon, C., Penrose, R., & Bouwmeester, D. (2003). "Towards Quantum Superpositions of a Mirror." *Physical Review Letters* 91, 130401. arXiv:quant-ph/0210001.

## TL;DR
The authors propose a concrete experimental scheme for creating quantum superposition states of a macroscopic mirror (containing ~10^14 atoms) by coupling a single photon via radiation pressure in a high-finesse Michelson interferometer cavity. The photon interference visibility exhibits a sharp revival after one full mechanical period, and the magnitude of this revival directly witnesses the decoherence of the mirror superposition. All experimental requirements are argued to be within reach of current technology.

## Problem & setting
Schrödinger's 1935 cat paradox raises the question of whether macroscopic objects can genuinely exist in quantum superpositions, or whether some unconventional decoherence mechanism (gravitationally induced collapse, spontaneous wave-function reduction à la Penrose–Diosi) intervenes at mesoscopic scales. Prior work demonstrated superpositions in superconducting devices and fullerene molecules but remained far from truly macroscopic systems. This proposal targets a mirror nine orders of magnitude more massive than any superposition demonstrated to date, bridging the gap toward testing fundamental decoherence models.

## Method
A single photon enters a Michelson interferometer whose arm A contains a high-finesse cavity with a tiny mirror (10×10×10 µm, mass ~5×10^{-12} kg) mounted on a micromechanical oscillator. The radiation pressure of the photon displaces the mirror, entangling the photon's path degree of freedom with the mirror's center-of-mass motion. The system Hamiltonian is the standard optomechanical form

$$H = \hbar\omega_c a^\dagger a + \hbar\omega_m b^\dagger b - \hbar g a^\dagger a (b + b^\dagger),$$

with coupling $g = (\omega_c/L)\sqrt{\hbar/2M\omega_m}$. The dimensionless displacement parameter $\kappa = g/\omega_m$ quantifies the separation of the two mirror branches in units of the coherent-state wavepacket width. After a full mechanical period $t = 2\pi/\omega_m$ the photon and mirror disentangle, producing a sharp revival of photon interference visibility. For a thermal initial mirror state, the revival amplitude decays only due to environmental decoherence (modeled as an Ohmic bath with rate $\gamma_D = \gamma_m k T M (\Delta x)^2/\hbar^2$), not due to thermal averaging of phases. The condition $\kappa^2 \gtrsim 1$ requires mirror quality factor $Q \gtrsim \bar{n} = k_B T/\hbar\omega_m$, achieved with $Q\sim10^5$ silicon cantilevers at $T \lesssim 3$ mK. Proposed oscillator frequency is $\omega_m = 2\pi \times 500$ Hz, with $N \approx 5.6\times10^6$ photon round-trips per period.

## Key results
The off-diagonal element of the photon's reduced density matrix (interference visibility divided by 2) evolves as

$$\tfrac{1}{2}\exp\!\bigl[-\kappa^2(2\bar{n}+1)(1-\cos\omega_m t)\bigr]\,e^{i\kappa^2(\omega_m t - \sin\omega_m t)},$$

decaying rapidly after $t=0$ for large thermal occupation $\bar{n}$, but reviving sharply to its full (decoherence-free) value at $t = 2\pi/\omega_m$. The width of the revival peak scales as $1/\sqrt{T}$, motivating operation at the lowest achievable temperature (60 µK demonstrated with nuclear demagnetization cryostats). Environmental decoherence suppresses the revival amplitude; a ratio $Q/T$ improved by five orders of magnitude beyond the discussed values would allow the Penrose gravitational-decoherence rate to compete with environmental decoherence. A detection rate of ~100 photons/hour in the revival window is estimated, making ~10-minute measurement runs statistically viable.

## Relevance to this research
This paper is directly relevant to the participatory-realism and quantum-foundations thread of the research program. Penrose is a co-author, and the proposal is explicitly designed to test the Penrose–Diosi gravitational wave-function collapse model — the same objective-collapse framework that motivates the participatory "it-from-bit" ontology and the role of observer-dependent reality in the PIFB manuscript. The decoherence revival structure (sudden loss of coherence followed by exact recovery at the mechanical period) is formally analogous to the time-reversal and revival structure that appears in VFE belief-state dynamics under cyclic transport. The use of a single photon to probe entanglement with a many-body system (mirror) mirrors the structure of a single agent updating beliefs coupled to a large environmental prior, and the quantification of decoherence through off-diagonal density-matrix elements maps directly onto the KL-divergence loss of coherence between transported belief states $\Omega_{ij} q_j$ and $q_i$ in the GL(K) attention framework.

## Cross-links
- Concepts: [[Quantum Decoherence]], [[Wavefunction Collapse]], [[Participatory Realism]], [[Optomechanics]]
- Related sources: [[penrose-2000-mathematical-physics]], [[diosi-1989-gravity-collapse]]
- Manuscript/Project: [[PIFB]], [[VFE Transformer Program]]

## BibTeX
```bibtex
@article{Marshall2003,
  author  = {Marshall, William and Simon, Christoph and Penrose, Roger and Bouwmeester, Dik},
  title   = {Towards Quantum Superpositions of a Mirror},
  journal = {Physical Review Letters},
  volume  = {91},
  pages   = {130401},
  year    = {2003},
  eprint  = {quant-ph/0210001},
  archivePrefix = {arXiv},
}
```
