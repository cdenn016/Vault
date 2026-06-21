---
type: concept
title: "Hierarchical generative model"
aliases:
  - "hierarchicalgenerativemodel"
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

## Related
[[Predictive coding network]], [[Variational free energy]], [[Multi-agent variational free energy]]

## Sources
[[clark-2013-predictive-brains]], [[friston-2010-free-energy-principle]]
