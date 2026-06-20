---
type: paper
title: "Riemannian Metrics for Neural Networks I: Feedforward Networks"
aliases:
  - "Ollivier 2015 — Riemannian Metrics for Neural Networks"
authors:
  - Yann Ollivier
year: 2015
arxiv: "1303.0818"
url: https://arxiv.org/abs/1303.0818
tags:
  - cluster/info-geometry
  - project/transformer
  - field/cs-ml
  - field/mathematics
  - field/statistics
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Riemannian Metrics for Neural Networks I: Feedforward Networks

> [!info] Citation
> Yann Ollivier (2015). *Riemannian Metrics for Neural Networks I: Feedforward Networks*. arXiv:1303.0818. <https://arxiv.org/abs/1303.0818>

## TL;DR

Ollivier reformulates feedforward network training as Riemannian gradient descent on the manifold of network outputs, where distance is measured by the [[Fisher information metric]] rather than by the arbitrary Euclidean metric of the raw parameters. The central principle is *invariance*: a good training algorithm should produce the same learning trajectory regardless of how the network is parameterized or how the data are coordinatized. From this requirement he derives a family of four practical metrics — the natural metric (full [[Natural gradient]]), a *backpropagated metric*, a *unitwise* (per-neuron) natural gradient, and *quasi-diagonal* reductions — that trade exactness for scalability while preserving as much invariance as possible.

## Problem & setting

Ordinary stochastic gradient descent depends on the chosen parameterization: rescaling a weight, changing a unit's activation convention, or reparameterizing the inputs changes the gradient direction and therefore the optimization path. This is geometrically unnatural, because none of those changes alter the function the network computes. Ollivier treats a feedforward network as defining a probability distribution over outputs given inputs, so that the parameter space inherits the [[Fisher information metric]] — the unique (up to scale) metric invariant under reparameterization. Steepest descent in this metric is the [[Natural gradient]], which is by construction independent of the representation of both parameters and data. The difficulty is purely computational: the full Fisher matrix is the size of the parameter count squared and is infeasible for large networks, so the paper's real contribution is a hierarchy of structured approximations that keep the invariance guarantees that matter while remaining cheap.

## Method

The paper builds the metric layer by layer. A **backpropagated metric** propagates an output-space Riemannian metric backward through the network, analogously to how error signals are backpropagated, yielding a per-layer notion of distance. A **unitwise natural gradient** treats the incoming weights of each neuron as a small block and inverts only the local Fisher block for that neuron, giving a block-diagonal preconditioner indexed by units. **Quasi-diagonal** approximations further reduce each block to a diagonal plus a correction for the bias term, collapsing cost to nearly that of plain SGD while retaining exact invariance under affine changes of each unit's incoming activations. The four resulting algorithms span a spectrum from the full Fisher natural gradient down to near-diagonal preconditioners, each labeled by the precise class of transformations under which it remains invariant. All are derived from the same differential-geometric template: choose a metric on outputs, pull it back to parameters, and descend.

## Key results

- The full natural gradient is invariant under arbitrary smooth reparameterization, but the practical contribution is showing that *partial* invariance can be retained cheaply: the quasi-diagonal methods are invariant under affine reparameterization of each neuron's activations at near-SGD cost.
- The backpropagated and unitwise metrics give block-structured preconditioners whose blocks correspond to network units, prefiguring later block-diagonal curvature methods such as [[martens-2015-kfac|K-FAC]].
- Empirically and theoretically, the invariant methods remove the sensitivity of training to weight scaling and activation conventions that plagues raw gradient descent.

## Relevance to this research

This paper is the information-geometric articulation of the invariance principle that the VFE-transformer is built around, and the connection is unusually direct. The model's [[Gauge transformation|gauge invariance]] under the block general-linear group is, at the level of optimization, exactly Ollivier's demand that learning be independent of the chosen representation of internal activations: a block-`GL(k)` change of frame is a structured affine reparameterization of a unit block, precisely the transformation class under which his unitwise and quasi-diagonal metrics are invariant. Where the model uses Killing-form per-block preconditioning and a [[Natural gradient]] on Lie-algebra coordinates, Ollivier supplies the prototype — block-structured Fisher preconditioning indexed by units, derived from the [[Fisher information metric]] — and the justification for why such preconditioning is not an arbitrary trick but the unique geometrically invariant choice. His backpropagated metric, which transports a Riemannian metric backward through the layers, is a discrete antecedent of [[Parallel transport|parallel transport]] of the SPD covariance metric used in the model's filtering updates. Finally, because the metric is defined through the network's output distribution, the framework dovetails with the model's variational/ELBO objective: natural-gradient descent on a likelihood is the same operation that a [[Variational free energy|free-energy]] M-step performs on the generative parameters. For practical purposes this note is the bridge between the abstract [[amari-1998-natural-gradient|natural-gradient theory]] and the engineering question of how to precondition a deep, block-structured, gauge-equivariant network at scale.

> [!note] Editorial: The mapping from "block-`GL(k)` gauge frame" to Ollivier's "affine reparameterization of a unit's incoming activations" is an interpretive bridge for this project; Ollivier himself frames invariance in terms of generic activation reparameterization, not gauge groups.

## Cross-links

- [[Fisher information metric]]
- [[Natural gradient]]
- [[amari-1998-natural-gradient]]
- [[amari-2000-methods-information-geometry]]
- [[martens-2020-natural-gradient-insights]]
- [[martens-2015-kfac]]
- [[Information geometry and natural gradient]]
- [[Gauge transformation]]
- [[Parallel transport]]
- [[Variational free energy]]

## BibTeX

```bibtex
@article{ollivier2015riemannian,
  title   = {Riemannian Metrics for Neural Networks {I}: Feedforward Networks},
  author  = {Ollivier, Yann},
  journal = {arXiv preprint arXiv:1303.0818},
  year    = {2015},
  eprint  = {1303.0818},
  archivePrefix = {arXiv},
  primaryClass  = {cs.NE},
  url     = {https://arxiv.org/abs/1303.0818}
}
```
