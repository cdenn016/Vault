---
type: concept
title: "Bayesian Belief Updating"
tags:
  - cluster/vfe
  - project/multi-agent
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Bayesian Belief Updating

Bayesian belief updating is the normative revision of a posterior belief over a latent state in light of new observations, combining a prior with a likelihood via Bayes' rule. In dynamic/non-stationary environments the effective learning rate is modulated by surprise (change-point probability) and by uncertainty (relative uncertainty), so that the agent weights new data more heavily after suspected changes or when its current estimate is imprecise. In the VFE framework this maps onto minimizing variational free energy, where the self-coupling KL term plays the role of prediction error and belief variance encodes uncertainty.

## Related
[[Variational Free Energy]], [[Change-Point Detection]], [[Relative Uncertainty]], [[Belief inertia]]

## Sources
[[mcguire2014-adaptive-learning]], [[nassar2010-approximately-bayesian]]
