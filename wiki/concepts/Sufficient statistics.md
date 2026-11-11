---
type: concept
title: "Sufficient statistics"
aliases:
  - "sufficient statistic"
  - "sufficiency"
  - "Sufficient Statistic"
tags:
  - cluster/info-geometry
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-11-11
---

# Sufficient statistics

A statistic T(X) is sufficient for a parameter theta if the conditional distribution of the data given T carries no further information about theta, equivalently (Fisher-Neyman) if the likelihood factorizes as p(x|theta) = h(x) g(T(x), theta). Sufficiency is the invariance principle underpinning information geometry: Chentsov's theorem shows the Fisher metric and the Amari-Chentsov tensor are the unique geometric structures invariant under sufficient statistics, and exponential families are exactly the models admitting finite-dimensional sufficient statistics (their natural parameters/expectation parameters being the dually flat coordinates used throughout the VFE program).

## Insufficient summaries in filtering, November 11, 2026

In linear-Gaussian filtering the cost of a statistic that is not sufficient can be stated exactly. When an agent reads a linear summary of a finer record, [[dennis-2026-collective-agents-approximate-blanket-conditions]] splits the expected relative entropy from the exact predictive law given the finer record to any belief computed from a coarse record into the excess relative to the law given the coarse record plus the conditional mutual information between the predicted variable and the finer record given the coarse record. If the acts depend on the summary alone, the initial mean of the predicted process is deterministic and the initial mean of the belief is a function of the agent's randomization, that information equals half the log-determinant ratio of the predictive covariances of the exact filters of the summary and of the finer record, and no model declared by the agent changes it. If the acts depend on the finer record, they carry part of the withheld information and, for a deterministic initial mean and a coarse record that contains the summary and the acts, the term is at most that value. For the information-form statistic of sensors that read the predicted variable alone, the corresponding gain residual of the summary vanishes. See [[Approximate meta-agent theorem]].

## Related
[[Fisher information metric]], [[Amari-Chentsov tensor]], [[Exponential family]], [[Information geometry and natural gradient]]

## Sources
[[ay2015-info-geometry-sufficient-statistics]]
