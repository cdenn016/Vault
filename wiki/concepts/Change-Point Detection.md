---
type: concept
title: "Change-Point Detection"
tags:
  - cluster/vfe
  - cluster/social-physics/opinion-dynamics
  - project/multi-agent
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Change-Point Detection

Change-point detection infers when the generative statistics of a sequence have abruptly shifted. In adaptive-learning models, the change-point probability (CPP) Omega_t is computed from the likelihood ratio of the latest observation under a 'stable' versus a 'change' hypothesis given a fixed hazard rate, and it drives a surprise-proportional boost to the learning rate. In the approximately-Bayesian delta rule alpha_t = Omega_t + (1 - Omega_t) tau_t, CPP is the surprise component that resets beliefs after a regime change. It corresponds to the prediction-error / KL-divergence term that elevates belief updating in the VFE model.

## Related
[[Bayesian Inference|Bayesian Belief Updating]], [[Relative Uncertainty]], [[Variational Free Energy]], [[Belief inertia]]

## Sources
[[mcguire2014-adaptive-learning]], [[nassar2010-bayesian-delta-rule|nassar2010-approximately-bayesian]]
