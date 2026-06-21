---
type: concept
title: "State space models"
aliases:
  - "State space model"
  - "SSM"
tags:
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# State space models

A state space model describes a sequence by a latent (hidden) state evolving through a Markov transition together with an observation/emission mapping from state to data. Classical instances include the linear-Gaussian Kalman filter and hidden Markov models; deep/nonlinear variants (deep Kalman filters, deep state space models, structured inference networks) parameterize the transition and emission with neural networks and fit them by amortized variational inference. They give a principled latent-dynamics prior for sequential data and underpin sequential variational autoencoders.

## Related
[[Variational free energy]], [[Amortized inference]], [[Kalman filter]]

## Sources
[[krishnan2017structured]], [[fraccaro2016sequential]]
