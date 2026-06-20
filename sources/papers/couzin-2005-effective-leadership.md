---
type: paper
title: "Effective leadership and decision-making in animal groups on the move"
aliases: ["Couzin et al. 2005", "Informed-minority leadership"]
authors: ["Couzin I. D.", "Krause J.", "Franks N. R.", "Levin S. A."]
year: 2005
url: https://doi.org/10.1038/nature03236
tags: [cluster/social-physics, project/social-physics, field/biology, field/physics, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Effective leadership and decision-making in animal groups on the move

> [!info] Citation
> Couzin, I. D., Krause, J., Franks, N. R., & Levin, S. A. (2005). *Effective leadership and decision-making in animal groups on the move*. Nature, 433(7025), 513–516. DOI 10.1038/nature03236.

## TL;DR
Building on the zonal self-propelled-particle model, the authors ask how a moving group can be steered when only a few members possess information about a preferred direction (a food source, a migration route). They show that a vanishingly small fraction of informed individuals can guide an entire naive group accurately, and that the fraction of leaders needed shrinks as group size grows — all without any signaling, recognition of who is informed, or knowledge of group membership.

## What it establishes
Informed individuals balance two drives: the standard social interaction (repulsion/alignment/attraction with neighbors) and a preference for a goal direction $\mathbf{g}_i$, weighted by a parameter $\omega$:
$$ \mathbf{d}_i'(t+\tau) = \frac{\mathbf{d}_i(t+\tau) + \omega\,\mathbf{g}_i}{|\mathbf{d}_i(t+\tau) + \omega\,\mathbf{g}_i|}, $$
where $\mathbf{d}_i$ is the socially-determined desired direction. Naive individuals set $\omega=0$. Simulations show the group's accuracy (alignment with the preferred direction) rises sharply with the proportion $p$ of informed members and saturates, with the proportion required for a given accuracy decreasing as $1/\sqrt{N}$-like scaling with group size. The result quantifies how leadership and consensus can emerge from purely local interactions plus a small biased minority, with the group implicitly averaging conflicting preferences among multiple informed subgroups.

## Relevance to this research
This is a consensus-and-influence result: a minority of anchored, goal-biased agents — directly analogous to the stubborn/anchored agents of the Friedkin–Johnsen model — steers the collective decision through purely local coupling. That maps onto how the program's attention-weighted belief coupling propagates influence from a few committed agents through the network, and the $\omega$-weighted blend of social and goal directions is structurally the same trade-off as anchoring a belief to a private prior while coupling to neighbors. This is a strong bridge between the collective-motion and opinion-dynamics framings, relevant as a phenomenological and mechanistic analogue rather than as an equation in the VFE functional. See [[Collective active inference]], [[Opinion dynamics]], [[Bounded confidence]].

## Cross-links
- Concept: [[Collective active inference]]
- Related sources: [[couzin-2002-collective-memory]], [[reynolds-1987-boids]], [[vicsek-1995-self-driven-particles]]

## BibTeX
```bibtex
@article{couzin2005effective,
  author  = {Couzin, Iain D. and Krause, Jens and Franks, Nigel R. and Levin, Simon A.},
  title   = {Effective leadership and decision-making in animal groups on the move},
  journal = {Nature},
  volume  = {433},
  number  = {7025},
  pages   = {513--516},
  year    = {2005},
  doi     = {10.1038/nature03236}
}
```
