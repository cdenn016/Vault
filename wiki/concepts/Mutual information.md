---
type: concept
title: "Mutual information"
aliases:
  - "I(X;Y)"
tags:
  - cluster/info-geometry
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Mutual information

Mutual information I(X;Y) = H(X) - H(X|Y) = D_KL(p(x,y) || p(x)p(y)) measures the reduction in uncertainty about one variable from observing another; it is symmetric, non-negative, and zero iff the variables are independent. Introduced by Shannon, it is the central currency of the information bottleneck (compressing X into T while preserving I(T;Y)) and of representation-learning objectives. In this program it underlies the IB account of attention and meta-agent membership and connects, in the local/quadratic limit, to the Fisher information metric.

## Related
[[Information bottleneck]], [[Fisher information metric]], [[Physics from Fisher information]]

## Sources
[[shannon-1948-mathematical-theory-communication]], [[slonim-2000-agglomerative-ib]], [[tishby2015-deep-learning-ib]], [[cover-thomas-2006-elements-information-theory]]
