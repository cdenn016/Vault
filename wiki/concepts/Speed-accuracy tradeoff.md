---
type: concept
title: "Speed-accuracy tradeoff"
aliases:
  - "speed-accuracy trade-off"
tags:
  - cluster/vfe
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Speed-accuracy tradeoff

The speed-accuracy tradeoff (SAT) is the inverse relationship between decision speed and decision accuracy in sequential-sampling models of choice: lowering the decision threshold (boundary separation) yields faster but more error-prone responses, while raising it yields slower, more accurate ones. In drift-diffusion / accumulator models the threshold is a free parameter the decision-maker can set to trade reaction time against error rate, making SAT a behavioral signature of evidence accumulation. It connects to the program's view of inference under precision-weighted evidence and bounded computation.

## Related
[[Belief inertia]]

## Sources
[[ratcliff-2008-diffusion-decision]], [[bogacz-2006-physics-optimal-decision]], [[gold-2001-neural-basis-decision]]
