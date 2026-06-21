---
type: concept
title: "Hierarchical Latent Variable Models"
aliases:
  - "hierarchicallatentvariablemodels"
  - "Hierarchical latent variables"
tags:
  - cluster/vfe
  - project/transformer
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Hierarchical Latent Variable Models

Generative models that stack multiple layers of latent variables so that higher layers capture increasingly abstract, slowly-varying factors and lower layers capture fine detail. Inference and learning typically proceed by a layered variational posterior (an inference network mirroring the generative hierarchy), as in ladder/hierarchical VAEs, where bottom-up data evidence is combined with top-down priors at each level. They are the deep-generative analogue of the program's hierarchical belief structure and a natural setting for stacked precision-weighted updates.

## Related
[[Variational free energy]], [[Variational autoencoder]], [[Predictive coding network]]

## Sources
[[sonderby-2016-ladder-vae]]
