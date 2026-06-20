---
type: reference
title: "Active Inference: A Process Theory"
aliases:
  - "Friston 2017"
  - "Friston et al. 2017"
authors:
  - Karl J. Friston
  - Thomas FitzGerald
  - Francesco Rigoli
  - Philipp Schwartenbeck
  - Giovanni Pezzulo
year: 2017
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/neuroscience
  - field/statistics
created: 2026-06-18
updated: 2026-06-18
---

# Active Inference: A Process Theory

> [!info] Citation
> Friston, K. J., FitzGerald, T., Rigoli, F., Schwartenbeck, P., & Pezzulo, G. (2017). "Active Inference: A Process Theory." *Neural Computation*, **29**(1), 1–49. DOI: [10.1162/NECO_a_00912](https://doi.org/10.1162/NECO_a_00912).

## TL;DR

This paper recasts active inference from an abstract normative principle into a concrete *process theory*: a set of belief-update equations on discrete Markov decision process (MDP) generative models, together with a proposed neuronal implementation. Perception, action, and learning all emerge from a single imperative — minimization of [[Variational free energy]] — with action selection driven by the *expected* free energy of competing policies, and dopaminergic signalling identified with the [[Precision weighting]] of those policy beliefs.

## What it establishes

The central move is to take the free-energy principle ([[Free-energy principle active inference]]) and supply the *mechanics* by which an agent realizes it. Working with a categorical (discrete-state) generative model, the authors derive gradient-descent belief updates that minimize variational free energy, so that approximate posterior beliefs over hidden states track the true posterior — a marginal/mean-field message-passing scheme closely related to [[Predictive coding network]] dynamics and [[Prediction error]] minimization.

Key contributions grounded in the work:

- **Variational free energy as the perceptual objective.** Inference over hidden states is gradient descent on $F$, the variational bound on (negative log) model evidence — the same quantity that, in continuous settings, defines the [[Evidence lower bound (ELBO)]].
- **Expected free energy as the planning objective.** Policies are scored by *expected* free energy $G(\pi)$, which decomposes into epistemic (information-gain / exploration) and pragmatic (goal-seeking / exploitation) terms. This gives a principled, single-currency account of the explore–exploit trade-off without ad hoc reward functions.
- **Precision as a hyper-parameter under inference.** The confidence (inverse temperature) on policy beliefs is itself estimated, and its update is mapped onto dopaminergic neuromodulation — a concrete instance of [[Precision weighting]] over beliefs.
- **A neuronal process theory.** The paper assigns the variables of the update equations to neuronal populations and synaptic dynamics, proposing how firing rates and plasticity could implement the variational updates.

## Why the project cites it

This reference is foundational scaffolding for the VFE side of the project. The variational-free-energy functional it formalizes is the scalar quantity the project lifts into a geometric and multi-agent setting:

- **Multi-agent extension.** Where this paper treats a single agent minimizing $F$, the project's [[Gauge-Theoretic Multi-Agent VFE Model]] generalizes the objective to interacting agents, yielding [[Multi-agent variational free energy]]. Friston et al. supply the canonical single-agent baseline that this generalization must reduce to.
- **Gauge / fibre-bundle structure.** Treating each agent's beliefs as living in a local frame motivates the project's picture of [[Agents as fibre-bundle sections]], with belief comparison across agents handled by [[Parallel transport]] under a [[Gauge transformation]]. The process-theory update equations are the per-fibre dynamics on top of which this connection structure is built.
- **Information geometry.** Because the belief updates are gradient descent on free energy, they connect naturally to the [[Fisher information metric]] and [[Natural gradient]] view of inference, and to the project's reading of [[Mass as Fisher information]] and [[Belief inertia]] in its [[Hamiltonian belief dynamics]].
- **Precision and hierarchy.** The precision-as-dopamine story underpins the project's use of [[Precision weighting]] and informs hierarchical constructions such as [[Meta-agents and hierarchical emergence]].

In short, the project cites this work as the definitive operationalization of active inference — the equations and the neuronal-process reading — which it then re-expresses in the language of gauge theory, information geometry, and multi-agent dynamics.

> [!note] Editorial: claims here are restricted to what the paper itself establishes (free-energy and expected-free-energy updates, the precision/dopamine mapping, the discrete-MDP process theory). The gauge-theoretic and multi-agent connections are the present project's contributions, not claims of the cited paper.

## BibTeX

```bibtex
@article{friston2017active,
  title   = {Active Inference: A Process Theory},
  author  = {Friston, Karl J. and FitzGerald, Thomas and Rigoli, Francesco and Schwartenbeck, Philipp and Pezzulo, Giovanni},
  journal = {Neural Computation},
  volume  = {29},
  number  = {1},
  pages   = {1--49},
  year    = {2017},
  doi     = {10.1162/NECO_a_00912},
  publisher = {MIT Press}
}
```
