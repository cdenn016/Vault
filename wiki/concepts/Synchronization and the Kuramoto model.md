---
type: concept
title: "Synchronization and the Kuramoto model"
aliases:
  - "Kuramoto model"
  - "Synchronization"
  - "Coupled oscillators"
  - "Phase locking"
tags:
  - cluster/social-physics
  - project/social-physics
status: stable
created: 2026-06-19
updated: 2026-11-18
---

# Synchronization and the Kuramoto model

## Definition

**Synchronization** is the spontaneous adjustment of rhythms among coupled self-sustained oscillators, each of which would, in isolation, run at its own natural frequency. When the coupling is strong enough to overcome the spread of those natural frequencies, a macroscopic fraction of the population locks to a common rhythm — a cooperative, emergent order rather than anything imposed from outside. The textbook treatment ([[pikovsky-rosenblum-kurths-2001-synchronization]]) frames the subject as a universal phenomenon across physics, chemistry, biology, and engineering, built up from the synchronization of two coupled periodic oscillators (phase-locking, frequency entrainment, and the wedge-shaped Arnold tongues in the coupling–detuning plane) through noisy and chaotic systems to collective synchrony in large ensembles.

The canonical mathematical model of the large-ensemble case is the **Kuramoto model**. Each of $N$ oscillators is reduced to a single phase $\theta_i$ on the circle, carrying a quenched natural frequency $\omega_i$ drawn from a distribution $g(\omega)$, and all pairs are coupled through a sinusoid of their phase difference,
$$ \dot\theta_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i). $$
The decisive step ([[kuramoto-1975-coupled-oscillators]]) is to define the complex **order parameter** $r e^{i\psi} = \frac{1}{N}\sum_j e^{i\theta_j}$, whose magnitude $r \in [0,1]$ measures phase coherence ($r=0$ incoherent, $r=1$ fully locked). Substituting it collapses the all-to-all sum into a mean-field self-coupling, $\dot\theta_i = \omega_i + K r \sin(\psi - \theta_i)$: every oscillator feels only the population's mean field of amplitude $r$. Solving the self-consistency condition for $r$ in the $N\to\infty$ limit gives a continuous (second-order) phase transition at a critical coupling $K_c = 2/[\pi g(0)]$ for a unimodal symmetric $g$. Below $K_c$ only the incoherent state $r=0$ survives; above it a partially synchronized branch appears, growing as $r \sim \sqrt{K-K_c}$. The conceptual origin of this threshold picture — incoherent population versus mutually entrained population — predates Kuramoto in [[winfree-1967-coupled-oscillators]], who separated each oscillator's outgoing influence from its phase sensitivity and identified the cooperative transition that Kuramoto's all-to-all sinusoidal model later made exactly solvable.

## Details

The substantive content of the synchronization literature relevant here organizes into four layers. The **mean-field self-consistency** layer is Kuramoto's original move: with the order parameter $r e^{i\psi}$ absorbing the coupling, oscillators split into a locked group (those with $|\omega_i - \psi| \le K r$, which settle to fixed phase offsets) and a drifting group (those whose natural frequency is too far from the mean field), and demanding that the locked group reproduce the very $r$ that organizes them yields the self-consistency relation $r = K r \int_{-\pi/2}^{\pi/2}\cos^2\theta\, g(K r \sin\theta)\, d\theta$, whose nontrivial branch is the supercritical $r \sim \sqrt{K-K_c}$ near onset ([[kuramoto-1975-coupled-oscillators]], [[strogatz-2000-kuramoto-to-crawford]]).

The **stability and bifurcation** layer makes that calculation rigorous. The subtlety, emphasized by [[strogatz-2000-kuramoto-to-crawford]], is that the incoherent state is only neutrally (marginally) stable below $K_c$ — its linearization has a continuous spectrum on the imaginary axis rather than a discrete set of decaying modes — so naive linear stability is inconclusive. Crawford's amplitude-equation / center-manifold treatment, working from the continuity equation for the oscillator density $\rho(\theta,\omega,t)$, resolves the nature of the branching synchronized solutions and shows how even a little noise regularizes the spectrum and restores ordinary stability.

The **kinetic / noisy** layer promotes the model to a stochastic system. Adding white noise of strength $D$ to each phase gives a single-oscillator density obeying a nonlinear Fokker–Planck equation,
$$ \partial_t \rho = D\,\partial_\theta^2 \rho - \partial_\theta\!\big[(\omega + K r \sin(\psi-\theta))\,\rho\big], $$
self-consistently closed through $r e^{i\psi} = \int e^{i\theta}\rho(\theta,\omega,t)\, g(\omega)\, d\theta\, d\omega$ ([[acebron-2005-kuramoto-review]]). This population-density description, together with finite-$N$ scaling of fluctuations and the reshaping of $K_c$ by network topology (degree heterogeneity, small-world, scale-free graphs), is the machinery for noisy collective dynamics on a coupling graph.

The **phase-reduction and two-oscillator** layer underpins all of the above. Reducing a weakly perturbed limit-cycle oscillator to a single phase governed by $\dot\phi = \omega + \varepsilon Q(\phi)$, and analyzing the phase-difference dynamics $\dot\psi = \Delta\omega - \varepsilon q(\psi)$ of a pair, yields the picture of stable locked solutions inside Arnold tongues, forced synchronization, and noise-induced phase slips (effective diffusion of the phase difference) ([[pikovsky-rosenblum-kurths-2001-synchronization]]). The historical root of the whole edifice remains [[winfree-1967-coupled-oscillators]]'s influence/sensitivity decomposition $\dot\theta_i = \omega_i + Z(\theta_i)\sum_j X(\theta_j)$ and its thermodynamic-style entrainment threshold, of which the Kuramoto model is the exactly-solvable specialization.

Collectively these results place synchronization within the broader theme of [[Statistical physics of social systems and collective behavior]]: a population of disordered units, a coupling that competes against that disorder, an order parameter, and a phase transition to emergent collective order.

## Sources

- [[kuramoto-1975-coupled-oscillators]] — the founding all-to-all sinusoidal phase model, the complex order parameter, and the mean-field critical coupling $K_c = 2/[\pi g(0)]$.
- [[winfree-1967-coupled-oscillators]] — the conceptual origin: influence/sensitivity split and the cooperative entrainment threshold for a dispersed-frequency population.
- [[strogatz-2000-kuramoto-to-crawford]] — analytical review of synchronization onset, marginal stability of the incoherent state, and Crawford's bifurcation treatment.
- [[acebron-2005-kuramoto-review]] — the definitive survey, including the nonlinear Fokker–Planck / population-density formulation and network-coupled, noisy, finite-$N$ extensions.
- [[pikovsky-rosenblum-kurths-2001-synchronization]] — the canonical textbook: phase reduction, phase-locking, Arnold tongues, noise-induced phase slips, and ensemble synchrony.

## See also

- [[Opinion dynamics]]
- [[Echo chambers and polarization]] — the fragmented (incoherent) phase of the coupling-driven transition.
- [[Renormalization group flow]]
- [[Sociophysics]]
