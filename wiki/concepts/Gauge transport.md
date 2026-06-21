---
type: concept
title: "Gauge transport"
aliases:
  - "gauge-covariant transport"
tags:
  - cluster/gauge-theory
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Gauge transport

Gauge transport is the program's term for moving belief/representation vectors between token frames using the connection of the gauge structure, so that comparisons (e.g. attention scores) are made in a common frame and remain covariant under local gauge transformations. It is the dynamical use of parallel transport along token positions, distinguished from a passive gauge transformation (relabeling the frame): transport carries data along a path, accumulating holonomy when the connection is non-flat. In gauge-theoretic attention, query-key comparisons implicitly transport one token's frame to another's before the inner product.

## Related
[[Parallel transport]], [[Gauge transformation]], [[Holonomy]], [[Parallel transport|connection]]

## Sources
[[su2024roformer]], [[voita-2019-attention-heads]]
