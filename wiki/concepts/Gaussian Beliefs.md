---
type: concept
title: "Gaussian Beliefs"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/multi-agent
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Gaussian Beliefs

A Gaussian belief is a variational posterior q(c)=N(mu,Sigma) parameterized by a mean vector and a covariance (often SPD) matrix. Gaussian beliefs are the workhorse representation in the gauge-theoretic VFE program: each agent/token carries (mu,Sigma), inter-agent transport acts on the covariance via congruence, and natural-gradient updates follow the Fisher metric of the Gaussian family. Closed-form KL divergences between Gaussians make the entropy-regularized KL-consensus coupling tractable, and the covariance's SPD geometry links beliefs to Riemannian/information-geometric structure.

## Related
[[Variational free energy]], [[SPD-manifold geometry and Riemannian optimization]], [[Information geometry and natural gradient]], [[Mass as Fisher information]]

## Sources
[[chechik2005information-bottleneck-gaussian]], [[petersen2012matrix]], [[chung-2015-vrnn]], [[fraccaro2016sequential]]
