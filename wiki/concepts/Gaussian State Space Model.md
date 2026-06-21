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
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Gaussian State Space Model

A Gaussian state space model is a latent-variable time series model with Gaussian (typically linear-Gaussian) transition and emission densities, so that the latent state evolves as a Markov chain with Gaussian noise. The linear case admits exact Kalman-filter/smoother inference; nonlinear or deep-parameterized variants (deep Kalman / deep state space models) use amortized variational inference. It is the structured-prior backbone for sequential latent-variable VAEs.

## Related
[[Reparameterization trick]], [[Variational autoencoder (VAE)]], [[Variational free energy]]

## Sources
[[krishnan2017structured]], [[chung-2015-vrnn]]
