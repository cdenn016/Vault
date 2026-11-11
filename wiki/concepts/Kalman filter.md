---
type: concept
title: "Kalman filter"
aliases:
  - "kalmanfilter"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - project/transformer
  - project/social-physics
status: stub
created: 2026-06-21
updated: 2026-11-11
---

# Kalman filter

The optimal recursive Bayesian estimator for a linear-Gaussian state-space model: it alternates a prediction step (propagating the mean and covariance through the dynamics) with an update step that combines the prior with a new observation using the Kalman gain, a precision-weighted blend of prediction and evidence. It is the canonical instance of precision-weighted belief updating that predictive coding and variational free energy generalize, and underlies expectation-formation models in macroeconomics (information rigidity) and learning-rate / pupil-arousal studies.

The fixed-interval smoother of [[rauch-1965-rts-smoother]] runs backward over the filter's stored moments, and with a probit readout and moment matching ([[minka-2001-expectation-propagation]]) the filter-smoother pair is the inference engine of the backprop-free learning test [[vfe3-2026-10-25-local-learner-test]]. Its switching generalization is [[barber-2006-expectation-correction]].

A filter run on a misspecified model has a computable cost. When the model is a Markov law for a coarse variable that is not closed, the difference between the exact and the declared predictive covariances obeys an exact quadratic equation, and the declared filter contracts in the metric of its own predictive covariance; together these bound the expected relative entropy from the exact predictive law to the filter's belief with no condition on the size of the misspecification ([[dennis-2026-collective-agents-approximate-meta-agent]]; synthesis in [[Approximate meta-agent theorem]]).

## Related
[[Variational free energy]], [[Predictive coding network]], [[Belief inertia]]

## Sources
[[nassar-2012-pupil-arousal-learning]], [[coibion2015-information-rigidity]]
