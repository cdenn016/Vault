---
type: reference
title: "Active Inference: The Free Energy Principle in Mind, Brain, and Behavior"
aliases:
  - "Parr 2022"
  - "Parr, Pezzulo & Friston 2022"
authors:
  - Thomas Parr
  - Giovanni Pezzulo
  - Karl J. Friston
year: 2022
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/cs-ml
  - field/statistics
created: 2026-06-18
updated: 2026-06-18
---

# Active Inference: The Free Energy Principle in Mind, Brain, and Behavior

> [!info] Citation
> Parr, T., Pezzulo, G., & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. Cambridge, MA: MIT Press. Open access. ISBN 978-0-262-04535-3.

## TL;DR

The first book-length, self-contained treatment of active inference: the framework in which perception, learning, planning, and action are all cast as minimization of [[Variational free energy]] under a generative model. It develops both the high-level normative story (organisms persist by minimizing free energy / maximizing model evidence) and the concrete computational machinery (variational message passing, expected free energy, and the discrete- and continuous-state process models that implement it).

## What it establishes

- **Free energy as a single objective for mind and behavior.** Perception, action, and learning are unified as gradient descent on [[Variational free energy]], an upper bound on surprisal that stands in for (negative) Bayesian model evidence — the bound made familiar in machine learning as the [[Evidence lower bound (ELBO)]].
- **The generative-model stance.** Agents carry an internal generative model of how hidden causes produce sensations; inference inverts this model to form approximate posterior beliefs. This is the [[Free-energy principle active inference]] program stated in full.
- **Expected free energy and planning.** Action selection minimizes *expected* free energy over policies, decomposing into epistemic (information-seeking) and pragmatic (goal-seeking) terms — the active-inference account of exploration vs. exploitation.
- **Precision and confidence.** Inference is modulated by [[Precision weighting]] of [[Prediction error]], connecting the discrete and continuous formulations to [[Predictive coding network]] implementations.
- **Two complementary process theories.** A discrete-state (Markov decision process) formulation and a continuous-state (predictive-coding / generalized-coordinates) formulation, with the message-passing schemes that realize each.

## Why the project cites it

This book is the canonical reference for the variational-free-energy substrate that the project generalizes. Several threads connect directly:

- **From single-agent to many.** The book formalizes free-energy minimization for one agent under one generative model; the [[Gauge-Theoretic Multi-Agent VFE Model]] extends this to [[Multi-agent variational free energy]], where each agent's belief state becomes a local section and inter-agent comparison requires a connection. Casting [[Agents as fibre-bundle sections]] and introducing a [[Gauge transformation]] between agents' belief frames is precisely the structure that single-agent active inference leaves implicit.
- **Geometry of belief updating.** The free-energy gradient flows the book describes are made geometric in the project via the [[Fisher information metric]] and [[Natural gradient]], with belief mass and resistance to update treated as [[Belief inertia]] and [[Mass as Fisher information]] — extensions that take the book's gradient-descent picture into [[Hamiltonian belief dynamics]].
- **Precision and prediction error** as developed here ground the project's treatment of [[Precision weighting]] and the [[Predictive coding network]] reading of attention layers in the [[VFE Transformer Program]].
- **Hierarchy and emergence.** The book's hierarchical (deep) generative models motivate the project's [[Meta-agents and hierarchical emergence]] and [[Ouroboros multi-scale dynamics]], where free-energy minimization at one scale composes into agents at the next.
- **Epistemics.** The book's commitment to inference-as-world-construction connects to the project's reading of [[Participatory realism (it from bit)]], where the observer's model is constitutive rather than merely descriptive.

> [!note] Editorial: The book itself does not develop the gauge-theoretic, fibre-bundle, or information-geometric extensions above; those are the project's contributions. The note links them here only to record *why* this reference is cited, not to attribute them to Parr, Pezzulo & Friston.

## Related references

The continuous-time, process-theoretic precursor is [[friston-2017-active-inference-process]]; the ecological / multi-agent extension the project also draws on is [[ramstead-2019-variational-neuroethology]]; the entropic-dynamics view of the same updating is [[caticha-2019-entropic-dynamics]].

## BibTeX

```bibtex
@book{parr2022active,
  title     = {Active Inference: The Free Energy Principle in Mind, Brain, and Behavior},
  author    = {Parr, Thomas and Pezzulo, Giovanni and Friston, Karl J.},
  year      = {2022},
  publisher = {MIT Press},
  address   = {Cambridge, MA},
  isbn      = {978-0-262-04535-3},
  note      = {Open access}
}
```
