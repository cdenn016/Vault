---
type: concept
title: "Bayesian Inference"
aliases:
  - "Bayesian Belief Updating"
  - "Bayesian belief updating"
  - "Bayesian reasoning"
  - "Belief Updating"
  - "Belief updating"
tags:
  - cluster/vfe
  - cluster/info-geometry
  - cluster/social-physics/opinion-dynamics
  - project/transformer
  - project/multi-agent
  - project/social-physics
status: stub
created: 2026-06-21
updated: 2026-06-21
---

# Bayesian Inference

Bayesian inference updates a prior belief p(c) over latent causes into a posterior p(c|x) proportional to the likelihood times the prior, given observed data x. Exact posteriors are usually intractable, so the program relies on variational approximations (minimizing free energy / maximizing the ELBO) and, in social settings, on bounded or biased approximations of Bayes. It is the conceptual backbone connecting predictive coding, active inference, and the gauge-theoretic VFE model, where agents carry (Gaussian) beliefs updated toward Bayesian posteriors via natural-gradient descent.

In the Bayesian/variational view, belief updating is a precision-weighted move from prior to posterior, with the effective learning rate set by the relative precision of prior versus likelihood; delta-rule and Kalman-style updates are special cases. In dynamic/non-stationary environments that rate is further modulated by surprise (change-point probability) and by relative uncertainty, so an agent weights new data more heavily after suspected changes or when its current estimate is imprecise ([[mcguire2014-adaptive-learning]], [[nassar2010-approximately-bayesian]]). Instantaneous Bayesian conditioning also serves as the rational benchmark against which empirical departures — confirmation bias, belief perseverance, motivated reasoning — are measured: a Bayesian reasoner weighs confirming and disconfirming evidence symmetrically, whereas human reasoners systematically deviate. The program's belief-inertia and active-inference dynamics relax this idealized update rule, recovering momentum and bias as deviations from instantaneous Bayesian updating ([[Belief inertia]], [[Mass as Fisher information]]).

## Related
[[Variational free energy]], [[Free-energy principle active inference]], [[Gaussian Beliefs]], [[Bayesian mechanics]], [[Information geometry and natural gradient]], [[Belief inertia]], [[Belief perseverance and confirmation bias]]

## Sources
[[caves-2002-quantum-bayesian]], [[salvatier2016probabilistic]], [[pilgrim-2023-confirmation]], [[anderson1980perseverance]], [[mcguire2014-adaptive-learning]], [[nassar2010-approximately-bayesian]], [[nickerson-1998-confirmation-bias]], [[bissiri-2016-general-bayesian-updating]]
