---
type: concept
title: "Recognition Density"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Recognition Density

In variational inference and the free energy principle, the recognition density q(x | data) is the approximate posterior an agent maintains over hidden causes, optimized to minimize variational free energy and thereby approximate the true (generally intractable) Bayesian posterior. It is the variational counterpart to the generative model's likelihood/prior, and free-energy minimization can be read as making the recognition density track the posterior (the basis of predictive coding and active inference). In amortized settings a recognition network outputs the parameters of q directly; in the VFE transformer the per-token beliefs (mu, Sigma) play exactly this recognition-density role.

## Related
[[Variational Free Energy]], [[Amortized inference]], [[Active Inference]], [[Free-energy principle active inference|Free Energy Principle]]

## Sources
[[ramstead-2019-enactive-inference]]
