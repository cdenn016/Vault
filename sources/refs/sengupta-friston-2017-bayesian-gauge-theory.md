---
type: reference
title: "Approximate Bayesian inference as a gauge theory"
aliases:
  - "Sengupta & Friston 2017"
  - "Sengupta-Friston (2017) Bayesian Gauge Theory"
authors:
  - Biswa Sengupta
  - Karl Friston
year: 2017
arxiv: "1705.06614"
tags:
  - cluster/vfe
  - cluster/gauge-theory
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/physics
  - field/neuroscience
  - field/statistics
  - cluster/participatory/consciousness
created: 2026-06-19
updated: 2026-06-19
---

# Approximate Bayesian inference as a gauge theory

> [!info] Citation
> Sengupta, B., & Friston, K. (2017). "Approximate Bayesian inference as a gauge theory." Preprint, [arXiv:1705.06614](https://arxiv.org/abs/1705.06614).

> [!note] Editorial (resolved 2026-06-19): This 2017 preprint (arXiv:1705.06614) is the technical follow-up to [[sengupta-2016-neuronal-gauge-theory]] ("Towards a Neuronal Gauge Theory," *PLoS Biology*) and is the project's most direct gauge–FEP precursor. The "belief-state synchronization" paper the domain brief tentatively listed *does* exist and is a **distinct** work: Sengupta & Friston, "How Belief States Get Synchronized through Active Inference" (arXiv:1810.08750), which the manuscript bibliography carries under key `SenguptaFriston2018`. Manuscript-side check (GL(K) peer review, 2026-06-19): the `GL(K)_attention.tex` body cites **no** Sengupta work; `references.bib` holds `Sengupta2016NeuronalGauge` and the 2018 synchronization entry but **not** this 1705.06614 gauge-theory preprint. The companion `Participatory_it_from_bit.tex` cites the 2016 and 2018 entries. Fix applied: 1705.06614 added to the manuscript bib under key `sengupta2017gauge` and cited in the GL(K) Introduction.

## TL;DR

This preprint develops the mathematics behind the neuronal-gauge-theory proposal: it casts **approximate (variational) Bayesian inference itself as a gauge theory**, in which the redundancy of belief parametrizations is a local gauge symmetry and free-energy minimization is the gauge-covariant dynamics. It supplies the connection/transport apparatus only sketched in the 2016 companion, making it the most directly relevant prior work on the project's gauge–free-energy axis.

## What it establishes

- **Inference has a gauge symmetry.** Distinct internal parametrizations of the same posterior are gauge-equivalent; physically meaningful quantities are gauge-invariant, and the dynamics of inference respect this redundancy.
- **Free-energy minimization as covariant flow.** Variational free-energy descent is formulated covariantly with respect to the gauge group acting on belief representations.
- **Toward connection and curvature.** The framework points to connection-like objects governing how beliefs are transported and compared, the natural setting for holonomy / curvature diagnostics.

## Why the project cites it

This is the **most technically explicit precursor** to the project's central thesis that variational inference *is* a gauge theory. [[participatory-it-from-bit]] makes the apparatus concrete: the gauge redundancy becomes a literal [[Gauge transformation]] on belief frames, belief comparison across agents becomes [[Parallel transport]] with operators `Omega_ij = exp(φ_i) exp(-φ_j)`, the connection's curvature becomes measurable [[Holonomy]], and free-energy descent runs as a gauge-equivariant minimizer over [[Agents as fibre-bundle sections]]. The gauge-invariance principle — physical content is what survives the freedom in any observer's belief frame — is the formal core of the project's [[Participatory realism (it from bit)]] reading. Together with [[sengupta-2016-neuronal-gauge-theory]], this fixes the gauge–FEP lineage the project extends to a working [[Multi-agent variational free energy]] model.

```bibtex
@article{sengupta2017gauge,
  title   = {Approximate Bayesian inference as a gauge theory},
  author  = {Sengupta, Biswa and Friston, Karl},
  journal = {arXiv preprint arXiv:1705.06614},
  year    = {2017},
  eprint  = {1705.06614},
  archivePrefix = {arXiv},
  primaryClass  = {q-bio.NC}
}
```
