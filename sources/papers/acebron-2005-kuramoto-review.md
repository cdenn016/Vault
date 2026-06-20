---
type: paper
title: "The Kuramoto model: A simple paradigm for synchronization phenomena"
aliases: ["Acebron et al. 2005", "Kuramoto model review"]
authors: ["Acebron J. A.", "Bonilla L. L.", "Perez Vicente C. J.", "Ritort F.", "Spigler R."]
year: 2005
url: https://doi.org/10.1103/RevModPhys.77.137
tags: [cluster/social-physics, project/social-physics, field/physics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# The Kuramoto model: A simple paradigm for synchronization phenomena

> [!info] Citation
> Acebrón, J. A., Bonilla, L. L., Pérez Vicente, C. J., Ritort, F., & Spigler, R. (2005). *The Kuramoto model: A simple paradigm for synchronization phenomena*. Reviews of Modern Physics, 77(1), 137–185. DOI 10.1103/RevModPhys.77.137.

## TL;DR
This is the comprehensive reference review of the Kuramoto model and its descendants. It gives the rigorous mean-field treatment of the synchronization transition, then systematically extends the analysis to noise (the nonlinear Fokker–Planck / population-density formulation), finite-size fluctuations, frequency-distribution effects, time delays, external forcing, and coupling on complex networks rather than all-to-all topology. It is the standard one-stop survey for synchronization phenomenology and its analytical machinery.

## What it establishes
Starting from $\dot\theta_i = \omega_i + \frac{K}{N}\sum_j \sin(\theta_j-\theta_i)$, the review develops the order-parameter self-consistency for the noiseless case and then the kinetic description for the noisy case. Adding white noise $\xi_i$ of strength $D$ promotes the dynamics to a stochastic system whose single-oscillator density $\rho(\theta,\omega,t)$ obeys a nonlinear Fokker–Planck equation,
$$ \partial_t \rho = D\,\partial_\theta^2 \rho - \partial_\theta\!\big[(\omega + Kr\sin(\psi-\theta))\,\rho\big], $$
self-consistently coupled through $r e^{i\psi} = \int e^{i\theta}\rho\, d\theta\, g(\omega)\, d\omega$. The review establishes the stability of the incoherent state, the bifurcation to partial synchrony, finite-$N$ scaling of fluctuations, and how network structure (degree heterogeneity, small-world, scale-free topologies) reshapes $K_c$ and the order parameter. It is the authoritative collation of these results with proofs and citations.

## Relevance to this research
This is the definitive survey a complete knowledge base needs for synchronization, and its noisy, network-coupled variants mirror the program's own setting: noisy belief updates coupled over a graph rather than all-to-all. The nonlinear Fokker–Planck / population-density formulation is precisely the kind of mean-field, finite-$N$ machinery one would port to analyze collective belief phase-locking and the consensus-versus-fragmentation transition. The relevance is methodological — it supplies the analytical toolkit for population synchrony — rather than machinery the belief-inertia VFE functional directly contains. See [[Hamiltonian belief dynamics]], [[Synchronization and the Kuramoto model]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Synchronization and the Kuramoto model]]
- Related sources: [[kuramoto-1975-coupled-oscillators]], [[strogatz-2000-kuramoto-to-crawford]], [[pikovsky-rosenblum-kurths-2001-synchronization]]

## BibTeX
```bibtex
@article{acebron2005kuramoto,
  author  = {Acebr\'on, Juan A. and Bonilla, Luis L. and P\'erez Vicente, Conrad J. and Ritort, Felix and Spigler, Renato},
  title   = {The Kuramoto model: A simple paradigm for synchronization phenomena},
  journal = {Reviews of Modern Physics},
  volume  = {77},
  number  = {1},
  pages   = {137--185},
  year    = {2005},
  doi     = {10.1103/RevModPhys.77.137}
}
```
