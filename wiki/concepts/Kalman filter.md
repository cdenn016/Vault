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

## A wrong observation model and a summarized record, November 11, 2026

The misspecification described above leaves the observation model correct. [[dennis-2026-collective-agents-approximate-blanket-conditions]] extends the bound to a stationary filter that reads a linear summary $s=\mathsf Tz$ of a finer record $z$ through a declared observation model $(\bar H,\bar R)$ that may be wrong, while the acts may depend on the finer record. The contraction of the declared filter in the metric of its own predictive covariance is unaffected, since it involves the declared matrices alone. The error of the mean acquires an innovation term, whose stationary energy the covariance equation gives exactly, and a drive from the parts of the closure defect and of the observation defect $(\mathsf TH_{\mathrm x}-\bar HC)x_t$ that the finer record resolves; the unresolved part of the observation defect acts as additional noise of the summary that is correlated with the prediction error. The resulting bound on the upper limit of the excess relative entropy holds whenever the fine process is detectable through the finer record, and it is of second order jointly in the defects, the noise mismatches and the gain residual of the summary.

Two features have no counterpart for a correctly read record. A summary that is not sufficient for the finer record contributes a term $\frac12\ln\det(P_{\mathrm e,t}^{-1}P_{\mathsf T,t})$, the log-determinant ratio of the predictive covariances of the exact filters of the summary and of the finer record, which no declared model changes when the acts read the summary alone and the initial means are deterministic, so no bound that vanishes with the model defects can hold. The argument also does not need the gain to come from a filter equation: a recursion with any fixed gain and an additive perturbation obeys a bound of the same kind once its closed-loop matrix contracts in the metric of the claimed covariance. Synthesis in [[Approximate meta-agent theorem]].

## Related
[[Variational free energy]], [[Predictive coding network]], [[Belief inertia]]

## Sources
[[nassar-2012-pupil-arousal-learning]], [[coibion2015-information-rigidity]]
