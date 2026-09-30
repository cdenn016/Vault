---
type: concept
title: "Gaussian State Space Model"
aliases:
  - "Gaussian state-space model"
  - "Linear-Gaussian state space model"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-09-30
---

# Gaussian State Space Model

## Correlated-noise inherited parent reference

[[multiagentelbo-2026-09-30-gaussian-parent-dynamics]] specializes exact Gaussian filtering to a retained/hidden partition of a pointwise network under deterministic observed controls. The forecast includes retained/hidden process-noise cross covariance, and initialization uses the actual joint preparation rather than a stationary conditional. General-SPD-mobility OU kernels carry passive GL frame changes consistently.

Seven tiny independent tests and one five-case 512-agent CPU reference support the declared implementation. Full-history innovations and direct Gaussian path KL agree numerically with the information loss of optimal one-step Markov rows. Correct pair marginals therefore remain distinct from history closure. The full hidden conditional is network-sized, externally controlled link motion is not endogenous learning, and no autonomous compressed parent is established. [[Coarse Graining]] records those boundaries.

A Gaussian state space model is a latent-variable time series model with Gaussian (typically linear-Gaussian) transition and emission densities, so that the latent state evolves as a Markov chain with Gaussian noise. The linear case admits exact Kalman-filter/smoother inference; nonlinear or deep-parameterized variants (deep Kalman / deep state space models) use amortized variational inference. It is the structured-prior backbone for sequential latent-variable VAEs.

## Related
[[Reparameterization trick]], [[Variational autoencoder (VAE)]], [[Variational free energy]]

## Sources
[[krishnan2017structured]], [[chung-2015-vrnn]]
