---
type: paper
title: Predictive Coding Approximates Backprop along Arbitrary Computation Graphs
aliases:
  - "Millidge 2020 — PC Approximates Backprop"
authors:
  - Beren Millidge
  - Alexander Tschantz
  - Christopher L. Buckley
year: 2020
arxiv: "2006.04182"
url: https://arxiv.org/abs/2006.04182
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
  - field/cs-ml
  - field/neuroscience
status: draft
created: 2026-06-18
updated: 2026-06-18
---

# Predictive Coding Approximates Backprop along Arbitrary Computation Graphs

> [!info] Citation
> Beren Millidge, Alexander Tschantz, and Christopher L. Buckley (2020). *Predictive Coding Approximates Backprop along Arbitrary Computation Graphs*. arXiv:2006.04182. [arxiv.org/abs/2006.04182](https://arxiv.org/abs/2006.04182)

## TL;DR

The paper proves that **predictive coding** — a free-energy-minimizing inference scheme using only *local* message passing — converges asymptotically, and in practice rapidly, to the *exact* gradients computed by backpropagation, and that this holds not only for multilayer perceptrons but for **arbitrary computation graphs** (CNNs, RNNs, LSTMs, branching and multiplicative structures). The consequence is that a network trained by minimizing a layerwise [[Variational free energy]] using local prediction-error dynamics can reproduce end-to-end backprop training without ever forming a non-local global gradient.

## Problem & setting

Backpropagation is biologically and architecturally non-local: each weight update depends on a global error signal transported backward through the entire graph. Predictive coding, by contrast, attaches to each node (layer) a belief and a local **prediction-error** unit; inference proceeds by exchanging messages only between adjacent nodes until the errors settle. Prior work (e.g. Whittington & Bogacz) had shown the two coincide for simple feedforward MLPs. The open question this paper settles is whether the equivalence is *general*: does free-energy minimization by local prediction-error dynamics recover exact backprop gradients on the kind of heterogeneous computation graph a real deep model actually is?

## Method

Each edge of a computation graph carries a generative prediction of its target node from its source node; the discrepancy is a [[Prediction error]] weighted by a precision. The network runs an inference (E-step-like) relaxation that updates node activities by gradient descent on the total [[Variational free energy]] until the prediction errors reach a fixed point. At that fixed point the local error signals at each node are shown to equal the backprop gradients (the Jacobian-vector products) that would have been transported to that node, so the subsequent weight update (an M-step-like move) matches the backprop update. The authors give explicit "translation" recipes that turn standard layers — convolutions, recurrent cells, multiplicative gates — into predictive-coding graphs, so the result is not confined to a toy architecture.

> [!note] Editorial: The relaxation-to-fixed-point/then-update structure is exactly a [[Variational EM]] alternation — an inner inference sweep over beliefs followed by an outer parameter step — which is why this result transfers cleanly to the VFE-transformer's E-step/M-step training loop rather than only to classical PC networks.

## Key results

- **Exact equivalence at convergence.** Predictive coding's local updates converge to the exact backprop gradient on any computation graph; equivalence is asymptotic but empirically reached in a few inference iterations.
- **Generality.** Demonstrated for CNNs, RNNs, and LSTMs, including branching topologies and multiplicative interactions — the structural ingredients of modern deep nets.
- **Locality.** All learning uses local, largely Hebbian plasticity (each update depends only on a node's own activity and its adjacent prediction errors), with no global backward pass.
- **Parity.** Performance matches backprop-trained baselines on the tested benchmarks.

## Relevance to this research

The VFE-transformer trains by minimizing an ELBO/free-energy objective with an explicit E-step (update per-token Gaussian beliefs $(\mu,\Sigma)$) and M-step (update parameters), under a `gradient_mode: filtering`. This paper supplies the load-bearing guarantee that such a **local, prediction-error-driven inference loop is not a biologically-flavored approximation that sacrifices gradient quality** — at its fixed point it *is* exact backprop. Concretely:

- It justifies treating the model's [[Variational EM]] inner loop and its end-to-end gradient training as the *same* optimization, so the [[Evidence lower bound (ELBO)]] descent and the parameter gradients are mutually consistent rather than two competing objectives.
- It extends the equivalence to **arbitrary computation graphs**, which matters because a transformer with attention, residual branches, and gating is exactly the heterogeneous-graph regime the paper covers — not the MLP special case of earlier proofs.
- The precision-weighted prediction-error machinery it formalizes is the same structure the architecture reuses for `precision_weighted_attention`, tying [[Precision weighting]] in inference to precision in attention.

It connects naturally to [[rao-1999-predictive-coding]] (the origin of predictive coding), [[bogacz-2017-free-energy-tutorial]] (the free-energy/PC update derivations), [[neal-1998-variational-em]] (the EM framing), and [[friston-2010-free-energy-principle]] (the broader free-energy account).

## Cross-links

- Concepts: [[Variational free energy]], [[Evidence lower bound (ELBO)]], [[Prediction error]], [[Precision weighting]]
- Methods: [[Variational EM]], [[Predictive coding network]], [[Free-energy principle active inference]]
- Related sources: [[rao-1999-predictive-coding]], [[bogacz-2017-free-energy-tutorial]], [[neal-1998-variational-em]], [[friston-2010-free-energy-principle]]
- Theme: [[Variational free energy and predictive coding]]
- Project: [[VFE Transformer Program]]

```bibtex
@article{millidge2020pcbackprop,
  title        = {Predictive Coding Approximates Backprop along Arbitrary Computation Graphs},
  author       = {Millidge, Beren and Tschantz, Alexander and Buckley, Christopher L.},
  journal      = {arXiv preprint arXiv:2006.04182},
  year         = {2020},
  eprint       = {2006.04182},
  archivePrefix = {arXiv},
  primaryClass = {cs.NE},
  url          = {https://arxiv.org/abs/2006.04182}
}
```
