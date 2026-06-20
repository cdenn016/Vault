---
type: paper
title: "Oscillators that sync and swarm"
aliases: ["O'Keeffe, Hong & Strogatz 2017", "Swarmalators"]
authors: ["O'Keeffe K. P.", "Hong H.", "Strogatz S. H."]
year: 2017
url: https://doi.org/10.1038/s41467-017-01190-3
tags: [cluster/social-physics, project/social-physics, field/physics, field/mathematics, cluster/social-physics/opinion-dynamics]
created: 2026-06-19
updated: 2026-06-19
---

# Oscillators that sync and swarm

> [!info] Citation
> O'Keeffe, K. P., Hong, H., & Strogatz, S. H. (2017). *Oscillators that sync and swarm*. Nature Communications, 8, 1504. DOI 10.1038/s41467-017-01190-3.

## TL;DR
The paper introduces "swarmalators," agents that simultaneously synchronize (like Kuramoto oscillators) and swarm (like self-propelled particles), with a two-way coupling between an agent's internal phase and its spatial position. Because phase influences motion and motion influences phase, the model produces collective states that neither pure synchronization nor pure swarming can reach — static phase waves, splintered phase clusters, and an "active phase wave" in which agents cycle in both space and phase.

## What it establishes
Each swarmalator $i$ carries a position $\mathbf{x}_i$ and a phase $\theta_i$ that co-evolve,
$$ \dot{\mathbf{x}}_i = \frac{1}{N}\sum_{j\neq i}\Big[\frac{\mathbf{x}_j-\mathbf{x}_i}{|\mathbf{x}_j-\mathbf{x}_i|}\big(1+J\cos(\theta_j-\theta_i)\big) - \frac{\mathbf{x}_j-\mathbf{x}_i}{|\mathbf{x}_j-\mathbf{x}_i|^2}\Big], \qquad \dot\theta_i = \frac{K}{N}\sum_{j\neq i}\frac{\sin(\theta_j-\theta_i)}{|\mathbf{x}_j-\mathbf{x}_i|}. $$
The parameter $J$ controls how strongly phase modulates spatial attraction, and $K$ controls phase coupling (which is itself distance-weighted). Varying $(J,K)$ the authors map five collective states, including the spatially ordered "static sync," "static async," "static phase wave," and the dynamic "splintered" and "active" phase waves, demonstrating genuinely new behavior from the bidirectional sync–swarm coupling.

## Relevance to this research
This is the cleanest existing model unifying synchronization with spatial collective motion, and it is unusually on-point: it is the closest analogue to the program's joint dynamics over a belief value and a belief phase / gauge frame, where phase-locking and position-style coupling interact. The program couples a belief $(\mu,\Sigma)$ with a gauge frame $\phi$ through $\Omega_{ij}=\exp(\phi_i)\exp(-\phi_j)$, and swarmalators are the toy physics version of "internal phase coupled to spatial coupling." The relevance is a strong structural analogy for the underdamped sync-plus-coupling picture rather than shared equations. See [[Hamiltonian belief dynamics]], [[Collective motion and flocking]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Collective motion and flocking]]
- Related sources: [[kuramoto-1975-coupled-oscillators]], [[vicsek-1995-self-driven-particles]], [[strogatz-2000-kuramoto-to-crawford]]

## BibTeX
```bibtex
@article{okeeffe2017swarmalators,
  author  = {O'Keeffe, Kevin P. and Hong, Hyunsuk and Strogatz, Steven H.},
  title   = {Oscillators that sync and swarm},
  journal = {Nature Communications},
  volume  = {8},
  pages   = {1504},
  year    = {2017},
  doi     = {10.1038/s41467-017-01190-3}
}
```
