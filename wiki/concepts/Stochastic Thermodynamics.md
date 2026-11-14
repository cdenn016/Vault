---
type: concept
title: "Stochastic Thermodynamics"
tags:
  - cluster/vfe
  - cluster/participatory/quantum-foundations
  - project/multi-agent
status: draft
created: 2026-06-21
updated: 2026-11-13
---

# Stochastic Thermodynamics

## Definition

Stochastic thermodynamics extends heat, work and entropy production to small systems in which fluctuations dominate, by defining these quantities along individual stochastic trajectories. Levitated optomechanical particles are a controlled setting for nanoscale thermodynamics and stochastic heat engines ([[millen-2020-levitated-optomechanics]]). The central quantity for a stationary Markov process is the entropy production rate, the relative entropy per unit time between the path measure of the process and that of its time reversal, $e_p=\frac{1}{t}H[P_{[0,t]}\mid\bar P_{[0,t]}]$, which vanishes exactly at detailed balance ([[dacosta-2023-entropy-production-stationary-diffusions|Da Costa and Pavliotis 2023]]).

## Details

For a stationary diffusion whose time reversal is again a diffusion, Da Costa and Pavliotis prove that when the time-irreversible drift $b_{\mathrm{irr}}$ lies in the range of the volatility almost everywhere, with an integrability or martingale condition, the forward and backward path measures are equivalent and

$$e_p=\int b_{\mathrm{irr}}^\top D^-b_{\mathrm{irr}}\rho dx,$$

with $D^-$ the Moore-Penrose pseudo-inverse of the diffusion tensor. When the range condition fails on a set of positive stationary measure the paper states $e_p=+\infty$ (Theorem 4.4). Underdamped Langevin dynamics therefore has infinite entropy production under this definition and zero under a generalized rate that applies the momentum flip to the reversed path; the theorems concern the unflipped definition.

The rate splits in several ways. [[feng-2011-potential-flux-decomposition|Feng and Wang 2011]] obtain $\dot S=e_p-\dot S_m$ and $Te_p=Q_{hk}-\dot F_{\mathrm{free}}$, with $F_{\mathrm{free}}=T\langle\ln(P/P^{SS})\rangle$, as equal-time limits of a generalized fluctuation-dissipation relation whose extra terms are carried by the steady-state flux, and they identify the medium entropy around a closed loop, up to a factor, with the flux of the curvature of an abelian connection through that loop; the letter omits most derivation steps. [[sakthivadivel-2026-markov-interacting-particles|Sakthivadivel 2026]] proves the stationary formula $e_p=\int J_\pi^\top D^\dagger J_\pi/\pi dx$ and a split of dissipation into housekeeping and excess parts in which the excess part is minus the rate of change of relative entropy to the stationary law. Proposition 12.6 of that paper shows that an exact path-space Markov boundary does not imply zero entropy production, nor the converse, so the quality of a boundary and irreversibility are logically independent; the author adds that a small conditional information gap does not imply small housekeeping heat.

For jump processes on a graph, [[polettini-2012-nonequilibrium-thermodynamics-gauge|Polettini 2012]] derives Schnakenberg's total entropy production $\sigma_{\mathrm{tot}}=\sum_{i<j}J_{ij}\log(w_{ij}\rho_j/w_{ji}\rho_i)$ as the simplest completion of the Gibbs entropy rate that is invariant under local rescaling $\rho_i\to e^{-\varphi_i}\rho_i$ of the density, read as a change of prior, and that does not vanish at the steady state. The thermodynamic force $A_{ij}=\log(w_{ij}/w_{ji})$ is the gauge potential, and the gauge choice $\varphi_i=\log\rho^*_i$ yields the adiabatic and non-adiabatic split (see [[Gauge transformation]] and [[Holonomy]]).

[[ueltzhoffer-2021-thermodynamic-efficiency-dissipative|Ueltzhöffer et al. 2021]] is a simulation study of a designed chemical reaction network in which competing nonequilibrium steady states lose stability, as the driving gradient is lowered, in order of the efficiency of their work-harvesting process, least efficient first. The result is numerical and specific to that network, the hierarchy of dissipative structures in the paper is argued without simulation, and no Markov blanket is used.

## In this work

> [!note] Editorial: bearing on the gauge-theoretic program
> These results concern physical states of one system, and their relation to belief dynamics on statistical fibers is interpretive. Two cautions carry over. A dissipation claim for inertial [[Hamiltonian belief dynamics]] with noise on the momenta alone would need the momentum-flipped entropy production, since for underdamped Langevin dynamics, the case the paper treats, the unflipped rate is infinite. Proposition 12.6 of Sakthivadivel 2026 implies that adding conservative currents to belief dynamics does not by itself decide whether a [[Markov Blanket]] of an agent or a collective holds. The gauge reading of entropy production is an abelian analogy to the nonabelian transport of the program and not a shared theorem.

## Related

[[Nonequilibrium steady state]], [[Bayesian mechanics]], [[Variational free energy]], [[Entropy]], [[Optomechanics]], [[Free-energy principle active inference]], [[Holonomy]], [[Gauge transformation]]

## Sources

- [[millen-2020-levitated-optomechanics]] — review of levitated particles, including nanoscale thermodynamics and stochastic heat engines.
- [[dacosta-2023-entropy-production-stationary-diffusions]] — entropy production of stationary diffusions; finite under the range condition, infinite otherwise.
- [[feng-2011-potential-flux-decomposition]] — flux decomposition identities; housekeeping and free-energy relaxation; loop entropy as curvature flux.
- [[polettini-2012-nonequilibrium-thermodynamics-gauge]] — entropy production as gauge-invariant completion of the entropy rate under change of prior.
- [[sakthivadivel-2026-markov-interacting-particles]] — housekeeping and excess split; boundary quality independent of entropy production.
- [[ueltzhoffer-2021-thermodynamic-efficiency-dissipative]] — simulated chemical network whose steady states lose stability in order of efficiency.
