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
updated: 2026-09-27
---

# Memory-Augmented Networks

Memory-augmented neural networks couple a controller (typically an RNN) to an external, addressable memory store that can be read from and written to via differentiable attention, decoupling computation from a fixed-size hidden state. Canonical instances include Neural Turing Machines, End-To-End Memory Networks, and pointer/cache mechanisms; the read operation is a soft attention over memory slots, making these models a direct architectural ancestor of attention-based copying and retrieval. In the VFE program they are relevant as precursors to content-addressable, attention-driven information routing.

Persistent memory can also replace the transformer feed-forward layer outright: [[sukhbaatar-2019-persistent-memory]] appends learned key/value vectors to self-attention and removes the feed-forward sublayer at parity. [[Template routing]] (2026-09-27) is the Gaussian, KL-routed analog for the vfe3 block MLP, with a separate normalization after attention rather than a joint softmax.

## Related
[[Template routing]], [[Attention mechanisms — theory and positional structure]]

## Sources
[[grave2017improving]], [[merity2017-pointer-sentinel]], [[sukhbaatar-2019-persistent-memory]], [[dennis-2026-template-routing]]
