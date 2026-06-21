---
type: concept
title: "Hierarchical generative model"
aliases:
  - "hierarchicalgenerativemodel"
  - "Hierarchical Latent Variable Models"
  - "Hierarchical latent variable models"
  - "Hierarchical latent variables"
tags:
  - cluster/vfe
  - cluster/attention
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Hierarchical generative model

A generative model with multiple layers of latent variables, where each level generates predictions for the level below and higher levels encode increasingly abstract/slowly-varying causes. Inverting such a model by minimizing variational free energy yields hierarchical predictive coding: top-down predictions and bottom-up prediction errors propagate across levels. It is the standard substrate for active inference and predictive-coding accounts of cortical processing, and motivates the layered, precision-weighted structure of the VFE transformer.

On the deep-generative side, inference and learning typically proceed by a *layered variational posterior* — an inference network mirroring the generative hierarchy — as in ladder / hierarchical VAEs, where bottom-up data evidence is combined with top-down priors at each level ([[sonderby-2016-ladder-vae]]). This is the deep-generative analogue of the program's hierarchical belief structure and a natural setting for stacked precision-weighted updates.

## Related
[[Predictive coding network]], [[Variational free energy]], [[Multi-agent variational free energy]], [[Variational autoencoder (VAE)]]

## Sources
[[clark-2013-predictive-brains]], [[friston-2010-free-energy-principle]], [[sonderby-2016-ladder-vae]]
