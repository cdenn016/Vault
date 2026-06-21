---
type: paper
title: "How particular is the physics of the free energy principle?"
aliases:
  - "Aguilera 2022"
  - "Aguilera et al. 2022"
  - "Aguilera (2022) How Particular"
authors:
  - Aguilera, Miguel
  - Millidge, Beren
  - Tschantz, Alexander
  - Buckley, Christopher L.
year: 2022
arxiv: "2105.11203"
url: https://doi.org/10.1016/j.plrev.2021.11.001
tags:
  - cluster/vfe
  - cluster/participatory/philosophy-of-mind
  - project/multi-agent
  - field/physics
  - field/neuroscience
  - field/philosophy
status: stable
created: 2026-06-19
updated: 2026-06-20
---

# How particular is the physics of the free energy principle?

> [!info] Citation
> Aguilera, M., Millidge, B., Tschantz, A., & Buckley, C. L. (2022). "How particular is the physics of the free energy principle?" *Physics of Life Reviews* **40**: 24–50. DOI: [10.1016/j.plrev.2021.11.001](https://doi.org/10.1016/j.plrev.2021.11.001). Preprint: [arXiv:2105.11203](https://arxiv.org/abs/2105.11203).

## TL;DR

A technical, worked-example critique that quantifies when the free-energy-principle's blanket construction actually holds. By analytically solving a family of linear (Ornstein–Uhlenbeck) non-equilibrium systems, the authors show that the conditions the FEP requires — a well-defined [[Markov blanket interpretation debate|Markov blanket]] with the right conditional-independence and synchronization structure — obtain only in a narrow region of parameter space. For generic non-equilibrium steady states with solenoidal (irreversible) flow, the blanket either fails to exist or the internal states do not cleanly parametrize a posterior over external states. The "particular physics" is, they argue, more particular than advertised.

## Problem & setting

The FEP-as-physics program ([[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]]) claims that any blanketed system at steady state looks like it performs inference. Aguilera et al. test this claim on exactly solvable linear systems, where every quantity — stationary covariance, drift decomposition, conditional densities — can be computed in closed form.

## Method

For multivariate Ornstein–Uhlenbeck processes the stationary density is Gaussian and the Helmholtz decomposition is explicit. The authors check, as a function of coupling strength and the solenoidal (antisymmetric) part of the drift, whether the blanket partition yields the conditional independence the FEP needs and whether the synchronization map from internal to external states is non-degenerate.

## Key results

The blanket condition is fragile: conditional independence across the blanket and a faithful internal-to-external belief map hold only when the irreversible or solenoidal coupling is small, and generic non-equilibrium dynamics break it. Outside that region, "internal states encode beliefs about external states" fails to hold even approximately. The paper thereby supplies a quantitative boundary on where Bayesian mechanics applies, complementing the conceptual critiques in the literature.

## Relevance to this research

Where [[bruineberg-2022-emperors-markov-blankets]] presses the conceptual instrumental-versus-ontological worry, Aguilera et al. supply the quantitative one: even granting the formalism, the blanket-and-belief structure that [[participatory-it-from-bit]] relies on exists only under restrictive coupling conditions. The PIFB manuscript therefore cannot assume the synchronization map for free; it must either operate in the regime where the blanket condition holds or motivate its belief fibers independently of a steady-state derivation. This is directly relevant to the project's [[Multi-agent variational free energy]] model, where many coupled agents generate exactly the dense, irreversible coupling Aguilera et al. flag as problematic. The note qualifies the constructive [[Bayesian mechanics]] lineage and anchors the [[Markov blanket interpretation debate]] cluster.

## Cross-links

- Concepts: [[Variational free energy]], [[Participatory realism (it from bit)]], [[Multi-agent variational free energy]], [[Hamiltonian belief dynamics]]
- Related sources: [[bruineberg-2022-emperors-markov-blankets]], [[biehl-2021-technical-critique]], [[friston-2019-particular-physics]], [[dacosta-2021-bayesian-mechanics]]
- Manuscript/Project: [[participatory-it-from-bit]], [[Markov blanket interpretation debate]], [[Bayesian mechanics]]

## BibTeX
```bibtex
@article{aguilera2022particular,
  author        = {Aguilera, Miguel and Millidge, Beren and Tschantz, Alexander and Buckley, Christopher L.},
  title         = {How particular is the physics of the free energy principle?},
  journal       = {Physics of Life Reviews},
  volume        = {40},
  pages         = {24--50},
  year          = {2022},
  doi           = {10.1016/j.plrev.2021.11.001},
  eprint        = {2105.11203},
  archivePrefix = {arXiv},
}
```
