---
type: concept
title: "Belief Compression"
aliases:
  - "beliefcompression"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Belief Compression

The view that maintaining a belief is an act of lossy compression: an agent retains only the (sufficient) statistics of its observations that are predictive of relevant variables, discarding the rest, exactly as in the (deterministic) Information Bottleneck. A belief's mean and covariance are then a compressed code whose rate is traded against predictive fidelity, linking variational free energy, MDL, and the IB Lagrangian. In the program, precision-weighted updates implement how much new evidence is worth encoding into the compressed belief.

## Related
[[Information bottleneck]], [[strouse-2017-deterministic-ib|Deterministic information bottleneck]], [[MDL and BIC model selection]], [[Variational free energy]]

## Sources
[[strouse-2017-deterministic-ib]], [[tishby-1999-information-bottleneck|tishby-2000-information-bottleneck]]
