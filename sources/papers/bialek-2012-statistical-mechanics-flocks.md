---
type: paper
title: "Statistical mechanics for natural flocks of birds"
aliases: ["Bialek et al. 2012", "Maximum-entropy flocks"]
authors: ["Bialek W.", "Cavagna A.", "Giardina I.", "Mora T.", "Silvestri E.", "Viale M.", "Walczak A. M."]
year: 2012
url: https://doi.org/10.1073/pnas.1118633109
tags: [cluster/social-physics, project/social-physics, field/physics, field/biology, field/statistics, cluster/social-physics/social-influence]
created: 2026-06-19
updated: 2026-06-19
---

# Statistical mechanics for natural flocks of birds

> [!info] Citation
> Bialek, W., Cavagna, A., Giardina, I., Mora, T., Silvestri, E., Viale, M., & Walczak, A. M. (2012). *Statistical mechanics for natural flocks of birds*. Proceedings of the National Academy of Sciences, 109(13), 4786–4791. DOI 10.1073/pnas.1118633109.

## TL;DR
Using high-resolution 3D reconstructions of starling flocks, the authors build the maximum-entropy (least-structured) probability model consistent with the measured pairwise correlations of flight directions. Remarkably, a model constrained only by local correlations — with effectively no free parameters once the data fix the constraints — reproduces flock-wide order, including the long-range propagation of directional information. This shows that the macroscopic order of a flock can be inferred directly from minimal statistical assumptions plus local interaction data.

## What it establishes
For normalized flight-direction vectors $\mathbf{s}_i$ (unit "spins"), the maximum-entropy distribution consistent with the measured average local alignment is
$$ P(\{\mathbf{s}_i\}) = \frac{1}{Z}\exp\!\Big(\frac{1}{2}\sum_{i}J\sum_{j\in n_i}\mathbf{s}_i\cdot\mathbf{s}_j\Big), $$
a Heisenberg-like model in which each bird couples to a fixed number $n_c$ of nearest neighbors. Fitting the single coupling $J$ and the interaction range $n_c$ to the data, the model predicts the full correlation function and the four-point statistics with no further tuning. The inferred $n_c \approx 11$–21 is consistent with the topological-interaction picture, and the model reproduces the scale-free correlations observed in real flocks. The work is a clean demonstration that maximum entropy plus local constraints captures emergent collective order.

## Relevance to this research
This connects collective motion to the maximum-entropy / configuration-counting view of a population — the same "statistical mechanics of a flock" logic that underlies the program's meta-entropy $S_{\text{meta}} = \log W$ and its thermodynamic-limit bridge to the continuum. The methodological link is strong: maximum entropy subject to measured constraints is exactly the inferential principle behind treating a belief population as a statistical ensemble, and the local-coupling Heisenberg model is the spin-model template for gauge-coupled beliefs. The relevance is at the level of shared inferential machinery (max-ent, configuration counting) rather than the specific spin couplings. See [[Meta-entropy]], [[Collective motion and flocking]], [[Multi-agent variational free energy]].

## Cross-links
- Concept: [[Meta-entropy]]
- Related sources: [[ballerini-2008-topological-interaction]], [[toner-tu-1995-flocking-hydrodynamics]], [[vicsek-zafeiris-2012-collective-motion]]

## BibTeX
```bibtex
@article{bialek2012statistical,
  author  = {Bialek, William and Cavagna, Andrea and Giardina, Irene and Mora, Thierry and Silvestri, Edmondo and Viale, Massimiliano and Walczak, Aleksandra M.},
  title   = {Statistical mechanics for natural flocks of birds},
  journal = {Proceedings of the National Academy of Sciences},
  volume  = {109},
  number  = {13},
  pages   = {4786--4791},
  year    = {2012},
  doi     = {10.1073/pnas.1118633109}
}
```
