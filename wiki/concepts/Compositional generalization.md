---
type: concept
title: "Compositional generalization"
aliases:
  - "Compositionality"
  - "Systematic generalization"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Compositional generalization

Compositional generalization is the ability of a learner to systematically recombine known primitives into novel combinations — understanding 'jump twice' from having seen 'jump' and 'walk twice'. It is the systematicity property that classical symbolic systems get for free but that standard sequence models notoriously lack: Lake & Baroni's SCAN benchmark showed seq2seq RNNs with attention fail catastrophically on held-out compositions despite near-perfect in-distribution accuracy. It is a central probe of whether a learned representation is genuinely structured/relational rather than memorized.

## Related
[[Attention mechanisms — theory and positional structure]], [[Neural scaling laws]]

## Sources
[[lake2018-generalization-scan]]
