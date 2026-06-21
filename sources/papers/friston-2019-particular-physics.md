---
type: paper
title: "A free energy principle for a particular physics"
aliases:
  - "Friston 2019"
  - "Friston (2019) Particular Physics"
  - "friston2019free"
  - "friston-2019-free-energy-particular-physics"
  - "friston-2019-free-energy-principle"
  - "friston2019-free-energy-principle"
  - "friston2019freeenergyprinciple"
  - "friston-2019-free-energy"
  - "friston-2019-free-energy-consciousness"
  - "friston2019freeenergyconsciousness"
authors:
  - Karl Friston
year: 2019
arxiv: "1906.10184"
url: https://arxiv.org/abs/1906.10184
tags:
  - cluster/vfe
  - cluster/participatory
  - project/multi-agent
  - project/transformer
  - field/neuroscience
  - field/physics
  - field/statistics
  - cluster/participatory/consciousness
status: stable
created: 2026-06-19
updated: 2026-06-19
---

# A free energy principle for a particular physics

> [!info] Citation
> Karl Friston (2019). "A free energy principle for a particular physics." Monograph, [arXiv:1906.10184](https://arxiv.org/abs/1906.10184).

## TL;DR

This is the canonical, book-length statement that recasts the free-energy principle as a *physics* — a "physics of particles," where a "particle" is anything possessing a [[Markov blanket interpretation debate|Markov blanket]]. Friston starts from the stationary density of a random dynamical system, applies the Helmholtz decomposition of its flow, and argues that any system with a blanket at non-equilibrium steady state will appear to track (infer) the states beyond its blanket. This is the parent text of the entire **[[Bayesian mechanics]]** lineage: the later Da Costa et al. 2021 and Ramstead et al. 2023 papers are the rigorous and the expository developments, respectively, of the program laid out here.

## Problem & setting

The aim is to derive lawful behaviour — perception, action, self-organization — not from a normative postulate but from the existence of a statistical boundary. Take a system whose states obey a stochastic differential equation with a (Pearl) Markov-blanket partition into internal, active, sensory, and external states. The question is what such a system *must* look like at steady state.

## Method

The construction rests on three ingredients: (i) a non-equilibrium steady-state density `p(x)` for the whole system, (ii) the Helmholtz decomposition of the drift into dissipative (gradient) and conservative (solenoidal) parts, and (iii) the conditional-independence structure of the blanket, which lets internal states be read as encoding sufficient statistics of a posterior over external states. The flow of the most likely internal state then performs a gradient descent on [[Variational free energy]], i.e. approximate Bayesian inference. The treatment is explicitly variational and uses generalized coordinates of motion, inheriting the DEM machinery.

## Key results

- **Particles = things with Markov blankets.** A general taxonomy of "particles" (inert, active, autonomous) follows from the structure of the blanket and the solenoidal flow.
- **FEP as physics, not biology.** Self-evidencing is presented as a generic property of blanketed steady-state systems, removing any appeal to teleology.
- **Bayesian mechanics in embryo.** The internal-states-parametrize-beliefs claim, the synchronization map, and the geometric gradient flow all appear here in their first systematic form.

## Relevance to this research

This is the conceptual progenitor of the observer-as-inference stance that **[[participatory-it-from-bit]]** builds on. PIFB's "it from bit" reading — that the apparent physics of a system is the geometry of an embedded observer's beliefs about the rest — is precisely the FEP-as-physics thesis, lifted into a gauge-covariant, multi-agent register. The project inherits the Markov-blanket notion of a statistical individual (seeding [[Multi-agent variational free energy]] and nested [[Meta-agents and hierarchical emergence]]) and the solenoidal/Helmholtz flow that underwrites its [[Hamiltonian belief dynamics]] and [[Belief inertia]]. It also inherits the live foundational tension this text provoked: the [[Markov blanket interpretation debate]] (Bruineberg et al., Aguilera et al., Biehl et al.) is, in large part, a critique of the assumptions made here, which PIFB must answer rather than assume. See the broader [[Free-energy principle active inference]] method page and [[Bayesian mechanics]].

## Cross-links

- Concepts: [[Variational free energy]], [[Hamiltonian belief dynamics]], [[Belief inertia]], [[Participatory realism (it from bit)]], [[Fisher information metric]]
- New pages: [[Bayesian mechanics]], [[Markov blanket interpretation debate]]
- Methods/themes: [[Free-energy principle active inference]], [[Multi-agent variational free energy]]
- Related sources: [[dacosta-2021-bayesian-mechanics]], [[ramstead-2023-bayesian-mechanics]], [[parr-2020-markov-blankets-thermodynamics]], [[friston-2010-free-energy-principle]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{friston2019particular,
  title   = {A free energy principle for a particular physics},
  author  = {Friston, Karl},
  journal = {arXiv preprint arXiv:1906.10184},
  year    = {2019},
  eprint  = {1906.10184},
  archivePrefix = {arXiv},
  primaryClass  = {q-bio.NC}
}
```
