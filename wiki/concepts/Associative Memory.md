---
type: concept
title: "Associative Memory"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-10-28
---

# Associative Memory

An associative (content-addressable) memory stores a set of patterns and retrieves the closest stored pattern from a partial or noisy cue, classically realized by Hopfield networks whose dynamics descend an energy landscape to a stored attractor. Modern continuous-state Hopfield networks store exponentially many patterns and retrieve in a single step; crucially, their update rule is mathematically equivalent to transformer scaled dot-product attention, giving an associative-memory reading of attention. In the VFE program this frames the belief-coupling term sum_ij beta_ij KL(q_i || Omega_ij q_j) as soft retrieval from stored key patterns, and grounds the PriorBank KL-to-prior decode as querying an external memory of prototypes.

[[Template routing]] (2026-09-27) applies the associative-memory reading to the vfe3 block MLP: token beliefs retrieve from a bank of learned Gaussian templates with responsibilities $\propto\pi_a e^{-\mathrm{KL}(q_i\|p_a)}$. With values tied to template means the update is a natural-gradient descent that reduces to modern-Hopfield retrieval; with untied values the block reads out what each template predicts, the key-value memory reading of feed-forward layers in [[geva-2021-ffn-key-value-memories]].

[[hoover-2023-energy-transformer]] (NeurIPS 2023) makes a whole transformer block an associative memory: attention is a log-sum-exp energy whose keys evolve with the queries (unlike a modern Hopfield network, whose keys are fixed memories), and the MLP is a Hopfield module over learned memories with tied weights, run in parallel with attention. With a softmax activation that module is retrieval against a learned bank, the role [[Template routing]] plays with Gaussian templates.

Two further readings bear on the template bank (2026-10-24). In the generative-gating mixture of experts of [[xu-1995-alternative-mixtures-of-experts]] the gate weight is the posterior probability of the component given the input, which is the `gaussian_template` routing rule with constant values. In [[schlag-2021-fast-weight-programmers]] linear attention is a fast weight memory written by additive key-value outer products and corrected by a delta rule; a template bank refit in context from the causal prefix would keep a memory of the same kind, with responsibilities as write weights.

The [[Cue-result generative memory]] (2026-10-28, [[dennis-2026-cue-result-memory]]) retrieves a different variable from the one used to address the memory: the cue law addresses a component by expected-likelihood overlap with the token's belief, and the component's affine result law supplies what is written back, so retrieval can rotate or reverse a direction, which same-state retrieval cannot.

## Related
[[Template routing]], [[Attention Mechanism]], [[Energy-Based Models]], [[Variational Free Energy]]

## Sources
[[ramsauer2021hopfield]], [[krotov-2016-dense-associative-memory|krotov2016dense]], [[geva-2021-ffn-key-value-memories]], [[dennis-2026-template-routing]], [[hoover-2023-energy-transformer]], [[xu-1995-alternative-mixtures-of-experts]], [[schlag-2021-fast-weight-programmers]]
