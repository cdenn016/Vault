---
type: concept
title: "Data processing inequality"
aliases:
  - "DPI"
tags:
  - cluster/info-geometry
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Data processing inequality

The data processing inequality (DPI) states that for any Markov chain X -> Y -> Z, the mutual information cannot increase under processing: I(X;Z) <= I(X;Y). No transformation of Y (deterministic or stochastic) can create information about X that was not already present. It is the formal backbone of the information-bottleneck view of deep learning, where each layer is a processing stage and the DPI bounds how much task-relevant information can survive successive representations. More generally it expresses the monotonicity (contraction) of f-divergences and Fisher information under stochastic maps, linking it to Cencov's characterization of the Fisher metric.

## Related
[[Quantum information geometry]], [[Fisher information metric]]

## Sources
[[tishby2015-deep-learning-ib]]
