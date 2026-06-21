---
type: concept
title: "Sequential Sampling Models"
tags:
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Sequential Sampling Models

Sequential sampling models explain two-choice (and multi-choice) decisions as the gradual accumulation of noisy evidence over time until a decision threshold is crossed, jointly predicting choice probabilities and full reaction-time distributions. The canonical instance is the drift-diffusion / diffusion decision model, with relatives including the linear ballistic accumulator and race models; they account for positively skewed RT distributions and the speed-accuracy tradeoff via separable parameters (drift rate, boundary separation, starting point, nondecision time). In the VFE program these connect to belief-update dynamics: precision-weighted prediction error plays the role of drift, the confidence threshold the role of boundary, and networks of coupled accumulators model opinion dynamics under social influence.

## Related
[[Evidence Accumulation]], [[Reaction Time Distributions]], [[Speed-Accuracy Tradeoff]], [[Variational Free Energy]]

## Sources
[[ratcliff-2008-diffusion-decision]]
