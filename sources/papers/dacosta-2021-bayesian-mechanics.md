---
type: paper
title: "Bayesian mechanics for stationary processes"
aliases:
  - "Da Costa et al. 2021"
  - "Da Costa (2021) Bayesian Mechanics"
  - "da-costa2021-bayesian-mechanics"
  - "dacosta2021bayesianmechanics"
authors:
  - Lancelot Da Costa
  - Karl Friston
  - Conor Heins
  - Grigorios A. Pavliotis
year: 2021
arxiv: "2106.13830"
url: https://royalsocietypublishing.org/doi/10.1098/rspa.2021.0518
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
updated: 2026-06-20
---

# Bayesian mechanics for stationary processes

> [!info] Citation
> Da Costa, L., Friston, K., Heins, C., & Pavliotis, G. A. (2021). "Bayesian mechanics for stationary processes." *Proceedings of the Royal Society A* **477**(2256): 20210518. DOI: [10.1098/rspa.2021.0518](https://doi.org/10.1098/rspa.2021.0518). Preprint: [arXiv:2106.13830](https://arxiv.org/abs/2106.13830).

## TL;DR

This is the technical core of geometric **Bayesian mechanics**: it shows precisely how, for a system at non-equilibrium steady state partitioned by a [[Markov blanket interpretation debate|Markov blanket]], the internal states come to *parametrize a probability density over external states*, so that internal dynamics can be read as approximate Bayesian inference. The construction proceeds from the stationary Fokker–Planck / Helmholtz decomposition of a diffusion process, derives the conditions under which a synchronization (or "bold") map links the most likely internal state to a posterior over external causes, and gives the gradient flows that realize free-energy minimization geometrically. It is the immediate predecessor of the (cited) Friston et al. 2023 statement and the formal engine behind [[Bayesian mechanics]].

## Problem & setting

Given a stochastic dynamical system whose state space splits into internal `μ`, external `η`, and blanket (sensory + active) states with conditional independence `μ ⫫ η | b`, when can we legitimately say the internal states *believe* something about the external states? The paper formalizes this for stationary diffusion processes, taking the steady-state density `p(x)` as primary and decomposing the drift into a gradient (dissipative) part and a divergence-free (solenoidal) part via the Helmholtz decomposition.

## Method

Working from the stationary density and its Helmholtz decomposition, the authors define the *synchronization map* `σ: μ ↦ η(μ)` sending each internal state to the expected external state under the conditional `p(η | b)`. The most likely internal state then indexes a variational density `q_μ(η)`, and minimizing [[Variational free energy]] with respect to `μ` performs approximate inference. The geometry is explicit: the flow on internal states is a gradient flow on free energy with respect to a metric inherited from the steady-state covariance, tying the dynamics to the [[Fisher information metric]] and [[Natural gradient]] descent.

## Key results

- **The interpretive bridge.** Internal states of a Markov-blanketed system at steady state encode (parametrize) a posterior over external states — the "physics of beliefs" claim, made rigorous for stationary processes.
- **Helmholtz / solenoidal structure.** Non-equilibrium steady states carry a divergence-free flow component; this is what gives Bayesian mechanics its Hamiltonian-like, oscillatory character rather than pure relaxation.
- **Geometric free-energy descent.** Inference is a Riemannian gradient flow, connecting the framework to information geometry.

## Relevance to this research

This paper is the precise precedent for the central move in **[[participatory-it-from-bit]]**: that an internal/observer state *parametrizes a density over the external world*, so that what looks like physics is the geometry of inference (the "it from bit" pullback). PIFB takes this internal-states-as-beliefs construction and lifts it into a gauge-covariant, multi-agent setting. Where Da Costa et al. fix a single Markov blanket and a single synchronization map, the project's [[Multi-agent variational free energy]] and [[Ouroboros multi-scale dynamics]] stack many such blankets across scales, with belief comparison handled by [[Parallel transport]] under a [[Gauge transformation]] rather than a single global frame. The Helmholtz/solenoidal decomposition here is the steady-state analogue of the project's [[Hamiltonian belief dynamics]] and [[Belief inertia]], and the Riemannian gradient flow is the same [[Fisher information metric]] / [[Natural gradient]] structure the model uses for belief updates. It is the technical heart underlying the more accessible [[Bayesian mechanics]] page and the foundation the [[Markov blanket interpretation debate]] (Bruineberg, Aguilera, Biehl) contests.

## Cross-links

- Concepts: [[Variational free energy]], [[Fisher information metric]], [[Natural gradient]], [[Hamiltonian belief dynamics]], [[Belief inertia]], [[Participatory realism (it from bit)]]
- New pages: [[Bayesian mechanics]], [[Markov blanket interpretation debate]]
- Methods/themes: [[Free-energy principle active inference]], [[Multi-agent variational free energy]]
- Related sources: [[friston-2019-particular-physics]], [[ramstead-2023-bayesian-mechanics]], [[parr-2020-markov-blankets-thermodynamics]], [[caticha-2019-entropic-dynamics-qm|caticha-2019-entropic-dynamics]]
- Manuscript: [[participatory-it-from-bit]]

```bibtex
@article{dacosta2021bayesian,
  title   = {Bayesian mechanics for stationary processes},
  author  = {Da Costa, Lancelot and Friston, Karl and Heins, Conor and Pavliotis, Grigorios A.},
  journal = {Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences},
  volume  = {477},
  number  = {2256},
  pages   = {20210518},
  year    = {2021},
  doi     = {10.1098/rspa.2021.0518},
  eprint  = {2106.13830},
  archivePrefix = {arXiv},
  publisher = {The Royal Society}
}
```
