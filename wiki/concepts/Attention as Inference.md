---
type: concept
title: "Attention as Inference"
tags:
  - cluster/attention
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Attention as Inference

The view that attention is not an ad hoc weighting but the computational signature of probabilistic inference: softmax attention implements a posterior over which keys are relevant to a query, equivalent to precision-weighted Bayesian cue combination in which more reliable (higher-precision) sources receive more weight. This reframes transformer attention as approximate inference and links it to predictive-coding / precision accounts of perception in the brain, the foundation of the VFE transformer's precision-weighted attention.

## Related
[[Precision weighting]], [[Attention mechanisms — theory and positional structure]], [[Variational free energy]], [[Predictive processing and controlled hallucination]]

## Sources
[[pouget-2013-probabilistic-brains]], [[Bissiri2016-generalized-bayes]]
