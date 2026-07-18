---
type: concept
title: "Belief Propagation"
aliases:
  - "Sum-product algorithm"
tags:
  - cluster/vfe
  - cluster/multi-agent
  - project/multi-agent
  - project/transformer
status: draft
created: 2026-06-21
updated: 2026-07-17
---

# Belief Propagation

Belief propagation is a message-passing algorithm for marginal inference on factor graphs. Variable
and factor nodes exchange sum-product messages that summarize local evidence. The algorithm is exact
on trees, while loopy belief propagation is an approximation whose fixed points, convergence, and
accuracy need separate analysis.

The variational formulation in [[yedidia-freeman-weiss-2005-region-free-energy]] identifies ordinary
belief-propagation fixed points with stationary points of the Bethe free energy and extends the idea
to generalized belief propagation on region graphs. Region beliefs retain selected joint marginals,
and counting numbers correct repeated energy and entropy contributions across overlapping regions.
This supplies one route beyond [[Mean-Field Approximation]], but local consistency of region beliefs
does not generally imply that they are marginals of one normalized global distribution. Tree or
junction-tree exactness therefore must not be transferred to a generic loopy region graph.

For the gauge-VFE program, region messages are a candidate inference mechanism for correlated local
blocks of the state posterior. They are distinct from attention weights computed from pairwise
belief discrepancies and from the configuration-level Gibbs law in [[Meta-entropy]]. The extension in
[[participatory-it-from-bit]] preserves those distinctions: a sparse normalized correlated posterior
retains conventional ELBO semantics, while a region approximation trades global normalization for
local tractability.

## Related
[[Free-energy principle active inference]], [[Variational free energy]], [[Bayesian Inference|Belief Updating]], [[Attention mechanisms — theory and positional structure]], [[Mean-Field Approximation]]

## Sources
[[yedidia-freeman-weiss-2005-region-free-energy]], [[friston2017graphical]], [[friston-2017-active-inference-process-theory]], [[friston2008hierarchical]], [[foerster-2016-dial]]
