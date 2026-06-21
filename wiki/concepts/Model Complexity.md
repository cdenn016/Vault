---
type: concept
title: "Model Complexity"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Model Complexity

Model complexity quantifies how much structure a model commits to in explaining data — operationalized variously as the number of effective parameters, the description length (MDL), or the mutual information the model captures versus the predictive information it actually extracts. In the predictability/complexity framing of [[bialek2001predictability|bialek-2001-predictability-complexity]], the predictive information (sub-extensive part of the entropy of a time series) is the unique measure of the complexity of the underlying process. In variational inference the complexity term is the KL divergence between approximate posterior and prior, the penalty that trades off against accuracy in the free-energy objective.

## Related
[[Information bottleneck]], [[Variational free energy]], [[Meta-entropy]]

## Sources
[[bialek2001predictability|bialek-2001-predictability-complexity]], [[tishby-1999-information-bottleneck]]
