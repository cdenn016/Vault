---
type: concept
title: "GL(K) gauge group"
aliases:
  - "glkgaugegroup"
  - "GL(K) group"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# GL(K) gauge group

The general linear group GL(K) of invertible K×K real matrices is the structure (gauge) group of the GL(K)-attention manuscript: each token carries a feature frame that is acted on by GL(K) change-of-basis transformations, and attention is required to transform covariantly (equivariantly) under this group. Gauging GL(K) introduces a connection whose holonomy encodes how frames are parallel-transported between tokens, generalizing fixed positional structure to a learned, geometry-aware transport. The relevant homogeneous space is the symmetric space GL(K)/O(K), which is isomorphic to the SPD cone, linking the gauge group to the covariance/precision geometry of the program.

## Related
[[Gauge transformation]], [[Group equivariance]], [[Symmetric spaces and the SPD cone]], [[Holonomy]], [[Parallel transport]], [[Irreducible representation]]

## Sources
[[hewitt-2019-structural-probe]]
