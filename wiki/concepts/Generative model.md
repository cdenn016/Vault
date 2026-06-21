---
type: concept
title: "Generative model"
aliases:
  - "generativemodel"
tags:
  - cluster/vfe
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Generative model

A generative model specifies a joint distribution p(x, z) over observations x and latent causes z, encoding how hidden states produce data. Bayesian inference inverts it to obtain the posterior p(z|x), which is generally intractable and approximated variationally by minimizing free energy. Generative models are the backbone of predictive coding, active inference, and the VFE framework: agents are taken to embody a generative model of their sensory inputs and act/perceive so as to minimize prediction error (free energy).

## Related
[[Variational free energy]], [[Predictive coding]], [[Amortized inference]]

## Sources
[[hoffman-2015-interface-perception]]
