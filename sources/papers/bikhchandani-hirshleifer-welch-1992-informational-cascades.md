---
type: paper
title: "A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades"
aliases: ["Bikhchandani, Hirshleifer & Welch 1992", "BHW 1992 informational cascades"]
authors: ["Bikhchandani S.", "Hirshleifer D.", "Welch I."]
year: 1992
url: https://doi.org/10.1086/261849
tags: [cluster/social-physics, project/social-physics, field/economics, field/sociology, cluster/social-physics/networks-and-contagion]
created: 2026-06-19
updated: 2026-06-19
---

# A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades

> [!info] Citation
> Bikhchandani, S., Hirshleifer, D., & Welch, I. (1992). *A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades*. Journal of Political Economy, 100(5), 992-1026. DOI: [10.1086/261849](https://doi.org/10.1086/261849).

## TL;DR
This is the paper that named and formalized the **informational cascade**. Agents decide sequentially (adopt or reject) after seeing a private binary signal and the public history of predecessors' actions. Bikhchandani, Hirshleifer, and Welch prove that after only a short run of agreeing actions, the public information embedded in those actions dominates any single private signal, so every subsequent agent rationally ignores her own evidence and copies the herd. Once that threshold is crossed, actions stop conveying private information, learning halts abruptly, and the population locks onto a behavior — possibly the wrong one — that is *fragile*: a small shock or a single contrary public signal can flip the entire cascade. They use this mechanism to explain fads, fashion, custom, and rapid cultural change as conformity that is locally rational yet globally arbitrary.

## What it establishes
With symmetric binary signals of precision $p>1/2$, an UP cascade begins as soon as the number of observed adoptions exceeds rejections by two; the decision rule reduces to following the public count whenever

$$|\#\text{adopt} - \#\text{reject}| \ge 2,$$

at which point the agent's own signal cannot tip her posterior and she imitates regardless. The defining properties they derive are: (i) cascades start almost surely and quickly; (ii) they are *informationally inefficient* because aggregation stops while most agents are still uninformed by the herd; (iii) they can be *wrong* with positive probability; and (iv) they are *fragile*, since the public belief is supported by very little hard information and is overturned by the arrival of a more precise public signal or a public shock. Cascades thus produce mass uniformity that looks like strong consensus but rests on a thin informational base — the formal account of why fashions appear and vanish so abruptly.

## Relevance to this research
This is the discrete, Bayesian-sequential cousin of the program's continuous VFE belief coupling, and core canon for the herding/tipping neighborhood. An agent suppressing its own evidence in favor of transported neighbor beliefs is exactly the cascade pathology: in the functional, this is the regime where softmax attention weight $\beta_{ij}$ concentrates on neighbors and the self-coupling $\alpha\,\mathrm{KL}(q_i\|p_i)$ is too weak to retain the private signal, so $q_i \to \Omega_{ij}[q_j]$ and the agent's own likelihood term stops shaping the posterior. The program should be able to recover cascades as a limiting regime of softmax-weighted $\mathrm{KL}(q_i\|\Omega_{ij}[q_j])$ coupling, and the *fragility* BHW emphasize maps naturally onto the shallow, easily perturbed basins of the belief-coupling dynamics. The correspondence is structural rather than a proven identity: BHW's information aggregation is discrete and one-shot, the program's is continuous and iterative.

See [[Information cascades and herding]], [[Multi-agent variational free energy]], [[Echo chambers and polarization]], [[Belief inertia]].

## Cross-links
- Concept: [[Information cascades and herding]]
- Related sources: [[banerjee-1992-herd-behavior]], [[bikhchandani-hirshleifer-welch-1998-learning-from-others]], [[anderson-holt-1997-cascades-laboratory]]

## BibTeX
```bibtex
@article{bikhchandani1992cascades,
  author  = {Bikhchandani, Sushil and Hirshleifer, David and Welch, Ivo},
  title   = {A Theory of Fads, Fashion, Custom, and Cultural Change as Informational Cascades},
  journal = {Journal of Political Economy},
  year    = {1992},
  volume  = {100},
  number  = {5},
  pages   = {992--1026},
  doi     = {10.1086/261849}
}
```
