---
type: reference
title: "Towards a Neuronal Gauge Theory"
aliases:
  - "Sengupta et al. 2016"
  - "Sengupta (2016) Neuronal Gauge Theory"
authors:
  - Biswa Sengupta
  - Arturo Tozzi
  - Gerald K. Cooray
  - Pamela K. Douglas
  - Karl J. Friston
year: 2016
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# Towards a Neuronal Gauge Theory

> [!info] Citation
> Sengupta, B., Tozzi, A., Cooray, G. K., Douglas, P. K., & Friston, K. J. (2016). "Towards a Neuronal Gauge Theory." *PLoS Biology* **14**(3): e1002400. DOI: [10.1371/journal.pbio.1002400](https://doi.org/10.1371/journal.pbio.1002400).

## TL;DR

This paper proposes that neuronal dynamics — and self-organizing biological systems generally — can be cast in the language of a **gauge theory**, where the free-energy-minimizing brain has a redundancy (a local symmetry) in how it parametrizes its beliefs, and the dynamics that matter are the gauge-invariant ones. It is the project's named **closest precursor on the gauge–FEP axis**: the explicit proposal that active inference and gauge theory should be unified. (The follow-up Sengupta & Friston 2017, "Approximate Bayesian inference as a gauge theory," [arXiv:1705.06614](https://arxiv.org/abs/1705.06614), develops the mathematics further.)

## What it establishes

- **A local symmetry on belief representations.** The same physical (inferential) state can be encoded by many internal parametrizations; the brain's dynamics should be invariant under this redundancy — exactly the logic of a gauge symmetry, with physical content living in gauge-invariant quantities.
- **Free-energy minimization as gauge-covariant dynamics.** Casting belief updating in gauge-theoretic terms suggests that connection/curvature-like objects govern how beliefs are transported and compared, and that phenomena resisting formal description (attention, the action–perception link) might be illuminated by this apparatus.
- **A research program, not a finished theory.** The title's "Towards" is deliberate: it sketches the correspondence and argues for its promise rather than delivering a complete gauge field theory of the brain.

## Why the project cites it

This is the **explicitly named precursor** for the gauge-theoretic side of [[participatory-it-from-bit]]: the prior proposal that free-energy minimization should be formulated as a gauge theory. The present project takes that proposal and makes it concrete and computational — beliefs are sections of a fiber bundle ([[Agents as fibre-bundle sections]]), the redundancy in belief parametrization is a literal [[Gauge transformation]], cross-agent belief comparison is [[Parallel transport]] with explicit transport operators `Omega_ij = exp(φ_i) exp(-φ_j)`, and the "gauge-invariant quantities that matter" become measurable [[Holonomy]] around loops. Where Sengupta et al. argue *that* the brain admits a gauge description, the project supplies *which* group, *which* connection, and a working [[Multi-agent variational free energy]] minimizer that respects gauge equivariance. The participatory reading — that physical content is what survives the gauge freedom of any observer's belief frame — is the project's extension of this paper's invariance principle, tying it to [[Participatory realism (it from bit)]] and the broader [[Free-energy principle active inference]] program. See also the [[Bayesian mechanics]] lineage for the non-gauge development of FEP-as-physics.

```bibtex
@article{sengupta2016neuronal,
  title   = {Towards a Neuronal Gauge Theory},
  author  = {Sengupta, Biswa and Tozzi, Arturo and Cooray, Gerald K. and Douglas, Pamela K. and Friston, Karl J.},
  journal = {PLoS Biology},
  volume  = {14},
  number  = {3},
  pages   = {e1002400},
  year    = {2016},
  doi     = {10.1371/journal.pbio.1002400},
  publisher = {Public Library of Science}
}
```
