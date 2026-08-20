---
type: paper
title: "On Markov blankets and hierarchical self-organisation"
aliases:
  - "Palacios et al. 2020 hierarchical Markov blankets"
authors:
  - Palacios, Ensor Rafael
  - Razi, Adeel
  - Parr, Thomas
  - Kirchhoff, Michael
  - Friston, Karl
year: 2020
arxiv: null
url: https://doi.org/10.1016/j.jtbi.2019.110089
tags:
  - cluster/multi-agent
  - cluster/vfe
  - project/multi-agent
  - field/biology
  - field/neuroscience
  - field/philosophy
created: 2026-08-20
---

# On Markov blankets and hierarchical self-organisation

> [!info] Citation
> Ensor Rafael Palacios, Adeel Razi, Thomas Parr, Michael Kirchhoff, and Karl Friston (2020). "On Markov blankets and hierarchical self-organisation." *Journal of Theoretical Biology* **486**, 110089. https://doi.org/10.1016/j.jtbi.2019.110089

## TL;DR

Microscopic systems endowed with prior beliefs that they occupy roles in a macroscopic Markov blanket can self-organize into blankets of blankets. The simulations are a proof of concept under a carefully chosen generative model, and the authors explicitly reject the inference that every coupled random dynamical system develops such a hierarchy.

## Problem & setting

The paper asks how boundaries separating internal and external states can arise recursively across biological scales. Synthetic cells already carrying microscopic blankets interact through short-range influences and infer their roles in a higher-level internal, active, sensory, or external partition.

## Method

Each element minimizes variational free energy under priors encoding conditional-dependence roles but not a fixed target morphology. Simulations first assemble one macroscopic blanket and then an ensemble of ensembles, illustrating recursive blankets of blankets.

## Key results

The specified systems form cell- and organ-like boundaries and exhibit a candidate higher-level blanket. The result depends on suitable priors, generative models, and interaction structure. It is numerical proof of principle, not a theorem that coupling alone induces hierarchical agency or a general Bayesian-mechanics synchronization map.

## Relevance to this research

This is the closest existing construction to the proposed multi-agent extension of [[Bayesian mechanics]]. It supplies a positive control for [[Meta-agents and hierarchical emergence]] and a warning: a group-level blanket must be demonstrated, not inferred from low divergence or coordinated motion. The project's partition selector and quotient map remain additional obligations.

## Cross-links

- Concepts: [[Bayesian mechanics]], [[Collective active inference]], [[Meta-agents and hierarchical emergence]], [[Ouroboros multi-scale dynamics]]
- Related sources: [[waade-2025-as-one-and-many]], [[maisto-2025-flock-joint-agency]]
- Project: [[Gauge-Theoretic Multi-Agent VFE Model]]

## BibTeX

```bibtex
@article{PalaciosEtAl2020HierarchicalBlankets,
  author  = {Palacios, Ensor Rafael and Razi, Adeel and Parr, Thomas and Kirchhoff, Michael and Friston, Karl},
  title   = {On Markov blankets and hierarchical self-organisation},
  journal = {Journal of Theoretical Biology},
  volume  = {486},
  pages   = {110089},
  year    = {2020},
  doi     = {10.1016/j.jtbi.2019.110089}
}
```
