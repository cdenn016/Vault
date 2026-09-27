---
type: concept
title: "Associative Memory"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-09-27
---

# Associative Memory

An associative (content-addressable) memory stores a set of patterns and retrieves the closest stored pattern from a partial or noisy cue, classically realized by Hopfield networks whose dynamics descend an energy landscape to a stored attractor. Modern continuous-state Hopfield networks store exponentially many patterns and retrieve in a single step; crucially, their update rule is mathematically equivalent to transformer scaled dot-product attention, giving an associative-memory reading of attention. In the VFE program this frames the belief-coupling term sum_ij beta_ij KL(q_i || Omega_ij q_j) as soft retrieval from stored key patterns, and grounds the PriorBank KL-to-prior decode as querying an external memory of prototypes.

[[Template routing]] (2026-09-27) applies the associative-memory reading to the vfe3 block MLP: token beliefs retrieve from a bank of learned Gaussian templates with responsibilities $\propto\pi_a e^{-\mathrm{KL}(q_i\|p_a)}$. With values tied to template means the update is a natural-gradient descent that reduces to modern-Hopfield retrieval; with untied values the block reads out what each template predicts, the key-value memory reading of feed-forward layers in [[geva-2021-ffn-key-value-memories]].

## Related
[[Template routing]], [[Attention Mechanism]], [[Energy-Based Models]], [[Variational Free Energy]]

## Sources
[[ramsauer2021hopfield]], [[krotov-2016-dense-associative-memory|krotov2016dense]], [[geva-2021-ffn-key-value-memories]], [[dennis-2026-template-routing]]
