---
type: paper
title: "Self-entrainment of a population of coupled non-linear oscillators"
aliases: ["Kuramoto 1975", "Kuramoto model (original)"]
authors: ["Kuramoto Y."]
year: 1975
url: https://doi.org/10.1007/BFb0013365
tags: [cluster/social-physics, project/social-physics, field/physics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Self-entrainment of a population of coupled non-linear oscillators

> [!info] Citation
> Kuramoto, Y. (1975). *Self-entrainment of a population of coupled non-linear oscillators*. In H. Araki (Ed.), International Symposium on Mathematical Problems in Theoretical Physics (Lecture Notes in Physics, vol. 39), Springer, pp. 420–422. DOI 10.1007/BFb0013365.

## TL;DR
Kuramoto reduces a generic population of weakly coupled limit-cycle oscillators, each with its own natural frequency, to a phase-only model in which every oscillator is pulled toward the population's mean phase. By choosing the all-to-all sinusoidal coupling, he obtains an exactly solvable mean-field model that undergoes a continuous phase transition: below a critical coupling the oscillators drift incoherently, and above it a macroscopic fraction spontaneously locks to a common frequency. This is the founding result of modern synchronization theory.

## What it establishes
The model governs $N$ phases $\theta_i$ with quenched natural frequencies $\omega_i$ drawn from a distribution $g(\omega)$,
$$ \dot\theta_i = \omega_i + \frac{K}{N}\sum_{j=1}^{N}\sin(\theta_j - \theta_i). $$
Kuramoto introduces the complex order parameter $r e^{i\psi} = \frac{1}{N}\sum_j e^{i\theta_j}$, which turns the all-to-all sum into a mean-field self-coupling $\dot\theta_i = \omega_i + K r \sin(\psi - \theta_i)$. Each oscillator feels only the mean field of amplitude $r$. Solving the self-consistency condition for $r$ in the $N\to\infty$ limit yields a critical coupling $K_c = 2/[\pi g(0)]$ (for unimodal symmetric $g$): for $K<K_c$ the incoherent state $r=0$ is the only solution, and for $K>K_c$ a partially synchronized branch with $r>0$ emerges, growing as $r \sim \sqrt{K-K_c}$. The transition is a genuine cooperative (mean-field, second-order) phase transition driven purely by coupling against frequency disorder.

## Relevance to this research
The Kuramoto model is the canonical exemplar of phase-locking, entrainment, and resonance in a coupled population, which is exactly the phenomenology the program's underdamped Hamiltonian belief regime predicts: oscillation, overshoot, and phase-locking of belief trajectories under $M\ddot\mu + \gamma\dot\mu + \nabla F = 0$. The mean-field order-parameter reduction is the physics analogue of asking what a population of momentum-carrying beliefs does collectively. The link is structural and inspirational rather than an identity — beliefs here are Gaussian tuples on a statistical manifold with gauge-transported coupling, not scalar phases on a circle — so the correspondence is at the level of phenomenology and mean-field method, not the same equations. See [[Hamiltonian belief dynamics]], [[Synchronization and the Kuramoto model]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Synchronization and the Kuramoto model]]
- Related sources: [[winfree-1967-coupled-oscillators]], [[strogatz-2000-kuramoto-to-crawford]], [[acebron-2005-kuramoto-review]]

## BibTeX
```bibtex
@incollection{kuramoto1975self,
  author    = {Kuramoto, Yoshiki},
  title     = {Self-entrainment of a population of coupled non-linear oscillators},
  booktitle = {International Symposium on Mathematical Problems in Theoretical Physics},
  series    = {Lecture Notes in Physics},
  volume    = {39},
  pages     = {420--422},
  publisher = {Springer},
  year      = {1975},
  doi       = {10.1007/BFb0013365}
}
```
