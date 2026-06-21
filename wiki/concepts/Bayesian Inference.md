---
type: concept
title: "Bayesian Inference"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
  - project/social-physics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Bayesian Inference

Bayesian inference updates a prior belief p(c) over latent causes into a posterior p(c|x) proportional to the likelihood times the prior, given observed data x. Exact posteriors are usually intractable, so the program relies on variational approximations (minimizing free energy / maximizing the ELBO) and, in social settings, on bounded or biased approximations of Bayes. It is the conceptual backbone connecting predictive coding, active inference, and the gauge-theoretic VFE model, where agents carry (Gaussian) beliefs updated toward Bayesian posteriors via natural-gradient descent.

## Related
[[Variational free energy]], [[Free-energy principle active inference]], [[Gaussian Beliefs]], [[Bayesian mechanics]], [[Information geometry and natural gradient]]

## Sources
[[caves-2002-quantum-bayesian]], [[salvatier2016probabilistic]], [[pilgrim-2023-confirmation]], [[anderson1980perseverance]]
