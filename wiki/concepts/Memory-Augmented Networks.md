---
type: concept
title: "Memory-Augmented Networks"
aliases:
  - "Memory Augmented Networks"
tags:
  - cluster/attention
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Memory-Augmented Networks

Memory-augmented neural networks couple a controller (typically an RNN) to an external, addressable memory store that can be read from and written to via differentiable attention, decoupling computation from a fixed-size hidden state. Canonical instances include Neural Turing Machines, End-To-End Memory Networks, and pointer/cache mechanisms; the read operation is a soft attention over memory slots, making these models a direct architectural ancestor of attention-based copying and retrieval. In the VFE program they are relevant as precursors to content-addressable, attention-driven information routing.

## Related
[[Attention mechanisms — theory and positional structure]]

## Sources
[[grave2017improving]], [[merity2017-pointer-sentinel]]
