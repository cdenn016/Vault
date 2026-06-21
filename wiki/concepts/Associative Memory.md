---
type: concept
title: "Associative Memory"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Associative Memory

An associative (content-addressable) memory stores a set of patterns and retrieves the closest stored pattern from a partial or noisy cue, classically realized by Hopfield networks whose dynamics descend an energy landscape to a stored attractor. Modern continuous-state Hopfield networks store exponentially many patterns and retrieve in a single step; crucially, their update rule is mathematically equivalent to transformer scaled dot-product attention, giving an associative-memory reading of attention. In the VFE program this frames the belief-coupling term sum_ij beta_ij KL(q_i || Omega_ij q_j) as soft retrieval from stored key patterns, and grounds the PriorBank KL-to-prior decode as querying an external memory of prototypes.

## Related
[[Attention Mechanism]], [[Energy-Based Models]], [[Variational Free Energy]]

## Sources
[[ramsauer2021hopfield]], [[krotov2016dense]]
