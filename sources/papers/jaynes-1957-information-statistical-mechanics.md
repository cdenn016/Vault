---
type: paper
title: "Information Theory and Statistical Mechanics"
aliases:
  - "Jaynes 1957"
  - "Jaynes (1957) MaxEnt"
  - "jaynes-1957-information-theory"
authors:
  - Edwin T. Jaynes
year: 1957
arxiv: null
url: https://doi.org/10.1103/PhysRev.106.620
tags:
  - cluster/info-geometry
  - cluster/methodology
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/statistics
  - cluster/participatory/quantum-foundations
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# Information Theory and Statistical Mechanics

> [!info] Citation
> Edwin T. Jaynes (1957). "Information Theory and Statistical Mechanics." *Physical Review* 106(4): 620–630. DOI: [10.1103/PhysRev.106.620](https://doi.org/10.1103/PhysRev.106.620).

## TL;DR

Jaynes recasts statistical mechanics as a problem of *inference under incomplete information* rather than of physical ensembles. Given only the expectation values of certain quantities, the least-biased probability distribution consistent with that knowledge is the one of maximum Shannon entropy subject to those constraints — the **maximum-entropy (MaxEnt) principle**. The Gibbs/Boltzmann distributions of thermodynamics drop out as the MaxEnt distributions for energy constraints, with temperature appearing as the Lagrange multiplier. Probability assignments are epistemic: they encode an observer's state of knowledge, not an objective frequency.

## Problem & setting

Conventional statistical mechanics justifies the canonical ensemble by ergodic or equal-a-priori-probability assumptions about physical microstates. Jaynes argues these are unnecessary and partly unfounded; the canonical distribution should instead follow from a principle of honest inference — assign the distribution that is maximally noncommittal about what is not known while reproducing what is.

## Method

Maximize the Shannon entropy $H = -\sum_i p_i \log p_i$ subject to normalization and to constraints fixing the expectations $\langle f_k\rangle = \sum_i p_i f_k(x_i)$. Lagrange-multiplier variation yields the exponential-family (Gibbs) form $p_i \propto \exp(-\sum_k \lambda_k f_k(x_i))$, with the multipliers $\lambda_k$ fixed by the constraints. The multipliers are the conjugate thermodynamic variables (inverse temperature, etc.), so thermodynamics is reconstructed as the consequence of constrained entropy maximization.

## Key results

1. The MaxEnt principle: the least-biased distribution consistent with stated constraints is the maximum-entropy one; physics-free, it is a general rule of inference.
2. The canonical and grand-canonical ensembles are MaxEnt distributions for energy/particle-number constraints; temperature and chemical potential are Lagrange multipliers.
3. Establishes the epistemic (information-as-knowledge) reading of probability in physics, the seed of the later entropic-inference and entropic-dynamics programs.

## Relevance to this research

Jaynes is the methodological root of two pillars of this research program. First, the project's **entropy-regularized softmax consensus** — the attention-distribution entropy term $\tau\,\beta_{ij}\log(\beta_{ij}/\pi_{ij})$ that makes the softmax $\beta$ a stationary point of the free energy — is precisely a MaxEnt construction: maximizing entropy of the coupling weights subject to a cost (KL) constraint yields the exponential/softmax form, with the temperature $\tau$ as the Lagrange multiplier, exactly as inverse temperature arises here. Second, Jaynes' epistemic, observer-centric reading of probability is the headwater of the Caticha entropic-dynamics lineage ([[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]]) that [[participatory-it-from-bit]] builds on, and it underwrites PIFB's "collapse/consensus as updating" stance and its [[Participatory realism (it from bit)]] framing alongside [[wheeler-1990-it-from-bit]]. The note carries `cluster/methodology` as well as `cluster/info-geometry` because MaxEnt is the inference method the project's variational machinery generalizes.

## Cross-links

- Concept: [[Fisher information metric]] (metric-side complement to entropy-side MaxEnt), [[Variational free energy]].
- Theme: [[Physics from Fisher information]], [[Participatory realism (it from bit)]], [[Information geometry and natural gradient]].
- Sources: [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]], [[caticha-bartolomeo-reginatto-2015-entropic-dynamics]], [[reginatto-1998-fisher-quantum]], [[wheeler-1990-it-from-bit]].
- Manuscript: [[participatory-it-from-bit]].

## BibTeX

```bibtex
@article{jaynes1957information,
  author  = {Jaynes, Edwin T.},
  title   = {Information Theory and Statistical Mechanics},
  journal = {Physical Review},
  volume  = {106},
  number  = {4},
  pages   = {620--630},
  year    = {1957},
  publisher = {American Physical Society},
  doi     = {10.1103/PhysRev.106.620}
}
```
